



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_substance_composition_request_db import GetSubstanceCompositionRequestDb
    from .get_substance_structures_request_db import GetSubstanceStructuresRequestDb
    from .search_by_identifier_request_db import SearchByIdentifierRequestDb
    from .search_by_identifier_request_representation import SearchByIdentifierRequestRepresentation
    from .search_by_identifier_request_term import SearchByIdentifierRequestTerm
    from .search_by_similarity_request_db import SearchBySimilarityRequestDb
    from .search_by_similarity_request_type import SearchBySimilarityRequestType
    from .search_by_smarts_request_db import SearchBySmartsRequestDb
    from .search_by_smarts_request_type import SearchBySmartsRequestType
_dynamic_imports: typing.Dict[str, str] = {
    "GetSubstanceCompositionRequestDb": ".get_substance_composition_request_db",
    "GetSubstanceStructuresRequestDb": ".get_substance_structures_request_db",
    "SearchByIdentifierRequestDb": ".search_by_identifier_request_db",
    "SearchByIdentifierRequestRepresentation": ".search_by_identifier_request_representation",
    "SearchByIdentifierRequestTerm": ".search_by_identifier_request_term",
    "SearchBySimilarityRequestDb": ".search_by_similarity_request_db",
    "SearchBySimilarityRequestType": ".search_by_similarity_request_type",
    "SearchBySmartsRequestDb": ".search_by_smarts_request_db",
    "SearchBySmartsRequestType": ".search_by_smarts_request_type",
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
    "GetSubstanceCompositionRequestDb",
    "GetSubstanceStructuresRequestDb",
    "SearchByIdentifierRequestDb",
    "SearchByIdentifierRequestRepresentation",
    "SearchByIdentifierRequestTerm",
    "SearchBySimilarityRequestDb",
    "SearchBySimilarityRequestType",
    "SearchBySmartsRequestDb",
    "SearchBySmartsRequestType",
]
