import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_excel('questions.xlsx')
questions = df.sample(n=15).values.tolist()

#Criacao da janela
janela = tk.Tk()
janela.title('Jogo de Perguntas e Respostas')
janela.geometry("800x600")

#cores do quiz
background_color = "#ECECEC"
text_color = "333333"
button_color = "#4CAF50"
janela.config(bg = background_color)
janela.option_add('Font', 'Arial')

janela.mainloop()