from typing import List, Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import func, and_

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate

def create_expense(db: Session, payload: ExpenseCreate) -> Expense:
    expense = Expense(
        date=payload.date,
        expense_type=payload.expense_type,
        description=payload.description,
        amount=payload.amount,
        transaction_type=payload.transaction_type,
        transaction_mode=payload.transaction_mode,
        category=payload.category,
        subcategory=payload.subcategory,
        account=payload.account,
        tags=payload.tags,
        comments=payload.comments
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_expense_by_id(db: Session, expense_id: UUID) -> Optional[Expense]:
    return (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.is_deleted.is_(False)
        )
        .first()
    )

def list_expenses(
    db: Session,
    expense_type: Optional[str] = None,
    transaction_mode: Optional[str] = None,
    category: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    skip: int = 0,
    limit: int = 50
) -> List[Expense]:

    filters = [Expense.is_deleted.is_(False)]

    if expense_type:
        filters.append(Expense.expense_type == expense_type)

    if transaction_mode:
        filters.append(Expense.transaction_mode == transaction_mode)

    if category:
        filters.append(Expense.category == category)

    if from_date:
        filters.append(Expense.date >= from_date)

    if to_date:
        filters.append(Expense.date <= to_date)

    return (
        db.query(Expense)
        .filter(and_(*filters))
        .order_by(Expense.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_expense(
    db: Session,
    expense: Expense,
    payload: ExpenseUpdate
) -> Expense:

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(expense, field, value)

    db.commit()
    db.refresh(expense)
    return expense

def delete_expense(db: Session, expense: Expense) -> None:
    expense.is_deleted = True
    db.commit()

def get_expense_summary(
    db: Session,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None
) -> dict:

    base_filter = [Expense.is_deleted.is_(False)]

    if from_date:
        base_filter.append(Expense.date >= from_date)

    if to_date:
        base_filter.append(Expense.date <= to_date)

    total_income = (
        db.query(func.coalesce(func.sum(Expense.amount), 0))
        .filter(
            Expense.expense_type == "Income",
            *base_filter
        )
        .scalar()
    )

    total_expense = (
        db.query(func.coalesce(func.sum(Expense.amount), 0))
        .filter(
            Expense.expense_type == "Expense",
            *base_filter
        )
        .scalar()
    )

    by_category = dict(
        db.query(
            Expense.category,
            func.coalesce(func.sum(Expense.amount), 0)
        )
        .filter(*base_filter)
        .group_by(Expense.category)
        .all()
    )

    by_transaction_mode = dict(
        db.query(
            Expense.transaction_mode,
            func.coalesce(func.sum(Expense.amount), 0)
        )
        .filter(*base_filter)
        .group_by(Expense.transaction_mode)
        .all()
    )

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense,
        "by_category": by_category,
        "by_transaction_mode": by_transaction_mode
    }
