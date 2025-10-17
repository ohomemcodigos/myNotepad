# < IMPORTS >
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import utils
from utils import resource_path

#define a janela "Sobre" como uma classe que herda de 'tk.Toplevel'
class AboutWindow(tk.Toplevel):
    # O método de inicialização dessa classe
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sobre o myNotepad")
        utils.center_window(self, 350, 350)
        self.resizable(False, False)
        self.iconbitmap(resource_path("icos/transparent.ico"))

        # --- Bloco  para adicionar a imagem ---
        try:
            image = Image.open(resource_path('icos/notepad.ico'))
            image = image.resize((80, 80)) # Redimensiona a imagem se necessário
            
            # Convertendo a imagem para um formato que o Tkinter pode usar
            self.photo_image = ImageTk.PhotoImage(image)

            image_label = tk.Label(self, image=self.photo_image)
            image_label.pack(pady=(15,0))   
        except FileNotFoundError:
            # Caso a imagem não seja encontrada, apenas mostra um texto de aviso
            error_label = tk.Label(self, text="[Imagem não encontrada]")
            error_label.pack(pady=(15,0))

        label = tk.Label(self, text="myNotepad", font=("Arial", 30, "bold"))
        label.pack(padx=20, pady=(10,10))

        about_separator = ttk.Separator(self, orient="horizontal")
        about_separator.pack(fill="x", padx=20, pady=5)

        label_text = tk.Label(self, text="Aplicação de Notas feita usando Python.")
        label_text.pack(padx=20, pady=10)

        label_text = tk.Label(self, text="Desenvolvido por Guilherme M.")
        label_text.pack(padx=20, pady=10)

        ok_button = ttk.Button(self, text="OK", command=self.destroy, style="Big.TButton")
        ok_button.place(relx=1.0, rely=1.0, anchor='se', x=-15, y=-15)
        ok_button.focus_set()

        version_label = tk.Label(
            self,
            text="v1.0",
            font=("Arial", 8), # Fonte pequena
            fg="gray" # Cor cinza para ser mais sutil
        )
        version_label.place(relx=1.0, rely=1.0, anchor='se', x=-15, y=-45)