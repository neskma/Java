import csv
import datetime

notes = []

def create_note():
    note_id = len(notes) + 1
    note_name = input("Enter note name: ")
    note_text = input("Enter note text: ")
    note_created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_last_edited_time = note_created_time
    notes.append({"id": note_id, "name": note_name, "text": note_text, 
                  "created_time": note_created_time, "last_edited_time": note_last_edited_time})
    with open("notes.csv", mode="a", newline="", encoding="utf-8") as notes_file:
        writer = csv.writer(notes_file)
        writer.writerow([note_id, note_name, note_text, note_created_time, note_last_edited_time])
    print(f"Note {note_id} created.")

def show_notes():
    with open("notes.csv", mode="r", encoding="utf-8") as notes_file:
        reader = csv.reader(notes_file)
        next(reader) # skip header
        for row in reader:
            note_id, note_name, note_text, note_created_time, note_last_edited_time = row
            note_created_time = datetime.datetime.strptime(note_created_time, "%Y-%m-%d %H:%M:%S")
            note_last_edited_time = datetime.datetime.strptime(note_last_edited_time, "%Y-%m-%d %H:%M:%S")
            if note_created_time > datetime.datetime.now() - datetime.timedelta(days=7): # filter by creation time
                print(f"{note_id} ; {note_name} ; {note_text} ; {note_created_time} ; {note_last_edited_time}")

def view_note():
    note_id = int(input("Enter note ID: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        print(f"{note['name']}\n{note['text']}\nLast edited: {note['last_edited_time']}")
    else:
        print("Note not found.")

def edit_note():
    note_id = int(input("Enter note ID: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        new_text = input("Enter new note text: ")
        note["text"] = new_text
        note["last_edited_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("notes.csv", mode="w", newline="", encoding="utf-8") as notes_file:
            writer = csv.writer(notes_file)
            writer.writerow(["id", "name", "text", "created_time", "last_edited_time"]) # write header
            for note in notes:
                writer.writerow([note["id"], note["name"], note["text"], 
                                  note["created_time"], note["last_edited_time"]])
        print(f"Note {note_id} edited.")
    else:
        print("Note not found.")

def delete_note():
    note_id = int(input("Enter note ID: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        notes.remove(note)
        with open("notes.csv", mode="w", newline="", encoding="utf-8") as notes_file:
            writer = csv.writer(notes_file)
            writer.writerow(["id", "name", "text", "created_time", "last_edited_time"]) # write header
            for note in notes:
                writer.writerow([note["id"], note["name"], note["text"], 
                                  note["created_time"], note["last_edited_time"]])
        print(f"Note {note_id} deleted.")
    else:
        print("Note not found.")

def main():
    # read notes from csv file
    with open("notes.csv", mode="r", encoding="utf-8") as notes_file:
        reader = csv.reader(notes_file)
        next(reader) # skip header
        for row in reader:
            note_id, note_name, note_text, note_created_time, note_last_edited_time = row
            note_created_time = datetime.datetime.strptime(note_created_time, "%Y-%m-%d %H:%M:%S")
            note_last_edited_time = datetime.datetime.strptime(note_last_edited_time, "%Y-%m-%d %H:%M:%S")
            notes.append({"id": int(note_id), "name": note_name, "text": note_text, 
                          "created_time": note_created_time, "last_edited_time": note_last_edited_time})

    while True:
        print("1. Create note")
        print("2. Show notes")
        print("3. View note")
        print("4. Edit note")
        print("5. Delete note")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
