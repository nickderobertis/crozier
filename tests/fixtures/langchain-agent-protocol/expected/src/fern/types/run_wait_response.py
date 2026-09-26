

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message import Message
from .run import Run


class RunWaitResponse(UniversalBaseModel):
    run: typing.Optional[Run] = pydantic.Field(default=None)
    """
    The run information.
    """

    values: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The values returned by the run.
    """

    messages: typing.Optional[typing.List[Message]] = pydantic.Field(default=None)
    """
    The messages returned by the run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
