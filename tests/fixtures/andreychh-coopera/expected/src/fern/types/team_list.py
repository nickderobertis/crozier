

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .team import Team


class TeamList(UniversalBaseModel):
    """
    Teams wrapped in an object rather than handed over as a bare array. A list eventually needs things said about it — where the next page starts, how many there are in all — and a bare array leaves nowhere to say them without changing the shape of every answer that came before.
    """

    items: typing.List[Team]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
