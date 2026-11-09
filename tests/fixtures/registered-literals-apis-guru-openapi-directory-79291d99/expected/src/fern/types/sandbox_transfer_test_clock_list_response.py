

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transfer_test_clock import TransferTestClock


class SandboxTransferTestClockListResponse(UniversalBaseModel):
    """
    Defines the response schema for `/sandbox/transfer/test_clock/list`
    """

    request_id: RequestId
    test_clocks: typing.List[TransferTestClock]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
