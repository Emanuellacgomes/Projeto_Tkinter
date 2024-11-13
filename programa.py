from tkinter import *
programa = Tk()
####### Programa - Configuração e Parâmetros #######
programa.title("Gerenciamento de Imovéis - Modo Administrador")
programa.state('zoomed')
programa.iconbitmap("OIP_1.ico")
programa.configure(background="#87cbff")
####### Programa - Botões e Lógica #######
programa.frame_1 = Frame(bd = 3, bg = "#47ff72")

programa.frame_1.place(relx = 0.01 ,rely = 0.02 ,relheight = 0.96 ,relwidth = 0.98)

programa.botao_cadastrar = Button(text="Cadastrar")
programa.botao_cadastrar.place(relx= 0.35, rely=0.05, relheight = 0.09, relwidth = 0.30)

programa.botao_pesquisar = Button(text="Pesquisar")
programa.botao_pesquisar.place(relx= 0.35, rely=0.30, relheight = 0.09, relwidth = 0.30)

programa.botao_alterar = Button(text="Alterar")
programa.botao_alterar.place(relx= 0.35, rely=0.55, relheight = 0.09, relwidth = 0.30)

programa.botao_excluir = Button(text="Excluir")
programa.botao_excluir.place(relx= 0.35, rely=0.80, relheight = 0.09, relwidth = 0.30)


programa.mainloop()