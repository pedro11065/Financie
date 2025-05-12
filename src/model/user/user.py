from sqlalchemy import String
from sqlalchemy import Date

from sqlalchemy import LargeBinary

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

import bcrypt, uuid

from psycopg2 import Binary
from datetime import datetime

from src.settings.cript import Crypt
from src.settings.db import Base

from sqlalchemy.dialects.postgresql import UUID


class User:

    lgpd_consent : bool
    created_at : datetime
    updated_at : datetime 
    deleted_at : datetime

    def __init__(self, fullname, cpf, phone, email, password, birthday):

        self.uuid : str = None
        self.fullname : str = fullname
        self.cpf : str = Crypt().decrypt(cpf)
        self.phone : str = Crypt().decrypt(phone)
        self.email : str = email
        self.password : str = password
        self.birthday : str = birthday


        self.to_table = table_users(

            id=str(uuid.uuid4()),
            fullname=self.fullname,
            cpf=Crypt().decrypt(self.cpf), # .encrypt(self.cpf)
            phone=Crypt().decrypt(self.phone), # .encrypt(self.phone)
            email=self.email,
            password=bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode(),
            birthday=self.birthday,
            lgpd_consent=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None
        )
        
class table_users(Base):

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fullname: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    birthday: Mapped[str] = mapped_column(Date, nullable=False)
    cpf: Mapped[bytes] = mapped_column(LargeBinary, nullable=False, unique=True)
    phone: Mapped[bytes] = mapped_column(LargeBinary, nullable=False, unique=False)
    lgpd_consent: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[datetime] = mapped_column(Date, nullable=True)

    def __repr__(self):
        return f'User(id={self.id!r}, fullname={self.fullname!r}, email={self.email!r}, password={self.password!r}, birthday={self.birthday!r}, cpf={self.cpf!r}, phone={self.phone!r}, lgpd_consent={self.lgpd_consent!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r}, deleted_at={self.deleted_at!r})'
