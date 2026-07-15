

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookSubscription(UniversalBaseModel):
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date and time the webhook subscription was created downstream
    """

    downstream_event_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of downstream Events this connection is subscribed to
    """

    downstream_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the downstream service
    """

    execute_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL the downstream is sending to when the event is triggered
    """

    unify_event_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of Unify Events this connection is subscribed to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
