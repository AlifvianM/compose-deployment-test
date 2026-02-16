from fastapi import FastAPI

from app.order.views import order_router

app = FastAPI()
app.include_router(order_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}