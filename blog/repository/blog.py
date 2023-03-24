# library
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
# files
from .. import models, schemas

# Blogs


# Get all blogs

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

# Function to get a blog with a particular id


def show(id: int, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available")

    return blog

# Create function


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,
                           body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete function


def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==
                                        id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


# Update function


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==
                                        id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.update(request)
    db.commit()
    return "updated"

# query.update is a bulk method so it updates both at the same time if both have the same value(ie id)
