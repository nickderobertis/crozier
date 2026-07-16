

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .superannuation_calculation_type import SuperannuationCalculationType
from .superannuation_contribution_type import SuperannuationContributionType


class SuperLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Amount"),
        pydantic.Field(alias="Amount", description="Super membership amount"),
    ] = None
    """
    Super membership amount
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
        pydantic.Field(alias="ExpenseAccountCode", description="expense account code"),
    ] = None
    """
    expense account code
    """

    liability_account_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LiabilityAccountCode"),
        pydantic.Field(alias="LiabilityAccountCode", description="liabilty account code"),
    ] = None
    """
    liabilty account code
    """

    minimum_monthly_earnings: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="MinimumMonthlyEarnings"),
        pydantic.Field(alias="MinimumMonthlyEarnings", description="amount of minimum earnings"),
    ] = None
    """
    amount of minimum earnings
    """

    percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Percentage"),
        pydantic.Field(alias="Percentage", description="percentage for super line"),
    ] = None
    """
    percentage for super line
    """

    super_membership_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SuperMembershipID"),
        pydantic.Field(alias="SuperMembershipID", description="Xero super membership ID"),
    ] = None
    """
    Xero super membership ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
