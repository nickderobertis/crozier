

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .campaigns.client import AsyncCampaignsClient, CampaignsClient
    from .fields.client import AsyncFieldsClient, FieldsClient
    from .lists.client import AsyncListsClient, ListsClient
    from .results.client import AsyncResultsClient, ResultsClient
    from .segments.client import AsyncSegmentsClient, SegmentsClient
    from .subscribers.client import AsyncSubscribersClient, SubscribersClient
    from .webhooks.client import AsyncWebhooksClient, WebhooksClient


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



    api_key : typing.Union[str, typing.Callable[[], str]]
    leave_empty : typing.Union[str, typing.Callable[[], str]]
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
        leave_empty="YOUR_LEAVE_EMPTY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: typing.Union[str, typing.Callable[[], str]],
        leave_empty: typing.Union[str, typing.Callable[[], str]],
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
            leave_empty=leave_empty,
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
        self._lists: typing.Optional[ListsClient] = None
        self._fields: typing.Optional[FieldsClient] = None
        self._segments: typing.Optional[SegmentsClient] = None
        self._subscribers: typing.Optional[SubscribersClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None
        self._campaigns: typing.Optional[CampaignsClient] = None
        self._results: typing.Optional[ResultsClient] = None

    @property
    def lists(self):
        if self._lists is None:
            from .lists.client import ListsClient

            self._lists = ListsClient(client_wrapper=self._client_wrapper)
        return self._lists

    @property
    def fields(self):
        if self._fields is None:
            from .fields.client import FieldsClient

            self._fields = FieldsClient(client_wrapper=self._client_wrapper)
        return self._fields

    @property
    def segments(self):
        if self._segments is None:
            from .segments.client import SegmentsClient

            self._segments = SegmentsClient(client_wrapper=self._client_wrapper)
        return self._segments

    @property
    def subscribers(self):
        if self._subscribers is None:
            from .subscribers.client import SubscribersClient

            self._subscribers = SubscribersClient(client_wrapper=self._client_wrapper)
        return self._subscribers

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .campaigns.client import CampaignsClient

            self._campaigns = CampaignsClient(client_wrapper=self._client_wrapper)
        return self._campaigns

    @property
    def results(self):
        if self._results is None:
            from .results.client import ResultsClient

            self._results = ResultsClient(client_wrapper=self._client_wrapper)
        return self._results


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



    api_key : typing.Union[str, typing.Callable[[], str]]
    leave_empty : typing.Union[str, typing.Callable[[], str]]
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
        leave_empty="YOUR_LEAVE_EMPTY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: typing.Union[str, typing.Callable[[], str]],
        leave_empty: typing.Union[str, typing.Callable[[], str]],
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
            leave_empty=leave_empty,
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
        self._lists: typing.Optional[AsyncListsClient] = None
        self._fields: typing.Optional[AsyncFieldsClient] = None
        self._segments: typing.Optional[AsyncSegmentsClient] = None
        self._subscribers: typing.Optional[AsyncSubscribersClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None
        self._campaigns: typing.Optional[AsyncCampaignsClient] = None
        self._results: typing.Optional[AsyncResultsClient] = None

    @property
    def lists(self):
        if self._lists is None:
            from .lists.client import AsyncListsClient

            self._lists = AsyncListsClient(client_wrapper=self._client_wrapper)
        return self._lists

    @property
    def fields(self):
        if self._fields is None:
            from .fields.client import AsyncFieldsClient

            self._fields = AsyncFieldsClient(client_wrapper=self._client_wrapper)
        return self._fields

    @property
    def segments(self):
        if self._segments is None:
            from .segments.client import AsyncSegmentsClient

            self._segments = AsyncSegmentsClient(client_wrapper=self._client_wrapper)
        return self._segments

    @property
    def subscribers(self):
        if self._subscribers is None:
            from .subscribers.client import AsyncSubscribersClient

            self._subscribers = AsyncSubscribersClient(client_wrapper=self._client_wrapper)
        return self._subscribers

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def campaigns(self):
        if self._campaigns is None:
            from .campaigns.client import AsyncCampaignsClient

            self._campaigns = AsyncCampaignsClient(client_wrapper=self._client_wrapper)
        return self._campaigns

    @property
    def results(self):
        if self._results is None:
            from .results.client import AsyncResultsClient

            self._results = AsyncResultsClient(client_wrapper=self._client_wrapper)
        return self._results


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
