



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_v1steam_filedetails_response import GetV1SteamFiledetailsResponse
    from .get_v1steam_login_request_openid_mode import GetV1SteamLoginRequestOpenidMode
    from .open_id_body_mode import OpenIdBodyMode
    from .post_v1steam_login_request_openid_mode import PostV1SteamLoginRequestOpenidMode
_dynamic_imports: typing.Dict[str, str] = {
    "GetV1SteamFiledetailsResponse": ".get_v1steam_filedetails_response",
    "GetV1SteamLoginRequestOpenidMode": ".get_v1steam_login_request_openid_mode",
    "OpenIdBodyMode": ".open_id_body_mode",
    "PostV1SteamLoginRequestOpenidMode": ".post_v1steam_login_request_openid_mode",
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
    "GetV1SteamFiledetailsResponse",
    "GetV1SteamLoginRequestOpenidMode",
    "OpenIdBodyMode",
    "PostV1SteamLoginRequestOpenidMode",
]
