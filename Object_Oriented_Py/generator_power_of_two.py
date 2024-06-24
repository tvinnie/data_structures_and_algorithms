def power_of_two(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

    # test case
    for i in power_of_two(5):
        print(i)

    # test casem 2
#    t =  [i for i in power_of_two(5)]
#     print(t)