import pandas as pd

# Lista de questões
questions = [
    ["Quem foi o responsável pela Proclamação da Independência do Brasil em 1822?", "Dom Pedro I", "Tiradentes", "Getúlio Vargas", "D. João VI", 1],
    ["Qual é a fórmula para calcular a área de um triângulo?", "Rio Amazonas", "Rio Nilo", "Rio Mississipi", "Rio Yangtsé", 1],
    ["Qual é o maior rio do mundo em volume de água?", "A = b * h", "A = b * h / 2", "A = 2b + h", "A = (b * b) * h", 2],
    ["Quem pintou a Mona Lisa?", "Van Gogh", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo", 3],
    ["Em que ano o Brasil foi descoberto?", "1500", "1492", "1600", "1700", 1],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "Abraham Lincoln", "George Washington", "John F. Kennedy", "Thomas Jefferson", 2],
    ["Qual foi a principal causa da Primeira Guerra Mundial?", "Invasão da Polônia", "Assassinato do arquiduque Francisco Ferdinando", "Revolução Industrial", "Dissolução do Império Austro-Húngaro", 2],
    ["Qual é o elemento químico representado pelo símbolo 'O'?", "Ouro", "Oxigênio", "Ósmio", "Ozônio", 2],
    ["Qual é o maior planeta do sistema solar?", "Terra", "Saturno", "Júpiter", "Urano", 3],
    ["Qual país tem o maior número de ilhas no mundo?", "Suécia", "Indonésia", "Canadá", "Grécia", 1],
    ["Quem é o autor de 'Harry Potter'?", "J.R.R. Tolkien", "Suzanne Collins", "J.K. Rowling", "George R.R. Martin", 3],
    ["Qual banda lançou o álbum 'Abbey Road'?", "The Rolling Stones", "Queen", "The Beatles", "Pink Floyd", 3],
    ["Quem é conhecido como o 'Rei do Pop'?", "Elvis Presley", "Michael Jackson", "Prince", "Stevie Wonder", 2],
    ["Em que esporte Michael Jordan se destacou?", "Futebol", "Tênis", "Basquete", "Natação", 3],
    ["Qual é o maior continente em termos de área?", "África", "Ásia", "América", "Europa", 2]
]

# Criando DataFrame do pandas
df = pd.DataFrame(questions, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

# Salvar no arquivo Excel
df.to_excel("questions.xlsx", index=False)

print("Perguntas Inseridas com Sucesso")
