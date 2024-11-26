from .db_config import User, session, ftime, stm
from rich.table import Table
from rich import print

class UserCRUD:    
    def create(self):        
        tb = Table(title='Cadastrado com sucesso!', show_lines=True, style='#370617', title_style='#6A040F')
        tb_header = ['nome', 'email', 'hora']
        for _, v in enumerate(tb_header):
            tb.add_column(v.title(), style='#E85D04', header_style='#6A040F')
        try:
            nome = str(input('Nome completo: ')).strip().title()
            email = str(input('Email: ')).strip().lower()
            pwd = str(input('Senha: ')).strip()
            
            c = User(nome, email, pwd)
            stm('clear')
            session.add(c)
            session.commit()
            tb.add_row(c.name, c.email, c.data.strftime(ftime))
            print(tb)
        except Exception as e:
            print(f'Erro! {type(e)} \n--{e}')
        finally:
            return
        

    def read(self):
        tb = Table(title='Usuários cadastrados!', show_lines=True, style='#370617', title_style='#6A040F')
        tb_header = ['nome', 'email', 'hora']
        for _, v in enumerate(tb_header):
            tb.add_column(v.title(), style='#E85D04', header_style='#6A040F')
        for i in session.query(User).all():
            tb.add_row(i.name, i.email, i.data.strftime(ftime))
        return print(tb)