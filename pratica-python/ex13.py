# Implemente um gerador que produza os números da sequência de Fibonacci.

a, b = 0, 1

print(a, b, end=' ')

for _ in range(11):
    c = a + b
    a, b = b, c
    print(c, end=' ')