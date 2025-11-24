
def compute_least_squares_line(x_values, y_values):
 
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xx = sum(x*x for x in x_values)
    sum_xy = sum(x*y for x, y in zip(x_values, y_values))

    # Normal equation:
    # [ n      sum_x ] [ b ] = [ sum_y ]
    # [ sum_x  sum_xx ] [ m ]   [ sum_xy ]

    det = n * sum_xx - sum_x * sum_x
    if det == 0:
        raise ValueError("Determinant zero. Cannot compute least-squares line.")

    b = (sum_y * sum_xx - sum_x * sum_xy) / det
    m = (n * sum_xy - sum_x * sum_y) / det

    return b, m


def format_least_squares_line(x_min, x_max, b, m):
    return (
        f"{x_min:3.0f} <= x <= {x_max:8.0f} ; "
        f"y = {b:10.4f} + {m:10.4f} x ; least-squares"
    )