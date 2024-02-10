import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            break
        else:
            print("Please Enter a number between 2 and 4\n")
    else:
        print("Enter Valid input again\n")


players_scores = [0 for _ in range(players)]
max_score = 50

while max_score > max(players_scores):
    for player_index in range(players):
        print("\nPlayer: ",player_index+1," your turn has started")
        print("Your total score is: ",players_scores[player_index],"\n")
        current_score=0

        while True:
            choice= input("Would you like to roll (y/Y)?")
            if choice.lower()!="y":
                break
            value = roll()
            if value==1:
                print("You rolled a 1!, your turn is over")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a: ",value)

            print("Your current score is: ",current_score)
                
        players_scores[player_index]+=current_score
        print("Your total score is: ",players_scores[player_index])

maximum_score = max(players_scores)
winning_index= players_scores.index(maximum_score)
print("\nPlayer: ",winning_index + 1," you are the winner, congratulations! and your score is: ",maximum_score)