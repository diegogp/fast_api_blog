from jose import JWTError, jwt
from datetime import datetime, timedelta

#SECRET_KEY - Random long hex 32
#Algorithm
#Expiration time

SECRET_KEY = "9532a2e4c01474cddc2ec650b4ca71681060c7dc2b3b6587cacbba910f12a703" #openssl rand -hex 32
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30

def create_acess_token(data: dict):
    to_encode = data.copy()
    expire = (datetime.now() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)).isoformat()
    to_encode.update({"expiration_time": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt