from fastapi import FastAPI
from .routes.router import router
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get('/', tags=['Home'])
def home():
	return {'msg': 'Pokemon API'}
