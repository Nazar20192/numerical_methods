if fa * fb >= 0:
    print("Помилка: однакові знаки на краях")
    return None

step = 0
while (b - a) / 2 > tol:
    step += 1
    c = (a + b) / 2
    fc = f(c)

    print("Крок", step, ": c =", round(c, 5), ", f(c) =", round(fc, 5))

    if fc == 0:
        return c

    if fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc

return (a + b) / 2
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
tol = float(input("Введіть точність: "))

root = bisection(a, b, tol)

if root is not None:
print("Наближений корінь:", round(root, 6))
