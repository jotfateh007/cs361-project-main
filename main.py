import login as l
import accountCreation as ac
import messageGeneration as mg
import messageLogging as ml
import preferences
import sendEmail as se


def home_page(username):
    print(f"\nWelcome back, {username}!")
    print("Here you can access motivational messages and more!\n")
    print("[1] Set Preferences")
    print("[2] Download User History")
    print("[3] Send Motivational Email")
    print("[4] Generate a Motivational Message")
    print("[5] Logout")

    choice = input("\nChoose an option: ")

    if choice == "1":
        preferences.display_preferences(username)
    elif choice == "2":
        ml.download_user_history(username)
    elif choice == "3":
        se.sendEmail(username)
    elif choice == "4":
        mg.generateMessage(username)
    elif choice == "5":
        print("\nLogging out... Returning to the main menu.\n")
        main()
    else:
        print("\nInvalid choice. Try again.\n")
        home_page(username)





def display_menu():
    print("=" * 50)
    print("Welcome to Hype-It-Up!")
    print("=" * 50)
    print("\nThis is a motivational message generation to program to make you feel better.\n")
    print("\n Please choose one of the following options:\n")
    print("[1] Login")
    print("[2] Register")
    print("[3] Exit\n")
    choice = input("Type the number corresponding to your choice:\n> ")
    return choice

def main():
    choice = display_menu()
    if choice == "1":
        print("\nYou selected Login.\n")
        username = l.login_screen()
        if username:
            home_page(username)
    elif choice == "2":
        print("\nYou selected Register.\n")
        username = ac.createAccount('')
        if username:
            home_page(username)
    elif choice == "3":
        print("\nExiting... Goodbye!\n")
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.\n")
        choice = display_menu()

if __name__ == "__main__":
    main()
