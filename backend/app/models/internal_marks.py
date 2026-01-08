from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.base import Base


class InternalMarks(Base):
    __tablename__ = "internal_marks"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    subject_code = Column(String)
    semester = Column(String)
    assessment1 = Column(Float, default=0)
    assessment2 = Column(Float, default=0)
    assessment3 = Column(Float, default=0)
    assessment4 = Column(Float, default=0)
    attendance = Column(Float, default=0)
    assignment_avg = Column(Float, default=0)
    internal_total = Column(Float, default=0)  # Out of 25
    entered_by = Column(Integer, ForeignKey("users.id"))
