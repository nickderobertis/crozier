

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_transfer_balance import BankTransferBalance
from .request_id import RequestId


class BankTransferBalanceGetResponse(UniversalBaseModel):
    """
    Defines the response schema for `/bank_transfer/balance/get`
    """

    balance: BankTransferBalance
    origination_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the origination account that this balance belongs to.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
