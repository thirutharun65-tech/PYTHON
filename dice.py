def roll_dice(value):
    if 1 <= value <= 6:
        return value
    else:
        print("Invalid dice value! Must be 1–6.")
        return None
def dice_game():
    print("Welcome to Dice Game!")
    while True:
        try:
            player_value = int(input("Enter your dice roll (1–6): "))
            player_roll = roll_dice(player_value)
            if player_roll is None:
                continue
            computer_roll = (player_value % 6) + 1  
            print(f"You rolled: {player_roll}")
            print(f"Computer rolled: {computer_roll}")
            if player_roll > computer_roll:
                print("You win!\n")
            elif player_roll < computer_roll:
                print("Computer wins!\n")
            else:
                print("It's a tie!\n")
            choice = input("Play again? (y/n): ").lower()
            if choice != "y":
                print("Thanks for playing!")
                break
        except ValueError:
            print("Please enter a valid number (1–6).")
dice_game()
