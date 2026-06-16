#succesion de fibonacci


n_terminos = 10 
fibonacci = []

a, b = 0, 1
while len(fibonacci) < n_terminos:
    fibonacci.append(a)
    a, b = a + b

print(fibonacci)