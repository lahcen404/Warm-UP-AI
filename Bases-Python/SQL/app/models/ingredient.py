from decimal import Decimal

from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    cout_unitaire: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    stock: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    fournisseur_id: Mapped[int] = mapped_column(
        ForeignKey("fournisseurs.id"),
        nullable=False
    )

    fournisseur: Mapped["Fournisseur"] = relationship(
        back_populates="ingredients"
    )

    plat_ingredients: Mapped[list["PlatIngredient"]] = relationship(
        back_populates="ingredient"
    )