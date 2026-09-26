



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .apis_v1components_error import ApisV1ComponentsError
    from .apis_v1components_error_code import ApisV1ComponentsErrorCode
    from .apis_v1components_error_response import ApisV1ComponentsErrorResponse
    from .apis_v1components_observation_scope import ApisV1ComponentsObservationScope
    from .job import Job
    from .job_outcome import JobOutcome
    from .job_status import JobStatus
    from .job_terminal import JobTerminal
    from .profiling_capabilities import ProfilingCapabilities
    from .profiling_capabilities_response import ProfilingCapabilitiesResponse
    from .profiling_capability import ProfilingCapability
    from .profiling_job import ProfilingJob
    from .profiling_job_list_response import ProfilingJobListResponse
    from .profiling_job_list_response_data import ProfilingJobListResponseData
    from .profiling_job_response import ProfilingJobResponse
    from .profiling_language import ProfilingLanguage
    from .profiling_mode import ProfilingMode
    from .profiling_type import ProfilingType
    from .protobuf_payload import ProtobufPayload
    from .raw_profile import RawProfile
    from .raw_profile_page import RawProfilePage
    from .raw_profile_page_response import RawProfilePageResponse
    from .tracing_capabilities import TracingCapabilities
    from .tracing_capabilities_response import TracingCapabilitiesResponse
    from .tracing_capability import TracingCapability
    from .tracing_job import TracingJob
    from .tracing_job_list_response import TracingJobListResponse
    from .tracing_job_list_response_data import TracingJobListResponseData
    from .tracing_job_response import TracingJobResponse
    from .tracing_type import TracingType
_dynamic_imports: typing.Dict[str, str] = {
    "ApisV1ComponentsError": ".apis_v1components_error",
    "ApisV1ComponentsErrorCode": ".apis_v1components_error_code",
    "ApisV1ComponentsErrorResponse": ".apis_v1components_error_response",
    "ApisV1ComponentsObservationScope": ".apis_v1components_observation_scope",
    "Job": ".job",
    "JobOutcome": ".job_outcome",
    "JobStatus": ".job_status",
    "JobTerminal": ".job_terminal",
    "ProfilingCapabilities": ".profiling_capabilities",
    "ProfilingCapabilitiesResponse": ".profiling_capabilities_response",
    "ProfilingCapability": ".profiling_capability",
    "ProfilingJob": ".profiling_job",
    "ProfilingJobListResponse": ".profiling_job_list_response",
    "ProfilingJobListResponseData": ".profiling_job_list_response_data",
    "ProfilingJobResponse": ".profiling_job_response",
    "ProfilingLanguage": ".profiling_language",
    "ProfilingMode": ".profiling_mode",
    "ProfilingType": ".profiling_type",
    "ProtobufPayload": ".protobuf_payload",
    "RawProfile": ".raw_profile",
    "RawProfilePage": ".raw_profile_page",
    "RawProfilePageResponse": ".raw_profile_page_response",
    "TracingCapabilities": ".tracing_capabilities",
    "TracingCapabilitiesResponse": ".tracing_capabilities_response",
    "TracingCapability": ".tracing_capability",
    "TracingJob": ".tracing_job",
    "TracingJobListResponse": ".tracing_job_list_response",
    "TracingJobListResponseData": ".tracing_job_list_response_data",
    "TracingJobResponse": ".tracing_job_response",
    "TracingType": ".tracing_type",
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
    "ApisV1ComponentsError",
    "ApisV1ComponentsErrorCode",
    "ApisV1ComponentsErrorResponse",
    "ApisV1ComponentsObservationScope",
    "Job",
    "JobOutcome",
    "JobStatus",
    "JobTerminal",
    "ProfilingCapabilities",
    "ProfilingCapabilitiesResponse",
    "ProfilingCapability",
    "ProfilingJob",
    "ProfilingJobListResponse",
    "ProfilingJobListResponseData",
    "ProfilingJobResponse",
    "ProfilingLanguage",
    "ProfilingMode",
    "ProfilingType",
    "ProtobufPayload",
    "RawProfile",
    "RawProfilePage",
    "RawProfilePageResponse",
    "TracingCapabilities",
    "TracingCapabilitiesResponse",
    "TracingCapability",
    "TracingJob",
    "TracingJobListResponse",
    "TracingJobListResponseData",
    "TracingJobResponse",
    "TracingType",
]
