

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transfer_sweep import TransferSweep


class TransferSweepListResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/sweep/list`
    """

    request_id: RequestId
    sweeps: typing.List[TransferSweep]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
