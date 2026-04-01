def get_computer_choice(round_number):
    choices = ["stone", "paper", "scissor"]
    return choices[round_number % 3]  # cycles through choices

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_round(round_number):
    user_choice = input("Enter stone, paper, or scissor: ").lower()
    if user_choice not in ["stone", "paper", "scissor"]:
        return "Invalid choice"
    computer_choice = get_computer_choice(round_number)
    print("Computer chose:", computer_choice)
    return decide_winner(user_choice, computer_choice)

def main():
    round_number = 0
    while True:
        print(play_round(round_number))
        round_number += 1
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            break

main()
