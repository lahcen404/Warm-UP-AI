from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Avis(Base):
    __tablename__ = "avis"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id"),
        nullable=False
    )

    plat_id: Mapped[int] = mapped_column(
        ForeignKey("plats.id"),
        nullable=False
    )

    note: Mapped[int] = mapped_column(
        nullable=False
    )

    commentaire: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    date_avis: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    client: Mapped["Client"] = relationship(
        back_populates="avis"
    )

    plat: Mapped["Plat"] = relationship(
        back_populates="avis"
    )