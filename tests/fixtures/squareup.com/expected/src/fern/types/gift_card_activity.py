

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gift_card_activity_activate import GiftCardActivityActivate
from .gift_card_activity_adjust_decrement import GiftCardActivityAdjustDecrement
from .gift_card_activity_adjust_increment import GiftCardActivityAdjustIncrement
from .gift_card_activity_block import GiftCardActivityBlock
from .gift_card_activity_clear_balance import GiftCardActivityClearBalance
from .gift_card_activity_deactivate import GiftCardActivityDeactivate
from .gift_card_activity_import import GiftCardActivityImport
from .gift_card_activity_import_reversal import GiftCardActivityImportReversal
from .gift_card_activity_load import GiftCardActivityLoad
from .gift_card_activity_redeem import GiftCardActivityRedeem
from .gift_card_activity_refund import GiftCardActivityRefund
from .gift_card_activity_unblock import GiftCardActivityUnblock
from .gift_card_activity_unlinked_activity_refund import GiftCardActivityUnlinkedActivityRefund
from .money import Money
from .type import Type


class GiftCardActivity(UniversalBaseModel):
    """
    Represents an action performed on a gift card that affects its state or balance.
    """

    activate_activity_details: typing.Optional[GiftCardActivityActivate] = None
    adjust_decrement_activity_details: typing.Optional[GiftCardActivityAdjustDecrement] = None
    adjust_increment_activity_details: typing.Optional[GiftCardActivityAdjustIncrement] = None
    block_activity_details: typing.Optional[GiftCardActivityBlock] = None
    clear_balance_activity_details: typing.Optional[GiftCardActivityClearBalance] = None
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the gift card activity was created, in RFC 3339 format.
    """

    deactivate_activity_details: typing.Optional[GiftCardActivityDeactivate] = None
    gift_card_balance_money: typing.Optional[Money] = None
    gift_card_gan: typing.Optional[str] = pydantic.Field(default=None)
    """
    The gift card GAN. The GAN is not required if `gift_card_id` is present.
    """

    gift_card_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The gift card ID. The ID is not required if a GAN is present.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the gift card activity.
    """

    import_activity_details: typing.Optional[GiftCardActivityImport] = None
    import_reversal_activity_details: typing.Optional[GiftCardActivityImportReversal] = None
    load_activity_details: typing.Optional[GiftCardActivityLoad] = None
    location_id: str = pydantic.Field()
    """
    The ID of the location at which the activity occurred.
    """

    redeem_activity_details: typing.Optional[GiftCardActivityRedeem] = None
    refund_activity_details: typing.Optional[GiftCardActivityRefund] = None
    type: Type
    unblock_activity_details: typing.Optional[GiftCardActivityUnblock] = None
    unlinked_activity_refund_activity_details: typing.Optional[GiftCardActivityUnlinkedActivityRefund] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
