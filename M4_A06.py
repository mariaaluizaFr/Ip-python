def menor_de(a, b):
    if a < b:
        return a
    return b

a, b, c = map(int, input().split())

print(menor_de(menor_de(a, b), c))