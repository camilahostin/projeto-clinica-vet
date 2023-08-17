from src.controllers.owner_screen import owner_list
from src.entities.animal import Animal

animal_list: list[Animal] = []

def animal_screen():
    print('Tela do Animal')
    print('Selecione uma das opções abaixo')
    option_str = input('[1] Cadastro Pets [2] Listagem dos pets [3] '/
                       'Atualização Cadastro do Pet [4] Remoção do Pet: ')

    try:
        option = int(option_str)
        if option == 1:
            animal_registration()
        elif option == 2:
            animal_listing()
        elif option == 3:
            animal_update()
        elif option == 4:
            animal_removal()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2, 3 ou 4.')

def animal_registration() -> list[Animal]:
    print('Tela de Cadastro de Pet')
    name = input('Nome: ')
    species = input('Espécie: ')
    weight = input('Peso: ')
    age = input('Idade: ')
    owner_name_input = input('Nome Dono(a): ')
    owner_name = _get_owner_by_name(owner_name_input)

    animal = Animal(name, species, weight, age, owner_name)
    animal_list.append(animal)

def animal_listing() -> list[Animal]:
    if len(animal_list) == 0:
        print('Lista de pets está vazia')

    print('Tela de Listagem de Pets')
    for index, animal in enumerate(animal_list):
        print(f'| {index} | {animal.name} | {animal.species} | '\
            f'{animal.weight} | {animal.age} | {animal.owner.name} |')

def animal_update():
    animal_listing()
    if len(animal_list) != []:
        update_animal = input('Digite o NOME do animal que deseja atualizar: ')
        for index, animal in enumerate(animal_list):
            if animal.name == update_animal:
                name = input('Nome: ')
                species = input('Espécie: ')
                weight = input('Peso: ')
                age = input('Idade: ')
                owner_name_input = input('Nome Dono(a): ')
                owner_name = _get_owner_by_name(owner_name_input)

                animal = Animal(name, species, weight, age, owner_name)
                animal_list[index] = animal
    else:
        print(f'O animal {update_animal} não está na lista')

def animal_removal() -> None:
    delete_animal = input('Digite o NOME do pet que deseja remover: ')

    for index, animal in enumerate(animal_list):
        if animal.name == delete_animal:
            del animal_list[index]

def _get_owner_by_name(owner_name_input: str):
    for owner in owner_list:
        if owner.name == owner_name_input:
            return owner
