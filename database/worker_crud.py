from .db_config import Worker, session, ftime
from rich.table import Table
from rich import print


class WorkerCRUD:
    def create(self):
        tb = Table(title='Cadastrado com sucesso!', show_lines=True, style='#370617', title_style='#6A040F')
        tb_header = ['nome', 'empresa', 'funcional', 'hora']
        for _, v in enumerate(tb_header):
            tb.add_column(v.title(), style='#E85D04', header_style='#6A040F')
        name = str(input('Nome do funcionário: ')).title().strip()
        enterprise = str(input('Empresa: ')).title().strip()
        worker_id = str(input('Funcional: ')).title().strip()
        try:
            c = Worker(name, enterprise, worker_id)
            session.add(c)
            session.commit()
            tb.add_row(c.name, c.enterprise, c.worker_id, c.data.strftime(ftime))
            print(tb)
        except Exception as e:
            print(f'Erro! {type(e)} \n--{e}')
        finally:
            return