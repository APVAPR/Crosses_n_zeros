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
                btn = tk.Button(self.root, width=3, font='Ubuntu 48')
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
            self.win_check()
            self.turn = False
        else:
            clicked_button.config(text=Cross.ZERO, disabledforeground='black')
            self.win_check()
            self.turn = True
        clicked_button.config(state='disabled')

    def win_check(self):
        flag = True
        winner = ''
        for i in range(3):
            horisont_temp = set(j['text'] for j in self.buttons[i])
            if horisont_temp == {'0'}:
                winner = 'Zero'

            elif horisont_temp == {'+'}:
                winner = 'Cross'

            if winner:
                flag = False
                break

        for i in range(3):
            vertical_temp = set()
            for j in range(3):
                vertical_temp.add(self.buttons[j][i]['text'])
            if vertical_temp == {'0'} or vertical_temp == {'+'}:
                flag = False
                break

        diag_temp = set()
        for i in range(3):
            diag_temp.add(self.buttons[i][i]['text'])

        diag_temp_nv = (self.buttons[2][0]['text'],
                        self.buttons[1][1]['text'],
                        self.buttons[0][2]['text'])
        diag_temp_nv = set(diag_temp_nv)

        if diag_temp == {'+'} or diag_temp_nv == {'+'}:
            winner = 'Cross'
        elif diag_temp == {'0'} or diag_temp_nv == {'0'}:
            winner = 'Zero'
        diag_temp.clear()
        if winner:
            flag = False
            

        print(flag, winner)
        return flag, winner

    def finish_game(self):
        if not self.win_check()[0]:
            tk.Label(self.root,
                     text=f'Winner is {self.win_check()[1]}',
                     font='Helvetica 48',
                     width=9).grid(row=1, column=1)

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
