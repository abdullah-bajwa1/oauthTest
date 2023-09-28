from fastapi import FastAPI, HTTPException, Depends
from model import User
from sec import hash_password,pwd_context

app = FastAPI()

# This is a simplified in-memory user database; replace with a real database
users_db = []

currentUser = ""

def is_authenticated():
    if currentUser != "":
        return True
    return False


@app.post("/register/")
def register(username: str, password: str):
    hashed_password = hash_password(password)
    user = User(username=username, password=hashed_password)
    users_db.append(user)
    currentUser = username
    return {"message": "User registered successfully"}

@app.post("/login/")
def login(username: str, password: str):
    user = next((u for u in users_db if u.username == username), None)
    if user and pwd_context.verify(password, user.password):
        currentUser = username
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
@app.get("/protected/")
def protected_route(authenticated: bool = is_authenticated):
    if authenticated:
        return {"message": "You have access to this protected route"}
    else:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
@app.post("/logout/")
def logout():
    currentUser = ""
    return {"current": currentUser}


