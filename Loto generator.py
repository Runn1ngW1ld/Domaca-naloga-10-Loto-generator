import random

print "Dobrodosli v generatorju Loto stevilk."


user = int(raw_input("Koliko stevilk hocete generirat: "))

def generator(start, end, num):
    numbers = []

    for x in range(user):
        numbers.append(random.randint(1, 39))
    return numbers

num = user
start = 1
end = 39
print (generator(start, end, num))
print "END"
