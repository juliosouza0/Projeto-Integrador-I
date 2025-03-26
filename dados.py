import pandas as pd

#lista de questoes
questions = [
    ["Quem foi o responsavel pela proclamaçao da Indenpedencia do Brasil em 1822 ?", "Dom Pedro I", "Tiradentes", "Getulio Vargas", "D. Joao VI", 1],
    ["Qual e a formula para calcular a area de um triangulo?", "Rio Amazonas", "Rio Nilo", "Rio Mississipi", "Rio Yangtsé", 1]
    ["Qual e o maior rio do mundo em volume de agua ?", "A = b * h", "A = b * h / 2", "A = 2b + h", "A = (b * b) * h", 2],
    ["Quem pintou a Mona Lisa?", "Van Gogh", "Van Gogh", "Leonardo da Vinci", "Michelangelo", 3]
    ["Em que ano o Brasil foi descoberto?", "1500", "1492", "1600", "1700", 1]
    ["Quem foi o primeiro presidente dos Estados Unidos?", "Abraham Lincoln", "George Washington", "John F. Kennedy", "Thomas Jefferson", 2]
    ["Qual foi a principal causa da Primeira Guerra Mundial?", "Invasão da Polônia", "Assassinato do arquiduque Francisco Ferdinando", "Revolução Industrial", "Dissolução do Império Austro-Húngaro", 2]
    ["Qual é o elemento químico representado pelo símbolo 'O'?", "Ouro", "Oxigênio", "Ósmio", "Ozônio", 2]
    ["Qual é o maior planeta do sistema solar?", "Terra", "Saturno", "Júpiter", "Urano", 3]
    
    
    
    
    
    
    
    
    
    ]

#Criando dataframes do pandas
df = pd.DataFrame(questions, columns=["Perguntas", "Opcao 1", "Opcao 2", "Opcao 3", "Opcao 4", "Resposta"])

#Salvar no arquivo excel
df.to_excel("questions.xlsx", index=False)

print ("Perguntas Inseridas com Sucesso")