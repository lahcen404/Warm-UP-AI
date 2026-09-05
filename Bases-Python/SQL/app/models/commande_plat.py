from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class CommandePlat(Base):
    __tablename__ = "commande_plats"

    commande_id: Mapped[int] = mapped_column(
        ForeignKey("commandes.id"),
        primary_key=True
    )

    plat_id: Mapped[int] = mapped_column(
        ForeignKey("plats.id"),
        primary_key=True
    )

    quantite: Mapped[int] = mapped_column(
        nullable=False
    )

    commande: Mapped["Commande"] = relationship(
        back_populates="commande_plats"
    )

    plat: Mapped["Plat"] = relationship(
        back_populates="commande_plats"
    )