import tkinter as tk
import threading
import queue





def console_logic(input_queue):
    while True:
        # Wait for input from the GUI
        user_input = input_queue.get()
        if user_input == "QUIT":
            print("Exiting thread.")
            break
        print(f"Received input: {user_input}")

class App(tk.Tk):
    def __init__(self, input_queue):
        super().__init__()
        self.input_queue = input_queue
        self.title("GUI Input to Console")
        self.geometry("300x100")
        
        self.input_entry = tk.Entry(self)
        self.input_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_input)
        self.submit_button.pack(pady=10)
        
        self.quit_button = tk.Button(self, text="Quit", command=self.quit_app)
        self.quit_button.pack(pady=10)

    def submit_input(self):
        jeff = input('whats your mom age lil boy?')
        if jeff == 12:
            print('wow awesome')

        # Get input from Entry widget and put it in the queue
        user_input = self.input_entry.get()
        self.input_queue.put(user_input)
        self.input_entry.delete(0, tk.END)  # Clear the entry box

    def quit_app(self):
        self.input_queue.put("QUIT")
        self.destroy()

def main():
    input_queue = queue.Queue()
    app = App(input_queue)

    # Thread for console logic
    thread = threading.Thread(target=console_logic, args=(input_queue,))
    thread.daemon = True
    thread.start()

    app.mainloop()
    thread.join()  # Wait for the thread to finish before exiting completely

if __name__ == "__main__":
    main()