



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AdjustConfig,
        AudioConfig,
        AudioFormat,
        AudioReference,
        BaseResponse,
        EncoderConfig,
        EnhancerConfig,
        EnhancerConfigSolver,
        FromUrl,
        GoogleTextSynthesizeResponse,
        HttpValidationError,
        InferConfig,
        InputAudio,
        SpeakerConfig,
        SpeakerReference,
        SttOutputFormat,
        SubtitleSegment,
        SynthesisInput,
        SynthesizeTtsV1TtsGetRequestNoCache,
        SynthesizeTtsV1TtsGetRequestNoCacheOne,
        TnConfig,
        TranscribeResult,
        TranscriptionsResponse,
        TtsConfig,
        ValidationError,
        ValidationErrorLocItem,
        VcConfig,
        VoiceSelectionParams,
    )
    from .errors import UnprocessableEntityError
    from . import (
        forge_v2,
        google_api,
        models,
        open_ai_api,
        speaker,
        ssml,
        stt,
        style,
        system,
        text,
        tts,
        voice_clone,
        xtts,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .text import TextNormalizeRequestPipeId
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AdjustConfig": ".types",
    "AsyncFernApi": ".client",
    "AudioConfig": ".types",
    "AudioFormat": ".types",
    "AudioReference": ".types",
    "BaseResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EncoderConfig": ".types",
    "EnhancerConfig": ".types",
    "EnhancerConfigSolver": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FromUrl": ".types",
    "GoogleTextSynthesizeResponse": ".types",
    "HttpValidationError": ".types",
    "InferConfig": ".types",
    "InputAudio": ".types",
    "SpeakerConfig": ".types",
    "SpeakerReference": ".types",
    "SttOutputFormat": ".types",
    "SubtitleSegment": ".types",
    "SynthesisInput": ".types",
    "SynthesizeTtsV1TtsGetRequestNoCache": ".types",
    "SynthesizeTtsV1TtsGetRequestNoCacheOne": ".types",
    "TextNormalizeRequestPipeId": ".text",
    "TnConfig": ".types",
    "TranscribeResult": ".types",
    "TranscriptionsResponse": ".types",
    "TtsConfig": ".types",
    "UnprocessableEntityError": ".errors",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "VcConfig": ".types",
    "VoiceSelectionParams": ".types",
    "__version__": ".version",
    "forge_v2": ".forge_v2",
    "google_api": ".google_api",
    "models": ".models",
    "open_ai_api": ".open_ai_api",
    "speaker": ".speaker",
    "ssml": ".ssml",
    "stt": ".stt",
    "style": ".style",
    "system": ".system",
    "text": ".text",
    "tts": ".tts",
    "voice_clone": ".voice_clone",
    "xtts": ".xtts",
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
    "AdjustConfig",
    "AsyncFernApi",
    "AudioConfig",
    "AudioFormat",
    "AudioReference",
    "BaseResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EncoderConfig",
    "EnhancerConfig",
    "EnhancerConfigSolver",
    "FernApi",
    "FernApiEnvironment",
    "FromUrl",
    "GoogleTextSynthesizeResponse",
    "HttpValidationError",
    "InferConfig",
    "InputAudio",
    "SpeakerConfig",
    "SpeakerReference",
    "SttOutputFormat",
    "SubtitleSegment",
    "SynthesisInput",
    "SynthesizeTtsV1TtsGetRequestNoCache",
    "SynthesizeTtsV1TtsGetRequestNoCacheOne",
    "TextNormalizeRequestPipeId",
    "TnConfig",
    "TranscribeResult",
    "TranscriptionsResponse",
    "TtsConfig",
    "UnprocessableEntityError",
    "ValidationError",
    "ValidationErrorLocItem",
    "VcConfig",
    "VoiceSelectionParams",
    "__version__",
    "forge_v2",
    "google_api",
    "models",
    "open_ai_api",
    "speaker",
    "ssml",
    "stt",
    "style",
    "system",
    "text",
    "tts",
    "voice_clone",
    "xtts",
]
