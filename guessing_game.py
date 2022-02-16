import random
import sys
scores = []

print("=========================")
print("=-----W3LC0M3 2 TH3-----=")
print("=--NUMB3R-GU3SS1NG-GAM3-=")
print("=========================\n")

def start_game():
	answer = random.randrange(1,11)
	attempts = 0
	while True:
		guess = input("Please guess a number between 1-10: ")
		try:
			guess = int(guess)
			attempts += 1
		except ValueError:
			print("\nOops! Invalid entry.")
		else:
			if guess < 1 or guess > 10:
				print("\nGuess is outside range.")
			elif guess < answer:
				print("\nIt's higher.")
			elif guess > answer:
				print("\nIt's lower.")
		finally:
			if guess == answer:
				print(f"\nGot it! Attempts: {attempts}")
				while True:
					play_again = input("\nWould you like to play again? Y/N: ")
					if play_again.lower() == 'y':
						scores.append(attempts)
						scores.sort()
						print(f"\n===HIGH SCORE: {scores[0]}===\n")
						start_game()
					elif play_again.lower() == 'n':
						sys.exit("\nAwww... I \"GUESS\" I'll see you later!")
					else:
						print("\nOops! Invalid entry.")		
start_game()

		