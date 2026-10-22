

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Address(UniversalBaseModel):
    email: str = pydantic.Field()
    """
    Valid email address from a domain defined in your account with valid DNS records
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name for the sender
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
