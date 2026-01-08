from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    staff_code = Column(String, unique=True)
    cl_taken = Column(Integer, default=0)  # Casual leaves used (max 12)

    user = relationship("User", back_populates="staff")
