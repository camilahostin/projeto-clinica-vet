from src.entities.owner import Owner

owner_list: list[Owner] = []

def owner_screen():
    print('Tela do Dono(a)')
    print('Selecione uma das opções abaixo')
    option_str = input('[1] Cadastro Dono [2] Listagem [3] Atualização Cadastral [4] Remoção: ')

    try:
        option = int(option_str)
        if option == 1:
            owner_registration()
        elif option == 2:
            owner_listing()
        elif option == 3:
            owner_update()
        elif option == 4:
            owner_removal()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2, 3 ou 4.')

def owner_registration() -> list[Owner]:
    print('Tela de Cadastro de Cliente')
    name = input('Nome: ')
    cpf = input('CPF: ')
    address = input('Endereço: ')
    telephone = input('Telefone: ')
    email = input('Email: ')

    owner = Owner(name, cpf, address, telephone, email)
    owner_list.append(owner)

def owner_listing() -> list[Owner]:
    if len(owner_list) == 0:
        print('Lista de clientes está vazia')

    print('Tela de Listagem de Clientes')
    for index, owner in enumerate(owner_list):
        print(f'| {index} | {owner.name} | {owner.cpf} | {owner.address} | '\
            f'{owner.telephone} | {owner.email} |')

def owner_update():
    owner_listing()
    if len(owner_listing) != []:
        update_owner = input('Digite o CPF do cliente que deseja atualizar: ')
        for index, owner in enumerate(owner_list):
            if owner.cpf == update_owner:
                name = input('Nome: ')
                cpf = input('CPF: ')
                address = input('Endereço: ')
                telephone = input('Telefone: ')
                email = input('Email: ')

                owner = Owner(name, cpf, address, telephone, email)
                owner_list[index] = owner
    else:
        print(f'Essa CPF {update_owner} não está na lista')

def owner_removal() -> None:
    delete_owner = input('Digite o CPF do cliente que deseja remover: ')

    for index, owner in enumerate(owner_list):
        if owner.cpf == delete_owner:
            del owner_list[index]
