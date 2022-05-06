from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# return the hashed password


def get_password_hash(password: str):
    return pwd_context.hash(password)

#  check the password


def verify_password(hashed_password: str, plain_password: str):
    return pwd_context.verify(plain_password, hashed_password)
