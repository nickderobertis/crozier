

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transfer_test_clock import TransferTestClock


class SandboxTransferTestClockGetResponse(UniversalBaseModel):
    """
    Defines the response schema for `/sandbox/transfer/test_clock/get`
    """

    request_id: RequestId
    test_clock: TransferTestClock

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
