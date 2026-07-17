

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .timesheet_lines import TimesheetLines
from .timesheet_status import TimesheetStatus
from .validation_error import ValidationError


class Timesheet(UniversalBaseModel):
    employee_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="EmployeeID"),
        pydantic.Field(alias="EmployeeID", description="The Xero identifier for an employee"),
    ]
    """
    The Xero identifier for an employee
    """

    end_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="EndDate"), pydantic.Field(alias="EndDate", description="Period end date (YYYY-MM-DD)")
    ]
    """
    Period end date (YYYY-MM-DD)
    """

    hours: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Hours"),
        pydantic.Field(alias="Hours", description="Timesheet total hours"),
    ] = None
    """
    Timesheet total hours
    """

    start_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StartDate"),
        pydantic.Field(alias="StartDate", description="Period start date (YYYY-MM-DD)"),
    ]
    """
    Period start date (YYYY-MM-DD)
    """

    status: typing_extensions.Annotated[
        typing.Optional[TimesheetStatus], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    timesheet_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TimesheetID"),
        pydantic.Field(alias="TimesheetID", description="The Xero identifier for a Payroll Timesheet"),
    ] = None
    """
    The Xero identifier for a Payroll Timesheet
    """

    timesheet_lines: typing_extensions.Annotated[
        typing.Optional[TimesheetLines], FieldMetadata(alias="TimesheetLines"), pydantic.Field(alias="TimesheetLines")
    ] = None
    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
    """
    Last modified timestamp
    """

    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[ValidationError]],
        FieldMetadata(alias="ValidationErrors"),
        pydantic.Field(
            alias="ValidationErrors", description="Displays array of validation error messages from the API"
        ),
    ] = None
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
