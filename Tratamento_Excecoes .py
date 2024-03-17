class Item:
    def __init__(self, nome):
        self.nome = nome

class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        if item in self.itens:
            exec(f'print("Este item já está na lista de compras.")' )
        else:
            self.itens.append(item)

    def remover_item(self, item):
        try:
            self.itens.remove(item)
        except ValueError:
            raise ValueError("Este item não está na lista de compras.")

    def consultar_lista(self):
        if not self.itens:
            print("A lista de compras está vazia.")
        else:
            for item in self.itens:
                print(item.nome)


# Função principal para interação com o usuário
def main():
    lista_compras = ListaDeCompras()

    while True:
        print("\n===== Menu =====")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Consultar lista")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome_item = input("Digite o nome do item a adicionar: ")
                item = Item(nome_item)
                lista_compras.adicionar_item(item)
                print(f"{item.nome} foi adicionado à lista de compras.")

            elif opcao == "2":
                nome_item = input("Digite o nome do item a remover: ")
                item = Item(nome_item)
                lista_compras.remover_item(item)
                print(f"{item.nome} foi removido da lista de compras.")

            elif opcao == "3":
                print("\n=== Lista de Compras ===")
                lista_compras.consultar_lista()

            elif opcao == "4":
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
