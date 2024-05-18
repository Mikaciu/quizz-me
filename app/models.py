import datetime
from app import db

from typing_extensions import Annotated

from sqlalchemy import String, ForeignKey, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import mapped_column, Mapped

intpk = Annotated[int, mapped_column(primary_key=True)]

class Quizz(db.Model):
    __tablename__ = "quizz"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(255), index=True)
    date: Mapped[DateTime] = mapped_column(DateTime, default=datetime.datetime.now(datetime.UTC))

class QuizzItem(db.Model):
    __tablename__ = "item"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(255), index=True)
    answer: Mapped[str] = mapped_column(Text)
    source_id = mapped_column("source_id", Integer, ForeignKey("source.id"))
    source_range: Mapped[str] = mapped_column(String(64))

class QuizzAnswerSource(db.Model):
    __tablename__ = "source"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String)

class JspLevel(db.Model):
    __tablename__ = "level"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String)

class Jsp(db.Model):
    __tablename__ = "jsp"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    level_id: Mapped[intpk] = mapped_column("level_id", Integer, ForeignKey("level.id"))
