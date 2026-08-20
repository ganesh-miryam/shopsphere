from fastapi import FastAPI
from app.routes.products import router as product_router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShopSphere API",
    version="1.0.0"
)

app = FastAPI(
    title="ShopSphere API",
    version="1.0.0"
)
app.include_router(product_router)

@app.get("/")
def root():
    return {
        "application": "ShopSphere",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
