from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    message = Column(Text)
    type = Column(String)  # SMS, Email, InApp
    channel = Column(String)  # Substitution, AssignmentReminder, Report
    priority = Column(String, default="normal")  # high, normal, low
    sent = Column(Boolean, default=False)
    sent_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User")


class NotificationQueue(Base):
    __tablename__ = "notification_queue"

    id = Column(Integer, primary_key=True)
    notification_id = Column(Integer, ForeignKey("notifications.id"))
    recipient_email = Column(String)
    recipient_phone = Column(String)
    sms_message = Column(Text)
    email_subject = Column(String)
    email_body = Column(Text)
    retries = Column(Integer, default=0)
    status = Column(String, default="pending")  # pending, sent, failed
    queued_at = Column(DateTime, server_default=func.now())
