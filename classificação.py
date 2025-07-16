from tkinter import messagebox #mansagem que iram aparecer caso tenha um erro
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

cont=1
# Função para o botão
def verifica():
    global cont #vai usar a variavel global fora fa função
    #colotando dados
    try:
        nome = str(p_nome.get()) #.get vai guarda ps dados, Isso vai pegar o texto digitado em cada campo da interface.
        temperatura = float(temp.get())
        fc = int(freq_c.get())
        fr = int(Freq_r.get())
        queixap = str(queixa.get())
        dorp = int(dor.get())
    except ValueError:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente com números ou letras de acordo com os exemplos.")
        return

    #senhas
    senha = f'A{cont:03}'
    cont = cont + 1
    

    if temperatura > 38 or fc > 120 or fr > 30 or dorp > 8:
        cor = 'VERMELHO'
    elif 37.8 <= temperatura <= 38 or 111 <= fc <= 120 or 21 <= fr <= 30 or 6 <= dorp <= 8:
        cor = 'AMARELO'
    elif 36.5 <= temperatura <= 37.7 or 60 <= fc <= 100 or 16 <= fr <= 20 or 3 <= dorp <= 5:
        cor = 'AZUL'
    else:
        cor = 'VERDE'

    # Exibição do resultado    
    resumo = (
        f'senha: {senha}\n'
        f'nome: {nome}\n'
        f"Temperatura: {temperatura} °C\n"
        f"FC: {fc} bpm\n"
        f"FR: {fr} irpm\n"
        f"Dor: {dorp}/10\n"
        f"Queixa: {queixap}\n\n"
        f"Classificação de risco: {cor}"
    )

    messagebox.showinfo('resumo da triagem', resumo)


janela = ctk.CTk() #Tela inteira
janela.title("Classificação de Risco") #titulo da tela inteira
janela.geometry("500x700") #tamanho da tela/pixes

ctk.CTkLabel(janela, text='Nome do paciente:').pack() #tabel é o titulo que vai tá dentro do sistema. pady espaço. custums começam com letras maisuculas.
p_nome = ctk.CTkEntry(janela, placeholder_text= 'Ex: maria') #input, pla. texto de instrução dentro do camp de digitação.
p_nome.pack(pady=10)

ctk.CTkLabel(janela, text="Temperatura (°C):").pack() #CTk Label, ou Entry
temp = ctk.CTkEntry(janela, placeholder_text= 'Ex: 35.8')
temp.pack(pady=10)

ctk.CTkLabel(janela, text="Frequencia cardiaca (FC):").pack()
freq_c = ctk.CTkEntry(janela, placeholder_text='Ex: 60')
freq_c.pack(pady=10)

ctk.CTkLabel(janela, text='Frequencia respuratoria (FR):').pack()
Freq_r = ctk.CTkEntry(janela, placeholder_text='Ex: 16')
Freq_r.pack(pady=10)

ctk.CTkLabel(janela, text='Queixa do paciente: ').pack()
queixa = ctk.CTkEntry(janela, placeholder_text='Ex: fadiga')
queixa.pack(pady=10)

ctk.CTkLabel(janela, text='Intensidade da dor: ').pack()
dor = ctk.CTkEntry(janela, placeholder_text="De 0 a 10")
dor.pack(pady=10)


ctk.CTkButton(janela, text="Classificar", command=verifica).pack(pady=10)

janela.mainloop()