import psycopg2
import hashlib
import random
import string

# Variáveis de conexão com o banco de dados
DB_HOST = "localhost" # Endereço do banco de dados
DB_PORT = 5432 # Porta do banco de dados
DB_NAME = "dataanonymization" # Nome do banco de dados
DB_USER = "seu_usuario" # Usuário do banco de dados
DB_PASSWORD = "sua_senha" # Senha do banco de dados

# Função para gerar uma string aleatória
def gerar_string_aleatoria(tamanho):
    letras = string.ascii_letters
    return ''.join(random.choice(letras) for _ in range(tamanho))

# Função para criptografar um valor usando SHA256
def criptografar_valor(valor):
    valor = str(valor)
    valor_criptografado = hashlib.sha256(valor.encode('utf-8')).hexdigest()
    return valor_criptografado

# Função para mascarar um valor substituindo caracteres por asteriscos
def mascarar_valor(valor):
    if isinstance(valor, str):
        return '*' * len(valor)
    else:
        return valor

# Função para generalizar um valor substituindo letras por 'X' e números por '0'
def generalizar_valor(valor):
    valor_generalizado = ''
    for char in valor:
        if char.isalpha():
            valor_generalizado += 'X'
        elif char.isdigit():
            valor_generalizado += '0'
        else:
            valor_generalizado += char
    return valor_generalizado

# Função para anonimizar um valor
def anonimizar_valor(valor, metodo):
    if metodo == "criptografar":
        return criptografar_valor(valor)
    elif metodo == "mascarar":
        return mascarar_valor(valor)
    elif metodo == "generalizar":
        return generalizar_valor(valor)
    else:
        return valor

# Função para verificar a conexão com o banco de dados
def verificar_conexao_banco():
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Conexão com o banco de dados estabelecida com sucesso.")
        return conexao
    except psycopg2.Error as e:
        print("Ocorreu um erro ao conectar ao banco de dados:", e)
        return None

# Função para anonimizar os dados
def anonimizar_dados(metodo, tabela, campo, conexao):
    if conexao is None:
        return
    
    cursor = conexao.cursor()

    try:
        cursor.execute(f"SELECT {campo} FROM {tabela}")
        registros = cursor.fetchall()

        for registro in registros:
            valor = registro[0]
            valor_anonimizado = anonimizar_valor(valor, metodo)
            
            cursor.execute(f"UPDATE {tabela} SET {campo} = %s WHERE {campo} = %s", (valor_anonimizado, valor))

        conexao.commit()
    
    except psycopg2.Error as e:
        print("Ocorreu um erro durante a anonimização dos dados:", e)
    
    finally:
        cursor.close()

# Função para selecionar a tabela
def selecionar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tabelas = [tabela[0] for tabela in cursor.fetchall()]
    print("Tabelas disponíveis:")
    for idx, tabela in enumerate(tabelas, 1):
        print(f"{idx}. {tabela}")
    opcao = input("Digite o número da tabela desejada: ")
    return tabelas[int(opcao) - 1]

# Função para selecionar o campo
def selecionar_campo(tabela, conexao):
    cursor = conexao.cursor()
    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tabela}'")
    campos = [campo[0] for campo in cursor.fetchall()]
    del campos[0]  # Remove o primeiro campo (ID)
    print("Campos disponíveis:")
    for idx, campo in enumerate(campos, 1):
        print(f"{idx}. {campo}")
    opcao = input("Digite o número do campo desejado: ")
    return campos[int(opcao) - 1]

# Menu de opções
def imprimir_menu():
    print("Selecione o método de anonimização:")
    print("1. Criptografar")
    print("2. Mascarar")
    print("3. Generalizar")
    print("0. Sair")

# Função para selecionar a opção do usuário
def selecionar_opcao():
    imprimir_menu()
    return input("Digite o número da opção desejada: ")

# Função para encerrar a conexão com o banco de dados
def encerrar_conexao_banco(conexao):
    conexao.close()
    print("Conexão com o banco de dados encerrada com sucesso.")

# Chamada da função para anonimizar os dados
conexao = verificar_conexao_banco()
if conexao is not None:
    metodos_anonimizacao = {
        "1": "criptografar",
        "2": "mascarar",
        "3": "generalizar"
    }

    while True:
        tabela = selecionar_tabela(conexao)
        campo = selecionar_campo(tabela, conexao)
        opcao = selecionar_opcao()

        if opcao in metodos_anonimizacao:
            anonimizar_dados(metodos_anonimizacao[opcao], tabela, campo, conexao)

            if opcao == "1":
                print("Dados criptografados com sucesso!")
            elif opcao == "2":
                print("Dados mascarados com sucesso!")
            elif opcao == "3":
                print("Dados generalizados com sucesso!")
            
            break
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    encerrar_conexao_banco(conexao)
    