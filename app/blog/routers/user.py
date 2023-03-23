from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from blog import schemas, database, models
from ..hashing import Hash
from blog.repository import user

router = APIRouter(prefix='/user', tags=['user'])


@ router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@ router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)
