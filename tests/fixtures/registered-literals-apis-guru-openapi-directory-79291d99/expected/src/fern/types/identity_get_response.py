

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_identity import AccountIdentity
from .item import Item
from .request_id import RequestId


class IdentityGetResponse(UniversalBaseModel):
    """
    IdentityGetResponse defines the response schema for `/identity/get`
    """

    accounts: typing.List[AccountIdentity] = pydantic.Field()
    """
    The accounts for which Identity data has been requested
    """

    item: Item
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
