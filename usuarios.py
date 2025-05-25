from conexao import conectar

def cadastrar_usuario():
    conexao = conectar()
    cursor = conexao.cursor() #variavel responsável por executar comandos SQL

    nome = input('Digite o seu nome: ')
    cpf = input('Digite o seu CPF: ')
    tipo = input('CLIENTE OU ESTOQUISTA: ').strip().lower()
    telefone = input('Digite o seu Telefone: ')
    endereco = input('Digite o seu endereço: ')
    data_nascimento = input('Digite a sua data de nascimento (YYYY-MM-DD): ')

    # Montando a query para inserir usuario na tabela usuarios
    sql = """
        INSERT INTO usuarios
        (nome, cpf, tipo, telefone, endereco, data_nascimento)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Executando o comando com a query acima já montada
    cursor.execute(sql, (nome, cpf, tipo, telefone, endereco, data_nascimento))

    # Salvando o comando executado
    conexao.commit()
    print('USUÁRIO CADASTRADO COM SUCESSO')

    # Fechando conexões
    cursor.close()
    conexao.close()


def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor() #variavel responsável por executar comandos SQL

    # Criando variavel para ser executada no banco de dados
    cursor.execute('SELECT id, nome, cpf, tipo, telefone, endereco, data_nascimento FROM usuarios')
    usuarios = cursor.fetchall()

    # Lembrando que a variavel usuarios esta em formato de TUPLA
    # Ou seja temos que acessar ela através de []
    # Temos 7 colunas para cada usuario, assim abaixo estamos pegando todos colocando uma legenda na frente
    # para identificar o nome do campo
    print('\n--------- LISTA DE USUÁRIOS ---------')
    for usuario in usuarios:
        print(f'ID: {usuario[0]} | Nome: {usuario[1]} | CPF: {usuario[2]} | Tipo: {usuario[3]} | '
              f'Telefone: {usuario[4]} | Endereço: {usuario[5]} | Data de Nascimento: {usuario[6]}')

    # Fechando as conexões
    cursor.close()
    conexao.close()

