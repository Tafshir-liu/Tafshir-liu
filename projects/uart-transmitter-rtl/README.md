# UART Transmitter in Verilog RTL

**Independent portfolio demonstration · Verilog · Digital design**

A compact, synchronous **8-N-1 UART transmitter** with an FSM, 8-bit data register, baud timing, active-high synchronous reset, and a completion pulse.

## Simulation

Install [Icarus Verilog](https://steveicarus.github.io/iverilog/) and run:

```bash
iverilog -g2012 -s tb_uart_tx -o uart_sim uart_tx.v tb_uart_tx.v
vvp uart_sim
```

The self-checking testbench sends `0xA5` and verifies the start bit, eight LSB-first data bits, stop bit, and busy/done signals.

## Interface

| Signal | Description |
| --- | --- |
| `start` | One-cycle transmit request when idle |
| `data[7:0]` | Byte sampled at the start request |
| `tx` | Idle high, then start/data/stop bits |
| `busy` | High during frame transmission |
| `done` | One-cycle pulse at frame completion |

Set `CLKS_PER_BIT = clock_frequency / baud_rate` as an integer. This is a **simulation-ready educational design**, not production IP. No FIFO, parity, oversampling receiver, error detection, or formal timing sign-off is included.

This project is independently created for a portfolio and is **not** submitted academic coursework or prior professional work.
