import numpy as np

def polyfit_r2(x, y, degree):
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)

    yhat = p(x)
    ybar = np.mean(y)

    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)

    r2 = ssreg / sstot
    return {"coefficients": coeffs, "r_squared": r2}

# przykład
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3.2, 3.6, 4.5, 5.1])

result = polyfit_r2(x, y, 2)
print(result)
