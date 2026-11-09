

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transfer_repayment import TransferRepayment


class TransferRepaymentListResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/repayments/list`
    """

    repayments: typing.List[TransferRepayment]
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
