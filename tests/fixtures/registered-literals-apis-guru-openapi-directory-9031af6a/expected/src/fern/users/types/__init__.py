



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_user_request_identification import DeleteUserRequestIdentification
    from .delete_user_response import DeleteUserResponse
    from .delete_user_response_meta import DeleteUserResponseMeta
    from .link_request_identification import LinkRequestIdentification
    from .link_response import LinkResponse
    from .link_response_meta import LinkResponseMeta
    from .upsert_user_request_identification import UpsertUserRequestIdentification
    from .upsert_user_request_properties_value import UpsertUserRequestPropertiesValue
    from .upsert_user_response import UpsertUserResponse
    from .upsert_user_response_meta import UpsertUserResponseMeta
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteUserRequestIdentification": ".delete_user_request_identification",
    "DeleteUserResponse": ".delete_user_response",
    "DeleteUserResponseMeta": ".delete_user_response_meta",
    "LinkRequestIdentification": ".link_request_identification",
    "LinkResponse": ".link_response",
    "LinkResponseMeta": ".link_response_meta",
    "UpsertUserRequestIdentification": ".upsert_user_request_identification",
    "UpsertUserRequestPropertiesValue": ".upsert_user_request_properties_value",
    "UpsertUserResponse": ".upsert_user_response",
    "UpsertUserResponseMeta": ".upsert_user_response_meta",
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
    "DeleteUserRequestIdentification",
    "DeleteUserResponse",
    "DeleteUserResponseMeta",
    "LinkRequestIdentification",
    "LinkResponse",
    "LinkResponseMeta",
    "UpsertUserRequestIdentification",
    "UpsertUserRequestPropertiesValue",
    "UpsertUserResponse",
    "UpsertUserResponseMeta",
]
