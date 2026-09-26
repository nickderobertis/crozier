

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_message_details_message_details_value import (
    GetEventsResponseEventsItemMessageDetailsMessageDetailsValue,
)
from .get_events_response_events_item_message_details_op import GetEventsResponseEventsItemMessageDetailsOp
from .get_events_response_events_item_message_details_operation import (
    GetEventsResponseEventsItemMessageDetailsOperation,
)
from .get_events_response_events_item_message_details_type import GetEventsResponseEventsItemMessageDetailsType


class GetEventsResponseEventsItemMessageDetails(UniversalBaseModel):
    """
    Event sent to a user when [message flags][message-flags] are
    removed from messages.

    See the description for the [`update_message_flags` op:
    `add`](/api/get-events#update_message_flags-add) event for
    more details about these events.

    [message-flags]: /api/update-message-flags#available-flags
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemMessageDetailsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemMessageDetailsOp] = None
    operation: typing.Optional[GetEventsResponseEventsItemMessageDetailsOperation] = pydantic.Field(default=None)
    """
    Old name for the `op` field in this event type.
    
    **Deprecated** in Zulip 4.0 (feature level 32), and
    replaced by the `op` field.
    """

    flag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [flag][message-flags] to be removed.
    """

    messages: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the IDs of the messages from which the flag
    was removed.
    """

    all_: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="all"),
        pydantic.Field(
            alias="all",
            description="Will be `false` for all specified flags.\n\n**Deprecated** and will be removed in a future release.",
        ),
    ] = None
    """
    Will be `false` for all specified flags.
    
    **Deprecated** and will be removed in a future release.
    """

    message_details: typing.Optional[typing.Dict[str, GetEventsResponseEventsItemMessageDetailsMessageDetailsValue]] = (
        pydantic.Field(default=None)
    )
    """
    Only present if the specified `flag` is `"read"`.
    
    A set of data structures describing the messages that
    are being marked as unread with additional details to
    allow clients to update the `unread_msgs` data
    structure for these messages (which may not be
    otherwise known to the client).
    
    **Changes**: New in Zulip 5.0 (feature level 121). Previously,
    marking already read messages as unread was not
    supported by the Zulip API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
