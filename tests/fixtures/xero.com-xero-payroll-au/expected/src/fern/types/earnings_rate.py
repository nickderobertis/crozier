

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .allowance_type import AllowanceType
from .earnings_type import EarningsType
from .employment_termination_payment_type import EmploymentTerminationPaymentType
from .rate_type import RateType


class EarningsRate(UniversalBaseModel):
    account_code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="AccountCode")] = (
        pydantic.Field(default=None)
    )
    """
    See Accounts
    """

    accrue_leave: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="AccrueLeave")] = (
        pydantic.Field(default=None)
    )
    """
    Indicates that this earnings rate should accrue leave. Only applicable if RateType is MULTIPLE
    """

    allowance_type: typing_extensions.Annotated[
        typing.Optional[AllowanceType], FieldMetadata(alias="AllowanceType")
    ] = None
    amount: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Amount")] = pydantic.Field(
        default=None
    )
    """
    Optional Amount for FIXEDAMOUNT RateType EarningsRate
    """

    current_record: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="CurrentRecord")] = (
        pydantic.Field(default=None)
    )
    """
    Is the current record
    """

    earnings_rate_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EarningsRateID")] = (
        pydantic.Field(default=None)
    )
    """
    Xero identifier
    """

    earnings_type: typing_extensions.Annotated[typing.Optional[EarningsType], FieldMetadata(alias="EarningsType")] = (
        None
    )
    employment_termination_payment_type: typing_extensions.Annotated[
        typing.Optional[EmploymentTerminationPaymentType], FieldMetadata(alias="EmploymentTerminationPaymentType")
    ] = None
    is_exempt_from_super: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsExemptFromSuper")
    ] = pydantic.Field(default=None)
    """
    See the ATO website for details of which payments are exempt from SGC
    """

    is_exempt_from_tax: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="IsExemptFromTax")] = (
        pydantic.Field(default=None)
    )
    """
    Most payments are subject to tax, so you should only set this value if you are sure that a payment is exempt from PAYG withholding
    """

    is_reportable_as_w1: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="IsReportableAsW1")] = (
        pydantic.Field(default=None)
    )
    """
    Boolean to determine if the earnings rate is reportable or exempt from W1
    """

    multiplier: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Multiplier")] = pydantic.Field(
        default=None
    )
    """
    This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MULTIPLE
    """

    name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Name")] = pydantic.Field(default=None)
    """
    Name of the earnings rate (max length = 100)
    """

    rate_per_unit: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="RatePerUnit")] = (
        pydantic.Field(default=None)
    )
    """
    Default rate per unit (optional). Only applicable if RateType is RATEPERUNIT.
    """

    rate_type: typing_extensions.Annotated[typing.Optional[RateType], FieldMetadata(alias="RateType")] = None
    type_of_units: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeOfUnits")] = (
        pydantic.Field(default=None)
    )
    """
    Type of units used to record earnings (max length = 50). Only When RateType is RATEPERUNIT
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
