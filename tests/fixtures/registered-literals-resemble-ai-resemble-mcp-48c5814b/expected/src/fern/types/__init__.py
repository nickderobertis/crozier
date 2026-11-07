



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .audio_timestamps import AudioTimestamps
    from .bad_request_error_body import BadRequestErrorBody
    from .custom_pronunciation import CustomPronunciation
    from .custom_pronunciation_status import CustomPronunciationStatus
    from .detect_audio_metrics import DetectAudioMetrics
    from .detect_image_metrics import DetectImageMetrics
    from .detect_video_metrics import DetectVideoMetrics
    from .detect_video_metrics_children_item import DetectVideoMetricsChildrenItem
    from .detect_video_metrics_children_item_children_item import DetectVideoMetricsChildrenItemChildrenItem
    from .detect_video_metrics_children_item_children_item_children_item import (
        DetectVideoMetricsChildrenItemChildrenItemChildrenItem,
    )
    from .error import Error
    from .forbidden_error_body import ForbiddenErrorBody
    from .not_found_error_body import NotFoundErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "AudioTimestamps": ".audio_timestamps",
    "BadRequestErrorBody": ".bad_request_error_body",
    "CustomPronunciation": ".custom_pronunciation",
    "CustomPronunciationStatus": ".custom_pronunciation_status",
    "DetectAudioMetrics": ".detect_audio_metrics",
    "DetectImageMetrics": ".detect_image_metrics",
    "DetectVideoMetrics": ".detect_video_metrics",
    "DetectVideoMetricsChildrenItem": ".detect_video_metrics_children_item",
    "DetectVideoMetricsChildrenItemChildrenItem": ".detect_video_metrics_children_item_children_item",
    "DetectVideoMetricsChildrenItemChildrenItemChildrenItem": ".detect_video_metrics_children_item_children_item_children_item",
    "Error": ".error",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "NotFoundErrorBody": ".not_found_error_body",
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
    "AudioTimestamps",
    "BadRequestErrorBody",
    "CustomPronunciation",
    "CustomPronunciationStatus",
    "DetectAudioMetrics",
    "DetectImageMetrics",
    "DetectVideoMetrics",
    "DetectVideoMetricsChildrenItem",
    "DetectVideoMetricsChildrenItemChildrenItem",
    "DetectVideoMetricsChildrenItemChildrenItemChildrenItem",
    "Error",
    "ForbiddenErrorBody",
    "NotFoundErrorBody",
]
