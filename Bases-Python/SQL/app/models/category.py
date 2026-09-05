from sqlalchemy import String
from sqlalchemy.orm import Mapped , mapped_column , relationship

from app.database import Base


class Category(Base):
    
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    
    plats: Mapped[list["Plat"]] = relationship(back_populates="categorie")
    
    