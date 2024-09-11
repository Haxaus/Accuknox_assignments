import time
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class Model1(models.Model):
    name = models.CharField(max_length=50)

# Signal 
@receiver(post_save, sender=Model1)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received!")
    ct=timezone.now()
    print(f"start at: {ct}")
    time.sleep(5)  # 5 seconds delay
    print("Signal handler finished processing")
    mt=timezone.now()
    print(f"end at: {mt}")
    
