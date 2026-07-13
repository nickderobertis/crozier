

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_stat import DestinyDestinyStat


class DestinyDestinyTalentNodeStatBlock(UniversalBaseModel):
    """
    This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.
    """

    current_step_stats: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyStat]], FieldMetadata(alias="currentStepStats")
    ] = pydantic.Field(default=None)
    """
    The stat benefits conferred when this talent node is activated for the current Step that is active on the node.
    """

    next_step_stats: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyStat]], FieldMetadata(alias="nextStepStats")
    ] = pydantic.Field(default=None)
    """
    This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring multiple steps worth of benefits: you would use this property to show what activating the "next" step on the node would provide vs. what the current step is providing. While Nodes are currently not being used this way, the underlying system for this functionality still exists. I hesitate to remove this property while the ability for designers to make such a talent grid still exists. Whether you want to show it is up to you.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
