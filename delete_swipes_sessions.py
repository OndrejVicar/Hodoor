from django.conf import settings

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ticker.settings")
django.setup()

from attendance.models import Swipe,Session

Swipe.objects.all().delete()
Session.objects.all().delete()

if(not (Swipe.objects.all() and Swipe.objects.all())):
	print("Swipes and Sessions deleted from database.")
print("Was not deleted")