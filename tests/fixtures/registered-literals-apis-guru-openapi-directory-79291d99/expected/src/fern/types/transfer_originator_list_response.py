

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .originator import Originator
from .request_id import RequestId


class TransferOriginatorListResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/originator/list`
    """

    originators: typing.List[Originator]
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
