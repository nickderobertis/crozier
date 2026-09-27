

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EnrollmentPeriodAnalytics(UniversalBaseModel):
    """
    Enrollment Period Analytics.
    """

    year: str
    period: str
    period_type: str
    month_start: str
    month_end: str
    months_in_period: int
    target_occupancy_percent: float
    actual_occupancy_percent: float
    difference: float
    target_tuition: float
    target_tuition_shortfall: float
    vacant_days_shortfall: float
    fte_enrollment_shortfall_month: int
    vacancy_months: float
    target_occupancy_days: float
    daily_tuition: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
