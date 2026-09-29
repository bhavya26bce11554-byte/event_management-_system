## 📌Problem Statement
Keeping track of upcoming events is a common challenge, whether it is a college seminar, a club meeting, a friend's birthday or a workshop.
Without a simple recording system, events are noted in scattered places (chats, notebooks, sticky notes) and are easily forgotten or double-booked.
Many existing calendar tools require online accounts and syncing, which is more than users need when they just want a simple local list of their events.

## 📌Scope of the Project
This project aims to develop an Event Management System, a simple desktop application with a graphical user interface built using Tkinter.
It bridges the gap between messy manual tracking and heavy online calendar or event platforms.

The scope includes:
* Local Data Storage: Using a local JSON file to persist event records without requiring internet access or external accounts.
* Data Processing: Logic to categorize events, validate names and dates, sort events by date, and count upcoming events.
* Graphical Interface: A single window with a form, buttons and an event table, so users do not need to type commands in a terminal.
* Object-Oriented Structure: The program is split into three classes (Event, EventManager, EventApp) that separate the data, the storage logic and the user interface.
* Resilience: The application handles a missing or empty data file gracefully and rejects invalid input with an error pop-up before it is saved.

## 📌Target Users
* Students: Users who want to keep track of exams, fests, seminars and club activities.
* Club / Society Coordinators: People who organise small events and need a quick list of what is coming up.
* Working Professionals: Users who want a simple offline record of meetings and workshops.
* General Users: Anyone who wants an easy way to remember birthdays, parties and personal events.

## 📌High-Level Features
* Event Recording: Add events with name, date, category and venue through an easy form.
* Smart Input Validation: Refuses blank names, badly formatted dates, past dates and invalid categories, preventing bad data and crashes.
* Automatic Sorting: Events are always listed in date order in a table.
* Visual Status: Past events are shown in grey, and a live counter shows total and upcoming events.
* Persistent Local Storage: Events are saved automatically to a JSON file and reloaded the next time the app is launched.
* Simple GUI: One window with Add, Delete, Clear and Exit buttons, built with Tkinter from Python's standard library, so no extra libraries are needed.