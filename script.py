import random

deck = {"2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5, "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, 
		"9 of Spades": 9, "10 of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10, "Ace of Spades": [1, 11],

		"2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5, "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, 
		"9 of Clubs": 9, "10 of Clubs": 10, "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10, "Ace of Clubs": [1, 11],

		"2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5, "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, 
		"9 of Hearts": 9, "10 of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10, "Ace of Hearts": [1, 11],

		"2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5, "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, 
		"9 of Diamonds": 9, "10 of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10, "Ace of Diamonds": [1, 11]}


def comp_opponent(card_names, card_values, comp_cards, comp_score):
	rand = random.randint(1, len(card_names)+1)
	card = card_names[rand]
	card_value = card_values[rand]
	card_names.remove(card)
	card_values.pop(rand)
	comp_cards.append(card)

	if isinstance(card_value, list):
		comp_score = ace(comp_score, card_value)
	else:
		comp_score += card_value

	return comp_score

def stick(card_names, card_values, player_score):
	comp_cards = []
	comp_score = 0

	while comp_score < 17:
		comp_score = comp_opponent(card_names, card_values, comp_cards, comp_score)

	if comp_score <= 21:
		if player_score > comp_score:
			print("Your oppenent scored " + str(comp_score) + ". You win!")
		elif player_score < comp_score:
			print("Your oppenent scored " + str(comp_score) + ". You lose.")
		else:
			print("You both scored " + str(comp_score) + ". It's a tie!")
	else:
		print("Your oppenent went bust! You win!")

def ace(player_score, *card_values):
	for value in card_values:
		if type(value) == list:
			if player_score + value[1] <= 21:
				player_score += value[1]
			else:
				player_score += value[0]
		else:
			player_score += value
	return player_score
	
def hit(card_names, card_values, player_cards, player_score):
	rand = random.randint(1, len(card_names)+1)

	card = card_names[rand]
	card_value = card_values[rand]

	card_names.remove(card)
	card_values.pop(rand)

	player_cards.append(card)

	if isinstance(card_value, list):
		player_score = ace(player_score, card_value)
	else:
		player_score += card_value

	if player_score > 21:
		print("You have gone bust! You lose!")
		print("")
		answer = input("Would you like to try again? (y/n) - ")
		if answer.lower == "y":
			pass
		else:
			pass
	else:
		msg = "Your cards are: "

		for card in player_cards:
			msg += card + ", "
		new_msg = msg[:-2]

		print(new_msg)
		print("Total score: " + str(player_score))
		print("")
		answer = input("Would you like to hit or stick? - ")
		print("")

		if answer.lower() == "hit":
			hit(card_names, card_values, player_cards, player_score)

		elif answer.lower() == "stick":
			stick(card_names, card_values, player_score)

def draw_2_cards():
	player_cards = []
	player_score = 0

	card_names = list(deck.keys())
	card_values = list(deck.values())

	rand1 = random.randint(0, 52)
	rand2 = random.randint(0, 52)

	card1 = card_names[12]
	card2 = card_names[rand2]

	card_names.remove(card1)
	card_names.remove(card2)

	card1_value = card_values[12]
	card2_value = card_values[rand2]
	
	card_values.pop(rand1)
	card_values.pop(rand2)

	if isinstance(card1_value, list) or isinstance(card2_value, list):
		player_score = ace(player_score, card1_value, card2_value)
	else:
		player_score = card1_value + card2_value

	print("Your cards are: " + card1 + ", " + card2)
	print("Total score: " + str(player_score))
	print("")
	answer = input("Would you like to hit or stick? - ")
	print("")

	if answer.lower() == "hit":
		player_cards.append(card1)
		player_cards.append(card2)
		hit(card_names, card_values, player_cards, player_score)

	elif answer.lower() == "stick":
		stick(card_names, card_values, player_score)


draw_2_cards()