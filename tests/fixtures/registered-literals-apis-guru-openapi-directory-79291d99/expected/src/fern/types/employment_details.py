

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pay import Pay


class EmploymentDetails(UniversalBaseModel):
    """
    An object representing employment details found on a paystub.
    """

    annual_salary: typing.Optional[Pay] = None
    hire_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date on which the employee was hired, in the YYYY-MM-DD format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
