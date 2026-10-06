



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import ApiResponse, Category, OauthScope, Order, OrderStatus, Pet, PetStatus, Tag, User
    from .errors import BadRequestError, NotFoundError, UnprocessableEntityError
    from . import pet, store, user
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncPetStoreApi, PetStoreApi
    from .environment import PetStoreApiEnvironment
    from .pet import FindPetsByStatusRequestStatus
_dynamic_imports: typing.Dict[str, str] = {
    "ApiResponse": ".types",
    "AsyncPetStoreApi": ".client",
    "BadRequestError": ".errors",
    "Category": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FindPetsByStatusRequestStatus": ".pet",
    "NotFoundError": ".errors",
    "OauthScope": ".types",
    "Order": ".types",
    "OrderStatus": ".types",
    "Pet": ".types",
    "PetStatus": ".types",
    "PetStoreApi": ".client",
    "PetStoreApiEnvironment": ".environment",
    "Tag": ".types",
    "UnprocessableEntityError": ".errors",
    "User": ".types",
    "pet": ".pet",
    "store": ".store",
    "user": ".user",
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
    "ApiResponse",
    "AsyncPetStoreApi",
    "BadRequestError",
    "Category",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FindPetsByStatusRequestStatus",
    "NotFoundError",
    "OauthScope",
    "Order",
    "OrderStatus",
    "Pet",
    "PetStatus",
    "PetStoreApi",
    "PetStoreApiEnvironment",
    "Tag",
    "UnprocessableEntityError",
    "User",
    "pet",
    "store",
    "user",
]
