# ADC

## Main Purpose

I measured how accurate the AD Converters in ESP32 & Arduino Uno are.

## Circuit Diagram

Will follow...

## Software

- [Here](https://github.com/PaulusElektrus/ADC_Uno) you can find the software which ran on the Arduino Uno to generate the data.
- [Here](https://github.com/PaulusElektrus/ADC_ESP32) you can find the software which ran on the ESP32 to generate the data.

## Plots

Can be found under /results.

## Findings

- ESP32 ADC is very unprecise und unlinear --> Not usable for my project
- Arduino Uno is only 10 bit but very precise and linear --> Good usable for my project