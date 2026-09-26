

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StreamingErrorResponse(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the command this response belongs to, or null if the command could not be correlated.
    """

    error: str = pydantic.Field()
    """
    Streaming protocol error code.
    """

    message: str = pydantic.Field()
    """
    Human-readable error message.
    """

    stacktrace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional stack trace for debugging.
    """

    meta: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
