



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .game_get_by_id_response import GameGetByIdResponse
    from .game_get_by_id_response_game import GameGetByIdResponseGame
    from .game_get_by_id_response_game_aggregated_performance import GameGetByIdResponseGameAggregatedPerformance
    from .game_get_by_id_response_game_source_links_item import GameGetByIdResponseGameSourceLinksItem
    from .game_get_by_id_response_game_source_links_item_source import GameGetByIdResponseGameSourceLinksItemSource
    from .game_get_by_id_response_reviews_item import GameGetByIdResponseReviewsItem
    from .game_get_by_id_response_reviews_item_chipset_variant import GameGetByIdResponseReviewsItemChipsetVariant
    from .game_get_by_id_response_reviews_item_graphics_settings import GameGetByIdResponseReviewsItemGraphicsSettings
    from .game_get_by_id_response_reviews_item_mac_config import GameGetByIdResponseReviewsItemMacConfig
    from .game_get_by_id_response_reviews_item_performance import GameGetByIdResponseReviewsItemPerformance
    from .game_get_by_id_response_reviews_item_play_method import GameGetByIdResponseReviewsItemPlayMethod
    from .game_get_by_id_response_reviews_item_translation_layer import GameGetByIdResponseReviewsItemTranslationLayer
    from .game_get_by_id_response_stats import GameGetByIdResponseStats
    from .game_get_by_id_response_stats_methods import GameGetByIdResponseStatsMethods
    from .game_get_by_id_response_stats_translation_layers_value import GameGetByIdResponseStatsTranslationLayersValue
    from .game_get_cover_art_response import GameGetCoverArtResponse
    from .game_get_filter_counts_request_chipset import GameGetFilterCountsRequestChipset
    from .game_get_filter_counts_request_chipset_variant import GameGetFilterCountsRequestChipsetVariant
    from .game_get_filter_counts_request_play_method import GameGetFilterCountsRequestPlayMethod
    from .game_get_filter_counts_response import GameGetFilterCountsResponse
    from .game_get_games_request_chipset import GameGetGamesRequestChipset
    from .game_get_games_request_chipset_variant import GameGetGamesRequestChipsetVariant
    from .game_get_games_request_performance import GameGetGamesRequestPerformance
    from .game_get_games_request_play_method import GameGetGamesRequestPlayMethod
    from .game_get_games_response import GameGetGamesResponse
    from .game_get_games_response_games_item import GameGetGamesResponseGamesItem
    from .game_get_games_response_games_item_performance_rating import GameGetGamesResponseGamesItemPerformanceRating
    from .game_get_prices_response import GameGetPricesResponse
    from .game_get_prices_response_prices import GameGetPricesResponsePrices
    from .game_get_screenshot_signed_urls_response_item import GameGetScreenshotSignedUrlsResponseItem
    from .game_get_sitemap_entries_response_item import GameGetSitemapEntriesResponseItem
    from .game_search_response_item import GameSearchResponseItem
    from .game_search_response_item_source import GameSearchResponseItemSource
_dynamic_imports: typing.Dict[str, str] = {
    "GameGetByIdResponse": ".game_get_by_id_response",
    "GameGetByIdResponseGame": ".game_get_by_id_response_game",
    "GameGetByIdResponseGameAggregatedPerformance": ".game_get_by_id_response_game_aggregated_performance",
    "GameGetByIdResponseGameSourceLinksItem": ".game_get_by_id_response_game_source_links_item",
    "GameGetByIdResponseGameSourceLinksItemSource": ".game_get_by_id_response_game_source_links_item_source",
    "GameGetByIdResponseReviewsItem": ".game_get_by_id_response_reviews_item",
    "GameGetByIdResponseReviewsItemChipsetVariant": ".game_get_by_id_response_reviews_item_chipset_variant",
    "GameGetByIdResponseReviewsItemGraphicsSettings": ".game_get_by_id_response_reviews_item_graphics_settings",
    "GameGetByIdResponseReviewsItemMacConfig": ".game_get_by_id_response_reviews_item_mac_config",
    "GameGetByIdResponseReviewsItemPerformance": ".game_get_by_id_response_reviews_item_performance",
    "GameGetByIdResponseReviewsItemPlayMethod": ".game_get_by_id_response_reviews_item_play_method",
    "GameGetByIdResponseReviewsItemTranslationLayer": ".game_get_by_id_response_reviews_item_translation_layer",
    "GameGetByIdResponseStats": ".game_get_by_id_response_stats",
    "GameGetByIdResponseStatsMethods": ".game_get_by_id_response_stats_methods",
    "GameGetByIdResponseStatsTranslationLayersValue": ".game_get_by_id_response_stats_translation_layers_value",
    "GameGetCoverArtResponse": ".game_get_cover_art_response",
    "GameGetFilterCountsRequestChipset": ".game_get_filter_counts_request_chipset",
    "GameGetFilterCountsRequestChipsetVariant": ".game_get_filter_counts_request_chipset_variant",
    "GameGetFilterCountsRequestPlayMethod": ".game_get_filter_counts_request_play_method",
    "GameGetFilterCountsResponse": ".game_get_filter_counts_response",
    "GameGetGamesRequestChipset": ".game_get_games_request_chipset",
    "GameGetGamesRequestChipsetVariant": ".game_get_games_request_chipset_variant",
    "GameGetGamesRequestPerformance": ".game_get_games_request_performance",
    "GameGetGamesRequestPlayMethod": ".game_get_games_request_play_method",
    "GameGetGamesResponse": ".game_get_games_response",
    "GameGetGamesResponseGamesItem": ".game_get_games_response_games_item",
    "GameGetGamesResponseGamesItemPerformanceRating": ".game_get_games_response_games_item_performance_rating",
    "GameGetPricesResponse": ".game_get_prices_response",
    "GameGetPricesResponsePrices": ".game_get_prices_response_prices",
    "GameGetScreenshotSignedUrlsResponseItem": ".game_get_screenshot_signed_urls_response_item",
    "GameGetSitemapEntriesResponseItem": ".game_get_sitemap_entries_response_item",
    "GameSearchResponseItem": ".game_search_response_item",
    "GameSearchResponseItemSource": ".game_search_response_item_source",
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
    "GameGetByIdResponse",
    "GameGetByIdResponseGame",
    "GameGetByIdResponseGameAggregatedPerformance",
    "GameGetByIdResponseGameSourceLinksItem",
    "GameGetByIdResponseGameSourceLinksItemSource",
    "GameGetByIdResponseReviewsItem",
    "GameGetByIdResponseReviewsItemChipsetVariant",
    "GameGetByIdResponseReviewsItemGraphicsSettings",
    "GameGetByIdResponseReviewsItemMacConfig",
    "GameGetByIdResponseReviewsItemPerformance",
    "GameGetByIdResponseReviewsItemPlayMethod",
    "GameGetByIdResponseReviewsItemTranslationLayer",
    "GameGetByIdResponseStats",
    "GameGetByIdResponseStatsMethods",
    "GameGetByIdResponseStatsTranslationLayersValue",
    "GameGetCoverArtResponse",
    "GameGetFilterCountsRequestChipset",
    "GameGetFilterCountsRequestChipsetVariant",
    "GameGetFilterCountsRequestPlayMethod",
    "GameGetFilterCountsResponse",
    "GameGetGamesRequestChipset",
    "GameGetGamesRequestChipsetVariant",
    "GameGetGamesRequestPerformance",
    "GameGetGamesRequestPlayMethod",
    "GameGetGamesResponse",
    "GameGetGamesResponseGamesItem",
    "GameGetGamesResponseGamesItemPerformanceRating",
    "GameGetPricesResponse",
    "GameGetPricesResponsePrices",
    "GameGetScreenshotSignedUrlsResponseItem",
    "GameGetSitemapEntriesResponseItem",
    "GameSearchResponseItem",
    "GameSearchResponseItemSource",
]
