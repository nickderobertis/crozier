

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinyDestinyProgressionResetEntry(UniversalBaseModel):
    """
    Represents a season and the number of resets you had in that season.
     We do not necessarily - even for progressions with resets - track it over all seasons. So be careful and check the season numbers being returned.
    """

    resets: typing.Optional[int] = None
    season: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
