from fastapi import FastAPI
from app.routers import expenses
from app.routers import reports

app = FastAPI(title="ExpenseTracker API")

app.include_router(reports.router)
app.include_router(expenses.router)
