def func1(x):
    print((x**4 - 8*(x**2) + 6*x - 5) - (x**3 - 2*(x**2) + 8) * (x**2 - 9*x - 5))


def func2(X):
    for x in X:
        print((x**4 - 8*(x**2) + 6*x - 5) - (x**3 - 2*(x**2) + 8) * (x**2 - 9*x - 5))


func1(2)
func2([5, 7, 2, 3.1])
