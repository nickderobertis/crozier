

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_progress_snapshot_response_snapshot_progress_snapshot_best_day_scores_item_day_of_week import (
    CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek,
)


class CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItem(UniversalBaseModel):
    correct_answers: typing_extensions.Annotated[
        int, FieldMetadata(alias="correctAnswers"), pydantic.Field(alias="correctAnswers")
    ]
    day_of_week: typing_extensions.Annotated[
        CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek,
        FieldMetadata(alias="dayOfWeek"),
        pydantic.Field(alias="dayOfWeek"),
    ]
    incorrect_answers: typing_extensions.Annotated[
        int, FieldMetadata(alias="incorrectAnswers"), pydantic.Field(alias="incorrectAnswers")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
