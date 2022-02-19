import random

def kameni_noj():
	my_numb = int(input("What you choose? 0 1 2 : "))
	comp_numb = random.randint(0, 2)
	choosed = {0: "Nojniti", 1: "Paper", 2: "Stone"}

	print(f"You choose: {choosed.get(my_numb,'Incorrect number')}")
	print(f"Computer choose: {choosed.get(comp_numb)}")

	if comp_numb == 0 and my_numb == 1:
		print("Computer Win!")
	elif comp_numb == 0 and my_numb == 2:
		print("You Win!")
	elif comp_numb == 1 and my_numb == 0:
		print("You Win!")
	elif comp_numb == 1 and my_numb == 2:
		print("Computer Win!")
	elif comp_numb == 2 and my_numb == 0:
		print("Computer Win!")
	elif comp_numb == 2 and my_numb == 1:
		print("You Win!")
	else:
		print("Nobody Win!")
	kameni_noj()

kameni_noj()