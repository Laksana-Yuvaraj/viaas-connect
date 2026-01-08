from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    register_number = Column(String, unique=True)
    bus_number = Column(String)

    user = relationship("User", back_populates="student")
    class_ = relationship("Class", back_populates="students")
