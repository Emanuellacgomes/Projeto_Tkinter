from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel
import cadastrar
import alterar
import excluir
# Variáveis globais para manter referências às imagens
global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_admin\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_admin_window(janela):
    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5

    janela.geometry("1531x850")
    janela.configure(bg="#6D88FF")
    janela.title("Gerenciamento de Imóveis - Painel Admin")
    janela.state("zoomed")
    janela.iconbitmap(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\OIP.ico") # Altere se estiver usando em outro computador
        
    def abrir_janela_cadastrar():
        cadastrar.create_cadastrar_window(Toplevel(janela))
    def abrir_janela_alterar():
        alterar.create_alterar_window(Toplevel(janela))
    def abrir_janela_excluir():
        excluir.create_excluir_window(Toplevel(janela))
    canvas = Canvas(
        janela,
        bg="#6D88FF",
        height=850,
        width=1531,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1531.0,
        850.0,
        fill="#AFB9E4",
        outline=""
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        1531.0,
        121.0,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_rectangle(
        0.0,
        121.0,
        171.0,
        850.0,
        fill="#C1C6DF",
        outline=""
    )

    canvas.create_rectangle(
        36.936,
        39.211,
        875.040,
        92.479,
        fill="#C8B9D9",
        outline=""
    )

    canvas.create_text(
        440.0,
        759.0,
        anchor="nw",
        text="Faz Log-Off do usuário e fecha o programa.",
        fill="#000000",
        font=("Itim Regular", 32 * -1)
    )

    canvas.create_text(
        68.0,
        46.0,
        anchor="nw",
        text="Olá Admin! O que você gostaria de fazer hoje?",
        fill="#000000",
        font=("Itim Regular", 48 * -1)
    )

    # Armazene os caminhos das imagens em variáveis
    caminho_button_1 = relative_to_assets("button_1.png")
    caminho_button_2 = relative_to_assets("button_2.png")
    caminho_button_3 = relative_to_assets("button_3.png")
    caminho_button_4 = relative_to_assets("button_4.png")
    caminho_button_5 = relative_to_assets("button_5.png")

    # Mantenha uma referência às imagens para evitar coleta de lixo
    button_image_1 = PhotoImage(file=caminho_button_1)
    button_image_2 = PhotoImage(file=caminho_button_2)
    button_image_3 = PhotoImage(file=caminho_button_3)
    button_image_4 = PhotoImage(file=caminho_button_4)
    button_image_5 = PhotoImage(file=caminho_button_5)

    button_1 = Button(
        janela,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_janela_alterar,
        relief="flat"
    )
    button_1.place(
        x=169.0,
        y=297.0,
        width=239.0,
        height=79.0
    )

    button_2 = Button(
        janela,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_janela_cadastrar,  # Corrigido para chamar a função
        relief="flat"
    )
    button_2.place(
        x=170.0,
        y=155.0,
        width=238.0,
        height=79.0
    )

    canvas.create_text(
        424.0,
        167.0,
        anchor="nw",
        text="Cadastra um novo Imóvel",
        fill="#000000",
        font=("Itim Regular", 36 * -1)
    )

    canvas.create_text(
        409.0,
        306.0,
        anchor="nw",
        text="Altera um Imóvel podendo-se alterar suas informações e/ou sua disponibilidade",
        fill="#000000",
        font=("Itim Regular", 32 * -1)
    )

    button_3 = Button(
        janela,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_janela_excluir,
        relief="flat"
    )
    button_3.place(
        x=167.0,
        y=452.0,
        width=241.0,
        height=79.0
    )

    canvas.create_text(
        421.0,
        619.0,
        anchor="nw",
        text="Pesquisa um Imóvel mostrando suas informações e disponibilidade",
        fill="#000000",
        font=("Itim Regular", 32 * -1)
    )

    canvas.create_text(
        432.0,
        465.0,
        anchor="nw",
        text="Exclui um Imóvel",
        fill="#000000",
        font=("Itim Regular", 36 * -1)
    )

    button_4 = Button(
        janela,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=167.0,
        y=605.0,
        width=241.0,
        height=79.0
    )

    button_5 = Button(
        janela,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: janela.destroy(),
        relief="flat"
    )
    button_5.place(
        x=171.0,
        y=747.0,
        width=253.0,
        height=63.0
    )

    janela.resizable(False, False)

if __name__ == "__main__":
    root = Tk()
    create_admin_window(root)
    root.mainloop()
