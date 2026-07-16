

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .settings_tracking_categories_employee_groups import SettingsTrackingCategoriesEmployeeGroups
from .settings_tracking_categories_timesheet_categories import SettingsTrackingCategoriesTimesheetCategories


class SettingsTrackingCategories(UniversalBaseModel):
    """
    Tracking categories for Employees and Timesheets
    """

    employee_groups: typing_extensions.Annotated[
        typing.Optional[SettingsTrackingCategoriesEmployeeGroups], FieldMetadata(alias="EmployeeGroups")
    ] = pydantic.Field(default=None)
    """
    The tracking category used for employees
    """

    timesheet_categories: typing_extensions.Annotated[
        typing.Optional[SettingsTrackingCategoriesTimesheetCategories], FieldMetadata(alias="TimesheetCategories")
    ] = pydantic.Field(default=None)
    """
    The tracking category used for timesheets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
