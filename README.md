# Keystroke Monitor

The Keystroke Monitor is a Python script designed to monitor keystrokes on a user's system and send periodic updates via email. It uses the `pynput` library to capture keystrokes and the `smtplib` library to send emails.

## Features

- Monitors keystrokes in the background.
- Saves keystrokes to a text file.
- Sends periodic updates of saved keystrokes via email.

## How to Use

1. Ensure you have Python installed on your system.
2. Install the required libraries using `pip install pynput`.
3. Update the script with your Gmail credentials (`gmail_email` and `gmail_password`) and the recipient's email address (`recipient_email`).
4. Run the script using Python: `python3 kelogsmtp.py`.
5. Type as usual. Keystrokes will be saved to `keystrokes.txt` and periodically sent via email.

## Modifying the Code

- To change the email provider, modify the `send_email` function to use the appropriate SMTP server and port.
- Customize the email subject and message as needed in the `send_email` function.
- Adjust the interval for sending email updates by changing the `time.sleep` value in the `print_saved_keystrokes` function.

## Disclaimer

This script is intended for educational and research purposes only. Monitoring keystrokes without consent may violate privacy laws and ethical guidelines. Use responsibly and ensure compliance with relevant regulations.

