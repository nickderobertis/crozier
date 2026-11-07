

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .command_run_status import CommandRunStatus


class CommandRunResult(UniversalBaseModel):
    status: CommandRunStatus
    execution_time: typing.Optional[float] = None
    return_code: typing.Optional[int] = None
    stdout: typing.Optional[str] = None
    stderr: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
