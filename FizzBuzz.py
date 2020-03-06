####### Solution for the Fizz Buzz problem ######


def fizzbuzz():
    list_of_nums = []
    num = 0

    for num in range(0, 100):
        num += 1

        if num % 3 == 0:
            list_of_nums.append("Fizz")
        elif num % 5 == 0:
            list_of_nums.append("Buzz")
        else:
            list_of_nums.append(num)

    print(list_of_nums)


fizzbuzz()

