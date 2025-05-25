from usuarios import cadastrar_usuario, listar_usuarios
from carros import cadastrar_carro, listar_carros
from pecas import cadastrar_pecas
from estoque import listar_movimentacao, movimentar_estoque, verificar_estoque_baixo

def menu():
    while True:
        print("\n ---- MENU ----")
        print('1. cadastrar usuario')
        print('2. cadastrar carro')
        print('3. cadastrar peça')
        print('4. movimentar estoque')
        print('5. verificar estoque minimo')
        print('6. listar usuario')
        print('7. listar carros')
        print('8. listar movimentaços de estoque ')
        print('0. sair ')
        op= input ('escolha uma opcao: ')

        if op== '1':
            cadastrar_usuario()
        elif op=='2':
            cadastrar_carro()
        elif op=='3':
            cadastrar_pecas()
        elif op=='4':
            movimentar_estoque()
        elif op=='5':
            verificar_estoque_baixo()
        elif op=='6':
            listar_usuarios()
        elif op== '7':
            listar_carros()
        elif op== '8':
            listar_movimentacao()
        elif op=='0':
            break
        else:
            print('opcao invalida')


if __name__== "__main__":
    menu()

