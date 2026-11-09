

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detailed_originator import DetailedOriginator
from .request_id import RequestId


class TransferOriginatorGetResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/originator/get`
    """

    originator: DetailedOriginator
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
