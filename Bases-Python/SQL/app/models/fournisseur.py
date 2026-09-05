from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Fournisseur(Base):
    __tablename__ = "fournisseurs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    contact: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    ingredients: Mapped[list["Ingredient"]] = relationship(
        back_populates="fournisseur"
    )