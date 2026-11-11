from funcoes import inicializar_arquivo, cadastrar_make, listar_makes, registrar_venda

def menu():
    inicializar_arquivo()
    
    while True:
        print("\n==============================")
        print("   ✨ LOJA DE MAKES - MENU ✨")
        print("==============================")
        print("1 - Cadastrar nova make")
        print("2 - Ver estoque")
        print("3 - Registrar venda")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto (ex: Gloss Labial): ")
            marca = input("Marca (ex: Franciny Ehlke): ")
            preco = float(input("Preço (ex: 39.90): ").replace(",", "."))
            qtd = int(input("Quantidade em estoque: "))
            cadastrar_make(nome, marca, preco, qtd)

        elif opcao == "2":
            listar_makes()

        elif opcao == "3":
            listar_makes()
            try:
                num = int(input("\nDigite o número do produto vendido: "))
                qtd = int(input("Quantidade vendida: "))
                registrar_venda(num, qtd)
            except ValueError:
                print("\n❌ Digite apenas números válidos.")

        elif opcao == "0":
            print("\nEncerrando o sistema... Até mais! 👋")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
