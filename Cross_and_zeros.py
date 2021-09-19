import tkinter as tk


class Cross:
    CROSS = '+'
    ZERO = '0'

    def __init__(self):
        self.root = tk.Tk()
        self.buttons = []
        self.turn = True
        for i in range(3):
            temp = []
            for j in range(3):
                btn = tk.Button(self.root, width=3, font='Helvetica 48')
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    def create_wigets(self):
        for i in range(3):
            for j in range(3):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def click(self, clicked_button):
        global turn
        if self.turn:
            clicked_button.config(text=Cross.CROSS, disabledforeground='black')
            self.turn = False
        else:
            clicked_button.config(text=Cross.ZERO, disabledforeground='black')
            self.turn = True
        clicked_button.config(state='disabled')


    def start_game(self):
        self.create_wigets()
        self.print_but()
        self.root.mainloop()

    def print_but(self):
        for i in range(3):
            for j in range(3):
                print(self.buttons[i][j], end='')
            print()

app = Cross()


app.start_game()