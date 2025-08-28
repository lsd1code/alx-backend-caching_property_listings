from .models import (
    Property
)

from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import (
    post_save, post_delete
)


@receiver(post_save, sender=Property, dispatch_uid='save_cache')
def handle_cache_invalidation_creation(sender, instance, created, **kwargs):
    if created:
        print('Created new Property')
        cache.delete('all_properties')


@receiver(post_delete, sender=Property, dispatch_uid='save_cache')
def handle_cache_invalidation_deletion(sender, instance, created, **kwargs):
    print('Clearing cache')
    cache.delete('all_properties')
