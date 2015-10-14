upper_line = 100
print "Fizz buzz counting up to {}.".format(upper_line)

for n in range(1,(upper_line + 1)):
    if n % 3 == 0 and n % 5 == 0:
        print("We're at #{} <--- **fizz buzz**".format(n))
    elif n % 3 == 0:
        print("We're at #{} <--- **fizz**".format(n))
    elif n % 5 == 0:
        print("We're at #{} <--- **buzz**".format(n))
    else:
        print("We're at #{}".format(n))