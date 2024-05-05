
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,String, ForeignKey

Base = declarative_base()


class Authors(Base):
    __tablename__ = 'Authors'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    born_date = Column(String)
    born_location = Column(String)
    description = Column(String)

    quotes = relationship("Quotes", back_populates="author_ref")


class Quotes(Base):
    __tablename__ = 'Quotes'
    id = Column(Integer, primary_key=True)
    tags = Column(String)
    author = Column(String, ForeignKey('Authors.fullname'))
    quote = Column(String)

    author_ref = relationship("Authors", back_populates='quotes')