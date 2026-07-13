

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_destiny_stat import DestinyDestinyStat


class DestinyEntitiesItemsDestinyItemStatsComponent(UniversalBaseModel):
    """
    If you want the stats on an item's instanced data, get this component.
    These are stats like Attack, Defense etc... and *not* historical stats.
    Note that some stats have additional computation in-game at runtime - for instance, Magazine Size - and thus these stats might not be 100% accurate compared to what you see in-game for some stats. I know, it sucks. I hate it too.
    """

    stats: typing.Optional[typing.Dict[str, DestinyDestinyStat]] = pydantic.Field(default=None)
    """
    If the item has stats that it provides (damage, defense, etc...), it will be given here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
