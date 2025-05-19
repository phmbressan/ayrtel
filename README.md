# Ayrtel

A Python script for extracting telemetry data from video using OpenCV and tesseract OCR.

## Requirements
- Python 3.8 or higher
- OpenCV
- Tesseract OCR

## Usage

After installing the required packages described in ``pyproject.toml``, simply run the script ``ayrtel/main.py``.

## Example

A sample of the results is shown below:

| Time (s) | Space (m) | Stgpr (psi) | Stgtgt (psi) | Stgstn (m/m²) | Stgact (psi) | Pedal 1 (%) | Gear (-) | Clutch (mm) | Pedal 2 (%) | Potd (%) | N (Rpm) | Rodsp (km/h) | Rearsp (km/h) | Lat Acc (g) | Lon Acc (g) |
|----------|-----------|-------------|--------------|----------------|---------------|--------------|-----------|--------------|--------------|-----------|---------|----------------|----------------|-------------|-------------|
| 8.9600   | 640.000   | 235.00      | 411.00       | -11.97          | 670.00        | 60           | 6         | 5.30         | 100.60       | 101.30    | 13709.00 | 302.00         | 8.00          | 1.90        | 2           |
| 8.9800   | 640.000   | 238.00      | 411.00       | -11.97          | 670.00        | 60           | 6         | 5.30         | 100.60       | 101.30    | 13739.00    | 302.00         | 8.00          | 1.36        | 3           |
| 9.0000   | 648.000   | 211.00       | 576.08       | -19.45          | 764.00        | 60           | 6         | 5.20         | 100.60       | 101.50    | 13649.00  | 306.00         |       -         | 1.78        | 0.7         |

Note: Due to the nature of OCR, the data may not be 100% accurate. It is recommended to verify the results manually.