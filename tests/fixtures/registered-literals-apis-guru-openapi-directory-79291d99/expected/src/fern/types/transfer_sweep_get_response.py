

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transfer_sweep import TransferSweep


class TransferSweepGetResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/sweep/get`
    """

    request_id: RequestId
    sweep: TransferSweep

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
