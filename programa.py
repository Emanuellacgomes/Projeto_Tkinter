from tkinter import *
programa = Tk()
####### Programa - Configuração e Parâmetros #######
programa.title("Gerenciamento de Imovéis - Modo Administrador")
programa.state('zoomed')
programa.iconbitmap("OIP_1.ico")
programa.configure(background="#87cbff")
####### Programa - Botões e Lógica #######
programa.frame_1 = Frame(bd = 3, bg = "#47ff72")

programa.frame_1.place(relx = 0.02 ,rely = 0.02 ,relheight = 0.96 ,relwidth = 0.46)

programa.frame_2 = Frame(bd = 3, bg = "#e6ff99" )

programa.frame_2.place(relx = 0.50, rely = 0.02, relheight = 0.96, relwidth = 0.48)

programa.botao_entrar = Button(programa.frame_1,text="Entrar")
programa.botao_entrar.place()

programa.botao_sair = Button(programa.frame_2,text="Sair")
programa.botao_sair.place()

programa.mainloop()