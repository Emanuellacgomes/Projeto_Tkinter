from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
global button_image_1, button_image_2, button_image_3, button_image_4

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_cadastrar\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
caminho_button_1 = relative_to_assets(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_cadastrar\frame0\button_1.png")
caminho_button_2 = relative_to_assets(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_cadastrar\frame0\button_2.png")
caminho_button_3 = relative_to_assets(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_cadastrar\frame0\entry_1.png")
caminho_button_4 = relative_to_assets(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_cadastrar\frame0\entry_2.png")

# Mantenha uma referência às imagens para evitar coleta de lixo
button_image_1 = PhotoImage(file=caminho_button_1)
button_image_2 = PhotoImage(file=caminho_button_2)
button_image_3 = PhotoImage(file=caminho_button_3)
button_image_4 = PhotoImage(file=caminho_button_4)



def create_cadastrar_window(window):
    window.geometry("1542x850")
    window.configure(bg = "#FFFFFF")
    window.state("zoomed")
    window.title("Gerenciamento de Imovéis - Cadastrar")
    window.iconbitmap(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\OIP.ico")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 850,
        width = 1542,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1542.0,
        850.0,
        fill="#AFB9E4",
        outline="")

    canvas.create_rectangle(
        0.0,
        121.0,
        171.0,
        850.0,
        fill="#C1C6DF",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        1542.0,
        121.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        56.0,
        25.0,
        anchor="nw",
        text="CADASTRAR:",
        fill="#000000",
        font=("Itim Regular", 64 * -1)
    )

    canvas.create_rectangle(
        171.0,
        121.0,
        401.0,
        226.0,
        fill="#A09AD4",
        outline="")

    canvas.create_text(
        175.0,
        141.0,
        anchor="nw",
        text="Insira o ID:",
        fill="#000000",
        font=("Itim Regular", 48 * -1)
    )

    entry_image_1 = PhotoImage(("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        971.5,
        173.5,
        image=button_image_3
    )
    entry_1 = Text(
        bd=0,
        bg="#8F8AC0",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=401.0,
        y=121.0,
        width=1141.0,
        height=103.0
    )

    canvas.create_rectangle(
        171.0,
        519.0,
        401.0,
        624.0,
        fill="#A09AD4",
        outline="")

    canvas.create_rectangle(
        171.0,
        320.0,
        401.0,
        425.0,
        fill="#A09AD4",
        outline="")

    canvas.create_text(
        180.0,
        550.0,
        anchor="nw",
        text="Disponibilidade:",
        fill="#000000",
        font=("Itim Regular", 31 * -1)
    )

    canvas.create_text(
        171.0,
        355.0,
        anchor="nw",
        text="Nome do Imóvel:\n",
        fill="#000000",
        font=("Itim Regular", 31 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        971.5,
        372.5,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#8F8AC0",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=401.0,
        y=320.0,
        width=1141.0,
        height=103.0
    )

    canvas.create_rectangle(
        401.0,
        519.0,
        1542.0,
        624.0,
        fill="#8F8AC0",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=1150.0,
        y=693.0,
        width=339.0,
        height=103.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy(),
        relief="flat"
    )
    button_2.place(
        x=196.0,
        y=693.0,
        width=338.0,
        height=103.0
    )
    window.resizable(False, False)
    window.mainloop()