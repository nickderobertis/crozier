



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .error_bad_request import ErrorBadRequest
    from .error_bad_request_issues_item import ErrorBadRequestIssuesItem
    from .error_forbidden import ErrorForbidden
    from .error_forbidden_issues_item import ErrorForbiddenIssuesItem
    from .error_internal_server_error import ErrorInternalServerError
    from .error_internal_server_error_issues_item import ErrorInternalServerErrorIssuesItem
    from .error_not_found import ErrorNotFound
    from .error_not_found_issues_item import ErrorNotFoundIssuesItem
    from .error_unauthorized import ErrorUnauthorized
    from .error_unauthorized_issues_item import ErrorUnauthorizedIssuesItem
_dynamic_imports: typing.Dict[str, str] = {
    "ErrorBadRequest": ".error_bad_request",
    "ErrorBadRequestIssuesItem": ".error_bad_request_issues_item",
    "ErrorForbidden": ".error_forbidden",
    "ErrorForbiddenIssuesItem": ".error_forbidden_issues_item",
    "ErrorInternalServerError": ".error_internal_server_error",
    "ErrorInternalServerErrorIssuesItem": ".error_internal_server_error_issues_item",
    "ErrorNotFound": ".error_not_found",
    "ErrorNotFoundIssuesItem": ".error_not_found_issues_item",
    "ErrorUnauthorized": ".error_unauthorized",
    "ErrorUnauthorizedIssuesItem": ".error_unauthorized_issues_item",
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
    "ErrorBadRequest",
    "ErrorBadRequestIssuesItem",
    "ErrorForbidden",
    "ErrorForbiddenIssuesItem",
    "ErrorInternalServerError",
    "ErrorInternalServerErrorIssuesItem",
    "ErrorNotFound",
    "ErrorNotFoundIssuesItem",
    "ErrorUnauthorized",
    "ErrorUnauthorizedIssuesItem",
]
