## Usage Guide for AutoGuiBot Script

### Description
The `index.py` script is used to send messages automatically using the `pyautogui` module. The following usage guide explains the steps to use this script.

### Steps

1. **Dependency Installation**
    - Ensure you have installed the `pyautogui` and `easygui` modules.
    - If not, install them using the following commands:
        ```
        pip install pyautogui
        pip install easygui
        ```

2. **Running the Script**
    - Open a terminal or command prompt.
    - Run the script with the command `python index.py`.

3. **Choosing Options**
    - After running the script, a GUI will appear with options between "File" or "Static," as shown in the following image:

    ![GUI Menu](https://raw.githubusercontent.com/willyamk/AutoGuiBot/main/menu_gui.png)

4. **Using the "File" Option**
    - If you choose the "File" option, the script will open File Explorer.
    - Select a `.txt` file containing the messages you want to send, with sample data like the following:
       ```
       test 1
       test 2
       test 3
       test 4
       test 5
       ```
       > **Warning:** The program will execute the data line by line!
    - Make sure to keep your cursor active in the targeted chat input field.
    - Click "OK" and the script will send the messages in the file sequentially.

5. **Using the "Static" Option**
    - If you choose the "Static" option, you will be prompted to enter the message you want to send, as shown in the following image:

    ![Static Message](https://raw.githubusercontent.com/willyamk/AutoGuiBot/main/statis_message.png)

    - Next, input the number of messages you want to send, as shown in the following image:

    ![Message Count](https://raw.githubusercontent.com/willyamk/AutoGuiBot/main/statis_message_loop.png)

    - Ensure your cursor is active in the targeted chat input field.
    - Click "OK" and the script will send the message as many times as specified.

6. **Important Notes**
    - Ensure your cursor is active in the targeted chat input field before clicking "OK" in the GUI.
    - For the "File" option, make sure the selected `.txt` file contains messages to be sent line by line.

### Script Overview
The `index.py` script imports the `pyautogui`, `time`, and `easygui` modules and defines the `AutoGuiBot` class and functions to run the bot and retrieve messages from a text file. The main `main()` function displays a GUI to select between the "File" or "Static" options, and based on the user's choice, retrieves messages from a file or user input. The bot then sends the messages automatically.

By following the steps above, you can use this script to send messages automatically through the provided GUI.
