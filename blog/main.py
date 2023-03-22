from fastapi import FastAPI
from . import models
from .database import engine
import uvicorn
from .routers import blog, user, authentication

app = FastAPI()

# create all the models to the database
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
