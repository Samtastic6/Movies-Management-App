import db_manager as mm
def create_movie():
    title = input("Enter the movie title: ")
    language = input("Enter the movie language (optional): ") or None
    watched = input("Have you watched this movie at least once? (yes/no): ").strip().lower() == 'yes'
    rating = input("Enter your star rating (1-5, optional): ") or None
    if rating:
        rating = int(rating)
    notes = input("Enter any notes (optional): ") or None
    
    result = mm.add_movie(title, language, watched, rating, notes)
    print(result)

def search_movie():
    title_part = input("Enter any part of the movie title to search for: ")
    search_notes = input("Do you want to search in notes also? (yes/no): ").strip().lower() == 'yes'
    
    results = mm.search_movies_by_title(title_part, search_notes)
    if not results:
        print("No movies found.")
        return
    
    print("\nSearch Results:")
    for movie in results:
        print_movie_details(movie)
        print("Options:")
        print("Press 'E' to edit this movie")
        print("Press 'D' to delete this movie")
        print("Press 'N' to search again")
        print("Press 'H' to go back to Home screen")
        option = input("Enter your choice: ").strip().upper()
        
        if option == 'E':
            edit_movie(movie[0])
        elif option == 'D':
            delete_movie(movie[0])
        elif option == 'N':
            search_movie()
            return
        elif option == 'H':
            return
        else:
            print("Invalid choice. Returning to Home screen.")
            return

def edit_movie(movie_id):
    title = input("Enter the new title (leave blank to keep current): ") or None
    language = input("Enter the new language (leave blank to keep current): ") or None
    watched = input("Have you watched this movie at least once? (yes/no, leave blank to keep current): ").strip().lower() or None
    if watched:
        watched = watched == 'yes'
    rating = input("Enter the new star rating (1-5, leave blank to keep current): ") or None
    if rating:
        rating = int(rating)
    notes = input("Enter the new notes (leave blank to keep current): ") or None
    
    result = mm.edit_movie(movie_id, title, language, watched, rating, notes)
    print(result)

def delete_movie(movie_id):
    confirm = input("Are you sure you want to delete this movie? (yes/no): ").strip().lower()
    if confirm == 'yes':
        result = mm.delete_movie(movie_id)
        print(result)
    else:
        print("Deletion cancelled.")

def print_movie_details(movie):
    print(f"\nID: {movie[0]}")
    print(f"Title: {movie[1]}")
    print(f"Language: {movie[2]}")
    print(f"Watched: {'Yes' if movie[3] else 'No'}")
    print(f"Rating: {movie[4]}")
    print(f"Notes: {movie[5]}")