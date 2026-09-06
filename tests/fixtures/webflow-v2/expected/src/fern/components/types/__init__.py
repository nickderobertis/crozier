



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_content_components_response import GetContentComponentsResponse
    from .get_content_components_response_nodes_item import (
        GetContentComponentsResponseNodesItem,
        GetContentComponentsResponseNodesItem_ComponentInstance,
        GetContentComponentsResponseNodesItem_Image,
        GetContentComponentsResponseNodesItem_SearchButton,
        GetContentComponentsResponseNodesItem_Select,
        GetContentComponentsResponseNodesItem_SubmitButton,
        GetContentComponentsResponseNodesItem_Text,
        GetContentComponentsResponseNodesItem_TextInput,
    )
    from .get_content_components_response_nodes_item_component_instance import (
        GetContentComponentsResponseNodesItemComponentInstance,
    )
    from .get_content_components_response_nodes_item_component_instance_property_overrides_item import (
        GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem,
    )
    from .get_content_components_response_nodes_item_component_instance_property_overrides_item_text import (
        GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemText,
    )
    from .get_content_components_response_nodes_item_component_instance_property_overrides_item_type import (
        GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType,
    )
    from .get_content_components_response_nodes_item_image import GetContentComponentsResponseNodesItemImage
    from .get_content_components_response_nodes_item_image_image import GetContentComponentsResponseNodesItemImageImage
    from .get_content_components_response_nodes_item_search_button import (
        GetContentComponentsResponseNodesItemSearchButton,
    )
    from .get_content_components_response_nodes_item_select import GetContentComponentsResponseNodesItemSelect
    from .get_content_components_response_nodes_item_select_choices_item import (
        GetContentComponentsResponseNodesItemSelectChoicesItem,
    )
    from .get_content_components_response_nodes_item_submit_button import (
        GetContentComponentsResponseNodesItemSubmitButton,
    )
    from .get_content_components_response_nodes_item_text import GetContentComponentsResponseNodesItemText
    from .get_content_components_response_nodes_item_text_input import GetContentComponentsResponseNodesItemTextInput
    from .get_content_components_response_nodes_item_text_text import GetContentComponentsResponseNodesItemTextText
    from .get_content_components_response_pagination import GetContentComponentsResponsePagination
    from .get_properties_components_response import GetPropertiesComponentsResponse
    from .get_properties_components_response_pagination import GetPropertiesComponentsResponsePagination
    from .get_properties_components_response_properties_item import GetPropertiesComponentsResponsePropertiesItem
    from .get_properties_components_response_properties_item_text import (
        GetPropertiesComponentsResponsePropertiesItemText,
    )
    from .get_properties_components_response_properties_item_type import (
        GetPropertiesComponentsResponsePropertiesItemType,
    )
    from .list_components_response import ListComponentsResponse
    from .list_components_response_components_item import ListComponentsResponseComponentsItem
    from .list_components_response_pagination import ListComponentsResponsePagination
    from .update_content_components_request_nodes_item import UpdateContentComponentsRequestNodesItem
    from .update_content_components_request_nodes_item_choices import UpdateContentComponentsRequestNodesItemChoices
    from .update_content_components_request_nodes_item_choices_choices_item import (
        UpdateContentComponentsRequestNodesItemChoicesChoicesItem,
    )
    from .update_content_components_request_nodes_item_five import UpdateContentComponentsRequestNodesItemFive
    from .update_content_components_request_nodes_item_placeholder import (
        UpdateContentComponentsRequestNodesItemPlaceholder,
    )
    from .update_content_components_request_nodes_item_property_overrides import (
        UpdateContentComponentsRequestNodesItemPropertyOverrides,
    )
    from .update_content_components_request_nodes_item_property_overrides_property_overrides_item import (
        UpdateContentComponentsRequestNodesItemPropertyOverridesPropertyOverridesItem,
    )
    from .update_content_components_request_nodes_item_text import UpdateContentComponentsRequestNodesItemText
    from .update_content_components_request_nodes_item_waiting_text import (
        UpdateContentComponentsRequestNodesItemWaitingText,
    )
    from .update_content_components_response import UpdateContentComponentsResponse
    from .update_properties_components_request_properties_item import UpdatePropertiesComponentsRequestPropertiesItem
    from .update_properties_components_response import UpdatePropertiesComponentsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetContentComponentsResponse": ".get_content_components_response",
    "GetContentComponentsResponseNodesItem": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponseNodesItemComponentInstance": ".get_content_components_response_nodes_item_component_instance",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem": ".get_content_components_response_nodes_item_component_instance_property_overrides_item",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemText": ".get_content_components_response_nodes_item_component_instance_property_overrides_item_text",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType": ".get_content_components_response_nodes_item_component_instance_property_overrides_item_type",
    "GetContentComponentsResponseNodesItemImage": ".get_content_components_response_nodes_item_image",
    "GetContentComponentsResponseNodesItemImageImage": ".get_content_components_response_nodes_item_image_image",
    "GetContentComponentsResponseNodesItemSearchButton": ".get_content_components_response_nodes_item_search_button",
    "GetContentComponentsResponseNodesItemSelect": ".get_content_components_response_nodes_item_select",
    "GetContentComponentsResponseNodesItemSelectChoicesItem": ".get_content_components_response_nodes_item_select_choices_item",
    "GetContentComponentsResponseNodesItemSubmitButton": ".get_content_components_response_nodes_item_submit_button",
    "GetContentComponentsResponseNodesItemText": ".get_content_components_response_nodes_item_text",
    "GetContentComponentsResponseNodesItemTextInput": ".get_content_components_response_nodes_item_text_input",
    "GetContentComponentsResponseNodesItemTextText": ".get_content_components_response_nodes_item_text_text",
    "GetContentComponentsResponseNodesItem_ComponentInstance": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponseNodesItem_Image": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponseNodesItem_SearchButton": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponseNodesItem_Select": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponseNodesItem_SubmitButton": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponseNodesItem_Text": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponseNodesItem_TextInput": ".get_content_components_response_nodes_item",
    "GetContentComponentsResponsePagination": ".get_content_components_response_pagination",
    "GetPropertiesComponentsResponse": ".get_properties_components_response",
    "GetPropertiesComponentsResponsePagination": ".get_properties_components_response_pagination",
    "GetPropertiesComponentsResponsePropertiesItem": ".get_properties_components_response_properties_item",
    "GetPropertiesComponentsResponsePropertiesItemText": ".get_properties_components_response_properties_item_text",
    "GetPropertiesComponentsResponsePropertiesItemType": ".get_properties_components_response_properties_item_type",
    "ListComponentsResponse": ".list_components_response",
    "ListComponentsResponseComponentsItem": ".list_components_response_components_item",
    "ListComponentsResponsePagination": ".list_components_response_pagination",
    "UpdateContentComponentsRequestNodesItem": ".update_content_components_request_nodes_item",
    "UpdateContentComponentsRequestNodesItemChoices": ".update_content_components_request_nodes_item_choices",
    "UpdateContentComponentsRequestNodesItemChoicesChoicesItem": ".update_content_components_request_nodes_item_choices_choices_item",
    "UpdateContentComponentsRequestNodesItemFive": ".update_content_components_request_nodes_item_five",
    "UpdateContentComponentsRequestNodesItemPlaceholder": ".update_content_components_request_nodes_item_placeholder",
    "UpdateContentComponentsRequestNodesItemPropertyOverrides": ".update_content_components_request_nodes_item_property_overrides",
    "UpdateContentComponentsRequestNodesItemPropertyOverridesPropertyOverridesItem": ".update_content_components_request_nodes_item_property_overrides_property_overrides_item",
    "UpdateContentComponentsRequestNodesItemText": ".update_content_components_request_nodes_item_text",
    "UpdateContentComponentsRequestNodesItemWaitingText": ".update_content_components_request_nodes_item_waiting_text",
    "UpdateContentComponentsResponse": ".update_content_components_response",
    "UpdatePropertiesComponentsRequestPropertiesItem": ".update_properties_components_request_properties_item",
    "UpdatePropertiesComponentsResponse": ".update_properties_components_response",
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
    "GetContentComponentsResponse",
    "GetContentComponentsResponseNodesItem",
    "GetContentComponentsResponseNodesItemComponentInstance",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemText",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType",
    "GetContentComponentsResponseNodesItemImage",
    "GetContentComponentsResponseNodesItemImageImage",
    "GetContentComponentsResponseNodesItemSearchButton",
    "GetContentComponentsResponseNodesItemSelect",
    "GetContentComponentsResponseNodesItemSelectChoicesItem",
    "GetContentComponentsResponseNodesItemSubmitButton",
    "GetContentComponentsResponseNodesItemText",
    "GetContentComponentsResponseNodesItemTextInput",
    "GetContentComponentsResponseNodesItemTextText",
    "GetContentComponentsResponseNodesItem_ComponentInstance",
    "GetContentComponentsResponseNodesItem_Image",
    "GetContentComponentsResponseNodesItem_SearchButton",
    "GetContentComponentsResponseNodesItem_Select",
    "GetContentComponentsResponseNodesItem_SubmitButton",
    "GetContentComponentsResponseNodesItem_Text",
    "GetContentComponentsResponseNodesItem_TextInput",
    "GetContentComponentsResponsePagination",
    "GetPropertiesComponentsResponse",
    "GetPropertiesComponentsResponsePagination",
    "GetPropertiesComponentsResponsePropertiesItem",
    "GetPropertiesComponentsResponsePropertiesItemText",
    "GetPropertiesComponentsResponsePropertiesItemType",
    "ListComponentsResponse",
    "ListComponentsResponseComponentsItem",
    "ListComponentsResponsePagination",
    "UpdateContentComponentsRequestNodesItem",
    "UpdateContentComponentsRequestNodesItemChoices",
    "UpdateContentComponentsRequestNodesItemChoicesChoicesItem",
    "UpdateContentComponentsRequestNodesItemFive",
    "UpdateContentComponentsRequestNodesItemPlaceholder",
    "UpdateContentComponentsRequestNodesItemPropertyOverrides",
    "UpdateContentComponentsRequestNodesItemPropertyOverridesPropertyOverridesItem",
    "UpdateContentComponentsRequestNodesItemText",
    "UpdateContentComponentsRequestNodesItemWaitingText",
    "UpdateContentComponentsResponse",
    "UpdatePropertiesComponentsRequestPropertiesItem",
    "UpdatePropertiesComponentsResponse",
]
