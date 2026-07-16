

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimesheetLine(UniversalBaseModel):
    earnings_rate_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EarningsRateID")] = (
        pydantic.Field(default=None)
    )
    """
    The Xero identifier for an Earnings Rate
    """

    number_of_units: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="NumberOfUnits")
    ] = pydantic.Field(default=None)
    """
    The number of units on a timesheet line
    """

    tracking_item_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TrackingItemID")] = (
        pydantic.Field(default=None)
    )
    """
    The Xero identifier for a Tracking Category. The TrackingOptionID must belong to the TrackingCategory selected as TimesheetCategories under Payroll Settings.
    """

    updated_date_utc: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="UpdatedDateUTC")] = (
        pydantic.Field(default=None)
    )
    """
    Last modified timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
