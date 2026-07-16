



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bulk_mapping_job import BulkMappingJob
    from .bulk_mapping_job_result import BulkMappingJobResult
    from .figi_result import FigiResult
    from .get_mapping_values_key_request_key import GetMappingValuesKeyRequestKey
    from .get_mapping_values_key_response import GetMappingValuesKeyResponse
    from .mapping_job import MappingJob
    from .mapping_job_id_type import MappingJobIdType
    from .mapping_job_id_value import MappingJobIdValue
    from .mapping_job_option_type import MappingJobOptionType
    from .mapping_job_result import MappingJobResult
    from .mapping_job_result_figi_list import MappingJobResultFigiList
    from .mapping_job_result_figi_not_found import MappingJobResultFigiNotFound
    from .mapping_job_state_code import MappingJobStateCode
    from .nullable_date_interval import NullableDateInterval
    from .nullable_number_interval import NullableNumberInterval
_dynamic_imports: typing.Dict[str, str] = {
    "BulkMappingJob": ".bulk_mapping_job",
    "BulkMappingJobResult": ".bulk_mapping_job_result",
    "FigiResult": ".figi_result",
    "GetMappingValuesKeyRequestKey": ".get_mapping_values_key_request_key",
    "GetMappingValuesKeyResponse": ".get_mapping_values_key_response",
    "MappingJob": ".mapping_job",
    "MappingJobIdType": ".mapping_job_id_type",
    "MappingJobIdValue": ".mapping_job_id_value",
    "MappingJobOptionType": ".mapping_job_option_type",
    "MappingJobResult": ".mapping_job_result",
    "MappingJobResultFigiList": ".mapping_job_result_figi_list",
    "MappingJobResultFigiNotFound": ".mapping_job_result_figi_not_found",
    "MappingJobStateCode": ".mapping_job_state_code",
    "NullableDateInterval": ".nullable_date_interval",
    "NullableNumberInterval": ".nullable_number_interval",
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
    "BulkMappingJob",
    "BulkMappingJobResult",
    "FigiResult",
    "GetMappingValuesKeyRequestKey",
    "GetMappingValuesKeyResponse",
    "MappingJob",
    "MappingJobIdType",
    "MappingJobIdValue",
    "MappingJobOptionType",
    "MappingJobResult",
    "MappingJobResultFigiList",
    "MappingJobResultFigiNotFound",
    "MappingJobStateCode",
    "NullableDateInterval",
    "NullableNumberInterval",
]
