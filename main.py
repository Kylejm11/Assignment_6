# Loads data for both books and movies, returning a dictionary with two keys, 'books' and 'movies', one for
# each subset of the collection.


def load_collections():
    # Load the two collections.
    book_collection, max_book_id = load_collection("books.csv")
    movie_collection, max_movie_id = load_collection("movies.csv")

    # Check for error.
    if book_collection is None or movie_collection is None:
        return None, None

    # Return the composite dictionary.
    return {"books": book_collection, "movies": movie_collection}, max(max_book_id, max_movie_id)


# Loads a single collection and returns the data as a dictionary.  Upon error, None is returned.
def load_collection(file_name):
    max_id = -1
    try:
        # Create an empty collection.
        collection = {}

        # Open the file and read the field names
        collection_file = open(file_name, "r")
        field_names = collection_file.readline().rstrip().split(",")

        # Read the remaining lines, splitting on commas, and creating dictionaries (one for each item)
        for item in collection_file:
            field_values = item.rstrip().split(",")
            collection_item = {}
            for index in range(len(field_values)):
                if (field_names[index] == "Available") or (field_names[index] == "Copies") or (field_names[index] == "ID"):
                    collection_item[field_names[index]] = int(field_values[index])
                else:
                    collection_item[field_names[index]] = field_values[index]
            # Add the full item to the collection.
            collection[collection_item["ID"]] = collection_item
            # Update the max ID value
            max_id = max(max_id, collection_item["ID"])

        # Close the file now that we are done reading all of the lines.
        collection_file.close()

    # Catch IO Errors, with the File Not Found error the primary possible problem to detect.
    except FileNotFoundError:
        print("File not found when attempting to read", file_name)
        return None
    except IOError:
        print("Error in data file when reading", file_name)
        return None

    # Return the collection.
    return collection, max_id


# Display the menu of commands and get user's selection.  Returns a string with  the user's reauexted command.
# No validation is performed.
def prompt_user_with_menu():
    print("\n\n********** Welcome to the Collection Manager. **********")
    print("COMMAND    FUNCTION")
    print("  ci         Check in an item")
    print("  co         Check out an item")
    print("  ab         Add a new book")
    print("  am         Add a new movie")
    print("  db         Display books")
    print("  dm         Display movies")
    print("  qb         Query for books")
    print("  qm         Query for movies")
    print("  x          Exit")
    return input("Please enter a command to proceed: ")

# Print all of the details of a single item (book or movie)
def display_item(item):
    for field_name in item:
        print(f"{field_name}: {item[field_name]}")
    print()


# Searches a collection for items that match the query in the specified fields.
# Returns a list of matching items from search.
def find_matches(collection, query, fields):
    query = query.lower()
    matches = []
    for item_id in sorted(collection):
        item = collection[item_id]
        for field in fields:
            if query in str(item.get(field, "")).lower():
                matches.append(item)
                break
    return matches

# Prompts the user for a query, searches, and displays details for matching items.
def query_collection(collection, fields, item_type):
    query = input("Enter a query string to use for the search: ")
    matches = find_matches(collection, query, fields)
    if len(matches) == 0:
        print(f" No {item_type} matched the query.")
    else:
        for item in matches:
            display_item(item)

# Looks up an item by its ID, returns the item or none if there was no match.
def find_item_by_id(library_collections, item_id):
    for collection in library_collections.values():
        if item_id in collection:
            return collection[item_id]
    return None

# Prompts user for an ID and returns it as an integer or None.
def prompt_for_id(action):
    text = input(f"Enter the ID for the item you wish to {action}: ")
    try:
        return int(text.strip())
    except ValueError:
        return None


# Checks out an item (decreasing availability accordingly) if it exists and is available.
def check_out(library_collections):
    item_id = prompt_for_id("check out")
    item = None if item_id is None else find_item_by_id(library_collections, item_id)
    if item is None:
        print("There is no item with that ID number.")
    elif item["Available"] <= 0:
        print("There are no copies of this item available, so it can not be checked out.")
    else:
        item["Available"] -= 1
        print(f"You have checked out {item['Title']}.")

# Checks in an item (increasing availability accordingly) if it exists and is not already checked in.
def check_in(library_collections):
    item_id = prompt_for_id("check in")
    item = None if item_id is None else find_item_by_id(library_collections, item_id)
    if item is None:
        print("There is no item with that ID number.")
    elif item["Available"] >= item["Copies"]:
        print("All copies are already available, so this item can not be checked in.")
    else:
        item["Available"] += 1
        print(f"You have checked in {item['Title']}.")

# Displays all items in a collection 10 at a time, prompting the user to press Enter to continue or 'm' to return to the menu.
def display_collection(collection):
    item_ids = sorted(collection)
    for position in range(len(item_ids)):
        display_item(collection[item_ids[position]])
        # Display every group of ten (unless that was the last item), ask whether to continue.
        if (position + 1) % 10 == 0 and position + 1 < len(item_ids):
            response = input("Press Enter to show more items, or type 'm' to return to the menu: ")
            if response.strip().lower() == "m":
                return

def add_item(collection, max_existing_id, item_type):
    if len(collection) == 0:
        print(f"The {item_type} collection is empty.")
        return max_existing_id

    # Use the field names and order of an existing item at a template for a new item
    field_names = list(next(iter(collection.values())).keys())
    new_id = max_existing_id + 1
    new_item = {}
    for field in field_names:
        if field == "ID":
            new_item[field] = new_id
        elif field == "Copies" or field == "Available":
            new_item[field] = 1
        else:
            value = input(f"Enter the {field.lower()}: ")
            # Pages and Year must be integers, so keep asking until a valid value is entered.
            while field in ("Pages", "Year") and not value.strip().isdigit():
                value = input(f"Enter a whole number for the {field.lower()}: ")
            # remove commas
            new_item[field] = value.replace(",", "").strip()

    collection[new_id] = new_item
    print(f"{new_item['Title']} has been added to the {item_type} collection.")
    return new_id



# This is the main program function.  It runs the main loop which prompts the user and performs the requested actions.
def main():
    # Load the collections, and check for an error.
    library_collections, max_existing_id = load_collections()

    if library_collections is None:
        print("The collections could not be loaded. Exiting.")
        return

    # No error, so print out a success message with the number of items.
    total_item_count = len(library_collections['books']) + len(library_collections['movies'])
    print(f"The collections have loaded successfully with {total_item_count} items. ")

    # Display the error and get the operation code entered by the user.  We perform this continuously until the
    # user enters "x" to exit the program.  Calls the appropriate function that corresponds to the requested operation.
    operation = prompt_user_with_menu()
    while operation != "x":
        if operation == "ci":
            check_in(library_collections)
        elif operation == "co":
            check_out(library_collections)
        elif operation == "ab":
            max_existing_id = add_item(library_collections["books"], max_existing_id, "book")
        elif operation == "am":
            max_existing_id = add_item(library_collections["movies"], max_existing_id, "movie")
        elif operation == "db":
            display_collection(library_collections["books"])
        elif operation == "dm":
            display_collection(library_collections["movies"])
        elif operation == "qb":
            query_collection(library_collections["books"], ["Title", "Author", "Publisher"], "books")
        elif operation == "qm":
            query_collection(library_collections["movies"], ["Title", "Director", "Genre"], "movies")
        else:
            print("Unknown command.  Please try again.")

        operation = prompt_user_with_menu()


# Kick off the execution of the program.
main()


