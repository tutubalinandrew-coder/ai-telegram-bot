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
    def __repr__(self):
        return (
        f"<Message("
        f"id={self.id}, "
        f"user_id={self.user_id}, "
        f"role='{self.role}', "
        f"message='{self.message[:50] + '...' if len(self.message) > 50 else self.message}', "
        f"created_at={self.created_at}, "
        f"user_id_db={self.user_id_db}"
        f")>"
    )







class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column (primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column (BigInteger, index=True)
    messages: Mapped[list["Message"]] = relationship(back_populates="user")
    def __repr__(self):
        return (
            f"<User("
            f"id={self.id}, "
            f"telegram_id={self.telegram_id})>"
            )

