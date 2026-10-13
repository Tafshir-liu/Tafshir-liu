"""Balanced three-phase electrical power calculations (SI units)."""
from math import sqrt

def three_phase_power(voltage_ll: float, current_line: float, power_factor: float) -> dict:
    """Return balanced 3-phase S (VA), P (W) and |Q| (var)."""
    if voltage_ll < 0 or current_line < 0:
        raise ValueError("voltage and current must be nonnegative")
    if not 0 <= power_factor <= 1:
        raise ValueError("power_factor must be in [0, 1]")
    apparent = sqrt(3) * voltage_ll * current_line
    active = apparent * power_factor
    reactive_magnitude = apparent * sqrt(1 - power_factor**2)
    return {"apparent_va": apparent, "active_w": active, "reactive_var_magnitude": reactive_magnitude}

def line_current(power_w: float, voltage_ll: float, power_factor: float) -> float:
    """Line current for known three-phase real power."""
    if power_w < 0 or voltage_ll <= 0 or not 0 < power_factor <= 1:
        raise ValueError("require P >= 0, V > 0, and 0 < PF <= 1")
    return power_w / (sqrt(3) * voltage_ll * power_factor)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("voltage_ll", type=float, help="line-line RMS voltage, V")
    p.add_argument("current_line", type=float, help="RMS line current, A")
    p.add_argument("power_factor", type=float)
    a = p.parse_args()
    for name, value in three_phase_power(a.voltage_ll, a.current_line, a.power_factor).items():
        print(f"{name}: {value:.2f}")
