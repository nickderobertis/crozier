

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_perks_destiny_perk_reference import DestinyPerksDestinyPerkReference


class DestinyEntitiesItemsDestinyItemPerksComponent(UniversalBaseModel):
    """
    Instanced items can have perks: benefits that the item bestows.
    These are related to DestinySandboxPerkDefinition, and sometimes - but not always - have human readable info. When they do, they are the icons and text that you see in an item's tooltip.
    Talent Grids, Sockets, and the item itself can apply Perks, which are then summarized here for your convenience.
    """

    perks: typing.Optional[typing.List[DestinyPerksDestinyPerkReference]] = pydantic.Field(default=None)
    """
    The list of perks to display in an item tooltip - and whether or not they have been activated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
