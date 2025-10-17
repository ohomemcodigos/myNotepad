# < IMPORTS >
import tkinter as tk
from tkinter import ttk
import utils
from utils import resource_path

# Define a janela "Ajuda" como uma classe que herda de 'tk.Toplevel'
class HelpWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ajuda")
        utils.center_window(self, 400, 450)
        self.resizable(False, False)
        self.iconbitmap(resource_path("icos/question_mark.ico"))

        # --- TÍTULO DA JANELA ---
        title_label = tk.Label(self, text="Atalhos do Teclado", font=("Arial", 16, "bold"))
        title_label.pack(padx=20, pady=(20, 10))

        # --- TABELA DE ATALHOS ---
        # Define as colunas da tabela
        columns = ('action', 'shortcut')

        # Cria o Treeview
        tree = ttk.Treeview(self, columns=columns, show='headings', height=10)

        # Define os cabeçalhos das colunas
        tree.heading('action', text='Ação')
        tree.heading('shortcut', text='Atalho')

        # Ajusta a largura e o alinhamento das colunas
        tree.column('action', width=240)
        tree.column('shortcut', width=120, anchor='center')

        # --- LISTA DE ATALHOS ---
        # Lista com tuplas contendo (Ação, Atalho)
        shortcuts = [
            ("Abrir Arquivo", "Ctrl + O"),
            ("Salvar Arquivo", "Ctrl + S"),
            ("", ""), # Linha em branco para separação
            ("Desfazer", "Ctrl + Z"),
            ("Recortar", "Ctrl + X"),
            ("Copiar", "Ctrl + C"),
            ("Colar", "Ctrl + V"),
            ("Excluir Seleção", "Del"),
        ]

        # Adiciona os dados da lista na tabela
        for action, shortcut in shortcuts:
            tree.insert('', tk.END, values=(action, shortcut))

        tree.pack(padx=20, pady=10, fill="x")

        # --- BOTÃO OK ---
        ok_button = ttk.Button(self, text="OK", command=self.destroy)
        ok_button.pack(pady=(10, 20))
        ok_button.focus_set()