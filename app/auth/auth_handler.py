from datetime import datetime, timedelta
from jose import jwt


SECRET_KEY = "supersecret"
ALGORITHM = "HS256"


def create_token(username: str):
    
    expire_time = datetime.utcnow() + timedelta(hours=1)

    
    payload = {
        "sub": username,
        "exp": expire_time
    }

    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  
    except Exception:
        return None