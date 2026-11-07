



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chat_generation_request_engine import ChatGenerationRequestEngine
    from .chat_message import ChatMessage
    from .chat_message_content import ChatMessageContent
    from .chat_message_content_one_item import ChatMessageContentOneItem
    from .chat_message_role import ChatMessageRole
    from .code_generation_request_engine import CodeGenerationRequestEngine
    from .code_generation_response import CodeGenerationResponse
    from .error_response import ErrorResponse
    from .health_response import HealthResponse
    from .health_response_providers_value import HealthResponseProvidersValue
    from .health_response_status import HealthResponseStatus
    from .models_response import ModelsResponse
    from .models_response_engines_item import ModelsResponseEnginesItem
    from .models_response_engines_item_engine import ModelsResponseEnginesItemEngine
    from .models_response_engines_item_models_item import ModelsResponseEnginesItemModelsItem
    from .render_complete import RenderComplete
    from .render_error import RenderError
    from .render_progress import RenderProgress
    from .video_generation_request_aspect_ratio import VideoGenerationRequestAspectRatio
    from .video_generation_request_engine import VideoGenerationRequestEngine
    from .video_rendering_request_aspect_ratio import VideoRenderingRequestAspectRatio
    from .video_rendering_response import VideoRenderingResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ChatGenerationRequestEngine": ".chat_generation_request_engine",
    "ChatMessage": ".chat_message",
    "ChatMessageContent": ".chat_message_content",
    "ChatMessageContentOneItem": ".chat_message_content_one_item",
    "ChatMessageRole": ".chat_message_role",
    "CodeGenerationRequestEngine": ".code_generation_request_engine",
    "CodeGenerationResponse": ".code_generation_response",
    "ErrorResponse": ".error_response",
    "HealthResponse": ".health_response",
    "HealthResponseProvidersValue": ".health_response_providers_value",
    "HealthResponseStatus": ".health_response_status",
    "ModelsResponse": ".models_response",
    "ModelsResponseEnginesItem": ".models_response_engines_item",
    "ModelsResponseEnginesItemEngine": ".models_response_engines_item_engine",
    "ModelsResponseEnginesItemModelsItem": ".models_response_engines_item_models_item",
    "RenderComplete": ".render_complete",
    "RenderError": ".render_error",
    "RenderProgress": ".render_progress",
    "VideoGenerationRequestAspectRatio": ".video_generation_request_aspect_ratio",
    "VideoGenerationRequestEngine": ".video_generation_request_engine",
    "VideoRenderingRequestAspectRatio": ".video_rendering_request_aspect_ratio",
    "VideoRenderingResponse": ".video_rendering_response",
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
    "ChatGenerationRequestEngine",
    "ChatMessage",
    "ChatMessageContent",
    "ChatMessageContentOneItem",
    "ChatMessageRole",
    "CodeGenerationRequestEngine",
    "CodeGenerationResponse",
    "ErrorResponse",
    "HealthResponse",
    "HealthResponseProvidersValue",
    "HealthResponseStatus",
    "ModelsResponse",
    "ModelsResponseEnginesItem",
    "ModelsResponseEnginesItemEngine",
    "ModelsResponseEnginesItemModelsItem",
    "RenderComplete",
    "RenderError",
    "RenderProgress",
    "VideoGenerationRequestAspectRatio",
    "VideoGenerationRequestEngine",
    "VideoRenderingRequestAspectRatio",
    "VideoRenderingResponse",
]
