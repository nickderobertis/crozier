

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_webhook_events_response_events_item import ListWebhookEventsResponseEventsItem


class ListWebhookEventsResponse(UniversalBaseModel):
    page: typing.Optional[float] = pydantic.Field(default=None)
    """
    Current page number
    """

    limit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of events per page (25)
    """

    has_more: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMore"),
        pydantic.Field(alias="hasMore", description="Whether there are more pages available"),
    ] = None
    """
    Whether there are more pages available
    """

    total_number_of_events: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="totalNumberOfEvents"),
        pydantic.Field(alias="totalNumberOfEvents", description="Total number of webhook events"),
    ] = None
    """
    Total number of webhook events
    """

    events: typing.Optional[typing.List[ListWebhookEventsResponseEventsItem]] = pydantic.Field(default=None)
    """
    List of webhook events
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
