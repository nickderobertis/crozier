

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EnrollmentAnalytics(UniversalBaseModel):
    """
    Enrollment Analytics.
    """

    period: str
    capacity_days: int
    vacancy_days: int
    vacancy_percent: float
    enrolled_days: int
    enrolled_percent: float
    target_occupancy: float
    targeted_enrolled_days: float
    vacant_days_shortfall: float
    monthly_tuition: float
    daily_tuition: float
    tuition_shortfall: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
