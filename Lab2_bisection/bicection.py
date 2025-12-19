def f(x): return x**3 - x - 3

def bisection(a, b, tol): fa, fb = f(a), f(b) if fa * fb >= 0: print("Помилка: однакові знаки на краях") return None

step = 0
while (b - a) / 2 > tol:
    step += 1
    c = (a + b) / 2
    fc = f(c)
    
    print(f"Крок {step}: c = {c:.5f}, f(c) = {fc:.5f}")

    if fc == 0:
        return c
    
    if fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc

return (a + b) / 2
