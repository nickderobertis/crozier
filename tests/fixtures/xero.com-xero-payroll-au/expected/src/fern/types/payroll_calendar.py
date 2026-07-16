

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .calendar_type import CalendarType
from .validation_error import ValidationError


class PayrollCalendar(UniversalBaseModel):
    calendar_type: typing_extensions.Annotated[typing.Optional[CalendarType], FieldMetadata(alias="CalendarType")] = (
        None
    )
    name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Name")] = pydantic.Field(default=None)
    """
    Name of the Payroll Calendar
    """

    payment_date: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PaymentDate")] = (
        pydantic.Field(default=None)
    )
    """
    The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD)
    """

    payroll_calendar_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PayrollCalendarID")] = (
        pydantic.Field(default=None)
    )
    """
    Xero identifier
    """

    start_date: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StartDate")] = pydantic.Field(
        default=None
    )
    """
    The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD)
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
