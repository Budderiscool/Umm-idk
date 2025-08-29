import sys

def tic_tac_toe():
    print("Launching Tic-Tac-Toe...")
    # [Game logic here]
    input("Press Enter to return to menu.")

def guess_the_number():
    print("Launching Guess the Number...")
    # [Game logic here]
    input("Press Enter to return to menu.")

def rock_paper_scissors():
    print("Launching Rock-Paper-Scissors...")
    # [Game logic here]
    input("Press Enter to return to menu.")

def main_menu():
    games = {
        "1": ("Tic-Tac-Toe", tic_tac_toe),
        "2": ("Guess the Number", guess_the_number),
        "3": ("Rock-Paper-Scissors", rock_paper_scissors),
        "0": ("Exit", sys.exit)
    }
    while True:
        print("\nChoose a game to play:")
        for key, (title, _) in games.items():
            print(f"{key}. {title}")
        choice = input("Enter your choice: ")
        if choice in games:
            games[choice][1]()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()