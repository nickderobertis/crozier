



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .review_create_request_graphics_settings import ReviewCreateRequestGraphicsSettings
    from .review_create_request_performance import ReviewCreateRequestPerformance
    from .review_create_request_play_method import ReviewCreateRequestPlayMethod
    from .review_create_request_translation_layer import ReviewCreateRequestTranslationLayer
    from .review_create_response import ReviewCreateResponse
    from .review_create_response_review import ReviewCreateResponseReview
    from .review_create_response_review_chipset_variant import ReviewCreateResponseReviewChipsetVariant
    from .review_create_response_review_graphics_settings import ReviewCreateResponseReviewGraphicsSettings
    from .review_create_response_review_performance import ReviewCreateResponseReviewPerformance
    from .review_create_response_review_play_method import ReviewCreateResponseReviewPlayMethod
    from .review_create_response_review_translation_layer import ReviewCreateResponseReviewTranslationLayer
    from .review_delete_review_response import ReviewDeleteReviewResponse
    from .review_get_upload_url_response import ReviewGetUploadUrlResponse
    from .review_list_mine_response_item import ReviewListMineResponseItem
    from .review_list_mine_response_item_chipset_variant import ReviewListMineResponseItemChipsetVariant
    from .review_list_mine_response_item_graphics_settings import ReviewListMineResponseItemGraphicsSettings
    from .review_list_mine_response_item_mac_config import ReviewListMineResponseItemMacConfig
    from .review_list_mine_response_item_performance import ReviewListMineResponseItemPerformance
    from .review_list_mine_response_item_play_method import ReviewListMineResponseItemPlayMethod
    from .review_list_mine_response_item_translation_layer import ReviewListMineResponseItemTranslationLayer
    from .review_update_review_request_performance import ReviewUpdateReviewRequestPerformance
    from .review_update_review_response import ReviewUpdateReviewResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ReviewCreateRequestGraphicsSettings": ".review_create_request_graphics_settings",
    "ReviewCreateRequestPerformance": ".review_create_request_performance",
    "ReviewCreateRequestPlayMethod": ".review_create_request_play_method",
    "ReviewCreateRequestTranslationLayer": ".review_create_request_translation_layer",
    "ReviewCreateResponse": ".review_create_response",
    "ReviewCreateResponseReview": ".review_create_response_review",
    "ReviewCreateResponseReviewChipsetVariant": ".review_create_response_review_chipset_variant",
    "ReviewCreateResponseReviewGraphicsSettings": ".review_create_response_review_graphics_settings",
    "ReviewCreateResponseReviewPerformance": ".review_create_response_review_performance",
    "ReviewCreateResponseReviewPlayMethod": ".review_create_response_review_play_method",
    "ReviewCreateResponseReviewTranslationLayer": ".review_create_response_review_translation_layer",
    "ReviewDeleteReviewResponse": ".review_delete_review_response",
    "ReviewGetUploadUrlResponse": ".review_get_upload_url_response",
    "ReviewListMineResponseItem": ".review_list_mine_response_item",
    "ReviewListMineResponseItemChipsetVariant": ".review_list_mine_response_item_chipset_variant",
    "ReviewListMineResponseItemGraphicsSettings": ".review_list_mine_response_item_graphics_settings",
    "ReviewListMineResponseItemMacConfig": ".review_list_mine_response_item_mac_config",
    "ReviewListMineResponseItemPerformance": ".review_list_mine_response_item_performance",
    "ReviewListMineResponseItemPlayMethod": ".review_list_mine_response_item_play_method",
    "ReviewListMineResponseItemTranslationLayer": ".review_list_mine_response_item_translation_layer",
    "ReviewUpdateReviewRequestPerformance": ".review_update_review_request_performance",
    "ReviewUpdateReviewResponse": ".review_update_review_response",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "ReviewCreateRequestGraphicsSettings",
    "ReviewCreateRequestPerformance",
    "ReviewCreateRequestPlayMethod",
    "ReviewCreateRequestTranslationLayer",
    "ReviewCreateResponse",
    "ReviewCreateResponseReview",
    "ReviewCreateResponseReviewChipsetVariant",
    "ReviewCreateResponseReviewGraphicsSettings",
    "ReviewCreateResponseReviewPerformance",
    "ReviewCreateResponseReviewPlayMethod",
    "ReviewCreateResponseReviewTranslationLayer",
    "ReviewDeleteReviewResponse",
    "ReviewGetUploadUrlResponse",
    "ReviewListMineResponseItem",
    "ReviewListMineResponseItemChipsetVariant",
    "ReviewListMineResponseItemGraphicsSettings",
    "ReviewListMineResponseItemMacConfig",
    "ReviewListMineResponseItemPerformance",
    "ReviewListMineResponseItemPlayMethod",
    "ReviewListMineResponseItemTranslationLayer",
    "ReviewUpdateReviewRequestPerformance",
    "ReviewUpdateReviewResponse",
]
