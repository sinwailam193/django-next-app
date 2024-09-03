from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404

from .models import WaitlistEntry
from .schema import WaitlistEntryDetailSchema

router = Router()


@router.get("", response=List[WaitlistEntryDetailSchema])
def list_waitlist_entries(request):
    return WaitlistEntry.objects.all()


@router.get("/{id}", response=WaitlistEntryDetailSchema)
def waitlist_entry_detail(request, id: int):
    return get_object_or_404(WaitlistEntry, id=id)
