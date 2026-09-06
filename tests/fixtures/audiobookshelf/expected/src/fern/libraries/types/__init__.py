



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_libraries_response import GetLibrariesResponse
    from .get_library_authors_response import GetLibraryAuthorsResponse
    from .get_library_items_response import GetLibraryItemsResponse
    from .get_library_series_by_id_request_sort import GetLibrarySeriesByIdRequestSort
    from .get_library_series_request_sort import GetLibrarySeriesRequestSort
    from .get_library_series_response import GetLibrarySeriesResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetLibrariesResponse": ".get_libraries_response",
    "GetLibraryAuthorsResponse": ".get_library_authors_response",
    "GetLibraryItemsResponse": ".get_library_items_response",
    "GetLibrarySeriesByIdRequestSort": ".get_library_series_by_id_request_sort",
    "GetLibrarySeriesRequestSort": ".get_library_series_request_sort",
    "GetLibrarySeriesResponse": ".get_library_series_response",
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
    "GetLibrariesResponse",
    "GetLibraryAuthorsResponse",
    "GetLibraryItemsResponse",
    "GetLibrarySeriesByIdRequestSort",
    "GetLibrarySeriesRequestSort",
    "GetLibrarySeriesResponse",
]
