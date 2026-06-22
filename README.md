# discrete-transistor-stepper-driver
Custom Darlington pair driver board for 5-wire stepper motors.

# Discrete Transistor Stepper Driver

A custom-designed, homemade hardware driver built using discrete NPN transistors configured as Darlington pairs to control a 5-wire unipolar stepper motor. 

## Hardware Build
Here is the fully assembled driver board built on a prototyping perfboard:

![Assembled Driver Board](driver-hardware.jpg)

## Schematic
The circuit layout for the Darlington pair configuration:

![Circuit Schematic](driver-schematic.jpg)

## Features
* **Discrete Components:** Built using classic 2N2222 TO-18 NPN transistors.
* **Darlington Pair Configuration:** Boosts current handling for switching inductive loads.
* **Integrated Flyback Protection:** Uses 1N4007 diodes to clamp high-voltage inductive spikes.
* **5-Wire Compatibility:** Optimized for unipolar motors with a common VCC rail.

## How It Works
Each motor channel uses a 10 kΩ base resistor protecting a two-stage Darlington transistor configuration. When a logic high signal is applied to an input channel, the Darlington pair saturates, pulling the motor coil to ground to complete the circuit.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
