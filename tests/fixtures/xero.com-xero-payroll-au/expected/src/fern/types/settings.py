

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account import Account
from .settings_tracking_categories import SettingsTrackingCategories


class Settings(UniversalBaseModel):
    accounts: typing_extensions.Annotated[
        typing.Optional[typing.List[Account]],
        FieldMetadata(alias="Accounts"),
        pydantic.Field(
            alias="Accounts",
            description="Payroll Account details for SuperExpense, SuperLiabilty, WagesExpense, PAYGLiability & WagesPayable.",
        ),
    ] = None
    """
    Payroll Account details for SuperExpense, SuperLiabilty, WagesExpense, PAYGLiability & WagesPayable.
    """

    days_in_payroll_year: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="DaysInPayrollYear"),
        pydantic.Field(alias="DaysInPayrollYear", description="Number of days in the Payroll year"),
    ] = None
    """
    Number of days in the Payroll year
    """

    tracking_categories: typing_extensions.Annotated[
        typing.Optional[SettingsTrackingCategories],
        FieldMetadata(alias="TrackingCategories"),
        pydantic.Field(alias="TrackingCategories", description="Tracking categories for Employees and Timesheets"),
    ] = None
    """
    Tracking categories for Employees and Timesheets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
