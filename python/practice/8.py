#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
def end(name):
    print(name+" won! cong!!")
    ans=input("again? y/n:")
    return ans

player1=input("input name 1P:")
player2=input("input name 2P:")
ans="y"

while(1):
    hand1=input(player1+": choose rock paper scissors:")
    hand2=input(player2+": choose rock paper scissors:")

    if(not(hand1=="rock" or hand1=="paper" or hand1 == "scissors")):
        print(hand1+":INVALID INPUT")
        exit()
    if(not(hand2=="rock" or hand2=="paper" or hand2 == "scissors")):
        print(hand2+":INVALID INPUT")
        exit()
    
    if(hand1 == hand2):
        print("Tie! AGAIN!")
    if(hand1 == "rock"):
        if(hand2 == "paper"):
            ans=end(player2)
        if(hand2 == "scissors"):
            ans=end(player1)
    if(hand1 == "paper"):
        if(hand2 == "scissors"):
            ans=end(player2)
        if(hand2 == "rock"):
            ans=end(player1)
    if(hand1 == "scissors"):
        if(hand2 == "rock"):
            ans=end(player2)
        if(hand2 == "paper"):
            ans=end(player1)
    if(ans=="n"):
        exit()
        
            
