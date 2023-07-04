import tkinter as tk
import math
from tkinter.messagebox import askyesno
from tkinter import ttk
from settings.constants import *


# ================================================================= USER INTERFACE ========================================================================

root = tk.Tk()

# Create GUI with entry boxes and buttons
canvas1 = tk.Canvas(root, bg='orange', width=300, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, activebackground='black', bg='orange', text='Standing Waves Calculator')
label1.config(font=('ds-digital', 15, 'bold'))
canvas1.create_window(150, 40, window=label1)

entry1 = tk.Entry(root, font=('ds-digital', 12, 'bold'),
                  justify='center', highlightbackground='black')
entry1.insert(0, 'Length')
canvas1.create_window(150, 108, window=entry1)

entry2 = tk.Entry(root, font=('ds-digital', 12, 'bold'),
                  justify='center', highlightbackground='black')
entry2.insert(0, 'Width')
canvas1.create_window(150, 130, window=entry2)

entry3 = tk.Entry(root, font=('ds-digital', 12, 'bold'),
                  justify='center', highlightbackground='black')
entry3.insert(0, 'Height')
canvas1.create_window(150, 152, window=entry3)

# Map the Standing Wave Function to a Button which executes
button1 = tk.Button(text='Calculate', command=lambda: [standing_wave(), results()],
                    bg='brown', fg='white', font=('ds-digital', 20, 'bold'))
canvas1.create_window(150, 220, window=button1)


# ================================================================= CALCULATE & SAVE DATA =======================================================================


def standing_wave():

    freq_arr = []

    length = entry1.get()
    height = entry2.get()            # Get User Input
    width = entry3.get()

    # Calculate frequencies
    for a, b, c in zip(nx, ny, nz):
        freq = round(172 * math.sqrt((a/float(length))**2 +
                     (b/float(width))**2 + (c/float(height))**2))

        freq_arr.append(f'({a}-{b}-{c}):  {freq} Hz')
        freq_output = '\n'.join(freq_arr)

    standing_wave.data = freq_output


def save():
    text = askyesno('Confirm', 'Do you want to save?')

    if text == True:
    # Save Calculated Data to a txt file
        with open('data.txt', 'w') as f:
            for line in standing_wave.data:
                f.write(line)
    

def results():
    window = tk.Toplevel(root)
    window.geometry("400x400")
    window.title("Calculation Results")

    scroll = ttk.Scrollbar(window)
    scroll.pack(side='right', fill='y')

    # Label for showing the calculations
    result = tk.Text(window, width=30, height=15, font=('ds-digital', 14),
                     background='orange', wrap=None, yscrollcommand=scroll.set)
    result.pack(side='top', pady=20, fill='x')
    result.insert(tk.END, standing_wave.data)

    # Button to save the data
    save_data = tk.Button(window, text='Save', command=save)
    save_data.pack(side='top', pady=10)

    window.mainloop()


root.mainloop()
