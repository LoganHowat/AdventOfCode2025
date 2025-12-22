batteries = open("batteries.txt").read().splitlines()

def joltFinder():
    total = 0
    for battery in batteries:
        prevJolt = '000000000000'
        for index1, jolt in enumerate(battery):
            remaining = len(battery) - (index1 + 1)
            for index, prev in enumerate(prevJolt):
                # We always want the bigest number at the start
                if remaining > 11 and int(prev) < int(jolt):
                    prevJolt = prevJolt[0:index] + jolt + ('0'*(len(prevJolt) - (index+1)))
                    break
                elif remaining <= 11:
                    # We don't want to replace a jolt if theres less than index jolts left on the battery
                    if index < 12-remaining-1:
                        continue
                    combo = prevJolt[0:index] + jolt + ('0'*(len(prevJolt) - (index+1)))
                    if int(combo) > int(prevJolt):
                        prevJolt = combo
                        break
        total = total + int(prevJolt)
    return total


print(joltFinder())