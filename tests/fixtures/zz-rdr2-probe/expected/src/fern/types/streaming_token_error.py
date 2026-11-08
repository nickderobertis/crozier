

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StreamingTokenError(UniversalBaseModel):
    error: str = pydantic.Field()
    """
    Error message describing what went wrong
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error code for programmatic handling
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional error details if available
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
