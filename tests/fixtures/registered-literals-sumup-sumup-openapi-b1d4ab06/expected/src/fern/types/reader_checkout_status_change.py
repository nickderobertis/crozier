

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reader_checkout_status_change_payload import ReaderCheckoutStatusChangePayload


class ReaderCheckoutStatusChange(UniversalBaseModel):
    """
    The callback payload containing the status change of the Reader Checkout.
    """

    event_type: str = pydantic.Field()
    """
    Type of event.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event.
    """

    payload: ReaderCheckoutStatusChangePayload = pydantic.Field()
    """
    The event payload.
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp of the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
