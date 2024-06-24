def powers(n):
    val_power = 1
    for i in range(n):
        yield val_power
        val_power *= 2

t = list(powers(6))
print(t)

# Output
