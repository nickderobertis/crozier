

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .lesson_completion_request_answers_value_match_columns_user_pairs_item import (
    LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem,
)


class LessonCompletionRequestAnswersValue_FillBlank(UniversalBaseModel):
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


class LessonCompletionRequestAnswersValue_Listening(UniversalBaseModel):
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


class LessonCompletionRequestAnswersValue_MatchColumns(UniversalBaseModel):
    kind: typing.Literal["matchColumns"] = "matchColumns"
    mistakes: int
    user_pairs: typing_extensions.Annotated[
        typing.List[LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem],
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


class LessonCompletionRequestAnswersValue_MultipleChoice(UniversalBaseModel):
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


class LessonCompletionRequestAnswersValue_Reading(UniversalBaseModel):
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


class LessonCompletionRequestAnswersValue_SelectImage(UniversalBaseModel):
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


class LessonCompletionRequestAnswersValue_SortOrder(UniversalBaseModel):
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


class LessonCompletionRequestAnswersValue_Translation(UniversalBaseModel):
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


LessonCompletionRequestAnswersValue = typing_extensions.Annotated[
    typing.Union[
        LessonCompletionRequestAnswersValue_FillBlank,
        LessonCompletionRequestAnswersValue_Listening,
        LessonCompletionRequestAnswersValue_MatchColumns,
        LessonCompletionRequestAnswersValue_MultipleChoice,
        LessonCompletionRequestAnswersValue_Reading,
        LessonCompletionRequestAnswersValue_SelectImage,
        LessonCompletionRequestAnswersValue_SortOrder,
        LessonCompletionRequestAnswersValue_Translation,
    ],
    pydantic.Field(discriminator="kind"),
]
