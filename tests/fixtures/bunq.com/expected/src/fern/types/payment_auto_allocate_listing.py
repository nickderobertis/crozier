

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .amount import Amount


class PaymentAutoAllocateListing(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the PaymentAutoAllocate was created.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the PaymentAutoAllocate.
    """

    payment: typing.Optional["Payment"] = pydantic.Field(default=None)
    """
    The payment that was used to define the triggers for this payment auto allocate.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status.
    """

    trigger_amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount on which this payment auto allocate will be triggered.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the PaymentAutoAllocate was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment

update_forward_refs(PaymentAutoAllocateListing)
