

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebSocketErrorEventError(UniversalBaseModel):
    """
    The WebSocket error payload.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error type, when supplied.
    """

    code: str = pydantic.Field()
    """
    A machine-readable error code.
    """

    message: str = pydantic.Field()
    """
    A human-readable error message.
    """

    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    The request parameter associated with the error, when supplied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
