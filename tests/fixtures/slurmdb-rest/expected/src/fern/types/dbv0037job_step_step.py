

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_step_step_het import Dbv0037JobStepStepHet
from .dbv0037job_step_step_task import Dbv0037JobStepStepTask
from .dbv0037job_step_step_tres import Dbv0037JobStepStepTres


class Dbv0037JobStepStep(UniversalBaseModel):
    """
    Step details
    """

    job_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Parent job id
    """

    het: typing.Optional[Dbv0037JobStepStepHet] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Step id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Step name
    """

    task: typing.Optional[Dbv0037JobStepStepTask] = None
    tres: typing.Optional[Dbv0037JobStepStepTres] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
