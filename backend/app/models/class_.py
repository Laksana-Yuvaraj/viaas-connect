from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # "III BSc CS"
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    mentor_id = Column(Integer, ForeignKey("users.id"))  # Class mentor (staff)

    department = relationship("Department", back_populates="classes")
    mentor = relationship("User", foreign_keys=[mentor_id])
    students = relationship("Student", back_populates="class_")
