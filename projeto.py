import os
import random

class Receita:
    def __init__(self, nome, pais, ingredientes, preparo):
        self.nome = nome
        self.pais = pais
        self.ingredientes = ingredientes
        self.preparo = preparo

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"País: {self.pais}\n"
                f"Ingredientes: {self.ingredientes}\n"
                f"Modo de Preparo: {self.preparo}\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_receitas():
    lista_receitas = []
    try:
        with open('projeto.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                nome = lines[i].strip()
                pais = lines[i + 1].strip()
                ingredientes = lines[i + 2].strip()
                preparo = lines[i + 3].strip()
                receita = Receita(nome, pais, ingredientes, preparo)
                lista_receitas.append(receita)

    except FileNotFoundError:
        print("Arquivo de receitas não encontrado.")
    return lista_receitas

def salvar_receitas(lista_receitas, modo='a'):
    with open('projeto.txt', modo, encoding='utf-8') as file:
        for receita in lista_receitas:
            file.write(f"{receita.nome}\n")
            file.write(f"{receita.pais}\n")
            file.write(f"{receita.ingredientes}\n")
            file.write(f"{receita.preparo}\n")
            file.write("\n")

def salvar_receita_favorita(receita):
    with open('favoritas.txt', 'a', encoding='utf-8') as file:
        file.write(f"{receita.nome}\n")
        file.write(f"{receita.pais}\n")
        file.write(f"{receita.ingredientes}\n")
        file.write(f"{receita.preparo}\n")
        file.write("\n")

def carregar_receitas_favoritas():
    lista_favoritas = []
    try:
        with open('favoritas.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                nome = lines[i].strip()
                pais = lines[i + 1].strip()
                ingredientes = lines[i + 2].strip()
                preparo = lines[i + 3].strip()
                receita = Receita(nome, pais, ingredientes, preparo)
                lista_favoritas.append(receita)

    except FileNotFoundError:
        print("Arquivo de receitas favoritadas não encontrado.")
    return lista_favoritas

def salvar_receitas_favoritas(lista_favoritas, modo='w'):
    with open('favoritas.txt', modo, encoding='utf-8') as file:
        for receita in lista_favoritas:
            file.write(f"{receita.nome}\n")
            file.write(f"{receita.pais}\n")
            file.write(f"{receita.ingredientes}\n")
            file.write(f"{receita.preparo}\n")
            file.write("\n")

def adicionar_receita(lista_receitas):
    clear_screen()
    nome = input("\nDigite o nome da receita: ")
    pais = input("Digite o país de origem: ")
    ingredientes = input("Digite os ingredientes utilizados na receita: ")
    preparo = input("Digite o modo de preparo da receita: ")
    nova_receita = Receita(nome, pais, ingredientes, preparo)
    lista_receitas.append(nova_receita)
    salvar_receitas([nova_receita])  # Salva apenas a nova receita em modo de append
    print("Nova receita adicionada")

def visualizar_receitas(lista_receitas):
    clear_screen()
    if not lista_receitas:
        print("Nenhuma receita cadastrada ainda.")
    else:
        pais_filtro = input("Digite o país para filtrar as receitas ou pressione Enter para ver todas: ")
        print("=== RECEITAS ===")
        idx = 1
        for receita in lista_receitas:
            if not pais_filtro or pais_filtro.lower() == receita.pais.lower():
                print(f"{idx}. {receita}")
                print()
                idx += 1

def atualizar_receita(lista_receitas):
    clear_screen()
    visualizar_receitas(lista_receitas)
    if not lista_receitas:
        return
    posicao = int(input("Digite a posição da receita que deseja atualizar: ")) - 1
    if 0 <= posicao < len(lista_receitas):
        receita = lista_receitas[posicao]
        print("=== ATUALIZAR RECEITA ===")
        print("1. Nome")
        print("2. País")
        print("3. Ingredientes")
        print("4. Modo de Preparo")
        escolha = input("Digite o número do campo que deseja atualizar: ")
        if escolha == "1":
            receita.nome = input("Digite o novo nome: ")
        elif escolha == "2":
            receita.pais = input("Digite o novo país: ")
        elif escolha == "3":
            receita.ingredientes = input("Digite os novos ingredientes: ")
        elif escolha == "4":
            receita.preparo = input("Digite o novo modo de preparo: ")
        salvar_receitas(lista_receitas, 'w')  # Reescreve todo o arquivo com as alterações
        print("Receita atualizada")
    else:
        print("Posição inválida")

def excluir_receita(lista_receitas):
    clear_screen()
    visualizar_receitas(lista_receitas)
    if not lista_receitas:
        return
    posicao = int(input("Digite a posição da receita que deseja excluir: ")) - 1
    if 0 <= posicao < len(lista_receitas):
        del lista_receitas[posicao]
        salvar_receitas(lista_receitas, 'w')  # Reescreve todo o arquivo com as receitas restantes
        print("Receita excluída")
    else:
        print("Posição inválida")

def sugerir_receita_aleatoria(lista_receitas):
    clear_screen()
    if not lista_receitas:
        print("Nenhuma receita cadastrada.")
    else:
        receita = random.choice(lista_receitas)
        print("=== SUGESTÃO DE RECEITA ===")
        print(receita)

def favoritar_receita(lista_receitas):
    clear_screen()
    visualizar_receitas(lista_receitas)
    if not lista_receitas:
        return
    posicao = int(input("Digite a posição da receita que deseja favoritar: ")) - 1
    if 0 <= posicao < len(lista_receitas):
        receita = lista_receitas[posicao]
        salvar_receita_favorita(receita)
        print("Receita favoritada")
    else:
        print("Posição inválida")

def visualizar_receitas_favoritas():
    clear_screen()
    lista_favoritas = carregar_receitas_favoritas()
    if not lista_favoritas:
        print("Nenhuma receita favoritada ainda.")
    else:
        print("=== RECEITAS FAVORITADAS ===")
        idx = 1
        for receita in lista_favoritas:
            print(f"{idx}. {receita}")
            print()
            idx += 1

def desfavoritar_receita():
    clear_screen()
    lista_favoritas = carregar_receitas_favoritas()
    if not lista_favoritas:
        print("Nenhuma receita favoritada ainda.")
        return
    visualizar_receitas(lista_favoritas)
    posicao = int(input("Digite a posição da receita que deseja desfavoritar: ")) - 1
    if 0 <= posicao < len(lista_favoritas):
        del lista_favoritas[posicao]
        salvar_receitas_favoritas(lista_favoritas, 'w')  # Reescreve o arquivo de favoritas sem a receita removida
        print("Receita desfavoritada")
    else:
        print("Posição inválida")

def menu():
    lista_receitas = carregar_receitas()
    while True:
        CRUD = input("Deseja adicionar, visualizar, atualizar, excluir ou favoritar receitas? Digite S para sim e N para não. ").upper()
        if CRUD == "S":
            escolha = input("""Digite A para adicionar uma nova receita.
Digite V para visualizar as receitas.
Digite T para atualizar as receitas.
Digite E para excluir alguma receita.
Digite R para sugerir uma receita aleatória.
Digite F para favoritar uma receita.
Digite VF para visualizar receitas favoritadas.
Digite DF para desfavoritar uma receita.
Digite Q para sair.
""").upper()
            if escolha == "A":
                adicionar_receita(lista_receitas)
            elif escolha == "V":
                visualizar_receitas(lista_receitas)
            elif escolha == "T":
                atualizar_receita(lista_receitas)
            elif escolha == "E":
                excluir_receita(lista_receitas)
            elif escolha == "R":
                sugerir_receita_aleatoria(lista_receitas)
            elif escolha == "F":
                favoritar_receita(lista_receitas)
            elif escolha == "VF":
                visualizar_receitas_favoritas()
            elif escolha == "DF":
                desfavoritar_receita()
            elif escolha == "Q":
                break
            else:
                print("Escolha inválida")
        elif CRUD == "N":
            break
        else:
            print("Escolha inválida")


if __name__ == "__main__":
    menu()
