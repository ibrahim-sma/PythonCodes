import uuid
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Enum,
    Boolean,
    ARRAY,
    func,
    Numeric
)
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.ext.declarative import declarative_base
from app.db.engine import Base


# Base = declarative_base()

# -----------------------
# ENUM DEFINITIONS
# -----------------------

ExpenseTypeEnum = Enum(
    "Income",
    "Expense",
    name="expense_type_enum"
)

TransactionTypeEnum = Enum(
    "Credit",
    "Debit",
    name="transaction_type_enum"
)

TransactionModeEnum = Enum(
    "UPI",
    "NEFT",
    "IMPS",
    "CASH",
    name="transaction_mode_enum"
)


# -----------------------
# EXPENSE MODEL
# -----------------------

class Expense(Base):
    __tablename__ = "expenses"

    # Primary Key
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )

    # Business Fields
    date = Column(
        DateTime(timezone=True),
        nullable=True,
        comment="Date on which the transaction occurred"
    )

    expense_type = Column(
        ExpenseTypeEnum,
        nullable=False,
        index=True
    )

    description = Column(
        String(500),
        nullable=False
    )

    amount = Column(
        Numeric(12, 2),
        nullable=False,
        index=True,
        comment="Transaction amount"
    )


    transaction_type = Column(
        TransactionTypeEnum,
        nullable=False
    )

    transaction_mode = Column(
        TransactionModeEnum,
        nullable=False,
        index=True
    )

    category = Column(
        String(100),
        nullable=True,
        index=True
    )

    subcategory = Column(
        String(100),
        nullable=True
    )

    account = Column(
        String(255),
        nullable=False,
        index=True,
        comment="Transaction with whom"
    )

    tags = Column(
        ARRAY(String),
        nullable=True,
        comment="Tags for grouping/filtering transactions"
    )

    comments = Column(
        String(500),
        nullable=True
    )

    # Audit Fields
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False
    )

    # -----------------------
    # REPRESENTATION
    # -----------------------

    def __repr__(self) -> str:
        return (
            f"<Expense(id={self.id}, "
            f"expense_type={self.expense_type}, "
            f"transaction_type={self.transaction_type}, "
            f"mode={self.transaction_mode}, "
            f"account={self.account})>"
        )
