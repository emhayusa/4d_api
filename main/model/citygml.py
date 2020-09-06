from .. import db

class CityGml(db.Model):
    """ City Gml Model for storing user city gml related details """
    __tablename__ = "city_gml"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contributor = db.Column(db.String(50), nullable=False)
    city_gml_file = db.Column(db.String(100), nullable=False)
    uploaded_on = db.Column(db.DateTime, nullable=False)
    verified_on = db.Column(db.DateTime, nullable=True)
    validator = db.Column(db.String(50), nullable=True)
    reason = db.Column(db.String(50), nullable=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id', ondelete='CASCADE'), nullable=False)
    status = db.relationship('Status', backref=db.backref('status', lazy='dynamic'))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id', ondelete='CASCADE'), nullable=False)
    area = db.relationship('Area', backref=db.backref('area_gml', lazy='dynamic'))
  
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'id'}