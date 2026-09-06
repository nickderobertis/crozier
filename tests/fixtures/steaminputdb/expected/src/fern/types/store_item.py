

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .store_browse_filter_failure import StoreBrowseFilterFailure
from .store_game_rating import StoreGameRating
from .store_item_assets import StoreItemAssets
from .store_item_basic_info import StoreItemBasicInfo
from .store_item_categories import StoreItemCategories
from .store_item_free_weekend import StoreItemFreeWeekend
from .store_item_link import StoreItemLink
from .store_item_platforms import StoreItemPlatforms
from .store_item_purchase_option import StoreItemPurchaseOption
from .store_item_related_items import StoreItemRelatedItems
from .store_item_release_info import StoreItemReleaseInfo
from .store_item_reviews import StoreItemReviews
from .store_item_screenshots import StoreItemScreenshots
from .store_item_supported_language import StoreItemSupportedLanguage
from .store_item_tag import StoreItemTag
from .store_item_trailers import StoreItemTrailers


class StoreItem(UniversalBaseModel):
    accessories: typing.Optional[typing.List[StoreItemPurchaseOption]] = None
    appid: typing.Optional[int] = None
    assets: typing.Optional[StoreItemAssets] = None
    assets_without_overrides: typing.Optional[StoreItemAssets] = None
    basic_info: typing.Optional[StoreItemBasicInfo] = None
    best_purchase_option: typing.Optional[StoreItemPurchaseOption] = None
    categories: typing.Optional[StoreItemCategories] = None
    content_descriptorids: typing.Optional[typing.List[int]] = None
    free_weekend: typing.Optional[StoreItemFreeWeekend] = None
    full_description: typing.Optional[str] = None
    game_count: typing.Optional[int] = None
    game_rating: typing.Optional[StoreGameRating] = None
    id: typing.Optional[int] = None
    included_appids: typing.Optional[typing.List[int]] = None
    included_items: typing.Optional["StoreItemIncludedItems"] = None
    included_types: typing.Optional[typing.List[int]] = None
    internal_name: typing.Optional[str] = None
    invalid_purchase_options: typing.Optional[typing.List[StoreItemPurchaseOption]] = None
    is_coming_soon: typing.Optional[bool] = None
    is_early_access: typing.Optional[bool] = None
    is_free: typing.Optional[bool] = None
    is_free_temporarily: typing.Optional[bool] = None
    item_type: typing.Optional[int] = None
    links: typing.Optional[typing.List[StoreItemLink]] = None
    name: typing.Optional[str] = None
    platforms: typing.Optional[StoreItemPlatforms] = None
    purchase_options: typing.Optional[typing.List[StoreItemPurchaseOption]] = None
    related_items: typing.Optional[StoreItemRelatedItems] = None
    release: typing.Optional[StoreItemReleaseInfo] = None
    reviews: typing.Optional[StoreItemReviews] = None
    screenshots: typing.Optional[StoreItemScreenshots] = None
    self_purchase_option: typing.Optional[StoreItemPurchaseOption] = None
    store_url_path: typing.Optional[str] = None
    store_url_path_override: typing.Optional[str] = None
    success: typing.Optional[int] = None
    supported_languages: typing.Optional[typing.List[StoreItemSupportedLanguage]] = None
    tagids: typing.Optional[typing.List[int]] = None
    tags: typing.Optional[typing.List[StoreItemTag]] = None
    trailers: typing.Optional[StoreItemTrailers] = None
    type: typing.Optional[int] = None
    unlisted: typing.Optional[bool] = None
    unvailable_for_country_restriction: typing.Optional[bool] = None
    user_filter_failure: typing.Optional[StoreBrowseFilterFailure] = None
    visible: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .store_item_included_items import StoreItemIncludedItems

update_forward_refs(StoreItem, StoreItemIncludedItems=StoreItemIncludedItems)
