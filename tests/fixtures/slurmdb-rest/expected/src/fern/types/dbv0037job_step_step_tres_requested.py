

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_step_step_tres_requested_average_item import Dbv0037JobStepStepTresRequestedAverageItem
from .dbv0037job_step_step_tres_requested_max_item import Dbv0037JobStepStepTresRequestedMaxItem
from .dbv0037job_step_step_tres_requested_min_item import Dbv0037JobStepStepTresRequestedMinItem
from .dbv0037job_step_step_tres_requested_total_item import Dbv0037JobStepStepTresRequestedTotalItem


class Dbv0037JobStepStepTresRequested(UniversalBaseModel):
    """
    TRES requested for job
    """

    average: typing.Optional[typing.List[Dbv0037JobStepStepTresRequestedAverageItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    max: typing.Optional[typing.List[Dbv0037JobStepStepTresRequestedMaxItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    min: typing.Optional[typing.List[Dbv0037JobStepStepTresRequestedMinItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    total: typing.Optional[typing.List[Dbv0037JobStepStepTresRequestedTotalItem]] = pydantic.Field(default=None)
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
