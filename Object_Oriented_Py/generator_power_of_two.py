def power_of_two(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

    # test case
    for i in power_of_two(5):
        print(i)