import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_separator():
    print("\n" + "=" * 50 + "\n")

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"

print(f"{CYAN}{BOLD}\
 _            _   ____  _           _   \n\
| |_ _____  _| |_|___ \\| |__   __ _| |_ \n\
| __/ _ \\ \\/ / __| __) | '_ \\ / _` | __|\n\
| ||  __/>  <| |_ / __/| |_) | (_| | |_ \n\
 \\__\\___/_/\\_\\\\__|_____|_.__/ \\__,_|\\__|{RESET}")

print(f"{YELLOW}Developed: https://dev-0618.github.io/127.4.7.8/{RESET}")
time.sleep(2.5)
clear_screen()

def get_input(prompt):
    return input(prompt).strip()

clear_screen()

def create_bat_script(steps, filename):
    with open(filename, "w") as bat_file:
        for step in steps:
            bat_file.write(step + "\n")
    print(f"{GREEN}BAT script '{filename}' has been created successfully.{RESET}")

clear_screen()

def add_open_browser():
    url = get_input("Enter the URL to open in the browser: ")
    command = f"start \"\" \"{url}\""
    return command

clear_screen()

def add_dialog_box():
    print(f"{MAGENTA}Choose an option for the dialog box:{RESET}")
    print("1. Show Message Box")
    print("2. Ask for User Input")
    print("3. Yes/No Prompt")
    choice = get_input("Enter your choice (1-3): ")
    
    if choice == '1':
        message = get_input("Enter the message to display: ")
        command = f"echo msg * {message} > temp.vbs && start wscript temp.vbs && del temp.vbs"
    elif choice == '2':
        prompt = get_input("Enter the prompt message: ")
        command = f"set /p userInput=\"{prompt}: \""
    elif choice == '3':
        question = get_input("Enter the yes/no question: ")
        command = f"set /p answer=\"{question} (Y/N): \" && if /i \"%answer%\"==\"Y\" (echo Yes) else (echo No)"
    else:
        command = "echo Invalid choice. No dialog created."
        
    return command

clear_screen()

def add_run_script():
    script_name = get_input("Enter the name of the script to run (with .bat extension): ")
    command = f"call {script_name}"
    return command

clear_screen()

def add_open_command_prompt():
    command = "start cmd"
    return command

clear_screen()

def add_create_folder():
    folder_name = get_input("Enter the name of the folder to create: ")
    command = f"mkdir \"{folder_name}\""
    return command

clear_screen()

def add_copy_files():
    source = get_input("Enter the source file path: ")
    destination = get_input("Enter the destination path: ")
    command = f"copy \"{source}\" \"{destination}\""
    return command

clear_screen()

def add_move_files():
    source = get_input("Enter the source file path: ")
    destination = get_input("Enter the destination path: ")
    command = f"move \"{source}\" \"{destination}\""
    return command

clear_screen()

def add_delete_files():
    file_path = get_input("Enter the file path to delete: ")
    command = f"del \"{file_path}\""
    return command

def add_ping_host():
    host = get_input("Enter the IP address or hostname to ping: ")
    command = f"ping {host}"
    return command

def add_schedule_task():
    task_name = get_input("Enter the name of the task: ")
    command = f"schtasks /create /tn \"{task_name}\" /tr \"cmd.exe /c echo Task executed!\" /sc once /st 12:00"
    return command

def add_sub_options(option):
    if option == '2':  # Dialog Box
        return add_dialog_box()
    elif option == '10':  # Schedule Task
        return add_schedule_task()
    else:
        print("No sub-options available for this choice.")
        return ""

def main():
    print(f"{GREEN}Welcome to the Enhanced Custom BAT Script Builder!{RESET}")
    steps = []
    
    while True:
        print_separator()
        print("Choose an option to add to the BAT script:")
        print("1. Open Browser")
        print("2. Show Dialog Box")
        print("3. Run Script")
        print("4. Open Command Prompt")
        print("5. Create a New Folder")
        print("6. Copy Files")
        print("7. Move Files")
        print("8. Delete Files")
        print("9. Ping a Host")
        print("10. Schedule a Task")
        print("11. Finish and Create BAT Script")
        print("12. Exit")
        
        choice = get_input("Enter your choice (1-12): ")

        if choice == '1':
            steps.append(add_open_browser())
        elif choice == '2':
            steps.append(add_sub_options('2'))
        elif choice == '3':
            steps.append(add_run_script())
        elif choice == '4':
            steps.append(add_open_command_prompt())
        elif choice == '5':
            steps.append(add_create_folder())
        elif choice == '6':
            steps.append(add_copy_files())
        elif choice == '7':
            steps.append(add_move_files())
        elif choice == '8':
            steps.append(add_delete_files())
        elif choice == '9':
            steps.append(add_ping_host())
        elif choice == '10':
            steps.append(add_sub_options('10'))
        elif choice == '11':
            filename = get_input("Enter the name of the BAT file to save (e.g., custom.bat): ")
            create_bat_script(steps, filename)
            break
        elif choice == '12':
            print("Exiting without creating a script.")
            break
        else:
            print(f"{YELLOW}Invalid choice, please select a valid option.{RESET}")

if __name__ == "__main__":
    main()
