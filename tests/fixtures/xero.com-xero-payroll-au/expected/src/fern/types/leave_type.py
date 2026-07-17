

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LeaveType(UniversalBaseModel):
    current_record: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="CurrentRecord"),
        pydantic.Field(alias="CurrentRecord", description="Is the current record"),
    ] = None
    """
    Is the current record
    """

    is_paid_leave: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsPaidLeave"),
        pydantic.Field(
            alias="IsPaidLeave",
            description="Set this to indicate that an employee will be paid when taking this type of leave",
        ),
    ] = None
    """
    Set this to indicate that an employee will be paid when taking this type of leave
    """

    leave_loading_rate: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="LeaveLoadingRate"),
        pydantic.Field(
            alias="LeaveLoadingRate",
            description="Enter an amount here if your organisation pays an additional percentage on top of ordinary earnings when your employees take leave (typically 17.5%)",
        ),
    ] = None
    """
    Enter an amount here if your organisation pays an additional percentage on top of ordinary earnings when your employees take leave (typically 17.5%)
    """

    leave_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LeaveTypeID"),
        pydantic.Field(alias="LeaveTypeID", description="Xero identifier"),
    ] = None
    """
    Xero identifier
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Name of the earnings rate (max length = 100)"),
    ] = None
    """
    Name of the earnings rate (max length = 100)
    """

    normal_entitlement: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NormalEntitlement"),
        pydantic.Field(
            alias="NormalEntitlement", description="The number of units the employee is entitled to each year"
        ),
    ] = None
    """
    The number of units the employee is entitled to each year
    """

    show_on_payslip: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ShowOnPayslip"),
        pydantic.Field(
            alias="ShowOnPayslip",
            description="Set this if you want a balance for this leave type to be shown on your employee’s payslips",
        ),
    ] = None
    """
    Set this if you want a balance for this leave type to be shown on your employee’s payslips
    """

    type_of_units: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeOfUnits"),
        pydantic.Field(
            alias="TypeOfUnits",
            description="The type of units by which leave entitlements are normally tracked. These are typically the same as the type of units used for the employee’s ordinary earnings rate",
        ),
    ] = None
    """
    The type of units by which leave entitlements are normally tracked. These are typically the same as the type of units used for the employee’s ordinary earnings rate
    """

    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
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
