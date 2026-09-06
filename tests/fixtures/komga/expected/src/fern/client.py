

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .announcements.client import AnnouncementsClient, AsyncAnnouncementsClient
    from .api_keys.client import ApiKeysClient, AsyncApiKeysClient
    from .book_pages.client import AsyncBookPagesClient, BookPagesClient
    from .book_poster.client import AsyncBookPosterClient, BookPosterClient
    from .books.client import AsyncBooksClient, BooksClient
    from .claim.client import AsyncClaimClient, ClaimClient
    from .client_settings.client import AsyncClientSettingsClient, ClientSettingsClient
    from .collection_poster.client import AsyncCollectionPosterClient, CollectionPosterClient
    from .collection_series.client import AsyncCollectionSeriesClient, CollectionSeriesClient
    from .collections.client import AsyncCollectionsClient, CollectionsClient
    from .comic_rack.client import AsyncComicRackClient, ComicRackClient
    from .current_user.client import AsyncCurrentUserClient, CurrentUserClient
    from .deprecated.client import AsyncDeprecatedClient, DeprecatedClient
    from .duplicate_pages.client import AsyncDuplicatePagesClient, DuplicatePagesClient
    from .file_system.client import AsyncFileSystemClient, FileSystemClient
    from .fonts.client import AsyncFontsClient, FontsClient
    from .history.client import AsyncHistoryClient, HistoryClient
    from .import_.client import AsyncImportClient, ImportClient
    from .libraries.client import AsyncLibrariesClient, LibrariesClient
    from .management.client import AsyncManagementClient, ManagementClient
    from .mihon.client import AsyncMihonClient, MihonClient
    from .o_auth2.client import AsyncOAuth2Client, OAuth2Client
    from .readlist_books.client import AsyncReadlistBooksClient, ReadlistBooksClient
    from .readlist_poster.client import AsyncReadlistPosterClient, ReadlistPosterClient
    from .readlists.client import AsyncReadlistsClient, ReadlistsClient
    from .referential_metadata.client import AsyncReferentialMetadataClient, ReferentialMetadataClient
    from .releases.client import AsyncReleasesClient, ReleasesClient
    from .series.client import AsyncSeriesClient, SeriesClient
    from .series_poster.client import AsyncSeriesPosterClient, SeriesPosterClient
    from .server_settings.client import AsyncServerSettingsClient, ServerSettingsClient
    from .sync_points.client import AsyncSyncPointsClient, SyncPointsClient
    from .tasks.client import AsyncTasksClient, TasksClient
    from .user_session.client import AsyncUserSessionClient, UserSessionClient
    from .users.client import AsyncUsersClient, UsersClient
    from .web_pub_manifest.client import AsyncWebPubManifestClient, WebPubManifestClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._management: typing.Optional[ManagementClient] = None
        self._user_session: typing.Optional[UserSessionClient] = None
        self._deprecated: typing.Optional[DeprecatedClient] = None
        self._announcements: typing.Optional[AnnouncementsClient] = None
        self._books: typing.Optional[BooksClient] = None
        self._import_: typing.Optional[ImportClient] = None
        self._book_poster: typing.Optional[BookPosterClient] = None
        self._web_pub_manifest: typing.Optional[WebPubManifestClient] = None
        self._book_pages: typing.Optional[BookPagesClient] = None
        self._claim: typing.Optional[ClaimClient] = None
        self._client_settings: typing.Optional[ClientSettingsClient] = None
        self._collections: typing.Optional[CollectionsClient] = None
        self._collection_series: typing.Optional[CollectionSeriesClient] = None
        self._collection_poster: typing.Optional[CollectionPosterClient] = None
        self._file_system: typing.Optional[FileSystemClient] = None
        self._fonts: typing.Optional[FontsClient] = None
        self._history: typing.Optional[HistoryClient] = None
        self._libraries: typing.Optional[LibrariesClient] = None
        self._o_auth2: typing.Optional[OAuth2Client] = None
        self._duplicate_pages: typing.Optional[DuplicatePagesClient] = None
        self._readlists: typing.Optional[ReadlistsClient] = None
        self._comic_rack: typing.Optional[ComicRackClient] = None
        self._readlist_books: typing.Optional[ReadlistBooksClient] = None
        self._mihon: typing.Optional[MihonClient] = None
        self._readlist_poster: typing.Optional[ReadlistPosterClient] = None
        self._releases: typing.Optional[ReleasesClient] = None
        self._series: typing.Optional[SeriesClient] = None
        self._series_poster: typing.Optional[SeriesPosterClient] = None
        self._server_settings: typing.Optional[ServerSettingsClient] = None
        self._sync_points: typing.Optional[SyncPointsClient] = None
        self._tasks: typing.Optional[TasksClient] = None
        self._referential_metadata: typing.Optional[ReferentialMetadataClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._current_user: typing.Optional[CurrentUserClient] = None
        self._api_keys: typing.Optional[ApiKeysClient] = None

    @property
    def management(self):
        if self._management is None:
            from .management.client import ManagementClient

            self._management = ManagementClient(client_wrapper=self._client_wrapper)
        return self._management

    @property
    def user_session(self):
        if self._user_session is None:
            from .user_session.client import UserSessionClient

            self._user_session = UserSessionClient(client_wrapper=self._client_wrapper)
        return self._user_session

    @property
    def deprecated(self):
        if self._deprecated is None:
            from .deprecated.client import DeprecatedClient

            self._deprecated = DeprecatedClient(client_wrapper=self._client_wrapper)
        return self._deprecated

    @property
    def announcements(self):
        if self._announcements is None:
            from .announcements.client import AnnouncementsClient

            self._announcements = AnnouncementsClient(client_wrapper=self._client_wrapper)
        return self._announcements

    @property
    def books(self):
        if self._books is None:
            from .books.client import BooksClient

            self._books = BooksClient(client_wrapper=self._client_wrapper)
        return self._books

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import ImportClient

            self._import_ = ImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def book_poster(self):
        if self._book_poster is None:
            from .book_poster.client import BookPosterClient

            self._book_poster = BookPosterClient(client_wrapper=self._client_wrapper)
        return self._book_poster

    @property
    def web_pub_manifest(self):
        if self._web_pub_manifest is None:
            from .web_pub_manifest.client import WebPubManifestClient

            self._web_pub_manifest = WebPubManifestClient(client_wrapper=self._client_wrapper)
        return self._web_pub_manifest

    @property
    def book_pages(self):
        if self._book_pages is None:
            from .book_pages.client import BookPagesClient

            self._book_pages = BookPagesClient(client_wrapper=self._client_wrapper)
        return self._book_pages

    @property
    def claim(self):
        if self._claim is None:
            from .claim.client import ClaimClient

            self._claim = ClaimClient(client_wrapper=self._client_wrapper)
        return self._claim

    @property
    def client_settings(self):
        if self._client_settings is None:
            from .client_settings.client import ClientSettingsClient

            self._client_settings = ClientSettingsClient(client_wrapper=self._client_wrapper)
        return self._client_settings

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import CollectionsClient

            self._collections = CollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def collection_series(self):
        if self._collection_series is None:
            from .collection_series.client import CollectionSeriesClient

            self._collection_series = CollectionSeriesClient(client_wrapper=self._client_wrapper)
        return self._collection_series

    @property
    def collection_poster(self):
        if self._collection_poster is None:
            from .collection_poster.client import CollectionPosterClient

            self._collection_poster = CollectionPosterClient(client_wrapper=self._client_wrapper)
        return self._collection_poster

    @property
    def file_system(self):
        if self._file_system is None:
            from .file_system.client import FileSystemClient

            self._file_system = FileSystemClient(client_wrapper=self._client_wrapper)
        return self._file_system

    @property
    def fonts(self):
        if self._fonts is None:
            from .fonts.client import FontsClient

            self._fonts = FontsClient(client_wrapper=self._client_wrapper)
        return self._fonts

    @property
    def history(self):
        if self._history is None:
            from .history.client import HistoryClient

            self._history = HistoryClient(client_wrapper=self._client_wrapper)
        return self._history

    @property
    def libraries(self):
        if self._libraries is None:
            from .libraries.client import LibrariesClient

            self._libraries = LibrariesClient(client_wrapper=self._client_wrapper)
        return self._libraries

    @property
    def o_auth2(self):
        if self._o_auth2 is None:
            from .o_auth2.client import OAuth2Client

            self._o_auth2 = OAuth2Client(client_wrapper=self._client_wrapper)
        return self._o_auth2

    @property
    def duplicate_pages(self):
        if self._duplicate_pages is None:
            from .duplicate_pages.client import DuplicatePagesClient

            self._duplicate_pages = DuplicatePagesClient(client_wrapper=self._client_wrapper)
        return self._duplicate_pages

    @property
    def readlists(self):
        if self._readlists is None:
            from .readlists.client import ReadlistsClient

            self._readlists = ReadlistsClient(client_wrapper=self._client_wrapper)
        return self._readlists

    @property
    def comic_rack(self):
        if self._comic_rack is None:
            from .comic_rack.client import ComicRackClient

            self._comic_rack = ComicRackClient(client_wrapper=self._client_wrapper)
        return self._comic_rack

    @property
    def readlist_books(self):
        if self._readlist_books is None:
            from .readlist_books.client import ReadlistBooksClient

            self._readlist_books = ReadlistBooksClient(client_wrapper=self._client_wrapper)
        return self._readlist_books

    @property
    def mihon(self):
        if self._mihon is None:
            from .mihon.client import MihonClient

            self._mihon = MihonClient(client_wrapper=self._client_wrapper)
        return self._mihon

    @property
    def readlist_poster(self):
        if self._readlist_poster is None:
            from .readlist_poster.client import ReadlistPosterClient

            self._readlist_poster = ReadlistPosterClient(client_wrapper=self._client_wrapper)
        return self._readlist_poster

    @property
    def releases(self):
        if self._releases is None:
            from .releases.client import ReleasesClient

            self._releases = ReleasesClient(client_wrapper=self._client_wrapper)
        return self._releases

    @property
    def series(self):
        if self._series is None:
            from .series.client import SeriesClient

            self._series = SeriesClient(client_wrapper=self._client_wrapper)
        return self._series

    @property
    def series_poster(self):
        if self._series_poster is None:
            from .series_poster.client import SeriesPosterClient

            self._series_poster = SeriesPosterClient(client_wrapper=self._client_wrapper)
        return self._series_poster

    @property
    def server_settings(self):
        if self._server_settings is None:
            from .server_settings.client import ServerSettingsClient

            self._server_settings = ServerSettingsClient(client_wrapper=self._client_wrapper)
        return self._server_settings

    @property
    def sync_points(self):
        if self._sync_points is None:
            from .sync_points.client import SyncPointsClient

            self._sync_points = SyncPointsClient(client_wrapper=self._client_wrapper)
        return self._sync_points

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import TasksClient

            self._tasks = TasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def referential_metadata(self):
        if self._referential_metadata is None:
            from .referential_metadata.client import ReferentialMetadataClient

            self._referential_metadata = ReferentialMetadataClient(client_wrapper=self._client_wrapper)
        return self._referential_metadata

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def current_user(self):
        if self._current_user is None:
            from .current_user.client import CurrentUserClient

            self._current_user = CurrentUserClient(client_wrapper=self._client_wrapper)
        return self._current_user

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import ApiKeysClient

            self._api_keys = ApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._management: typing.Optional[AsyncManagementClient] = None
        self._user_session: typing.Optional[AsyncUserSessionClient] = None
        self._deprecated: typing.Optional[AsyncDeprecatedClient] = None
        self._announcements: typing.Optional[AsyncAnnouncementsClient] = None
        self._books: typing.Optional[AsyncBooksClient] = None
        self._import_: typing.Optional[AsyncImportClient] = None
        self._book_poster: typing.Optional[AsyncBookPosterClient] = None
        self._web_pub_manifest: typing.Optional[AsyncWebPubManifestClient] = None
        self._book_pages: typing.Optional[AsyncBookPagesClient] = None
        self._claim: typing.Optional[AsyncClaimClient] = None
        self._client_settings: typing.Optional[AsyncClientSettingsClient] = None
        self._collections: typing.Optional[AsyncCollectionsClient] = None
        self._collection_series: typing.Optional[AsyncCollectionSeriesClient] = None
        self._collection_poster: typing.Optional[AsyncCollectionPosterClient] = None
        self._file_system: typing.Optional[AsyncFileSystemClient] = None
        self._fonts: typing.Optional[AsyncFontsClient] = None
        self._history: typing.Optional[AsyncHistoryClient] = None
        self._libraries: typing.Optional[AsyncLibrariesClient] = None
        self._o_auth2: typing.Optional[AsyncOAuth2Client] = None
        self._duplicate_pages: typing.Optional[AsyncDuplicatePagesClient] = None
        self._readlists: typing.Optional[AsyncReadlistsClient] = None
        self._comic_rack: typing.Optional[AsyncComicRackClient] = None
        self._readlist_books: typing.Optional[AsyncReadlistBooksClient] = None
        self._mihon: typing.Optional[AsyncMihonClient] = None
        self._readlist_poster: typing.Optional[AsyncReadlistPosterClient] = None
        self._releases: typing.Optional[AsyncReleasesClient] = None
        self._series: typing.Optional[AsyncSeriesClient] = None
        self._series_poster: typing.Optional[AsyncSeriesPosterClient] = None
        self._server_settings: typing.Optional[AsyncServerSettingsClient] = None
        self._sync_points: typing.Optional[AsyncSyncPointsClient] = None
        self._tasks: typing.Optional[AsyncTasksClient] = None
        self._referential_metadata: typing.Optional[AsyncReferentialMetadataClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._current_user: typing.Optional[AsyncCurrentUserClient] = None
        self._api_keys: typing.Optional[AsyncApiKeysClient] = None

    @property
    def management(self):
        if self._management is None:
            from .management.client import AsyncManagementClient

            self._management = AsyncManagementClient(client_wrapper=self._client_wrapper)
        return self._management

    @property
    def user_session(self):
        if self._user_session is None:
            from .user_session.client import AsyncUserSessionClient

            self._user_session = AsyncUserSessionClient(client_wrapper=self._client_wrapper)
        return self._user_session

    @property
    def deprecated(self):
        if self._deprecated is None:
            from .deprecated.client import AsyncDeprecatedClient

            self._deprecated = AsyncDeprecatedClient(client_wrapper=self._client_wrapper)
        return self._deprecated

    @property
    def announcements(self):
        if self._announcements is None:
            from .announcements.client import AsyncAnnouncementsClient

            self._announcements = AsyncAnnouncementsClient(client_wrapper=self._client_wrapper)
        return self._announcements

    @property
    def books(self):
        if self._books is None:
            from .books.client import AsyncBooksClient

            self._books = AsyncBooksClient(client_wrapper=self._client_wrapper)
        return self._books

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import AsyncImportClient

            self._import_ = AsyncImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def book_poster(self):
        if self._book_poster is None:
            from .book_poster.client import AsyncBookPosterClient

            self._book_poster = AsyncBookPosterClient(client_wrapper=self._client_wrapper)
        return self._book_poster

    @property
    def web_pub_manifest(self):
        if self._web_pub_manifest is None:
            from .web_pub_manifest.client import AsyncWebPubManifestClient

            self._web_pub_manifest = AsyncWebPubManifestClient(client_wrapper=self._client_wrapper)
        return self._web_pub_manifest

    @property
    def book_pages(self):
        if self._book_pages is None:
            from .book_pages.client import AsyncBookPagesClient

            self._book_pages = AsyncBookPagesClient(client_wrapper=self._client_wrapper)
        return self._book_pages

    @property
    def claim(self):
        if self._claim is None:
            from .claim.client import AsyncClaimClient

            self._claim = AsyncClaimClient(client_wrapper=self._client_wrapper)
        return self._claim

    @property
    def client_settings(self):
        if self._client_settings is None:
            from .client_settings.client import AsyncClientSettingsClient

            self._client_settings = AsyncClientSettingsClient(client_wrapper=self._client_wrapper)
        return self._client_settings

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import AsyncCollectionsClient

            self._collections = AsyncCollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def collection_series(self):
        if self._collection_series is None:
            from .collection_series.client import AsyncCollectionSeriesClient

            self._collection_series = AsyncCollectionSeriesClient(client_wrapper=self._client_wrapper)
        return self._collection_series

    @property
    def collection_poster(self):
        if self._collection_poster is None:
            from .collection_poster.client import AsyncCollectionPosterClient

            self._collection_poster = AsyncCollectionPosterClient(client_wrapper=self._client_wrapper)
        return self._collection_poster

    @property
    def file_system(self):
        if self._file_system is None:
            from .file_system.client import AsyncFileSystemClient

            self._file_system = AsyncFileSystemClient(client_wrapper=self._client_wrapper)
        return self._file_system

    @property
    def fonts(self):
        if self._fonts is None:
            from .fonts.client import AsyncFontsClient

            self._fonts = AsyncFontsClient(client_wrapper=self._client_wrapper)
        return self._fonts

    @property
    def history(self):
        if self._history is None:
            from .history.client import AsyncHistoryClient

            self._history = AsyncHistoryClient(client_wrapper=self._client_wrapper)
        return self._history

    @property
    def libraries(self):
        if self._libraries is None:
            from .libraries.client import AsyncLibrariesClient

            self._libraries = AsyncLibrariesClient(client_wrapper=self._client_wrapper)
        return self._libraries

    @property
    def o_auth2(self):
        if self._o_auth2 is None:
            from .o_auth2.client import AsyncOAuth2Client

            self._o_auth2 = AsyncOAuth2Client(client_wrapper=self._client_wrapper)
        return self._o_auth2

    @property
    def duplicate_pages(self):
        if self._duplicate_pages is None:
            from .duplicate_pages.client import AsyncDuplicatePagesClient

            self._duplicate_pages = AsyncDuplicatePagesClient(client_wrapper=self._client_wrapper)
        return self._duplicate_pages

    @property
    def readlists(self):
        if self._readlists is None:
            from .readlists.client import AsyncReadlistsClient

            self._readlists = AsyncReadlistsClient(client_wrapper=self._client_wrapper)
        return self._readlists

    @property
    def comic_rack(self):
        if self._comic_rack is None:
            from .comic_rack.client import AsyncComicRackClient

            self._comic_rack = AsyncComicRackClient(client_wrapper=self._client_wrapper)
        return self._comic_rack

    @property
    def readlist_books(self):
        if self._readlist_books is None:
            from .readlist_books.client import AsyncReadlistBooksClient

            self._readlist_books = AsyncReadlistBooksClient(client_wrapper=self._client_wrapper)
        return self._readlist_books

    @property
    def mihon(self):
        if self._mihon is None:
            from .mihon.client import AsyncMihonClient

            self._mihon = AsyncMihonClient(client_wrapper=self._client_wrapper)
        return self._mihon

    @property
    def readlist_poster(self):
        if self._readlist_poster is None:
            from .readlist_poster.client import AsyncReadlistPosterClient

            self._readlist_poster = AsyncReadlistPosterClient(client_wrapper=self._client_wrapper)
        return self._readlist_poster

    @property
    def releases(self):
        if self._releases is None:
            from .releases.client import AsyncReleasesClient

            self._releases = AsyncReleasesClient(client_wrapper=self._client_wrapper)
        return self._releases

    @property
    def series(self):
        if self._series is None:
            from .series.client import AsyncSeriesClient

            self._series = AsyncSeriesClient(client_wrapper=self._client_wrapper)
        return self._series

    @property
    def series_poster(self):
        if self._series_poster is None:
            from .series_poster.client import AsyncSeriesPosterClient

            self._series_poster = AsyncSeriesPosterClient(client_wrapper=self._client_wrapper)
        return self._series_poster

    @property
    def server_settings(self):
        if self._server_settings is None:
            from .server_settings.client import AsyncServerSettingsClient

            self._server_settings = AsyncServerSettingsClient(client_wrapper=self._client_wrapper)
        return self._server_settings

    @property
    def sync_points(self):
        if self._sync_points is None:
            from .sync_points.client import AsyncSyncPointsClient

            self._sync_points = AsyncSyncPointsClient(client_wrapper=self._client_wrapper)
        return self._sync_points

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import AsyncTasksClient

            self._tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def referential_metadata(self):
        if self._referential_metadata is None:
            from .referential_metadata.client import AsyncReferentialMetadataClient

            self._referential_metadata = AsyncReferentialMetadataClient(client_wrapper=self._client_wrapper)
        return self._referential_metadata

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def current_user(self):
        if self._current_user is None:
            from .current_user.client import AsyncCurrentUserClient

            self._current_user = AsyncCurrentUserClient(client_wrapper=self._client_wrapper)
        return self._current_user

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import AsyncApiKeysClient

            self._api_keys = AsyncApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
