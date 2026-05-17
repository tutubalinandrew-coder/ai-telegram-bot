from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String, Integer, ForeignKey
from sqlalchemy import DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    role: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
    created_at = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    user_id_db: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )
    user: Mapped["User"] = relationship(back_populates="messages")

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column (primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column (BigInteger)
    messages: Mapped[list["Message"]] = relationship(back_populates="user")

