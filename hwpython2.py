import json
import csv
import os
import datetime
import argparse

notes_file = 'notes.json'  # Change this to 'notes.csv' for CSV format

def add_note():
    title = input('Enter note title: ')
    body = input('Enter note body: ')
    note = {
        'id': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        'title': title,
        'body': body,
        'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'modified': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print('Note saved successfully')

def list_notes():
    notes = load_notes()
    notes.sort(key=lambda n: n['modified'], reverse=True)
    print('{:<20} {:<20} {:<20}'.format('ID', 'Title', 'Modified'))
    for note in notes:
        print('{:<20} {:<20} {:<20}'.format(note['id'], note['title'], note['modified']))

def edit_note():
    notes = load_notes()
    id = input('Enter note ID to edit: ')
    note = next((n for n in notes if n['id'] == id), None)
    if note is None:
        print('Note not found')
        return
    title = input('Enter new note title (empty to keep current): ')
    if title.strip() != '':
        note['title'] = title
    body = input('Enter new note body (empty to keep current): ')
    if body.strip() != '':
        note['body'] = body
    note['modified'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_notes(notes)
    print('Note updated successfully')

def delete_note():
    notes = load_notes()
    id = input('Enter note ID to delete: ')
    notes = [n for n in notes if n['id'] != id]
    save_notes(notes)
    print('Note deleted successfully')

def load_notes():
    if not os.path.isfile(notes_file):
        return []
    with open(notes_file, 'r') as f:
        if notes_file.endswith('.json'):
            return json.load(f)
        elif notes_file.endswith('.csv'):
            reader = csv.DictReader(f)
            return [dict(row) for row in reader]
        else:
            raise ValueError('Invalid file format: {}'.format(notes_file))

def save_notes(notes):
    with open(notes_file, 'w') as f:
        if notes_file.endswith('.json'):
            json.dump(notes, f, indent=2)
        elif notes_file.endswith('.csv'):
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body', 'created', 'modified'])
            writer.writeheader()
            writer.writerows(notes)
        else:
            raise ValueError('Invalid file format: {}'.format(notes_file))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Note taking program')
    parser.add_argument('command', help='add, list, edit, or delete')
    parser.add_argument('-d', '--date', help='filter by date (YYYY-MM-DD)')
    args = parser.parse_args()

    if args.command == 'add':
        add_note()
    elif args.command == 'list':
        list_notes()
    elif args.command == 'edit':
        edit_note()
    elif args.command ==
