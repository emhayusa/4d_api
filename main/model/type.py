from .. import db

class Type(db.Model):
    """ Type Model for storing user type related details """
    __tablename__ = "type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(50), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id'}