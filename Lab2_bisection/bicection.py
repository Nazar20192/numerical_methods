def f(x):
    """Задана функція"""
    return x**3 - x - 3

def bisection(a, b, tol):
    """Метод бісекції для пошуку кореня рівняння f(x)=0"""
    if f(a) * f(b) >= 0:
        print("Помилка: на кінцях інтервалу знаки функції однакові.")
        return None

    step = 0
    while (b - a) / 2 > tol:
        step += 1
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        print(f"Крок {step}: a = {a:.5f}, b = {b:.5f}, c = {c:.5f}, f(c) = {f(c):.5f}")

    return (a + b) / 2

# Example usage:
# root = bisection(1, 2, 0.001)
# if root is not None:
#     print(f"\nЗнайдений корінь: {root:.5f}")
