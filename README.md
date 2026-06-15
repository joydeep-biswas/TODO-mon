# TODO-mon

TODO-mon is a **FastAPI** and **Streamlit** based web application.  

The **FastAPI** backend handles API requests, and SQLite database operations, while the **Streamlit** frontend provides an interactive UI.

---

## Tech Stack

- Backend: FastAPI
- Frontend: Streamlit
- Database: SQLite
- ORM: SQLAlchemy

---

## Project Structure
```text
TODO-mon/
├── backend/
│ ├── scripts/
│ │   └── init_db.py
│ ├── main.py
│ ├── database.py
│ ├── model.py
│ └── routes.py 
│
├── frontend/
│ ├── app.py
│ └── api.py
│
├── data/
│
├── requirements.txt
└── README.md
```

---

## Getting Started (Local Setup)

### 1. Create Virtual Environment (Optional)

```bash
python -m venv .venv

# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Initialize Database

```bash
cd backend
python -m scripts.init_db
```

---

### 4. Run the Application

Start FastAPI backend:

```bash
cd backend
fastapi dev main.py
```

Start Streamlit frontend (new terminal):

```bash
cd frontend
streamlit run app.py
```