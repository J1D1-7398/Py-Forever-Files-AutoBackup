# Py Forever Files (Python AutoBackup)
A python program that automatically backs up files and folders to an external drive. Useful when needing periodical backups of important files or folders
## Requirements
- Python (I have coded and tested it on python 3.14.8)
Libraries:
- subprocess
- os
- threading
- datetime
- time
- shutil
All of them should come with default python installation, but check, just in case

## How to install
1. Clone this repo onto your computer with:
```
git clone https://github.com/J1D1-7398/Py-Forever-Files-AutoBackup.git
```
Or download the zip file by clicking the green "<> Code" button and pressing "Download ZIP"
For Windows, you can download the .exe in releases as well, but we'll talk about it later

2. If you have downloaded the .zip file, extract it.
3. To run the program, just enter into the "Code" folder in the terminal and execute:
```
python PyFileBackup.py
```
Or, on Windows, you can just double click the .py file IF you have it run in python automatically, you can select "Open With" and select python
If you have downloaded the .exe in releases, just double click it

## How to use
The program will generate two files (.txt and .log) after it is first started. The .txt will store all tasks, while the .log file is used for the logs so you know what went wrong or if your files are being backed up
After having started the code, navigate through the program by typing a number, then pressing enter
At first you will have 8 options:
1. View a task
2. Create a task
3. Edit a task
4. Delete a task
5. Run tasks
6. Stop tasks
7. Clear screen/Refresh tasks
8. Exit

### 1. View a task
You will be prompted to select a task
If you have no tasks, only the cancel option will appear
If you do have tasks already registered, it will display all tasks plus the cancel option
Select cancel to return to main menu or select a task to view its contents:
It will display:
Task Name:
   Name of you task
Backup location:
   Location where your files will be stored
Files to backup:
   The files that will be backed up by the program to Backup Location
Time between backups:
   The time between backups, represented as xy where x is a number and y is d, h or m (day, hour, minute)

### 2. Create a task
You will be prompted to enter a name for your task, a backup location, files to be backed up (it will ask for confirmation y/n (yes/no)) and time between backups
Important! You can enter various files and even folders to be backed up, but no file nor folder must have any space in the path or else the program will break!

### 3. Edit a task
You will be prompted to select a task to edit, again, if you have no tasks, only the Cancel option will appear
Select cancel to return to main menu or select a task to edit its contents:
It will ask what part of the task you want to change:
1. Task Name
2. Backup location
3. Files to backup
4. Time between backups
It will be the same as the task creation part except it is just to modify a part of the task

### 4. Delete a task
You will be prompted to select a task to delete or the cancel option
When you select a task to delete it will prompt for confirmation, so no worries if you accidentally type the wrong number

### 5. Run tasks
Runs all tasks, it will start them with a one second delay

### 6. Stop tasks
Stops all active tasks, it will take up to 30 seconds to stop, be patient!

### 7. Clear screen/Refresh tasks
Clears the screen and refreshes its list of tasks in case you have changed some things directly from the file

### 8. Exit
Exits the program, on windows, if you have opened it with double click, you will need to close the window manually AFTER exiting


## Why should you use this?
If you have a lot of important files you don't want to lose, but at the same time, you work on them quite often, you must know it is very tedious having to back up everything, all the time manually
So I offer to you this solution, this program will back up automatically all the files and folders you ask it to back up, with flexible time between backups, from 1 minute (min) (not recommended, but do whatever you want), to lots of days (max) (there should be no max days except for 32 bit limit)

## Why did I build this?
I work all the time coding on projects that I need to ensure to back up, but I find it tedious having to select files from all over the computer to transfer them to an external drive, so I built this tool to help me back up my files


Everything should work correctly!

If you have any questions, feel free to send me an e-mail or post an issue on this repo!

J1D1.7398@gmail.com
