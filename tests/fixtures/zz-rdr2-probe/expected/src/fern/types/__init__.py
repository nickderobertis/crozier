



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .audio_chunk import AudioChunk
    from .custom_formatting_request_body import CustomFormattingRequestBody
    from .custom_formatting_request_body_custom_formatting import CustomFormattingRequestBodyCustomFormatting
    from .custom_formatting_response import CustomFormattingResponse
    from .custom_formatting_response_custom_formatting import CustomFormattingResponseCustomFormatting
    from .error import Error
    from .error_status import ErrorStatus
    from .force_endpoint_payload import ForceEndpointPayload
    from .lemur_task_params import LemurTaskParams
    from .receive_payload import ReceivePayload
    from .session_begins_payload import SessionBeginsPayload
    from .session_termination_payload import SessionTerminationPayload
    from .speaker_identification_request_body import SpeakerIdentificationRequestBody
    from .speaker_identification_request_body_speaker_identification import (
        SpeakerIdentificationRequestBodySpeakerIdentification,
    )
    from .speaker_identification_request_body_speaker_identification_speaker_type import (
        SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType,
    )
    from .speaker_identification_response import SpeakerIdentificationResponse
    from .speaker_identification_response_speaker_identification import (
        SpeakerIdentificationResponseSpeakerIdentification,
    )
    from .streaming_token_error import StreamingTokenError
    from .termination_payload import TerminationPayload
    from .translation_request_body import TranslationRequestBody
    from .translation_request_body_translation import TranslationRequestBodyTranslation
    from .translation_response import TranslationResponse
    from .translation_response_translation import TranslationResponseTranslation
    from .turn_payload import TurnPayload
    from .update_configuration_payload import UpdateConfigurationPayload
    from .word import Word
_dynamic_imports: typing.Dict[str, str] = {
    "AudioChunk": ".audio_chunk",
    "CustomFormattingRequestBody": ".custom_formatting_request_body",
    "CustomFormattingRequestBodyCustomFormatting": ".custom_formatting_request_body_custom_formatting",
    "CustomFormattingResponse": ".custom_formatting_response",
    "CustomFormattingResponseCustomFormatting": ".custom_formatting_response_custom_formatting",
    "Error": ".error",
    "ErrorStatus": ".error_status",
    "ForceEndpointPayload": ".force_endpoint_payload",
    "LemurTaskParams": ".lemur_task_params",
    "ReceivePayload": ".receive_payload",
    "SessionBeginsPayload": ".session_begins_payload",
    "SessionTerminationPayload": ".session_termination_payload",
    "SpeakerIdentificationRequestBody": ".speaker_identification_request_body",
    "SpeakerIdentificationRequestBodySpeakerIdentification": ".speaker_identification_request_body_speaker_identification",
    "SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType": ".speaker_identification_request_body_speaker_identification_speaker_type",
    "SpeakerIdentificationResponse": ".speaker_identification_response",
    "SpeakerIdentificationResponseSpeakerIdentification": ".speaker_identification_response_speaker_identification",
    "StreamingTokenError": ".streaming_token_error",
    "TerminationPayload": ".termination_payload",
    "TranslationRequestBody": ".translation_request_body",
    "TranslationRequestBodyTranslation": ".translation_request_body_translation",
    "TranslationResponse": ".translation_response",
    "TranslationResponseTranslation": ".translation_response_translation",
    "TurnPayload": ".turn_payload",
    "UpdateConfigurationPayload": ".update_configuration_payload",
    "Word": ".word",
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
    "AudioChunk",
    "CustomFormattingRequestBody",
    "CustomFormattingRequestBodyCustomFormatting",
    "CustomFormattingResponse",
    "CustomFormattingResponseCustomFormatting",
    "Error",
    "ErrorStatus",
    "ForceEndpointPayload",
    "LemurTaskParams",
    "ReceivePayload",
    "SessionBeginsPayload",
    "SessionTerminationPayload",
    "SpeakerIdentificationRequestBody",
    "SpeakerIdentificationRequestBodySpeakerIdentification",
    "SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType",
    "SpeakerIdentificationResponse",
    "SpeakerIdentificationResponseSpeakerIdentification",
    "StreamingTokenError",
    "TerminationPayload",
    "TranslationRequestBody",
    "TranslationRequestBodyTranslation",
    "TranslationResponse",
    "TranslationResponseTranslation",
    "TurnPayload",
    "UpdateConfigurationPayload",
    "Word",
]
