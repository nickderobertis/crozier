



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_error import ApiError
    from .audio_response import AudioResponse
    from .chunk import Chunk
    from .gpu_compute_info import GpuComputeInfo
    from .gpu_utilization_info import GpuUtilizationInfo
    from .hardware_information import HardwareInformation
    from .hardware_stats import HardwareStats
    from .health_check import HealthCheck
    from .health_check_status import HealthCheckStatus
    from .http_error import HttpError
    from .http_validation_error import HttpValidationError
    from .image_response import ImageResponse
    from .image_to_text_response import ImageToTextResponse
    from .live_video_to_video_response import LiveVideoToVideoResponse
    from .llm_choice import LlmChoice
    from .llm_message import LlmMessage
    from .llm_response import LlmResponse
    from .llm_token_usage import LlmTokenUsage
    from .masks_response import MasksResponse
    from .media import Media
    from .media_url import MediaUrl
    from .text_response import TextResponse
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .video_response import VideoResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ApiError": ".api_error",
    "AudioResponse": ".audio_response",
    "Chunk": ".chunk",
    "GpuComputeInfo": ".gpu_compute_info",
    "GpuUtilizationInfo": ".gpu_utilization_info",
    "HardwareInformation": ".hardware_information",
    "HardwareStats": ".hardware_stats",
    "HealthCheck": ".health_check",
    "HealthCheckStatus": ".health_check_status",
    "HttpError": ".http_error",
    "HttpValidationError": ".http_validation_error",
    "ImageResponse": ".image_response",
    "ImageToTextResponse": ".image_to_text_response",
    "LiveVideoToVideoResponse": ".live_video_to_video_response",
    "LlmChoice": ".llm_choice",
    "LlmMessage": ".llm_message",
    "LlmResponse": ".llm_response",
    "LlmTokenUsage": ".llm_token_usage",
    "MasksResponse": ".masks_response",
    "Media": ".media",
    "MediaUrl": ".media_url",
    "TextResponse": ".text_response",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VideoResponse": ".video_response",
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
    "ApiError",
    "AudioResponse",
    "Chunk",
    "GpuComputeInfo",
    "GpuUtilizationInfo",
    "HardwareInformation",
    "HardwareStats",
    "HealthCheck",
    "HealthCheckStatus",
    "HttpError",
    "HttpValidationError",
    "ImageResponse",
    "ImageToTextResponse",
    "LiveVideoToVideoResponse",
    "LlmChoice",
    "LlmMessage",
    "LlmResponse",
    "LlmTokenUsage",
    "MasksResponse",
    "Media",
    "MediaUrl",
    "TextResponse",
    "ValidationError",
    "ValidationErrorLocItem",
    "VideoResponse",
]
