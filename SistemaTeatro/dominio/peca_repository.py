from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dominio.base_repository import *
from dominio.models import *

class PecaRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.model = Peca