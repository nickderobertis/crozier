



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_books_by_series_id_request_media_status_item import GetBooksBySeriesIdRequestMediaStatusItem
    from .get_books_by_series_id_request_read_status_item import GetBooksBySeriesIdRequestReadStatusItem
    from .get_series_alphabetical_groups_deprecated_request_read_status_item import (
        GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem,
    )
    from .get_series_alphabetical_groups_deprecated_request_status_item import (
        GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem,
    )
    from .get_series_deprecated_request_read_status_item import GetSeriesDeprecatedRequestReadStatusItem
    from .get_series_deprecated_request_status_item import GetSeriesDeprecatedRequestStatusItem
    from .series_metadata_update_dto_reading_direction import SeriesMetadataUpdateDtoReadingDirection
    from .series_metadata_update_dto_status import SeriesMetadataUpdateDtoStatus
_dynamic_imports: typing.Dict[str, str] = {
    "GetBooksBySeriesIdRequestMediaStatusItem": ".get_books_by_series_id_request_media_status_item",
    "GetBooksBySeriesIdRequestReadStatusItem": ".get_books_by_series_id_request_read_status_item",
    "GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem": ".get_series_alphabetical_groups_deprecated_request_read_status_item",
    "GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem": ".get_series_alphabetical_groups_deprecated_request_status_item",
    "GetSeriesDeprecatedRequestReadStatusItem": ".get_series_deprecated_request_read_status_item",
    "GetSeriesDeprecatedRequestStatusItem": ".get_series_deprecated_request_status_item",
    "SeriesMetadataUpdateDtoReadingDirection": ".series_metadata_update_dto_reading_direction",
    "SeriesMetadataUpdateDtoStatus": ".series_metadata_update_dto_status",
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
    "GetBooksBySeriesIdRequestMediaStatusItem",
    "GetBooksBySeriesIdRequestReadStatusItem",
    "GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem",
    "GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem",
    "GetSeriesDeprecatedRequestReadStatusItem",
    "GetSeriesDeprecatedRequestStatusItem",
    "SeriesMetadataUpdateDtoReadingDirection",
    "SeriesMetadataUpdateDtoStatus",
]
