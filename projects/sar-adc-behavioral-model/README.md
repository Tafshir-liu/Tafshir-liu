# Ideal SAR ADC Behavioral Model (Python)

**Independent portfolio demonstration · Python · ADC algorithms**

A small, testable reference model of an **ideal unipolar successive-approximation ADC**. It traces each MSB-to-LSB trial decision and returns the quantized code.

This is **new independent portfolio code**, not code from the TSEK06 Group 03 ADC. It complements the [academic transistor-level SAR ADC case study](../8-bit-sar-adc/README.md).

## Run

Requires Python 3.10+; no external dependencies.

```bash
python sar_adc.py 1.65
python -m unittest discover -v
```

For an 8-bit, 3.3 V range, an input of 1.65 V yields code **128** (`10000000`). One LSB is 3.3/256 = 12.890625 mV.

## Design decisions and limitations

- Binary-search trials start at the MSB and execute once per bit.
- Ideal sample, DAC, reference, and comparator. No noise, offset, settling, mismatch, DNL, or INL.
- Input range: 0 to Vref; full-scale input saturates at code 255.
- Not a verified model of a *fully differential* physical ADC.
- Tests check endpoints, midscale, bit-trace length, and invalid input handling.

**Suggested next steps:** add a differential front-end, capacitor mismatch model, Monte Carlo simulation, and plots of DNL/INL.
