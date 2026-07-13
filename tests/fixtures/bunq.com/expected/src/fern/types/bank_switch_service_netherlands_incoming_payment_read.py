

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .bank_switch_service_netherlands_incoming import BankSwitchServiceNetherlandsIncoming


class BankSwitchServiceNetherlandsIncomingPaymentRead(UniversalBaseModel):
    bank_switch_service: typing.Optional[BankSwitchServiceNetherlandsIncoming] = pydantic.Field(default=None)
    """
    The bank switch service details.
    """

    payment: typing.Optional["Payment"] = pydantic.Field(default=None)
    """
    The payment made using bank switch service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment

update_forward_refs(BankSwitchServiceNetherlandsIncomingPaymentRead)
