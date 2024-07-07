

```markdown
# WhatsApp Message Automation Script

This Python script automates sending a WhatsApp message to multiple contacts using `pywhatkit` and `pyautogui`.

## Requirements

Before running the script, make sure you have the following Python libraries installed:
- `pywhatkit`
- `pyautogui`

You can install them using pip:
```bash
pip install pywhatkit pyautogui
```

## Setup

1. Create a text file named `WhattsappNumbers.txt` in the same directory as the script. This file should contain the list of WhatsApp numbers (without the country code prefix) you want to send messages to, with each number on a new line.
2. Ensure you are logged into WhatsApp Web on your default browser.

## How to Use

1. Run the script using a Python interpreter.
2. When prompted, enter the message you want to send.
3. Press Enter to start the process.

The script will then:
1. Read the numbers from the `WhattsappNumbers.txt` file.
2. Send the specified message to each number.
3. Add a delay between each message to comply with WhatsApp's rate limits.

## Script Breakdown

1. **Reading Numbers**: The script reads the phone numbers from the `WhattsappNumbers.txt` file and stores them in a list.
2. **User Input**: The user is prompted to input the message to be sent.
3. **Sending Messages**: The script sends the message to each number using `pywhatkit.sendwhatmsg_instantly`, waits for 20 seconds before sending the next message, and closes the WhatsApp tab.

```python
import pywhatkit as kit
import time
import pyautogui as pg

# List of WhatsApp numbers
numbers = []
with open("WhattsappNumbers.txt", "r") as fp:
    for line in fp:
        numbers.append(line.strip())  
        print(f"{line.strip()} added")

# Message to send
message = input("Enter a message: ")
input("Press Enter to start")

a = len(numbers)

# Sending the message to each number
for number in numbers:
    kit.sendwhatmsg_instantly(f"+91{number}", message, 10)
    pg.press("enter")
    a = a - 1
    print(a, "left")
    time.sleep(20)  # Add delay to avoid spamming and to comply with WhatsApp's rate limits
    pg.hotkey('ctrl', 'w')
```

## Important Notes

- This script is intended for educational purposes only. Ensure you have permission to message the numbers in your list.
- Spamming or unsolicited messaging can lead to your WhatsApp account being banned. Use this script responsibly.
- Adjust the delay time if necessary to avoid triggering any rate limits on WhatsApp.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

