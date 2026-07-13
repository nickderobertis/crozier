

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .event_object import EventObject


class InsightEventListing(UniversalBaseModel):
    action: typing.Optional[str] = pydantic.Field(default=None)
    """
    The performed action. Can be: CREATE or UPDATE.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the event's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the event.
    """

    monetary_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the monetary account the event applied to (if it was a monetary account event).
    """

    object: typing.Optional[EventObject] = pydantic.Field(default=None)
    """
    The details of the external object the event was created for.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event status. Can be: FINALIZED or AWAITING_REPLY. An example of FINALIZED event is a payment received event, while an AWAITING_REPLY event is a request received event.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the event's last update.
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user the event applied to (if it was a user event).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(InsightEventListing)
