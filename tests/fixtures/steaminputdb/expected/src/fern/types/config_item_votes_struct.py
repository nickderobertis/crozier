

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigItemVotesStruct(UniversalBaseModel):
    down: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of downvotes
    """

    score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Average vote score
    """

    up: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of upvotes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
