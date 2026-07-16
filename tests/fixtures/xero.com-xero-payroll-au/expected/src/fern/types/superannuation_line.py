

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .superannuation_calculation_type import SuperannuationCalculationType
from .superannuation_contribution_type import SuperannuationContributionType


class SuperannuationLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Amount")] = pydantic.Field(
        default=None
    )
    """
    Superannuation amount
    """

    calculation_type: typing_extensions.Annotated[
        typing.Optional[SuperannuationCalculationType], FieldMetadata(alias="CalculationType")
    ] = None
    contribution_type: typing_extensions.Annotated[
        typing.Optional[SuperannuationContributionType], FieldMetadata(alias="ContributionType")
    ] = None
    expense_account_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ExpenseAccountCode")
    ] = pydantic.Field(default=None)
    """
    Superannuation expense account code.
    """

    liability_account_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LiabilityAccountCode")
    ] = pydantic.Field(default=None)
    """
    Superannuation liability account code
    """

    minimum_monthly_earnings: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="MinimumMonthlyEarnings")
    ] = pydantic.Field(default=None)
    """
    Superannuation minimum monthly earnings.
    """

    payment_date_for_this_period: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PaymentDateForThisPeriod")
    ] = pydantic.Field(default=None)
    """
    Superannuation payment date for the current period (YYYY-MM-DD)
    """

    percentage: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Percentage")] = pydantic.Field(
        default=None
    )
    """
    Superannuation percentage
    """

    super_membership_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="SuperMembershipID")] = (
        pydantic.Field(default=None)
    )
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
