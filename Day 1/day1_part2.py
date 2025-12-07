moves = open("moves.txt").read().splitlines()

def find_password(moves):
    answer = 0
    current_position = 50
    for move in moves:
        number = move.strip('LR')
        if len(number) > 2:
            # If number is greater thn 99 we know it will cross 0 at least number/100 times
            answer = answer + int(number[0])
            number = int(number[1:])
        number = int(number)
        if 'L' in move:
            new_position = current_position - number
            previous_position = current_position
            if new_position < 0:
                current_position = (current_position - number) + 100
                #If the prev position was 0 it won't pass it again
                if current_position !=0 and previous_position !=0:
                    answer = answer + 1 
            else:
                current_position = new_position
        else:
            new_position = current_position + number
            if new_position > 99:
                current_position = (current_position + number) - 100
                if current_position != 0:
                    answer = answer + 1
            else:
                current_position = new_position
        if current_position == 0:
            print('Has landed on 0')
            answer = answer + 1
    
    return answer

print(find_password(moves))
