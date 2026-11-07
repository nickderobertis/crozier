



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_rest_api_token_response import CreateRestApiTokenResponse
    from .create_user_request_default_visibility import CreateUserRequestDefaultVisibility
    from .get_self_response import GetSelfResponse
    from .get_tokens_by_type_request_type import GetTokensByTypeRequestType
    from .get_tokens_by_type_response import GetTokensByTypeResponse
    from .modify_user_by_id_request_default_visibility import ModifyUserByIdRequestDefaultVisibility
_dynamic_imports: typing.Dict[str, str] = {
    "CreateRestApiTokenResponse": ".create_rest_api_token_response",
    "CreateUserRequestDefaultVisibility": ".create_user_request_default_visibility",
    "GetSelfResponse": ".get_self_response",
    "GetTokensByTypeRequestType": ".get_tokens_by_type_request_type",
    "GetTokensByTypeResponse": ".get_tokens_by_type_response",
    "ModifyUserByIdRequestDefaultVisibility": ".modify_user_by_id_request_default_visibility",
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
    "CreateRestApiTokenResponse",
    "CreateUserRequestDefaultVisibility",
    "GetSelfResponse",
    "GetTokensByTypeRequestType",
    "GetTokensByTypeResponse",
    "ModifyUserByIdRequestDefaultVisibility",
]
