# função para validar o sexo do atleta
def validar_sexo():
    while True:
        sexo = input("Sexo (F/M): ").upper()
        if sexo == 'F' or sexo == 'M':
            return sexo
        else:
            print("Valor inválido! Favor digitar F ou M.")

# função para validar altura e peso do atleta
def validar_dado(mensagem):
    while True:
        dado = float(input(mensagem))
        if dado > 0:
            return dado
        else:
            print("Valor inválido! Favor digitar um valor positivo.")

# leitura da quantidade de atletas
n = int(input("Qual a quantidade de atletas? "))

# inicialização das variáveis
soma_pesos = 0
maior_altura = 0
nome_maior_altura = ''
qtde_mulheres = 0
soma_altura_mulheres = 0

# leitura dos dados dos atletas
for i in range(1, n+1):
    print(f"Digite os dados do atleta número {i}:")
    nome = input("Nome: ")
    sexo = validar_sexo()
    altura = validar_dado("Altura: ")
    peso = validar_dado("Peso: ")

    # atualização das variáveis de acordo com o sexo do atleta
    soma_pesos += peso
    if altura > maior_altura:
        maior_altura = altura
        nome_maior_altura = nome
    if sexo == 'F':
        qtde_mulheres += 1
        soma_altura_mulheres += altura

# cálculo das médias e porcentagem
if qtde_mulheres > 0:
    altura_media_mulheres = soma_altura_mulheres / qtde_mulheres
    print(f"Altura média das mulheres: {altura_media_mulheres:.2f}")
else:
    print("Não há mulheres cadastradas.")

peso_medio = soma_pesos / n
porcentagem_homens = (n - qtde_mulheres) / n * 100

# impressão do relatório
print(f"Peso médio dos atletas: {peso_medio:.2f}")
print(f"Atleta mais alto: {nome_maior_altura}")
print(f"Porcentagem de homens: {porcentagem_homens:.1f} %")
