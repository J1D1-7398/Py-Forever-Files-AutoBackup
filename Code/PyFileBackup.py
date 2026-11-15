import subprocess, os, threading, datetime, time, shutil
try:
    with open("backuptasks.txt", "a") as ensure_availability_of_tasklist:
        ensure_availability_of_tasklist.write("")
    with open("application.log", "a") as write_log:
        write_log.write(f"\n{time.ctime()}, General: Creating functions\n{time.ctime()}, General: Creating necessary files\n")
    def backup_execution(*backup_execution_info):
        try:
            print(" Started task", backup_execution_info[0])
            with open("application.log", "a") as write_log:
                write_log.write(f"{time.ctime()}, Thread {backup_execution_info[0]}: Started\n")
            files_backed_up = ""
            for i in backup_execution_info[2].split(","):
                files_backed_up += " "+i.removeprefix("\"").removesuffix("\"")
            while True:
                if stop_all_tasks != True:
                    if backup_execution_info[3][-1] == "d":
                        time_between_backups = int(backup_execution_info[3][:-1]) * 2880
                    elif backup_execution_info[3][-1] == "h":
                        time_between_backups = int(backup_execution_info[3][:-1]) * 120
                    elif backup_execution_info[3][-1] == "m":
                        time_between_backups = int(backup_execution_info[3][:-1]) * 2
                    try:
                        if os.path.exists(backup_execution_info[1]):
                            create_backup_path = backup_execution_info[1]+"/Backup-"+backup_execution_info[0]+"-"+time.ctime().split()[3].replace(":", "")+"-"+datetime.date.today().strftime("%d/%m/%y").replace("/", "")
                            os.mkdir(create_backup_path)
                            for i in backup_execution_info[2].split(","):
                                if os.path.isdir(i.removeprefix("\"").removesuffix("\"")):
                                    os.mkdir(create_backup_path+"/"+(i.removeprefix("\"").removesuffix("\"")).rsplit("/", 1)[1])
                                    shutil.copytree(i.removeprefix("\"").removesuffix("\""), create_backup_path+"/"+(i.removeprefix("\"").removesuffix("\"")).rsplit("/", 1)[1], dirs_exist_ok=True)
                                elif os.path.isfile(i.removeprefix("\"").removesuffix("\"")):
                                    shutil.copy(i.removeprefix("\"").removesuffix("\""), create_backup_path)
                            with open("application.log", "a") as write_log:
                                write_log.write(f"{time.ctime()}, Thread {backup_execution_info[0]}: Backed up{files_backed_up} in {backup_execution_info[1]}\n")
                        else:
                            with open("application.log", "a") as write_log:
                                write_log.write(f"{time.ctime()}, Thread {backup_execution_info[0]}: Failed to back up{files_backed_up} in {backup_execution_info[1]} due to the backup path being inexistent\n")
                    except Exception as ex:
                        with open("application.log", "a") as write_log:
                            write_log.write(f"{time.ctime()}, Thread {backup_execution_info[0]}: Error! Failed to back up{files_backed_up} in {backup_execution_info[1]} Error: {ex}\n")
                    for i in range(time_between_backups):
                        time.sleep(30)
                        if stop_all_tasks == True:
                            break
                else:
                    print(" Stopped", backup_execution_info[0])
                    with open("application.log", "a") as write_log:
                        write_log.write(f"{time.ctime()}, Thread {backup_execution_info[0]}: Stopped\n")
                    break
        except Exception as e:
            print(f" Thread Error! {e}")
            with open("application.log", "a") as write_log:
                write_log.write(f"{time.ctime()}, Thread {backup_execution_info[0]}: Error! {e}\n")
    with open("application.log", "a") as write_log:
        write_log.write(f"{time.ctime()}, General: Starting program\n")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    while True:
        print("\n ███████╗ █████╗ ██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗██╗██╗     ███████╗ ██████╗\n ██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██║██║     ██╔════╝██╔════╝\n █████╗  ██║  ██║██████╔╝█████╗  ╚██╗ ██╔╝█████╗  ██████╔╝█████╗  ██║██║     █████╗  ╚█████╗\n ██╔══╝  ██║  ██║██╔══██╗██╔══╝   ╚████╔╝ ██╔══╝  ██╔══██╗██╔══╝  ██║██║     ██╔══╝   ╚═══██╗\n ██║     ╚█████╔╝██║  ██║███████╗  ╚██╔╝  ███████╗██║  ██║██║     ██║███████╗███████╗██████╔╝\n ╚═╝      ╚════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═════╝")
        tasks = []
        with open("application.log", "a") as write_log:
            write_log.write(f"{time.ctime()}, General: Parsing tasks file\n")
        with open("backuptasks.txt", "r") as read_backup_tasks:
            for line in read_backup_tasks:
                if not line.startswith("###"):
                    task_build = []
                    for i in range(8):
                        if i % 2 == 1:
                            task_build.append(line.replace("\n", "").split()[i].removeprefix("\"").removesuffix("\",") if line.replace("\n", "").split()[i].removeprefix("\"").endswith("\",") else line.replace("\n", "").split()[i].removeprefix("\"").removesuffix("\""))
                    tasks.append(task_build)
        print("\n Backup Tasks:\n")
        for i in tasks:
            print(" "+i[0])
        main_menu_selection = input("\n Select an option:\n 1. View a task\n 2. Create a task\n 3. Edit a task\n 4. Delete a task\n 5. Run tasks\n 6. Stop tasks\n 7. Clear screen/Refresh tasks\n 8. Exit\n > ")
        if main_menu_selection == "1":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("\n TASK VIEW\n\n Select a task to view:\n")
            x = 1
            for i in tasks:
                print(f" {x}. {i[0]}")
                x += 1
            print(f" {x}. Cancel")
            task_to_view = input(" > ")
            if task_to_view != str(x):
                print(f"\n Task Name:\n   {tasks[int(task_to_view) - 1][0]}\n Backup location:\n   {tasks[int(task_to_view) - 1][1]}\n Files to backup:")
                for i in tasks[int(task_to_view) - 1][2].split(","):
                    print("   "+i.removeprefix("\"").removesuffix("\""))
                print(f" Time between backups:\n   {tasks[int(task_to_view) - 1][3]}")
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Viewing task {tasks[int(task_to_view) - 1][0]}\n")
                input("\n Press Enter to return to main menu...")
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        elif main_menu_selection == "2":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            create_task_name = input("\n TASK CREATION\n\n Enter task name: ")
            if " " in create_task_name:
                print(" Spaces have been replaced with \"-\" as spaces are not allowed")
                create_task_name = create_task_name.replace(" ", "-")
            create_task_backup_location = input(" Enter backup folder location: ")
            while os.path.exists(create_task_backup_location) == False:
                create_task_backup_location = input(" Please enter a valid path!\n Enter backup folder location: ")
            ctftb_isok = "n"
            while ctftb_isok == "n":
                ctftb_path_isok = False
                while ctftb_path_isok == False:
                    create_task_files_to_backup = input(" Enter files to backup (Spaced): ")
                    ctftb_path_isok = True
                    for i in create_task_files_to_backup.split():
                        if os.path.exists(i) == False:
                            ctftb_path_isok = False
                    if ctftb_path_isok == False:
                        print(f" Please check you have entered a valid path! (No spaces in the path)")
                print(" File selection to be backed up:")
                task_files_to_backup_write = ""
                for i in create_task_files_to_backup.split():
                    print("   "+i)
                    task_files_to_backup_write += f"\"{i}\","
                ctftb_isok = input(" Is this selection correct? (y/n): ")
            create_task_time_between_backups = input(" Enter time between backups (d/h/m): ")
            while create_task_time_between_backups[-1] not in "dhm" or create_task_time_between_backups[:-1].isdigit() == False:
                create_task_time_between_backups = input(" Ensure correct format! xy where x is a number and y is d,h or m (day, hour, minute)\n Enter new time between backups (d/h/m): ")
            with open("backuptasks.txt", "a") as add_task:
                add_task.write(f"\"taskname\": \"{create_task_name}\", \"drivelocation\": \"{create_task_backup_location}\", \"backupfiles\": \"{task_files_to_backup_write.removesuffix(",")}\", \"backupeach\": \"{create_task_time_between_backups}\"\n")
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print(f"\n Created task: {create_task_name}")
            with open("application.log", "a") as write_log:
                write_log.write(f"{time.ctime()}, General: Created task {create_task_name}\n")
        elif main_menu_selection == "3":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("\n TASK EDITING\n\n Select task you want to edit:")
            x = 1
            for i in tasks:
                print(f" {x}. {i[0]}")
                x += 1
            selected_task_to_edit = input(" > ")
            selected_task_content = tasks[int(selected_task_to_edit) - 1]
            edit_task_selection = input("\n What do you want to modify?\n 1. Task Name\n 2. Backup location\n 3. Files to backup\n 4. Time between backups\n 5. Cancel\n > ")
            if edit_task_selection == "1":
                edit_task_name = input(" Enter new task name: ")
                if " " in edit_task_name:
                    print(" Spaces have been replaced with \"-\" as spaces are not allowed")
                    edit_task_name = edit_task_name.replace(" ", "-")
                with open("backuptasks.txt", "r") as edit_task_read:
                    edit_task_content = edit_task_read.read()
                with open("backuptasks.txt", "w") as edit_task_write:
                    edit_task_write.write(edit_task_content.replace(f"\"taskname\": \"{selected_task_content[0]}\"", f"\"taskname\": \"{edit_task_name}\""))
            elif edit_task_selection == "2":
                edit_task_backup_location = input(" Enter new backup folder location: ")
                while os.path.exists(create_task_backup_location) == False:
                    edit_task_backup_location = input(" Please enter a valid path!\n Enter new backup folder location: ")
                with open("backuptasks.txt", "r") as edit_task_read:
                    edit_task_content = edit_task_read.read()
                with open("backuptasks.txt", "w") as edit_task_write:
                    edit_task_write.write(edit_task_content.replace(f"\"drivelocation\": \"{selected_task_content[1]}\"", f"\"drivelocation\": \"{edit_task_backup_location}\""))
            elif edit_task_selection == "3":
                etfb_isok = "n"
                while etfb_isok == "n":
                    etfb_path_isok = False
                    while etfb_path_isok == False:
                        edit_task_files_backup = input(" Enter new files to backup (Spaced): ")
                        etfb_path_isok = True
                        for i in edit_task_files_backup.split():
                            if os.path.exists(i) == False:
                                etfb_path_isok = False
                        if etfb_path_isok == False:
                            print(f" Please check you have entered a valid path!")
                    print(" New file selection to be backed up:")
                    task_files_to_backup_write = ""
                    print_task_edition_files_backup = ""
                    for i in edit_task_files_backup.split():
                        print("   "+i)
                        print_task_edition_files_backup += f"\n   {i}"
                        task_files_to_backup_write += f"\"{i}\","
                    etfb_isok = input(" Is this selection correct? (y/n): ")
                with open("backuptasks.txt", "r") as edit_task_read:
                    edit_task_content = edit_task_read.read()
                with open("backuptasks.txt", "w") as edit_task_write:
                    edit_task_write.write(edit_task_content.replace(f"\"backupfiles\": \"{selected_task_content[2]}\"", f"\"backupfiles\": \"{task_files_to_backup_write.removesuffix(",")}\""))
            elif edit_task_selection == "4":
                edit_task_time_between_backups = input(" Enter new time between backups (d/h/m): ")
                while edit_task_time_between_backups[-1] not in "dhm" or edit_task_time_between_backups[:-1].isdigit() == False:
                    edit_task_time_between_backups = input("\n Ensure correct format! xy where x is a number and y is d,h or m (day, hour, minute)\n Enter new time between backups (d/h/m): ")
                with open("backuptasks.txt", "r") as edit_task_read:
                    edit_task_content = edit_task_read.read()
                with open("backuptasks.txt", "w") as edit_task_write:
                    edit_task_write.write(edit_task_content.replace(f"\"backupeach\": \"{selected_task_content[3]}\"", f"\"backupeach\": \"{edit_task_time_between_backups}\""))
            if edit_task_selection in "1234":
                task_backup_files = ""
                for i in tasks[int(selected_task_to_edit) - 1][2].split(","):
                    task_backup_files += "\n   "+i.removeprefix("\"").removesuffix("\"")
                input(f"\n Old:\n Task Name: {tasks[int(selected_task_to_edit) - 1][0]}\n Task backup location: {tasks[int(selected_task_to_edit) - 1][1]}\n Task backup files:{task_backup_files}\n Task time between backups: {tasks[int(selected_task_to_edit) - 1][3]}\n\n New:\n Task Name: {edit_task_name if edit_task_selection == "1" else tasks[int(selected_task_to_edit) - 1][0]}\n Task backup location: {edit_task_backup_location if edit_task_selection == "2" else tasks[int(selected_task_to_edit) - 1][1]}\n Task backup files:{print_task_edition_files_backup if edit_task_selection == "3" else task_backup_files}\n Task time between backups: {edit_task_time_between_backups if edit_task_selection == "4" else tasks[int(selected_task_to_edit) - 1][3]}\n\n Press Enter to return to main menu...")
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Edited task {tasks[int(selected_task_to_edit) - 1][0]}\n")
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        elif main_menu_selection == "4":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("\n TASK DELETION\n\n Select task you want to delete:")
            x = 1
            for i in tasks:
                print(f" {x}. {i[0]}")
                x += 1
            print(f" {x}. Cancel")
            selected_task_to_delete = input(" > ")
            if selected_task_to_delete == str(x):
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            else:
                selected_task_for_deletion_content = tasks[int(selected_task_to_delete) - 1]
                if input(f" Are you sure you want to delete task \"{tasks[int(selected_task_to_delete) - 1][0]}\" from backup tasks? (y/n): ") == "y":
                    with open("backuptasks.txt", "r") as delete_task_read:
                        delete_task_content = delete_task_read.read()
                    with open("backuptasks.txt", "w") as delete_task_write:
                        delete_task_write.write(delete_task_content.replace(f"\"taskname\": \"{selected_task_for_deletion_content[0]}\", \"drivelocation\": \"{selected_task_for_deletion_content[1]}\", \"backupfiles\": \"{selected_task_for_deletion_content[2]}\", \"backupeach\": \"{selected_task_for_deletion_content[3]}\"\n", ""))
                else:
                    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                    print(f"\n Cancelled deletion of {selected_task_for_deletion_content[0]}")
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print(f"\n Deleted task: {selected_task_for_deletion_content[0]}")
            with open("application.log", "a") as write_log:
                write_log.write(f"{time.ctime()}, General: Deleted task {selected_task_for_deletion_content[0]}\n")
        elif main_menu_selection == "5":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("\n Running tasks...")
            stop_all_tasks = False
            try:
                threads = []
                for i in tasks:
                    t = threading.Thread(target=backup_execution, args=(i))
                    threads.append(t)
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Starting tasks\n")
                for i in threads:
                    i.start()
                    time.sleep(1)
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Started all tasks\n")
                x = 0
                for i in tasks:
                    x+=1
                print(f" All tasks are running ({x})")
            except Exception as e:
                print(f" Error when running {i[0]}! {e}")
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Error when starting tasks! {e}\n")
        elif main_menu_selection == "6":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("\n Stopping tasks (Can take up to 30 seconds)...")
            try:
                stop_all_tasks = True
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Stopping tasks\n")
                for i in threads:
                    i.join()
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Stopped all tasks\n")
                x = 0
                for i in tasks:
                    x+=1
                print(f" All tasks are stopped ({x})")
            except Exception as e:
                print(f" Error! {e}")
                with open("application.log", "a") as write_log:
                    write_log.write(f"{time.ctime()}, General: Error when stopping tasks! {e}\n")
        elif main_menu_selection == "7":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            with open("application.log", "a") as write_log:
                write_log.write(f"{time.ctime()}, General: Refreshed\n")
        elif main_menu_selection == "8":
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            with open("application.log", "a") as write_log:
                write_log.write(f"{time.ctime()}, General: Stopping program\n")
            break
    with open("application.log", "a") as write_log:
        write_log.write(f"{time.ctime()}, General: Stopped program\n")
except Exception as e:
    print(f"\n General error! {e}")
    with open("application.log", "a") as write_log:
        write_log.write(f"{time.ctime()}, General: Error! {e}\n{time.ctime()}, General: Stopped program\n")