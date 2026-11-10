

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .simulated_transfer_sweep import SimulatedTransferSweep


class SandboxTransferSweepSimulateResponse(UniversalBaseModel):
    """
    Defines the response schema for `/sandbox/transfer/sweep/simulate`
    """

    request_id: RequestId
    sweep: typing.Optional[SimulatedTransferSweep] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
