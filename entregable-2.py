import tkinter as tk
from tkinter import messagebox
import random

# Crear la ventana principal
root = tk.Tk()
root.title("Tic Tac Toe - Jugador vs Máquina")

# Variables del juego
current_player = "X"
board = [""] * 9  # Tablero 3x3 (representado como una lista)
buttons = []

# Función para verificar si hay un ganador
def check_winner():
    # Combinaciones ganadoras
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]  # Devuelve el ganador ("X" o "O")
    
    if "" not in board:
        return "Empate"  # Si el tablero está lleno y no hay ganador
    
    return None  # Continúa el juego

# Movimiento de la máquina
def computer_move():
    available_moves = [i for i, x in enumerate(board) if x == ""]
    
    if available_moves:
        move = random.choice(available_moves)
        board[move] = "O"
        buttons[move].config(text="O")
        
        winner = check_winner()
        
        if winner:
            if winner == "Empate":
                messagebox.showinfo("Empate", "¡Es un empate!")
            else:
                messagebox.showinfo("Ganador", f"¡{winner} ha ganado!")
            reset_board()
        else:
            global current_player
            current_player = "X"  # Cambiar el turno de vuelta al jugador

# Función para gestionar el clic de un botón (jugador)
def button_click(index):
    global current_player
    
    if current_player == "X" and board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        winner = check_winner()
        
        if winner:
            if winner == "Empate":
                messagebox.showinfo("Empate", "¡Es un empate!")
            else:
                messagebox.showinfo("Ganador", f"¡{winner} ha ganado!")
            reset_board()
        else:
            current_player = "O"
            root.after(500, computer_move)  # Espera un poco antes de que la máquina haga su movimiento

# Función para reiniciar el tablero
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")

# Crear los botones del tablero
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Iniciar el bucle principal de tkinter
root.mainloop()
