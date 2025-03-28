from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

hero_powers = db.Table(
    "hero_powers",
    metadata,
    db.Column("hero_id", db.Integer, db.ForeignKey("heroes.id"), primary_key=True),
    db.Column("power_id", db.Integer, db.ForeignKey("powers.id"), primary_key=True)
)

class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    serialization_rules = ("-powers.hero",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    powers = db.relationship("Power", secondary=hero_powers, back_populates="heroes", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Hero {self.id}, {self.name}, {self.super_name}"

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    serialization_rules = ("-heroes.power",)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    heroes = db.relationship("Hero", secondary=hero_powers, back_populates="powers", cascade="all, delete-orphan")

