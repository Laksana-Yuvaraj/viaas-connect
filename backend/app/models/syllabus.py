from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class SyllabusUnit(Base):
    __tablename__ = "syllabus_units"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    subject_code = Column(String)
    unit_number = Column(Integer)
    title = Column(String)
    content = Column(Text)
    total_expected = Column(Integer)  # Total hours

    completions = relationship("SyllabusCompletion", back_populates="unit")


class SyllabusCompletion(Base):
    __tablename__ = "syllabus_completions"

    id = Column(Integer, primary_key=True)
    syllabus_unit_id = Column(Integer, ForeignKey("syllabus_units.id"))
    staff_id = Column(Integer, ForeignKey("staff.id"))
    topics_covered = Column(String)
    methodology = Column(String)  # Chalk & Talk, PPT, etc.
    aids_used = Column(String)  # LCD, Model, etc.
    hours_taken = Column(Integer)
    completed_at = Column(String, server_default=func.now())
    unit = relationship("SyllabusUnit", back_populates="completions")
