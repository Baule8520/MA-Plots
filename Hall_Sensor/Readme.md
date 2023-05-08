# Hall Sensor

## Main Purpose

I measured how accurate Hall Sensor current measurement is...

- [20 A](https://www.reichelt.de/entwicklerboards-stromsensor-modul-20-a-5-v-acs712elc-debo-sens-20a-p282569.html?&nbc=1&trstct=lsbght_sldr::282584)
- [30 A](https://www.reichelt.de/entwicklerboards-stromsensor-bis-30-a-acs712elc-30a-debo1-sen-strom-p282584.html?&nbc=1&trstct=lsbght_sldr::282569)

## Circuit Diagrams

- For the hall sensor measurement:

Will follow...

## Software

No software was used, I noted the results by hand with precise multimeter.

## Plots

Can be found under /results.

## Findings

- Hall Sensor very accurate, BUT...
- reference voltage is crucial --> 0 A = Vref / 2
- I think in 20 A sensor measurement, there was a up in Vref while measuring from 1 A upwards?
- Otherwise the 30 A sensor is more accurate... (?)
- Also I plotted the data from 0 - 4 A to directly compare with Shunt measurement --> see [here](https://github.com/PaulusElektrus/MA-Plots/tree/main/Shunt)