from datetime import datetime

from src.core.database import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str]
    
    email: Mapped[str]
    username: Mapped[str]
    
    birthdate : Mapped[datetime]

    hashed_password: Mapped[str]