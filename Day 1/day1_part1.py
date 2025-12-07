moves = open("moves.txt").read().splitlines()

def find_password(moves):
    answer = 0
    current_position = 50
    for move in moves:
        number = move.strip('LR')
        if len(number) > 2:
            number = int(number[1:])
        number = int(number)
        if 'L' in move:
            new_position = current_position - number
            if new_position < 0:
                current_position = (current_position - number) + 100
            else:
                current_position = new_position
        else:
            new_position = current_position + number
            if new_position > 99:
                current_position = (current_position + number) - 100
            else:
                current_position = new_position
        if current_position == 0:
            answer = answer + 1
    
    return answer

print(find_password(moves))
