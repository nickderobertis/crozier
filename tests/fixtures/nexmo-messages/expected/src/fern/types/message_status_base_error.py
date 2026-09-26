

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageStatusBaseError(UniversalBaseModel):
    """
    If the message encountered a problem a descriptive error will be supplied in this object.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Text describing the error. See [our errors list](https://developer.nexmo.com/api-errors/messages-olympus) for a list of possible errors
    """

    instance: typing.Optional[str] = pydantic.Field(default=None)
    """
    The record id of this error's occurrence.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error code encountered when sending the message. See [our errors list](https://developer.nexmo.com/api-errors/messages-olympus) for a list of possible errors
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of error encountered, follow URL for more details
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
