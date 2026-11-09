



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_speech_request_model import CreateSpeechRequestModel
    from .create_speech_request_model_one import CreateSpeechRequestModelOne
    from .create_speech_request_response_format import CreateSpeechRequestResponseFormat
    from .create_speech_request_voice import CreateSpeechRequestVoice
    from .create_transcription_request_model import CreateTranscriptionRequestModel
    from .create_transcription_request_model_one import CreateTranscriptionRequestModelOne
    from .create_transcription_request_response_format import CreateTranscriptionRequestResponseFormat
    from .create_transcription_request_timestamp_granularities_item import (
        CreateTranscriptionRequestTimestampGranularitiesItem,
    )
    from .create_transcription_response import CreateTranscriptionResponse
    from .create_translation_request_model import CreateTranslationRequestModel
    from .create_translation_request_model_one import CreateTranslationRequestModelOne
    from .create_translation_response import CreateTranslationResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateSpeechRequestModel": ".create_speech_request_model",
    "CreateSpeechRequestModelOne": ".create_speech_request_model_one",
    "CreateSpeechRequestResponseFormat": ".create_speech_request_response_format",
    "CreateSpeechRequestVoice": ".create_speech_request_voice",
    "CreateTranscriptionRequestModel": ".create_transcription_request_model",
    "CreateTranscriptionRequestModelOne": ".create_transcription_request_model_one",
    "CreateTranscriptionRequestResponseFormat": ".create_transcription_request_response_format",
    "CreateTranscriptionRequestTimestampGranularitiesItem": ".create_transcription_request_timestamp_granularities_item",
    "CreateTranscriptionResponse": ".create_transcription_response",
    "CreateTranslationRequestModel": ".create_translation_request_model",
    "CreateTranslationRequestModelOne": ".create_translation_request_model_one",
    "CreateTranslationResponse": ".create_translation_response",
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
    "CreateSpeechRequestModel",
    "CreateSpeechRequestModelOne",
    "CreateSpeechRequestResponseFormat",
    "CreateSpeechRequestVoice",
    "CreateTranscriptionRequestModel",
    "CreateTranscriptionRequestModelOne",
    "CreateTranscriptionRequestResponseFormat",
    "CreateTranscriptionRequestTimestampGranularitiesItem",
    "CreateTranscriptionResponse",
    "CreateTranslationRequestModel",
    "CreateTranslationRequestModelOne",
    "CreateTranslationResponse",
]
