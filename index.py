# Definindo a variável para armazenar o nome e a experiência do herói
nome = input("Informe o nome do herói: ")
xp = int(input("Informe a experiência do herói: "))  # Experiência do herói

# Usando estrutura de decisão para determinar o nível do herói
if xp < 1000:
    nivel = "Ferro"
elif 1000 < xp <= 2000:
    nivel = "Bronze"
elif 2000 < xp <= 5000:
    nivel = "Prata"
elif 5000 < xp <= 7000:
    nivel = "Ouro"
elif 7000 < xp <= 8000:
    nivel = "Platina"
elif 8000 < xp <= 9000:
    nivel = "Ascendente"
elif 9000 < xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"


print(f"O Herói de nome **{nome}** está no nível de **{nivel}**")