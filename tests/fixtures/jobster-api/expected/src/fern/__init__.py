



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import Error, JobInput, JobInputJobType, JobInputStatus, UserProfile
    from .errors import BadRequestError, ConflictError, NotFoundError, UnauthorizedError
    from . import auth, jobs
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .jobs import GetJobsRequestJobType, GetJobsRequestSort, GetJobsRequestStatus
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetJobsRequestJobType": ".jobs",
    "GetJobsRequestSort": ".jobs",
    "GetJobsRequestStatus": ".jobs",
    "JobInput": ".types",
    "JobInputJobType": ".types",
    "JobInputStatus": ".types",
    "NotFoundError": ".errors",
    "UnauthorizedError": ".errors",
    "UserProfile": ".types",
    "__version__": ".version",
    "auth": ".auth",
    "jobs": ".jobs",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "GetJobsRequestJobType",
    "GetJobsRequestSort",
    "GetJobsRequestStatus",
    "JobInput",
    "JobInputJobType",
    "JobInputStatus",
    "NotFoundError",
    "UnauthorizedError",
    "UserProfile",
    "__version__",
    "auth",
    "jobs",
]
