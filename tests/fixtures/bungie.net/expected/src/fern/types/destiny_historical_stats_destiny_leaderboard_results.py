

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyHistoricalStatsDestinyLeaderboardResults(UniversalBaseModel):
    focus_character_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="focusCharacterId")] = (
        pydantic.Field(default=None)
    )
    """
    Indicate the character ID of the character that is the focal point of the provided leaderboards. May be null, in which case any character from the focus membership can appear in the provided leaderboards.
    """

    focus_membership_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="focusMembershipId")] = (
        pydantic.Field(default=None)
    )
    """
    Indicate the membership ID of the account that is the focal point of the provided leaderboards.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
