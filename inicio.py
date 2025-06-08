import os

ARQUIVO = "alunos.txt"

def menu():
    print("\n--- MENU ---")
    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno por matrícula")
    print("4. Sair")
    return input("Escolha uma opção: ")

def adicionar_aluno():
    nome = input("Nome do aluno: ").strip()
    matricula = input("Matrícula: ").strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    status = "Aprovado" if media >= 6 else "Reprovado"

    linha = f"{nome};{matricula};{nota1};{nota2};{media:.2f};{status}\n"

    with open(ARQUIVO, "a") as f:
        f.write(linha)
    print("✅ Aluno adicionado com sucesso!")

def listar_alunos():
    if not os.path.exists(ARQUIVO):
        print("Nenhum aluno cadastrado.")
        return

    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
        if not linhas:
            print("Nenhum aluno cadastrado.")
            return

        print("\n--- LISTA DE ALUNOS ---")
        for linha in linhas:
            nome, matricula, nota1, nota2, media, status = linha.strip().split(";")
            print(f"Nome: {nome}, Matrícula: {matricula}, Média: {media}, Status: {status}")

def buscar_aluno():
    matricula_busca = input("Digite a matrícula para buscar: ").strip()
    encontrado = False

    if not os.path.exists(ARQUIVO):
        print("Nenhum aluno cadastrado.")
        return
