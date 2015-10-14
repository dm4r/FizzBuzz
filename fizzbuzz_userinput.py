import sys

try:
    upper_limit = int(sys.argv[1])
except IndexError:
    upper_limit = int(raw_input("Enter an upper limit number for fizzbuzz to assess --> "))
except ValueError:
    upper_limit = int(raw_input("Non-numeric input detected, please enter an upper limit number for fizzbuzz to assess --> "))

print "Fizz buzz counting up to {}.".format(upper_limit)

# QUESTION: For the below (upper_limit + 1), is there a better way to include 100
# in teh defined range otherwise the value 100 is excluded when the for loop 
# assesses the range and I compensate for this by adding in: + 1
for n in range(1, (upper_limit + 1)):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
