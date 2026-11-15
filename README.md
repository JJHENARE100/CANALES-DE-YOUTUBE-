# Departamento de futuros CME

Equipo de agentes de IA para operar micro futuros de CME Group en eToro, según
el organigrama que presentó Javier Molina (eToro) en «De Inversor a Trader
Activo», Rankia, Valencia, 13 de noviembre de 2026.

```
                 Javier — decide y da el «sí»
                            │
                   Coordinador Futuros
        ┌──────────────┬────┴─────────┬──────────────┐
  Contratos CME   Coberturas    Estrategias      Profesor
     (apoyo)     (estrategia)   direccionales     (apoyo)
        └──────────────┴────┬─────────┴──────────────┘
                   Control de riesgos — filtro
                            │
                     Ejecutor eToro — único que envía órdenes
```

El Coordinador es la sesión principal de Claude Code (`CLAUDE.md`); los otros
seis son subagentes en `.claude/agents/`. Los cálculos no los hace ningún
modelo: salen de `futuros/`, que es Python sin dependencias.

## Uso

Abre Claude Code en este repositorio y dile el objetivo, por ejemplo: «quiero
cubrir una cartera de 100.000 USD de bolsa americana» o «idea alcista en oro a
tres meses». También puedes usar los cálculos directamente:

```
python -m futuros ficha SP500.DEC26
python -m futuros cobertura --simbolo SP500.DEC26 --cartera 100000 --beta 1 --precio 7646
python -m futuros riesgo --simbolo SP500.DEC26 --direccion largo --contratos 1 \
       --entrada 7646 --stop 7613 --ultimo-dia 2026-12-18 [--ticket]
python -m futuros enviar TICKET --confirmo TICKET [--simular] [--real]
python -m futuros resultado --pnl -165
python -m unittest discover -s tests
```

## Antes de la primera operación

1. **Capital y cambio** en `datos/limites.json` (`capital_eur`, `eurusd`). Vienen
   los de la charla: 15.000 EUR al tipo BCE 1,1081.
2. **Márgenes** en `datos/margenes.json`: están vacíos a propósito. Sin margen
   con fecha de los últimos 7 días, Control de riesgos rechaza todo.
3. **Claves de eToro** como variables de entorno `ETORO_API_KEY` y
   `ETORO_USER_KEY`. Nunca en el repositorio.

## El filtro

| Límite | Valor |
|---|---|
| Margen / capital | ≤ 25 % direccional · ≤ 30 % cobertura documentada |
| Capital | ≥ 3× el margen inicial |
| Riesgo por operación | objetivo 1 % · máximo 2 % |
| Pérdida diaria | 4 % del capital o 4 stops seguidos |
| Stop | obligatorio, en múltiplos del tick |
| Cobertura | solo venta, nocional ≤ cartera × beta |

## Las cinco cerraduras del Ejecutor

1. Solo envía un ticket emitido por Control de riesgos, con su huella intacta.
2. El ticket caduca a los 30 minutos y se envía una sola vez.
3. Se vuelve a pasar el filtro justo antes de enviar.
4. Hay que teclear el identificador del ticket (`--confirmo`), y Claude Code
   pide permiso a la persona cada vez que se ejecuta `enviar`.
5. Cuenta demo por defecto. La real exige `--real` y `ETORO_ENTORNO=real`.

La orden se envía como `limitIOC` al precio de entrada del ticket: se ejecuta a
ese precio o mejor, o se cancela. Así el riesgo aprobado es el riesgo real.

## Qué falta

- **Probarlo contra eToro.** El Ejecutor sigue la documentación pública
  (`api-portal.etoro.com`) y está probado con un bróker simulado, no contra la
  API. Primera orden, siempre en demo. El parámetro `orderId` de la consulta de
  estado es el punto menos seguro: confírmalo en esa primera prueba.
- **Cerrar posiciones.** El endpoint de órdenes de eToro solo abre. La salida
  es el stop de la orden o el cierre manual en eToro; después se anota con
  `resultado`.
- **Roll.** Control de riesgos avisa a 5 días del último día de negociación,
  pero el roll no está automatizado.

Nada de esto es asesoramiento de inversión. Se puede perder más que el margen
inicial; los stops no están garantizados en mercados rápidos o con gaps; los
márgenes pueden cambiar; los contratos vencen.
