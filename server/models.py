from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)


class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"
    
    serialization_rules = ("-heropowers",)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    
    heropowers = db.relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")
   
    
    def __repr__(self):
        return f"<Power {self.id}, {self.name}, {self.description}, {len(self.heropowers)}>"
    
    @validates("description")
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError(f"Description: {key} should be at least 20 characters long")
        return description


class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"
    
    serialization_rules = ("-heropowers",)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    
    heropowers = db.relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Hero {self.id}, {self.name}, {self.super_name}, {len(self.heropowers)}>"
    


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "heropowers"
    
    serialization_rules = ("-power", "-hero")
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    strength = db.Column(db.String)  
    
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))

    power = db.relationship("Power", back_populates="heropowers")
    hero = db.relationship("Hero", back_populates="heropowers")
    
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


