

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Claims(UniversalBaseModel):
    """
    Claim in JWT format, self- or issuer-signed.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    scope: str = pydantic.Field()
    """
    claim scope
    """

    sub: str = pydantic.Field()
    """
    UUID
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
