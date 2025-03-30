from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

convection = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention = convection)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"
    
    serialize_rules = ("-hero_powers.power",)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    
    hero_powers = db.relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")
   
    
    def __repr__(self):
        return f"<Power {self.id}, {self.name}, {self.description}, {self.hero_powers}>"
    
    @validates("description")
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError(f"Description: {key} should be at least 20 characters long")
        return description


class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"
    
    serialize_rules = ("-hero_powers.hero",)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    
    hero_powers = db.relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Hero {self.id}, {self.name}, {self.super_name}, {self.hero_powers}>"
    


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"
    
    serialize_rules = ("-power.hero_powers", "-hero.hero_powers")
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    strength = db.Column(db.String)  
    
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))

    power = db.relationship("Power", back_populates="hero_powers")
    hero = db.relationship("Hero", back_populates="hero_powers")
    
    def __repr__(self):
        return f"<HeroPower {self.id}, {self.hero_id}, {self.power_id}, {self.strength}>"
    
    @validates("strength")
    def validate_strength(self, key, strength):
        if strength not in ["Strong", "Average", "Weak"]:
            raise ValueError(f"Strength: {key} should be either Strong, Average or Weak")
        
        return strength



 # heroes = db.relationship("Hero", secondary=hero_power, back_populates='powers')


    # powers = db.relationship("Power", secondary=hero_power, back_populates='heroes')
    
#    @property
#     def description(self):
#         return self._description
#     @description.setter




#     @property
#     def strength(self):
#         return self._strength
#     @strength.setter
#     def strength(self, val):
#         if val not in ["Strong", "Weak", "Average"]:
#             raise ValueError("Strength must be either Strong, Weak or Average")
#         self._strength = val 


