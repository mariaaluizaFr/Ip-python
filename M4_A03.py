def tensao(adc):
    return adc * 5.0 / 1023

adc = int(input())

print(f"{tensao(adc):.2f}")