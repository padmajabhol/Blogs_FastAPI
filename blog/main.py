# libraries
from fastapi import FastAPI
import uvicorn
# files
from . import models
from .database import engine
from .routers import blog, user, authentication

# instance of the fastAPI
app = FastAPI()

# create all the models to the database
models.Base.metadata.create_all(engine)

# include routers
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
