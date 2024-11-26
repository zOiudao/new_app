from .db_config import User, session, ftime, stm
from firulas.processo import title, barra_processo
from InquirerPy import prompt
from rich.table import Table
from rich.progress import track
from rich import print
from sqlalchemy.exc import IntegrityError, NoResultFound
from time import sleep

class UserCRUD:    
    def create(self):        
        tb = Table(title='Cadastrado com sucesso!', show_lines=True, style='#370617', title_style='#6A040F')
        tb_header = ['nome', 'email', 'hora']
        for _, v in enumerate(tb_header):
            tb.add_column(v.title(), style='#E85D04', header_style='#6A040F')
        try:
            nome = str(input('Nome completo: ')).strip().title()
            email = str(input('Email: ')).strip().lower()
            try:
                check = session.query(User).filter_by(email=email).one()
                if check:
                    return print('Email já cadastrado!')
            except NoResultFound:
                pass
            pwd = str(input('Senha: ')).strip()
            
            c = User(nome, email, pwd)
            stm('clear')
            session.add(c)
            session.commit()
            tb.add_row(c.name, c.email, c.data.strftime(ftime))
            print(tb)
        except IntegrityError:
            session.rollback()
            session.close()
            print('Erro! \n--Email já cadastrado')
        except Exception as e:
            print(f'Erro! {type(e)} \n--{e}')
        finally:
            barra_processo()
            return user_menu()
        
    def read(self):
        tb = Table(title='Usuários cadastrados!', show_lines=True, style='#370617', title_style='#6A040F')
        tb_header = ['nome', 'email', 'hora']
        for _, v in enumerate(tb_header):
            tb.add_column(v.title(), style='#E85D04', header_style='#6A040F')
        for i in session.query(User).all():
            tb.add_row(i.name, i.email, i.data.strftime(ftime))
        return print(tb)
    
    
    def update(self):
        title('usuários cadastrados')
        nome = [i.name for i in session.query(User).all()]
        menu = [
            {
                'type': 'list',
                'message': 'Selecione uma opção abaixo!',
                'choices': nome,
                'name': 'nome',
            }
        ]
        r = prompt(menu)
        name = r['nome']
        up = session.query(User).filter_by(name=name).one()
        n = input('Digite o nome para atualizar: ').strip().title()
        if n:
            up.name = n
        e = input('Digite o email para atualizar: ').strip().lower()
        if e:
            up.email = e
        s = input('Digite a senha para atualizar: ').strip()
        if s:
            up.pwd = s
        session.commit()
        barra_processo('Cadastro atualizado com sucesso!')
        return user_menu()
    
    
    def delete(self):
        title('usuários cadastrados')
        nome = [i.name for i in session.query(User).all()]
        menu = [
            {
                'type': 'list',
                'message': 'Selecione uma opção abaixo!',
                'choices': nome,
                'name': 'nome',
            }
        ]
        r = prompt(menu)
        name = r['nome']
        up = session.query(User).filter_by(name=name).one()
        if up:
            print(f'Tem certeza que deseja deletar o cadastro {name}?')
            yn = [
                {
                    'type': 'list',
                    'message': 'Selecione uma opção abaixo!',
                    'choices': ['Sim', 'Não'],
                    'name': 'yn',
                }
            ]
            r = prompt(yn)
            if r['yn'] == 'Sim':
                session.delete(up)
                session.commit()
                session.close()
                barra_processo('Cadastro deletado com sucesso!')
                return user_menu()
            else:
                session.close()
                barra_processo('Operação cancelada!')
                return user_menu()
                
            
def user_menu():
    from menu.menu import Menu
    user = UserCRUD()
    stm('clear')
    title('menu usuário')
    m = Menu()
    menu = [
        {
            'type': 'list',
            'message': 'Selecione uma opção abaixo!',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Voltar'],
            'name': 'user',
        }
    ]
    r = prompt(menu)
    if r['user'] == 'Cadastrar':
        stm('clear')
        return user.create()
    if r['user'] == 'Exibir':
        stm('clear')
        return user.read()
    if r['user'] == 'Editar':
        stm('clear')
        return user.update()
    if r['user'] == 'Deletar':
        stm('clear')
        return user.delete()
    if r['user'] == 'Voltar':
        stm('clear')
        return m.principal('Selecione uma opção abaixo!')
    return r['user']