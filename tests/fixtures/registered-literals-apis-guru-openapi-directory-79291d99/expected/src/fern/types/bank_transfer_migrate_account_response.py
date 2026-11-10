

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class BankTransferMigrateAccountResponse(UniversalBaseModel):
    """
    Defines the response schema for `/bank_transfer/migrate_account`
    """

    access_token: str = pydantic.Field()
    """
    The Plaid `access_token` for the newly created Item.
    """

    account_id: str = pydantic.Field()
    """
    The Plaid `account_id` for the newly created Item.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
