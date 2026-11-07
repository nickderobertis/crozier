



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_intelligence_response import GetIntelligenceResponse
    from .get_intelligence_response_item import GetIntelligenceResponseItem
    from .get_intelligence_response_item_media_type import GetIntelligenceResponseItemMediaType
    from .list_intelligences_response import ListIntelligencesResponse
    from .list_intelligences_response_items_item import ListIntelligencesResponseItemsItem
    from .list_intelligences_response_items_item_media_type import ListIntelligencesResponseItemsItemMediaType
    from .run_intelligence_request_media_type import RunIntelligenceRequestMediaType
    from .run_intelligence_response import RunIntelligenceResponse
    from .run_intelligence_response_item import RunIntelligenceResponseItem
    from .run_intelligence_response_item_description import RunIntelligenceResponseItemDescription
    from .run_intelligence_response_item_media_type import RunIntelligenceResponseItemMediaType
_dynamic_imports: typing.Dict[str, str] = {
    "GetIntelligenceResponse": ".get_intelligence_response",
    "GetIntelligenceResponseItem": ".get_intelligence_response_item",
    "GetIntelligenceResponseItemMediaType": ".get_intelligence_response_item_media_type",
    "ListIntelligencesResponse": ".list_intelligences_response",
    "ListIntelligencesResponseItemsItem": ".list_intelligences_response_items_item",
    "ListIntelligencesResponseItemsItemMediaType": ".list_intelligences_response_items_item_media_type",
    "RunIntelligenceRequestMediaType": ".run_intelligence_request_media_type",
    "RunIntelligenceResponse": ".run_intelligence_response",
    "RunIntelligenceResponseItem": ".run_intelligence_response_item",
    "RunIntelligenceResponseItemDescription": ".run_intelligence_response_item_description",
    "RunIntelligenceResponseItemMediaType": ".run_intelligence_response_item_media_type",
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
    "GetIntelligenceResponse",
    "GetIntelligenceResponseItem",
    "GetIntelligenceResponseItemMediaType",
    "ListIntelligencesResponse",
    "ListIntelligencesResponseItemsItem",
    "ListIntelligencesResponseItemsItemMediaType",
    "RunIntelligenceRequestMediaType",
    "RunIntelligenceResponse",
    "RunIntelligenceResponseItem",
    "RunIntelligenceResponseItemDescription",
    "RunIntelligenceResponseItemMediaType",
]
