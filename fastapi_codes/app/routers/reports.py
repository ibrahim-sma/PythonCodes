from fastapi import APIRouter, Depends
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.expense import ExpenseSummaryResponse
from app.crud.expense import get_expense_summary

router = APIRouter(
    prefix="/expenses",
    tags=["Reports"]
)

@router.get(
    "/summary",
    response_model=ExpenseSummaryResponse
)
def expense_summary_api(
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    return get_expense_summary(db, from_date, to_date)
