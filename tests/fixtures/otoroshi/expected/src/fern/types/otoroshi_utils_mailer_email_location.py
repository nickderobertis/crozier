

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OtoroshiUtilsMailerEmailLocation(UniversalBaseModel):
    """
    Email location settings
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Destination name
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
