

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_level import MessageLevel


class Message(UniversalBaseModel):
    """
    Individual (info/warning/error) message in a response.
    """

    code: typing.Optional[str] = None
    message: str
    level: typing.Optional[MessageLevel] = None
    args: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
