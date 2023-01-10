from ..database import Base
from sqlalchemy import Column, Boolean, Integer

class Pokemon(Base):
	__tablename__ = "Pokemon"
	id = Column(Integer, primary_key=True, autoincrement=True)
	seen = Column(Boolean)
	catch = Column(Boolean)