



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .survey_ai_category_list_response_item import SurveyAiCategoryListResponseItem
    from .survey_all_response_item import SurveyAllResponseItem
    from .survey_all_response_item_payload import SurveyAllResponseItemPayload
    from .survey_all_response_item_payload_items_item import SurveyAllResponseItemPayloadItemsItem
    from .survey_all_response_item_payload_items_item_type import SurveyAllResponseItemPayloadItemsItemType
    from .survey_create_request_payload import SurveyCreateRequestPayload
    from .survey_create_request_payload_items_item import SurveyCreateRequestPayloadItemsItem
    from .survey_create_request_payload_items_item_type import SurveyCreateRequestPayloadItemsItemType
    from .survey_create_response import SurveyCreateResponse
    from .survey_create_response_payload import SurveyCreateResponsePayload
    from .survey_create_response_payload_items_item import SurveyCreateResponsePayloadItemsItem
    from .survey_create_response_payload_items_item_type import SurveyCreateResponsePayloadItemsItemType
    from .survey_delete_response import SurveyDeleteResponse
    from .survey_delete_response_payload import SurveyDeleteResponsePayload
    from .survey_delete_response_payload_items_item import SurveyDeleteResponsePayloadItemsItem
    from .survey_delete_response_payload_items_item_type import SurveyDeleteResponsePayloadItemsItemType
    from .survey_duplicate_response import SurveyDuplicateResponse
    from .survey_duplicate_response_payload import SurveyDuplicateResponsePayload
    from .survey_duplicate_response_payload_items_item import SurveyDuplicateResponsePayloadItemsItem
    from .survey_duplicate_response_payload_items_item_type import SurveyDuplicateResponsePayloadItemsItemType
    from .survey_get_response import SurveyGetResponse
    from .survey_get_response_payload import SurveyGetResponsePayload
    from .survey_get_response_payload_items_item import SurveyGetResponsePayloadItemsItem
    from .survey_get_response_payload_items_item_type import SurveyGetResponsePayloadItemsItemType
    from .survey_get_result_response import SurveyGetResultResponse
    from .survey_result_list_response import SurveyResultListResponse
    from .survey_result_list_response_items_item import SurveyResultListResponseItemsItem
    from .survey_stats_response_item import SurveyStatsResponseItem
    from .survey_submit_response import SurveySubmitResponse
    from .survey_update_request_payload import SurveyUpdateRequestPayload
    from .survey_update_request_payload_items_item import SurveyUpdateRequestPayloadItemsItem
    from .survey_update_request_payload_items_item_type import SurveyUpdateRequestPayloadItemsItemType
    from .survey_update_response import SurveyUpdateResponse
    from .survey_update_response_payload import SurveyUpdateResponsePayload
    from .survey_update_response_payload_items_item import SurveyUpdateResponsePayloadItemsItem
    from .survey_update_response_payload_items_item_type import SurveyUpdateResponsePayloadItemsItemType
_dynamic_imports: typing.Dict[str, str] = {
    "SurveyAiCategoryListResponseItem": ".survey_ai_category_list_response_item",
    "SurveyAllResponseItem": ".survey_all_response_item",
    "SurveyAllResponseItemPayload": ".survey_all_response_item_payload",
    "SurveyAllResponseItemPayloadItemsItem": ".survey_all_response_item_payload_items_item",
    "SurveyAllResponseItemPayloadItemsItemType": ".survey_all_response_item_payload_items_item_type",
    "SurveyCreateRequestPayload": ".survey_create_request_payload",
    "SurveyCreateRequestPayloadItemsItem": ".survey_create_request_payload_items_item",
    "SurveyCreateRequestPayloadItemsItemType": ".survey_create_request_payload_items_item_type",
    "SurveyCreateResponse": ".survey_create_response",
    "SurveyCreateResponsePayload": ".survey_create_response_payload",
    "SurveyCreateResponsePayloadItemsItem": ".survey_create_response_payload_items_item",
    "SurveyCreateResponsePayloadItemsItemType": ".survey_create_response_payload_items_item_type",
    "SurveyDeleteResponse": ".survey_delete_response",
    "SurveyDeleteResponsePayload": ".survey_delete_response_payload",
    "SurveyDeleteResponsePayloadItemsItem": ".survey_delete_response_payload_items_item",
    "SurveyDeleteResponsePayloadItemsItemType": ".survey_delete_response_payload_items_item_type",
    "SurveyDuplicateResponse": ".survey_duplicate_response",
    "SurveyDuplicateResponsePayload": ".survey_duplicate_response_payload",
    "SurveyDuplicateResponsePayloadItemsItem": ".survey_duplicate_response_payload_items_item",
    "SurveyDuplicateResponsePayloadItemsItemType": ".survey_duplicate_response_payload_items_item_type",
    "SurveyGetResponse": ".survey_get_response",
    "SurveyGetResponsePayload": ".survey_get_response_payload",
    "SurveyGetResponsePayloadItemsItem": ".survey_get_response_payload_items_item",
    "SurveyGetResponsePayloadItemsItemType": ".survey_get_response_payload_items_item_type",
    "SurveyGetResultResponse": ".survey_get_result_response",
    "SurveyResultListResponse": ".survey_result_list_response",
    "SurveyResultListResponseItemsItem": ".survey_result_list_response_items_item",
    "SurveyStatsResponseItem": ".survey_stats_response_item",
    "SurveySubmitResponse": ".survey_submit_response",
    "SurveyUpdateRequestPayload": ".survey_update_request_payload",
    "SurveyUpdateRequestPayloadItemsItem": ".survey_update_request_payload_items_item",
    "SurveyUpdateRequestPayloadItemsItemType": ".survey_update_request_payload_items_item_type",
    "SurveyUpdateResponse": ".survey_update_response",
    "SurveyUpdateResponsePayload": ".survey_update_response_payload",
    "SurveyUpdateResponsePayloadItemsItem": ".survey_update_response_payload_items_item",
    "SurveyUpdateResponsePayloadItemsItemType": ".survey_update_response_payload_items_item_type",
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
