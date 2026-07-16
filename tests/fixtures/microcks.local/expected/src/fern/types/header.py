

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Header(UniversalBaseModel):
    """
    Transport headers for both Requests and Responses
    """

    name: str = pydantic.Field()
    """
    Unique distinct name of this Header
    """

    values: typing.List[str] = pydantic.Field()
    """
    Values for this Header
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
