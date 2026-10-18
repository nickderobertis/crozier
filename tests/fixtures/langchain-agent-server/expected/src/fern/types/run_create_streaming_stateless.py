

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .run_create_stateless import RunCreateStateless
from .run_create_streaming_stateless_on_disconnect import RunCreateStreamingStatelessOnDisconnect


class RunCreateStreamingStateless(RunCreateStateless):
    on_disconnect: typing.Optional[RunCreateStreamingStatelessOnDisconnect] = pydantic.Field(default=None)
    """
    The disconnect mode to use. Must be one of 'cancel' or 'continue'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
