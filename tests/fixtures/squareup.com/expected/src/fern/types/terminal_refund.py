

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class TerminalRefund(UniversalBaseModel):
    """ """

    amount_money: Money
    app_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the application that created the refund.
    """

    cancel_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if the status is `CANCELED`.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the `TerminalRefund` was created, as an RFC 3339 timestamp.
    """

    deadline_duration: typing.Optional[str] = pydantic.Field(default=None)
    """
    The RFC 3339 duration, after which the refund is automatically canceled.
    A `TerminalRefund` that is `PENDING` is automatically `CANCELED` and has a cancellation reason
    of `TIMED_OUT`.
    
    Default: 5 minutes from creation.
    
    Maximum: 5 minutes
    """

    device_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the device intended for this `TerminalRefund`.
    The Id can be retrieved from /v2/devices api.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for this `TerminalRefund`.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location of the device where the `TerminalRefund` was directed.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reference to the Square order ID for the payment identified by the `payment_id`.
    """

    payment_id: str = pydantic.Field()
    """
    The unique ID of the payment being refunded.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the reason for the refund.
    Note: maximum 192 characters
    """

    refund_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reference to the payment refund created by completing this `TerminalRefund`.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the `TerminalRefund`.
    Options: `PENDING`, `IN_PROGRESS`, `CANCELED`, or `COMPLETED`.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the `TerminalRefund` was last updated, as an RFC 3339 timestamp.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
