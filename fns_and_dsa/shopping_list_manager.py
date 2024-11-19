MENU_TITLE = "Shopping List Manager"

def display_menu():
    """
    Display the shopping list menu options.
    """
    print(f"\n{MENU_TITLE}")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """
    Main function to manage the shopping list.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
            else:

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
            else:
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
