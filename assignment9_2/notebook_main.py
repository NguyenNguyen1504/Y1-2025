from notebook import Notebook

def main():
    restaurant_reviews = Notebook("Restaurant reviews")
    restaurant_reviews.add_or_update_note("Foodies", "The food was great, and the service was excellent. Rating: 10/10")
    restaurant_reviews.add_or_update_note("Ham & Burger", "Great location, but undercooked food. Wouldn't go again. Rating: 3/10")
    name2 = input("What is the name of notebook 2?")
    book2 = Notebook(name2)
    name3 = input("What is the name of notebook 3?")
    book3 = Notebook(name3)
    for notebook in [book2, book3]:
        for i in range(2):
            print(f"Add new note to {notebook.get_name()}:")
            title_str = input("Title:\n")
            body_str = input("Body:\n")
            notebook.add_or_update_note(title_str, body_str)
    name_str = input("Which note to delete from notebook 2?\n")
    if book2.delete_note(name_str):
        print("Successfully deleted the note from notebook 2!")
    else:
        print("The note could not be deleted from notebook 2.")
    search_str = input("Search by body from notebook 1:\n")
    results = restaurant_reviews.search_by_body(search_str)
    if len(results) == 0:
        print("Could not find notes containing the search term.")
    else:
        print("Found the following notes containing the search term:")
        for result in results:
            print(result)
    search_str = input("Print a note from notebook 1 with the title:\n")
    note_str = restaurant_reviews.get_note_str(search_str)
    if note_str == "":
        print("Could not find that note.")
    else:
        print(note_str)
    print("Deleting all notes from notebook 3...")
    book3.delete_all_notes()
    print("Printing all notebooks:")
    print(restaurant_reviews)
    print(book2)
    print(book3)


main()

