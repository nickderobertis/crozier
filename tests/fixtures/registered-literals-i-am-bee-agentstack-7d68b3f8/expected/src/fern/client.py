

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .a2a.client import A2AClient, AsyncA2AClient
    from .auth.client import AsyncAuthClient, AuthClient
    from .configurations.client import AsyncConfigurationsClient, ConfigurationsClient
    from .connectors.client import AsyncConnectorsClient, ConnectorsClient
    from .contexts.client import AsyncContextsClient, ContextsClient
    from .files.client import AsyncFilesClient, FilesClient
    from .model_providers.client import AsyncModelProvidersClient, ModelProvidersClient
    from .openai.client import AsyncOpenaiClient, OpenaiClient
    from .provider_builds.client import AsyncProviderBuildsClient, ProviderBuildsClient
    from .provider_discovery.client import AsyncProviderDiscoveryClient, ProviderDiscoveryClient
    from .providers.client import AsyncProvidersClient, ProvidersClient
    from .user.client import AsyncUserClient, UserClient
    from .user_feedback.client import AsyncUserFeedbackClient, UserFeedbackClient
    from .users.client import AsyncUsersClient, UsersClient
    from .variables.client import AsyncVariablesClient, VariablesClient
    from .vector_stores.client import AsyncVectorStoresClient, VectorStoresClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            base_url=base_url,
            username=username,
            password=password,
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
        self._user: typing.Optional[UserClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._a2a: typing.Optional[A2AClient] = None
        self._providers: typing.Optional[ProvidersClient] = None
        self._provider_discovery: typing.Optional[ProviderDiscoveryClient] = None
        self._provider_builds: typing.Optional[ProviderBuildsClient] = None
        self._model_providers: typing.Optional[ModelProvidersClient] = None
        self._configurations: typing.Optional[ConfigurationsClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._variables: typing.Optional[VariablesClient] = None
        self._contexts: typing.Optional[ContextsClient] = None
        self._openai: typing.Optional[OpenaiClient] = None
        self._vector_stores: typing.Optional[VectorStoresClient] = None
        self._user_feedback: typing.Optional[UserFeedbackClient] = None
        self._connectors: typing.Optional[ConnectorsClient] = None
        self._auth: typing.Optional[AuthClient] = None

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def a2a(self):
        if self._a2a is None:
            from .a2a.client import A2AClient

            self._a2a = A2AClient(client_wrapper=self._client_wrapper)
        return self._a2a

    @property
    def providers(self):
        if self._providers is None:
            from .providers.client import ProvidersClient

            self._providers = ProvidersClient(client_wrapper=self._client_wrapper)
        return self._providers

    @property
    def provider_discovery(self):
        if self._provider_discovery is None:
            from .provider_discovery.client import ProviderDiscoveryClient

            self._provider_discovery = ProviderDiscoveryClient(client_wrapper=self._client_wrapper)
        return self._provider_discovery

    @property
    def provider_builds(self):
        if self._provider_builds is None:
            from .provider_builds.client import ProviderBuildsClient

            self._provider_builds = ProviderBuildsClient(client_wrapper=self._client_wrapper)
        return self._provider_builds

    @property
    def model_providers(self):
        if self._model_providers is None:
            from .model_providers.client import ModelProvidersClient

            self._model_providers = ModelProvidersClient(client_wrapper=self._client_wrapper)
        return self._model_providers

    @property
    def configurations(self):
        if self._configurations is None:
            from .configurations.client import ConfigurationsClient

            self._configurations = ConfigurationsClient(client_wrapper=self._client_wrapper)
        return self._configurations

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def variables(self):
        if self._variables is None:
            from .variables.client import VariablesClient

            self._variables = VariablesClient(client_wrapper=self._client_wrapper)
        return self._variables

    @property
    def contexts(self):
        if self._contexts is None:
            from .contexts.client import ContextsClient

            self._contexts = ContextsClient(client_wrapper=self._client_wrapper)
        return self._contexts

    @property
    def openai(self):
        if self._openai is None:
            from .openai.client import OpenaiClient

            self._openai = OpenaiClient(client_wrapper=self._client_wrapper)
        return self._openai

    @property
    def vector_stores(self):
        if self._vector_stores is None:
            from .vector_stores.client import VectorStoresClient

            self._vector_stores = VectorStoresClient(client_wrapper=self._client_wrapper)
        return self._vector_stores

    @property
    def user_feedback(self):
        if self._user_feedback is None:
            from .user_feedback.client import UserFeedbackClient

            self._user_feedback = UserFeedbackClient(client_wrapper=self._client_wrapper)
        return self._user_feedback

    @property
    def connectors(self):
        if self._connectors is None:
            from .connectors.client import ConnectorsClient

            self._connectors = ConnectorsClient(client_wrapper=self._client_wrapper)
        return self._connectors

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth


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
    base_url : str
        The base url to use for requests from the client.

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            base_url=base_url,
            username=username,
            password=password,
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
        self._user: typing.Optional[AsyncUserClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._a2a: typing.Optional[AsyncA2AClient] = None
        self._providers: typing.Optional[AsyncProvidersClient] = None
        self._provider_discovery: typing.Optional[AsyncProviderDiscoveryClient] = None
        self._provider_builds: typing.Optional[AsyncProviderBuildsClient] = None
        self._model_providers: typing.Optional[AsyncModelProvidersClient] = None
        self._configurations: typing.Optional[AsyncConfigurationsClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._variables: typing.Optional[AsyncVariablesClient] = None
        self._contexts: typing.Optional[AsyncContextsClient] = None
        self._openai: typing.Optional[AsyncOpenaiClient] = None
        self._vector_stores: typing.Optional[AsyncVectorStoresClient] = None
        self._user_feedback: typing.Optional[AsyncUserFeedbackClient] = None
        self._connectors: typing.Optional[AsyncConnectorsClient] = None
        self._auth: typing.Optional[AsyncAuthClient] = None

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def a2a(self):
        if self._a2a is None:
            from .a2a.client import AsyncA2AClient

            self._a2a = AsyncA2AClient(client_wrapper=self._client_wrapper)
        return self._a2a

    @property
    def providers(self):
        if self._providers is None:
            from .providers.client import AsyncProvidersClient

            self._providers = AsyncProvidersClient(client_wrapper=self._client_wrapper)
        return self._providers

    @property
    def provider_discovery(self):
        if self._provider_discovery is None:
            from .provider_discovery.client import AsyncProviderDiscoveryClient

            self._provider_discovery = AsyncProviderDiscoveryClient(client_wrapper=self._client_wrapper)
        return self._provider_discovery

    @property
    def provider_builds(self):
        if self._provider_builds is None:
            from .provider_builds.client import AsyncProviderBuildsClient

            self._provider_builds = AsyncProviderBuildsClient(client_wrapper=self._client_wrapper)
        return self._provider_builds

    @property
    def model_providers(self):
        if self._model_providers is None:
            from .model_providers.client import AsyncModelProvidersClient

            self._model_providers = AsyncModelProvidersClient(client_wrapper=self._client_wrapper)
        return self._model_providers

    @property
    def configurations(self):
        if self._configurations is None:
            from .configurations.client import AsyncConfigurationsClient

            self._configurations = AsyncConfigurationsClient(client_wrapper=self._client_wrapper)
        return self._configurations

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def variables(self):
        if self._variables is None:
            from .variables.client import AsyncVariablesClient

            self._variables = AsyncVariablesClient(client_wrapper=self._client_wrapper)
        return self._variables

    @property
    def contexts(self):
        if self._contexts is None:
            from .contexts.client import AsyncContextsClient

            self._contexts = AsyncContextsClient(client_wrapper=self._client_wrapper)
        return self._contexts

    @property
    def openai(self):
        if self._openai is None:
            from .openai.client import AsyncOpenaiClient

            self._openai = AsyncOpenaiClient(client_wrapper=self._client_wrapper)
        return self._openai

    @property
    def vector_stores(self):
        if self._vector_stores is None:
            from .vector_stores.client import AsyncVectorStoresClient

            self._vector_stores = AsyncVectorStoresClient(client_wrapper=self._client_wrapper)
        return self._vector_stores

    @property
    def user_feedback(self):
        if self._user_feedback is None:
            from .user_feedback.client import AsyncUserFeedbackClient

            self._user_feedback = AsyncUserFeedbackClient(client_wrapper=self._client_wrapper)
        return self._user_feedback

    @property
    def connectors(self):
        if self._connectors is None:
            from .connectors.client import AsyncConnectorsClient

            self._connectors = AsyncConnectorsClient(client_wrapper=self._client_wrapper)
        return self._connectors

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth
