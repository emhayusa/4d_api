from .. import db

class MonitoringPhoto(db.Model):
    """ Monitoring Photo Model for storing feedback photo related details """
    __tablename__ = "monitoring_photo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    buildings_id = db.Column(db.Integer, db.ForeignKey('buildings.id', ondelete='CASCADE'), nullable=False)
    buildings = db.relationship('Buildings', backref=db.backref('buildings_photo', lazy='dynamic'))
    timestamp = db.Column(db.DateTime, nullable=False)
    photo_file = db.Column(db.String(100), nullable=False)
    contributor = db.Column(db.String(50), nullable=False)
    verified_on = db.Column(db.DateTime, nullable=True)
    validator = db.Column(db.String(50), nullable=True)
    reason = db.Column(db.String(50), nullable=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id', ondelete='CASCADE'), nullable=False)
    status = db.relationship('Status', backref=db.backref('status_photo', lazy='dynamic'))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'user_id'}