import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    ### 없어도 잘 실행 되는듯? 최신버전 ###
    # class Config:
    #     orm_mode = True