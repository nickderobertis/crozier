

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .calendar_type import CalendarType
from .validation_error import ValidationError


class PayrollCalendar(UniversalBaseModel):
    calendar_type: typing_extensions.Annotated[
        typing.Optional[CalendarType], FieldMetadata(alias="CalendarType"), pydantic.Field(alias="CalendarType")
    ] = None
    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Name of the Payroll Calendar"),
    ] = None
    """
    Name of the Payroll Calendar
    """

    payment_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PaymentDate"),
        pydantic.Field(
            alias="PaymentDate",
            description="The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD)",
        ),
    ] = None
    """
    The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD)
    """

    payroll_calendar_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PayrollCalendarID"),
        pydantic.Field(alias="PayrollCalendarID", description="Xero identifier"),
    ] = None
    """
    Xero identifier
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StartDate"),
        pydantic.Field(
            alias="StartDate",
            description="The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD)",
        ),
    ] = None
    """
    The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD)
    """

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
