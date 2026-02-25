## Local Setup Instructions

### 1. Clone repo
git clone https://github.com/ibrahim-sma/fmtc-temp.git
cd fastapi-project

### 2. Create virtual env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Setup PostgreSQL
- Create database: fastapi_db
- Restore DB:
Using Method1 - If (.dump file is exported)
pg_restore -U postgres -d fmtc_db fastapi_db.dump

Using Method2 - If (.sql file is exported)
psql -U postgres -d fastapi_db -f db/fastapi_db.sql 
(Modify db/fastapi_db.dump or fastapi_db.sql to API working directory folder path)

Note: Also, pg_dump/pg_restore by default may throw error and the same can be found
in C:/Program Files/PostgreSQL/18/bin folder. Execute commands from there. 

### 5. Setup env
cp .env.example .env
Note: this is a linux command and use git-bash to execute this.

Windows comands if reqd:
- copy .env.example .env
- Copy-Item .env.example .env (PowerShell)
- OPTION 3: Manual (Fallback)
Right-click .env.example -> Copy → Paste -> Rename to .env

### 6. Modify Database Info & creds in files if environmental variables are not used.
make sure to change the following files:
    - .env.example, .env
    - alembic.ini (sqlalchemy.url = postgresql://postgres:postgres123@localhost:5432/fmtc_db)
    - app/db/engine.py (DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/fmtc_db")
    (or)
    - app/database.py (DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/fmtc_db") 

### 7. Run API
uvicorn app.main:app --reload
