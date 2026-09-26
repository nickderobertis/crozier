

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .run_create import RunCreate
from .run_stream_stream_mode import RunStreamStreamMode


class RunStream(RunCreate):
    stream_mode: typing.Optional[RunStreamStreamMode] = pydantic.Field(default=None)
    """
    The stream mode(s) to use.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
