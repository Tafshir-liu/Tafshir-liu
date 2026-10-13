# Balanced Three-Phase Power Calculator

**Independent portfolio demonstration · Python · Power engineering**

An easy-to-audit calculator for balanced sinusoidal three-phase AC systems using line-to-line RMS voltage, line current, and power factor.

## Equations

- Apparent power: `S = sqrt(3) × V_LL × I_L` (VA)
- Active power: `P = S × PF` (W)
- Reactive magnitude: `|Q| = S × sqrt(1 − PF²)` (var)
- Current: `I_L = P / (sqrt(3) × V_LL × PF)` (A)

## Run

Python 3.10+, standard library only:

```bash
python power.py 400 10 0.8
python -m unittest discover -v
```

Example: 400 V line-to-line, 10 A, PF 0.8 returns approximately **6.93 kVA**, **5.54 kW**, and **4.16 kvar**.

## Engineering assumptions

- **Balanced**, steady-state, sinusoidal, three-phase circuits only.
- Reactive power output is a **magnitude**. Leading/lagging direction is not modeled.
- Does not calculate short-circuit current, cable ampacity, thermal limits, harmonics, or equipment protection settings.
- **Not** for final equipment sizing or safety-critical electrical decisions without engineering checks and applicable standards.

This is new independent portfolio code motivated by prior industrial electrical engineering experience, **not an employer project**.
