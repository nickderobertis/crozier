

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .employment_termination_payment_type import EmploymentTerminationPaymentType
from .entitlement_final_pay_payout_type import EntitlementFinalPayPayoutType
from .leave_line_calculation_type import LeaveLineCalculationType


class LeaveLine(UniversalBaseModel):
    annual_number_of_units: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="AnnualNumberOfUnits")
    ] = pydantic.Field(default=None)
    """
    Hours of leave accrued each year
    """

    calculation_type: typing_extensions.Annotated[
        typing.Optional[LeaveLineCalculationType], FieldMetadata(alias="CalculationType")
    ] = None
    employment_termination_payment_type: typing_extensions.Annotated[
        typing.Optional[EmploymentTerminationPaymentType], FieldMetadata(alias="EmploymentTerminationPaymentType")
    ] = None
    entitlement_final_pay_payout_type: typing_extensions.Annotated[
        typing.Optional[EntitlementFinalPayPayoutType], FieldMetadata(alias="EntitlementFinalPayPayoutType")
    ] = None
    full_time_number_of_units_per_period: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="FullTimeNumberOfUnitsPerPeriod")
    ] = pydantic.Field(default=None)
    """
    Normal ordinary earnings number of units for leave line.
    """

    include_superannuation_guarantee_contribution: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IncludeSuperannuationGuaranteeContribution")
    ] = pydantic.Field(default=None)
    """
    amount of leave line
    """

    leave_type_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LeaveTypeID")] = (
        pydantic.Field(default=None)
    )
    """
    Xero leave type identifier
    """

    number_of_units: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="NumberOfUnits")] = (
        pydantic.Field(default=None)
    )
    """
    Number of units for leave line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
