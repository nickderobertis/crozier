

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_token_get_metadata_response import LinkTokenGetMetadataResponse
from .request_id import RequestId


class LinkTokenGetResponse(UniversalBaseModel):
    """
    LinkTokenGetResponse defines the response schema for `/link/token/get`
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The creation timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    expiration: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The expiration timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    link_token: str = pydantic.Field()
    """
    A `link_token`, which can be supplied to Link in order to initialize it and receive a `public_token`, which can be exchanged for an `access_token`.
    """

    metadata: LinkTokenGetMetadataResponse
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
