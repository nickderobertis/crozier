

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .lesson_completion_request_answers_value_match_columns_user_pairs_item import (
    LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem,
)


class LessonCompletionRequestAnswersValueMatchColumns(UniversalBaseModel):
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
