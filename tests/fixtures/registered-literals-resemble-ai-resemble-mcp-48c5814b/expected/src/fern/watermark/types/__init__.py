



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .apply_watermark_request_prefer import ApplyWatermarkRequestPrefer
    from .apply_watermark_response import ApplyWatermarkResponse
    from .apply_watermark_response_item import ApplyWatermarkResponseItem
    from .apply_watermark_response_item_media_type import ApplyWatermarkResponseItemMediaType
    from .detect_watermark_request_prefer import DetectWatermarkRequestPrefer
    from .detect_watermark_response import DetectWatermarkResponse
    from .detect_watermark_response_item import DetectWatermarkResponseItem
    from .detect_watermark_response_item_media_type import DetectWatermarkResponseItemMediaType
    from .get_watermark_apply_result_response import GetWatermarkApplyResultResponse
    from .get_watermark_apply_result_response_item import GetWatermarkApplyResultResponseItem
    from .get_watermark_apply_result_response_item_media_type import GetWatermarkApplyResultResponseItemMediaType
    from .get_watermark_detection_result_response import GetWatermarkDetectionResultResponse
    from .get_watermark_detection_result_response_item import GetWatermarkDetectionResultResponseItem
    from .get_watermark_detection_result_response_item_media_type import (
        GetWatermarkDetectionResultResponseItemMediaType,
    )
    from .get_watermark_detection_result_response_item_metrics import GetWatermarkDetectionResultResponseItemMetrics
_dynamic_imports: typing.Dict[str, str] = {
    "ApplyWatermarkRequestPrefer": ".apply_watermark_request_prefer",
    "ApplyWatermarkResponse": ".apply_watermark_response",
    "ApplyWatermarkResponseItem": ".apply_watermark_response_item",
    "ApplyWatermarkResponseItemMediaType": ".apply_watermark_response_item_media_type",
    "DetectWatermarkRequestPrefer": ".detect_watermark_request_prefer",
    "DetectWatermarkResponse": ".detect_watermark_response",
    "DetectWatermarkResponseItem": ".detect_watermark_response_item",
    "DetectWatermarkResponseItemMediaType": ".detect_watermark_response_item_media_type",
    "GetWatermarkApplyResultResponse": ".get_watermark_apply_result_response",
    "GetWatermarkApplyResultResponseItem": ".get_watermark_apply_result_response_item",
    "GetWatermarkApplyResultResponseItemMediaType": ".get_watermark_apply_result_response_item_media_type",
    "GetWatermarkDetectionResultResponse": ".get_watermark_detection_result_response",
    "GetWatermarkDetectionResultResponseItem": ".get_watermark_detection_result_response_item",
    "GetWatermarkDetectionResultResponseItemMediaType": ".get_watermark_detection_result_response_item_media_type",
    "GetWatermarkDetectionResultResponseItemMetrics": ".get_watermark_detection_result_response_item_metrics",
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
    "ApplyWatermarkRequestPrefer",
    "ApplyWatermarkResponse",
    "ApplyWatermarkResponseItem",
    "ApplyWatermarkResponseItemMediaType",
    "DetectWatermarkRequestPrefer",
    "DetectWatermarkResponse",
    "DetectWatermarkResponseItem",
    "DetectWatermarkResponseItemMediaType",
    "GetWatermarkApplyResultResponse",
    "GetWatermarkApplyResultResponseItem",
    "GetWatermarkApplyResultResponseItemMediaType",
    "GetWatermarkDetectionResultResponse",
    "GetWatermarkDetectionResultResponseItem",
    "GetWatermarkDetectionResultResponseItemMediaType",
    "GetWatermarkDetectionResultResponseItemMetrics",
]
