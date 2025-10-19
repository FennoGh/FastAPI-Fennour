from fastapi import FastAPI

app = FastAPI()

users = ["yousef","juan","adam","martin","paco"]

@app.get("/")
def home():
    return {"message": "Servidor FastAPI funcionant!"}


# Endpoint per crear un nou usuari
@app.post("/api/users/")
def crear_usuari(nom: str):
    users.append(nom)
    return {"message": "Usuari creat correctament."}

# Endpoint per obtenir un usuari per nom
@app.get("/api/users/{id}")
def obtenir_usuari(nom):
    return {"user": nom}

# Endpoint per obtenir la llista d'usuaris
@app.get("/api/users/")
def obtenir_usuaris():
    return {"users": users}

# Endpoint per actualitzar un usuari
@app.put("/api/users/{id}")
def actualitzar_usuari(id, nou_nom):
    contaPosicio = 0
    for user in users:
        if id == user:
            users[contaPosicio] = nou_nom
        contaPosicio += 1
    return {"message": "Usuari actualitzat"}

# Endpoint per eliminar un usuari
@app.delete("/api/users/{id}")
def eliminar_usuari(id):
    contaPosicio = 0
    for user in users:
        if id == user:
            users.pop(contaPosicio)
            return {"message": "Usuari eliminat"}
        contaPosicio += 1
    return {"message": "Usuari no trobat"}

