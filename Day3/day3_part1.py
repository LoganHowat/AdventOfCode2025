batteries = open("batteries.txt").read().splitlines()


def joltFinder():
    total = 0
    for battery in batteries:
        prevJolt = '00'
        for jolt in battery:
            combo1 = prevJolt[0] + jolt
            combo2 = prevJolt[1] + jolt
            if int(combo1) > int(prevJolt) and int(combo1) >= int(combo2):
                prevJolt = combo1
            elif int(combo2) > int(prevJolt) and int(combo2) > int(combo1):
                prevJolt = combo2
        total = total + int(prevJolt)
    return total

print(joltFinder())