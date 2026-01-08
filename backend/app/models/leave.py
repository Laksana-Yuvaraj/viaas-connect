from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.base import Base


class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("staff.id"))
    date = Column(Date)
    type = Column(String)  # CL, OD, SOD
    reason = Column(String)
    approved_by = Column(Integer, ForeignKey("users.id"))


class Substitution(Base):
    __tablename__ = "substitutions"

    id = Column(Integer, primary_key=True)
    original_staff_id = Column(Integer, ForeignKey("staff.id"))
    substitution_staff_id = Column(Integer, ForeignKey("staff.id"))
    timetable_entry_id = Column(Integer, ForeignKey("weekly_timetables.id"))
    date = Column(Date)
    hour = Column(Integer)
    notified = Column(String, default="false")
