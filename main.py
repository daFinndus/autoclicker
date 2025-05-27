import threading

import keyboard
import mouse
import time


class Clicker:
    def __init__(self):
        self.speed = 5  # Default click speed
        self.hotkey = 'f'  # Default hotkey for toggling the clicker
        self.running = False

    # This function retrieves user input for click speed and hotkey
    def info(self):
        # Retrieve user information
        self.speed = input("Please enter the clicks per second (default is 5): ")
        if not self.speed.isdigit() or int(self.speed) <= 0:
            self.speed = 5
            print(f"Seems your input is invalid, setting speed to {self.speed} clicks per second.")
        else:
            self.speed = int(self.speed.strip())
            print(f"Setting speed to {self.speed} clicks per second.")

        time.sleep(2)

        self.hotkey = input("\nPlease enter the hotkey to toggle the clicker (default is 'f'): ")

        if not self.hotkey.strip() or len(self.hotkey) > 1:
            self.hotkey = 'f'
            print(f"Seems your input is invalid, setting hotkey to '{self.hotkey}'.")
        else:
            self.hotkey = self.hotkey.strip()
            print(f"Setting hotkey to '{self.hotkey}'.")

    # This function is for the clicker functionality
    def clicker(self):
        print(f"\nClicker is now running. Click 'CTRL+C' to exit.")
        print(f"Listening for hotkey '{self.hotkey}' to toggle clicking at {self.speed} clicks per second.")

        while True:
            if keyboard.is_pressed(self.hotkey):
                time.sleep(1)
                self.running = not self.running
                if self.running:
                    print("Clicking started.")
                else:
                    print("Clicking ended.")

            if self.running:
                mouse.click(button='left')
                time.sleep(1 / self.speed)

            if keyboard.is_pressed('CTRL+C'):
                print("Exiting clicker.")
                break

        exit(0)


if __name__ == "__main__":
    clicker = Clicker()

    clicker.info()
    time.sleep(2)

    threading.Thread(target=clicker.clicker).start()
