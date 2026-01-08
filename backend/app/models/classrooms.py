from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Classroom(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    name = Column(String)  # "III BSc CS - Sem 5"
    created_by = Column(Integer, ForeignKey("users.id"))


class ClassroomPost(Base):
    __tablename__ = "classroom_posts"

    id = Column(Integer, primary_key=True)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))
    posted_by = Column(Integer, ForeignKey("users.id"))
    post_type = Column(String)  # Material, Announcement, Assignment, Link
    title = Column(String)
    content = Column(Text)
    file_url = Column(String, nullable=True)
    youtube_id = Column(String, nullable=True)
    external_link = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))
    posted_by = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(Text)
    due_date = Column(DateTime)
    max_marks = Column(Integer, default=5)
    is_closed = Column(Boolean, default=False)


class AssignmentSubmission(Base):
    __tablename__ = "assignment_submissions"

    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    file_url = Column(String)
    submitted_at = Column(DateTime, server_default=func.now())
    status = Column(String, default="submitted")  # submitted, needs_correction, graded
    marks = Column(Integer, nullable=True)
    feedback = Column(Text, nullable=True)
    version = Column(Integer, default=1)
