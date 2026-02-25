from typing import Optional
from uuid import UUID
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpenseResponse,
    ExpenseCreateResponse,
    ExpenseListResponse,
    ExpenseSummaryResponse
)
from app.crud.expense import (
    create_expense,
    get_expense_by_id,
    list_expenses,
    update_expense,
    delete_expense,
    get_expense_summary
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post(
    "",
    response_model=ExpenseCreateResponse,
    status_code=status.HTTP_201_CREATED
)
def create_expense_api(
    payload: ExpenseCreate,
    db: Session = Depends(get_db)
):
    expense = create_expense(db, payload)
    return {
        "id": expense.id,
        "message": "Transaction created successfully"
    }

@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse
)
def get_expense_api(
    expense_id: UUID,
    db: Session = Depends(get_db)
):
    expense = get_expense_by_id(db, expense_id)
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    return expense


@router.get(
    "",
    response_model=ExpenseListResponse
)
def list_expenses_api(
    expense_type: Optional[str] = None,
    transaction_mode: Optional[str] = None,
    category: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    expenses = list_expenses(
        db=db,
        expense_type=expense_type,
        transaction_mode=transaction_mode,
        category=category,
        from_date=from_date,
        to_date=to_date,
        skip=skip,
        limit=limit
    )

    return {
        "count": len(expenses),
        "data": expenses
    }


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse
)
def update_expense_api(
    expense_id: UUID,
    payload: ExpenseUpdate,
    db: Session = Depends(get_db)
):
    expense = get_expense_by_id(db, expense_id)
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    updated_expense = update_expense(db, expense, payload)
    return updated_expense


@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_200_OK
)
def delete_expense_api(
    expense_id: UUID,
    db: Session = Depends(get_db)
):
    expense = get_expense_by_id(db, expense_id)
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    delete_expense(db, expense)
    return {"message": "Transaction deleted successfully"}
