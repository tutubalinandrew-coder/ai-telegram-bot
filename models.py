from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey, Integer, String


class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    role: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
    user: Mapped["User"] = relationship(back_populates="messages")

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column (primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column (BigInteger)
    messages: Mapped[list["Message"]] = relationship(back_populates="user")
