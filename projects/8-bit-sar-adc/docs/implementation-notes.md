# SAR ADC architecture and implementation notes

**TSEK06 VLSI Design Project, Group 03, Linköping University**

This document supplements the [project README](../README.md). The project was collaborative, and the original report remains the primary source of detailed simulation and design information.

## Conversion sequence

1. The differential CDAC samples the analog input.
2. The SAR controller sets a trial bit, starting with the most significant bit (MSB).
3. Charge redistribution produces a differential DAC voltage.
4. The StrongARM dynamic comparator decides the trial bit value.
5. SAR flip-flops store the comparator result, and the controller moves to the next bit.
6. After eight bit decisions, the eight-bit code is available and the conversion completes.

## Building blocks

- **Dynamic latch comparator:** regenerative StrongARM-style comparator for low-static-power differential decisions, with downstream logic/latching.
- **SAR controller:** digital control using 19 D flip-flops with set/reset (DFFSR) for bit sequencing and data storage.
- **Capacitive DAC:** binary-weighted, fully differential capacitor array with bottom-plate sampling.
- **Physical design:** circuit schematics, layouts, and design-rule / layout-versus-schematic checks.

## My work

Contributions focused on SAR control logic modeling, testbench development and debugging with Kun Lin, DFFSR schematic/layout work, and SAR logic verification and integration. The complete converter and measured or simulated performance are **team results**.

## Reproducing the project

The report, Cadence schematics/layouts, process design kit (PDK), and simulation outputs have not been added to this folder. A reader cannot reproduce transistor-level results from this Markdown documentation alone. Process-library files should not be published without licensing authorization.
