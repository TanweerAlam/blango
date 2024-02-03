from django.core.management.base import BaseCommand

from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from blango_auth.models import User

class Clean_Inactive_User(BaseCommand):
  help = "Use the command to delete inactive users after activation period"

  def handle(self, *args, **options):
    User.objects.filter(
      is_active=False, 
      date_joined__lt=timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
    ).delete()