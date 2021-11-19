# import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from sqlalchemy.sql.schema import Index

import database as _database

class User(_database.Base):
    __tablename__ = "users"
    id_user = _sql.Column(_sql.Integer, primary_key=True, index=True)
    # nama_user = _sql.Column(_sql.String, default="", index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    # no_HP = _sql.Column(_sql.String, default="", index=True)
    # instansi = _sql.Column(_sql.String, default="ITB", index=True)
    # usia = _sql.Column(_sql.Integer, default=20, index=True)
    # jenis_kelamin = _sql.Column(_sql.String, default="Laki-laki", index=True)
    # id_paket = _sql.Column(_sql.Integer, _sql.ForeignKey("pakets.id_paket"), default=0)
    is_active = _sql.Column(_sql.Boolean, default=True)

    # pakets = _orm.relationship("Paket", back_populates="owner")

class Paket(_database.Base):
    __tablename__ = "pakets"
    id_paket = _sql.Column(_sql.Integer, primary_key=True, index=True)
    jumlah_CV = _sql.Column(_sql.Integer, index=True)
    durasi = _sql.Column(_sql.String, index=True)
    harga = _sql.Column(_sql.Integer, index=True)
    # data_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    # data_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    # owner = _orm.relationship("User", back_populates="pakets")