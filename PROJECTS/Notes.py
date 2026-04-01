def create_note(filename):
    note = input("Enter your note: ")
    with open(filename, "a") as f:
        f.write(note + "\n")
    print("Note saved successfully!\n")
def read_notes(filename):
    try:
        with open(filename, "r") as f:
            notes = f.readlines()
        if notes:
            print("\n--- Saved Notes ---")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
            print("-------------------\n")
        else:
            print("No notes found.\n")
    except FileNotFoundError:
        print("Notes file not found. Create a note first!\n")
def main():
    filename = "notes.txt"
    while True:
        print("File-based Notes Saver")
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            create_note(filename)
        elif choice == "2":
            read_notes(filename)
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
if __name__ == "__main__":
    main()
