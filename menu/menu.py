from InquirerPy import prompt
from database import user_crud, worker_crud
from database.db_config import stm

user = user_crud.UserCRUD()
work = worker_crud.WorkerCRUD()

class Menu:
    def principal(self, msg):
        print(f"{'MENU PRINCIPAL':=^50}")
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
            user.create()
        if escolha['menu'] == 'Funcionários':
            work.create()
        if escolha['menu'] == 'Sair':
            stm('clear')
            return print('Sistema encerrado')
        return escolha['menu']