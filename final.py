with open(ARQUIVO, "r") as f:
        for linha in f:
            nome, matricula, nota1, nota2, media, status = linha.strip().split(";")
            if matricula == matricula_busca:
                print(f"\nAluno encontrado:")
                print(f"Nome: {nome}")
                print(f"Matrícula: {matricula}")
                print(f"Notas: {nota1}, {nota2}")
                print(f"Média: {media}")
                print(f"Status: {status}")
                encontrado = True
                break

    if not encontrado:
        print("❌ Aluno não encontrado.")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

main()
