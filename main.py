from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Post
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PostResponse(BaseModel):
    response_data: List[dict]
    response_message: str
    response_code: int

class PostCreate(BaseModel):
    title: str
    body: str

# POST /posts
@app.post("/posts",response_model=PostResponse)
def create_post(post_data: PostCreate, db: Session = Depends(get_db)):
    try:
        post = Post(**post_data.dict(by_alias=True))
        db.add(post)
        db.commit()
        db.refresh(post)

        response_data = PostResponse(
            response_data=[],
            response_message='Blog Posted Successfully',
            response_code=200
        )
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET /posts
@app.get("/posts", response_model=PostResponse)
def get_posts(db: Session = Depends(get_db)):
    try:
        posts = db.query(Post).all()

        # Transform posts to a list of dictionaries
        post_list = [{"title": post.title, "body": post.body, "id": post.id} for post in posts]

        response_data = PostResponse(
            response_data=post_list,
            response_message='Data Fetched Successfully',
            response_code=200
        )

        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET /posts/{id}
@app.get("/posts/{id}", response_model=PostResponse)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    try:
        post = db.query(Post).filter(Post.id == id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        
        # Transform posts to a list of dictionaries
        post_list = [{"title": post.title, "body": post.body, "id": post.id}]

        response_data = PostResponse(
            response_data=post_list,
            response_message='Data Fetched Successfully',
            response_code=200
        )
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PUT /posts/{id}
@app.put("/posts/{id}", response_model=PostResponse)
def update_post(id: int, title: str = None, body: str = None, db: Session = Depends(get_db)):
    try:
        post = db.query(Post).filter(Post.id == id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")

        if title is not None:
            post.title = title
        if body is not None:
            post.body = body

        db.commit()
        db.refresh(post)
        response_data = PostResponse(
            response_data=[],
            response_message='Post Updated Successfully',
            response_code=200
        )
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# DELETE /posts/{id}
@app.delete("/posts/{id}",response_model=PostResponse)
def delete_post(id: int, db: Session = Depends(get_db)):
    try:
        post = db.query(Post).filter(Post.id == id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")

        db.delete(post)
        db.commit()
        response_data = PostResponse(
            response_data=[],
            response_message="Post deleted successfully",
            response_code=200
        )
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

