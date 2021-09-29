import random


class TicTacToe:
    def __init__(self):
        self.table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.casillas = 9
        self.flow()

    def display(self):
        for row in self.table:
            for num in row:
                print("|", num, sep="", end="")
            print("|")

    def cheker(self):
        def checkline(arr):
            if arr[0] == arr[1] and arr[1] == arr[2]:
                return True
            else:
                return False

        for i in range(3):
            lines = []
            colms = []
            cross = []
            i_crs = []
            for j in range(3):
                lines.append(self.table[i][j])
                colms.append(self.table[j][i])
                i_crs.append(self.table[j][2-j])
                cross.append(self.table[j][j])

            if checkline(lines):
                return lines[0]
            elif checkline(colms):
                return colms[0]
            elif checkline(i_crs):
                return i_crs[0]
            elif checkline(cross):
                return cross[0]
            else:
                pass
        return False

    def input(self):
        # User
        row, col = int(input("Ingrese la fila a insertar valor: ")), int(
            input("Ingrese la col a insertar valor: "))
        while self.table[row][col] == "o" or self.table[row][col] == "x":
            row, col = int(input("Ingrese la fila a insertar valor: ")), int(
                input("Ingrese la col a insertar valor: "))
        self.table[row][col] = "x"
        self.casillas -= 1

        if self.cheker() == "x":
            print("Ganaste!")
            return True
        elif self.casillas == 0:
            print("Empataste!")
            return True

        # Machine
        row, col = random.randint(0, 2), random.randint(0, 2)
        while self.table[row][col] == "o" or self.table[row][col] == "x":
            row, col = random.randint(0, 2), random.randint(0, 2)
        self.table[row][col] = "o"
        self.casillas -= 1

        if self.cheker() == "o":
            print("Perdiste!")
            return True
        elif self.casillas == 0:
            print("Empataste!")
            return True

        # Sends a False result meaning there is no winer yet,and needs more inputs
        return False

    def flow(self):
        self.display()
        while (self.input()) == False:
            self.display()
        self.display()
