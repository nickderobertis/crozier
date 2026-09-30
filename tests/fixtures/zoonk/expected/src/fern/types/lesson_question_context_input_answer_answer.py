

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_question_context_input_answer_answer_match_columns_user_pairs_item import (
    LessonQuestionContextInputAnswerAnswerMatchColumnsUserPairsItem,
)


class LessonQuestionContextInputAnswerAnswer_FillBlank(UniversalBaseModel):
    kind: typing.Literal["fillBlank"] = "fillBlank"
    user_answers: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="userAnswers"), pydantic.Field(alias="userAnswers")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInputAnswerAnswer_Listening(UniversalBaseModel):
    kind: typing.Literal["listening"] = "listening"
    arranged_words: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="arrangedWords"), pydantic.Field(alias="arrangedWords")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInputAnswerAnswer_MatchColumns(UniversalBaseModel):
    kind: typing.Literal["matchColumns"] = "matchColumns"
    mistakes: int
    user_pairs: typing_extensions.Annotated[
        typing.List[LessonQuestionContextInputAnswerAnswerMatchColumnsUserPairsItem],
        FieldMetadata(alias="userPairs"),
        pydantic.Field(alias="userPairs"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInputAnswerAnswer_MultipleChoice(UniversalBaseModel):
    kind: typing.Literal["multipleChoice"] = "multipleChoice"
    selected_option_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="selectedOptionId"), pydantic.Field(alias="selectedOptionId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInputAnswerAnswer_Reading(UniversalBaseModel):
    kind: typing.Literal["reading"] = "reading"
    arranged_words: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="arrangedWords"), pydantic.Field(alias="arrangedWords")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInputAnswerAnswer_SelectImage(UniversalBaseModel):
    kind: typing.Literal["selectImage"] = "selectImage"
    selected_option_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="selectedOptionId"), pydantic.Field(alias="selectedOptionId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInputAnswerAnswer_SortOrder(UniversalBaseModel):
    kind: typing.Literal["sortOrder"] = "sortOrder"
    user_order: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="userOrder"), pydantic.Field(alias="userOrder")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInputAnswerAnswer_Translation(UniversalBaseModel):
    kind: typing.Literal["translation"] = "translation"
    selected_option_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="selectedOptionId"), pydantic.Field(alias="selectedOptionId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LessonQuestionContextInputAnswerAnswer = typing_extensions.Annotated[
    typing.Union[
        LessonQuestionContextInputAnswerAnswer_FillBlank,
        LessonQuestionContextInputAnswerAnswer_Listening,
        LessonQuestionContextInputAnswerAnswer_MatchColumns,
        LessonQuestionContextInputAnswerAnswer_MultipleChoice,
        LessonQuestionContextInputAnswerAnswer_Reading,
        LessonQuestionContextInputAnswerAnswer_SelectImage,
        LessonQuestionContextInputAnswerAnswer_SortOrder,
        LessonQuestionContextInputAnswerAnswer_Translation,
    ],
    pydantic.Field(discriminator="kind"),
]
