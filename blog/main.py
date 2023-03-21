from fastapi import FastAPI
from . import models
from .database import engine
import uvicorn
from .routers import blog, user

app = FastAPI()

# create all the models to the database
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get('/blog', response_model=List[schemas.ShowBlog, ], tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
