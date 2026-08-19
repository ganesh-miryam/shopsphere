from fastapi import FastAPI
from app.routes.products import router as product_router

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
