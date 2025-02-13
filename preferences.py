import json
import main
import time


PREFERENCES_FILE = "user_preferences.json"  

def load_all_preferences():
    with open(PREFERENCES_FILE, "r") as f:
        return json.load(f)
    return {}

def save_all_preferences(preferences):
    with open(PREFERENCES_FILE, "w") as f:
        json.dump(preferences, f, indent=4)

def get_user_preferences(username):
    all_preferences = load_all_preferences()
    return all_preferences.get(username)

def edit_preferences(username):
    """Allows the user to edit their preferences."""
    print("\n===== Edit Preferences =====")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    all_preferences = load_all_preferences()
    all_preferences[username] = {"name": name, "age": age, "email": email}

    save_all_preferences(all_preferences)
    print("\n✅ Preferences updated successfully!")
    time.sleep(1.5)

def reset_preferences(username):
    all_preferences = load_all_preferences()

    if username in all_preferences:
        del all_preferences[username]
        save_all_preferences(all_preferences)
        print("\n⚠️ Your preferences have been reset.")
        time.sleep(1)
    else:
        print("\n❌ No preferences found to reset.")
        time.sleep(1)

def display_preferences(username):
    print("Retrieving preferences...")
    time.sleep(2)
    user_prefs = get_user_preferences(username)

    print("\n" + "=" * 50)
    print(f" Preferences for {username} ")
    print("=" * 50)

    if user_prefs:
        print(f"\nYour current preferences:")
        print(f"- Name: {user_prefs['name']}")
        print(f"- Age: {user_prefs['age']}")
        print(f"- Email: {user_prefs['email']}")
    else:
        print("\n🚫 No preferences found. You need to set them first.")

    print("\n[1] Edit Preferences")
    print("[2] Reset Preferences (Warning: All saved data will be lost)")
    print("[3] Go Back to Home Page")

    choice = input("\nType the number corresponding to your choice:\n> ")
    while (choice != '1' and choice != '2' and choice !='3'):
        choice = input("Invalid choice! Please enter 1, 2, or 3 (to go back to the home page)")
    if choice == "1":
        edit_preferences(username)
        main.home_page(username)
        return
    elif choice == "2":
        reset_preferences(username)
        main.home_page(username)
        return
    elif choice == "3":
        print("\n🔙 Returning to Home Page...")
        time.sleep(1.5)
        main.home_page(username)
        return




