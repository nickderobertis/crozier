

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_transfer_sweep import BankTransferSweep
from .request_id import RequestId


class BankTransferSweepGetResponse(UniversalBaseModel):
    """
    BankTransferSweepGetResponse defines the response schema for `/bank_transfer/sweep/get`
    """

    request_id: RequestId
    sweep: BankTransferSweep

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
