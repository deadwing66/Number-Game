import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

value = roll()
print(value)
while True:
    players = input("Number of players (2-5): ")
    if players.isdigit():
        players = int(players)
        if 2<=players<=5: 
            break
        else:
             print("enter valid number of players")
    else:
        print("Invalid Input")       
print (players)

max_score = 50
player_score = [0 for _ in range(players)]
print(player_score)

while max(player_score)<max_score:

    for i in range(players):
        print("player", i +1," your turn has started! \n")
        current_score = 0

        while True:
            should_roll = input("If you want to roll, enter (y) ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value ==1:
                print("you got a 1. turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print("you got a ", value)

            print ("your current score is ", current_score)

        player_score[i] += current_score
        print("your final score is: ", player_score[i])

            
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("player number ", winning_idx+1, " has won! With heighest score of ", max_score)