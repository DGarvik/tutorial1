###### Solution for the Fizz Buzz problem #####
#Description: Prints out numbers between 0 and 100, for multiples of 3 it prints Fuzz
# and for multiples of 5 it prints Buzz.


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

