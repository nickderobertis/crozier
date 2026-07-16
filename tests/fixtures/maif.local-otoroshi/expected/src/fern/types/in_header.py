

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InHeader(UniversalBaseModel):
    """
    JWT location in a header
    """

    name: str = pydantic.Field()
    """
    Name of the header
    """

    remove: str = pydantic.Field()
    """
    Remove regex inside the value, like 'Bearer '
    """

    type: str = pydantic.Field()
    """
    String with value InHeader
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
