from wsgiref import headers
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')
#SECRET_KEY - Random long hex 32
#Algorithm
#Expiration time

SECRET_KEY = "9532a2e4c01474cddc2ec650b4ca71681060c7dc2b3b6587cacbba910f12a703" #openssl rand -hex 32
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 1

def create_acess_token(data: dict):
    to_encode = data.copy()
    expire = (datetime.now() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)).isoformat()
    to_encode.update({"expiration_time": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_acess_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could'nt validate credentials.",
        headers={"WWW-Authenticate": "Bearer"})
    return verify_acess_token(token, credentials_exception)