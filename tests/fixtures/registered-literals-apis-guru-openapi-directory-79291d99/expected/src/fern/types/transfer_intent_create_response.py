

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transfer_intent_create import TransferIntentCreate


class TransferIntentCreateResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/intent/create`
    """

    request_id: RequestId
    transfer_intent: TransferIntentCreate

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
