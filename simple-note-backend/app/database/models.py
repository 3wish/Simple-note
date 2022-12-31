from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy import func

from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    nick_name: Mapped[str | None] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(120))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    notes: Mapped[list['Note']] = relationship(back_populates='author')

    def __repr__(self):
        return f"User(username={self.username!r}, note_list={self.notes!r}, created_at={self.created_at!r})"


class Note(Base):
    __tablename__ = 'note'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    author: Mapped[User] = relationship(back_populates='notes')

    def __repr__(self):
        return f"Note(title={self.title!r}, author={self.author.username!r}, created_at={self.created_at!r})"
