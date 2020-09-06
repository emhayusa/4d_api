from .. import db

class Area(db.Model):
    """ Area Model for storing area related details """
    __tablename__ = "area"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_name = db.Column(db.String(50), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id'}