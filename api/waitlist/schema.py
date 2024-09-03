from datetime import datetime
from ninja import Schema
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    email: EmailStr


class WaitlistEntryDetailSchema(Schema):
    id: int
    email: EmailStr
    updated_at: datetime
    created_at: datetime
