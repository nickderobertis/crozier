



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .context_create_new_context_request_owner import ContextCreateNewContextRequestOwner
    from .context_create_new_context_request_owner_id import ContextCreateNewContextRequestOwnerId
    from .context_create_new_context_request_owner_id_type import ContextCreateNewContextRequestOwnerIdType
    from .context_create_new_context_request_owner_slug import ContextCreateNewContextRequestOwnerSlug
    from .context_create_new_context_request_owner_slug_type import ContextCreateNewContextRequestOwnerSlugType
    from .context_list_owner_contexts_request_owner_type import ContextListOwnerContextsRequestOwnerType
_dynamic_imports: typing.Dict[str, str] = {
    "ContextCreateNewContextRequestOwner": ".context_create_new_context_request_owner",
    "ContextCreateNewContextRequestOwnerId": ".context_create_new_context_request_owner_id",
    "ContextCreateNewContextRequestOwnerIdType": ".context_create_new_context_request_owner_id_type",
    "ContextCreateNewContextRequestOwnerSlug": ".context_create_new_context_request_owner_slug",
    "ContextCreateNewContextRequestOwnerSlugType": ".context_create_new_context_request_owner_slug_type",
    "ContextListOwnerContextsRequestOwnerType": ".context_list_owner_contexts_request_owner_type",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "ContextCreateNewContextRequestOwner",
    "ContextCreateNewContextRequestOwnerId",
    "ContextCreateNewContextRequestOwnerIdType",
    "ContextCreateNewContextRequestOwnerSlug",
    "ContextCreateNewContextRequestOwnerSlugType",
    "ContextListOwnerContextsRequestOwnerType",
]
