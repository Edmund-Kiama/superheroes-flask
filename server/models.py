from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
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


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    serialization_rules = ("-hero_powers.power","-hero_powers.hero",)

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    _strength = db.Column(db.String)

    hero_id = db.Column("hero_id", db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column("power_id", db.Integer, db.ForeignKey("powers.id"))

    hero = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")

    def __repr__(self):
        return f"<HeroPower {self.id}, {self.hero_id}, {self.power_id},  {self.hero}, {self.power}"

    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self, val):
        if val not in ["Strong", "Weak", "Average"]:
            raise ValueError("Strength must be either Strong, Weak or Average")
        self._strength = val 



class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    serialization_rules = ("-hero_powers.power", "-hero_powers.hero",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers = db.relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Hero {self.id}, {self.name}, {self.super_name}, {len(self.hero_powers)}"

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    serialization_rules = ("-hero_powers.power", "-hero_powers.hero",)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    _description = db.Column(db.String)
    
    hero_powers = db.relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Power {self.id}, {self.name}, {self._description}, {len(self.hero_powers)}"

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, val):
        if len(val) < 20:
            raise ValueError("Description should be at least 20 characters long")
        self._description = val


