

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EnrollmentTrend(UniversalBaseModel):
    """
    Enrollment Trend.
    """

    period: str
    enrolled: int
    capacity: int
    occupancy_rate: float = pydantic.Field()
    """
    Enrolled divided by capacity; ratio, not a percentage. Zero when capacity is zero.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
