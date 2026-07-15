

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .id import Id
from .time_off_request_notes import TimeOffRequestNotes
from .time_off_request_request_type import TimeOffRequestRequestType
from .time_off_request_status import TimeOffRequestStatus
from .time_off_request_units import TimeOffRequestUnits
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class TimeOffRequest(UniversalBaseModel):
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of time off requested.
    """

    approval_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the request was approved
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the time off request.
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the employee
    """

    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end date of the time off request.
    """

    id: typing.Optional[Id] = None
    notes: typing.Optional[TimeOffRequestNotes] = None
    policy_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the policy
    """

    request_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the request was made.
    """

    request_type: typing.Optional[TimeOffRequestRequestType] = pydantic.Field(default=None)
    """
    The type of request
    """

    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the time off request.
    """

    status: typing.Optional[TimeOffRequestStatus] = pydantic.Field(default=None)
    """
    The status of the time off request.
    """

    units: typing.Optional[TimeOffRequestUnits] = pydantic.Field(default=None)
    """
    The unit of time off requested. Possible values include: `hours`, `days`, or `other`.
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
