



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateCategoryRequestPermissions,
        CreateCategoryResponse,
        CreateCategoryResponseCategory,
        CreateCategoryResponseCategoryCustomFields,
        CreateCategoryResponseCategoryGroupPermissionsItem,
        CreateCategoryResponseCategoryRequiredTagGroupsItem,
        GetCategoryResponse,
        GetCategoryResponseCategory,
        GetCategoryResponseCategoryCustomFields,
        GetCategoryResponseCategoryGroupPermissionsItem,
        GetCategoryResponseCategoryRequiredTagGroupsItem,
        ListCategoriesResponse,
        ListCategoriesResponseCategoryList,
        ListCategoriesResponseCategoryListCategoriesItem,
        ListCategoryTopicsResponse,
        ListCategoryTopicsResponseTopicList,
        ListCategoryTopicsResponseTopicListTopicsItem,
        ListCategoryTopicsResponseTopicListTopicsItemPostersItem,
        ListCategoryTopicsResponseUsersItem,
        UpdateCategoryRequestPermissions,
        UpdateCategoryResponse,
        UpdateCategoryResponseCategory,
        UpdateCategoryResponseCategoryCustomFields,
        UpdateCategoryResponseCategoryGroupPermissionsItem,
        UpdateCategoryResponseCategoryRequiredTagGroupsItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateCategoryRequestPermissions": ".types",
    "CreateCategoryResponse": ".types",
    "CreateCategoryResponseCategory": ".types",
    "CreateCategoryResponseCategoryCustomFields": ".types",
    "CreateCategoryResponseCategoryGroupPermissionsItem": ".types",
    "CreateCategoryResponseCategoryRequiredTagGroupsItem": ".types",
    "GetCategoryResponse": ".types",
    "GetCategoryResponseCategory": ".types",
    "GetCategoryResponseCategoryCustomFields": ".types",
    "GetCategoryResponseCategoryGroupPermissionsItem": ".types",
    "GetCategoryResponseCategoryRequiredTagGroupsItem": ".types",
    "ListCategoriesResponse": ".types",
    "ListCategoriesResponseCategoryList": ".types",
    "ListCategoriesResponseCategoryListCategoriesItem": ".types",
    "ListCategoryTopicsResponse": ".types",
    "ListCategoryTopicsResponseTopicList": ".types",
    "ListCategoryTopicsResponseTopicListTopicsItem": ".types",
    "ListCategoryTopicsResponseTopicListTopicsItemPostersItem": ".types",
    "ListCategoryTopicsResponseUsersItem": ".types",
    "UpdateCategoryRequestPermissions": ".types",
    "UpdateCategoryResponse": ".types",
    "UpdateCategoryResponseCategory": ".types",
    "UpdateCategoryResponseCategoryCustomFields": ".types",
    "UpdateCategoryResponseCategoryGroupPermissionsItem": ".types",
    "UpdateCategoryResponseCategoryRequiredTagGroupsItem": ".types",
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
    "CreateCategoryRequestPermissions",
    "CreateCategoryResponse",
    "CreateCategoryResponseCategory",
    "CreateCategoryResponseCategoryCustomFields",
    "CreateCategoryResponseCategoryGroupPermissionsItem",
    "CreateCategoryResponseCategoryRequiredTagGroupsItem",
    "GetCategoryResponse",
    "GetCategoryResponseCategory",
    "GetCategoryResponseCategoryCustomFields",
    "GetCategoryResponseCategoryGroupPermissionsItem",
    "GetCategoryResponseCategoryRequiredTagGroupsItem",
    "ListCategoriesResponse",
    "ListCategoriesResponseCategoryList",
    "ListCategoriesResponseCategoryListCategoriesItem",
    "ListCategoryTopicsResponse",
    "ListCategoryTopicsResponseTopicList",
    "ListCategoryTopicsResponseTopicListTopicsItem",
    "ListCategoryTopicsResponseTopicListTopicsItemPostersItem",
    "ListCategoryTopicsResponseUsersItem",
    "UpdateCategoryRequestPermissions",
    "UpdateCategoryResponse",
    "UpdateCategoryResponseCategory",
    "UpdateCategoryResponseCategoryCustomFields",
    "UpdateCategoryResponseCategoryGroupPermissionsItem",
    "UpdateCategoryResponseCategoryRequiredTagGroupsItem",
]
