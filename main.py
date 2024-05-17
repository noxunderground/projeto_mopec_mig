import pandas as pd

# Definindo as variáveis e suas opções
horario = ["Manhã", "Tarde", "Noite"]
fome = ["Lanche leve", "Reforçado"]
tempo = ["Rápido e prático", "Tempo para preparar"]
vontade = ["Doce", "Salgado", "Fruta", "Outro"]
ingredientes = ["Sim", "Não"]
restricoes = ["Sim", "Não"]

# Criando o dataframe vazio
df = pd.DataFrame()

# Coletando as respostas do usuário
while True:
    # Perguntas e armazenamento das respostas
    hora = input("Qual o horário do dia? (" + ", ".join(horario) + "): ")
    while hora not in horario:
        print("Opção inválida. Tente novamente.")
        hora = input("Qual o horário do dia? (" + ", ".join(horario) + "): ")

    fome_nivel = input("Qual o nível de fome? (" + ", ".join(fome) + "): ")
    while fome_nivel not in fome:
        print("Opção inválida. Tente novamente.")
        fome_nivel = input("Qual o nível de fome? (" + ", ".join(fome) + "): ")

    tempo_disp = input("Quanto tempo você tem? (" + ", ".join(tempo) + "): ")
    while tempo_disp not in tempo:
        print("Opção inválida. Tente novamente.")
        tempo_disp = input("Quanto tempo você tem? (" + ", ".join(tempo) + "): ")

    vontade_tipo = input("Qual tipo de lanche você deseja? (" + ", ".join(vontade) + "): ")
    while vontade_tipo not in vontade:
        print("Opção inválida. Tente novamente.")
        vontade_tipo = input("Qual tipo de lanche você deseja? (" + ", ".join(vontade) + "): ")

    ingredientes_disp = input("Tem os ingredientes necessários? (" + ", ".join(ingredientes) + "): ")
    while ingredientes_disp not in ingredientes:
        print("Opção inválida. Tente novamente.")
        ingredientes_disp = input("Tem os ingredientes necessários? (" + ", ".join(ingredientes) + "): ")

    restricoes_alim = input("Há restrições alimentares? (" + ", ".join(restricoes) + "): ")
    while restricoes_alim not in restricoes:
        print("Opção inválida. Tente novamente.")
        restricoes_alim = input("Há restrições alimentares? (" + ", ".join(restricoes) + "): ")

    # Armazenando as respostas no dataframe
    nova_linha = {
        "Horário": hora,
        "Fome": fome_nivel,
        "Tempo disponível": tempo_disp,
        "Vontade": vontade_tipo,
        "Ingredientes disponíveis": ingredientes_disp,
        "Restrições alimentares": restricoes_alim
    }
    df = df.append(nova_linha, ignore_index=True)

    # Perguntar se deseja adicionar mais dados
    continuar = input("Deseja adicionar mais dados? (Sim/Não): ")
    if continuar.lower() != "sim":
        break

# Processamento e predição (a ser implementado com base na sua lógica de decisão)

# Apresentando o resultado
print("\nCom base nas suas respostas, a sugestão de lanche é:")
# Imprimir a sugestão de lanche aqui

# Salvando o dataframe (opcional)
df.to_csv("dados_lanches.csv")

print("\nDados salvos no arquivo 'dados_lanches.csv'.")
