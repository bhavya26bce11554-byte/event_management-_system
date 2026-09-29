# Event Management System - Introduction to Problem Solving and Programming Project

## 📌Overview
This is a Python based desktop application with a simple graphical interface (GUI) for planning and keeping track of events, designed to help users record upcoming meetings, birthdays, workshops and other events without relying on paper diaries or online calendar accounts. The user fills in a small form in a window and clicks buttons to add or delete events, and all events are saved to a local JSON file, so they remain available across sessions without needing an internet connection.

## 📌Features
* Event Scheduling: Record events with a name, date, category, and an optional venue using a simple form.
* Category Selection: Choose a category like Meeting, Birthday, Workshop, Seminar, etc. from a dropdown, or type its number or name in any case (e.g. "meeting" or "MEETING").
* Sorted Table: Events are shown in a table automatically arranged by date so the nearest event is always at the top.
* Past Events Highlight: Events whose date has already passed are shown in grey.
* Persistent Storage: Automatically saves all events to a local JSON file so data isn't lost when the program closes.
* Input Validation: Rejects a blank name, a wrongly formatted date, a past date and an invalid category, with a clear error pop-up.
* Delete Events: Remove cancelled or incorrect events by selecting a row and clicking "Delete Selected" (with a Yes/No confirmation).
* Event Counter: Displays the total number of events and how many are still upcoming.
* Simple GUI: One window with a form, four buttons (Add Event, Delete Selected, Clear Form, Exit) and an event table. Pressing Enter also adds an event.
* Object-Oriented Design: The code is organised into three small classes, each with one job.

## 📌Code Design (Classes)
| Class | What it does |
|---|---|
| `Event` | Stores the details of one event (name, date, category, venue) and turns it into a dictionary for saving or a line of text for display. |
| `EventManager` | Keeps the list of events and handles loading, saving, adding, deleting and counting upcoming events. |
| `EventApp` | Shows the menu, reads the user's input, validates it and prints the results. |

Keeping the data (`Event`, `EventManager`) separate from the menu (`EventApp`) means each part can be understood and changed on its own.

## 📌Technologies/Tools Used
* Programming Language: Python 3.7
* Interface: Graphical User Interface (Tkinter)
* Data Format: JSON (local file storage)
* Standard Library: tkinter, os, datetime, json

## 📌Steps to Install & Run the Project
### 1. *Requirement:*
Make sure that Python is installed on your system. You can check this by running:
```bash
python --version
```
### 2. *Clone/Download the Repository:*
Download the project files to your local machine.
### 3. *Install Dependencies:*
This project only uses Python's standard library, so no extra installation is required.
### 4. *▶️ Run the Application:*
Go to your project directory and run the script:
```bash
python Event_Manager.py
```

## 📌Instructions for Testing
Conduct the following tests to ensure that the application works as anticipated.

### 1. *Standard Entry Test:*
* Run the program. The Event Manager window opens.
* Enter "Tech Fest" as the name and "2026-12-15" as the date.
* Choose "Workshop" from the category dropdown (or type 3 or "workshop"), and enter "Main Auditorium" as the venue.
* Click "Add Event" (or press Enter).
* Expected Output: An "Event added!" pop-up appears, the event is listed in the table and the counter shows "Total Events: 1 | Upcoming: 1".

### 2. *Input Validation Test:*
* Leave the name blank, or type a date like "15/12/2026", or enter a past date, then click "Add Event".
* Expected Output: An error pop-up such as "Please Enter An Event Name", "Please Enter The Date As YYYY-MM-DD" or "Event Date Cannot Be In The Past".
* Type "xyz" in the category box and click "Add Event".
* Expected Output: "Please Choose A Valid Category".
* Click "Delete Selected" without selecting any row.
* Expected Output: "Please Select An Event To Delete".

### 3. *Sorting Test:*
* Add an event for a later date, then one for an earlier date.
* Expected Output: The earlier event is shown above the later one in the table.

### 4. *Persistence Test:*
* Add a few events and click "Exit".
* Run the program again.
* Expected Output: The previously added events are already shown in the table, loaded automatically from events.json.

### 5. *Delete Event Test:*
* Click on an event in the table, then click "Delete Selected" and choose "Yes".
* Expected Output: "Event deleted!" pop-up and the event is removed from the table.

## 📌Project Structure
```
event manager
├── Event_Manager.py
├── events.json   (created automatically on first run)
├── README.md
├── statement.md
└── Report.pdf
```
## 📌Screenshots
1. Adding an event 
<img width="556" height="436" alt="image" src="https://github.com/user-attachments/assets/17daea3a-c864-4d82-8993-17bd77e6126c" />

2. Viewing the event list, sorted by date
<img width="626" height="481" alt="image" src="https://github.com/user-attachments/assets/59cef0a3-a91e-49a4-84b5-f8cd834e381a" />

3. Error messages for a blank name, a wrong date format, a past date and a wrong menu choice
<img width="1083" height="785" alt="image" src="https://github.com/user-attachments/assets/25fa4cda-2a8a-4d71-ac14-43399e97eeda" />

4. Deleting an event
<img width="583" height="417" alt="image" src="https://github.com/user-attachments/assets/f5be97bc-5ffa-4612-bea9-9658786fc84f" />
