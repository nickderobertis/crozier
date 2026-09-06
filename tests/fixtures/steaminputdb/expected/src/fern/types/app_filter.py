

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AppFilter(UniversalBaseModel):
    include_demos: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include demos in the search results
    """

    include_games: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include games in the search results
    """

    include_mods: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include mods in the search results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
