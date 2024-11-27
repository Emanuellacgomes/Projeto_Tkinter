from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\emanuel.20524\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_pesquisar\frame0") #mude o usuario necessario

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_pesquisar_window(window):
    window.geometry("1542x850")
    window.configure(bg = "#FFFFFF")
    window.title("Gerenciamento de Produtos - Pesquisar")
    window.state("zoomed")

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
        0.0,
        1542.0,
        121.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        56.0,
        0.0,
        anchor="nw",
        text="PESQUISAR:",
        fill="#000000",
        font=("Itim Regular", 64 * -1)
    )

    canvas.create_rectangle(
        0.0,
        121.0,
        171.0,
        850.0,
        fill="#C1C6DF",
        outline="")

    canvas.create_rectangle(
        171.0,
        121.0,
        401.0,
        226.0,
        fill="#A09AD4",
        outline="")

    canvas.create_text(
        171.0,
        121.0,
        anchor="nw",
        text="Insira o ID:",
        fill="#000000",
        font=("Itim Regular", 36 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        971.5,
        173.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        window,
        bd=0,
        bg="#8F8AC0",
        fg="#000716",
        font=("Arial", 30),
        highlightthickness=0
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
        command=lambda: search_db(entry_1.get()),
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

    canvas.create_rectangle(
        171.0,
        335.0,
        534.0,
        425.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        534.0,
        335.0,
        893.0,
        425.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        893.0,
        335.0,
        1252.0,
        425.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        171.0,
        335.0,
        anchor="nw",
        text="ID",
        fill="#000000",
        font=("Itim Regular", 64 * -1)
    )

    canvas.create_text(
        534.0,
        335.0,
        anchor="nw",
        text="NOME:",
        fill="#000000",
        font=("Itim Regular", 64 * -1)
    )

    canvas.create_text(
        897.0,
        335.0,
        anchor="nw",
        text="ESTOQUE:",
        fill="#000000",
        font=("Itim Regular", 36 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        352.5,
        523.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        window,
        bd=0,
        bg="#ECB8B8",
        fg="#000716",
        font=("Arial", 30),
        highlightthickness=0,
        state="readonly"
    )
    entry_2.place(
        x=171.0,
        y=425.0,
        width=363.0,
        height=194.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        715.5,
        523.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        window,
        bd=0,
        bg="#EF6E6E",
        fg="#000716",
        font=("Arial", 30),
        highlightthickness=0,
        state="readonly"
    )
    entry_3.place(
        x=534.0,
        y=425.0,
        width=363.0,
        height=194.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        1070.5,
        523.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        window,
        bd=0,
        bg="#FF4949",
        fg="#000716",
        font=("Arial", 30),
        highlightthickness=0,
        state="readonly"
    )
    entry_4.place(
        x=889.0,
        y=425.0,
        width=363.0,
        height=194.0
    )

    def search_db(id_value):
        if id_value:
            try:
                conexao_banco = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="imobiliaria"
                )
                cursor = conexao_banco.cursor()

                select_query = "SELECT * FROM dados WHERE id = %s"
                cursor.execute(select_query, (id_value,))
                result = cursor.fetchone()

                if result:
                    entry_2.config(state="normal")
                    entry_2.delete(0, "end")
                    entry_2.insert(0, result[0])
                    entry_2.config(state="readonly")

                    entry_3.config(state="normal")
                    entry_3.delete(0, "end")
                    entry_3.insert(0, result[1])
                    entry_3.config(state="readonly")

                    entry_4.config(state="normal")
                    entry_4.delete(0, "end")
                    entry_4.insert(0, result[2])
                    entry_4.config(state="readonly")
                else:
                    messagebox.showwarning("Atenção", "ID não encontrado no banco de dados.")

                cursor.close()
                conexao_banco.close()
                
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao buscar no banco de dados: {err}")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira um ID válido.")

    window.resizable(False, False)
    window.mainloop()
