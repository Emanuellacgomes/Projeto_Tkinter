from pathlib import Path
from tkinter import Canvas, Text, Button, PhotoImage, Toplevel, StringVar, Entry, messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\emanuel.20524\Documents\GitHub\Projeto_Tkinter\Admin\build\assets_cadastrar\frame0") #mude o usuario necessario
global button_image_1, button_image_2, button_image_3, button_image_4

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_cadastrar_window(window):
    global button_image_1, button_image_2, button_image_3, button_image_4
    window.geometry("1542x850")
    window.configure(bg = "#FFFFFF")
    window.state("zoomed")
    window.title("Gerenciamento de Produtos - Cadastrar")
    window.iconbitmap(r"C:\Users\emanuel.20524\Documents\GitHub\Projeto_Tkinter\Admin\build\OIP.ico") #mude o usuario necessario

    caminho_button_1 = relative_to_assets("button_1.png")
    caminho_button_2 = relative_to_assets("button_2.png")
    caminho_button_3 = relative_to_assets("entry_1.png")
    caminho_button_4 = relative_to_assets("entry_2.png")

    # Mantenha uma referência às imagens para evitar coleta de lixo
    button_image_1 = PhotoImage(file=caminho_button_1)
    button_image_2 = PhotoImage(file=caminho_button_2)
    button_image_3 = PhotoImage(file=caminho_button_3)
    button_image_4 = PhotoImage(file=caminho_button_4)

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
        0.0,
        0.0,
        1542.0,
        121.0,
        fill="#D9D9D9",
        outline=""
    )

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
        outline=""
    )

    canvas.create_text(
        175.0,
        141.0,
        anchor="nw",
        text="Insira o ID:",
        fill="#000000",
        font=("Itim Regular", 48 * -1)
    )

    entry_bg_1 = canvas.create_image(
        971.5,
        173.5,
        image=button_image_3
    )

    # Função de validação
    def only_numbers(char):
        return char.isdigit()

    # Registre a função de validação
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

    canvas.create_rectangle(
        171.0,
        519.0,
        401.0,
        624.0,
        fill="#A09AD4",
        outline=""
    )

    canvas.create_rectangle(
        171.0,
        320.0,
        401.0,
        425.0,
        fill="#A09AD4",
        outline=""
    )

    canvas.create_text(
        180.0,
        550.0,
        anchor="nw",
        text="Estoque:",
        fill="#000000",
        font=("Itim Regular", 31 * -1)
    )

    canvas.create_text(
        171.0,
        355.0,
        anchor="nw",
        text="Nome do Produto:\n",
        fill="#000000",
        font=("Itim Regular", 31 * -1)
    )

    entry_bg_2 = canvas.create_image(
        971.5,
        372.5,
        image=button_image_4
    )
    entry_2 = Text(
        window,
        bd=0,
        bg="#8F8AC0",
        fg="#000716",
        font=("Arial", 30),  # Mantido o tamanho da fonte
        highlightthickness=0
    )
    entry_2.place(
        x=401.0,
        y=320.0,
        width=1141.0,
        height=103.0
    )

    entry_estoque = Entry(
        window,
        bd=0,
        bg="#8F8AC0",
        fg="#000716",
        font=("Arial", 30),
        highlightthickness=0,
        validate="key",
        validatecommand=(validate_command, '%S')
    )
    entry_estoque.place(
        x=401.0,
        y=519.0,
        width=1141.0,
        height=103.0
    )

    def save_to_db():
        id_value = entry_1.get()
        nome_imovel = entry_2.get("1.0", "end-1c")
        estoque = entry_estoque.get()
        
        if id_value and nome_imovel and estoque:
            try:
                conexao_banco = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="imobiliaria"
                )
                cursor = conexao_banco.cursor()

                insert_query = "INSERT INTO dados (id, nome, estoque) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (id_value, nome_imovel, estoque))

                conexao_banco.commit()
                cursor.close()
                conexao_banco.close()

                messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {err}")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=save_to_db,
        relief="flat"
    )
    button_1.place(
        x=1150.0,
        y=693.0,
        width=339.0,
        height=103.0
    )

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

    window.resizable(False, False)
    window.mainloop()
