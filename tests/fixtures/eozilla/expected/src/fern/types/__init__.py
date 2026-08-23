



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .additional_parameter import AdditionalParameter
    from .additional_parameter_value_item import AdditionalParameterValueItem
    from .api_error import ApiError
    from .bbox import Bbox
    from .capabilities import Capabilities
    from .conformance_declaration import ConformanceDeclaration
    from .crs import Crs
    from .data_type import DataType
    from .description_type import DescriptionType
    from .description_type_additional_parameters import DescriptionTypeAdditionalParameters
    from .format import Format
    from .format_schema import FormatSchema
    from .inline_or_ref_value import InlineOrRefValue
    from .inline_value import InlineValue
    from .input_description import InputDescription
    from .input_description_max_occurs import InputDescriptionMaxOccurs
    from .job_control_options import JobControlOptions
    from .job_info import JobInfo
    from .job_list import JobList
    from .job_results import JobResults
    from .job_status import JobStatus
    from .job_type import JobType
    from .link import Link
    from .max_occurs import MaxOccurs
    from .metadata import Metadata
    from .output import Output
    from .output_description import OutputDescription
    from .process_description import ProcessDescription
    from .process_list import ProcessList
    from .process_summary import ProcessSummary
    from .qualified_value import QualifiedValue
    from .response_type import ResponseType
    from .schema import Schema
    from .schema_additional_properties import SchemaAdditionalProperties
    from .schema_discriminator import SchemaDiscriminator
    from .schema_items import SchemaItems
    from .subscriber import Subscriber
    from .transmission_mode import TransmissionMode
_dynamic_imports: typing.Dict[str, str] = {
    "AdditionalParameter": ".additional_parameter",
    "AdditionalParameterValueItem": ".additional_parameter_value_item",
    "ApiError": ".api_error",
    "Bbox": ".bbox",
    "Capabilities": ".capabilities",
    "ConformanceDeclaration": ".conformance_declaration",
    "Crs": ".crs",
    "DataType": ".data_type",
    "DescriptionType": ".description_type",
    "DescriptionTypeAdditionalParameters": ".description_type_additional_parameters",
    "Format": ".format",
    "FormatSchema": ".format_schema",
    "InlineOrRefValue": ".inline_or_ref_value",
    "InlineValue": ".inline_value",
    "InputDescription": ".input_description",
    "InputDescriptionMaxOccurs": ".input_description_max_occurs",
    "JobControlOptions": ".job_control_options",
    "JobInfo": ".job_info",
    "JobList": ".job_list",
    "JobResults": ".job_results",
    "JobStatus": ".job_status",
    "JobType": ".job_type",
    "Link": ".link",
    "MaxOccurs": ".max_occurs",
    "Metadata": ".metadata",
    "Output": ".output",
    "OutputDescription": ".output_description",
    "ProcessDescription": ".process_description",
    "ProcessList": ".process_list",
    "ProcessSummary": ".process_summary",
    "QualifiedValue": ".qualified_value",
    "ResponseType": ".response_type",
    "Schema": ".schema",
    "SchemaAdditionalProperties": ".schema_additional_properties",
    "SchemaDiscriminator": ".schema_discriminator",
    "SchemaItems": ".schema_items",
    "Subscriber": ".subscriber",
    "TransmissionMode": ".transmission_mode",
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
    "Bbox",
    "Capabilities",
    "ConformanceDeclaration",
    "Crs",
    "DataType",
    "DescriptionType",
    "DescriptionTypeAdditionalParameters",
    "Format",
    "FormatSchema",
    "InlineOrRefValue",
    "InlineValue",
    "InputDescription",
    "InputDescriptionMaxOccurs",
    "JobControlOptions",
    "JobInfo",
    "JobList",
    "JobResults",
    "JobStatus",
    "JobType",
    "Link",
    "MaxOccurs",
    "Metadata",
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
]
