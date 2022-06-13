while True:
    def possible_actions(R, P, S):
        rock = "R"
    scissors = "S"
    paper = "P"
    possible_actions("Rock", "Paper", "Scissors")
    import random

    user_action = input("Enter a choice (R, P, S): ").upper()
    if user_action not in ("R", "P", "S"):
        print ("invalid choice!")
        continue
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"Player ({user_action}), CPU({computer_action}).\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        continue
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    break
