from tkinter import messagebox #mansagem que iram aparecer caso tenha um erro/avisos
import customtkinter as ctk
from datetime import datetime  # Para registrar a data e hora

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

cont=1
# Função para o botão
def verifica():
    global cont #
    #colotando dados
    #converte todos como se fosse texto 
    nome = p_nome.get().strip() #.get vai guarda ps dados, Isso vai pegar o texto digitado em cada campo da interface.
    temperatura = temp.get().strip()
    fc = freq_c.get().strip()
    fr = Freq_r.get().strip() # strip irá converter todos os caracteres em texto
    queixap = queixa.get().strip()
    dorp = dor.get().strip()

    #verificando de algum campo está vazio
    if not all([nome, temperatura, fc, fr, queixap, dorp]):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    #os numeros que foram lidos como texto vão se converte em numeros
    try:
        temperatura = float(temperatura)
        fc = int(fc)
        fr = int(fr)
        dorp = int(dorp)
    except ValueError:
        messagebox.showerror("Erro", "Preencha os campos numéricos corretamente (Temperatura, FC, FR, Dor).")
        return
    

    #senhas
    senha = f'A{cont:03}'
    cont = cont + 1
    

    if temperatura > 38 or fc > 120 or fr > 30 or dorp > 8:
        cor = 'VERMELHO'
    elif 37.8 <= temperatura <= 38 or 101 <= fc <= 120 or 21 <= fr <= 30 or 7 <= dorp <= 8:
        cor = 'AMARELO'
    else:
        cor = 'VERDE'




    # Captura da data e hora
    data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M")

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

    messagebox.showinfo('Resumo da triagem', resumo)

    # NOVO: Adiciona os dados na tabela
    linha = len(tabela_frame.winfo_children()) // len(colunas) + 1
    valores = [senha, nome, cor, data_hora]
    for i, valor in enumerate(valores):
        item = ctk.CTkLabel(tabela_frame, text=valor, anchor="w")
        item.grid(row=linha, column=i, padx=10, pady=2)

    

    #salvando em arquivo
    with open("triagens.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("=-=-=-= TRIAGEM =-=-=-=\n")
        arquivo.write(f"Data/Hora: {data_hora}\n")
        arquivo.write(f'Senha: {senha}\n')
        arquivo.write(f'Nome: {nome}\n')
        arquivo.write(f"Temperatura: {temperatura} °C\n")
        arquivo.write(f"FC: {fc} bpm\n")
        arquivo.write(f"FR: {fr} irpm\n")
        arquivo.write(f"Dor: {dorp}/10\n")
        arquivo.write(f"Queixa: {queixap}\n")
        arquivo.write(f"Classificação de risco: {cor}\n")
        arquivo.write("=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")


janela = ctk.CTk() #Tela inteira
janela.title("Classificação de Risco") #titulo da tela inteira
janela.geometry("1000x700") #tamanho da tela/pixes


# Título da tela
ctk.CTkLabel(janela, text="Sistema de Classificação de Risco", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))

# Frame para organizar o formulário
formulario = ctk.CTkFrame(janela)
formulario.pack(side="left",padx=20, pady=20, fill="both", expand=True)

# Campos
ctk.CTkLabel(formulario, text='Nome do paciente:', font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
p_nome = ctk.CTkEntry(formulario, placeholder_text='Ex: Maria')
p_nome.pack(pady=(0, 10))

ctk.CTkLabel(formulario, text="Temperatura (°C):", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
temp = ctk.CTkEntry(formulario, placeholder_text='Ex: 35.8')
temp.pack(pady=(0, 10))

ctk.CTkLabel(formulario, text="Frequência Cardíaca (FC):", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
freq_c = ctk.CTkEntry(formulario, placeholder_text='Ex: 80')
freq_c.pack(pady=(0, 10))

ctk.CTkLabel(formulario, text='Frequência Respiratória (FR):', font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
Freq_r = ctk.CTkEntry(formulario, placeholder_text='Ex: 16')
Freq_r.pack(pady=(0, 10))

ctk.CTkLabel(formulario, text='Queixa do paciente:', font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
queixa = ctk.CTkEntry(formulario, placeholder_text='Ex: fadiga')
queixa.pack(pady=(0, 10))

ctk.CTkLabel(formulario, text='Intensidade da dor (0 a 10):', font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
dor = ctk.CTkEntry(formulario, placeholder_text='Ex: 6')
dor.pack(pady=(0, 10))

# Botão
ctk.CTkButton(formulario, text="Classificar Paciente", command=verifica, fg_color="green", hover_color="darkgreen").pack(pady=20)

# Frame de tabela para exibir triagens feitas
tabela_frame = ctk.CTkScrollableFrame(janela, height=250)
tabela_frame.pack(side="right",padx=20, pady=(20), fill="both", expand=True)

# Cabeçalho da tabela
colunas = ["Senha", "Nome", "Classificação", "Data/Hora"]
for i, nome_coluna in enumerate(colunas):
    label = ctk.CTkLabel(tabela_frame, text=nome_coluna, font=ctk.CTkFont(size=12, weight="bold"))
    label.grid(row=0, column=i, padx=10, pady=5)

janela.mainloop()

