



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .audio_field import AudioField
    from .audio_length_sec_field import AudioLengthSecField
    from .avg_audio_length_sec_field import AvgAudioLengthSecField
    from .best_podcasts_ln_url_field import BestPodcastsLnUrlField
    from .best_podcasts_response import BestPodcastsResponse
    from .country_field import CountryField
    from .curated_description_field import CuratedDescriptionField
    from .curated_id_field import CuratedIdField
    from .curated_list_full import CuratedListFull
    from .curated_list_search_result import CuratedListSearchResult
    from .curated_list_simple import CuratedListSimple
    from .curated_ln_url_field import CuratedLnUrlField
    from .curated_name_field import CuratedNameField
    from .curated_pub_date_ms_field import CuratedPubDateMsField
    from .curated_source_domain_field import CuratedSourceDomainField
    from .curated_source_url_field import CuratedSourceUrlField
    from .curated_total_podcasts_field import CuratedTotalPodcastsField
    from .custom_audio import CustomAudio
    from .delete_podcast_response import DeletePodcastResponse
    from .delete_podcast_response_status import DeletePodcastResponseStatus
    from .deleted_item import DeletedItem
    from .earliest_pub_date_ms_field import EarliestPubDateMsField
    from .email_field import EmailField
    from .episode_description_field import EpisodeDescriptionField
    from .episode_full import EpisodeFull
    from .episode_id_field import EpisodeIdField
    from .episode_image_field import EpisodeImageField
    from .episode_ln_edit_url_field import EpisodeLnEditUrlField
    from .episode_ln_url_field import EpisodeLnUrlField
    from .episode_minimum import EpisodeMinimum
    from .episode_name_field import EpisodeNameField
    from .episode_pub_date_ms_field import EpisodePubDateMsField
    from .episode_search_result import EpisodeSearchResult
    from .episode_search_result_podcast import EpisodeSearchResultPodcast
    from .episode_simple import EpisodeSimple
    from .episode_thumbnail_field import EpisodeThumbnailField
    from .explicit_field import ExplicitField
    from .genre import Genre
    from .genre_ids_field import GenreIdsField
    from .get_curated_podcasts_response import GetCuratedPodcastsResponse
    from .get_episode_recommendations_response import GetEpisodeRecommendationsResponse
    from .get_episodes_in_batch_form import GetEpisodesInBatchForm
    from .get_episodes_in_batch_response import GetEpisodesInBatchResponse
    from .get_genres_response import GetGenresResponse
    from .get_languages_response import GetLanguagesResponse
    from .get_podcast_recommendations_response import GetPodcastRecommendationsResponse
    from .get_podcasts_in_batch_form import GetPodcastsInBatchForm
    from .get_podcasts_in_batch_response import GetPodcastsInBatchResponse
    from .get_regions_response import GetRegionsResponse
    from .i_tunes_id_field import ITunesIdField
    from .image_field import ImageField
    from .is_claimed_field import IsClaimedField
    from .language_field import LanguageField
    from .latest_episode_id_field import LatestEpisodeIdField
    from .latest_pub_date_ms_field import LatestPubDateMsField
    from .link_field import LinkField
    from .listen_score_field import ListenScoreField
    from .listen_score_global_rank_field import ListenScoreGlobalRankField
    from .maybe_audio_invalid_field import MaybeAudioInvalidField
    from .next_episode_pub_date_field import NextEpisodePubDateField
    from .playlist_description_field import PlaylistDescriptionField
    from .playlist_id_field import PlaylistIdField
    from .playlist_image_field import PlaylistImageField
    from .playlist_item import PlaylistItem
    from .playlist_item_data import PlaylistItemData
    from .playlist_item_type import PlaylistItemType
    from .playlist_last_timestamp_ms_field import PlaylistLastTimestampMsField
    from .playlist_listennotes_url_field import PlaylistListennotesUrlField
    from .playlist_name_field import PlaylistNameField
    from .playlist_response import PlaylistResponse
    from .playlist_response_type import PlaylistResponseType
    from .playlist_thumbnail_field import PlaylistThumbnailField
    from .playlist_visibility_field import PlaylistVisibilityField
    from .playlists_response import PlaylistsResponse
    from .playlists_response_playlists_item import PlaylistsResponsePlaylistsItem
    from .podcast_audience_response import PodcastAudienceResponse
    from .podcast_audience_response_by_regions_item import PodcastAudienceResponseByRegionsItem
    from .podcast_description_field import PodcastDescriptionField
    from .podcast_domain_response import PodcastDomainResponse
    from .podcast_extra_field import PodcastExtraField
    from .podcast_full import PodcastFull
    from .podcast_id_field import PodcastIdField
    from .podcast_ln_url_field import PodcastLnUrlField
    from .podcast_looking_for_field import PodcastLookingForField
    from .podcast_minimum import PodcastMinimum
    from .podcast_minimum_rss import PodcastMinimumRss
    from .podcast_name_field import PodcastNameField
    from .podcast_search_result import PodcastSearchResult
    from .podcast_simple import PodcastSimple
    from .podcast_title_highlighted_field import PodcastTitleHighlightedField
    from .podcast_title_original_field import PodcastTitleOriginalField
    from .podcast_type_field import PodcastTypeField
    from .podcast_typeahead_result import PodcastTypeaheadResult
    from .post_podcasts_submit_rejected_payload import PostPodcastsSubmitRejectedPayload
    from .post_podcasts_submit_rejected_payload_podcast import PostPodcastsSubmitRejectedPayloadPodcast
    from .publisher_field import PublisherField
    from .publisher_highlighted_field import PublisherHighlightedField
    from .publisher_original_field import PublisherOriginalField
    from .related_searches_response import RelatedSearchesResponse
    from .rss_field import RssField
    from .search_response import SearchResponse
    from .search_response_results_item import SearchResponseResultsItem
    from .spell_check_response import SpellCheckResponse
    from .spell_check_response_tokens_item import SpellCheckResponseTokensItem
    from .submit_podcast_form import SubmitPodcastForm
    from .submit_podcast_response import SubmitPodcastResponse
    from .submit_podcast_response_status import SubmitPodcastResponseStatus
    from .thumbnail_field import ThumbnailField
    from .total_episodes_field import TotalEpisodesField
    from .transcript_field import TranscriptField
    from .trending_searches_response import TrendingSearchesResponse
    from .typeahead_response import TypeaheadResponse
    from .update_frequency_hours_field import UpdateFrequencyHoursField
    from .website_field import WebsiteField
_dynamic_imports: typing.Dict[str, str] = {
    "AudioField": ".audio_field",
    "AudioLengthSecField": ".audio_length_sec_field",
    "AvgAudioLengthSecField": ".avg_audio_length_sec_field",
    "BestPodcastsLnUrlField": ".best_podcasts_ln_url_field",
    "BestPodcastsResponse": ".best_podcasts_response",
    "CountryField": ".country_field",
    "CuratedDescriptionField": ".curated_description_field",
    "CuratedIdField": ".curated_id_field",
    "CuratedListFull": ".curated_list_full",
    "CuratedListSearchResult": ".curated_list_search_result",
    "CuratedListSimple": ".curated_list_simple",
    "CuratedLnUrlField": ".curated_ln_url_field",
    "CuratedNameField": ".curated_name_field",
    "CuratedPubDateMsField": ".curated_pub_date_ms_field",
    "CuratedSourceDomainField": ".curated_source_domain_field",
    "CuratedSourceUrlField": ".curated_source_url_field",
    "CuratedTotalPodcastsField": ".curated_total_podcasts_field",
    "CustomAudio": ".custom_audio",
    "DeletePodcastResponse": ".delete_podcast_response",
    "DeletePodcastResponseStatus": ".delete_podcast_response_status",
    "DeletedItem": ".deleted_item",
    "EarliestPubDateMsField": ".earliest_pub_date_ms_field",
    "EmailField": ".email_field",
    "EpisodeDescriptionField": ".episode_description_field",
    "EpisodeFull": ".episode_full",
    "EpisodeIdField": ".episode_id_field",
    "EpisodeImageField": ".episode_image_field",
    "EpisodeLnEditUrlField": ".episode_ln_edit_url_field",
    "EpisodeLnUrlField": ".episode_ln_url_field",
    "EpisodeMinimum": ".episode_minimum",
    "EpisodeNameField": ".episode_name_field",
    "EpisodePubDateMsField": ".episode_pub_date_ms_field",
    "EpisodeSearchResult": ".episode_search_result",
    "EpisodeSearchResultPodcast": ".episode_search_result_podcast",
    "EpisodeSimple": ".episode_simple",
    "EpisodeThumbnailField": ".episode_thumbnail_field",
    "ExplicitField": ".explicit_field",
    "Genre": ".genre",
    "GenreIdsField": ".genre_ids_field",
    "GetCuratedPodcastsResponse": ".get_curated_podcasts_response",
    "GetEpisodeRecommendationsResponse": ".get_episode_recommendations_response",
    "GetEpisodesInBatchForm": ".get_episodes_in_batch_form",
    "GetEpisodesInBatchResponse": ".get_episodes_in_batch_response",
    "GetGenresResponse": ".get_genres_response",
    "GetLanguagesResponse": ".get_languages_response",
    "GetPodcastRecommendationsResponse": ".get_podcast_recommendations_response",
    "GetPodcastsInBatchForm": ".get_podcasts_in_batch_form",
    "GetPodcastsInBatchResponse": ".get_podcasts_in_batch_response",
    "GetRegionsResponse": ".get_regions_response",
    "ITunesIdField": ".i_tunes_id_field",
    "ImageField": ".image_field",
    "IsClaimedField": ".is_claimed_field",
    "LanguageField": ".language_field",
    "LatestEpisodeIdField": ".latest_episode_id_field",
    "LatestPubDateMsField": ".latest_pub_date_ms_field",
    "LinkField": ".link_field",
    "ListenScoreField": ".listen_score_field",
    "ListenScoreGlobalRankField": ".listen_score_global_rank_field",
    "MaybeAudioInvalidField": ".maybe_audio_invalid_field",
    "NextEpisodePubDateField": ".next_episode_pub_date_field",
    "PlaylistDescriptionField": ".playlist_description_field",
    "PlaylistIdField": ".playlist_id_field",
    "PlaylistImageField": ".playlist_image_field",
    "PlaylistItem": ".playlist_item",
    "PlaylistItemData": ".playlist_item_data",
    "PlaylistItemType": ".playlist_item_type",
    "PlaylistLastTimestampMsField": ".playlist_last_timestamp_ms_field",
    "PlaylistListennotesUrlField": ".playlist_listennotes_url_field",
    "PlaylistNameField": ".playlist_name_field",
    "PlaylistResponse": ".playlist_response",
    "PlaylistResponseType": ".playlist_response_type",
    "PlaylistThumbnailField": ".playlist_thumbnail_field",
    "PlaylistVisibilityField": ".playlist_visibility_field",
    "PlaylistsResponse": ".playlists_response",
    "PlaylistsResponsePlaylistsItem": ".playlists_response_playlists_item",
    "PodcastAudienceResponse": ".podcast_audience_response",
    "PodcastAudienceResponseByRegionsItem": ".podcast_audience_response_by_regions_item",
    "PodcastDescriptionField": ".podcast_description_field",
    "PodcastDomainResponse": ".podcast_domain_response",
    "PodcastExtraField": ".podcast_extra_field",
    "PodcastFull": ".podcast_full",
    "PodcastIdField": ".podcast_id_field",
    "PodcastLnUrlField": ".podcast_ln_url_field",
    "PodcastLookingForField": ".podcast_looking_for_field",
    "PodcastMinimum": ".podcast_minimum",
    "PodcastMinimumRss": ".podcast_minimum_rss",
    "PodcastNameField": ".podcast_name_field",
    "PodcastSearchResult": ".podcast_search_result",
    "PodcastSimple": ".podcast_simple",
    "PodcastTitleHighlightedField": ".podcast_title_highlighted_field",
    "PodcastTitleOriginalField": ".podcast_title_original_field",
    "PodcastTypeField": ".podcast_type_field",
    "PodcastTypeaheadResult": ".podcast_typeahead_result",
    "PostPodcastsSubmitRejectedPayload": ".post_podcasts_submit_rejected_payload",
    "PostPodcastsSubmitRejectedPayloadPodcast": ".post_podcasts_submit_rejected_payload_podcast",
    "PublisherField": ".publisher_field",
    "PublisherHighlightedField": ".publisher_highlighted_field",
    "PublisherOriginalField": ".publisher_original_field",
    "RelatedSearchesResponse": ".related_searches_response",
    "RssField": ".rss_field",
    "SearchResponse": ".search_response",
    "SearchResponseResultsItem": ".search_response_results_item",
    "SpellCheckResponse": ".spell_check_response",
    "SpellCheckResponseTokensItem": ".spell_check_response_tokens_item",
    "SubmitPodcastForm": ".submit_podcast_form",
    "SubmitPodcastResponse": ".submit_podcast_response",
    "SubmitPodcastResponseStatus": ".submit_podcast_response_status",
    "ThumbnailField": ".thumbnail_field",
    "TotalEpisodesField": ".total_episodes_field",
    "TranscriptField": ".transcript_field",
    "TrendingSearchesResponse": ".trending_searches_response",
    "TypeaheadResponse": ".typeahead_response",
    "UpdateFrequencyHoursField": ".update_frequency_hours_field",
    "WebsiteField": ".website_field",
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
    "AudioField",
    "AudioLengthSecField",
    "AvgAudioLengthSecField",
    "BestPodcastsLnUrlField",
    "BestPodcastsResponse",
    "CountryField",
    "CuratedDescriptionField",
    "CuratedIdField",
    "CuratedListFull",
    "CuratedListSearchResult",
    "CuratedListSimple",
    "CuratedLnUrlField",
    "CuratedNameField",
    "CuratedPubDateMsField",
    "CuratedSourceDomainField",
    "CuratedSourceUrlField",
    "CuratedTotalPodcastsField",
    "CustomAudio",
    "DeletePodcastResponse",
    "DeletePodcastResponseStatus",
    "DeletedItem",
    "EarliestPubDateMsField",
    "EmailField",
    "EpisodeDescriptionField",
    "EpisodeFull",
    "EpisodeIdField",
    "EpisodeImageField",
    "EpisodeLnEditUrlField",
    "EpisodeLnUrlField",
    "EpisodeMinimum",
    "EpisodeNameField",
    "EpisodePubDateMsField",
    "EpisodeSearchResult",
    "EpisodeSearchResultPodcast",
    "EpisodeSimple",
    "EpisodeThumbnailField",
    "ExplicitField",
    "Genre",
    "GenreIdsField",
    "GetCuratedPodcastsResponse",
    "GetEpisodeRecommendationsResponse",
    "GetEpisodesInBatchForm",
    "GetEpisodesInBatchResponse",
    "GetGenresResponse",
    "GetLanguagesResponse",
    "GetPodcastRecommendationsResponse",
    "GetPodcastsInBatchForm",
    "GetPodcastsInBatchResponse",
    "GetRegionsResponse",
    "ITunesIdField",
    "ImageField",
    "IsClaimedField",
    "LanguageField",
    "LatestEpisodeIdField",
    "LatestPubDateMsField",
    "LinkField",
    "ListenScoreField",
    "ListenScoreGlobalRankField",
    "MaybeAudioInvalidField",
    "NextEpisodePubDateField",
    "PlaylistDescriptionField",
    "PlaylistIdField",
    "PlaylistImageField",
    "PlaylistItem",
    "PlaylistItemData",
    "PlaylistItemType",
    "PlaylistLastTimestampMsField",
    "PlaylistListennotesUrlField",
    "PlaylistNameField",
    "PlaylistResponse",
    "PlaylistResponseType",
    "PlaylistThumbnailField",
    "PlaylistVisibilityField",
    "PlaylistsResponse",
    "PlaylistsResponsePlaylistsItem",
    "PodcastAudienceResponse",
    "PodcastAudienceResponseByRegionsItem",
    "PodcastDescriptionField",
    "PodcastDomainResponse",
    "PodcastExtraField",
    "PodcastFull",
    "PodcastIdField",
    "PodcastLnUrlField",
    "PodcastLookingForField",
    "PodcastMinimum",
    "PodcastMinimumRss",
    "PodcastNameField",
    "PodcastSearchResult",
    "PodcastSimple",
    "PodcastTitleHighlightedField",
    "PodcastTitleOriginalField",
    "PodcastTypeField",
    "PodcastTypeaheadResult",
    "PostPodcastsSubmitRejectedPayload",
    "PostPodcastsSubmitRejectedPayloadPodcast",
    "PublisherField",
    "PublisherHighlightedField",
    "PublisherOriginalField",
    "RelatedSearchesResponse",
    "RssField",
    "SearchResponse",
    "SearchResponseResultsItem",
    "SpellCheckResponse",
    "SpellCheckResponseTokensItem",
    "SubmitPodcastForm",
    "SubmitPodcastResponse",
    "SubmitPodcastResponseStatus",
    "ThumbnailField",
    "TotalEpisodesField",
    "TranscriptField",
    "TrendingSearchesResponse",
    "TypeaheadResponse",
    "UpdateFrequencyHoursField",
    "WebsiteField",
]
