from .. import db

class Monitoring(db.Model):
    """ Monitoring Model for storing feedback monitoring related details """
    __tablename__ = "monitoring"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    gml_id = db.Column(db.String(50), nullable=False)
    attribute = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.String(100), db.ForeignKey('user.public_id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('user', lazy='dynamic'))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'user_id'}