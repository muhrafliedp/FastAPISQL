from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas

app = _fastapi.FastAPI(title="FastAPI with SQLite - Muhammad Raflie Dwi Putra")

_services.create_database()


@app.post("/users/", response_model=_schemas.User)
def create_user(user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops... this email is in use"
        )
    return _services.create_user(db=db, user=user)

@app.get("/users/", response_model=List[_schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get("/users/{id_user}", response_model=_schemas.User)
def read_user(id_user: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = _services.get_user(db=db, id_user=id_user)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry!!! this user does not exist"
        )
    return db_user

@app.post("/paket/", response_model=_schemas.Paket)
def create_paket(
    paket: _schemas.PaketCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.create_paket(db=db, paket=paket)

@app.get("/paket/", response_model=List[_schemas.Paket])
def read_pakets(skip: int = 0, limit: int = 10, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    pakets = _services.get_pakets(db=db, skip=skip, limit=limit)
    return pakets

@app.delete("/paket/{id_paket}")
def delete_paket(id_paket: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_paket(db=db, id_paket=id_paket)
    return {"message": f"successfully deleted paket with id: {id_paket}"}

@app.put("/paket/{id_paket}", response_model=_schemas.Paket)
def update_paket(id_paket: int, paket: _schemas.PaketCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.update_paket(db=db, paket=paket, id_paket=id_paket)