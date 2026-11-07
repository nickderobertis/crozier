



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ask_transcript_question_response import AskTranscriptQuestionResponse
    from .ask_transcript_question_response_item import AskTranscriptQuestionResponseItem
    from .create_transcript_response import CreateTranscriptResponse
    from .create_transcript_response_item import CreateTranscriptResponseItem
    from .create_transcript_response_item_status import CreateTranscriptResponseItemStatus
    from .get_transcript_question_response import GetTranscriptQuestionResponse
    from .get_transcript_question_response_item import GetTranscriptQuestionResponseItem
    from .get_transcript_response import GetTranscriptResponse
    from .get_transcript_response_item import GetTranscriptResponseItem
    from .get_transcript_response_item_status import GetTranscriptResponseItemStatus
    from .get_transcript_response_item_words_item import GetTranscriptResponseItemWordsItem
    from .list_transcript_questions_response import ListTranscriptQuestionsResponse
    from .list_transcript_questions_response_items_item import ListTranscriptQuestionsResponseItemsItem
    from .list_transcripts_response import ListTranscriptsResponse
    from .list_transcripts_response_items_item import ListTranscriptsResponseItemsItem
    from .list_transcripts_response_meta import ListTranscriptsResponseMeta
_dynamic_imports: typing.Dict[str, str] = {
    "AskTranscriptQuestionResponse": ".ask_transcript_question_response",
    "AskTranscriptQuestionResponseItem": ".ask_transcript_question_response_item",
    "CreateTranscriptResponse": ".create_transcript_response",
    "CreateTranscriptResponseItem": ".create_transcript_response_item",
    "CreateTranscriptResponseItemStatus": ".create_transcript_response_item_status",
    "GetTranscriptQuestionResponse": ".get_transcript_question_response",
    "GetTranscriptQuestionResponseItem": ".get_transcript_question_response_item",
    "GetTranscriptResponse": ".get_transcript_response",
    "GetTranscriptResponseItem": ".get_transcript_response_item",
    "GetTranscriptResponseItemStatus": ".get_transcript_response_item_status",
    "GetTranscriptResponseItemWordsItem": ".get_transcript_response_item_words_item",
    "ListTranscriptQuestionsResponse": ".list_transcript_questions_response",
    "ListTranscriptQuestionsResponseItemsItem": ".list_transcript_questions_response_items_item",
    "ListTranscriptsResponse": ".list_transcripts_response",
    "ListTranscriptsResponseItemsItem": ".list_transcripts_response_items_item",
    "ListTranscriptsResponseMeta": ".list_transcripts_response_meta",
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
    "AskTranscriptQuestionResponse",
    "AskTranscriptQuestionResponseItem",
    "CreateTranscriptResponse",
    "CreateTranscriptResponseItem",
    "CreateTranscriptResponseItemStatus",
    "GetTranscriptQuestionResponse",
    "GetTranscriptQuestionResponseItem",
    "GetTranscriptResponse",
    "GetTranscriptResponseItem",
    "GetTranscriptResponseItemStatus",
    "GetTranscriptResponseItemWordsItem",
    "ListTranscriptQuestionsResponse",
    "ListTranscriptQuestionsResponseItemsItem",
    "ListTranscriptsResponse",
    "ListTranscriptsResponseItemsItem",
    "ListTranscriptsResponseMeta",
]
