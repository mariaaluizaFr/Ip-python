def tensao(adc):
    return adc * 5.0 / 1023

def para_motor(v):
    return v * 100 / 5.0

def saturar(p):
    if p > 80:
        return 80
    return p

adc = int(input())

p = saturar(para_motor(tensao(adc)))

print(f"motor: {round(p)}%")