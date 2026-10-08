

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .http_request import HttpRequest
from .set_breakpoints_command_type import SetBreakpointsCommandType


class SetBreakpointsCommand(UniversalBaseModel):
    """
    Set the live debugger's breakpoints (session-scoped, not persisted).

        Replaces the full breakpoint set: the frontend always sends the complete
        map of cell id -> 1-based line numbers. Only meaningful when the
        `debugger` experimental feature is enabled.

        Attributes:
            breakpoints: Map of cell id to lines that have a breakpoint.
            request: HTTP request context if available.
    """

    breakpoints: typing.Dict[str, typing.List[int]]
    request: typing.Optional[HttpRequest] = None
    type: SetBreakpointsCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
