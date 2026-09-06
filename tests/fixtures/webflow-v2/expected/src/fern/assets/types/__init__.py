



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_assets_response import CreateAssetsResponse
    from .create_assets_response_upload_details import CreateAssetsResponseUploadDetails
    from .create_folder_assets_response import CreateFolderAssetsResponse
    from .get_assets_response import GetAssetsResponse
    from .get_assets_response_variants_item import GetAssetsResponseVariantsItem
    from .get_folder_assets_response import GetFolderAssetsResponse
    from .list_assets_response import ListAssetsResponse
    from .list_assets_response_assets_item import ListAssetsResponseAssetsItem
    from .list_assets_response_assets_item_variants_item import ListAssetsResponseAssetsItemVariantsItem
    from .list_assets_response_pagination import ListAssetsResponsePagination
    from .list_folders_assets_response import ListFoldersAssetsResponse
    from .list_folders_assets_response_asset_folders_item import ListFoldersAssetsResponseAssetFoldersItem
    from .list_folders_assets_response_pagination import ListFoldersAssetsResponsePagination
    from .update_assets_response import UpdateAssetsResponse
    from .update_assets_response_variants_item import UpdateAssetsResponseVariantsItem
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAssetsResponse": ".create_assets_response",
    "CreateAssetsResponseUploadDetails": ".create_assets_response_upload_details",
    "CreateFolderAssetsResponse": ".create_folder_assets_response",
    "GetAssetsResponse": ".get_assets_response",
    "GetAssetsResponseVariantsItem": ".get_assets_response_variants_item",
    "GetFolderAssetsResponse": ".get_folder_assets_response",
    "ListAssetsResponse": ".list_assets_response",
    "ListAssetsResponseAssetsItem": ".list_assets_response_assets_item",
    "ListAssetsResponseAssetsItemVariantsItem": ".list_assets_response_assets_item_variants_item",
    "ListAssetsResponsePagination": ".list_assets_response_pagination",
    "ListFoldersAssetsResponse": ".list_folders_assets_response",
    "ListFoldersAssetsResponseAssetFoldersItem": ".list_folders_assets_response_asset_folders_item",
    "ListFoldersAssetsResponsePagination": ".list_folders_assets_response_pagination",
    "UpdateAssetsResponse": ".update_assets_response",
    "UpdateAssetsResponseVariantsItem": ".update_assets_response_variants_item",
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
    "CreateAssetsResponse",
    "CreateAssetsResponseUploadDetails",
    "CreateFolderAssetsResponse",
    "GetAssetsResponse",
    "GetAssetsResponseVariantsItem",
    "GetFolderAssetsResponse",
    "ListAssetsResponse",
    "ListAssetsResponseAssetsItem",
    "ListAssetsResponseAssetsItemVariantsItem",
    "ListAssetsResponsePagination",
    "ListFoldersAssetsResponse",
    "ListFoldersAssetsResponseAssetFoldersItem",
    "ListFoldersAssetsResponsePagination",
    "UpdateAssetsResponse",
    "UpdateAssetsResponseVariantsItem",
]
