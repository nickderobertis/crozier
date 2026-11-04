



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .contributor_get_by_id_response import ContributorGetByIdResponse
    from .contributor_get_by_id_response_reviews_item import ContributorGetByIdResponseReviewsItem
    from .contributor_get_by_id_response_reviews_item_chipset_variant import (
        ContributorGetByIdResponseReviewsItemChipsetVariant,
    )
    from .contributor_get_by_id_response_reviews_item_graphics_settings import (
        ContributorGetByIdResponseReviewsItemGraphicsSettings,
    )
    from .contributor_get_by_id_response_reviews_item_mac_config import ContributorGetByIdResponseReviewsItemMacConfig
    from .contributor_get_by_id_response_reviews_item_performance import (
        ContributorGetByIdResponseReviewsItemPerformance,
    )
    from .contributor_get_by_id_response_reviews_item_play_method import ContributorGetByIdResponseReviewsItemPlayMethod
    from .contributor_get_by_id_response_reviews_item_translation_layer import (
        ContributorGetByIdResponseReviewsItemTranslationLayer,
    )
    from .contributor_get_top_contributors_response import ContributorGetTopContributorsResponse
    from .contributor_get_top_contributors_response_contributors_item import (
        ContributorGetTopContributorsResponseContributorsItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ContributorGetByIdResponse": ".contributor_get_by_id_response",
    "ContributorGetByIdResponseReviewsItem": ".contributor_get_by_id_response_reviews_item",
    "ContributorGetByIdResponseReviewsItemChipsetVariant": ".contributor_get_by_id_response_reviews_item_chipset_variant",
    "ContributorGetByIdResponseReviewsItemGraphicsSettings": ".contributor_get_by_id_response_reviews_item_graphics_settings",
    "ContributorGetByIdResponseReviewsItemMacConfig": ".contributor_get_by_id_response_reviews_item_mac_config",
    "ContributorGetByIdResponseReviewsItemPerformance": ".contributor_get_by_id_response_reviews_item_performance",
    "ContributorGetByIdResponseReviewsItemPlayMethod": ".contributor_get_by_id_response_reviews_item_play_method",
    "ContributorGetByIdResponseReviewsItemTranslationLayer": ".contributor_get_by_id_response_reviews_item_translation_layer",
    "ContributorGetTopContributorsResponse": ".contributor_get_top_contributors_response",
    "ContributorGetTopContributorsResponseContributorsItem": ".contributor_get_top_contributors_response_contributors_item",
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
    "ContributorGetByIdResponse",
    "ContributorGetByIdResponseReviewsItem",
    "ContributorGetByIdResponseReviewsItemChipsetVariant",
    "ContributorGetByIdResponseReviewsItemGraphicsSettings",
    "ContributorGetByIdResponseReviewsItemMacConfig",
    "ContributorGetByIdResponseReviewsItemPerformance",
    "ContributorGetByIdResponseReviewsItemPlayMethod",
    "ContributorGetByIdResponseReviewsItemTranslationLayer",
    "ContributorGetTopContributorsResponse",
    "ContributorGetTopContributorsResponseContributorsItem",
]
