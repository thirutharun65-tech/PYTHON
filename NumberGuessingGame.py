print("=== Number Guessing Game ===")
print("Level 1: Guess the number between 1 and 10")
secret_number1 = 4

g1 = int(input("Chance 1: "))
if g1 == secret_number1:
    print("You Win Level 1 on Chance 1!")
else:
    g2 = int(input("Chance 2: "))
    if g2 == secret_number1:
        print("You Win Level 1 on Chance 2!")
    else:
        g3 = int(input("Chance 3: "))
        if g3 == secret_number1:
            print("You Win Level 1 on Chance 3!")
        else:
            print("Game Over for Level 1! The number was", secret_number1)

print("Level 2: Guess the number between 1 and 20")
secret_number2 = 15

h1 = int(input("Chance 1: "))
if h1 == secret_number2:
    print("You Win Level 2 on Chance 1!")
else:
    h2 = int(input("Chance 2: "))
    if h2 == secret_number2:
        print("You Win Level 2 on Chance 2!")
    else:
        h3 = int(input("Chance 3: "))
        if h3 == secret_number2:
            print("You Win Level 2 on Chance 3!")
        else:
            print("Game Over for Level 2! The number was", secret_number2)

print("Level 3: Guess the number between 1 and 50")
secret_number3 = 27

k1 = int(input("Chance 1: "))
if k1 == secret_number3:
    print("You Win Level 3 on Chance 1!")
else:
    k2 = int(input("Chance 2: "))
    if k2 == secret_number3:
        print("You Win Level 3 on Chance 2!")
    else:
        k3 = int(input("Chance 3: "))
        if k3 == secret_number3:
            print("You Win Level 3 on Chance 3!")
        else:
            print("Game Over for Level 3! The number was", secret_number3)
