from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    telephone: Mapped[str] = mapped_column(
        String(30),
        nullable=True
    )

    commandes: Mapped[list["Commande"]] = relationship(
        back_populates="client"
    )

    avis: Mapped[list["Avis"]] = relationship(
        back_populates="client"
    )