from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str    #we will need to hash this for storage, passlib automatically identifies the available libraries to use for hashing (bcrypt in my case)

# I have not tested with multiple libs installed as i was developing inside a venv with only bcrypt installed
# you might have to watch out for any conflicts and need some additional config if you run with multiple encryption libraries installed on your system
