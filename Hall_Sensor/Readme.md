# Hall Sensor

## Main Purpose

I measured how accurate Hall Sensor current measurement is...

- [5 A](https://www.reichelt.de/entwicklerboards-stromsensor-bis-5-a-acs712elc-05b-debo2-sen-strom-p282585.html)
- [20 A](https://www.reichelt.de/entwicklerboards-stromsensor-modul-20-a-5-v-acs712elc-debo-sens-20a-p282569.html?&nbc=1&trstct=lsbght_sldr::282584)
- [30 A](https://www.reichelt.de/entwicklerboards-stromsensor-bis-30-a-acs712elc-30a-debo1-sen-strom-p282584.html?&nbc=1&trstct=lsbght_sldr::282569)

## Circuit Diagrams

Will follow...

## Software

No software was used, I noted the results by hand with precise multimeter.

## Plots

Can be found under /results.

## Findings

- Hall Sensor not very accurate, AND...
- reference voltage is crucial --> 0 A = Vref / 2
- I think in 20 A sensor measurement, there was a up in Vref while measuring from 1 A upwards?
- 5 A Sensor is defect!