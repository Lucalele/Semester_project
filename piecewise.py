from least_squares import compute_least_squares_line, format_least_squares_line

def compute_piecewise_lines(x_values, y_values):
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
    return f"{x0:3.0f} <= x <= {x1:8.0f} ; y = {b:10.4f} + {m:10.4f} x ; interpolation"


def write_interpolation_file(filename, x_values, y_values):
    with open(filename, "w") as out:

        # Existing interpolation code
        for (x0, x1, b, m) in compute_piecewise_lines(x_values, y_values):
            out.write(format_line(x0, x1, b, m) + "\n")

        # Append least-squares line
        b_ls, m_ls = compute_least_squares_line(x_values, y_values)
        x_min, x_max = min(x_values), max(x_values)

        out.write(format_least_squares_line(x_min, x_max, b_ls, m_ls) + "\n")
