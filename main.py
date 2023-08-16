from scr.controllers.animal_screen import animal_screen
from scr.controllers.owner_screen import owner_screen
from scr.controllers.schedule_treatment_screen import schedule_treatment_screen
from scr.controllers.veterinarian_screen import veterinarian_screen


def run():
    print('Selecione uma das opções abaixo: ')
    option_str = input('[1] Dono [2] Animal [3] Veterinário [4] Agendamento: ')

    try:
        option = int(option_str)

        if option == 1:
            owner_screen()
        elif option == 2:
            animal_screen()
        elif option == 3:
            veterinarian_screen()
        elif option == 4:
            schedule_treatment_screen()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2, 3 ou 4.')

if __name__ == '__main__':
    while True:
        run()
