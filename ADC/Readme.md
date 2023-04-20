# ADC

## Main Purpose

I measured how accurate diverse analog digital converters (ADC) are...

## Circuit Diagrams

- For the voltage measurement:

![Circuit Diagram](Spannungsmessung.png)

- For the shunt measurement:

Will follow...

## Software

- [Arduino](https://github.com/PaulusElektrus/ADC_Uno)
- [ESP32](https://github.com/PaulusElektrus/ADC_ESP32)
- [Shunt](https://github.com/PaulusElektrus/Uno_Shunt) --> 0.1 Ohm shunt
- [ADS1115](https://github.com/PaulusElektrus/Arduino_and_ADS1115)

## Plots

Can be found under /results.

## Findings

- ESP32 ADC is very unprecise und unlinear --> Not usable for my project
- Arduino Uno is only 10 bit but very precise and linear --> Good usable for my project
- The 0,1 Ohm shunt results with the arduino are acceptable
- ADS1115 is with the integrated Vref and 16bit the best choice over all!