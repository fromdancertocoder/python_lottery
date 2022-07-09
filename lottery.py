import random
winning_numbers = [] 
while len(winning_numbers) < 5:
  new_number = random.randint(1, 99) 
  if new_number in winning_numbers:
    continue
  else: winning_numbers.append(new_number) 
print(winning_numbers)
guess_numbers = []
print("Welcome to the lottery, 5 numbers have been randomly selected try to guess them all")
while len(guess_numbers) < 5:
  guess = (input("You have entered {} guesses. Guess a number between 1 and 99: ".format(len(guess_numbers))))
  try: int_guess = int(guess)
  except ValueError: 
    print("no letters or decimal points please, whole numbers only, one guess at a time. Jeez")
    continue
  else: int_guess = int(guess)
  if int_guess > 99 or int_guess < 1:
    print("I said between 1 and 99 try again")
    continue
  if int_guess in guess_numbers:
    print("you already guessed that try a different number") 
    continue
  else: guess_numbers.append(int_guess) 
#print(guess_numbers)
correct = 0 
correct_guesses = []
for num in range(len(winning_numbers)):
  if winning_numbers[num] in guess_numbers:
    correct += 1
    correct_guesses.append(winning_numbers[num])   
if correct == 0:
  print("you got 0 correct sorry you get nothing") 
elif correct == 1:
  print("you got 1 right number {} you earn 100 credits".format(correct_guesses))
elif correct == 2:
  print("you got 2 right numbers {} you earn 1000 credits".format(correct_guesses))
elif correct == 3:
  print("you got 3 right numbers {} you earn 10000 credits".format(correct_guesses)) 
elif correct == 4:
  print("you got 4 right numbers {} you earn 100000 credits".format(correct_guesses)) 
elif correct == 5: 
  print("JACKPOT!!!!!! you got all 5 correct {} you earn 1000000 credits".format(correct_guesses))              
