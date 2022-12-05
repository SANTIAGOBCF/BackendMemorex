import datetime

from ninja import Schema


class PayloadPostAddPost(Schema):
    politician_id: str

    date: datetime.date
    image: str
    source: str
    text: str
    title: str
