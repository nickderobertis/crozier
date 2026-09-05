



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Container,
        ContainerCpu,
        ContainerEnvVar,
        ContainerImage,
        ContainerList,
        ContainerMemory,
        ContainerMetadata,
        ContainerNetwork,
        ContainerPort,
        ContainerPortVisibility,
        ContainerProcess,
        ContainerResources,
        ContainerSpec,
        ContainerSpecServiceType,
        ContainerStatus,
        Error,
        ErrorDetail,
        ErrorType,
        Health,
        ServiceInfo,
        ServiceInfoType,
        ServicePort,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        UnauthorizedError,
    )
    from . import containers, health
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "Container": ".types",
    "ContainerCpu": ".types",
    "ContainerEnvVar": ".types",
    "ContainerImage": ".types",
    "ContainerList": ".types",
    "ContainerMemory": ".types",
    "ContainerMetadata": ".types",
    "ContainerNetwork": ".types",
    "ContainerPort": ".types",
    "ContainerPortVisibility": ".types",
    "ContainerProcess": ".types",
    "ContainerResources": ".types",
    "ContainerSpec": ".types",
    "ContainerSpecServiceType": ".types",
    "ContainerStatus": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "ErrorDetail": ".types",
    "ErrorType": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "Health": ".types",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "ServiceInfo": ".types",
    "ServiceInfoType": ".types",
    "ServicePort": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "containers": ".containers",
    "health": ".health",
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
    "ConflictError",
    "Container",
    "ContainerCpu",
    "ContainerEnvVar",
    "ContainerImage",
    "ContainerList",
    "ContainerMemory",
    "ContainerMetadata",
    "ContainerNetwork",
    "ContainerPort",
    "ContainerPortVisibility",
    "ContainerProcess",
    "ContainerResources",
    "ContainerSpec",
    "ContainerSpecServiceType",
    "ContainerStatus",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "ErrorDetail",
    "ErrorType",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "Health",
    "InternalServerError",
    "NotFoundError",
    "ServiceInfo",
    "ServiceInfoType",
    "ServicePort",
    "UnauthorizedError",
    "__version__",
    "containers",
    "health",
]
