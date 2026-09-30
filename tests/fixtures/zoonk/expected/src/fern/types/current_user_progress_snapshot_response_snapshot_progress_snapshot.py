

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_progress_snapshot_response_snapshot_progress_snapshot_best_day_scores_item import (
    CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItem,
)


class CurrentUserProgressSnapshotResponseSnapshotProgressSnapshot(UniversalBaseModel):
    best_day_scores: typing_extensions.Annotated[
        typing.Optional[typing.List[CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItem]],
        FieldMetadata(alias="bestDayScores"),
        pydantic.Field(alias="bestDayScores"),
    ] = None
    current_energy: typing_extensions.Annotated[
        float, FieldMetadata(alias="currentEnergy"), pydantic.Field(alias="currentEnergy")
    ]
    full_energy_days: typing_extensions.Annotated[
        int, FieldMetadata(alias="fullEnergyDays"), pydantic.Field(alias="fullEnergyDays")
    ]
    highest_previous_daily_brain_power: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="highestPreviousDailyBrainPower"),
        pydantic.Field(alias="highestPreviousDailyBrainPower"),
    ]
    learning_days: typing_extensions.Annotated[
        int, FieldMetadata(alias="learningDays"), pydantic.Field(alias="learningDays")
    ]
    today_brain_power: typing_extensions.Annotated[
        int, FieldMetadata(alias="todayBrainPower"), pydantic.Field(alias="todayBrainPower")
    ]
    today_completed_lessons: typing_extensions.Annotated[
        int, FieldMetadata(alias="todayCompletedLessons"), pydantic.Field(alias="todayCompletedLessons")
    ]
    today_energy_at_end: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="todayEnergyAtEnd"), pydantic.Field(alias="todayEnergyAtEnd")
    ] = None
    today_interactive_lessons: typing_extensions.Annotated[
        int, FieldMetadata(alias="todayInteractiveLessons"), pydantic.Field(alias="todayInteractiveLessons")
    ]
    total_learning_seconds: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalLearningSeconds"), pydantic.Field(alias="totalLearningSeconds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
