

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubaccountResponse(UniversalBaseModel):
    api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique subaccount ID.
    """

    balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Balance of the subAccount. Value is null if balance is shared with primary account.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subaccount creation date and time.
    """

    credit_limit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Credit limit of the subAccount. Value is null if balance is shared with primary account.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the subaccount.
    """

    primary_account_api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique primary account ID.
    """

    suspended: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Subaccount suspension status.
    """

    use_primary_account_balance: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Flag showing if balance is shared with primary account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
