



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .check_new_episodes_response import CheckNewEpisodesResponse
    from .find_episode_response import FindEpisodeResponse
    from .get_episode_downloads_response import GetEpisodeDownloadsResponse
    from .get_feeds_from_opml_text_response import GetFeedsFromOpmlTextResponse
    from .get_feeds_from_opml_text_response_feeds_item import GetFeedsFromOpmlTextResponseFeedsItem
    from .get_podcast_feed_response import GetPodcastFeedResponse
    from .quick_match_episodes_response import QuickMatchEpisodesResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CheckNewEpisodesResponse": ".check_new_episodes_response",
    "FindEpisodeResponse": ".find_episode_response",
    "GetEpisodeDownloadsResponse": ".get_episode_downloads_response",
    "GetFeedsFromOpmlTextResponse": ".get_feeds_from_opml_text_response",
    "GetFeedsFromOpmlTextResponseFeedsItem": ".get_feeds_from_opml_text_response_feeds_item",
    "GetPodcastFeedResponse": ".get_podcast_feed_response",
    "QuickMatchEpisodesResponse": ".quick_match_episodes_response",
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
    "CheckNewEpisodesResponse",
    "FindEpisodeResponse",
    "GetEpisodeDownloadsResponse",
    "GetFeedsFromOpmlTextResponse",
    "GetFeedsFromOpmlTextResponseFeedsItem",
    "GetPodcastFeedResponse",
    "QuickMatchEpisodesResponse",
]
