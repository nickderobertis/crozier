

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employment_status import EmploymentStatus
from .hris_job_location import HrisJobLocation
from .id import Id
from .title import Title


class HrisJob(UniversalBaseModel):
    department: typing.Optional[str] = pydantic.Field(default=None)
    """
    Department name
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of the employee
    """

    employment_status: typing.Optional[EmploymentStatus] = None
    end_date: typing.Optional[dt.date] = None
    id: typing.Optional[Id] = None
    is_primary: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether this the employee's primary job.
    """

    location: typing.Optional[HrisJobLocation] = None
    start_date: typing.Optional[dt.date] = None
    title: typing.Optional[Title] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
