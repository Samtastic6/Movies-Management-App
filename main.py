import db_manager as mm
import ui_manager as ui


def main():
    mm.initialize_db()
    print("Welcome to the Movie Manager App!")
    while True:
        print("\nOptions:")
        print("Press 'C' to create a new movie entry")
        print("Press 'S' to search for a movie by title")
        print("Press 'Q' to quit")
        choice = input("Enter your choice: ").strip().upper()

        if choice == 'C':
            ui.create_movie()
        elif choice == 'S':
            ui.search_movie()
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()