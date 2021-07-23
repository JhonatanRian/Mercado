from os import system
from time import sleep
from typing import List, Dict
from models.produto import Produto
from util.help import formata_din

produtos: List[Produto] = list()
carrinho: List[Dict[Produto, int]] = list()

def main() -> None:
    menu()
    
def menu() -> None:
    system("clear")
    print(60*"=")
    print(" Bem vindo(a) ".center(60,"="))
    print("Lojão popular".center(60, "="))
    print(60*"=")
    print("Selecione uma opção abaixo".center(60))
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produtos")
    print("4 - Visualizar carrinho")
    print("5 - Fechar pedido")
    print("6 - Sair do sistema")
    
    opcao: int = int(input("\n»» "))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produtos()
    elif opcao == 4:
        visualisar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        exit(0)
    else:
        print("Opção inválida, tente novamente")
        sleep(2)
        menu()
            
    

def cadastrar_produto() -> None:
    system("clear")
    print(60*"=")
    print("Cadastro de produto".center(60, "="))
    print(60*"=")
    nome: str = input("Informe o nome do produto.\n»» ")
    preco: float = float(input("Informe o preço do produto\n»» "))
    
    produto: Produto = Produto(nome, preco)
    produtos.append(produto)
    
    print(f"O produto {nome} foi cadastrado(a) com sucesso!")
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print("Listagem de produtos".center(60, " "))
        print(60*"-")
        for produto in produtos:
            print(produto)
            print("---------------------")
        
    else:
        print("Sem produtos cadastrados")
        print(60*"-")
        sleep(2)
        menu()
    sleep(5)
    menu()

def comprar_produtos() ->   None:
    if len(produtos) > 0:
        system("clear")
        print("Informe o código do produto que deseja adicionar no carrinho")
        print(60*"=")
        print("produtos disponíveis".center(60, "="))
        for produto in produtos:
            print(produto)
            print(60*"=")
        codigo: int = int(input("»» "))
        
        produto: Produto = pegar_por_codigo(codigo)
        
        if produto:
            if len(carrinho) > 0:
                true_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'no carinho, {produto.nome}: {quant+1}')
                        true_carrinho = True
                        sleep(2)
                        menu()
                if not true_carrinho:
                    prod: dict = {produto: 1}
                    carrinho.append(prod)
                    print(f'{produto.nome} foi adicionado ao carrinho')
            else:
                item: dict = {produto: 1}
                carrinho.append(item)
                print(f'{produto.nome} foi adicionadoao carrinho')
                sleep(2)
                menu()
        else:
            print(f"O produto {codigo} não foi encontrado")
        
        sleep(2)
        menu()
        
        
    else:
        print("Não existe produtos para vender")
        
    sleep(2)
    menu()

def visualisar_carrinho() -> None:
    if len(carrinho) > 0:
        system("clear")
        print("Produtos no carrinho".center(60, "="))
        for item in carrinho:
            for dado in item.items():
                print(dado[0])
                print(f'Quantidade: {dado[1]}')
                print(60*"=")
                sleep(1)
    else:
        print("Não existe produtos no carrinho")
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print("Produtos do carrinho".center(60, " "))
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print(60*"=")
        
        print(f"Total da compra: {formata_din(valor_total)}")
        print("Até mais")
        carrinho.clear()
        sleep(2)
                
    else:
        print("Sem produtos para fechar a compra")
    sleep(2)
    menu()

def pegar_por_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    
    return p

if __name__ == "__main__":
    main() 