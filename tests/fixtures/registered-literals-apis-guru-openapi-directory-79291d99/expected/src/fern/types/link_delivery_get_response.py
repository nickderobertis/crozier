

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_token import AccessToken
from .item_id import ItemId
from .link_delivery_session_status import LinkDeliverySessionStatus
from .request_id import RequestId


class LinkDeliveryGetResponse(UniversalBaseModel):
    """
    LinkDeliveryGetRequest defines the response schema for `/link_delivery/get`
    """

    access_tokens: typing.Optional[typing.List[AccessToken]] = pydantic.Field(default=None)
    """
    An array of access tokens associated with the Link Delivery session.
    """

    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the time the given Link Delivery Session was completed at.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the time the given Link Delivery Session was created at.
    """

    item_ids: typing.Optional[typing.List[ItemId]] = pydantic.Field(default=None)
    """
    An array of `item_id`s associated with the Link Delivery session.
    """

    request_id: RequestId
    status: LinkDeliverySessionStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
