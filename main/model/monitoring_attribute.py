from .. import db

class MonitoringAttribute(db.Model):
    """ Monitoring Attribute Model for storing feedback attribute related details """
    __tablename__ = "monitoring_attribute"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    buildings_id = db.Column(db.Integer, db.ForeignKey('buildings.id', ondelete='CASCADE'), nullable=False)
    buildings = db.relationship('Buildings', backref=db.backref('buildings', lazy='dynamic'))
    timestamp = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.String(50), nullable=True)
    function = db.Column(db.String(50), nullable=True)
    height = db.Column(db.Float, nullable=True)
    contributor = db.Column(db.String(50), nullable=False)
    verified_on = db.Column(db.DateTime, nullable=True)
    validator = db.Column(db.String(50), nullable=True)
    reason = db.Column(db.String(50), nullable=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id', ondelete='CASCADE'), nullable=False)
    status = db.relationship('Status', backref=db.backref('status_attribute', lazy='dynamic'))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'user_id'}