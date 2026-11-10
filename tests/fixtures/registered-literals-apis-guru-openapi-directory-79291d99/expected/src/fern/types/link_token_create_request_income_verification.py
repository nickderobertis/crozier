

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_token import AccessToken
from .income_verification_source_type import IncomeVerificationSourceType
from .link_token_create_request_income_verification_bank_income import (
    LinkTokenCreateRequestIncomeVerificationBankIncome,
)
from .link_token_create_request_income_verification_payroll_income import (
    LinkTokenCreateRequestIncomeVerificationPayrollIncome,
)
from .link_token_create_request_user_stated_income_source import LinkTokenCreateRequestUserStatedIncomeSource


class LinkTokenCreateRequestIncomeVerification(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with the Income product. This field is required if `income_verification` is included in the `products` array.
    """

    access_tokens: typing.Optional[typing.List[AccessToken]] = pydantic.Field(default=None)
    """
    An array of access tokens corresponding to Items that a user has previously connected with. Data from these institutions will be cross-referenced with document data received during the Document Income flow to help verify that the uploaded documents are accurate. If the `transactions` product was not initialized for these Items during link, it will be initialized after this Link session.
    
    This field should only be used with the `payroll` income source type.
    """

    asset_report_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `asset_report_id` of an asset report associated with the user, as provided by `/asset_report/create`. Providing an `asset_report_id` is optional and can be used to verify the user through a streamlined flow. If provided, the bank linking flow will be skipped.
    """

    bank_income: typing.Optional[LinkTokenCreateRequestIncomeVerificationBankIncome] = None
    income_source_types: typing.Optional[typing.List[IncomeVerificationSourceType]] = pydantic.Field(default=None)
    """
    The types of source income data that users will be permitted to share. Options include `bank` and `payroll`. Currently you can only specify one of these options.
    """

    income_verification_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `income_verification_id` of the verification instance, as provided by `/income/verification/create`.
    """

    payroll_income: typing.Optional[LinkTokenCreateRequestIncomeVerificationPayrollIncome] = None
    precheck_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow by streamlining the Link interface presented to the end user.
    """

    stated_income_sources: typing.Optional[typing.List[LinkTokenCreateRequestUserStatedIncomeSource]] = pydantic.Field(
        default=None
    )
    """
    A list of user stated income sources
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
