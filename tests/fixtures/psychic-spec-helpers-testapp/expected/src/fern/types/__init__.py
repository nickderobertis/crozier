



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .balloon import Balloon
    from .balloon_color import BalloonColor
    from .balloon_summary import BalloonSummary
    from .openapi_validation_errors import OpenapiValidationErrors
    from .openapi_validation_errors_errors_item import OpenapiValidationErrorsErrorsItem
    from .openapi_validation_errors_target import OpenapiValidationErrorsTarget
    from .openapi_validation_errors_type import OpenapiValidationErrorsType
    from .user import User
    from .validation_errors import ValidationErrors
    from .validation_errors_type import ValidationErrorsType
_dynamic_imports: typing.Dict[str, str] = {
    "Balloon": ".balloon",
    "BalloonColor": ".balloon_color",
    "BalloonSummary": ".balloon_summary",
    "OpenapiValidationErrors": ".openapi_validation_errors",
    "OpenapiValidationErrorsErrorsItem": ".openapi_validation_errors_errors_item",
    "OpenapiValidationErrorsTarget": ".openapi_validation_errors_target",
    "OpenapiValidationErrorsType": ".openapi_validation_errors_type",
    "User": ".user",
    "ValidationErrors": ".validation_errors",
    "ValidationErrorsType": ".validation_errors_type",
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
    "Balloon",
    "BalloonColor",
    "BalloonSummary",
    "OpenapiValidationErrors",
    "OpenapiValidationErrorsErrorsItem",
    "OpenapiValidationErrorsTarget",
    "OpenapiValidationErrorsType",
    "User",
    "ValidationErrors",
    "ValidationErrorsType",
]
