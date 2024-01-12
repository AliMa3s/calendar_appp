import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk, simpledialog
import datetime
from database import add_note, get_notes, delete_note

def show_notes_for_date(date):
    notes = get_notes(date)
    note_text.delete('1.0', tk.END)
    for note in notes:
        note_text.insert(tk.END, note[1] + '\n\n')

def prompt_for_note(date):
    note = simpledialog.askstring("New Note", "Enter note for " + date)
    if note:
        add_note(date, note)
        show_notes_for_date(date)

def delete_selected_note():
    if selected_date.get():
        delete_note(selected_date.get())
        show_notes_for_date(selected_date.get())

app = tk.Tk()
app.title("Advanced Calendar and Notes App")
app.geometry('800x600')

# Styling
style = ttk.Style(app)
style.theme_use('clam')

# Configure grid layout
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

# Calendar widget
cal_frame = ttk.Frame(app)
cal_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
cal = Calendar(cal_frame, selectmode='day')
cal.pack()

# Note display area
note_frame = tk.Frame(app)
note_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
note_text = tk.Text(note_frame, height=20, width=40)
note_text.pack()

# Delete Note Button
delete_button = tk.Button(app, text="Delete Note", command=delete_selected_note)
delete_button.grid(row=1, column=0, padx=10, pady=10)

selected_date = tk.StringVar()

def date_changed(event):
    selected_date.set(cal.get_date())
    show_notes_for_date(selected_date.get())
    prompt_for_note(selected_date.get())  # Prompt for note on date selection

# Bind the calendar date change event
cal.bind("<<CalendarSelected>>", date_changed)

# Load notes for current date on start
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
selected_date.set(current_date)
show_notes_for_date(current_date)

app.mainloop()
