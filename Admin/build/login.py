

from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage,Toplevel
import admin
import cadastrar
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\emanuel.20524\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_login\frame0") #altere se estiver usando em outro computador


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def abrir_janela_admin():
    admin.create_admin_window(Toplevel(window))
    window.state("withdraw") # levei 3 seculos pra descobrir que isso fecha a janela sem fechar as outras

window = Tk()
window.title("Gerenciamento de Produtos - Login")
window.geometry("1544x1024")
window.configure(bg = "#FFFFFF")
window.state("zoomed")
window.iconbitmap(r"C:\Users\emanuel.20524\Documents\GitHub\Projeto_Tkinter\Admin\build\OIP.ico") #altere se estiver usando em outro computador

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1544,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    772.0,
    402.0,
    image=image_image_1
)

canvas.create_rectangle(
    643.0,
    442.0,
    902.0,
    509.0,
    fill="#3E3333",
    outline="")

canvas.create_text(
    715.5,
    455.0,
    anchor="nw",
    text="ADMIN\n",
    fill="#FFFFFF",
    font=("Inter BoldItalic", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_janela_admin,
    relief="flat"
)
button_1.place(
    x=630.0,
    y=543.0,
    width=281.0,
    height=88.4654541015625
)
window.resizable(False, False)
window.mainloop()
