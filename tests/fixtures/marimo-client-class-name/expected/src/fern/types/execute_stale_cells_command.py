

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .execute_stale_cells_command_type import ExecuteStaleCellsCommandType
from .http_request import HttpRequest


class ExecuteStaleCellsCommand(UniversalBaseModel):
    """
    Execute all stale cells.

        Cells become stale when their dependencies change but haven't been
        re-executed yet. Brings the notebook to a consistent state.

        Attributes:
            request: HTTP request context if available.
    """

    request: typing.Optional[HttpRequest] = None
    type: ExecuteStaleCellsCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
