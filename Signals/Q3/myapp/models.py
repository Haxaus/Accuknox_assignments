from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Model3(models.Model):
    name = models.CharField(max_length=100)

# Signal

@receiver(post_save, sender=Model3)
def my_signal(sender, instance, **kwargs):
    print("Signal triggered for: ", instance.name)

    #condition for failing transaction
    if instance.name == "fail":
        raise ValidationError("Error in signal!")

# Transaction
def test_the_transaction(Name):
    try:
        with transaction.atomic():
            total_objects = Model3.objects.count()
            print(f"Total objects created yet: {total_objects}") #for counting object created yet in model
            obj = Model3(name=str(Name))
            obj.save()
            print("Model saved ")
        print("Transaction committed")
        total_objects = Model3.objects.count()
        print(f"Total objects created yet: {total_objects}")#see current count of objects if transaction is sucessful
        print("for failing transaction use fail string inside function")
    except Exception as e:
        print("Transaction is failed, rolling back:", str(e))
        total_objects = Model3.objects.count()
        print(f"Total objects created yet: {total_objects}")#see current count of objects if transaction is fail

