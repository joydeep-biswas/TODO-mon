from database import engine, Base
from model import Task

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database Tables Created!")

if __name__ == "__main__":
    init_db()