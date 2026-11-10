

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .transfer_sweep import TransferSweep


class SimulatedTransferSweep(TransferSweep):
    """
    A sweep returned from the `/sandbox/transfer/sweep/simulate` endpoint.
    Can be null if there are no transfers to include in a sweep.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
