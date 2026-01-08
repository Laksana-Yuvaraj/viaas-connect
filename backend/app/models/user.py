from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base
from .department import Department


class RoleEnum(str):
    ADMIN = "Admin"
    HOD = "HOD"
    STAFF = "Staff"
    STUDENT = "Student"
    IQAC = "IQAC"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    is_active = Column(String, default="true")

    department = relationship("Department", back_populates="users")
    student = relationship("Student", back_populates="user", uselist=False)
    staff = relationship("Staff", back_populates="user", uselist=False)

    created_at = Column(String, server_default=func.now())
