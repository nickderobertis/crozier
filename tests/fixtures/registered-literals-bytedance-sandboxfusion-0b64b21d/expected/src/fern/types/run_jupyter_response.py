

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_run_result import CellRunResult
from .command_run_result import CommandRunResult
from .run_status import RunStatus


class RunJupyterResponse(UniversalBaseModel):
    status: RunStatus
    message: str
    driver: typing.Optional[CommandRunResult] = None
    cells: typing.Optional[typing.List[CellRunResult]] = None
    executor_pod_name: typing.Optional[str] = None
    files: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
