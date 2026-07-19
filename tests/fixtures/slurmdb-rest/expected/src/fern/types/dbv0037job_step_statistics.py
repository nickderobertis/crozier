

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dbv0037job_step_statistics_cpu import Dbv0037JobStepStatisticsCpu
from .dbv0037job_step_statistics_energy import Dbv0037JobStepStatisticsEnergy


class Dbv0037JobStepStatistics(UniversalBaseModel):
    """
    Statistics of job step
    """

    cpu: typing_extensions.Annotated[
        typing.Optional[Dbv0037JobStepStatisticsCpu], FieldMetadata(alias="CPU"), pydantic.Field(alias="CPU")
    ] = None
    energy: typing.Optional[Dbv0037JobStepStatisticsEnergy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
