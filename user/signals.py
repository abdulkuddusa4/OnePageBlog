from django.dispatch import receiver
from django.db.models.signals import post_save,post_init
from django.contrib.auth.models import User
from .models import EmailValidator


@receiver(post_save,sender=User)
def email_validator_creator(sender,**kwargs):
    print('signal passed')
    try:
        EmailValidator(user=kwargs['instance']).save() if kwargs['instance'].email else ...
    except:pass
    print('signal passed')
    # try:
    #     EmailValidator(user=kwargs['instance']).save()
    #     pass
    # except Exception as e:
    #     print('lolo failed')
    #     pass
