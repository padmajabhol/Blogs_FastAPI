from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user

router = APIRouter(prefix='/users', tags=['user'])

# routers for user


# create user
@ router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)

# get user by id


@ router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)
