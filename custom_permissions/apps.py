from django.apps import AppConfig
from unittest.mock import patch


def get_permission_codename(action, opts):
    """
    Return the codename of the permission for the specified action.
    """
    return f'{opts.app_label}.{opts.model_name}.{action}'


def get_builtin_permissions(opts):
    """
    Disable default permissions.
    """
    return []


def monkey_patch():
    from django.contrib.auth import management
    # Muda o formato do nome das permissões padrões.
    management.get_permission_codename = get_permission_codename
    
    # Bloqueia a aplicação inicial das permissões padrões.
    management._get_builtin_permissions = get_builtin_permissions       


class CustomPermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_permissions'

    def ready(self):
        monkey_patch()
        