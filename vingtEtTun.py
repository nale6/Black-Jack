#
# Alejandro Cazorla
#
# vingtEtTun.py
#
# A program that simulates the game of Vingt-et-un, where the players roll dice to score 21 points or as close as possible
# without going over. This will be a two-player game where the computer is the House. After either player scores 14 or higher,
# each subsequent roll will be made with only one die. The player may choose to stay at any time, however the House continues to
# play until 17 or higher, unless they have busted, which means to go above 21.

# Processing:
# 1. The program begins and asks the user for their name.
# 2. The user will be given a menu so they may choose from a selection.
# 3. The menu will consist of options that vary from reading the rules, quitting and starting the game.
# 4. On starting the game, the user will get two dice rolls made and be asked if they want to stay or not.
# 5. The House will always go after the player, and chooses to stay after 17 as per the game rules.
# 6. Two dice is rolled for both players until they are at or above 14, where they roll one die.
# 7. Whoever busts first automatically loses. If there is no busts, then when both players stay, the total is compared.
# 8. The player may choose to play however many times they wish, exiting once the game is finished.

# Output: Vingt-Et-Un

import random;
import os;

#Global variables to keep proper track of the score
wins = 0
loss = 0
ties = 0

#Main function
def main() :
  #Asks and returns the name of player
  name = introduction()
  #The menu is brought up here, the quit verification is for if an exit message is needed.
  quitVerification = userInput(name)
  #Restart function called at the end, only showing text if the player has played a game. If they haven't, then they quit in the menu.
  restart(quitVerification)
  

#Introductory text
def introduction() :
  print("Ving-et-un Game...\n")
  name = input("What is your name?\n\n")
  return name

#Generates the menu and keeps track of the user's name
def userInput(name) :
  valid = False
  #Input validation
  while(valid == False) :
    print("1. See the Rules.")
    print("2. Play Vint-et-un.")
    print("3. Quit.\n")
    #User chooses the menu, and the number must be valid or they get asked again
    userInput = int(input("Please choose one of the options: "))
    if(userInput > 0 and userInput < 4) :
      print("")
      valid = True
    else :
      print("You have made an invalid input, please try again.\n")
  #Runs the proper option input they took, still passing the name to keep track of it
  option(userInput, name)

#The function that goes through several if-statements and runs the option accordingly
def option(userInput, name) :
  #This quit verification exists as a validation for the restart function's text showing up.
  #Basically, if the user quits, then they won't get the text from the restart function asking
  #if they want to play again, because they are already quitting,
  quitVerification = False

  if(userInput == 1) :
    #We pass the name variable into rules just for the sake of keeping track the user's name.
    rules(name)
  elif(userInput == 2) :
    #This starts the actual game
    game(name)
  elif(userInput == 3) :
    #Print the goodbye message here and return true for quit verification so that the restart function's text does not show up
    print("Exiting program... Goodbye")
    quitVerification = True
  else :
    #Default error message, this should never come up
    print("An error has been made, please restart the program.")
    quitVerification = True

  return quitVerification

#Prints the full list of rules for this game
def rules(name) :
  print("The goal of the game is to score 21 points or as close as possible without going over.")
  print("Two players take turns throwing two dice, as many as desired, adding the number rolled on the dice.")
  print("The two players will be the player, you, versus the House, the program CPU.\n")
  print("1. A player getting over 21 loses the game.")
  print("2. The player with the total closest to 21 wins.")
  print("3. If both players roll equal number, it is a tie.\n")
  print("The game is over at the end of a round when one or both players are bust (over 21), or both players choose to stay.\n")
  print("If a player has a total of 14 or more, the player only rolls one dice for the remaining round.")
  print("The house must throw dice until the total is 17 or higher. At 17 or higher, the house must stay.\n")

  #This is an input because it would be annoying to get more text back from the menu, so we ask the user to make an
  #input to go back to the menu once they are done reading.
  input("After you are done reading, please make any input to continue back to the menu.")

  #Brings up the menu option again and passes the name in it to keep track
  userInput(name)

#Game function
def game(name) :
  #Initialize the needed variables. We make a boolean variable for the game loop, two bools for the House for when they are finished with their turn or finished playing (choosing to stay).
  #We make another boolean variable for the player for when they are fully finished, which is if they choose to stay with their total.
  #The final boolean will be for input validation. After this, it will just be variables that store numbers, such as the number of rounds played, the House's and user's total, and for what the dice rolls.
  gameLoop = True
  houseFinished = False
  houseFinishedTurn = False
  playerFinished = False
  playerWin = 'a'
  inputValidation = False
  houseTotal = 0
  userTotal = 0
  dice1 = 0
  dice2 = 0
  round = 0
  
  #Game loop that runs until House and player are finished playing the game, or if either goes bust.
  while(gameLoop == True) :

    #As long as the House does not stay, they will get their turn played in the round.
    if(houseFinished != True) :
      houseFinishedTurn = False

    #Adds one to the round and prints it.
    round += 1
    print(f"Round {round}")

    #The player's turn
    if(playerFinished != True) :
      print(f"{name}'s turn.")

      #On the first round, there is no option to stay, it's always played. Always rolls two dice.
      if(round == 1) :
        #Use the imported random library to have proper random numbers for the dice, 1 to 6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        userTotal += (dice1 + dice2)
        print(f"You rolled {dice1} and {dice2} for a total of {userTotal}.\n")
        #Stay is always equal to 'n' which is no
        stay = 'n'

      #If not round 1, the user is asked if they choose to stay
      elif(round != 1) :
        inputValidation = False

        #If they do, they are completely done playing and the House will continue to play until they stay or go bust
        while(inputValidation == False) :
          stay = input("Do you stay? (y/n) : ")
          #'y' means yes, use lower function so that if they write it in capital, it still goes through
          if(stay.lower() == 'y') :
            inputValidation = True
            playerFinished = True

          #'n' means no, same deal here, if they write it in capitals, it still runs.
          elif(stay.lower() == 'n') :
            inputValidation = True

          #Invalid variable entered
          else :
            print("\nInvalid input.\n")

      #If it's not round 1 and user does not choose to stay and the total is below 14, two dice is rolled and added.
      if(round != 1 and userTotal < 14 and stay.lower() == 'n') :
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        userTotal += (dice1 + dice2)
        print(f"You rolled {dice1} and {dice2} for a total of {userTotal}.\n")

      #Same thing, except if user has 14 or more as a total, only one die is rolled and added.
      elif(round != 1 and userTotal >= 14 and userTotal < 22 and stay.lower() == 'n') :
        dice1 = random.randint(1, 6)
        userTotal += dice1
        print(f"You rolled {dice1} for a total of {userTotal}.\n")

      #If the user busts, they automatically lose. All necessary bool variables needed for the game to end is switched here.
      if(round != 1 and userTotal > 21 and stay.lower() == 'n') :
        print("You have gone over 21 and busted!\n")
        playerFinished = True
        houseFinished = True
        gameLoop = False


    #House's turn, and as long as they are not done playing, this will run
    if(houseFinished == False) :
      print("The House's turn.")

      #This bool only resets if the House is not done playing.
      while(houseFinishedTurn == False) :
        if(round == 1) : 
          #Same thing here, the dice will store a random digit from 1-6
          dice1 = random.randint(1, 6)
          dice2 = random.randint(1, 6)
          houseTotal += (dice1 + dice2)
          houseFinishedTurn = True

          print(f"House rolls {dice1} and {dice2} for a total of {houseTotal}.\n")

        #If the house has less than 17 and 14, they roll two dice and they are added to the total
        elif(houseTotal < 17 and houseTotal < 14) :
          dice1 = random.randint(1, 6)
          dice2 = random.randint(1, 6)
          houseTotal += (dice1 + dice2)
          houseFinishedTurn = True
          print(f"House rolls {dice1} and {dice2} for a total of {houseTotal}.\n")

          #Checks here if the house didn't bust. This occurs in every if-statement where the house rolls.
          #If they bust, all the necessary bools to end the game is switched here as the house automatically loses.
          if(houseTotal > 21) :
            playerFinished = True
            houseFinished = True
            playerWin = 'w'
            gameLoop = False

        #If house total is less than 17 but 14 or more, but did not bust, then they roll one die and it gets added to the total
        elif(houseTotal < 17 and houseTotal >= 14 and houseTotal < 22) :
          dice1 = random.randint(1, 6)
          houseTotal += dice1
          houseFinishedTurn = True

          print(f"House rolls {dice1} for a total of {houseTotal}.\n")

          #Checks if house busts.
          if(houseTotal > 21) :
            playerFinished = True
            houseFinished = True
            playerWin = 'w'
            gameLoop = False

        #If house has 17 or more but did not bust, the house will stay and this will be the final action the house takes until the user also stays.
        elif(houseTotal >= 17 and houseTotal < 22) :
          print(f"House has decided to stay with a total of {houseTotal}.\n")

          #Set the bool variable for the house to be completely done here.
          houseFinished = True
          houseFinishedTurn = True

        #Checks again if the house has gone over 21 as a precaution.
        elif(houseTotal > 21) :

          playerFinished = True
          houseFinished = True
          playerWin = 'w'
          gameLoop = False
          houseFinishedTurn = True

    #If both the house and the user stay, the game is over, or if either one busted.
    if(houseFinished == True and playerFinished == True) :
      #If user's total is over 21, meaning they busted, they lose.
      if(userTotal > 21) :
        print(f"{name} went over 21 and busted.")
        #Sets player win to 'l' for lose.
        playerWin = 'l'

      #If house busted, they lose.
      elif(houseTotal > 21) :
        print("House went over 21 and busted.")
        #Player win set to 'w' for win
        playerWin = 'w'

      #If user and house have same total, they tie. This should never happen if either busts because the game immediately ends if either one busts.
      elif(userTotal == houseTotal) :
        #Compares the score.
        print(f"{name} : {userTotal} | House : {houseTotal}")
        #Sets to tie.
        playerWin = 't'

      #If any of the above is not the case, then there is a victor from cases where neither have busted.
      else :
        #If user has higher total, then they win
        if(userTotal > houseTotal) :
          print(f"{userTotal} | House : {houseTotal}")
          playerWin = 'w'

        else :
          #Otherwise, the house has a higher total and they win.
          print(f"{name} : {userTotal} | House : {houseTotal}")
          playerWin = 'l'

      #Passes whether if player lost, tied or won and their name to a function that prints out a message accordingly.
      victoryLossMessage(playerWin, name)
      #Sets gameloop to false as the game is over.
      gameLoop = False

#This prints the score which is kept as a global variable
def printScore() :
  #Need to initialize the global variable
  global wins
  global loss
  global ties
  
  print("Your score:")
  print("------------")
  print(f"Wins: {wins}")
  print(f"Losses: {loss}")
  print(f"Ties: {ties}")

  #Will ask if the user wants to restart, a false verification is sent in it to give the restart message.
  restart(False)

#The function that prints whether player won, lost or tied
def victoryLossMessage(playerWin, name) :
  #Need to initialize the global variable
  global wins
  global loss
  global ties

  #The passed char element determines if the user won, lost or tied and prints their name.
  #If 'w', it means won, if 'l', it means loss, if 't', it means tie.
  if(playerWin == 'w') :
    print(f"{name} wins, congratulations!")
    #Adds one to the win global variable
    wins += 1

  elif(playerWin == 'l') :
    print(f"Sorry {name}, you lost...")
    #Adds one to the loss global variable
    loss += 1

  elif(playerWin == 't') :
    print(f"{name}, There's been a tie!")
    #Adds one to the tie global variable
    ties += 1

  #Blank line for formatting
  print("\n")
  #Prints the score after
  printScore()

#Restart function
def restart(quitVerification) :
  #If the quit verification variable is false, it will print a message asking the user if they would like to restart.
  #We do this because if the user quits, then this function is ran because it's in main, but it does not actually print out anything, or do anything.
  #This is so the user is not asked to restart a game they never played, because they chose to exit from the menu already.

  #Use quit verification as an input verification two-for-one as well
  while(quitVerification == False) :
    userInput = input("\nWould you like to restart? (y/n) : ")

    #If user wants to restart, main will be ran from the start
    if(userInput.lower() == 'y') :
      quitVerification = True
      #Print lines to clear the terminal of text
      print('\n' * 100)
      #We use the imported os library to clear the terminal here
      os.system('cls||clear')
      #Restarts from main from the top
      main()

    #Otherwise, lets restart function go through without doing anything, and lets main run to the end where the program finishes.
    elif(userInput.lower() == 'n') :
      quitVerification = True
      print("Quitting... Thank you for playing. Goodbye")

    #Default error message
    else :
      print("You have made an invalid input, please try again.\n")
  
#Calls the main function to begin the program
main()