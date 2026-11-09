



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .audio_intelligence_model_status import AudioIntelligenceModelStatus
    from .auto_highlight_result import AutoHighlightResult
    from .auto_highlights_result import AutoHighlightsResult
    from .chapter import Chapter
    from .content_safety_label import ContentSafetyLabel
    from .content_safety_label_result import ContentSafetyLabelResult
    from .content_safety_labels_result import ContentSafetyLabelsResult
    from .entity import Entity
    from .entity_type import EntityType
    from .page_details import PageDetails
    from .paragraphs_response import ParagraphsResponse
    from .pii_policy import PiiPolicy
    from .redact_pii_audio_quality import RedactPiiAudioQuality
    from .redacted_audio_notification import RedactedAudioNotification
    from .redacted_audio_response import RedactedAudioResponse
    from .redacted_audio_status import RedactedAudioStatus
    from .sentences_response import SentencesResponse
    from .sentiment import Sentiment
    from .sentiment_analysis_result import SentimentAnalysisResult
    from .severity_score_summary import SeverityScoreSummary
    from .speech_model import SpeechModel
    from .substitution_policy import SubstitutionPolicy
    from .subtitle_format import SubtitleFormat
    from .summary_model import SummaryModel
    from .summary_type import SummaryType
    from .timestamp import Timestamp
    from .topic_detection_model_result import TopicDetectionModelResult
    from .topic_detection_result import TopicDetectionResult
    from .topic_detection_result_labels_item import TopicDetectionResultLabelsItem
    from .transcript import Transcript
    from .transcript_custom_spelling import TranscriptCustomSpelling
    from .transcript_language_code import TranscriptLanguageCode
    from .transcript_language_detection_options import TranscriptLanguageDetectionOptions
    from .transcript_language_detection_options_on_no_speech_detected import (
        TranscriptLanguageDetectionOptionsOnNoSpeechDetected,
    )
    from .transcript_list import TranscriptList
    from .transcript_list_item import TranscriptListItem
    from .transcript_metadata import TranscriptMetadata
    from .transcript_metadata_warnings_item import TranscriptMetadataWarningsItem
    from .transcript_optional_params import TranscriptOptionalParams
    from .transcript_optional_params_domain import TranscriptOptionalParamsDomain
    from .transcript_optional_params_language_code import TranscriptOptionalParamsLanguageCode
    from .transcript_optional_params_language_detection_options import TranscriptOptionalParamsLanguageDetectionOptions
    from .transcript_optional_params_language_detection_options_on_no_speech_detected import (
        TranscriptOptionalParamsLanguageDetectionOptionsOnNoSpeechDetected,
    )
    from .transcript_optional_params_redact_pii_audio_options import TranscriptOptionalParamsRedactPiiAudioOptions
    from .transcript_optional_params_redact_pii_audio_options_override_audio_redaction_method import (
        TranscriptOptionalParamsRedactPiiAudioOptionsOverrideAudioRedactionMethod,
    )
    from .transcript_optional_params_remove_audio_tags import TranscriptOptionalParamsRemoveAudioTags
    from .transcript_optional_params_speaker_options import TranscriptOptionalParamsSpeakerOptions
    from .transcript_optional_params_speech_understanding import TranscriptOptionalParamsSpeechUnderstanding
    from .transcript_optional_params_speech_understanding_request import (
        TranscriptOptionalParamsSpeechUnderstandingRequest,
    )
    from .transcript_paragraph import TranscriptParagraph
    from .transcript_ready_notification import TranscriptReadyNotification
    from .transcript_ready_status import TranscriptReadyStatus
    from .transcript_redact_pii_audio_options import TranscriptRedactPiiAudioOptions
    from .transcript_redact_pii_audio_options_override_audio_redaction_method import (
        TranscriptRedactPiiAudioOptionsOverrideAudioRedactionMethod,
    )
    from .transcript_remove_audio_tags import TranscriptRemoveAudioTags
    from .transcript_sentence import TranscriptSentence
    from .transcript_speech_understanding import TranscriptSpeechUnderstanding
    from .transcript_speech_understanding_request import TranscriptSpeechUnderstandingRequest
    from .transcript_speech_understanding_response import TranscriptSpeechUnderstandingResponse
    from .transcript_status import TranscriptStatus
    from .transcript_translated_texts import TranscriptTranslatedTexts
    from .transcript_utterance import TranscriptUtterance
    from .transcript_word import TranscriptWord
    from .word_search_match import WordSearchMatch
    from .word_search_response import WordSearchResponse
    from .word_search_timestamp import WordSearchTimestamp
_dynamic_imports: typing.Dict[str, str] = {
    "AudioIntelligenceModelStatus": ".audio_intelligence_model_status",
    "AutoHighlightResult": ".auto_highlight_result",
    "AutoHighlightsResult": ".auto_highlights_result",
    "Chapter": ".chapter",
    "ContentSafetyLabel": ".content_safety_label",
    "ContentSafetyLabelResult": ".content_safety_label_result",
    "ContentSafetyLabelsResult": ".content_safety_labels_result",
    "Entity": ".entity",
    "EntityType": ".entity_type",
    "PageDetails": ".page_details",
    "ParagraphsResponse": ".paragraphs_response",
    "PiiPolicy": ".pii_policy",
    "RedactPiiAudioQuality": ".redact_pii_audio_quality",
    "RedactedAudioNotification": ".redacted_audio_notification",
    "RedactedAudioResponse": ".redacted_audio_response",
    "RedactedAudioStatus": ".redacted_audio_status",
    "SentencesResponse": ".sentences_response",
    "Sentiment": ".sentiment",
    "SentimentAnalysisResult": ".sentiment_analysis_result",
    "SeverityScoreSummary": ".severity_score_summary",
    "SpeechModel": ".speech_model",
    "SubstitutionPolicy": ".substitution_policy",
    "SubtitleFormat": ".subtitle_format",
    "SummaryModel": ".summary_model",
    "SummaryType": ".summary_type",
    "Timestamp": ".timestamp",
    "TopicDetectionModelResult": ".topic_detection_model_result",
    "TopicDetectionResult": ".topic_detection_result",
    "TopicDetectionResultLabelsItem": ".topic_detection_result_labels_item",
    "Transcript": ".transcript",
    "TranscriptCustomSpelling": ".transcript_custom_spelling",
    "TranscriptLanguageCode": ".transcript_language_code",
    "TranscriptLanguageDetectionOptions": ".transcript_language_detection_options",
    "TranscriptLanguageDetectionOptionsOnNoSpeechDetected": ".transcript_language_detection_options_on_no_speech_detected",
    "TranscriptList": ".transcript_list",
    "TranscriptListItem": ".transcript_list_item",
    "TranscriptMetadata": ".transcript_metadata",
    "TranscriptMetadataWarningsItem": ".transcript_metadata_warnings_item",
    "TranscriptOptionalParams": ".transcript_optional_params",
    "TranscriptOptionalParamsDomain": ".transcript_optional_params_domain",
    "TranscriptOptionalParamsLanguageCode": ".transcript_optional_params_language_code",
    "TranscriptOptionalParamsLanguageDetectionOptions": ".transcript_optional_params_language_detection_options",
    "TranscriptOptionalParamsLanguageDetectionOptionsOnNoSpeechDetected": ".transcript_optional_params_language_detection_options_on_no_speech_detected",
    "TranscriptOptionalParamsRedactPiiAudioOptions": ".transcript_optional_params_redact_pii_audio_options",
    "TranscriptOptionalParamsRedactPiiAudioOptionsOverrideAudioRedactionMethod": ".transcript_optional_params_redact_pii_audio_options_override_audio_redaction_method",
    "TranscriptOptionalParamsRemoveAudioTags": ".transcript_optional_params_remove_audio_tags",
    "TranscriptOptionalParamsSpeakerOptions": ".transcript_optional_params_speaker_options",
    "TranscriptOptionalParamsSpeechUnderstanding": ".transcript_optional_params_speech_understanding",
    "TranscriptOptionalParamsSpeechUnderstandingRequest": ".transcript_optional_params_speech_understanding_request",
    "TranscriptParagraph": ".transcript_paragraph",
    "TranscriptReadyNotification": ".transcript_ready_notification",
    "TranscriptReadyStatus": ".transcript_ready_status",
    "TranscriptRedactPiiAudioOptions": ".transcript_redact_pii_audio_options",
    "TranscriptRedactPiiAudioOptionsOverrideAudioRedactionMethod": ".transcript_redact_pii_audio_options_override_audio_redaction_method",
    "TranscriptRemoveAudioTags": ".transcript_remove_audio_tags",
    "TranscriptSentence": ".transcript_sentence",
    "TranscriptSpeechUnderstanding": ".transcript_speech_understanding",
    "TranscriptSpeechUnderstandingRequest": ".transcript_speech_understanding_request",
    "TranscriptSpeechUnderstandingResponse": ".transcript_speech_understanding_response",
    "TranscriptStatus": ".transcript_status",
    "TranscriptTranslatedTexts": ".transcript_translated_texts",
    "TranscriptUtterance": ".transcript_utterance",
    "TranscriptWord": ".transcript_word",
    "WordSearchMatch": ".word_search_match",
    "WordSearchResponse": ".word_search_response",
    "WordSearchTimestamp": ".word_search_timestamp",
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
    "AudioIntelligenceModelStatus",
    "AutoHighlightResult",
    "AutoHighlightsResult",
    "Chapter",
    "ContentSafetyLabel",
    "ContentSafetyLabelResult",
    "ContentSafetyLabelsResult",
    "Entity",
    "EntityType",
    "PageDetails",
    "ParagraphsResponse",
    "PiiPolicy",
    "RedactPiiAudioQuality",
    "RedactedAudioNotification",
    "RedactedAudioResponse",
    "RedactedAudioStatus",
    "SentencesResponse",
    "Sentiment",
    "SentimentAnalysisResult",
    "SeverityScoreSummary",
    "SpeechModel",
    "SubstitutionPolicy",
    "SubtitleFormat",
    "SummaryModel",
    "SummaryType",
    "Timestamp",
    "TopicDetectionModelResult",
    "TopicDetectionResult",
    "TopicDetectionResultLabelsItem",
    "Transcript",
    "TranscriptCustomSpelling",
    "TranscriptLanguageCode",
    "TranscriptLanguageDetectionOptions",
    "TranscriptLanguageDetectionOptionsOnNoSpeechDetected",
    "TranscriptList",
    "TranscriptListItem",
    "TranscriptMetadata",
    "TranscriptMetadataWarningsItem",
    "TranscriptOptionalParams",
    "TranscriptOptionalParamsDomain",
    "TranscriptOptionalParamsLanguageCode",
    "TranscriptOptionalParamsLanguageDetectionOptions",
    "TranscriptOptionalParamsLanguageDetectionOptionsOnNoSpeechDetected",
    "TranscriptOptionalParamsRedactPiiAudioOptions",
    "TranscriptOptionalParamsRedactPiiAudioOptionsOverrideAudioRedactionMethod",
    "TranscriptOptionalParamsRemoveAudioTags",
    "TranscriptOptionalParamsSpeakerOptions",
    "TranscriptOptionalParamsSpeechUnderstanding",
    "TranscriptOptionalParamsSpeechUnderstandingRequest",
    "TranscriptParagraph",
    "TranscriptReadyNotification",
    "TranscriptReadyStatus",
    "TranscriptRedactPiiAudioOptions",
    "TranscriptRedactPiiAudioOptionsOverrideAudioRedactionMethod",
    "TranscriptRemoveAudioTags",
    "TranscriptSentence",
    "TranscriptSpeechUnderstanding",
    "TranscriptSpeechUnderstandingRequest",
    "TranscriptSpeechUnderstandingResponse",
    "TranscriptStatus",
    "TranscriptTranslatedTexts",
    "TranscriptUtterance",
    "TranscriptWord",
    "WordSearchMatch",
    "WordSearchResponse",
    "WordSearchTimestamp",
]
