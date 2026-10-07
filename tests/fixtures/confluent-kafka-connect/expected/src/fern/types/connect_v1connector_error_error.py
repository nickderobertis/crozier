

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectV1ConnectorErrorError(UniversalBaseModel):
    """
    Connector Error with error code and message.
    """

    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    Error code for the type of error
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human readable error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
