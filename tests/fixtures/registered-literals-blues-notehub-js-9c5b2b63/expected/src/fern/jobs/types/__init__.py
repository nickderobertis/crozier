



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cancel_job_run_response import CancelJobRunResponse
    from .create_job_response import CreateJobResponse
    from .delete_job_response import DeleteJobResponse
    from .get_job_run_request_view import GetJobRunRequestView
    from .get_job_runs_response import GetJobRunsResponse
    from .get_jobs_response import GetJobsResponse
    from .run_job_response import RunJobResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CancelJobRunResponse": ".cancel_job_run_response",
    "CreateJobResponse": ".create_job_response",
    "DeleteJobResponse": ".delete_job_response",
    "GetJobRunRequestView": ".get_job_run_request_view",
    "GetJobRunsResponse": ".get_job_runs_response",
    "GetJobsResponse": ".get_jobs_response",
    "RunJobResponse": ".run_job_response",
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
    "CancelJobRunResponse",
    "CreateJobResponse",
    "DeleteJobResponse",
    "GetJobRunRequestView",
    "GetJobRunsResponse",
    "GetJobsResponse",
    "RunJobResponse",
]
