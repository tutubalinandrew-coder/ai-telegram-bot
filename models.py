from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String


class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    role: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column (primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column (BigInteger)

