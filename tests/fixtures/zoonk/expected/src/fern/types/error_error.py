

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorError(UniversalBaseModel):
    code: str = pydantic.Field()
    """
    Stable machine-readable error code. Clients must preserve unknown codes for forward compatibility.
    """

    details: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Additional error details
    """

    message: str = pydantic.Field()
    """
    Error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
