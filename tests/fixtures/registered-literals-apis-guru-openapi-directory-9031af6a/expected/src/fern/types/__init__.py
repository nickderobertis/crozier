



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_errors import BadRequestErrorBodyErrors
    from .bad_request_error_body_errors_parameters import BadRequestErrorBodyErrorsParameters
    from .bad_request_error_body_meta import BadRequestErrorBodyMeta
    from .forbidden_error_body import ForbiddenErrorBody
    from .forbidden_error_body_meta import ForbiddenErrorBodyMeta
    from .internal_server_error_body import InternalServerErrorBody
    from .internal_server_error_body_meta import InternalServerErrorBodyMeta
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_meta import NotFoundErrorBodyMeta
    from .too_many_requests_error_body import TooManyRequestsErrorBody
    from .too_many_requests_error_body_meta import TooManyRequestsErrorBodyMeta
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unauthorized_error_body_meta import UnauthorizedErrorBodyMeta
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyErrors": ".bad_request_error_body_errors",
    "BadRequestErrorBodyErrorsParameters": ".bad_request_error_body_errors_parameters",
    "BadRequestErrorBodyMeta": ".bad_request_error_body_meta",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "ForbiddenErrorBodyMeta": ".forbidden_error_body_meta",
    "InternalServerErrorBody": ".internal_server_error_body",
    "InternalServerErrorBodyMeta": ".internal_server_error_body_meta",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyMeta": ".not_found_error_body_meta",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
    "TooManyRequestsErrorBodyMeta": ".too_many_requests_error_body_meta",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnauthorizedErrorBodyMeta": ".unauthorized_error_body_meta",
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
    "BadRequestErrorBodyErrors",
    "BadRequestErrorBodyErrorsParameters",
    "BadRequestErrorBodyMeta",
    "ForbiddenErrorBody",
    "ForbiddenErrorBodyMeta",
    "InternalServerErrorBody",
    "InternalServerErrorBodyMeta",
    "NotFoundErrorBody",
    "NotFoundErrorBodyMeta",
    "TooManyRequestsErrorBody",
    "TooManyRequestsErrorBodyMeta",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyMeta",
]
