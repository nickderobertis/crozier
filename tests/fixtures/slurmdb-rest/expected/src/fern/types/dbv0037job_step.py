

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dbv0037job_exit_code import Dbv0037JobExitCode
from .dbv0037job_step_cpu import Dbv0037JobStepCpu
from .dbv0037job_step_nodes import Dbv0037JobStepNodes
from .dbv0037job_step_statistics import Dbv0037JobStepStatistics
from .dbv0037job_step_step import Dbv0037JobStepStep
from .dbv0037job_step_tasks import Dbv0037JobStepTasks
from .dbv0037job_step_time import Dbv0037JobStepTime


class Dbv0037JobStep(UniversalBaseModel):
    time: typing.Optional[Dbv0037JobStepTime] = None
    exit_code: typing.Optional[Dbv0037JobExitCode] = None
    nodes: typing.Optional[Dbv0037JobStepNodes] = None
    tasks: typing.Optional[Dbv0037JobStepTasks] = None
    pid: typing.Optional[str] = pydantic.Field(default=None)
    """
    First process PID
    """

    cpu: typing_extensions.Annotated[
        typing.Optional[Dbv0037JobStepCpu], FieldMetadata(alias="CPU"), pydantic.Field(alias="CPU")
    ] = None
    kill_request_user: typing.Optional[str] = pydantic.Field(default=None)
    """
    User who requested job killed
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State of job step
    """

    statistics: typing.Optional[Dbv0037JobStepStatistics] = None
    step: typing.Optional[Dbv0037JobStepStep] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
