import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class Model2(models.Model):
    name = models.CharField(max_length=50)

# Signal
@receiver(post_save, sender=Model2)
def my_signal_handler(sender, instance, **kwargs):
    
    print("Signal received in thread:", threading.get_ident())
