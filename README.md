It's a simple and fun game of 4 players where you keep getting a new random number ranging from 1 to 6, any number other than 1 adds up to your score but as soon as you get a 1 your chance is over! The player with the highest score wins. 

The game starts with player 1


![Image](https://github.com/user-attachments/assets/42d36bd5-b13d-4b92-86ac-dfbfc180bbd0)


-- Player gets a random number between 1 - 6
-- Any number other than 1 adds up to the player's score



![Image](https://github.com/user-attachments/assets/937369b5-8e6e-4a23-85f6-9d6342f56da7)



-- As soon as a player gets a  1  their chance gets over



![Image](https://github.com/user-attachments/assets/878e0f59-a004-48e7-8eac-7c5c0d662b6e)



Next Player begins 
--> The game goes on until the player with the highest score wins.

Here is the code of the full game!

```
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

value = roll()
print(value)
while True:
    players = input("Number of players (2-5): `")`
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
```
