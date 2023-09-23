from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)

    def update(self, entity):
        self.session.merge(entity)

    def delete(self, entity):
        self.session.delete(entity)

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, id):
        return self.session.query(self.model).get(id)