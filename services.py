import sqlalchemy.orm as _orm

import database as _database, models as _models, schemas as _schemas

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(db: _orm.Session, id_user: int):
    return db.query(_models.User).filter(_models.User.id_user == id_user).first()

def get_user_by_email(db: _orm.Session, email: str):
    return db.query(_models.User).filter(_models.User.email == email).first()

def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.User).offset(skip).limit(limit).all()

def create_user(db: _orm.Session, user: _schemas.UserCreate):
    fake_hashed_password = user.password + "thisisnotsecure"
    db_user = _models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_paket(db: _orm.Session, paket: _schemas.PaketCreate):
    db_paket = _models.Paket(jumlah_CV = paket.jumlah_CV, durasi = paket.durasi, harga = paket.harga)
    db.add(db_paket)
    db.commit()
    db.refresh(db_paket)
    return db_paket

def get_pakets(db: _orm.Session, skip: int = 0, limit: int = 9):
    return db.query(_models.Paket).offset(skip).limit(limit).all()

def get_paket(db: _orm.Session, id_paket: int):
    return db.query(_models.Paket).filter(_models.Paket.id_paket == id_paket).first()

def delete_paket(db: _orm.Session, id_paket: int):
    db.query(_models.Paket).filter(_models.Paket.id_paket == id_paket).delete()
    db.commit()

def update_paket(db: _orm.Session, id_paket: int, paket: _schemas.PaketCreate):
    db_paket = get_paket(db=db, id_paket=id_paket)
    db_paket.jumlah_CV = paket.jumlah_CV
    db_paket.durasi = paket.durasi
    db_paket.harga = paket.harga
    db.commit()
    db.refresh(db_paket)
    return db_paket