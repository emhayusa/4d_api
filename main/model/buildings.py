from .. import db

class Buildings(db.Model):
    """ Buildings Model for storing building related details """
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gml_id = db.Column(db.String(100), unique=True)
    city_gml_id = db.Column(db.Integer, db.ForeignKey('city_gml.id', ondelete='CASCADE'), nullable=False)
    city_gml = db.relationship('CityGml', backref=db.backref('city_gml', lazy='dynamic'))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id'}