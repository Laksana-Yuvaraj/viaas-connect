from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.sql import func
from app.db.base import Base


class StaffLogEntry(Base):
    __tablename__ = "staff_log_entries"

    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("staff.id"))
    date = Column(Date)
    hour = Column(Integer)  # 1-6
    class_name = Column(String)
    subject = Column(String)
    work_done = Column(Text)
    hour_type = Column(String)  # Theory/Practical/Substitution
    is_substitution = Column(Boolean, default=False)
    created_at = Column(String, server_default=func.now())


class ClassLogEntry(Base):
    __tablename__ = "class_log_entries"

    id = Column(Integer
