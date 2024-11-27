from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Emanuel\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_excluir\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def only_numbers(char):
    return char.isdigit()

def create_excluir_window(window):
    window.geometry("1542x850")
    window.configure(bg = "#FFFFFF")
    window.state("zoomed")
    window.title("Gerenciamento de Imóveis - Excluir")
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
        text="EXCLUIR:",
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
        171.0,
        145.5,
        anchor="nw",
        text="Insira o ID:",
        fill="#000000",
        font=("Itim Regular", 48 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        971.5,
        173.5,
        image=entry_image_1
    )

    validate_command = window.register(only_numbers)

    entry_1 = Entry(
        window,
        bd=0,
        bg="#8F8AC0",
        fg="#000716",
        font=("Arial", 30),
        highlightthickness=0,
        validate="key",
        validatecommand=(validate_command, '%S')
    )
    entry_1.place(
        x=401.0,
        y=121.0,
        width=1141.0,
        height=103.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
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
        window,
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

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        794.0,
        412.0,
        image=image_image_1
    )

    canvas.create_text(
        439.0,
        568.0,
        anchor="nw",
        text="Cuidado! Essa Ação é irreversível",
        fill="#000000",
        font=("Itim Regular", 48 * -1)
    )

    window.resizable(False, False)
    window.mainloop()
