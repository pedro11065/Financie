from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Uuid
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

import uuid

from datetime import datetime

from src.settings.security.cript import Crypt
from src.settings.db.db import Base

from sqlalchemy.dialects.postgresql import UUID


class Asset:

    def __init__(self, name, description, category, status, location, user_id, created_at, id, updated_at=None, deleted_at=None):
        self.id: str = id
        self.user_id : str = user_id
        self.name : str = name
        self.description: str = description
        self.category: str = category
        self.status: str = status
        self.location: str = location
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at
        self.deleted_at: datetime = deleted_at

    def self_to_table(self):

        data = table_assets(

            id=uuid.uuid4(),
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            category=self.category,
            status=self.status,
            location=self.location,
            created_at=self.created_at,
            updated_at=datetime.now(),
            deleted_at=None

        )

        return data

        
class table_assets(Base):

    __tablename__ = "assets"

    id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[datetime] = mapped_column(Date, nullable=True)

    def __repr__(self):
       return f'User(id={self.id!r}, fullname={self.fullname!r}, email={self.email!r}, password={self.password!r}, birthday={self.birthday!r}, cpf={self.cpf!r}, phone={self.phone!r}, lgpd_consent={self.lgpd_consent!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r}, deleted_at={self.deleted_at!r})'

