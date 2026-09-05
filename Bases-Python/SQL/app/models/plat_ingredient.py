from decimal import Decimal

from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class PlatIngredient(Base):
    __tablename__ = "plat_ingredients"

    plat_id: Mapped[int] = mapped_column(
        ForeignKey("plats.id"),
        primary_key=True
    )

    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id"),
        primary_key=True
    )

    quantite_necessaire: Mapped[Decimal] = mapped_column(
        Numeric(10, 3),
        nullable=False
    )

    plat: Mapped["Plat"] = relationship(
        back_populates="plat_ingredients"
    )

    ingredient: Mapped["Ingredient"] = relationship(
        back_populates="plat_ingredients"
    )