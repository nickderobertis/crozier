

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .time_off_requests_filter_time_off_request_status import TimeOffRequestsFilterTimeOffRequestStatus


class TimeOffRequestsFilter(UniversalBaseModel):
    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Employee ID
    """

    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    End date
    """

    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Start date
    """

    time_off_request_status: typing.Optional[TimeOffRequestsFilterTimeOffRequestStatus] = pydantic.Field(default=None)
    """
    Time off request status to filter on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
