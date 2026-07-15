

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageError(UniversalBaseModel):
    """
    The error returned if your message status is failed or undelivered.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error_code provides more information about the failure. If the message was successful, this value is null
    """

    message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
