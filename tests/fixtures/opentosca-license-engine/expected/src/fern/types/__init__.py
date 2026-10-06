



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .body_generate_token_token_post import BodyGenerateTokenTokenPost
    from .conditions import Conditions
    from .http_validation_error import HttpValidationError
    from .license import License
    from .license_types import LicenseTypes
    from .limitations import Limitations
    from .permissions import Permissions
    from .user import User
    from .validation_error import ValidationError
_dynamic_imports: typing.Dict[str, str] = {
    "BodyGenerateTokenTokenPost": ".body_generate_token_token_post",
    "Conditions": ".conditions",
    "HttpValidationError": ".http_validation_error",
    "License": ".license",
    "LicenseTypes": ".license_types",
    "Limitations": ".limitations",
    "Permissions": ".permissions",
    "User": ".user",
    "ValidationError": ".validation_error",
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
    "BodyGenerateTokenTokenPost",
    "Conditions",
    "HttpValidationError",
    "License",
    "LicenseTypes",
    "Limitations",
    "Permissions",
    "User",
    "ValidationError",
]
