import datetime
from scr.controllers.animal_screen import animal_list
from scr.controllers.veterinarian_screen import veterinarian_list
from scr.entities.schedule_treatment import ScheduleTreatment

schedule_treatment_list: list[ScheduleTreatment] = []

def schedule_treatment_screen():
    print('Tela da Agenda')
    print('Selecione uma das opções abaixo')
    option_str = input('[1] Agendamento [2] Listagem Agenda [3] Excluir agendamento: ')

    try:
        option = int(option_str)
        if option == 1:
            schedule_treatment()
        elif option == 2:
            schedule_listing()
        elif option == 3:
            schedule_removal()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2 ou 3.')

def schedule_treatment() -> list[ScheduleTreatment]:
    print('Tela de Agendamento')
    animal_name_input = input('Nome Pet: ')
    animal_name = _get_animal_by_name(animal_name_input)

    vet_name_input = input('Nome Veterinário: ')
    vet_name = _get_veterinarian_by_name(vet_name_input)

    datetime_str = input('Marque um horário "Dia/Mês/Ano Hora:Minutos" : ')
    datetime_ = datetime.datetime.strptime(datetime_str, '%d/%m/%Y %H:%M')

    notes = input('Anotações: ')

    schedule = ScheduleTreatment(animal_name, vet_name, datetime_, notes)
    schedule_treatment_list.append(schedule)

    # enviar email
    # send_email(animal_name, datetime_str)

def schedule_listing() -> list[ScheduleTreatment]:
    if len(schedule_treatment_list) == 0:
        print('Agenda está vazia')

    print('Agenda Tratamentos')
    for index, treatment in enumerate(schedule_treatment_list):
        print(f'| {index} | {treatment.animal.name} | {treatment.veterinarian.name} | '\
              f'{treatment.datetime_} | {treatment.notes}')

def schedule_removal() -> None:
    delete_schedule = input('Digite o nome do PET para remoção do agendamento: ')

    for index, treatment in enumerate(schedule_treatment_list):
        if treatment.animal.name == delete_schedule:
            del schedule_treatment_list[index]

    # enviar email

def send_email(animal_name: str, datetime_str: datetime):
    pass


def _get_animal_by_name(animal_name_input: str):
    for animal in animal_list:
        if animal.name == animal_name_input:
            return animal

def _get_veterinarian_by_name(vet_name_input: str):
    for veterinarian in veterinarian_list:
        if veterinarian.name == vet_name_input:
            return veterinarian
