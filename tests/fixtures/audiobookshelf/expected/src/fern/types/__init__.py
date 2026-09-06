



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .added_at import AddedAt
    from .apprise_api_url import AppriseApiUrl
    from .audio_file import AudioFile
    from .audio_meta_tags import AudioMetaTags
    from .audio_track import AudioTrack
    from .author import Author
    from .author_asin import AuthorAsin
    from .author_description import AuthorDescription
    from .author_expanded import AuthorExpanded
    from .author_id import AuthorId
    from .author_image_path import AuthorImagePath
    from .author_merged import AuthorMerged
    from .author_name import AuthorName
    from .author_search_name import AuthorSearchName
    from .author_series import AuthorSeries
    from .author_updated import AuthorUpdated
    from .auto_download_episodes import AutoDownloadEpisodes
    from .body_template import BodyTemplate
    from .book_chapter import BookChapter
    from .book_cover_path import BookCoverPath
    from .book_metadata_base import BookMetadataBase
    from .book_metadata_minified import BookMetadataMinified
    from .book_minified import BookMinified
    from .collapse_series import CollapseSeries
    from .created_at import CreatedAt
    from .duration_sec import DurationSec
    from .email_settings import EmailSettings
    from .enabled import Enabled
    from .ereader_device_object import EreaderDeviceObject
    from .ereader_device_object_availability_option import EreaderDeviceObjectAvailabilityOption
    from .ereader_name import EreaderName
    from .file_metadata import FileMetadata
    from .filter_by import FilterBy
    from .folder import Folder
    from .folder_id import FolderId
    from .image_format import ImageFormat
    from .image_height import ImageHeight
    from .image_raw import ImageRaw
    from .image_url import ImageUrl
    from .image_width import ImageWidth
    from .inode import Inode
    from .library import Library
    from .library_display_order import LibraryDisplayOrder
    from .library_folders import LibraryFolders
    from .library_icon import LibraryIcon
    from .library_id import LibraryId
    from .library_id_nullable import LibraryIdNullable
    from .library_include import LibraryInclude
    from .library_item_base import LibraryItemBase
    from .library_item_id import LibraryItemId
    from .library_item_minified import LibraryItemMinified
    from .library_item_sequence import LibraryItemSequence
    from .library_media_type import LibraryMediaType
    from .library_name import LibraryName
    from .library_provider import LibraryProvider
    from .library_settings import LibrarySettings
    from .limit import Limit
    from .max_failed_attempts import MaxFailedAttempts
    from .max_notification_queue import MaxNotificationQueue
    from .media_minified import MediaMinified
    from .media_type import MediaType
    from .minified import Minified
    from .notification import Notification
    from .notification_event import NotificationEvent
    from .notification_event_defaults import NotificationEventDefaults
    from .notification_event_name import NotificationEventName
    from .notification_id import NotificationId
    from .notification_settings import NotificationSettings
    from .notification_type import NotificationType
    from .old_library_item_id import OldLibraryItemId
    from .old_podcast_id import OldPodcastId
    from .page import Page
    from .podcast import Podcast
    from .podcast_episode import PodcastEpisode
    from .podcast_id import PodcastId
    from .podcast_metadata import PodcastMetadata
    from .region import Region
    from .sequence import Sequence
    from .series import Series
    from .series_books import SeriesBooks
    from .series_description import SeriesDescription
    from .series_id import SeriesId
    from .series_name import SeriesName
    from .series_progress import SeriesProgress
    from .series_with_progress_and_rss import SeriesWithProgressAndRss
    from .series_with_progress_and_rss_progress import SeriesWithProgressAndRssProgress
    from .size import Size
    from .sort_by import SortBy
    from .sort_desc import SortDesc
    from .tags import Tags
    from .title_template import TitleTemplate
    from .total import Total
    from .updated_at import UpdatedAt
    from .urls import Urls
_dynamic_imports: typing.Dict[str, str] = {
    "AddedAt": ".added_at",
    "AppriseApiUrl": ".apprise_api_url",
    "AudioFile": ".audio_file",
    "AudioMetaTags": ".audio_meta_tags",
    "AudioTrack": ".audio_track",
    "Author": ".author",
    "AuthorAsin": ".author_asin",
    "AuthorDescription": ".author_description",
    "AuthorExpanded": ".author_expanded",
    "AuthorId": ".author_id",
    "AuthorImagePath": ".author_image_path",
    "AuthorMerged": ".author_merged",
    "AuthorName": ".author_name",
    "AuthorSearchName": ".author_search_name",
    "AuthorSeries": ".author_series",
    "AuthorUpdated": ".author_updated",
    "AutoDownloadEpisodes": ".auto_download_episodes",
    "BodyTemplate": ".body_template",
    "BookChapter": ".book_chapter",
    "BookCoverPath": ".book_cover_path",
    "BookMetadataBase": ".book_metadata_base",
    "BookMetadataMinified": ".book_metadata_minified",
    "BookMinified": ".book_minified",
    "CollapseSeries": ".collapse_series",
    "CreatedAt": ".created_at",
    "DurationSec": ".duration_sec",
    "EmailSettings": ".email_settings",
    "Enabled": ".enabled",
    "EreaderDeviceObject": ".ereader_device_object",
    "EreaderDeviceObjectAvailabilityOption": ".ereader_device_object_availability_option",
    "EreaderName": ".ereader_name",
    "FileMetadata": ".file_metadata",
    "FilterBy": ".filter_by",
    "Folder": ".folder",
    "FolderId": ".folder_id",
    "ImageFormat": ".image_format",
    "ImageHeight": ".image_height",
    "ImageRaw": ".image_raw",
    "ImageUrl": ".image_url",
    "ImageWidth": ".image_width",
    "Inode": ".inode",
    "Library": ".library",
    "LibraryDisplayOrder": ".library_display_order",
    "LibraryFolders": ".library_folders",
    "LibraryIcon": ".library_icon",
    "LibraryId": ".library_id",
    "LibraryIdNullable": ".library_id_nullable",
    "LibraryInclude": ".library_include",
    "LibraryItemBase": ".library_item_base",
    "LibraryItemId": ".library_item_id",
    "LibraryItemMinified": ".library_item_minified",
    "LibraryItemSequence": ".library_item_sequence",
    "LibraryMediaType": ".library_media_type",
    "LibraryName": ".library_name",
    "LibraryProvider": ".library_provider",
    "LibrarySettings": ".library_settings",
    "Limit": ".limit",
    "MaxFailedAttempts": ".max_failed_attempts",
    "MaxNotificationQueue": ".max_notification_queue",
    "MediaMinified": ".media_minified",
    "MediaType": ".media_type",
    "Minified": ".minified",
    "Notification": ".notification",
    "NotificationEvent": ".notification_event",
    "NotificationEventDefaults": ".notification_event_defaults",
    "NotificationEventName": ".notification_event_name",
    "NotificationId": ".notification_id",
    "NotificationSettings": ".notification_settings",
    "NotificationType": ".notification_type",
    "OldLibraryItemId": ".old_library_item_id",
    "OldPodcastId": ".old_podcast_id",
    "Page": ".page",
    "Podcast": ".podcast",
    "PodcastEpisode": ".podcast_episode",
    "PodcastId": ".podcast_id",
    "PodcastMetadata": ".podcast_metadata",
    "Region": ".region",
    "Sequence": ".sequence",
    "Series": ".series",
    "SeriesBooks": ".series_books",
    "SeriesDescription": ".series_description",
    "SeriesId": ".series_id",
    "SeriesName": ".series_name",
    "SeriesProgress": ".series_progress",
    "SeriesWithProgressAndRss": ".series_with_progress_and_rss",
    "SeriesWithProgressAndRssProgress": ".series_with_progress_and_rss_progress",
    "Size": ".size",
    "SortBy": ".sort_by",
    "SortDesc": ".sort_desc",
    "Tags": ".tags",
    "TitleTemplate": ".title_template",
    "Total": ".total",
    "UpdatedAt": ".updated_at",
    "Urls": ".urls",
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
    "AddedAt",
    "AppriseApiUrl",
    "AudioFile",
    "AudioMetaTags",
    "AudioTrack",
    "Author",
    "AuthorAsin",
    "AuthorDescription",
    "AuthorExpanded",
    "AuthorId",
    "AuthorImagePath",
    "AuthorMerged",
    "AuthorName",
    "AuthorSearchName",
    "AuthorSeries",
    "AuthorUpdated",
    "AutoDownloadEpisodes",
    "BodyTemplate",
    "BookChapter",
    "BookCoverPath",
    "BookMetadataBase",
    "BookMetadataMinified",
    "BookMinified",
    "CollapseSeries",
    "CreatedAt",
    "DurationSec",
    "EmailSettings",
    "Enabled",
    "EreaderDeviceObject",
    "EreaderDeviceObjectAvailabilityOption",
    "EreaderName",
    "FileMetadata",
    "FilterBy",
    "Folder",
    "FolderId",
    "ImageFormat",
    "ImageHeight",
    "ImageRaw",
    "ImageUrl",
    "ImageWidth",
    "Inode",
    "Library",
    "LibraryDisplayOrder",
    "LibraryFolders",
    "LibraryIcon",
    "LibraryId",
    "LibraryIdNullable",
    "LibraryInclude",
    "LibraryItemBase",
    "LibraryItemId",
    "LibraryItemMinified",
    "LibraryItemSequence",
    "LibraryMediaType",
    "LibraryName",
    "LibraryProvider",
    "LibrarySettings",
    "Limit",
    "MaxFailedAttempts",
    "MaxNotificationQueue",
    "MediaMinified",
    "MediaType",
    "Minified",
    "Notification",
    "NotificationEvent",
    "NotificationEventDefaults",
    "NotificationEventName",
    "NotificationId",
    "NotificationSettings",
    "NotificationType",
    "OldLibraryItemId",
    "OldPodcastId",
    "Page",
    "Podcast",
    "PodcastEpisode",
    "PodcastId",
    "PodcastMetadata",
    "Region",
    "Sequence",
    "Series",
    "SeriesBooks",
    "SeriesDescription",
    "SeriesId",
    "SeriesName",
    "SeriesProgress",
    "SeriesWithProgressAndRss",
    "SeriesWithProgressAndRssProgress",
    "Size",
    "SortBy",
    "SortDesc",
    "Tags",
    "TitleTemplate",
    "Total",
    "UpdatedAt",
    "Urls",
]
