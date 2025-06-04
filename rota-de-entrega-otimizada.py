# Produtos disponíveis
produtos_disponiveis = {
    1: {"nome": "Notebook", "preco": 3500.00},
    2: {"nome": "Mouse", "preco": 150.00},
    3: {"nome": "Teclado", "preco": 250.00},
    4: {"nome": "Monitor", "preco": 1200.00},
    5: {"nome": "Headset", "preco": 300.00}
}

# Carrinho (pilha)
carrinho = []

# Funções
def listar_produtos():
    print("\nProdutos disponíveis:")
    for pid, info in produtos_disponiveis.items():
        print(f"{pid}: {info['nome']} - R$ {info['preco']:.2f}")

def adicionar_ao_carrinho():
    try:
        produto_id = int(input("Digite o ID do produto que deseja adicionar: "))
        if produto_id in produtos_disponiveis:
            carrinho.append(produto_id)
            print(f"✅ Adicionado: {produtos_disponiveis[produto_id]['nome']}")
        else:
            print("❌ Produto não encontrado.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")

def desfazer_ultima_adicao():
    if carrinho:
        ultimo_id = carrinho.pop()
        print(f"↩️ Removido: {produtos_disponiveis[ultimo_id]['nome']}")
    else:
        print("❌ Carrinho já está vazio.")

def mostrar_carrinho():
    if not carrinho:
        print("\n🛒 Carrinho vazio.")
        return

    print("\n🛒 Produtos no carrinho:")
    total = 0
    for pid in carrinho:
        produto = produtos_disponiveis[pid]
        print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")
        total += produto['preco']
    print(f"💰 Total: R$ {total:.2f}")

# Menu principal
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Listar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Desfazer última adição")
        print("4. Ver carrinho e total")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_produtos()
        elif escolha == "2":
            listar_produtos()
            adicionar_ao_carrinho()
        elif escolha == "3":
            desfazer_ultima_adicao()
        elif escolha == "4":
            mostrar_carrinho()
        elif escolha == "5":
            print("Encerrando programa. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Iniciar programa
menu()
