


from fastapi import FastAPI
from db.database import engine, Base
from routes.health import router as health_router
app = FastAPI(title="Singleton db connection!")
@app.on_event("startup")
def startup_event():
    with engine.connect() as connection:
        connection.execute("SELECT 1")

    Base.metadata.create_all(engine)

@app.on_event("shutdown")
def shutdown_event():
    engine.dispose()

app.include_router(health_router)