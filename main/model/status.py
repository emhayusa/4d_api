from .. import db

class Status(db.Model):
    """ Status Model for storing status type related details """
    __tablename__ = "status"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(50), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id'}