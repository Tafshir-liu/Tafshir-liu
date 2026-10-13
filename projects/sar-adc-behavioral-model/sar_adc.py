"""Ideal 8-bit SAR ADC model. Standard-library only."""
from dataclasses import dataclass

@dataclass(frozen=True)
class SARResult:
    code: int
    bits: tuple[int, ...]
    trial_codes: tuple[int, ...]

def convert(vin: float, vref: float = 3.3, bits: int = 8) -> SARResult:
    """Unipolar ideal SAR quantizer for 0 <= vin <= vref.

    Inputs at/above full scale saturate at the maximum code.
    This is a teaching model, not a transistor-level circuit simulator.
    """
    if not (1 <= bits <= 16 and vref > 0):
        raise ValueError("bits must be 1..16 and vref > 0")
    if not (0 <= vin <= vref):
        raise ValueError("vin must be within [0, vref]")
    code = 0
    trials = []
    decisions = []
    for index in range(bits - 1, -1, -1):
        trial = code | (1 << index)
        trials.append(trial)
        if vin >= trial * vref / (1 << bits):
            code = trial
            decisions.append(1)
        else:
            decisions.append(0)
    return SARResult(code, tuple(decisions), tuple(trials))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ideal SAR ADC bit-decision trace")
    parser.add_argument("voltage", type=float)
    parser.add_argument("--vref", type=float, default=3.3)
    args = parser.parse_args()
    result = convert(args.voltage, args.vref)
    print(f"code={result.code}, binary={result.code:08b}")
    for index, (trial, decision) in enumerate(zip(result.trial_codes, result.bits), 1):
        print(f"step {index}: trial={trial:3d}, keep={decision}")
