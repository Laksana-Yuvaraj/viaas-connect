from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.base import Base


class WeeklyTimetable(Base):
    __tablename__ = "weekly_timetables"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    day_order = Column(Integer)  # 1-6
    hour = Column(Integer)  # 1-6
    subject = Column(String)
    staff_id = Column(Integer, ForeignKey("staff.id"))
    substitution_staff_id = Column(Integer, ForeignKey("staff.id"), nullable=True)
    session_type = Column(String)  # Theory/Practical


class SemesterTimetable(Base):
    __tablename__ = "semester_timetables"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    semester = Column(String)  # "Sem 3"
    exam_date = Column(Date)
    subject = Column(String)
    session = Column(String)  # Morning/Afternoon
