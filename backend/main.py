from fastapi import FastAPI
from database import Base, engine
from routes import router as task_router

app = FastAPI()

# create tables (simple version)
Base.metadata.create_all(bind=engine)

app.include_router(task_router)


@app.get("/")
def root():
    return {"message": "TODO-mon is UP!"}