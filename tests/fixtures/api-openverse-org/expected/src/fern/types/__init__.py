



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .audio import Audio
    from .error import Error
    from .image import Image
    from .paginated_audio_results import PaginatedAudioResults
    from .paginated_image_results import PaginatedImageResults
    from .report_request import ReportRequest
    from .report_request_reason import ReportRequestReason
    from .source_stats import SourceStats
    from .tag import Tag
_dynamic_imports: typing.Dict[str, str] = {
    "Audio": ".audio",
    "Error": ".error",
    "Image": ".image",
    "PaginatedAudioResults": ".paginated_audio_results",
    "PaginatedImageResults": ".paginated_image_results",
    "ReportRequest": ".report_request",
    "ReportRequestReason": ".report_request_reason",
    "SourceStats": ".source_stats",
    "Tag": ".tag",
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
    "Audio",
    "Error",
    "Image",
    "PaginatedAudioResults",
    "PaginatedImageResults",
    "ReportRequest",
    "ReportRequestReason",
    "SourceStats",
    "Tag",
]
