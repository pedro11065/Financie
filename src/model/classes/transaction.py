from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Uuid
from sqlalchemy import Text
from sqlalchemy import Float

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

import uuid

from datetime import datetime

from src.model.db.DbConnect import Base

from sqlalchemy.dialects.postgresql import UUID

columns = ['redit_card_id', 'transaction_type', 'payment_method', 'payment_status', 'currency', 'amount']


class Transaction:

    def __init__(
        self,
        id,
        user_id,
        asset_id,
        liability_id,
        credit_card_id,
        statement_id,
        transaction_type,
        payment_method,
        payment_status,
        currency,
        amount,
        created_at,
        updated_at=None,
        deleted_at=None
    ):
        self.id = id
        self.user_id = user_id
        self.asset_id = asset_id
        self.liability = liability_id
        self.credit_card_id = credit_card_id
        self.statement_id = statement_id
        self.transaction_type = transaction_type
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.currency = currency
        self.amount = amount
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at


    def self_to_table(self):

        data = table_transactions(
            id=self.id,
            user_id=self.user_id,
            asset_id=self.asset_id,
            liability_id=self.liability,
            credit_card_id=self.credit_card_id,
            statement_id=self.statement_id,
            transaction_type=self.transaction_type,
            payment_method=self.payment_method,
            payment_status=self.payment_status,
            currency=self.currency,
            amount=self.amount,
            created_at=self.created_at,
            updated_at=self.updated_at,
            deleted_at=self.deleted_at
        )
        return data


# ==============================================================================

        
class table_transactions(Base):

    __tablename__ = "transactions"

    id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    asset_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), nullable=True, default=uuid.uuid4) 
    liability_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), nullable=True, default=uuid.uuid4) 
    credit_card_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True),nullable=True, default=uuid.uuid4)
    statement_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), nullable=True, default=uuid.uuid4) 
    transaction_type: Mapped[str] = mapped_column(String(20), nullable=False)
    payment_method: Mapped[str] = mapped_column(String(20), nullable=False)
    payment_status: Mapped[str] = mapped_column(String(20), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    amount: Mapped[str] = mapped_column(Float, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(Date, nullable=False)
    deleted_at: Mapped[datetime] = mapped_column(Date, nullable=True)

    def __repr__(self):
       return f'User(id={self.id!r}, fullname={self.fullname!r}, email={self.email!r}, password={self.password!r}, birthday={self.birthday!r}, cpf={self.cpf!r}, phone={self.phone!r}, lgpd_consent={self.lgpd_consent!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r}, deleted_at={self.deleted_at!r})'

