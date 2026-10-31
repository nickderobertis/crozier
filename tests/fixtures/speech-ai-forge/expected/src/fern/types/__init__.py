



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .adjust_config import AdjustConfig
    from .audio_config import AudioConfig
    from .audio_format import AudioFormat
    from .audio_reference import AudioReference
    from .base_response import BaseResponse
    from .encoder_config import EncoderConfig
    from .enhancer_config import EnhancerConfig
    from .enhancer_config_solver import EnhancerConfigSolver
    from .from_url import FromUrl
    from .google_text_synthesize_response import GoogleTextSynthesizeResponse
    from .http_validation_error import HttpValidationError
    from .infer_config import InferConfig
    from .input_audio import InputAudio
    from .speaker_config import SpeakerConfig
    from .speaker_reference import SpeakerReference
    from .stt_output_format import SttOutputFormat
    from .subtitle_segment import SubtitleSegment
    from .synthesis_input import SynthesisInput
    from .synthesize_tts_v1tts_get_request_no_cache import SynthesizeTtsV1TtsGetRequestNoCache
    from .synthesize_tts_v1tts_get_request_no_cache_one import SynthesizeTtsV1TtsGetRequestNoCacheOne
    from .tn_config import TnConfig
    from .transcribe_result import TranscribeResult
    from .transcriptions_response import TranscriptionsResponse
    from .tts_config import TtsConfig
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .vc_config import VcConfig
    from .voice_selection_params import VoiceSelectionParams
_dynamic_imports: typing.Dict[str, str] = {
    "AdjustConfig": ".adjust_config",
    "AudioConfig": ".audio_config",
    "AudioFormat": ".audio_format",
    "AudioReference": ".audio_reference",
    "BaseResponse": ".base_response",
    "EncoderConfig": ".encoder_config",
    "EnhancerConfig": ".enhancer_config",
    "EnhancerConfigSolver": ".enhancer_config_solver",
    "FromUrl": ".from_url",
    "GoogleTextSynthesizeResponse": ".google_text_synthesize_response",
    "HttpValidationError": ".http_validation_error",
    "InferConfig": ".infer_config",
    "InputAudio": ".input_audio",
    "SpeakerConfig": ".speaker_config",
    "SpeakerReference": ".speaker_reference",
    "SttOutputFormat": ".stt_output_format",
    "SubtitleSegment": ".subtitle_segment",
    "SynthesisInput": ".synthesis_input",
    "SynthesizeTtsV1TtsGetRequestNoCache": ".synthesize_tts_v1tts_get_request_no_cache",
    "SynthesizeTtsV1TtsGetRequestNoCacheOne": ".synthesize_tts_v1tts_get_request_no_cache_one",
    "TnConfig": ".tn_config",
    "TranscribeResult": ".transcribe_result",
    "TranscriptionsResponse": ".transcriptions_response",
    "TtsConfig": ".tts_config",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VcConfig": ".vc_config",
    "VoiceSelectionParams": ".voice_selection_params",
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
    "AudioConfig",
    "AudioFormat",
    "AudioReference",
    "BaseResponse",
    "EncoderConfig",
    "EnhancerConfig",
    "EnhancerConfigSolver",
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
    "TnConfig",
    "TranscribeResult",
    "TranscriptionsResponse",
    "TtsConfig",
    "ValidationError",
    "ValidationErrorLocItem",
    "VcConfig",
    "VoiceSelectionParams",
]
