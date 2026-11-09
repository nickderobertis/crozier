

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transfer_authorization import TransferAuthorization


class TransferAuthorizationCreateResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/authorization/create`
    """

    authorization: TransferAuthorization
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
