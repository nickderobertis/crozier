



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .files_detail_response_item import FilesDetailResponseItem
    from .files_detail_response_item_attributes import FilesDetailResponseItemAttributes
    from .files_detail_response_item_links import FilesDetailResponseItemLinks
    from .files_detail_response_item_relationships import FilesDetailResponseItemRelationships
    from .files_version_detail_response_item import FilesVersionDetailResponseItem
    from .files_version_detail_response_item_attributes import FilesVersionDetailResponseItemAttributes
    from .files_version_detail_response_item_links import FilesVersionDetailResponseItemLinks
    from .files_versions_response_item import FilesVersionsResponseItem
    from .files_versions_response_item_attributes import FilesVersionsResponseItemAttributes
    from .files_versions_response_item_links import FilesVersionsResponseItemLinks
_dynamic_imports: typing.Dict[str, str] = {
    "FilesDetailResponseItem": ".files_detail_response_item",
    "FilesDetailResponseItemAttributes": ".files_detail_response_item_attributes",
    "FilesDetailResponseItemLinks": ".files_detail_response_item_links",
    "FilesDetailResponseItemRelationships": ".files_detail_response_item_relationships",
    "FilesVersionDetailResponseItem": ".files_version_detail_response_item",
    "FilesVersionDetailResponseItemAttributes": ".files_version_detail_response_item_attributes",
    "FilesVersionDetailResponseItemLinks": ".files_version_detail_response_item_links",
    "FilesVersionsResponseItem": ".files_versions_response_item",
    "FilesVersionsResponseItemAttributes": ".files_versions_response_item_attributes",
    "FilesVersionsResponseItemLinks": ".files_versions_response_item_links",
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
    "FilesDetailResponseItem",
    "FilesDetailResponseItemAttributes",
    "FilesDetailResponseItemLinks",
    "FilesDetailResponseItemRelationships",
    "FilesVersionDetailResponseItem",
    "FilesVersionDetailResponseItemAttributes",
    "FilesVersionDetailResponseItemLinks",
    "FilesVersionsResponseItem",
    "FilesVersionsResponseItemAttributes",
    "FilesVersionsResponseItemLinks",
]
