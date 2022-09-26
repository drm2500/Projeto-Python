import os
lista_de_alunos = []
loop_decisao = 1

def cadastrar_aluno():
    os.system('cls')
    id = int(input('Digite o ID do aluno: '))
    nome = input('Digite o nome do aluno: ')
    cpf = input('Digite o CPF do aluno: ')
    data_nascimento = input('Digite a data de nascimento do aluno: ')
    curso = input('Digite o curso do aluno: ')
    aluno={'id':id,'nome':nome,'cpf':cpf,'data_nascimento':data_nascimento,'curso':curso}
    lista_de_alunos.append(aluno)

    
    while loop_decisao == 1:
        decisao = input('Deseja cadastrar um novo aluno? S/N: ').lower()
        if decisao == 's':
            cadastrar_aluno()
        if decisao == 'n':
            menu()

def remover_aluno():
    os.system('cls')
    id_aluno = int(input('Digite o ID do aluno que deseja remover: '))
    contador = 0
    for aluno in lista_de_alunos:
        if aluno['id'] == id_aluno:
            lista_de_alunos.pop(contador)
            print('Aluno removido com sucesso')
        contador+=1

    while loop_decisao == 1:
        decisao = input('Deseja remover mais um aluno? S/N: ').lower()
        if decisao == 's':
            remover_aluno()
        if decisao == 'n':
            menu()

def mostrar_aluno(aluno):
    print(f" ID: {aluno['id']}\n NOME: {aluno['nome']}\n CPF:{aluno['cpf']}\n Data de nascimento: {aluno['data_nascimento']}\n Curso: {aluno['curso']}")
    print('-----------------------------------------------------------------')

def listar_aluno():
    os.system('cls')
    for aluno in lista_de_alunos:
        mostrar_aluno(aluno)
    while loop_decisao == 1:
        sair = input("pressione 'S' para sair: ").lower()
        if sair == 's':
            menu()
    
  
def atualizar_aluno():
    os.system('cls')
    id = int(input('Digite o ID do aluno que deseja atualizar o cadastro: '))
    for aluno in lista_de_alunos:
        if aluno['id'] == id:
            mostrar_aluno(aluno)

            novo_nome = input('Digite o novo nome: ')
            novo_cpf = input('Digite o novo CPF: ')
            nova_data = input('Digite o nova Data de nascimento: ')
            novo_curso = input('Digite o novo Curso: ')

            aluno['nome'] = novo_nome
            aluno['cpf'] = novo_cpf
            aluno['data_nascimento'] = nova_data
            aluno['curso'] = novo_curso

    while loop_decisao == 1:    
        decisao = input('Deseja atualizar mais um aluno? S/N: ').lower()
        if decisao == 's':
            atualizar_aluno()
        if decisao == 'n':
            menu()


def menu():
    os.system('cls')
    print('### Menu ###')
    print('1 - Cadastrar #')
    print('2 - Remover #')
    print('3 - Listar #')
    print('4 - Atualizar #')
    print('5 - Fechar #')
    print('## ------ ##')

    opcao = int(input('Digite a operação: '))

    if opcao == 1:
        cadastrar_aluno()

    elif opcao == 2:
        remover_aluno()

    elif opcao == 3:
        listar_aluno()

    elif opcao == 4:
        atualizar_aluno()

    elif opcao == 5:
        quit()
    else:
        menu()
menu()



