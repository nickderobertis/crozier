



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dataset import Dataset
    from .facet import Facet
    from .investigation import Investigation
    from .solr_query import SolrQuery
    from .solr_response import SolrResponse
    from .solr_response_response import SolrResponseResponse
    from .solr_response_response_header import SolrResponseResponseHeader
    from .substance import Substance
    from .substance_composition import SubstanceComposition
    from .substance_study import SubstanceStudy
    from .substance_study_summary import SubstanceStudySummary
_dynamic_imports: typing.Dict[str, str] = {
    "Dataset": ".dataset",
    "Facet": ".facet",
    "Investigation": ".investigation",
    "SolrQuery": ".solr_query",
    "SolrResponse": ".solr_response",
    "SolrResponseResponse": ".solr_response_response",
    "SolrResponseResponseHeader": ".solr_response_response_header",
    "Substance": ".substance",
    "SubstanceComposition": ".substance_composition",
    "SubstanceStudy": ".substance_study",
    "SubstanceStudySummary": ".substance_study_summary",
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
    "Dataset",
    "Facet",
    "Investigation",
    "SolrQuery",
    "SolrResponse",
    "SolrResponseResponse",
    "SolrResponseResponseHeader",
    "Substance",
    "SubstanceComposition",
    "SubstanceStudy",
    "SubstanceStudySummary",
]
