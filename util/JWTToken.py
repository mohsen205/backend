from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from schemas import TokenData, TokenReset


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 43800

# create access token


def create_access_token(data: dict, expires: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires:
        expire = datetime.utcnow() + expires
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#  verfiy token


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("id")
        name: str = payload.get("name")
        email: str = payload.get("email")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id, name=name, email=email)
    except JWTError:
        raise credentials_exception
    return token_data

# verify token password


def verify_token_reset(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        hash: str = payload.get("hash")
        if hash is None:
            raise credentials_exception

        token_data = TokenReset(hash=hash)

    except JWTError:
        raise credentials_exception
    return token_data
