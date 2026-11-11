def mapear(x, de_min, de_max, para_min, para_max):
    return para_min + (x - de_min) / (de_max - de_min) * (para_max - para_min)

x, de_min, de_max, para_min, para_max = map(float, input().split())

print(f"{mapear(x, de_min, de_max, para_min, para_max):.2f}")