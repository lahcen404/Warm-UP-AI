from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Commande(Base):
    __tablename__ = "commandes"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id"),
        nullable=False
    )

    date_commande: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    client: Mapped["Client"] = relationship(
        back_populates="commandes"
    )

    commande_plats: Mapped[list["CommandePlat"]] = relationship(
        back_populates="commande"
    )