import os

ARQUIVO = "estoque.txt"

def inicializar_arquivo():
    # Cria o arquivo .txt caso ele ainda não exista na pasta
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            pass

def cadastrar_make(nome, marca, preco, quantidade):
    # O modo "a" (append) adiciona no final sem apagar o que já existe
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        linha = f"{nome};{marca};{preco:.2f};{quantidade}\n"
        f.write(linha)
    print(f"\n✅ '{nome}' cadastrado com sucesso!")

def listar_makes():
    inicializar_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    if not linhas:
        print("\n⚠️ O estoque está vazio.")
        return

    print("\n--- 💄 ESTOQUE DE MAKES ---")
    for i, linha in enumerate(linhas, start=1):
        nome, marca, preco, qtd = linha.strip().split(";")
        alerta = " ⚠️ (Estoque baixo!)" if int(qtd) < 3 else ""
        print(f"{i}. {nome} ({marca}) | R$ {preco} | Qtd: {qtd}{alerta}")

def registrar_venda(indice_produto, qtd_vendida):
    inicializar_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    if indice_produto < 1 or indice_produto > len(linhas):
        print("\n❌ Produto inválido.")
        return

    # Pega os dados da linha escolhida
    dados = linhas[indice_produto - 1].strip().split(";")
    nome, marca, preco, qtd_atual = dados[0], dados[1], float(dados[2]), int(dados[3])

    if qtd_vendida > qtd_atual:
        print(f"\n❌ Estoque insuficiente! Você só tem {qtd_atual} unidades.")
        return

    # Atualiza a quantidade e reescreve o arquivo
    nova_qtd = qtd_atual - qtd_vendida
    linhas[indice_produto - 1] = f"{nome};{marca};{preco:.2f};{nova_qtd}\n"

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        f.writelines(linhas)

    total = preco * qtd_vendida
    print(f"\n💰 Venda concluída! Total: R$ {total:.2f} | Restam {nova_qtd} unidades.")
