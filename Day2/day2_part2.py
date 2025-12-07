id_ranges = open("ids.txt").read().split(',')

def invalidIDFinder():
    total = 0
    for id_range in id_ranges:
        start = int(id_range.split('-')[0])
        end = int(id_range.split('-')[1])
        for i in range(start, end + 1):
            id_check = str(i)
            middle = round(len(id_check)/2)
            first_half = id_check[0:middle]
            combination = ''
            for digit in first_half:
                combination = combination + digit
                if len(id_check.replace(combination, '')) == 0:
                    total = total + i
                    break
                

    return total

print(invalidIDFinder())