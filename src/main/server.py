from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.main.estoque.estoque_routes import router as estoque_route

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {'message': 'Hello :)'}

app.include_router(estoque_route)
