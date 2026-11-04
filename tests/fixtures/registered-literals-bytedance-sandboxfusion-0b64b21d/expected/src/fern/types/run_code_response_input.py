

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .command_run_result import CommandRunResult
from .run_status import RunStatus


class RunCodeResponseInput(UniversalBaseModel):
    status: RunStatus
    message: str
    compile_result: typing.Optional[CommandRunResult] = None
    run_result: typing.Optional[CommandRunResult] = None
    executor_pod_name: typing.Optional[str] = None
    files: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
