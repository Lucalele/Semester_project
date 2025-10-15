
"""
Piecewise Linear Interpolation Module
-------------------------------------
Implements piecewise linear interpolation between consecutive data points.
"""

def compute_piecewise_lines(x_values, y_values):
    """
    Given two lists of equal length (x_values, y_values),
    compute the slope (m) and intercept (b) for each adjacent pair.

    Returns a list of tuples:
        [(x_k, x_k+1, b, m), ...]
    """
    lines = []
    for k in range(len(x_values) - 1):
        x0, x1 = x_values[k], x_values[k + 1]
        y0, y1 = y_values[k], y_values[k + 1]

        # slope and intercept
        m = (y1 - y0) / (x1 - x0)
        b = y0 - m * x0

        lines.append((x0, x1, b, m))
    return lines


def format_line(x0, x1, b, m):
    """
    Format a single interpolation line exactly like the sample output.
    Example:
        0 <= x <= 30 ; y = 61.0000 + 0.6333 x ; interpolation
    """
    return f"{x0:3.0f} <= x <= {x1:8.0f} ; y = {b:10.4f} + {m:10.4f} x ; interpolation"


def write_interpolation_file(filename, x_values, y_values):
    """
    Write all piecewise interpolation lines for a single core to a file.
    """
    with open(filename, "w") as out:
        for (x0, x1, b, m) in compute_piecewise_lines(x_values, y_values):
            out.write(format_line(x0, x1, b, m) + "\n")
