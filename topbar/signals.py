from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import TopBar


@receiver(post_save, sender=TopBar)
def single_published_topbar(sender, instance, **kwargs):
    if instance.is_active:
        TopBar.objects.filter(is_active=True).exclude(pk=instance.pk).update(is_active=False)   
    else:
        TopBar.objects.filter(is_active=False).exclude(pk=instance.pk).update(is_active=True)   
    
    publishes = TopBar.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_active)
    
    if all(not item for item in is_publishes):
        obj = TopBar.objects.get(pk=instance.pk)
        obj.is_active=True
        obj.save()
    
@receiver(post_delete,sender=TopBar)
def deleted_published_topbar(sender,instance,*args, **kwargs):
    if instance.is_active:
        obj = TopBar.objects.all().exclude(pk=instance.pk).first()
        obj.is_active=True
        obj.save()