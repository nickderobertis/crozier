

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_transfer import BankTransfer
from .request_id import RequestId


class BankTransferListResponse(UniversalBaseModel):
    """
    Defines the response schema for `/bank_transfer/list`
    """

    bank_transfers: typing.List[BankTransfer]
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
