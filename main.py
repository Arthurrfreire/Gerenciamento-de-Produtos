from inventory import add_product, list_products, update_product, delete_product, search_product

def main():
    while True:
        print("\n=== Gerenciamento de Produtos - AgilStore ===")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome do Produto: ")
            category = input("Categoria: ")
            quantity = input("Quantidade: ")
            price = input("Preço: ")
            add_product(name, category, quantity, price)

        elif choice == "2":
            list_products()

        elif choice == "3":
            product_id = input("ID do Produto: ")
            print("Campos disponíveis: name, category, quantity, price")
            field = input("Qual campo deseja atualizar? ")
            value = input("Novo valor: ")
            update_product(product_id, {field: value})

        elif choice == "4":
            product_id = input("ID do Produto: ")
            confirm = input(f"Tem certeza que deseja excluir o produto {product_id}? (s/n): ")
            if confirm.lower() == "s":
                delete_product(product_id)

        elif choice == "5":
            term = input("Digite o ID ou parte do nome do produto: ")
            search_product(term)

        elif choice == "6":
            print("Encerrando aplicação...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
