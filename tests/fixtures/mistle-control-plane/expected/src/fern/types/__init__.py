



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_gateway_error_body import BadGatewayErrorBody
    from .bad_gateway_error_body_code import BadGatewayErrorBodyCode
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_code import BadRequestErrorBodyCode
    from .bad_request_error_body_one import BadRequestErrorBodyOne
    from .bad_request_error_body_one_code import BadRequestErrorBodyOneCode
    from .bad_request_error_body_resource_kind_not_supported import BadRequestErrorBodyResourceKindNotSupported
    from .bad_request_error_body_validation_error import BadRequestErrorBodyValidationError
    from .bad_request_error_body_zero import BadRequestErrorBodyZero
    from .conflict_error_body import ConflictErrorBody
    from .conflict_error_body_code import ConflictErrorBodyCode
    from .internal_dispatch_schedules_response import InternalDispatchSchedulesResponse
    from .internal_dispatch_schedules_response_status import InternalDispatchSchedulesResponseStatus
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_code import NotFoundErrorBodyCode
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unauthorized_error_body_code import UnauthorizedErrorBodyCode
_dynamic_imports: typing.Dict[str, str] = {
    "BadGatewayErrorBody": ".bad_gateway_error_body",
    "BadGatewayErrorBodyCode": ".bad_gateway_error_body_code",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyCode": ".bad_request_error_body_code",
    "BadRequestErrorBodyOne": ".bad_request_error_body_one",
    "BadRequestErrorBodyOneCode": ".bad_request_error_body_one_code",
    "BadRequestErrorBodyResourceKindNotSupported": ".bad_request_error_body_resource_kind_not_supported",
    "BadRequestErrorBodyValidationError": ".bad_request_error_body_validation_error",
    "BadRequestErrorBodyZero": ".bad_request_error_body_zero",
    "ConflictErrorBody": ".conflict_error_body",
    "ConflictErrorBodyCode": ".conflict_error_body_code",
    "InternalDispatchSchedulesResponse": ".internal_dispatch_schedules_response",
    "InternalDispatchSchedulesResponseStatus": ".internal_dispatch_schedules_response_status",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyCode": ".not_found_error_body_code",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnauthorizedErrorBodyCode": ".unauthorized_error_body_code",
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
    "BadGatewayErrorBody",
    "BadGatewayErrorBodyCode",
    "BadRequestErrorBody",
    "BadRequestErrorBodyCode",
    "BadRequestErrorBodyOne",
    "BadRequestErrorBodyOneCode",
    "BadRequestErrorBodyResourceKindNotSupported",
    "BadRequestErrorBodyValidationError",
    "BadRequestErrorBodyZero",
    "ConflictErrorBody",
    "ConflictErrorBodyCode",
    "InternalDispatchSchedulesResponse",
    "InternalDispatchSchedulesResponseStatus",
    "NotFoundErrorBody",
    "NotFoundErrorBodyCode",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyCode",
]
