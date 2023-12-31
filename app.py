import math
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

import settings.constants as const


class StandingWave:
    def __init__(self, length, height, width):
        self._length = length
        self._height = height
        self._width = width

    def calculate_frequencies(self, array_const1, array_const2, array_const3):
        """ Takes in const triplet arrays and creates a string of the room nodes by frequency"""
        length = float(self._length.get())
        width = float(self._width.get())
        height = float(self._height.get())
        freq_arr = []

        for a, b, c in zip(array_const1, array_const2, array_const3):
            freq = round(172 * math.sqrt((a / length) ** 2 +
                                         (b / width) ** 2 + (c / height) ** 2))

            freq_arr.append(f'({a}-{b}-{c}):  {freq} Hz')

        return '\n'.join(freq_arr)

    def save(self, output_data: str):
        text = askyesno('Confirm', 'Do you want to save?')
        if text:
            with open('data.txt', 'w') as f:
                for line in output_data:
                    f.write(line)

    def results(self, root, data):
        window = tk.Toplevel(root)
        window.geometry("400x400")
        window.title("Calculation Results")

        scroll = ttk.Scrollbar(window)
        scroll.pack(side='right', fill='y')

        # Label for showing the calculations
        result = tk.Text(window, width=30, height=15, font=('ds-digital', 14),
                         background='orange', wrap="none", yscrollcommand=scroll.set)
        result.pack(side='top', pady=20, fill='x')
        result.insert(tk.END, data)

        # Button to save the data
        save_data = tk.Button(window, text='Save', command=lambda: self.save(data))
        save_data.pack(side='top', pady=10)

        window.mainloop()


class UserInterface:
    def __init__(self):
        self.root = tk.Tk()

        self.canvas1 = tk.Canvas(self.root, bg='orange', width=300, height=300, relief='raised')
        self.canvas1.pack()

        self.label1 = tk.Label(self.root, activebackground='black', bg='orange', text='Standing Waves Calculator')
        self.label1.config(font=('ds-digital', 15, 'bold'))
        self.canvas1.create_window(150, 40, window=self.label1)

        self.entry1 = tk.Entry(self.root, font=('ds-digital', 12, 'bold'),
                               justify='center', highlightbackground='black')
        self.entry1.insert(0, 'Length')
        self.canvas1.create_window(150, 108, window=self.entry1)

        self.entry2 = tk.Entry(self.root, font=('ds-digital', 12, 'bold'),
                               justify='center', highlightbackground='black')
        self.entry2.insert(0, 'Width')
        self.canvas1.create_window(150, 130, window=self.entry2)

        self.entry3 = tk.Entry(self.root, font=('ds-digital', 12, 'bold'),
                               justify='center', highlightbackground='black')
        self.entry3.insert(0, 'Height')
        self.canvas1.create_window(150, 152, window=self.entry3)

        # Map the Standing Wave Function to a Button which executes
        self.room = StandingWave(self.entry1, self.entry2, self.entry3)
        self.button1 = tk.Button(text='Calculate', command=self.calculate_and_display_results,
                                 bg='brown', fg='white', font=('ds-digital', 20, 'bold'))
        self.canvas1.create_window(150, 220, window=self.button1)

    def calculate_and_display_results(self):
        output_data = self.room.calculate_frequencies(const.nx, const.ny, const.nz)
        self.room.results(self.root, output_data)


def main():
    interface = UserInterface()
    interface.root.mainloop()


if __name__ == "__main__":
    main()
