'''Wylicz największy wspólny dzielnik 2 liczb podanych jako parametry'''


def greatest_common_measure(x,y):
    all_divisors = []
    for i in range(1, y) or i in range(1, x):
        if x % i == 0 and y % i == 0:
            all_divisors.append(i)
    print(max(all_divisors))


greatest_common_measure(60, 100)



