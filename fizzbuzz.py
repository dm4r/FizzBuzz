upper_limit = 100
print "Fizz buzz counting up to {}.".format(upper_limit)

# QUESTION: For the below (upper_limit + 1), is there a cleaner way to include 100
# otherwise the value 100 is excluded when the for loop assesses the range
for n in range(1, (upper_limit + 1)):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
