from conexao import conectar

def movimentar_estoque():
    conexao = conectar()
    cursor = conexao.cursor() #variavel responsável por executar comandos SQL

    cpf = input('Digite seu CPF: ')
    # Verificando se o CPF informado pelo usuario esta na base de dados
    cursor.execute('SELECT id, tipo FROM usuarios WHERE cpf = %s', (cpf,))
    usuario = cursor.fetchone()

    if not usuario:
        print('\n-------- USUÁRIO NÃO ENCONTRADO --------')
        return

    usuario_id, tipo = usuario
    if tipo != 'estoquista':
        print('ACESSO RESTRITO APENAS PARA ESTOQUISTAS.')
        return

    # toda vez que usamos o fetchall ele recupera os dados do BD em 
    # forma de tupla, por exemplo do for abaixo:
    #[{'id': 1, 'nome': 'Parafuso', 'qtd_estoque': 150}]
    cursor.execute('SELECT id, nome, qtd_estoque FROM pecas')
    for p in cursor.fetchall():
        print(f'{p[0]} - {p[1]} (estoque: {p[2]})')

    peca_id = int(input('Digite o ID da peça: '))
    tipo_movi = input('Tipo de movimentação (entrada ou saída): ').strip().lower()
    qtd = int(input('Digite a quantidade: '))

    # Verificando se tem a peça em estoque
    if tipo_movi == 'saida':
        cursor.execute('SELECT qtd_estoque, estoque_min FROM pecas WHERE id = %s', (peca_id,))
        dados = cursor.fetchone()
        if not dados:
            print('------------ PEÇA NÃO ENCONTRADA --------')
            return

        # Como estamos lidando com TUPLA
        # a variavel atual ocupa a posição [0] ou seja (qtd_estoque)
        # a variavel minimo ocupa a posição [1] ou seja (estoque_min)
        atual, minimo = dados
        # Se a quantidade de saída que o usuario digitou for maior
        # Do que tem no estoque ele devolve estoque insuficiente
        if qtd > atual:
            print('---------- ERRO: ESTOQUE INSUFICIENTE --------')
            return

        # Se a quantidade de estoque for maior do que usuario digitou
        # então atualizamos o novo valor de estoque com UPDATE
        novo_estoque = atual - qtd
        cursor.execute('UPDATE pecas SET qtd_estoque = %s WHERE id = %s', (novo_estoque, peca_id))

        # O usuario ira receber uma mensagem quando o estoque estiver
        # abaixo do estoque minimo declarado
        if novo_estoque < minimo:
            print(f'ESTOQUE DA PEÇA {peca_id} ABAIXO DO MÍNIMO ({novo_estoque} < {minimo})')

    # Se o usuario digitou entrada temos que fazer uma conta de adição
    # atualizando o valor da coluna qtd_estoque
    elif tipo_movi == 'entrada':
        cursor.execute('UPDATE pecas SET qtd_estoque = qtd_estoque + %s WHERE id = %s', (qtd, peca_id))
    else:
        print('Tipo de movimentação inválido.')
        return

    cursor.execute('INSERT INTO estoque_movimentacao (peca_id, usuario_id, tipo_movimentacao, qtd) VALUES (%s, %s, %s, %s)', 
                   (peca_id, usuario_id, tipo_movi, qtd))

    # comando para salvar a operação
    conexao.commit()
    print('Movimentação registrada com sucesso.')

    cursor.close()
    conexao.close()


def verificar_estoque_baixo():
    conexao = conectar()
    cursor = conexao.cursor() #variavel responsável por executar comandos SQL

    cursor.execute('SELECT nome, qtd_estoque, estoque_min FROM pecas WHERE qtd_estoque < estoque_min')
    resultados = cursor.fetchall()

    # Lembrando que resultado é uma TUPLA
    # e temos que acessar ela conforme as colunas corretas
    if resultados:
        print('\nPEÇAS COM ESTOQUE ABAIXO DO MÍNIMO:')
        for nome, atual, minimo in resultados:
            print(f'- {nome}: {atual} em estoque (mínimo: {minimo})')
    else:
        print('Todos os estoques estão dentro do limite mínimo.')

    # fechando as conexões
    cursor.close()
    conexao.close()


def listar_movimentacao():
    conexao = conectar()
    cursor = conexao.cursor() #variavel responsável por executar comandos SQL

    # A query abaixo busca o histórico de movimentações no estoque,
    #  mostrando o nome do usuário, o nome da peça, 
    # o tipo de movimentação (entrada ou saída), 
    # a quantidade e a data
    cursor.execute('''
        SELECT m.id, u.nome, p.nome, m.tipo_movimentacao, m.qtd, m.data_movimentacao 
        FROM estoque_movimentacao m
        JOIN usuarios u ON m.usuario_id = u.id 
        JOIN pecas p ON m.peca_id = p.id
        ORDER BY m.data_movimentacao DESC
    ''')
    
    # Movimentação vem como forma de TUPLA temos que acessar as colunas
    # com o nome da variavel do for acompanho de []
    movimentacao = cursor.fetchall()
    print('\n-------- HISTÓRICO DE MOVIMENTAÇÃO --------')
    for m in movimentacao:
         print(f'ID: {m[0]} | Usuário: {m[1]} | Peça: {m[2]} | Tipo: {m[3]} | Qtd: {m[4]} | Data: {m[5]}')

    # Fechando as conexões
    cursor.close()
    conexao.close()
