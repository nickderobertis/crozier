



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .base_element_options import BaseElementOptions
    from .blocks_options import BlocksOptions
    from .box import Box
    from .document import Document
    from .document_type import DocumentType
    from .element import Element
    from .element_type import ElementType
    from .error_response import ErrorResponse
    from .figure_options import FigureOptions
    from .grounding import Grounding
    from .http_validation_error import HttpValidationError
    from .page import Page
    from .page_status import PageStatus
    from .page_type import PageType
    from .parse_billing import ParseBilling
    from .parse_billing_service_tier import ParseBillingServiceTier
    from .parse_metadata import ParseMetadata
    from .parse_metadata_range_units import ParseMetadataRangeUnits
    from .parse_response import ParseResponse
    from .prebuilt_workflow_step import PrebuiltWorkflowStep
    from .prebuilt_workflow_step_name import PrebuiltWorkflowStepName
    from .range import Range
    from .table_options import TableOptions
    from .table_options_format import TableOptionsFormat
    from .v2billing import V2Billing
    from .v2billing_service_tier import V2BillingServiceTier
    from .v2extract_metadata import V2ExtractMetadata
    from .v2extract_metadata_range_units import V2ExtractMetadataRangeUnits
    from .v2extract_options import V2ExtractOptions
    from .v2ground_metadata import V2GroundMetadata
    from .v2workflow_metadata import V2WorkflowMetadata
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .workflow_document_input import WorkflowDocumentInput
    from .workflow_step_options import WorkflowStepOptions
_dynamic_imports: typing.Dict[str, str] = {
    "BaseElementOptions": ".base_element_options",
    "BlocksOptions": ".blocks_options",
    "Box": ".box",
    "Document": ".document",
    "DocumentType": ".document_type",
    "Element": ".element",
    "ElementType": ".element_type",
    "ErrorResponse": ".error_response",
    "FigureOptions": ".figure_options",
    "Grounding": ".grounding",
    "HttpValidationError": ".http_validation_error",
    "Page": ".page",
    "PageStatus": ".page_status",
    "PageType": ".page_type",
    "ParseBilling": ".parse_billing",
    "ParseBillingServiceTier": ".parse_billing_service_tier",
    "ParseMetadata": ".parse_metadata",
    "ParseMetadataRangeUnits": ".parse_metadata_range_units",
    "ParseResponse": ".parse_response",
    "PrebuiltWorkflowStep": ".prebuilt_workflow_step",
    "PrebuiltWorkflowStepName": ".prebuilt_workflow_step_name",
    "Range": ".range",
    "TableOptions": ".table_options",
    "TableOptionsFormat": ".table_options_format",
    "V2Billing": ".v2billing",
    "V2BillingServiceTier": ".v2billing_service_tier",
    "V2ExtractMetadata": ".v2extract_metadata",
    "V2ExtractMetadataRangeUnits": ".v2extract_metadata_range_units",
    "V2ExtractOptions": ".v2extract_options",
    "V2GroundMetadata": ".v2ground_metadata",
    "V2WorkflowMetadata": ".v2workflow_metadata",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "WorkflowDocumentInput": ".workflow_document_input",
    "WorkflowStepOptions": ".workflow_step_options",
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
    "BaseElementOptions",
    "BlocksOptions",
    "Box",
    "Document",
    "DocumentType",
    "Element",
    "ElementType",
    "ErrorResponse",
    "FigureOptions",
    "Grounding",
    "HttpValidationError",
    "Page",
    "PageStatus",
    "PageType",
    "ParseBilling",
    "ParseBillingServiceTier",
    "ParseMetadata",
    "ParseMetadataRangeUnits",
    "ParseResponse",
    "PrebuiltWorkflowStep",
    "PrebuiltWorkflowStepName",
    "Range",
    "TableOptions",
    "TableOptionsFormat",
    "V2Billing",
    "V2BillingServiceTier",
    "V2ExtractMetadata",
    "V2ExtractMetadataRangeUnits",
    "V2ExtractOptions",
    "V2GroundMetadata",
    "V2WorkflowMetadata",
    "ValidationError",
    "ValidationErrorLocItem",
    "WorkflowDocumentInput",
    "WorkflowStepOptions",
]
