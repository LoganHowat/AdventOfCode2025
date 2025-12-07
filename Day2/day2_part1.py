id_ranges = open("ids.txt").read().split(',')
print(id_ranges)

def invalidIDFinder():
    total = 0
    for id_range in id_ranges:
        start = int(id_range.split('-')[0])
        end = int(id_range.split('-')[1])
        for i in range(start, end + 1):
            if len(str(i))%2 == 0:
                id_check = str(i)
                middle = int(len(id_check)/2)
                first_half = id_check[0:middle]
                second_half = id_check[middle:]
                if first_half == second_half:
                    total = total + i
    return total

print(invalidIDFinder())