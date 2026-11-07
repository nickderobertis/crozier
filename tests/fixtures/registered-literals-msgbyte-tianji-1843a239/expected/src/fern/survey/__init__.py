



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        SurveyAiCategoryListResponseItem,
        SurveyAllResponseItem,
        SurveyAllResponseItemPayload,
        SurveyAllResponseItemPayloadItemsItem,
        SurveyAllResponseItemPayloadItemsItemType,
        SurveyCreateRequestPayload,
        SurveyCreateRequestPayloadItemsItem,
        SurveyCreateRequestPayloadItemsItemType,
        SurveyCreateResponse,
        SurveyCreateResponsePayload,
        SurveyCreateResponsePayloadItemsItem,
        SurveyCreateResponsePayloadItemsItemType,
        SurveyDeleteResponse,
        SurveyDeleteResponsePayload,
        SurveyDeleteResponsePayloadItemsItem,
        SurveyDeleteResponsePayloadItemsItemType,
        SurveyDuplicateResponse,
        SurveyDuplicateResponsePayload,
        SurveyDuplicateResponsePayloadItemsItem,
        SurveyDuplicateResponsePayloadItemsItemType,
        SurveyGetResponse,
        SurveyGetResponsePayload,
        SurveyGetResponsePayloadItemsItem,
        SurveyGetResponsePayloadItemsItemType,
        SurveyGetResultResponse,
        SurveyResultListResponse,
        SurveyResultListResponseItemsItem,
        SurveyStatsResponseItem,
        SurveySubmitResponse,
        SurveyUpdateRequestPayload,
        SurveyUpdateRequestPayloadItemsItem,
        SurveyUpdateRequestPayloadItemsItemType,
        SurveyUpdateResponse,
        SurveyUpdateResponsePayload,
        SurveyUpdateResponsePayloadItemsItem,
        SurveyUpdateResponsePayloadItemsItemType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "SurveyAiCategoryListResponseItem": ".types",
    "SurveyAllResponseItem": ".types",
    "SurveyAllResponseItemPayload": ".types",
    "SurveyAllResponseItemPayloadItemsItem": ".types",
    "SurveyAllResponseItemPayloadItemsItemType": ".types",
    "SurveyCreateRequestPayload": ".types",
    "SurveyCreateRequestPayloadItemsItem": ".types",
    "SurveyCreateRequestPayloadItemsItemType": ".types",
    "SurveyCreateResponse": ".types",
    "SurveyCreateResponsePayload": ".types",
    "SurveyCreateResponsePayloadItemsItem": ".types",
    "SurveyCreateResponsePayloadItemsItemType": ".types",
    "SurveyDeleteResponse": ".types",
    "SurveyDeleteResponsePayload": ".types",
    "SurveyDeleteResponsePayloadItemsItem": ".types",
    "SurveyDeleteResponsePayloadItemsItemType": ".types",
    "SurveyDuplicateResponse": ".types",
    "SurveyDuplicateResponsePayload": ".types",
    "SurveyDuplicateResponsePayloadItemsItem": ".types",
    "SurveyDuplicateResponsePayloadItemsItemType": ".types",
    "SurveyGetResponse": ".types",
    "SurveyGetResponsePayload": ".types",
    "SurveyGetResponsePayloadItemsItem": ".types",
    "SurveyGetResponsePayloadItemsItemType": ".types",
    "SurveyGetResultResponse": ".types",
    "SurveyResultListResponse": ".types",
    "SurveyResultListResponseItemsItem": ".types",
    "SurveyStatsResponseItem": ".types",
    "SurveySubmitResponse": ".types",
    "SurveyUpdateRequestPayload": ".types",
    "SurveyUpdateRequestPayloadItemsItem": ".types",
    "SurveyUpdateRequestPayloadItemsItemType": ".types",
    "SurveyUpdateResponse": ".types",
    "SurveyUpdateResponsePayload": ".types",
    "SurveyUpdateResponsePayloadItemsItem": ".types",
    "SurveyUpdateResponsePayloadItemsItemType": ".types",
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
    "SurveyAiCategoryListResponseItem",
    "SurveyAllResponseItem",
    "SurveyAllResponseItemPayload",
    "SurveyAllResponseItemPayloadItemsItem",
    "SurveyAllResponseItemPayloadItemsItemType",
    "SurveyCreateRequestPayload",
    "SurveyCreateRequestPayloadItemsItem",
    "SurveyCreateRequestPayloadItemsItemType",
    "SurveyCreateResponse",
    "SurveyCreateResponsePayload",
    "SurveyCreateResponsePayloadItemsItem",
    "SurveyCreateResponsePayloadItemsItemType",
    "SurveyDeleteResponse",
    "SurveyDeleteResponsePayload",
    "SurveyDeleteResponsePayloadItemsItem",
    "SurveyDeleteResponsePayloadItemsItemType",
    "SurveyDuplicateResponse",
    "SurveyDuplicateResponsePayload",
    "SurveyDuplicateResponsePayloadItemsItem",
    "SurveyDuplicateResponsePayloadItemsItemType",
    "SurveyGetResponse",
    "SurveyGetResponsePayload",
    "SurveyGetResponsePayloadItemsItem",
    "SurveyGetResponsePayloadItemsItemType",
    "SurveyGetResultResponse",
    "SurveyResultListResponse",
    "SurveyResultListResponseItemsItem",
    "SurveyStatsResponseItem",
    "SurveySubmitResponse",
    "SurveyUpdateRequestPayload",
    "SurveyUpdateRequestPayloadItemsItem",
    "SurveyUpdateRequestPayloadItemsItemType",
    "SurveyUpdateResponse",
    "SurveyUpdateResponsePayload",
    "SurveyUpdateResponsePayloadItemsItem",
    "SurveyUpdateResponsePayloadItemsItemType",
]
