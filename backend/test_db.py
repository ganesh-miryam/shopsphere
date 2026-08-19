from app.database import engine, Base
from app.models import Product

try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
except Exception as e:
    print("Error:")
    print(e)
