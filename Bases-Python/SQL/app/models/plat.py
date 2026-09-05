from decimal import Decimal

from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Plat(Base):
    __tablename__ = "plats"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    prix: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    categorie_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    categorie: Mapped["Category"] = relationship(
        back_populates="plats"
    )

    commande_plats: Mapped[list["CommandePlat"]] = relationship(
        back_populates="plat"
    )

    plat_ingredients: Mapped[list["PlatIngredient"]] = relationship(
        back_populates="plat"
    )

    avis: Mapped[list["Avis"]] = relationship(
        back_populates="plat"
    )