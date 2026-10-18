



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_gateway_error_body import BadGatewayErrorBody
    from .conflict_error_body import ConflictErrorBody
    from .internal_server_error_body import InternalServerErrorBody
    from .list_experiments_request_started_after import ListExperimentsRequestStartedAfter
    from .list_experiments_request_started_before import ListExperimentsRequestStartedBefore
    from .not_found_error_body import NotFoundErrorBody
    from .unprocessable_entity_error_body import UnprocessableEntityErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "BadGatewayErrorBody": ".bad_gateway_error_body",
    "ConflictErrorBody": ".conflict_error_body",
    "InternalServerErrorBody": ".internal_server_error_body",
    "ListExperimentsRequestStartedAfter": ".list_experiments_request_started_after",
    "ListExperimentsRequestStartedBefore": ".list_experiments_request_started_before",
    "NotFoundErrorBody": ".not_found_error_body",
    "UnprocessableEntityErrorBody": ".unprocessable_entity_error_body",
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
    "ConflictErrorBody",
    "InternalServerErrorBody",
    "ListExperimentsRequestStartedAfter",
    "ListExperimentsRequestStartedBefore",
    "NotFoundErrorBody",
    "UnprocessableEntityErrorBody",
]
