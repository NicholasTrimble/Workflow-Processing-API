from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.models.user import User

def create_user(db: Session, username: str, password: str):
    hashed = bcrypt.hash(password)
    user = User(username=username, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def verify_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not bcrypt.verify(password, user.password):
        return None
    return user
