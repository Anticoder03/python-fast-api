from fastapi import FastAPI
app = FastAPI()
users = []
@app.get("/")
def get_user():
    return {
        "message":"Srever is running",
        "status":"success",
        "users":users
    }
    
@app.post("/create")
def create_user(user: dict):
    users.append(user)
    return {
        "message":"User created",
        "status":"success",
        "users":user
    }
    
@app.delete("/del/{name}")
def del_user(name: str):
    for user in users:
        if user.get("name") == name:
            users.remove(user)
            return {
                "message": "User deleted",
                "status": "success"
            }

    return {
        "message": "User not found",
        "status": "error"
    }

@app.put("/update/{name}")
def update_user(name: str, updated_user: dict):
    for index, user in enumerate(users):
        if user.get("name") == name:
            users[index].update(updated_user)
            return {
                "message": "User updated",
                "status": "success",
                "user": users[index]
            }

    return {
        "message": "User not found",
        "status": "error"
    }
