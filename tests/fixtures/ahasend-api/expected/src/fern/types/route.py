

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .route_object import RouteObject


class Route(UniversalBaseModel):
    object: RouteObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the route
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the route was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the route was last updated
    """

    name: str = pydantic.Field()
    """
    Route name
    """

    url: str = pydantic.Field()
    """
    Webhook URL for the route
    """

    recipient: str = pydantic.Field()
    """
    Recipient filter; an empty string means no recipient filter
    """

    attachments: bool = pydantic.Field()
    """
    Whether to include attachments in route payload
    """

    headers: bool = pydantic.Field()
    """
    Whether to include headers in route payload
    """

    group_by_message_id: bool = pydantic.Field()
    """
    Whether to group by message ID
    """

    strip_replies: bool = pydantic.Field()
    """
    Whether to strip reply content
    """

    enabled: bool = pydantic.Field()
    """
    Whether the route is enabled
    """

    success_count: int = pydantic.Field()
    """
    Number of successful calls
    """

    error_count: int = pydantic.Field()
    """
    Number of unsuccessful calls
    """

    errors_since_last_success: int = pydantic.Field()
    """
    Number of consecutive failed calls. Reset to zero by the next
    successful call.
    """

    last_request_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the route was last called
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
