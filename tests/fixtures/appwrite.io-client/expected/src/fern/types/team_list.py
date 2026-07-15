

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .team import Team


class TeamList(UniversalBaseModel):
    """
    Teams List
    """

    sum: int = pydantic.Field()
    """
    Total sum of items in the list.
    """

    teams: typing.List[Team] = pydantic.Field()
    """
    List of teams.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
