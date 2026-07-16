

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyEntitiesItemsDestinyItemObjectivesComponent(UniversalBaseModel):
    """
    Items can have objectives and progression. When you request this block, you will obtain information about any Objectives and progression tied to this item.
    """

    date_completed: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dateCompleted"),
        pydantic.Field(
            alias="dateCompleted",
            description="If we have any information on when these objectives were completed, this will be the date of that completion. This won't be on many items, but could be interesting for some items that do store this information.",
        ),
    ] = None
    """
    If we have any information on when these objectives were completed, this will be the date of that completion. This won't be on many items, but could be interesting for some items that do store this information.
    """

    flavor_objective: typing_extensions.Annotated[
        typing.Optional[DestinyQuestsDestinyObjectiveProgress],
        FieldMetadata(alias="flavorObjective"),
        pydantic.Field(
            alias="flavorObjective",
            description='I may regret naming it this way - but this represents when an item has an objective that doesn\'t serve a beneficial purpose, but rather is used for "flavor" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.',
        ),
    ] = None
    """
    I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for "flavor" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.
    """

    objectives: typing.Optional[typing.List[DestinyQuestsDestinyObjectiveProgress]] = pydantic.Field(default=None)
    """
    If the item has a hard association with objectives, your progress on them will be defined here. 
    Objectives are our standard way to describe a series of tasks that have to be completed for a reward.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
