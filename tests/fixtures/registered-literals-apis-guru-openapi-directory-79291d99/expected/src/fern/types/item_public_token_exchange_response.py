

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_token import AccessToken
from .request_id import RequestId


class ItemPublicTokenExchangeResponse(UniversalBaseModel):
    """
    ItemPublicTokenExchangeResponse defines the response schema for `/item/public_token/exchange`
    """

    access_token: AccessToken
    item_id: str = pydantic.Field()
    """
    The `item_id` value of the Item associated with the returned `access_token`
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
