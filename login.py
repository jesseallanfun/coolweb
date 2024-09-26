import pyautogui as pag
import time
import pyperclip

# Define the coordinates and use the `actions` list
actions = [
    (116, 457, 10),  # install
    (116, 457, 2),  # install
    (539, 461, 10),  # install again
    (539, 461, 2),  # install again
    (761, 25, 7),  # maximize
    (761, 25, 2),  # maximize
    (89, 159, 2),  #rightclick
    (139, 169, 2),  #select all
    (88, 152, 2),  #right click
    (138, 162, 2),  #copy
    (930, 19, 2),   # 3 bars
    (930, 19, 2),   # 3 bars
    (53, 163, 2),   # secu
    (53, 163, 2),   # secu
    (445, 62, 2),   # enable
    (445, 62, 2),   # enable
    (357, 660, 2),  # set pass
    (357, 660, 2),  # set pass
    (278, 307, 2),  # first fill
    (278, 396, 2),  # second fill
    (741, 494, 2),  # ok
    (741, 494, 2),  # ok
    (958, 10, 2),    #minimize
]

# Wait for a few seconds to give time to focus on the target application
time.sleep(20)

# Perform the actions in the specified order
for x, y, duration in actions:
    if (x, y) == (89, 159) or (x, y) == (88, 152):
        # For right-click coordinates, perform right-click
        pag.rightClick(x, y, duration=duration)
    else:
        pag.click(x, y, duration=duration)
    if (x, y) in [(278, 307), (278, 396)]:
        # For "first fill" and "second fill" coordinates, type the desired text
        pag.click(x, y, duration=duration)
        pag.keyDown('D')  # Press the "D" key
        text_to_type = "Disalardp1"
        pag.typewrite(text_to_type)

def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}\n')

def run_rustdesk_command():
    clipboard_text = pyperclip.paste()
    password_echo = 'RustDesk Password : Disalardp1'  
    save_echo_to_batch('show.bat', f'RustDesk ID: {clipboard_text}')
    save_echo_to_batch('show.bat', password_echo)

if __name__ == "__main__":
    run_rustdesk_command()

print("Done , Log in Credintials is below")
