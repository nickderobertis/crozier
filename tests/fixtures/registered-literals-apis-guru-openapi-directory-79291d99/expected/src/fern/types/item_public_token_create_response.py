

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class ItemPublicTokenCreateResponse(UniversalBaseModel):
    """
    ItemPublicTokenCreateResponse defines the response schema for `/item/public_token/create`
    """

    expiration: typing.Optional[dt.datetime] = None
    public_token: str = pydantic.Field()
    """
    A `public_token` for the particular Item corresponding to the specified `access_token`
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
