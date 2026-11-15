import json
import unittest
from datetime import date, datetime, timedelta
from unittest import mock

from futuros import ejecutor, riesgo
from futuros.riesgo import Operacion, evaluar

HOY = date(2026, 11, 13)
# Margen que reproduce la diapositiva: 18,9 % de 16.621,50 USD.
MARGENES = {"SP500": {"margen_inicial_usd": 3141.46, "fecha": "2026-11-12", "fuente": "prueba"}}


def mes(**k):
    base = dict(simbolo="SP500.DEC26", direccion="largo", contratos=1,
                entrada=7646.0, stop=7613.0, ultimo_dia="2026-12-18")
    return Operacion(**{**base, **k})


def ev(op, **k):
    with mock.patch.object(riesgo, "perdidas_de_hoy", return_value=k.pop("hoy_perdido", (0.0, 0))):
        return evaluar(op, hoy=HOY, margenes=k.pop("margenes", MARGENES))


class Riesgo(unittest.TestCase):
    def test_reproduce_la_diapositiva(self):
        v = ev(mes())
        self.assertEqual(v["veredicto"], "APTO")
        self.assertEqual(v["capital_usd"], 16621.50)
        self.assertAlmostEqual(v["margen_capital"], 0.189, places=3)
        self.assertEqual(v["apalancamiento"], 2.3)
        self.assertEqual(v["riesgo_usd"], 165.0)
        self.assertAlmostEqual(v["riesgo_capital"], 0.0099, places=4)
        self.assertEqual(v["limite_diario_usd"], 664.86)

    def test_como_maximo_un_mes(self):
        v = ev(mes(contratos=2))
        self.assertEqual(v["veredicto"], "NO APTO")
        self.assertTrue(any("Margen/capital" in m for m in v["motivos"]))

    def test_riesgo_entre_1_y_2_avisa_y_por_encima_rechaza(self):
        self.assertEqual(ev(mes(stop=7600.0))["veredicto"], "APTO CON AVISOS")   # 230 USD
        self.assertEqual(ev(mes(stop=7570.0))["veredicto"], "NO APTO")           # 380 USD

    def test_stop_en_lado_equivocado_o_fuera_de_tick(self):
        self.assertEqual(ev(mes(stop=7700.0))["veredicto"], "NO APTO")
        self.assertEqual(ev(mes(stop=7613.1))["veredicto"], "NO APTO")

    def test_margen_ausente_o_caducado(self):
        self.assertEqual(ev(mes(), margenes={"SP500": {"margen_inicial_usd": None, "fecha": None}})
                         ["veredicto"], "NO APTO")
        viejo = {"SP500": {**MARGENES["SP500"], "fecha": "2026-10-01"}}
        self.assertEqual(ev(mes(), margenes=viejo)["veredicto"], "NO APTO")

    def test_limite_diario_y_cuatro_stops(self):
        self.assertEqual(ev(mes(), hoy_perdido=(495.0, 3))["veredicto"], "APTO")
        self.assertEqual(ev(mes(), hoy_perdido=(520.0, 3))["veredicto"], "NO APTO")
        self.assertEqual(ev(mes(), hoy_perdido=(100.0, 4))["veredicto"], "NO APTO")

    def test_contrato_vencido(self):
        self.assertEqual(ev(mes(ultimo_dia="2026-11-01"))["veredicto"], "NO APTO")

    def test_cobertura_nunca_aumenta_la_exposicion(self):
        c = riesgo.contratos_cobertura(100000, 1.0, 7646.0, "SP500.DEC26")
        self.assertEqual(c["contratos"], 2)          # 2,6 -> 2, nunca 3
        self.assertLessEqual(c["cubierto"], 1.0)
        corto = dict(direccion="corto", stop=7679.0, tipo="cobertura", beta=1.0)
        self.assertEqual(ev(mes(**corto, cartera_usd=50000))["veredicto"], "APTO")
        self.assertEqual(ev(mes(**corto, cartera_usd=30000))["veredicto"], "NO APTO")
        self.assertEqual(ev(mes(tipo="cobertura", cartera_usd=50000))["veredicto"], "NO APTO")


class Ejecutor(unittest.TestCase):
    def setUp(self):
        import tempfile, pathlib
        d = pathlib.Path(tempfile.mkdtemp())
        for p in (mock.patch.object(ejecutor, "TICKETS", d / "tickets"),
                  mock.patch.object(ejecutor, "ENVIOS", d / "envios.jsonl"),
                  mock.patch.object(ejecutor, "evaluar", lambda op: evaluar(op, hoy=HOY, margenes=MARGENES)),
                  mock.patch.object(riesgo, "perdidas_de_hoy", return_value=(0.0, 0)),
                  mock.patch.dict("os.environ", {"ETORO_API_KEY": "k", "ETORO_USER_KEY": "u"})):
            p.start(); self.addCleanup(p.stop)
        self.llamadas = []

    def http(self, metodo, url, cuerpo, rid):
        self.llamadas.append((metodo, url, cuerpo))
        return {"orderId": 42} if metodo == "POST" else {"status": {"id": 3}}

    def test_no_emite_ticket_si_no_es_apto(self):
        with self.assertRaises(ejecutor.Rechazo):
            ejecutor.emitir_ticket(mes(contratos=2))

    def test_envio_a_demo_con_el_cuerpo_correcto(self):
        t = ejecutor.emitir_ticket(mes())
        r = ejecutor.enviar(t["id"], t["id"], http=self.http)
        metodo, url, cuerpo = self.llamadas[0]
        self.assertEqual(url, "https://public-api.etoro.com/api/v2/trading/execution/demo/orders")
        self.assertEqual(cuerpo, {"action": "open", "transaction": "buy", "symbol": "SP500.DEC26",
                                  "settlementType": "realFutures", "orderType": "limitIOC",
                                  "contracts": 1, "stopLossRate": 7613.0, "stopLossType": "fixed",
                                  "limitRate": 7646.0})
        self.assertEqual(r["estado"]["estado"], "ejecutada")

    def test_sin_confirmacion_no_se_envia(self):
        t = ejecutor.emitir_ticket(mes())
        with self.assertRaisesRegex(ejecutor.Rechazo, "sí"):
            ejecutor.enviar(t["id"], "si", http=self.http)
        self.assertEqual(self.llamadas, [])

    def test_ticket_manipulado_caducado_o_repetido(self):
        t = ejecutor.emitir_ticket(mes())
        ruta = ejecutor.TICKETS / f"{t['id']}.json"
        original = ruta.read_text()
        d = json.loads(original); d["operacion"]["contratos"] = 5
        ruta.write_text(json.dumps(d))
        with self.assertRaisesRegex(ejecutor.Rechazo, "modificado"):
            ejecutor.enviar(t["id"], t["id"], http=self.http)
        ruta.write_text(original)
        tarde = datetime.now() + timedelta(hours=1)
        with mock.patch.object(ejecutor, "datetime") as dt:
            dt.now.return_value = tarde
            dt.fromisoformat = datetime.fromisoformat
            with self.assertRaisesRegex(ejecutor.Rechazo, "caducado"):
                ejecutor.enviar(t["id"], t["id"], http=self.http)
        ejecutor.enviar(t["id"], t["id"], http=self.http)
        with self.assertRaisesRegex(ejecutor.Rechazo, "ya se envió"):
            ejecutor.enviar(t["id"], t["id"], http=self.http)
        self.assertEqual(sum(m == "POST" for m, *_ in self.llamadas), 1)

    def test_cuenta_real_bloqueada_sin_variable(self):
        t = ejecutor.emitir_ticket(mes())
        with self.assertRaisesRegex(ejecutor.Rechazo, "real bloqueada"):
            ejecutor.enviar(t["id"], t["id"], real=True, http=self.http)
        with mock.patch.dict("os.environ", {"ETORO_ENTORNO": "real"}):
            ejecutor.enviar(t["id"], t["id"], real=True, http=self.http)
        self.assertEqual(self.llamadas[0][1], "https://public-api.etoro.com/api/v2/trading/execution/orders")


if __name__ == "__main__":
    unittest.main()
