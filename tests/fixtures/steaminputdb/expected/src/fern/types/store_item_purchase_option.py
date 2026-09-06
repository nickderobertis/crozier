

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_purchase_option_discount import StoreItemPurchaseOptionDiscount
from .store_item_purchase_option_recurrence_info import StoreItemPurchaseOptionRecurrenceInfo


class StoreItemPurchaseOption(UniversalBaseModel):
    active_discounts: typing.Optional[typing.List[StoreItemPurchaseOptionDiscount]] = None
    bundle_discount_pct: typing.Optional[int] = None
    bundleid: typing.Optional[int] = None
    discount_pct: typing.Optional[int] = None
    final_price_in_cents: typing.Optional[int] = None
    formatted_final_price: typing.Optional[str] = None
    formatted_original_price: typing.Optional[str] = None
    formatted_price_before_bundle_discount: typing.Optional[str] = None
    free_to_keep_ends: typing.Optional[int] = None
    hide_discount_pct_for_compliance: typing.Optional[bool] = None
    included_game_count: typing.Optional[int] = None
    is_commercial_license: typing.Optional[bool] = None
    is_free_to_keep: typing.Optional[bool] = None
    lowest_recent_price_in_cents: typing.Optional[int] = None
    must_purchase_as_set: typing.Optional[bool] = None
    original_price_in_cents: typing.Optional[int] = None
    packageid: typing.Optional[int] = None
    price_before_bundle_discount: typing.Optional[int] = None
    purchase_option_name: typing.Optional[str] = None
    recurrence_info: typing.Optional[StoreItemPurchaseOptionRecurrenceInfo] = None
    requires_shipping: typing.Optional[bool] = None
    should_suppress_discount_pct: typing.Optional[bool] = None
    user_can_purchase_as_gift: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
