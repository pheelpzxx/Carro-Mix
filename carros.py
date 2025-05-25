from conexao import conectar

def cadastrar_carro():
    conexao = conectar()
    cursor = conexao.cursor() #variavel responsável por executar comandos SQL

    modelo = input('Escreva o modelo do seu veículo: ')
    marca = input('Escreva a marca do seu veículo: ')
    ano = int(input('Digite o ano do seu veículo: '))

    sql = """
        INSERT INTO carros 
        (modelo, marca, ano)
        VALUES (%s, %s, %s)
    """
    # Executa o comando SQL, 
    # substituindo os %s pelos valores inseridos pelo usuário
    cursor.execute(sql, (modelo, marca, ano)) 
    conexao.commit()
    print('VEÍCULO CADASTRADO COM SUCESSO')

    # Fechando as conexões abertas
    cursor.close()
    conexao.close()


def listar_carros():
    comm = conectar()
    cursor = comm.cursor()
    cursor.execute('SELECT id, modelo, marca, ano FROM carros')
    # Comando fetchall() = Pega todos os registros retornados pelo banco e coloca na variável carros
    carros = cursor.fetchall()

    # a variavel carros é virou uma TUPLA, então devemos fazer o acesso
    # dos campos usando [] pois como temos 4 colunas dentro da tupla devemos específicar qual coluna queremos
    # Exemplo: (1, 'Civic', 'Honda', 2020)
    print('\n--------- LISTA DE CARROS ---------')
    for carro in carros:
        print(f'ID: {carro[0]} | Modelo: {carro[1]} | Marca: {carro[2]} | Ano: {carro[3]}')

    # Fechando as conexões abertas
    cursor.close()
    comm.close()
