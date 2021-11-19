from typing import List
import datetime as _dt
import pydantic as _pydantic

from sqlalchemy.sql.sqltypes import String
from sqlalchemy.sql.expression import true


class _PaketBase(_pydantic.BaseModel):
    jumlah_CV: int
    durasi: str
    harga: int

class PaketCreate(_PaketBase):
    pass

# {
#     "id": 1,
#     "owner_id": 23,
#     "title": "this is a title",
#     "content": "some content for the post",
#     "data_created": "12-12-12",
#     "data_last_updated": "12-12-12"
# }

class Paket(_PaketBase):
    id_paket: int
    # data_created: _dt.datetime
    # data_last_updated: _dt.datetime

    class Config:
        orm_mode = True

class _UserBase(_pydantic.BaseModel):
    email: str

class UserCreate(_UserBase):
    password: str

class User(_UserBase):
    id_user: int
    # id_paket: int
    # nama_user: str
    # no_HP: str
    # instansi: str
    # usia: int
    # jenis_kelamin: str
    # pakets: List[Paket] = []
    is_active: bool

    class Config:
        orm_mode = True