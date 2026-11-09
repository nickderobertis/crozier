

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_test_clock_id import TransferTestClockId
from .virtual_time import VirtualTime


class TransferTestClock(UniversalBaseModel):
    """
    Defines the test clock for a transfer.
    """

    test_clock_id: TransferTestClockId
    virtual_time: VirtualTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
