



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetContentComponentsResponse,
        GetContentComponentsResponseNodesItem,
        GetContentComponentsResponseNodesItemComponentInstance,
        GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem,
        GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemText,
        GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType,
        GetContentComponentsResponseNodesItemImage,
        GetContentComponentsResponseNodesItemImageImage,
        GetContentComponentsResponseNodesItemSearchButton,
        GetContentComponentsResponseNodesItemSelect,
        GetContentComponentsResponseNodesItemSelectChoicesItem,
        GetContentComponentsResponseNodesItemSubmitButton,
        GetContentComponentsResponseNodesItemText,
        GetContentComponentsResponseNodesItemTextInput,
        GetContentComponentsResponseNodesItemTextText,
        GetContentComponentsResponseNodesItem_ComponentInstance,
        GetContentComponentsResponseNodesItem_Image,
        GetContentComponentsResponseNodesItem_SearchButton,
        GetContentComponentsResponseNodesItem_Select,
        GetContentComponentsResponseNodesItem_SubmitButton,
        GetContentComponentsResponseNodesItem_Text,
        GetContentComponentsResponseNodesItem_TextInput,
        GetContentComponentsResponsePagination,
        GetPropertiesComponentsResponse,
        GetPropertiesComponentsResponsePagination,
        GetPropertiesComponentsResponsePropertiesItem,
        GetPropertiesComponentsResponsePropertiesItemText,
        GetPropertiesComponentsResponsePropertiesItemType,
        ListComponentsResponse,
        ListComponentsResponseComponentsItem,
        ListComponentsResponsePagination,
        UpdateContentComponentsRequestNodesItem,
        UpdateContentComponentsRequestNodesItemChoices,
        UpdateContentComponentsRequestNodesItemChoicesChoicesItem,
        UpdateContentComponentsRequestNodesItemFive,
        UpdateContentComponentsRequestNodesItemPlaceholder,
        UpdateContentComponentsRequestNodesItemPropertyOverrides,
        UpdateContentComponentsRequestNodesItemPropertyOverridesPropertyOverridesItem,
        UpdateContentComponentsRequestNodesItemText,
        UpdateContentComponentsRequestNodesItemWaitingText,
        UpdateContentComponentsResponse,
        UpdatePropertiesComponentsRequestPropertiesItem,
        UpdatePropertiesComponentsResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetContentComponentsResponse": ".types",
    "GetContentComponentsResponseNodesItem": ".types",
    "GetContentComponentsResponseNodesItemComponentInstance": ".types",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem": ".types",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemText": ".types",
    "GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType": ".types",
    "GetContentComponentsResponseNodesItemImage": ".types",
    "GetContentComponentsResponseNodesItemImageImage": ".types",
    "GetContentComponentsResponseNodesItemSearchButton": ".types",
    "GetContentComponentsResponseNodesItemSelect": ".types",
    "GetContentComponentsResponseNodesItemSelectChoicesItem": ".types",
    "GetContentComponentsResponseNodesItemSubmitButton": ".types",
    "GetContentComponentsResponseNodesItemText": ".types",
    "GetContentComponentsResponseNodesItemTextInput": ".types",
    "GetContentComponentsResponseNodesItemTextText": ".types",
    "GetContentComponentsResponseNodesItem_ComponentInstance": ".types",
    "GetContentComponentsResponseNodesItem_Image": ".types",
    "GetContentComponentsResponseNodesItem_SearchButton": ".types",
    "GetContentComponentsResponseNodesItem_Select": ".types",
    "GetContentComponentsResponseNodesItem_SubmitButton": ".types",
    "GetContentComponentsResponseNodesItem_Text": ".types",
    "GetContentComponentsResponseNodesItem_TextInput": ".types",
    "GetContentComponentsResponsePagination": ".types",
    "GetPropertiesComponentsResponse": ".types",
    "GetPropertiesComponentsResponsePagination": ".types",
    "GetPropertiesComponentsResponsePropertiesItem": ".types",
    "GetPropertiesComponentsResponsePropertiesItemText": ".types",
    "GetPropertiesComponentsResponsePropertiesItemType": ".types",
    "ListComponentsResponse": ".types",
    "ListComponentsResponseComponentsItem": ".types",
    "ListComponentsResponsePagination": ".types",
    "UpdateContentComponentsRequestNodesItem": ".types",
    "UpdateContentComponentsRequestNodesItemChoices": ".types",
    "UpdateContentComponentsRequestNodesItemChoicesChoicesItem": ".types",
    "UpdateContentComponentsRequestNodesItemFive": ".types",
    "UpdateContentComponentsRequestNodesItemPlaceholder": ".types",
    "UpdateContentComponentsRequestNodesItemPropertyOverrides": ".types",
    "UpdateContentComponentsRequestNodesItemPropertyOverridesPropertyOverridesItem": ".types",
    "UpdateContentComponentsRequestNodesItemText": ".types",
    "UpdateContentComponentsRequestNodesItemWaitingText": ".types",
    "UpdateContentComponentsResponse": ".types",
    "UpdatePropertiesComponentsRequestPropertiesItem": ".types",
    "UpdatePropertiesComponentsResponse": ".types",
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
