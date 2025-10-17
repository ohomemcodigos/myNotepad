# < IMPORTS >
import tkinter as tk
import utils
from about_window import AboutWindow
from help_window import HelpWindow
from utils import resource_path

# --- < JANELA PRINCIPAL > ---
# Cria a Janela Principal
root = tk.Tk() # Renderiza a janela
root.title("myNotepad") # Define o título da janela
utils.center_window(root, 1250, 750) # Usando uma função do utils, centralia a janela + define o tamanho da janela

root.iconbitmap(resource_path("icos/notepad.ico")) # Define o ícone personalizado

# --- < JANELA HELP >
# Cria a Janela do Ajuda
def open_help():
    # Cria uma instância para nova janela
    help_win = HelpWindow(root)
    help_win.focus_force()
    help_win.grab_set() # Faz com que a janela "Ajuda" seja modal

# --- < JANELA ABOUT > ---
# Cria a Janela do Sobre
def open_about():
    # Cria uma instância para nova janela
    about = AboutWindow(root)
    about.focus_force() 
    about.grab_set() # Faz com que a janela "Sobre" seja modal

# --- < WIDGETS E LAYOUT > ---
# Frame Principal da Aplicação
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(main_frame) # Renderiza a scrollbar dentro do frame principal
scrollbar.pack(side="right", fill="y")

# Caixa de Texto
text_area = tk.Text(
    main_frame,
    undo=True,
    yscrollcommand=scrollbar.set,
    font=("Arial", 12), # Define a fonte e seu tamanho
    wrap="word", # Quebra de linha autômatica 
    
    # --- Customizações de Aparência ---
    borderwidth=0,
    relief=tk.FLAT,
    padx=4,
)
# Posiciona a caixa de texto à esquerda, fazendo com que ela ocupe todo o espaço restante
text_area.pack(side="left", fill="both", expand=True)

# Configura a barra de rolagem para controlar a visão vertical ('yview') da caixa de texto
scrollbar.config(command=text_area.yview)

# Menubar
# Cria a barra de menu e a coloca na janela principal
menubar = tk.Menu(root)
root.config(menu=menubar)
# Menu Arquivo
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label = "Abrir...                      ", accelerator="Ctrl+O", command= lambda: utils.open_file(text_area))
file_menu.add_command(label = "Salvar...                      ", accelerator="Ctrl+S", command= lambda: utils.save_text(text_area))
file_menu.add_separator() # Adiciona um separador para melhorar a claridade dos menus
file_menu.add_command(label="Sair", command=root.destroy)
# Menu Editar
edit_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label= "Desfazer                      ", accelerator="Ctrl+Z", command=lambda: text_area.event_generate("<<Undo>>"))
edit_menu.add_separator() # Adiciona um separador para melhorar a claridade dos menus
edit_menu.add_command(label= "Recortar                      ", accelerator="Ctrl+X", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label= "Copiar                      ", accelerator="Ctrl+C", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label= "Colar                      ", accelerator="Ctrl+V", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_command(label= "Excluir                      ", accelerator="Del", command=lambda: utils.delete_selectText(text_area))
# Menu Ajuda
help_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Ajuda", menu=help_menu)
help_menu.add_command(label="Exibir Ajuda", command=open_help)
help_menu.add_separator() # Adiciona um separador para melhorar a claridade dos menus
help_menu.add_command(label="Sobre o myNotepad", command=open_about)

# < BINDS >
# Atalhos do teclado
# Arquivo
root.bind("<Control-s>", lambda e: utils.save_text(text_area, e)) #atalho de salvamento
root.bind("<Control-o>", lambda e: utils.open_file(text_area, e)) #atalho de abrir arquivos
# Editar
root.bind("<Control-z>", lambda e: text_area.event_generate("<<Undo>>")) #atalho de desfazer
root.bind("<Control-x>", lambda e: text_area.event_generate("<<Cut>>")) #atalho de cortar
root.bind("<Control-c>", lambda e: text_area.event_generate("<<Copy>>")) #atalho de copiar
root.bind("<Control-v>", lambda e: text_area.event_generate("<<Paste>>")) #atalho de colar

# --- < INICIA A APLICAÇÃO > ---
# Roda a Aplicação
text_area.focus_set()
root.mainloop()