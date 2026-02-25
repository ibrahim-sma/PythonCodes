from datetime import datetime
from typing import List, Optional, Literal
from uuid import UUID
from decimal import Decimal

from pydantic import BaseModel, Field


# -----------------------
# BASE CONFIG
# -----------------------

class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True,  # ORM compatibility
        "populate_by_name": True
    }


# -----------------------
# ENUM-LIKE CONSTANTS
# -----------------------

ExpenseType = Literal["Income", "Expense"]
TransactionType = Literal["Credit", "Debit"]
TransactionMode = Literal["UPI", "NEFT", "IMPS", "CASH"]


# -----------------------
# REQUEST SCHEMAS
# -----------------------

class ExpenseCreate(BaseSchema):
    date: Optional[datetime] = Field(
        default=None,
        description="Date on which the transaction occurred"
    )
    expense_type: ExpenseType
    description: str = Field(..., max_length=500)
    amount: Decimal = Field(..., gt=0, description="Transaction amount")
    transaction_type: TransactionType
    transaction_mode: TransactionMode
    category: Optional[str] = Field(default=None, max_length=100)
    subcategory: Optional[str] = Field(default=None, max_length=100)
    account: str = Field(..., max_length=255)
    tags: Optional[List[str]] = None
    comments: Optional[str] = Field(default=None, max_length=500)


class ExpenseUpdate(BaseSchema):
    date: Optional[datetime] = None
    expense_type: Optional[ExpenseType] = None
    description: Optional[str] = Field(default=None, max_length=500)
    amount: Optional[Decimal] = Field(None, gt=0)
    transaction_type: Optional[TransactionType] = None
    transaction_mode: Optional[TransactionMode] = None
    category: Optional[str] = Field(default=None, max_length=100)
    subcategory: Optional[str] = Field(default=None, max_length=100)
    account: Optional[str] = Field(default=None, max_length=255)
    tags: Optional[List[str]] = None
    comments: Optional[str] = Field(default=None, max_length=500)


# -----------------------
# RESPONSE SCHEMAS
# -----------------------

class ExpenseResponse(BaseSchema):
    id: UUID
    date: Optional[datetime]
    expense_type: ExpenseType
    description: str
    amount: Decimal
    transaction_type: TransactionType
    transaction_mode: TransactionMode
    category: Optional[str]
    subcategory: Optional[str]
    account: str
    tags: Optional[List[str]]
    comments: Optional[str]
    created_at: datetime
    updated_at: datetime


class ExpenseCreateResponse(BaseSchema):
    id: UUID
    message: str = "Transaction created successfully"


class ExpenseListResponse(BaseSchema):
    count: int
    data: List[ExpenseResponse]


# -----------------------
# SUMMARY / REPORT SCHEMA
# -----------------------

class ExpenseSummaryResponse(BaseSchema):
    total_income: float
    total_expense: float
    net_balance: float
    by_category: dict[str, float]
    by_transaction_mode: dict[str, float]
