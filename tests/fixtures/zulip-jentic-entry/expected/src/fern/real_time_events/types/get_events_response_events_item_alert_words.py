

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_alert_words_type import GetEventsResponseEventsItemAlertWordsType


class GetEventsResponseEventsItemAlertWords(UniversalBaseModel):
    """
    Event sent to a user's clients when that user's set of configured
    [alert words](/help/dm-mention-alert-notifications#alert-words) have changed.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemAlertWordsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    alert_words: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of strings, where each string is an alert word (or phrase)
    configured by the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
