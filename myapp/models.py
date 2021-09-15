from django.db import models

# Create your models here.


from django.db.models.signals import pre_save
from django.dispatch import receiver

class Contact(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField(default='abc@gmail.com')
    phone=models.IntegerField() 
    image=models.ImageField(default='download.png')

    def __str__(self) -> str:
        return self.name

@receiver(pre_save,sender=Contact)
def task_handler(sender,instance,**kwargs):
    print("you call me 2nd way!!")
    print(instance)

'''
1st method of signals
def task_handler(sender,instance,**kwargs):
    print("you call me")
    print(instance.name)
    print(instance.email)

pre_save.connect(task_handler,sender=Contact)
'''