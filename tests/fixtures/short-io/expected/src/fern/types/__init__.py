



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .conflict_error_body import ConflictErrorBody
    from .forbidden_error_body import ForbiddenErrorBody
    from .forbidden_error_body_type import ForbiddenErrorBodyType
    from .get_links_tweetbot_request_url_only import GetLinksTweetbotRequestUrlOnly
    from .get_links_tweetbot_request_url_only_one import GetLinksTweetbotRequestUrlOnlyOne
    from .get_links_tweetbot_request_url_only_zero import GetLinksTweetbotRequestUrlOnlyZero
    from .internal_server_error_body import InternalServerErrorBody
    from .not_found_error_body import NotFoundErrorBody
    from .payment_required_error_body import PaymentRequiredErrorBody
    from .unauthorized_error_body import UnauthorizedErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "ConflictErrorBody": ".conflict_error_body",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "ForbiddenErrorBodyType": ".forbidden_error_body_type",
    "GetLinksTweetbotRequestUrlOnly": ".get_links_tweetbot_request_url_only",
    "GetLinksTweetbotRequestUrlOnlyOne": ".get_links_tweetbot_request_url_only_one",
    "GetLinksTweetbotRequestUrlOnlyZero": ".get_links_tweetbot_request_url_only_zero",
    "InternalServerErrorBody": ".internal_server_error_body",
    "NotFoundErrorBody": ".not_found_error_body",
    "PaymentRequiredErrorBody": ".payment_required_error_body",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
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
    "BadRequestErrorBody",
    "ConflictErrorBody",
    "ForbiddenErrorBody",
    "ForbiddenErrorBodyType",
    "GetLinksTweetbotRequestUrlOnly",
    "GetLinksTweetbotRequestUrlOnlyOne",
    "GetLinksTweetbotRequestUrlOnlyZero",
    "InternalServerErrorBody",
    "NotFoundErrorBody",
    "PaymentRequiredErrorBody",
    "UnauthorizedErrorBody",
]
