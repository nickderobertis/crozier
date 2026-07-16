

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .leave_period import LeavePeriod
from .validation_error import ValidationError


class LeaveApplication(UniversalBaseModel):
    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    The Description of the Leave
    """

    employee_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EmployeeID")] = pydantic.Field(
        default=None
    )
    """
    The Xero identifier for Payroll Employee
    """

    end_date: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EndDate")] = pydantic.Field(
        default=None
    )
    """
    End date of the leave (YYYY-MM-DD)
    """

    leave_application_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LeaveApplicationID")
    ] = pydantic.Field(default=None)
    """
    The Xero identifier for Payroll Employee
    """

    leave_periods: typing_extensions.Annotated[
        typing.Optional[typing.List[LeavePeriod]], FieldMetadata(alias="LeavePeriods")
    ] = None
    leave_type_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LeaveTypeID")] = (
        pydantic.Field(default=None)
    )
    """
    The Xero identifier for Leave Type
    """

    start_date: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StartDate")] = pydantic.Field(
        default=None
    )
    """
    Start date of the leave (YYYY-MM-DD)
    """

    title: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Title")] = pydantic.Field(
        default=None
    )
    """
    The title of the leave
    """

    updated_date_utc: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="UpdatedDateUTC")] = (
        pydantic.Field(default=None)
    )
    """
    Last modified timestamp
    """

    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[ValidationError]], FieldMetadata(alias="ValidationErrors")
    ] = pydantic.Field(default=None)
    """
    Displays array of validation error messages from the API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
