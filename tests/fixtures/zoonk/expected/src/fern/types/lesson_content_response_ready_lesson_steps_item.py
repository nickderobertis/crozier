

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_content_response_ready_lesson_steps_item_fill_blank_options_item import (
    LessonContentResponseReadyLessonStepsItemFillBlankOptionsItem,
)
from .lesson_content_response_ready_lesson_steps_item_sentence import LessonContentResponseReadyLessonStepsItemSentence
from .lesson_content_response_ready_lesson_steps_item_sentence_word_options_item import (
    LessonContentResponseReadyLessonStepsItemSentenceWordOptionsItem,
)
from .lesson_content_response_ready_lesson_steps_item_translation_options_item import (
    LessonContentResponseReadyLessonStepsItemTranslationOptionsItem,
)
from .lesson_content_response_ready_lesson_steps_item_vocabulary_options_item import (
    LessonContentResponseReadyLessonStepsItemVocabularyOptionsItem,
)
from .lesson_content_response_ready_lesson_steps_item_word import LessonContentResponseReadyLessonStepsItemWord
from .lesson_content_response_ready_lesson_steps_item_word_bank_options_item import (
    LessonContentResponseReadyLessonStepsItemWordBankOptionsItem,
)


class LessonContentResponseReadyLessonStepsItem(UniversalBaseModel):
    fill_blank_options: typing_extensions.Annotated[
        typing.List[LessonContentResponseReadyLessonStepsItemFillBlankOptionsItem],
        FieldMetadata(alias="fillBlankOptions"),
        pydantic.Field(alias="fillBlankOptions"),
    ]
    id: str
    match_columns_right_items: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="matchColumnsRightItems"), pydantic.Field(alias="matchColumnsRightItems")
    ]
    position: int
    sentence: typing.Optional[LessonContentResponseReadyLessonStepsItemSentence] = None
    sentence_word_options: typing_extensions.Annotated[
        typing.List[LessonContentResponseReadyLessonStepsItemSentenceWordOptionsItem],
        FieldMetadata(alias="sentenceWordOptions"),
        pydantic.Field(alias="sentenceWordOptions"),
    ]
    sort_order_items: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="sortOrderItems"), pydantic.Field(alias="sortOrderItems")
    ]
    translation_options: typing_extensions.Annotated[
        typing.List[LessonContentResponseReadyLessonStepsItemTranslationOptionsItem],
        FieldMetadata(alias="translationOptions"),
        pydantic.Field(alias="translationOptions"),
    ]
    vocabulary_options: typing_extensions.Annotated[
        typing.List[LessonContentResponseReadyLessonStepsItemVocabularyOptionsItem],
        FieldMetadata(alias="vocabularyOptions"),
        pydantic.Field(alias="vocabularyOptions"),
    ]
    word: typing.Optional[LessonContentResponseReadyLessonStepsItemWord] = None
    word_bank_options: typing_extensions.Annotated[
        typing.List[LessonContentResponseReadyLessonStepsItemWordBankOptionsItem],
        FieldMetadata(alias="wordBankOptions"),
        pydantic.Field(alias="wordBankOptions"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
