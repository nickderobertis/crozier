

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .assignment.client import AssignmentClient, AsyncAssignmentClient
    from .auth.client import AsyncAuthClient, AuthClient
    from .contribution.client import AsyncContributionClient, ContributionClient
    from .form.client import AsyncFormClient, FormClient
    from .info.client import AsyncInfoClient, InfoClient
    from .media.client import AsyncMediaClient, MediaClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .subscriptions.client import AsyncSubscriptionsClient, SubscriptionsClient
    from .tag.client import AsyncTagClient, TagClient
    from .user.client import AsyncUserClient, UserClient


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



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            token=token,
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
        self._info: typing.Optional[InfoClient] = None
        self._assignment: typing.Optional[AssignmentClient] = None
        self._contribution: typing.Optional[ContributionClient] = None
        self._auth: typing.Optional[AuthClient] = None
        self._form: typing.Optional[FormClient] = None
        self._media: typing.Optional[MediaClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._subscriptions: typing.Optional[SubscriptionsClient] = None
        self._tag: typing.Optional[TagClient] = None
        self._user: typing.Optional[UserClient] = None

    @property
    def info(self):
        if self._info is None:
            from .info.client import InfoClient

            self._info = InfoClient(client_wrapper=self._client_wrapper)
        return self._info

    @property
    def assignment(self):
        if self._assignment is None:
            from .assignment.client import AssignmentClient

            self._assignment = AssignmentClient(client_wrapper=self._client_wrapper)
        return self._assignment

    @property
    def contribution(self):
        if self._contribution is None:
            from .contribution.client import ContributionClient

            self._contribution = ContributionClient(client_wrapper=self._client_wrapper)
        return self._contribution

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def form(self):
        if self._form is None:
            from .form.client import FormClient

            self._form = FormClient(client_wrapper=self._client_wrapper)
        return self._form

    @property
    def media(self):
        if self._media is None:
            from .media.client import MediaClient

            self._media = MediaClient(client_wrapper=self._client_wrapper)
        return self._media

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def subscriptions(self):
        if self._subscriptions is None:
            from .subscriptions.client import SubscriptionsClient

            self._subscriptions = SubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._subscriptions

    @property
    def tag(self):
        if self._tag is None:
            from .tag.client import TagClient

            self._tag = TagClient(client_wrapper=self._client_wrapper)
        return self._tag

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user


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



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._info: typing.Optional[AsyncInfoClient] = None
        self._assignment: typing.Optional[AsyncAssignmentClient] = None
        self._contribution: typing.Optional[AsyncContributionClient] = None
        self._auth: typing.Optional[AsyncAuthClient] = None
        self._form: typing.Optional[AsyncFormClient] = None
        self._media: typing.Optional[AsyncMediaClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._subscriptions: typing.Optional[AsyncSubscriptionsClient] = None
        self._tag: typing.Optional[AsyncTagClient] = None
        self._user: typing.Optional[AsyncUserClient] = None

    @property
    def info(self):
        if self._info is None:
            from .info.client import AsyncInfoClient

            self._info = AsyncInfoClient(client_wrapper=self._client_wrapper)
        return self._info

    @property
    def assignment(self):
        if self._assignment is None:
            from .assignment.client import AsyncAssignmentClient

            self._assignment = AsyncAssignmentClient(client_wrapper=self._client_wrapper)
        return self._assignment

    @property
    def contribution(self):
        if self._contribution is None:
            from .contribution.client import AsyncContributionClient

            self._contribution = AsyncContributionClient(client_wrapper=self._client_wrapper)
        return self._contribution

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def form(self):
        if self._form is None:
            from .form.client import AsyncFormClient

            self._form = AsyncFormClient(client_wrapper=self._client_wrapper)
        return self._form

    @property
    def media(self):
        if self._media is None:
            from .media.client import AsyncMediaClient

            self._media = AsyncMediaClient(client_wrapper=self._client_wrapper)
        return self._media

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def subscriptions(self):
        if self._subscriptions is None:
            from .subscriptions.client import AsyncSubscriptionsClient

            self._subscriptions = AsyncSubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._subscriptions

    @property
    def tag(self):
        if self._tag is None:
            from .tag.client import AsyncTagClient

            self._tag = AsyncTagClient(client_wrapper=self._client_wrapper)
        return self._tag

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
