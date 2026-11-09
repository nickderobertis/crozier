

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .income_verification_source_type import IncomeVerificationSourceType
from .sandbox_public_token_create_request_income_verification_bank_income import (
    SandboxPublicTokenCreateRequestIncomeVerificationBankIncome,
)


class SandboxPublicTokenCreateRequestOptionsIncomeVerification(UniversalBaseModel):
    """
    A set of parameters for income verification options. This field is required if `income_verification` is included in the `initial_products` array.
    """

    bank_income: typing.Optional[SandboxPublicTokenCreateRequestIncomeVerificationBankIncome] = None
    income_source_types: typing.Optional[typing.List[IncomeVerificationSourceType]] = pydantic.Field(default=None)
    """
    The types of source income data that users will be permitted to share. Options include `bank` and `payroll`. Currently you can only specify one of these options.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
