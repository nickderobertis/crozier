



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .error_response import ErrorResponse
    from .internal_server_error_body import InternalServerErrorBody
    from .job import Job
    from .job_response import JobResponse
    from .job_source import JobSource
    from .job_status import JobStatus
    from .unauthorized_response import UnauthorizedResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ErrorResponse": ".error_response",
    "InternalServerErrorBody": ".internal_server_error_body",
    "Job": ".job",
    "JobResponse": ".job_response",
    "JobSource": ".job_source",
    "JobStatus": ".job_status",
    "UnauthorizedResponse": ".unauthorized_response",
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
    "ErrorResponse",
    "InternalServerErrorBody",
    "Job",
    "JobResponse",
    "JobSource",
    "JobStatus",
    "UnauthorizedResponse",
]
