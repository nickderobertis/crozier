

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class LinkDeliveryCreateResponse(UniversalBaseModel):
    """
    LinkDeliveryCreateResponse defines the response schema for `/link_delivery/create`
    """

    link_delivery_session_id: str = pydantic.Field()
    """
    The ID for the Link Delivery session. Same as the `link_token` string excluding the "link-{env}-" prefix.
    """

    link_delivery_url: str = pydantic.Field()
    """
    The URL to the Link Delivery session, which will be delivered by the specified delivery method.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
