

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .superannuation_calculation_type import SuperannuationCalculationType
from .superannuation_contribution_type import SuperannuationContributionType


class SuperLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Amount")] = pydantic.Field(
        default=None
    )
    """
    Super membership amount
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
    expense account code
    """

    liability_account_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LiabilityAccountCode")
    ] = pydantic.Field(default=None)
    """
    liabilty account code
    """

    minimum_monthly_earnings: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="MinimumMonthlyEarnings")
    ] = pydantic.Field(default=None)
    """
    amount of minimum earnings
    """

    percentage: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Percentage")] = pydantic.Field(
        default=None
    )
    """
    percentage for super line
    """

    super_membership_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="SuperMembershipID")] = (
        pydantic.Field(default=None)
    )
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
