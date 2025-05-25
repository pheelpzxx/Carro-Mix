from conexao import conectar

def cadastrar_pecas():
    conexao = conectar()
    cursor = conexao.cursor() #variavel responsável por executar comandos SQL

    nome = input('Digite o nome da sua peça: ')
    marca = input('Escreva a marca da sua peça: ')
    valor = float(input('Digite o valor da peça: '))
    qtd_estoque = int(input('Digite a quantidade de estoque: '))
    estoque_min = int(input('Digite a quantidade de estoque mínimo: '))

    # Buscando todos os carros cadastrados trazendo somente ID e MODELO
    cursor.execute('SELECT id, modelo FROM carros')
    carros = cursor.fetchall()
    print('\n---------------- CARROS DISPONÍVEIS -------------')

    # Lembrando que a variavel carros esta em formato de uma TUPLA
    # Exemplo [(1, 'Fusca')]
    # tem o campo [0] que é o ID do carro
    # e tem o campo [1] que é o MODELO do carro
    for carro in carros:
        print(f'ID: {carro[0]} - Modelo: {carro[1]}')
    carro_id = int(input('Digite o ID do veículo vinculado: '))

    # Montando a query para realizar o insert na tabela pecas
    sql = """
        INSERT INTO pecas 
        (nome, marca, valor, qtd_estoque, estoque_min, carro_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Executando o comando para inserir os dados
    cursor.execute(sql, (nome, marca, valor, qtd_estoque, estoque_min, carro_id))

    # Salvando o comando executado
    conexao.commit()
    print('PEÇA CADASTRADA COM SUCESSO.')

    # Fechando as conexões
    cursor.close()
    conexao.close()
