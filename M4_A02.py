def em_serie(r1, r2):
    return r1 + r2

def em_paralelo(r1, r2):
    return r1 * r2 / (r1 + r2)

r1, r2 = map(float, input().split())

print(f"Serie: {em_serie(r1, r2):.2f}")
print(f"Paralelo: {em_paralelo(r1, r2):.2f}")