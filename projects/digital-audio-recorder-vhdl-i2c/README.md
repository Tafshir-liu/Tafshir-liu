# Digital Audio Recorder with VHDL and I²C

**TSTE12 · Linköping University · Team project · Completed**

## Project overview

This university team project involved developing a **digital audio recorder** using **VHDL** and the **I²C (Inter-Integrated Circuit)** communication protocol. The project brought together digital logic, peripheral control, timing-sensitive communication, and system integration.

## My contribution: I²C peripheral interface

My primary responsibility was implementing the **I²C interface for peripheral control** and helping integrate it into the audio-recorder system.

- Developed VHDL logic for I²C-based peripheral communication and control.
- Worked through protocol timing requirements and debugged communication behavior during implementation.
- Supported integration of the interface with the larger digital audio recorder.
- Collaborated with the project team to achieve successful system communication.

## Technology and engineering focus

| Area | Details |
| --- | --- |
| Hardware description language | VHDL |
| Communication | I²C peripheral control |
| Design area | Digital logic, embedded systems |
| Engineering challenges | Protocol timing, debugging, subsystem integration |
| Project context | Digital audio recording system developed collaboratively |

## Design evidence from project screenshots

The available presentation screenshots show a recorder system organized around an FPGA with an audio CODEC, audio I/O, I²C peripheral-control interface, SRAM storage, recorder logic, volume/balance functions, keyboard/control interfaces, and VGA output. The screenshots also show hierarchical hardware block schematics.

### FPGA device utilization

A supplied compilation screenshot identifies device **EP4CE115F29C7** and shows the following resource usage:

| Resource | Used | Available | Utilization |
| --- | ---: | ---: | ---: |
| I/O pins | 83 | 529 | 15.69% |
| LUTs | 1,932 | 114,480 | 1.69% |
| Registers | 994 | 114,753 | 0.85% |
| Memory bits | 0 | 3,981,312 | 0.00% |
| DSP 9-bit elements | 0 | 532 | 0.00% |

These figures come from the **supplied compilation screenshot** and describe reported FPGA resource allocation. They do not by themselves establish measured audio quality, timing closure, hardware performance, or final system testing.

### Available figures

The user has provided screenshots of the system-level architecture, hierarchical design blocks, and FPGA utilization report. **Image assets have not yet been committed to this repository**, so they are not embedded below. Once the image files are published in the project folder, this section can be converted to a visual gallery with original captions and relative links.

## What I learned

The project strengthened my skills in designing timing-sensitive digital interfaces, debugging hardware-description-language implementations, and coordinating interfaces within a larger embedded system.

## Portfolio documentation status

This README is a **description of a completed academic team project**, based on the contributor's project summary. It is **not** a claim that the full audio recorder was individually designed by me.

The original VHDL sources, testbenches, waveforms, block diagrams, hardware specifications, and demonstration recordings **have not been uploaded here**. Those artifacts can be added when available and when the team and course sharing rules allow it. As a result, this folder is currently a project case study rather than a reproducible source-code release.

[Back to GitHub profile](../../README.md)
