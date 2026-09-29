import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

DATA_FILE = "events.json"

categories = ["Meeting", "Birthday", "Workshop", "Seminar", "Party", "Sports", "Other"]

class Event:
    def __init__(self, name, event_date, category, venue):
        self.name = name
        self.date = event_date
        self.category = category
        self.venue = venue

    def to_dict(self):
        return {"name": self.name, "date": self.date, "category": self.category, "venue": self.venue}

    def to_row(self):
        return (self.date, self.name, self.category, self.venue)

class EventManager:
    def __init__(self):
        self.events = []
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                for item in data:
                    self.events.append(Event(item["name"], item["date"], item["category"], item["venue"]))
                self.events.sort(key=lambda e: e.date)
            except Exception:
                self.events = []

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump([event.to_dict() for event in self.events], f, indent=4)

    def add(self, event):
        self.events.append(event)
        self.events.sort(key=lambda e: e.date)
        self.save()

    def delete(self, index):
        self.events.pop(index)
        self.save()

    def upcoming_count(self):
        today = str(date.today())
        return sum(1 for event in self.events if event.date >= today)

class EventApp:
    def __init__(self, root):
        self.manager = EventManager()
        self.root = root
        self.root.title("Event Manager")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.build_form()
        self.build_buttons()
        self.build_list()
        self.refresh_list()

    def build_form(self):
        title = tk.Label(self.root, text="Event Manager", font=("Times New Roman", 20, "bold"))
        title.pack(pady=10)

        form = tk.LabelFrame(self.root, text="Event Details", padx=10, pady=10)
        form.pack(padx=15, fill="x")

        tk.Label(form, text="Event Name:").grid(row=0, column=0, sticky="w", pady=4)
        self.name_entry = tk.Entry(form, width=35)
        self.name_entry.grid(row=0, column=1, sticky="w", pady=4)

        tk.Label(form, text="Date (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", pady=4)
        self.date_entry = tk.Entry(form, width=35)
        self.date_entry.grid(row=1, column=1, sticky="w", pady=4)

        tk.Label(form, text="Category:").grid(row=2, column=0, sticky="w", pady=4)
        self.category_box = ttk.Combobox(form, values=categories, width=32)
        self.category_box.set("Other")
        self.category_box.grid(row=2, column=1, sticky="w", pady=4)

        tk.Label(form, text="Venue (optional):").grid(row=3, column=0, sticky="w", pady=4)
        self.venue_entry = tk.Entry(form, width=35)
        self.venue_entry.grid(row=3, column=1, sticky="w", pady=4)

        self.name_entry.focus()
        self.root.bind("<Return>", lambda e: self.add_event())

    def build_buttons(self):
        buttons = tk.Frame(self.root)
        buttons.pack(pady=10)

        tk.Button(buttons, text="Add Event", width=14, bg="#4CAF50", fg="white",
                  command=self.add_event).grid(row=0, column=0, padx=5)
        tk.Button(buttons, text="Delete Selected", width=14, bg="#E53935", fg="white",
                  command=self.delete_event).grid(row=0, column=1, padx=5)
        tk.Button(buttons, text="Clear Form", width=14,
                  command=self.clear_form).grid(row=0, column=2, padx=5)
        tk.Button(buttons, text="Exit", width=14,
                  command=self.root.destroy).grid(row=0, column=3, padx=5)

    def build_list(self):
        frame = tk.LabelFrame(self.root, text="Scheduled Events", padx=5, pady=5)
        frame.pack(padx=15, fill="both", expand=True)

        columns = ("Date", "Name", "Category", "Venue")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        widths = {"Date": 100, "Name": 220, "Category": 110, "Venue": 200}
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=widths[col])

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.tag_configure("past", foreground="grey")

        self.counter_label = tk.Label(self.root, text="", font=("Times New Roman", 11, "bold"))
        self.counter_label.pack(pady=8)

    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        today = str(date.today())
        for event in self.manager.events:
            tag = "past" if event.date < today else ""
            self.tree.insert("", "end", values=event.to_row(), tags=(tag,))

        total = len(self.manager.events)
        upcoming = self.manager.upcoming_count()
        self.counter_label.config(text=f"Total Events: {total}   |   Upcoming: {upcoming}")

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.venue_entry.delete(0, tk.END)
        self.category_box.set("Other")
        self.name_entry.focus()

    def get_category(self):
        choice = self.category_box.get().strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        for c in categories:
            if c.lower() == choice.lower():
                return c
        return None

    def add_event(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please Enter An Event Name")
            return

        date_text = self.date_entry.get().strip()
        try:
            event_date = datetime.strptime(date_text, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Please Enter The Date As YYYY-MM-DD")
            return

        if event_date < date.today():
            messagebox.showerror("Error", "Event Date Cannot Be In The Past")
            return

        category = self.get_category()
        if category is None:
            messagebox.showerror("Error", "Please Choose A Valid Category")
            return

        venue = self.venue_entry.get().strip()

        self.manager.add(Event(name, str(event_date), category, venue))
        self.refresh_list()
        self.clear_form()
        messagebox.showinfo("Success", "Event added!")

    def delete_event(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please Select An Event To Delete")
            return

        index = self.tree.index(selected[0])
        event = self.manager.events[index]
        if messagebox.askyesno("Confirm", f"Delete '{event.name}' on {event.date}?"):
            self.manager.delete(index)
            self.refresh_list()
            messagebox.showinfo("Success", "Event deleted!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()
