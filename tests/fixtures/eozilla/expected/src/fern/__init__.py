



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AdditionalParameter,
        AdditionalParameterValueItem,
        ApiError,
        Bbox,
        Capabilities,
        ConformanceDeclaration,
        Crs,
        DataType,
        DescriptionType,
        DescriptionTypeAdditionalParameters,
        Format,
        FormatSchema,
        InlineOrRefValue,
        InlineValue,
        InputDescription,
        InputDescriptionMaxOccurs,
        JobControlOptions,
        JobInfo,
        JobList,
        JobResults,
        JobStatus,
        JobType,
        Link,
        MaxOccurs,
        Metadata,
        Output,
        OutputDescription,
        ProcessDescription,
        ProcessList,
        ProcessSummary,
        QualifiedValue,
        ResponseType,
        Schema,
        SchemaAdditionalProperties,
        SchemaDiscriminator,
        SchemaItems,
        Subscriber,
        TransmissionMode,
    )
    from .errors import InternalServerError, NotFoundError
    from . import (
        capabilities,
        conformance_declaration,
        dismiss,
        job_list,
        job_results,
        job_status,
        process_description,
        process_list,
        process_request,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AdditionalParameter": ".types",
    "AdditionalParameterValueItem": ".types",
    "ApiError": ".types",
    "AsyncFernApi": ".client",
    "Bbox": ".types",
    "Capabilities": ".types",
    "ConformanceDeclaration": ".types",
    "Crs": ".types",
    "DataType": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DescriptionType": ".types",
    "DescriptionTypeAdditionalParameters": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Format": ".types",
    "FormatSchema": ".types",
    "InlineOrRefValue": ".types",
    "InlineValue": ".types",
    "InputDescription": ".types",
    "InputDescriptionMaxOccurs": ".types",
    "InternalServerError": ".errors",
    "JobControlOptions": ".types",
    "JobInfo": ".types",
    "JobList": ".types",
    "JobResults": ".types",
    "JobStatus": ".types",
    "JobType": ".types",
    "Link": ".types",
    "MaxOccurs": ".types",
    "Metadata": ".types",
    "NotFoundError": ".errors",
    "Output": ".types",
    "OutputDescription": ".types",
    "ProcessDescription": ".types",
    "ProcessList": ".types",
    "ProcessSummary": ".types",
    "QualifiedValue": ".types",
    "ResponseType": ".types",
    "Schema": ".types",
    "SchemaAdditionalProperties": ".types",
    "SchemaDiscriminator": ".types",
    "SchemaItems": ".types",
    "Subscriber": ".types",
    "TransmissionMode": ".types",
    "__version__": ".version",
    "capabilities": ".capabilities",
    "conformance_declaration": ".conformance_declaration",
    "dismiss": ".dismiss",
    "job_list": ".job_list",
    "job_results": ".job_results",
    "job_status": ".job_status",
    "process_description": ".process_description",
    "process_list": ".process_list",
    "process_request": ".process_request",
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
    "AdditionalParameter",
    "AdditionalParameterValueItem",
    "ApiError",
    "AsyncFernApi",
    "Bbox",
    "Capabilities",
    "ConformanceDeclaration",
    "Crs",
    "DataType",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DescriptionType",
    "DescriptionTypeAdditionalParameters",
    "FernApi",
    "FernApiEnvironment",
    "Format",
    "FormatSchema",
    "InlineOrRefValue",
    "InlineValue",
    "InputDescription",
    "InputDescriptionMaxOccurs",
    "InternalServerError",
    "JobControlOptions",
    "JobInfo",
    "JobList",
    "JobResults",
    "JobStatus",
    "JobType",
    "Link",
    "MaxOccurs",
    "Metadata",
    "NotFoundError",
    "Output",
    "OutputDescription",
    "ProcessDescription",
    "ProcessList",
    "ProcessSummary",
    "QualifiedValue",
    "ResponseType",
    "Schema",
    "SchemaAdditionalProperties",
    "SchemaDiscriminator",
    "SchemaItems",
    "Subscriber",
    "TransmissionMode",
    "__version__",
    "capabilities",
    "conformance_declaration",
    "dismiss",
    "job_list",
    "job_results",
    "job_status",
    "process_description",
    "process_list",
    "process_request",
]
