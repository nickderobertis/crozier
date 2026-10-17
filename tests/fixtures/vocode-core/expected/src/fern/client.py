

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi

if typing.TYPE_CHECKING:
    from .account_connections.client import AccountConnectionsClient, AsyncAccountConnectionsClient
    from .actions.client import ActionsClient, AsyncActionsClient
    from .agents.client import AgentsClient, AsyncAgentsClient
    from .calls.client import AsyncCallsClient, CallsClient
    from .numbers.client import AsyncNumbersClient, NumbersClient
    from .prompts.client import AsyncPromptsClient, PromptsClient
    from .usage.client import AsyncUsageClient, UsageClient
    from .vector_databases.client import AsyncVectorDatabasesClient, VectorDatabasesClient
    from .voices.client import AsyncVoicesClient, VoicesClient
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



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._numbers: typing.Optional[NumbersClient] = None
        self._calls: typing.Optional[CallsClient] = None
        self._usage: typing.Optional[UsageClient] = None
        self._actions: typing.Optional[ActionsClient] = None
        self._agents: typing.Optional[AgentsClient] = None
        self._voices: typing.Optional[VoicesClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None
        self._prompts: typing.Optional[PromptsClient] = None
        self._vector_databases: typing.Optional[VectorDatabasesClient] = None
        self._account_connections: typing.Optional[AccountConnectionsClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def metrics_metrics_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Endpoint that serves Prometheus metrics.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics_metrics_get()
        """
        _response = self._raw_client.metrics_metrics_get(request_options=request_options)
        return _response.data

    @property
    def numbers(self):
        if self._numbers is None:
            from .numbers.client import NumbersClient

            self._numbers = NumbersClient(client_wrapper=self._client_wrapper)
        return self._numbers

    @property
    def calls(self):
        if self._calls is None:
            from .calls.client import CallsClient

            self._calls = CallsClient(client_wrapper=self._client_wrapper)
        return self._calls

    @property
    def usage(self):
        if self._usage is None:
            from .usage.client import UsageClient

            self._usage = UsageClient(client_wrapper=self._client_wrapper)
        return self._usage

    @property
    def actions(self):
        if self._actions is None:
            from .actions.client import ActionsClient

            self._actions = ActionsClient(client_wrapper=self._client_wrapper)
        return self._actions

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AgentsClient

            self._agents = AgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def voices(self):
        if self._voices is None:
            from .voices.client import VoicesClient

            self._voices = VoicesClient(client_wrapper=self._client_wrapper)
        return self._voices

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import PromptsClient

            self._prompts = PromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def vector_databases(self):
        if self._vector_databases is None:
            from .vector_databases.client import VectorDatabasesClient

            self._vector_databases = VectorDatabasesClient(client_wrapper=self._client_wrapper)
        return self._vector_databases

    @property
    def account_connections(self):
        if self._account_connections is None:
            from .account_connections.client import AccountConnectionsClient

            self._account_connections = AccountConnectionsClient(client_wrapper=self._client_wrapper)
        return self._account_connections


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



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._numbers: typing.Optional[AsyncNumbersClient] = None
        self._calls: typing.Optional[AsyncCallsClient] = None
        self._usage: typing.Optional[AsyncUsageClient] = None
        self._actions: typing.Optional[AsyncActionsClient] = None
        self._agents: typing.Optional[AsyncAgentsClient] = None
        self._voices: typing.Optional[AsyncVoicesClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None
        self._prompts: typing.Optional[AsyncPromptsClient] = None
        self._vector_databases: typing.Optional[AsyncVectorDatabasesClient] = None
        self._account_connections: typing.Optional[AsyncAccountConnectionsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def metrics_metrics_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Endpoint that serves Prometheus metrics.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics_metrics_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.metrics_metrics_get(request_options=request_options)
        return _response.data

    @property
    def numbers(self):
        if self._numbers is None:
            from .numbers.client import AsyncNumbersClient

            self._numbers = AsyncNumbersClient(client_wrapper=self._client_wrapper)
        return self._numbers

    @property
    def calls(self):
        if self._calls is None:
            from .calls.client import AsyncCallsClient

            self._calls = AsyncCallsClient(client_wrapper=self._client_wrapper)
        return self._calls

    @property
    def usage(self):
        if self._usage is None:
            from .usage.client import AsyncUsageClient

            self._usage = AsyncUsageClient(client_wrapper=self._client_wrapper)
        return self._usage

    @property
    def actions(self):
        if self._actions is None:
            from .actions.client import AsyncActionsClient

            self._actions = AsyncActionsClient(client_wrapper=self._client_wrapper)
        return self._actions

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AsyncAgentsClient

            self._agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def voices(self):
        if self._voices is None:
            from .voices.client import AsyncVoicesClient

            self._voices = AsyncVoicesClient(client_wrapper=self._client_wrapper)
        return self._voices

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import AsyncPromptsClient

            self._prompts = AsyncPromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def vector_databases(self):
        if self._vector_databases is None:
            from .vector_databases.client import AsyncVectorDatabasesClient

            self._vector_databases = AsyncVectorDatabasesClient(client_wrapper=self._client_wrapper)
        return self._vector_databases

    @property
    def account_connections(self):
        if self._account_connections is None:
            from .account_connections.client import AsyncAccountConnectionsClient

            self._account_connections = AsyncAccountConnectionsClient(client_wrapper=self._client_wrapper)
        return self._account_connections


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
