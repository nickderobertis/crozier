

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_step_step_tres_allocated_item import Dbv0037JobStepStepTresAllocatedItem
from .dbv0037job_step_step_tres_requested import Dbv0037JobStepStepTresRequested


class Dbv0037JobStepStepTres(UniversalBaseModel):
    """
    TRES usage
    """

    requested: typing.Optional[Dbv0037JobStepStepTresRequested] = None
    consumed: typing.Optional[Dbv0037JobStepStepTresRequested] = None
    allocated: typing.Optional[typing.List[Dbv0037JobStepStepTresAllocatedItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
