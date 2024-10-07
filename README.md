# text2bat
[![An image of @dev0618's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/dev0618)](https://holopin.io/@dev0618)


`text2bat` is a customizable Python tool designed to help web penetration testers convert normal text commands into batch (BAT) scripts efficiently. This tool offers an interactive interface for users to select various operations and generate BAT scripts quickly, making it a valuable addition to the toolkit of any pentester.

## Features

- **Open a Web Browser**: Easily launch your default browser to a specified URL.
- **Display Dialog Boxes**: Create various types of dialog boxes for user interaction.
  - Show a message box.
  - Prompt for user input.
  - Yes/No confirmation prompts.
- **Run Existing Scripts**: Call other batch scripts from within the generated script.
- **Open Command Prompt**: Start a new command prompt window directly from the script.
- **File Operations**:
  - Create new folders.
  - Copy files from one location to another.
  - Move files between directories.
  - Delete specified files.
- **Ping a Host**: Check the connectivity of a specified IP address or hostname.
- **Schedule Tasks**: Schedule commands to run at a specific time using Windows Task Scheduler.

## Installation

To set up and use the `text2bat` tool, follow these steps:

1. **Clone the Repository**:
   Open your terminal and execute the following command to clone the repository:

   ```bash
   git clone https://github.com/Dev-0618/text2bat.git
   ```

2. **Navigate to the Project Directory**:
   Change into the newly created directory:

   ```bash
   cd text2bat
   ```

3. **Install Python**:
   Ensure you have Python 3.x installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

4. **Run the Script**:
   To start using the `text2bat` tool, run the following command:

   ```bash
   python3 text2bat.py
   ```

## Usage

Upon running the script, you will be presented with a menu of options. You can choose which operations to include in your BAT script. Below are the available options and detailed explanations of their functionalities:

### Available Options

1. **Open Browser**
   - Launches your default web browser to the specified URL.
   - **Input Required**: The URL to open.

2. **Show Dialog Box**
   - Allows you to create dialog boxes for user interaction.
   - **Sub-options**:
     - **Show Message Box**: Displays a message to the user.
       - **Input Required**: The message content.
     - **Ask for User Input**: Prompts the user to enter a value in the command line.
       - **Input Required**: Prompt message.
     - **Yes/No Prompt**: Asks the user a yes/no question and captures the response.
       - **Input Required**: The yes/no question.

3. **Run Script**
   - Executes an existing batch script specified by the user.
   - **Input Required**: The name of the script file (with .bat extension).

4. **Open Command Prompt**
   - Opens a new command prompt window for further commands.
   - **No Input Required**.

5. **Create a New Folder**
   - Creates a folder with the name provided by the user.
   - **Input Required**: The name of the folder.

6. **Copy Files**
   - Copies files from a specified source path to a destination path.
   - **Input Required**: Source file path and destination path.

7. **Move Files**
   - Moves files from one location to another.
   - **Input Required**: Source file path and destination path.

8. **Delete Files**
   - Deletes a specified file.
   - **Input Required**: The file path to delete.

9. **Ping a Host**
   - Pings an IP address or hostname to check connectivity.
   - **Input Required**: The IP address or hostname to ping.

10. **Schedule a Task**
    - Schedules a task to run a command at a specified time.
    - **Input Required**: Task name (command execution is set to echo a simple message).

11. **Finish and Create BAT Script**
    - Finalizes the selections and saves the BAT script to a user-defined filename.
    - **Input Required**: The desired filename for the BAT script.

12. **Exit**
    - Exits the application without saving any changes.
    - **No Input Required**.

## Contributing

Contributions to the `text2bat` project are welcome! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the community and resources that helped in the development of this tool. Happy scripting!
