



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_agents_for_folder_request_order import ListAgentsForFolderRequestOrder
    from .list_agents_for_folder_request_order_by import ListAgentsForFolderRequestOrderBy
    from .list_files_for_folder_request_order import ListFilesForFolderRequestOrder
    from .list_files_for_folder_request_order_by import ListFilesForFolderRequestOrderBy
    from .list_folder_passages_request_order import ListFolderPassagesRequestOrder
    from .list_folder_passages_request_order_by import ListFolderPassagesRequestOrderBy
    from .list_folders_request_order import ListFoldersRequestOrder
    from .list_folders_request_order_by import ListFoldersRequestOrderBy
_dynamic_imports: typing.Dict[str, str] = {
    "ListAgentsForFolderRequestOrder": ".list_agents_for_folder_request_order",
    "ListAgentsForFolderRequestOrderBy": ".list_agents_for_folder_request_order_by",
    "ListFilesForFolderRequestOrder": ".list_files_for_folder_request_order",
    "ListFilesForFolderRequestOrderBy": ".list_files_for_folder_request_order_by",
    "ListFolderPassagesRequestOrder": ".list_folder_passages_request_order",
    "ListFolderPassagesRequestOrderBy": ".list_folder_passages_request_order_by",
    "ListFoldersRequestOrder": ".list_folders_request_order",
    "ListFoldersRequestOrderBy": ".list_folders_request_order_by",
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
    "ListAgentsForFolderRequestOrder",
    "ListAgentsForFolderRequestOrderBy",
    "ListFilesForFolderRequestOrder",
    "ListFilesForFolderRequestOrderBy",
    "ListFolderPassagesRequestOrder",
    "ListFolderPassagesRequestOrderBy",
    "ListFoldersRequestOrder",
    "ListFoldersRequestOrderBy",
]
