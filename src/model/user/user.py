from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Uuid
from sqlalchemy import LargeBinary

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

import bcrypt, uuid

from datetime import datetime

from src.settings.security.cript import Crypt
from src.settings.db.db import Base

from sqlalchemy.dialects.postgresql import UUID


class User:

    def __init__(self, fullname, cpf, phone, email, password, birthday, id=None, lgpd_consent=None, created_at=None, updated_at=None, deleted_at=None):
        self.id: str = id
        self.fullname: str = fullname
        self.cpf: str = cpf
        self.phone: str = phone
        self.email: str = email
        self.password: str = password
        self.birthday: str = birthday
        self.lgpd_consent: bool = lgpd_consent
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at
        self.deleted_at: datetime = deleted_at

    def self_to_table(self):

        data = table_users(

            id=uuid.uuid4(),
            full_name=self.fullname,
            cpf=self.cpf,  # Directly store the binary data
            phone=self.phone,  # Directly store the binary data
            email=self.email,
            password_hash=bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode(),
            birthday=self.birthday,
            lgpd_consent=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None
        )

        return data

    def encrypt(self):
        self.cpf = Crypt().encrypt(self.cpf)
        self.phone = Crypt().encrypt(self.phone)

    def decrypt(self):
        self.cpf = Crypt().decrypt(self.cpf)
        self.phone = Crypt().decrypt(self.phone)
    

        
class table_users(Base):

    __tablename__ = "users"

    id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(60), nullable=False)
    birthday: Mapped[str] = mapped_column(Date, nullable=False)
    cpf: Mapped[bytes] = mapped_column(LargeBinary, nullable=False, unique=True)
    phone: Mapped[bytes] = mapped_column(LargeBinary, nullable=False, unique=False)
    lgpd_consent: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[datetime] = mapped_column(Date, nullable=True)

    #def __repr__(self):
     #   return f'User(id={self.id!r}, fullname={self.fullname!r}, email={self.email!r}, password={self.password!r}, birthday={self.birthday!r}, cpf={self.cpf!r}, phone={self.phone!r}, lgpd_consent={self.lgpd_consent!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r}, deleted_at={self.deleted_at!r})'

