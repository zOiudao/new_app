from InquirerPy import prompt
from database.db_config import stm
from database.user_crud import user_menu


class Menu:
    def principal(self, msg):
        stm('clear')
        print(''.center(50, '-'))
        print('MENU PRINCIPAL'.center(50))
        print(''.center(50, '-'))
        menu = [
            {
                'type': 'list',
                'message': msg,
                'choices': ['Usuários', 'Funcionários', 'Sair'],
                'name': 'menu',
            }
        ]
        escolha = prompt(menu)
        if escolha['menu'] == 'Usuários':
            user_menu()
        if escolha['menu'] == 'Funcionários':
            ...
        if escolha['menu'] == 'Sair':
            stm('clear')
            return print('Sistema encerrado')
        return escolha['menu']