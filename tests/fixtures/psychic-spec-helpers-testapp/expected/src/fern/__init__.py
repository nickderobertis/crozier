



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Balloon,
        BalloonColor,
        BalloonSummary,
        OpenapiValidationErrors,
        OpenapiValidationErrorsErrorsItem,
        OpenapiValidationErrorsTarget,
        OpenapiValidationErrorsType,
        User,
        ValidationErrors,
        ValidationErrorsType,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        UnauthorizedError,
        UnprocessableEntityError,
    )
    from . import balloons
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .balloons import (
        PatchUsersUserIdBalloonsIdRequestColor,
        PostUsersUserIdBalloonsRequestColor,
        PutUsersUserIdBalloonsIdUpdatePutRequestColor,
    )
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Balloon": ".types",
    "BalloonColor": ".types",
    "BalloonSummary": ".types",
    "ConflictError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "ForbiddenError": ".errors",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "OpenapiValidationErrors": ".types",
    "OpenapiValidationErrorsErrorsItem": ".types",
    "OpenapiValidationErrorsTarget": ".types",
    "OpenapiValidationErrorsType": ".types",
    "PatchUsersUserIdBalloonsIdRequestColor": ".balloons",
    "PostUsersUserIdBalloonsRequestColor": ".balloons",
    "PutUsersUserIdBalloonsIdUpdatePutRequestColor": ".balloons",
    "UnauthorizedError": ".errors",
    "UnprocessableEntityError": ".errors",
    "User": ".types",
    "ValidationErrors": ".types",
    "ValidationErrorsType": ".types",
    "__version__": ".version",
    "balloons": ".balloons",
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
    "AsyncFernApi",
    "BadRequestError",
    "Balloon",
    "BalloonColor",
    "BalloonSummary",
    "ConflictError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "ForbiddenError",
    "InternalServerError",
    "NotFoundError",
    "OpenapiValidationErrors",
    "OpenapiValidationErrorsErrorsItem",
    "OpenapiValidationErrorsTarget",
    "OpenapiValidationErrorsType",
    "PatchUsersUserIdBalloonsIdRequestColor",
    "PostUsersUserIdBalloonsRequestColor",
    "PutUsersUserIdBalloonsIdUpdatePutRequestColor",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "User",
    "ValidationErrors",
    "ValidationErrorsType",
    "__version__",
    "balloons",
]
