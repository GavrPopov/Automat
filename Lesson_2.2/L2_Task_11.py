def bank(X, Y):
    total = X
    for _ in range(Y):
        total += total * 0.10
    return total

X = 1000  # Размер вклада в рублях
Y = 5  # Срок вклада в годах
result = bank(X, Y)
print(f"Сумма на счету спустя {Y} лет: {result:.2f} рублей")