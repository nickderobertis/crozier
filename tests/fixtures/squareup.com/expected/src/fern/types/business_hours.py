

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .business_hours_period import BusinessHoursPeriod


class BusinessHours(UniversalBaseModel):
    """
    Represents the hours of operation for a business location.
    """

    periods: typing.Optional[typing.List[BusinessHoursPeriod]] = pydantic.Field(default=None)
    """
    The list of time periods during which the business is open. There may be at most 10
    periods per day.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
