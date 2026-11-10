

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_override_password import SandboxOverridePassword
from .sandbox_override_username import SandboxOverrideUsername
from .sandbox_public_token_create_request_options_income_verification import (
    SandboxPublicTokenCreateRequestOptionsIncomeVerification,
)
from .sandbox_public_token_create_request_options_transactions import SandboxPublicTokenCreateRequestOptionsTransactions


class SandboxPublicTokenCreateRequestOptions(UniversalBaseModel):
    """
    An optional set of options to be used when configuring the Item. If specified, must not be `null`.
    """

    income_verification: typing.Optional[SandboxPublicTokenCreateRequestOptionsIncomeVerification] = None
    override_password: typing.Optional[SandboxOverridePassword] = None
    override_username: typing.Optional[SandboxOverrideUsername] = None
    transactions: typing.Optional[SandboxPublicTokenCreateRequestOptionsTransactions] = None
    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specify a webhook to associate with the new Item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
