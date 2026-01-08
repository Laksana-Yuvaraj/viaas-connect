from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum

from app.db.base import Base


class AttendanceStatus(str, PyEnum):
    PRESENT = "Present"
    ABSENT = "Absent"
    CL = "CL"
    OD = "OD"
    SOD = "SOD"


class StudentAttendance(Base):
    __tablename__ = "student_attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    date = Column(Date)
    status = Column(Enum(AttendanceStatus))
    reason = Column(String)
    leave_form_url = Column(String)
    session = Column(String, default="AM")  # AM/PM
    created_at = Column(String, server_default=func.now())


class StaffAttendance(Base):
    __tablename__ = "staff_attendance"

    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("staff.id"))
    date = Column(Date)
    status = Column(Enum(AttendanceStatus))
    reason = Column(String)
    created_at = Column(String, server_default=func.now())


class HourlyAttendance(Base):
    __tablename__ = "hourly_attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    timetable_entry_id = Column(Integer, ForeignKey("weekly_timetables.id"))
    hour = Column(Integer)  # 1-6
    status = Column(Enum(AttendanceStatus))
    marked_by = Column(Integer, ForeignKey("users.id"))
    marked_at = Column(String, server_default=func.now())
