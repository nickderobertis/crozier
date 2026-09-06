

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trace_scope_type import TraceScopeType


class TraceScope(UniversalBaseModel):
    """
    Process entire traces (all spans sharing the same root_span_id)
    """

    type: TraceScopeType
    idle_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Consider trace complete after this many seconds of inactivity (default: 30)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
