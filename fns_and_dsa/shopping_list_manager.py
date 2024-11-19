MENU_OPTIONS = [
    "Shopping List Manager",
    "1. Add Item",
    "2. Remove Item",
    "3. View List",
    "4. Exit"
]

def generate_menu():
    """
    Generate the menu as a single string to display.
    """
    return "\n".join(MENU_OPTIONS)

def display_output(messages):
    """
    A function to display messages.
    Emulates the output functionality without using print().
    """
    import sys
    sys.stdout.write("\n".join(messages) + "\n")

def main():
    """
    Main function to manage the shopping list.
    """
    shopping_list = []

    while True:
        # Display the menu
        display_output([generate_menu()])
        choice = input("Enter your choice: ").strip()

        messages = []

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            messages.append(f'"{item}" has been added to the shopping list.')

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                messages.append(f'"{item}" has been removed from the shopping list.')
            else:
                messages.append(f'"{item}" is not in the shopping list.')

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                messages.append("Current Shopping List:")
                messages.extend(f"{index + 1}. {item}" for index, item in enumerate(shopping_list))
            else:
                messages.append("Your shopping list is empty.")

        elif choice == '4':
            # Exit the program
            messages.append("Goodbye!")
            display_output(messages)
            break

        else:
            messages.append("Invalid choice. Please try again.")

        # Display the accumulated messages
        display_output(messages)


if __name__ == "__main__":
    main()
