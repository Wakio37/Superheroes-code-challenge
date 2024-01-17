from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)

    hero_power = db.relationship('hero_powers', backref='hero')

# add any models you may need.

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime) 

    hero_power = db.relationship('hero_powers', backref='power')

    @validates('description')
    def validate_description(self,key,description):
        if len(description) < 20:
            raise ValueError('Description must be at least 20 characters long')

        if not description:
            raise ValueError('Must provide a description')

class hero_powers(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'),nullable=False)
    power_id = db.Column(db.Integer,db.ForeignKey('powers.id'),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)

    @validates('strength')
    def validate_strength(self,key,strength):
        strengths = ["Strong", "Weak", "Average"]
        if strength not in strengths:
            raise ValueError('Strength must be "Strong", "Weak" or "Average"')
        return strength