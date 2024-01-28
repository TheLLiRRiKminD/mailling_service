from django.core.cache import cache

from mailing.models.client import Client


def get_cached_clients(user):
    key = 'clients_list'
    clients_list = cache.get(key)

    if clients_list is None:
        clients_list = Client.objects.filter(user=user)
        cache.set(key, clients_list, 60 * 15)
    return clients_list
