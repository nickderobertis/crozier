

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.navigation_view import NavigationView
from .get_events_response_events_item_navigation_view_op import GetEventsResponseEventsItemNavigationViewOp
from .get_events_response_events_item_navigation_view_type import GetEventsResponseEventsItemNavigationViewType


class GetEventsResponseEventsItemNavigationView(UniversalBaseModel):
    """
    Event containing details of a newly configured navigation view.

    **Changes**: New in Zulip 11.0 (feature level 390).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemNavigationViewType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemNavigationViewOp] = None
    navigation_view: typing.Optional[NavigationView] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
