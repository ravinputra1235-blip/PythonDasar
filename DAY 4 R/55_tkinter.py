import tkinter as tk
root = tk.Tk()
LabeL1 = tk.Label(root, text="Label 1")
LabeL2 = tk.Label(root, text="Label 2")
LabeL3 = tk.Label(root, text="Label 3")

LabeL1.grid(row=0, column=0)
LabeL2.grid(row=0, column=1)
LabeL3.grid(row=1, column=0, columnspan=2)
root.mainloop()