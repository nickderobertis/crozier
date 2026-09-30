



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_endpoint_summary_request_db import GetEndpointSummaryRequestDb
    from .get_endpoint_summary_request_top import GetEndpointSummaryRequestTop
    from .get_investigation_results_request_db import GetInvestigationResultsRequestDb
    from .get_investigation_results_request_type import GetInvestigationResultsRequestType
    from .get_substance_study_request_db import GetSubstanceStudyRequestDb
    from .get_substance_study_request_top import GetSubstanceStudyRequestTop
    from .get_substance_study_summary_request_db import GetSubstanceStudySummaryRequestDb
    from .get_substance_study_summary_request_top import GetSubstanceStudySummaryRequestTop
_dynamic_imports: typing.Dict[str, str] = {
    "GetEndpointSummaryRequestDb": ".get_endpoint_summary_request_db",
    "GetEndpointSummaryRequestTop": ".get_endpoint_summary_request_top",
    "GetInvestigationResultsRequestDb": ".get_investigation_results_request_db",
    "GetInvestigationResultsRequestType": ".get_investigation_results_request_type",
    "GetSubstanceStudyRequestDb": ".get_substance_study_request_db",
    "GetSubstanceStudyRequestTop": ".get_substance_study_request_top",
    "GetSubstanceStudySummaryRequestDb": ".get_substance_study_summary_request_db",
    "GetSubstanceStudySummaryRequestTop": ".get_substance_study_summary_request_top",
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
    "GetEndpointSummaryRequestDb",
    "GetEndpointSummaryRequestTop",
    "GetInvestigationResultsRequestDb",
    "GetInvestigationResultsRequestType",
    "GetSubstanceStudyRequestDb",
    "GetSubstanceStudyRequestTop",
    "GetSubstanceStudySummaryRequestDb",
    "GetSubstanceStudySummaryRequestTop",
]
