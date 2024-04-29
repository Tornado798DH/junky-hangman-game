#   Tornado DH
#Just saying hi :)
import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 100.")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                messagebox.showinfo("Result", "Try a higher number.")
            elif guess > self.secret_number:
                messagebox.showinfo("Result", "Try a lower number.")
            else:
                messagebox.showinfo("Congratulations", f"You've guessed the number in {self.attempts} attempts.")
                self.master.destroy()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number between 1 and 100.")

def main():
    DH = tk.Tk()
    game = GuessNumberGame(DH)
    DH.mainloop()

if __name__ == "__main__":
    main()