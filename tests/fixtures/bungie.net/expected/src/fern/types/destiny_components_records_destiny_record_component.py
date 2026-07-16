

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyComponentsRecordsDestinyRecordComponent(UniversalBaseModel):
    completed_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="completedCount"),
        pydantic.Field(
            alias="completedCount",
            description="If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded.",
        ),
    ] = None
    """
    If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded.
    """

    interval_objectives: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyQuestsDestinyObjectiveProgress]],
        FieldMetadata(alias="intervalObjectives"),
        pydantic.Field(alias="intervalObjectives"),
    ] = None
    intervals_redeemed_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="intervalsRedeemedCount"),
        pydantic.Field(alias="intervalsRedeemedCount"),
    ] = None
    objectives: typing.Optional[typing.List[DestinyQuestsDestinyObjectiveProgress]] = None
    reward_visibilty: typing_extensions.Annotated[
        typing.Optional[typing.List[bool]],
        FieldMetadata(alias="rewardVisibilty"),
        pydantic.Field(
            alias="rewardVisibilty",
            description="If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards.",
        ),
    ] = None
    """
    If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards.
    """

    state: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
