



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_content_pages_response import GetContentPagesResponse
    from .get_content_pages_response_nodes_item import (
        GetContentPagesResponseNodesItem,
        GetContentPagesResponseNodesItem_ComponentInstance,
        GetContentPagesResponseNodesItem_Image,
        GetContentPagesResponseNodesItem_SearchButton,
        GetContentPagesResponseNodesItem_Select,
        GetContentPagesResponseNodesItem_SubmitButton,
        GetContentPagesResponseNodesItem_Text,
        GetContentPagesResponseNodesItem_TextInput,
    )
    from .get_content_pages_response_nodes_item_component_instance import (
        GetContentPagesResponseNodesItemComponentInstance,
    )
    from .get_content_pages_response_nodes_item_component_instance_property_overrides_item import (
        GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItem,
    )
    from .get_content_pages_response_nodes_item_component_instance_property_overrides_item_text import (
        GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItemText,
    )
    from .get_content_pages_response_nodes_item_component_instance_property_overrides_item_type import (
        GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItemType,
    )
    from .get_content_pages_response_nodes_item_image import GetContentPagesResponseNodesItemImage
    from .get_content_pages_response_nodes_item_image_image import GetContentPagesResponseNodesItemImageImage
    from .get_content_pages_response_nodes_item_search_button import GetContentPagesResponseNodesItemSearchButton
    from .get_content_pages_response_nodes_item_select import GetContentPagesResponseNodesItemSelect
    from .get_content_pages_response_nodes_item_select_choices_item import (
        GetContentPagesResponseNodesItemSelectChoicesItem,
    )
    from .get_content_pages_response_nodes_item_submit_button import GetContentPagesResponseNodesItemSubmitButton
    from .get_content_pages_response_nodes_item_text import GetContentPagesResponseNodesItemText
    from .get_content_pages_response_nodes_item_text_input import GetContentPagesResponseNodesItemTextInput
    from .get_content_pages_response_nodes_item_text_text import GetContentPagesResponseNodesItemTextText
    from .get_content_pages_response_pagination import GetContentPagesResponsePagination
    from .get_metadata_pages_response import GetMetadataPagesResponse
    from .get_metadata_pages_response_open_graph import GetMetadataPagesResponseOpenGraph
    from .get_metadata_pages_response_seo import GetMetadataPagesResponseSeo
    from .list_pages_response import ListPagesResponse
    from .list_pages_response_pages_item import ListPagesResponsePagesItem
    from .list_pages_response_pages_item_open_graph import ListPagesResponsePagesItemOpenGraph
    from .list_pages_response_pages_item_seo import ListPagesResponsePagesItemSeo
    from .list_pages_response_pagination import ListPagesResponsePagination
    from .page_created_payload import PageCreatedPayload
    from .page_created_payload_payload import PageCreatedPayloadPayload
    from .page_deleted_payload import PageDeletedPayload
    from .page_deleted_payload_payload import PageDeletedPayloadPayload
    from .page_metadata_updated_payload import PageMetadataUpdatedPayload
    from .page_metadata_updated_payload_payload import PageMetadataUpdatedPayloadPayload
    from .update_page_settings_request_open_graph import UpdatePageSettingsRequestOpenGraph
    from .update_page_settings_request_seo import UpdatePageSettingsRequestSeo
    from .update_page_settings_response import UpdatePageSettingsResponse
    from .update_page_settings_response_open_graph import UpdatePageSettingsResponseOpenGraph
    from .update_page_settings_response_seo import UpdatePageSettingsResponseSeo
    from .update_static_content_request_nodes_item import UpdateStaticContentRequestNodesItem
    from .update_static_content_request_nodes_item_choices import UpdateStaticContentRequestNodesItemChoices
    from .update_static_content_request_nodes_item_choices_choices_item import (
        UpdateStaticContentRequestNodesItemChoicesChoicesItem,
    )
    from .update_static_content_request_nodes_item_five import UpdateStaticContentRequestNodesItemFive
    from .update_static_content_request_nodes_item_placeholder import UpdateStaticContentRequestNodesItemPlaceholder
    from .update_static_content_request_nodes_item_property_overrides import (
        UpdateStaticContentRequestNodesItemPropertyOverrides,
    )
    from .update_static_content_request_nodes_item_property_overrides_property_overrides_item import (
        UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem,
    )
    from .update_static_content_request_nodes_item_text import UpdateStaticContentRequestNodesItemText
    from .update_static_content_request_nodes_item_waiting_text import UpdateStaticContentRequestNodesItemWaitingText
    from .update_static_content_response import UpdateStaticContentResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetContentPagesResponse": ".get_content_pages_response",
    "GetContentPagesResponseNodesItem": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponseNodesItemComponentInstance": ".get_content_pages_response_nodes_item_component_instance",
    "GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItem": ".get_content_pages_response_nodes_item_component_instance_property_overrides_item",
    "GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItemText": ".get_content_pages_response_nodes_item_component_instance_property_overrides_item_text",
    "GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItemType": ".get_content_pages_response_nodes_item_component_instance_property_overrides_item_type",
    "GetContentPagesResponseNodesItemImage": ".get_content_pages_response_nodes_item_image",
    "GetContentPagesResponseNodesItemImageImage": ".get_content_pages_response_nodes_item_image_image",
    "GetContentPagesResponseNodesItemSearchButton": ".get_content_pages_response_nodes_item_search_button",
    "GetContentPagesResponseNodesItemSelect": ".get_content_pages_response_nodes_item_select",
    "GetContentPagesResponseNodesItemSelectChoicesItem": ".get_content_pages_response_nodes_item_select_choices_item",
    "GetContentPagesResponseNodesItemSubmitButton": ".get_content_pages_response_nodes_item_submit_button",
    "GetContentPagesResponseNodesItemText": ".get_content_pages_response_nodes_item_text",
    "GetContentPagesResponseNodesItemTextInput": ".get_content_pages_response_nodes_item_text_input",
    "GetContentPagesResponseNodesItemTextText": ".get_content_pages_response_nodes_item_text_text",
    "GetContentPagesResponseNodesItem_ComponentInstance": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponseNodesItem_Image": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponseNodesItem_SearchButton": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponseNodesItem_Select": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponseNodesItem_SubmitButton": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponseNodesItem_Text": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponseNodesItem_TextInput": ".get_content_pages_response_nodes_item",
    "GetContentPagesResponsePagination": ".get_content_pages_response_pagination",
    "GetMetadataPagesResponse": ".get_metadata_pages_response",
    "GetMetadataPagesResponseOpenGraph": ".get_metadata_pages_response_open_graph",
    "GetMetadataPagesResponseSeo": ".get_metadata_pages_response_seo",
    "ListPagesResponse": ".list_pages_response",
    "ListPagesResponsePagesItem": ".list_pages_response_pages_item",
    "ListPagesResponsePagesItemOpenGraph": ".list_pages_response_pages_item_open_graph",
    "ListPagesResponsePagesItemSeo": ".list_pages_response_pages_item_seo",
    "ListPagesResponsePagination": ".list_pages_response_pagination",
    "PageCreatedPayload": ".page_created_payload",
    "PageCreatedPayloadPayload": ".page_created_payload_payload",
    "PageDeletedPayload": ".page_deleted_payload",
    "PageDeletedPayloadPayload": ".page_deleted_payload_payload",
    "PageMetadataUpdatedPayload": ".page_metadata_updated_payload",
    "PageMetadataUpdatedPayloadPayload": ".page_metadata_updated_payload_payload",
    "UpdatePageSettingsRequestOpenGraph": ".update_page_settings_request_open_graph",
    "UpdatePageSettingsRequestSeo": ".update_page_settings_request_seo",
    "UpdatePageSettingsResponse": ".update_page_settings_response",
    "UpdatePageSettingsResponseOpenGraph": ".update_page_settings_response_open_graph",
    "UpdatePageSettingsResponseSeo": ".update_page_settings_response_seo",
    "UpdateStaticContentRequestNodesItem": ".update_static_content_request_nodes_item",
    "UpdateStaticContentRequestNodesItemChoices": ".update_static_content_request_nodes_item_choices",
    "UpdateStaticContentRequestNodesItemChoicesChoicesItem": ".update_static_content_request_nodes_item_choices_choices_item",
    "UpdateStaticContentRequestNodesItemFive": ".update_static_content_request_nodes_item_five",
    "UpdateStaticContentRequestNodesItemPlaceholder": ".update_static_content_request_nodes_item_placeholder",
    "UpdateStaticContentRequestNodesItemPropertyOverrides": ".update_static_content_request_nodes_item_property_overrides",
    "UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem": ".update_static_content_request_nodes_item_property_overrides_property_overrides_item",
    "UpdateStaticContentRequestNodesItemText": ".update_static_content_request_nodes_item_text",
    "UpdateStaticContentRequestNodesItemWaitingText": ".update_static_content_request_nodes_item_waiting_text",
    "UpdateStaticContentResponse": ".update_static_content_response",
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
    "GetContentPagesResponse",
    "GetContentPagesResponseNodesItem",
    "GetContentPagesResponseNodesItemComponentInstance",
    "GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItem",
    "GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItemText",
    "GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItemType",
    "GetContentPagesResponseNodesItemImage",
    "GetContentPagesResponseNodesItemImageImage",
    "GetContentPagesResponseNodesItemSearchButton",
    "GetContentPagesResponseNodesItemSelect",
    "GetContentPagesResponseNodesItemSelectChoicesItem",
    "GetContentPagesResponseNodesItemSubmitButton",
    "GetContentPagesResponseNodesItemText",
    "GetContentPagesResponseNodesItemTextInput",
    "GetContentPagesResponseNodesItemTextText",
    "GetContentPagesResponseNodesItem_ComponentInstance",
    "GetContentPagesResponseNodesItem_Image",
    "GetContentPagesResponseNodesItem_SearchButton",
    "GetContentPagesResponseNodesItem_Select",
    "GetContentPagesResponseNodesItem_SubmitButton",
    "GetContentPagesResponseNodesItem_Text",
    "GetContentPagesResponseNodesItem_TextInput",
    "GetContentPagesResponsePagination",
    "GetMetadataPagesResponse",
    "GetMetadataPagesResponseOpenGraph",
    "GetMetadataPagesResponseSeo",
    "ListPagesResponse",
    "ListPagesResponsePagesItem",
    "ListPagesResponsePagesItemOpenGraph",
    "ListPagesResponsePagesItemSeo",
    "ListPagesResponsePagination",
    "PageCreatedPayload",
    "PageCreatedPayloadPayload",
    "PageDeletedPayload",
    "PageDeletedPayloadPayload",
    "PageMetadataUpdatedPayload",
    "PageMetadataUpdatedPayloadPayload",
    "UpdatePageSettingsRequestOpenGraph",
    "UpdatePageSettingsRequestSeo",
    "UpdatePageSettingsResponse",
    "UpdatePageSettingsResponseOpenGraph",
    "UpdatePageSettingsResponseSeo",
    "UpdateStaticContentRequestNodesItem",
    "UpdateStaticContentRequestNodesItemChoices",
    "UpdateStaticContentRequestNodesItemChoicesChoicesItem",
    "UpdateStaticContentRequestNodesItemFive",
    "UpdateStaticContentRequestNodesItemPlaceholder",
    "UpdateStaticContentRequestNodesItemPropertyOverrides",
    "UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem",
    "UpdateStaticContentRequestNodesItemText",
    "UpdateStaticContentRequestNodesItemWaitingText",
    "UpdateStaticContentResponse",
]
