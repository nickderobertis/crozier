

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorStreamingEventError(UniversalBaseModel):
    """
    The error payload that was emitted.
    """

    type: str = pydantic.Field()
    """
    The error type that was emitted.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error code that was emitted, if any.
    """

    message: str = pydantic.Field()
    """
    The human-readable error message that was emitted.
    """

    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    The parameter name that was associated with the error, if any.
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The response headers that were emitted with the error, if any.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
