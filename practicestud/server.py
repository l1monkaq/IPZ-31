from fastapi import FastAPI

app = FastAPI()
db = [{"id": 1, "name": "Олексій"}]

@app.get("/users")
def get_users():
    return {"status": "success", "data": db, "message": "List loaded"}

@app.post("/users")
def add_user(id: int, name: str):
    new_user = {"id": id, "name": name}
    db.append(new_user)
    return {"status": "success", "data": new_user, "message": "Created"}

@app.get("/users/{uid}")
def get_user(uid: int):
    for u in db:
        if u["id"] == uid:
            return {"status": "success", "data": u, "message": "Found"}
    return {"status": "error", "data": None, "message": "Not found"}

@app.put("/users/{uid}")
def update_user(uid: int, name: str):
    for u in db:
        if u["id"] == uid:
            u["name"] = name
            return {"status": "success", "data": u, "message": "Updated"}
    return {"status": "error", "data": None, "message": "Not found"}

@app.delete("/users/{uid}")
def delete_user(uid: int):
    for i, u in enumerate(db):
        if u["id"] == uid:
            db.pop(i)
            return {"status": "success", "data": None, "message": "Deleted"}
    return {"status": "error", "data": None, "message": "Not found"}