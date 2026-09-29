



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Dataset,
        Facet,
        Investigation,
        SolrQuery,
        SolrResponse,
        SolrResponseResponse,
        SolrResponseResponseHeader,
        Substance,
        SubstanceComposition,
        SubstanceStudy,
        SubstanceStudySummary,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ForbiddenError,
        InternalServerError,
        NotExtendedError,
        NotFoundError,
        ServiceUnavailableError,
        UnauthorizedError,
        UnsupportedMediaTypeError,
    )
    from . import search, structures, studies, substances
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .search import SolrqueryGetRequestWt, SolrqueryPostRequestParams, SolrqueryPostRequestWt
    from .structures import (
        GetSubstanceCompositionRequestDb,
        GetSubstanceStructuresRequestDb,
        SearchByIdentifierRequestDb,
        SearchByIdentifierRequestRepresentation,
        SearchByIdentifierRequestTerm,
        SearchBySimilarityRequestDb,
        SearchBySimilarityRequestType,
        SearchBySmartsRequestDb,
        SearchBySmartsRequestType,
    )
    from .studies import (
        GetEndpointSummaryRequestDb,
        GetEndpointSummaryRequestTop,
        GetInvestigationResultsRequestDb,
        GetInvestigationResultsRequestType,
        GetSubstanceStudyRequestDb,
        GetSubstanceStudyRequestTop,
        GetSubstanceStudySummaryRequestDb,
        GetSubstanceStudySummaryRequestTop,
    )
    from .substances import GetSubstanceByUuidRequestDb, GetSubstancesRequestDb, GetSubstancesRequestType
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "Dataset": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Facet": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GetEndpointSummaryRequestDb": ".studies",
    "GetEndpointSummaryRequestTop": ".studies",
    "GetInvestigationResultsRequestDb": ".studies",
    "GetInvestigationResultsRequestType": ".studies",
    "GetSubstanceByUuidRequestDb": ".substances",
    "GetSubstanceCompositionRequestDb": ".structures",
    "GetSubstanceStructuresRequestDb": ".structures",
    "GetSubstanceStudyRequestDb": ".studies",
    "GetSubstanceStudyRequestTop": ".studies",
    "GetSubstanceStudySummaryRequestDb": ".studies",
    "GetSubstanceStudySummaryRequestTop": ".studies",
    "GetSubstancesRequestDb": ".substances",
    "GetSubstancesRequestType": ".substances",
    "InternalServerError": ".errors",
    "Investigation": ".types",
    "NotExtendedError": ".errors",
    "NotFoundError": ".errors",
    "SearchByIdentifierRequestDb": ".structures",
    "SearchByIdentifierRequestRepresentation": ".structures",
    "SearchByIdentifierRequestTerm": ".structures",
    "SearchBySimilarityRequestDb": ".structures",
    "SearchBySimilarityRequestType": ".structures",
    "SearchBySmartsRequestDb": ".structures",
    "SearchBySmartsRequestType": ".structures",
    "ServiceUnavailableError": ".errors",
    "SolrQuery": ".types",
    "SolrResponse": ".types",
    "SolrResponseResponse": ".types",
    "SolrResponseResponseHeader": ".types",
    "SolrqueryGetRequestWt": ".search",
    "SolrqueryPostRequestParams": ".search",
    "SolrqueryPostRequestWt": ".search",
    "Substance": ".types",
    "SubstanceComposition": ".types",
    "SubstanceStudy": ".types",
    "SubstanceStudySummary": ".types",
    "UnauthorizedError": ".errors",
    "UnsupportedMediaTypeError": ".errors",
    "__version__": ".version",
    "search": ".search",
    "structures": ".structures",
    "studies": ".studies",
    "substances": ".substances",
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
    "Dataset",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Facet",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GetEndpointSummaryRequestDb",
    "GetEndpointSummaryRequestTop",
    "GetInvestigationResultsRequestDb",
    "GetInvestigationResultsRequestType",
    "GetSubstanceByUuidRequestDb",
    "GetSubstanceCompositionRequestDb",
    "GetSubstanceStructuresRequestDb",
    "GetSubstanceStudyRequestDb",
    "GetSubstanceStudyRequestTop",
    "GetSubstanceStudySummaryRequestDb",
    "GetSubstanceStudySummaryRequestTop",
    "GetSubstancesRequestDb",
    "GetSubstancesRequestType",
    "InternalServerError",
    "Investigation",
    "NotExtendedError",
    "NotFoundError",
    "SearchByIdentifierRequestDb",
    "SearchByIdentifierRequestRepresentation",
    "SearchByIdentifierRequestTerm",
    "SearchBySimilarityRequestDb",
    "SearchBySimilarityRequestType",
    "SearchBySmartsRequestDb",
    "SearchBySmartsRequestType",
    "ServiceUnavailableError",
    "SolrQuery",
    "SolrResponse",
    "SolrResponseResponse",
    "SolrResponseResponseHeader",
    "SolrqueryGetRequestWt",
    "SolrqueryPostRequestParams",
    "SolrqueryPostRequestWt",
    "Substance",
    "SubstanceComposition",
    "SubstanceStudy",
    "SubstanceStudySummary",
    "UnauthorizedError",
    "UnsupportedMediaTypeError",
    "__version__",
    "search",
    "structures",
    "studies",
    "substances",
]
