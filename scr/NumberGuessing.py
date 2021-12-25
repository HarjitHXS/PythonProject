import random
attempts_lists = []
def show_socre():
     if len(attempts_lists) <= 0:
          print("There is currently no high score, its yours for the taking!")
     else:
          print("The current high score is {} attempts".format(min(attempts_lists)))
def start_game():
      random_number = int(random.randint(1,10))
      print("Hello traveler! Welcome to the game of guesses!")
      player_name = input("What is your name? ")
      wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No)".format(player_name))
      attempts = 0
      show_socre()
      while wanna_play.lower() == 'yes':
            try:
                 guess = input("Pick a number between 1 and 10 ")
                 if int(guess) < 1 or int(guess) > 10:
                      raise ValueError("Please guess a number within the given range")
                 if int(guess) ==  random_number:
                      print("Nice you got it!")
                      attempts +=1
                      attempts_lists.append(attempts)
                      print("It took you {} attempts".format(attempts))
                      play_agian = input("Would you like to play again? (Enter Yes/No")


                      attempts = 0
                      show_socre()
                      random_number = int(random.randint(1,10))
                      if play_agian.lower() == "no":
                          print("That's cool, have a good onr!")
                          break
                      elif int(guess) > random_number:
                          print("It's lower")
                          attempts +=1
                      elif int(guess) < random_number:
                          print("It's higher")
                          attempts += 1
            except ValueError as err:
                print("Oh no!, that is not a valid vlaue. Try again..")
                print("({})".format(err))
      else:
           print("That's cool, have a good one!")

if __name__ == '__main__':
        start_game()

