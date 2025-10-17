# < IMPORTS >
import tkinter as tk
from tkinter import filedialog, messagebox, END
import sys
import os

def resource_path(relative_path):
    """ Retorna o caminho absoluto para o recurso, funciona para dev e para PyInstaller """
    try:
        # PyInstaller cria uma pasta temp e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# < FUNÇÕES >
# Função Centralizante de Tela
def center_window(window, width, height):
    # Pega as dimenssões da tela do computador
    screen_wid = window.winfo_screenwidth()
    screen_hei = window.winfo_screenheight()
    # Calcula a posição X (horizontal) para a janela ficar no centro
    x = (screen_wid // 2) - (width // 2)
    # Calcula a posição Y (vertical) para a janela ficar no centro
    y = (screen_hei // 2) - (height // 2)
    # Define a geometria da janela com o tamanho (width x height) e a posição (+x+y)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Função de Salvar Arquivos
# "event=None" permite que a função seja chamada tanto por um bind (que envia um evento) quanto por um menu (que não envia)
def save_text(text_widget, event=None):
    file_path = filedialog.asksaveasfilename(initialfile="*.txt",defaultextension=".txt",filetypes=[("Arquivos de Texto", "*.txt")])
    saved_Text = text_widget.get("1.0", END)
    if file_path:
        with open(file_path, "w") as file:
            file.write(saved_Text)
            messagebox.showinfo("showinfo", "Sucesso!")

# Função de Abrir Arquivos
def open_file(text_widget, event=None): # Mesmo caso do "event=None" acima
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            open_Text = file.read()
        text_widget.delete("1.0", END)
        text_widget.insert(END,open_Text)

# Função de Deletar
def delete_selectText(text_widget, event=None):
    try:
        text_widget.delete("sel.first", "sel.last")
    except tk.TclError:
        pass