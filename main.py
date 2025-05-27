import threading
import keyboard
import mouse
import time
import sys


class Clicker:
    DEFAULT_SPEED = 5  # Default clicks per second
    DEFAULT_HOTKEY = 'f'  # Default hotkey

    def __init__(self):
        self.speed = self.DEFAULT_SPEED
        self.hotkey = self.DEFAULT_HOTKEY

        self.running = False
        self.last = 0

    # This function retrieves user input for click speed and hotkey
    def info(self):
        # Retrieve user information
        geschwindigkeit = input("Please enter the clicks per second (default is 5): ").strip()
        if geschwindigkeit.isdigit() and int(geschwindigkeit) > 0:
            print(f"Setting speed to {geschwindigkeit} clicks per second.")
            self.speed = int(geschwindigkeit)
        else:
            print(f"Seems your input is invalid, setting speed to {self.speed} clicks per second.")

        time.sleep(2)

        taste = input("\nPlease enter the hotkey to toggle the clicker (default is 'f'): ").strip()
        if len(taste) == 1:
            print(f"Setting hotkey to '{taste}'.")
            self.hotkey = taste
        else:
            print(f"Seems your input is invalid, setting hotkey to '{self.hotkey}'.")

    def toggle(self):
        while True:
            keyboard.wait(self.hotkey)

            # Debounce the hotkey press
            if time.time() - self.last > 0.3:
                self.running = not self.running
                state = "started" if self.running else "stopped"
                print(f"Clicking {state}.")
                self.last = time.time()

    # This function is for the clicker functionality
    def clicker(self):
        print(f"\nClicker is ready. Press '{self.hotkey}' to toggle. Press 'CTRL+C' to quit.\n")

        try:
            while True:
                if self.running:
                    mouse.click(button='left')
                    time.sleep(1 / self.speed)
                else:
                    # Reduce CPU usage when idle
                    time.sleep(0.01)
        except KeyboardInterrupt:
            print("\nExiting clicker...")
            sys.exit(0)


if __name__ == "__main__":
    clicker = Clicker()
    clicker.info()

    # Start listener in a thread
    threading.Thread(target=clicker.toggle, daemon=True).start()

    # Start clicker loop
    clicker.clicker()
