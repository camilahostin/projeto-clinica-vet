from scr.entities.veterinarian import Veterinarian

veterinarian_list: list[Veterinarian] = []

def veterinarian_screen():
    print('Tela do(a) Veterinário(a)')
    print('Selecione uma das opções abaixo')
    option_str = input('[1] Cadastro Veterinário [2] Listagem [3] Remoção: ')

    try:
        option = int(option_str)
        if option == 1:
            veterinarian_registration()
        elif option == 2:
            veterinarian_listing()
        elif option == 3:
            veterinarian_removal()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2 ou 3.')

def veterinarian_registration() -> list[Veterinarian]:
    print('Tela de Cadastro de Veterinário(a)')
    name = input('Nome: ')
    crmv = input('CRMV: ')
    cpf = input('CPF: ')
    address = input('Endereço: ')
    telephone = input('Telefone: ')

    veterinarian = Veterinarian(name, crmv, cpf, address, telephone)
    veterinarian_list.append(veterinarian)

def veterinarian_listing() -> list[Veterinarian]:
    if len(veterinarian_list) == 0:
        print('Lista de veterinários está vazia')

    print('Tela de Listagem de Veterinários')
    for index, veterinarian in enumerate(veterinarian_list):
        print(f'| {index} | {veterinarian.name} | {veterinarian.crmv} | '\
              f'{veterinarian.cpf} | {veterinarian.address} | {veterinarian.telephone} |')

def veterinarian_removal() -> None:
    delete_veterinarian = input('Digite o CRMV do veterinário que deseja remover: ')

    for index, veterinarian in enumerate(veterinarian_list):
        if veterinarian.crmv == delete_veterinarian:
            del veterinarian_list[index]
