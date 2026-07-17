

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .superannuation_calculation_type import SuperannuationCalculationType
from .superannuation_contribution_type import SuperannuationContributionType


class SuperannuationLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Amount"),
        pydantic.Field(alias="Amount", description="Superannuation amount"),
    ] = None
    """
    Superannuation amount
    """

    calculation_type: typing_extensions.Annotated[
        typing.Optional[SuperannuationCalculationType],
        FieldMetadata(alias="CalculationType"),
        pydantic.Field(alias="CalculationType"),
    ] = None
    contribution_type: typing_extensions.Annotated[
        typing.Optional[SuperannuationContributionType],
        FieldMetadata(alias="ContributionType"),
        pydantic.Field(alias="ContributionType"),
    ] = None
    expense_account_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExpenseAccountCode"),
        pydantic.Field(alias="ExpenseAccountCode", description="Superannuation expense account code."),
    ] = None
    """
    Superannuation expense account code.
    """

    liability_account_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LiabilityAccountCode"),
        pydantic.Field(alias="LiabilityAccountCode", description="Superannuation liability account code"),
    ] = None
    """
    Superannuation liability account code
    """

    minimum_monthly_earnings: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="MinimumMonthlyEarnings"),
        pydantic.Field(alias="MinimumMonthlyEarnings", description="Superannuation minimum monthly earnings."),
    ] = None
    """
    Superannuation minimum monthly earnings.
    """

    payment_date_for_this_period: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PaymentDateForThisPeriod"),
        pydantic.Field(
            alias="PaymentDateForThisPeriod",
            description="Superannuation payment date for the current period (YYYY-MM-DD)",
        ),
    ] = None
    """
    Superannuation payment date for the current period (YYYY-MM-DD)
    """

    percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Percentage"),
        pydantic.Field(alias="Percentage", description="Superannuation percentage"),
    ] = None
    """
    Superannuation percentage
    """

    super_membership_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SuperMembershipID"),
        pydantic.Field(alias="SuperMembershipID", description="Xero identifier for payroll super fund membership ID."),
    ] = None
    """
    Xero identifier for payroll super fund membership ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
