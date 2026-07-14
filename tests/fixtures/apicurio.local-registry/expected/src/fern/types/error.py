

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    """
    All error responses, whether `4xx` or `5xx` will include one of these as the response
    body.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full details about the error.  This might contain a server stack trace, for example.
    """

    error_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    The server-side error code.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The short error message.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error name - typically the classname of the exception thrown by the server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
