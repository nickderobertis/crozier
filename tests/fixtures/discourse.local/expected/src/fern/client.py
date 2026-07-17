

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.search_response import SearchResponse

if typing.TYPE_CHECKING:
    from .backups.client import AsyncBackupsClient, BackupsClient
    from .badges.client import AsyncBadgesClient, BadgesClient
    from .categories.client import AsyncCategoriesClient, CategoriesClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .invites.client import AsyncInvitesClient, InvitesClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .posts.client import AsyncPostsClient, PostsClient
    from .private_messages.client import AsyncPrivateMessagesClient, PrivateMessagesClient
    from .site.client import AsyncSiteClient, SiteClient
    from .tags.client import AsyncTagsClient, TagsClient
    from .topics.client import AsyncTopicsClient, TopicsClient
    from .uploads.client import AsyncUploadsClient, UploadsClient
    from .users.client import AsyncUsersClient, UsersClient


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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._backups: typing.Optional[BackupsClient] = None
        self._badges: typing.Optional[BadgesClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._categories: typing.Optional[CategoriesClient] = None
        self._invites: typing.Optional[InvitesClient] = None
        self._topics: typing.Optional[TopicsClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._posts: typing.Optional[PostsClient] = None
        self._site: typing.Optional[SiteClient] = None
        self._tags: typing.Optional[TagsClient] = None
        self._private_messages: typing.Optional[PrivateMessagesClient] = None
        self._uploads: typing.Optional[UploadsClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def search(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponse:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            The query string needs to be url encoded and is made up of the following options:
            - Search term. This is just a string. Usually it would be the first item in the query.
            - `@<username>`: Use the `@` followed by the username to specify posts by this user.
            - `#<category>`: Use the `#` followed by the category slug to search within this category.
            - `tags:`: `api,solved` or for posts that have all the specified tags `api+solved`.
            - `before:`: `yyyy-mm-dd`
            - `after:`: `yyyy-mm-dd`
            - `order:`: `latest`, `likes`, `views`, `latest_topic`
            - `assigned:`: username (without `@`)
            - `in:`: `title`, `likes`, `personal`, `messages`, `seen`, `unseen`, `posted`, `created`, `watching`, `tracking`, `bookmarks`, `assigned`, `unassigned`, `first`, `pinned`, `wiki`
            - `with:`: `images`
            - `status:`: `open`, `closed`, `public`, `archived`, `noreplies`, `single_user`, `solved`, `unsolved`
            - `group:`: group_name or group_id
            - `group_messages:`: group_name or group_id
            - `min_posts:`: 1
            - `max_posts:`: 10
            - `min_views:`: 1
            - `max_views:`: 10
            
            If you are using cURL you can use the `-G` and the `--data-urlencode` flags to encode the query:
            
            ```
            curl -i -sS -X GET -G "http://localhost:4200/search.json" \\
            --data-urlencode 'q=wordpress @scossar #fun after:2020-01-01'
            ```
        
        page : typing.Optional[int]
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        SearchResponse
            success response
        
        Examples
        --------
        from fern import FernApi
        
        client = FernApi()
        client.search(
            q="api @blake #support tags:api after:2021-06-04 in:unseen in:open\norder:latest_topic",
        )
        """
        _response = self._raw_client.search(q=q, page=page, request_options=request_options)
        return _response.data

    @property
    def backups(self):
        if self._backups is None:
            from .backups.client import BackupsClient

            self._backups = BackupsClient(client_wrapper=self._client_wrapper)
        return self._backups

    @property
    def badges(self):
        if self._badges is None:
            from .badges.client import BadgesClient

            self._badges = BadgesClient(client_wrapper=self._client_wrapper)
        return self._badges

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def categories(self):
        if self._categories is None:
            from .categories.client import CategoriesClient

            self._categories = CategoriesClient(client_wrapper=self._client_wrapper)
        return self._categories

    @property
    def invites(self):
        if self._invites is None:
            from .invites.client import InvitesClient

            self._invites = InvitesClient(client_wrapper=self._client_wrapper)
        return self._invites

    @property
    def topics(self):
        if self._topics is None:
            from .topics.client import TopicsClient

            self._topics = TopicsClient(client_wrapper=self._client_wrapper)
        return self._topics

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def posts(self):
        if self._posts is None:
            from .posts.client import PostsClient

            self._posts = PostsClient(client_wrapper=self._client_wrapper)
        return self._posts

    @property
    def site(self):
        if self._site is None:
            from .site.client import SiteClient

            self._site = SiteClient(client_wrapper=self._client_wrapper)
        return self._site

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import TagsClient

            self._tags = TagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def private_messages(self):
        if self._private_messages is None:
            from .private_messages.client import PrivateMessagesClient

            self._private_messages = PrivateMessagesClient(client_wrapper=self._client_wrapper)
        return self._private_messages

    @property
    def uploads(self):
        if self._uploads is None:
            from .uploads.client import UploadsClient

            self._uploads = UploadsClient(client_wrapper=self._client_wrapper)
        return self._uploads


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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._backups: typing.Optional[AsyncBackupsClient] = None
        self._badges: typing.Optional[AsyncBadgesClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._categories: typing.Optional[AsyncCategoriesClient] = None
        self._invites: typing.Optional[AsyncInvitesClient] = None
        self._topics: typing.Optional[AsyncTopicsClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._posts: typing.Optional[AsyncPostsClient] = None
        self._site: typing.Optional[AsyncSiteClient] = None
        self._tags: typing.Optional[AsyncTagsClient] = None
        self._private_messages: typing.Optional[AsyncPrivateMessagesClient] = None
        self._uploads: typing.Optional[AsyncUploadsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def search(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponse:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            The query string needs to be url encoded and is made up of the following options:
            - Search term. This is just a string. Usually it would be the first item in the query.
            - `@<username>`: Use the `@` followed by the username to specify posts by this user.
            - `#<category>`: Use the `#` followed by the category slug to search within this category.
            - `tags:`: `api,solved` or for posts that have all the specified tags `api+solved`.
            - `before:`: `yyyy-mm-dd`
            - `after:`: `yyyy-mm-dd`
            - `order:`: `latest`, `likes`, `views`, `latest_topic`
            - `assigned:`: username (without `@`)
            - `in:`: `title`, `likes`, `personal`, `messages`, `seen`, `unseen`, `posted`, `created`, `watching`, `tracking`, `bookmarks`, `assigned`, `unassigned`, `first`, `pinned`, `wiki`
            - `with:`: `images`
            - `status:`: `open`, `closed`, `public`, `archived`, `noreplies`, `single_user`, `solved`, `unsolved`
            - `group:`: group_name or group_id
            - `group_messages:`: group_name or group_id
            - `min_posts:`: 1
            - `max_posts:`: 10
            - `min_views:`: 1
            - `max_views:`: 10
            
            If you are using cURL you can use the `-G` and the `--data-urlencode` flags to encode the query:
            
            ```
            curl -i -sS -X GET -G "http://localhost:4200/search.json" \\
            --data-urlencode 'q=wordpress @scossar #fun after:2020-01-01'
            ```
        
        page : typing.Optional[int]
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        SearchResponse
            success response
        
        Examples
        --------
        import asyncio
        
        from fern import AsyncFernApi
        
        client = AsyncFernApi()
        
        
        async def main() -> None:
            await client.search(
                q="api @blake #support tags:api after:2021-06-04 in:unseen in:open\norder:latest_topic",
            )
        
        
        asyncio.run(main())
        """
        _response = await self._raw_client.search(q=q, page=page, request_options=request_options)
        return _response.data

    @property
    def backups(self):
        if self._backups is None:
            from .backups.client import AsyncBackupsClient

            self._backups = AsyncBackupsClient(client_wrapper=self._client_wrapper)
        return self._backups

    @property
    def badges(self):
        if self._badges is None:
            from .badges.client import AsyncBadgesClient

            self._badges = AsyncBadgesClient(client_wrapper=self._client_wrapper)
        return self._badges

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def categories(self):
        if self._categories is None:
            from .categories.client import AsyncCategoriesClient

            self._categories = AsyncCategoriesClient(client_wrapper=self._client_wrapper)
        return self._categories

    @property
    def invites(self):
        if self._invites is None:
            from .invites.client import AsyncInvitesClient

            self._invites = AsyncInvitesClient(client_wrapper=self._client_wrapper)
        return self._invites

    @property
    def topics(self):
        if self._topics is None:
            from .topics.client import AsyncTopicsClient

            self._topics = AsyncTopicsClient(client_wrapper=self._client_wrapper)
        return self._topics

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def posts(self):
        if self._posts is None:
            from .posts.client import AsyncPostsClient

            self._posts = AsyncPostsClient(client_wrapper=self._client_wrapper)
        return self._posts

    @property
    def site(self):
        if self._site is None:
            from .site.client import AsyncSiteClient

            self._site = AsyncSiteClient(client_wrapper=self._client_wrapper)
        return self._site

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import AsyncTagsClient

            self._tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def private_messages(self):
        if self._private_messages is None:
            from .private_messages.client import AsyncPrivateMessagesClient

            self._private_messages = AsyncPrivateMessagesClient(client_wrapper=self._client_wrapper)
        return self._private_messages

    @property
    def uploads(self):
        if self._uploads is None:
            from .uploads.client import AsyncUploadsClient

            self._uploads = AsyncUploadsClient(client_wrapper=self._client_wrapper)
        return self._uploads


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
