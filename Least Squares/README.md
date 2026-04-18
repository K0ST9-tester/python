# Least Squares Linear Fit in Python

This project implements a **linear least squares regression** from scratch in Python and visualizes the result using `matplotlib`.

It computes the best-fit line:

y = ax + b

along with the **uncertainties of the coefficients** (`error_a`, `error_b`) and displays them directly on the plot.

---

## Method

The program uses the **analytical solution to linear least squares**:

* Slope:

  a = (N Σxy − Σx Σy) / (N Σx² − (Σx)²)

* Intercept:

  b = (Σy − a Σx) / N

* Variance estimate:

  σ² = Σ(yi − (axi + b))² / (N − 2)

* Uncertainties:

  error_a = √(N σ² / denominator)
  error_b = √(σ² Σx² / denominator)

---

## Data Format

The input file should look like:

(skip first two header lines)

index   x_value   y_value

Example:

```
# header
# header
1   10.0   2.1
2   20.0   4.3
3   30.0   6.2
```

---

## How to Run

1. Install dependencies:

```
pip install numpy matplotlib
```

2. Place your data file (e.g. `data_RMS.txt`) in the project directory.

3. Run:

```
python main.py
```

---

## Output

The program generates a plot showing:

* Blue points → measured data
* Red line → least squares fit
* Annotation box → fitted equation with uncertainties

Example:

a = 1.234 ± 0.056
b = 0.789 ± 0.032

---

## Notes

* Assumes uncertainty only in **y-values**
* Uses **unweighted least squares**
* Requires at least 3 data points

---

## Possible Improvements

* Add error bars for measurements
* Support weighted least squares
* Load other file formats (CSV, JSON)

---
