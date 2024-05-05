from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('sqlite:///Authors_info.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()