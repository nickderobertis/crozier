

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .cle.client import AsyncCleClient, CleClient
    from .tea_artifact.client import AsyncTeaArtifactClient, TeaArtifactClient
    from .tea_component.client import AsyncTeaComponentClient, TeaComponentClient
    from .tea_component_release.client import AsyncTeaComponentReleaseClient, TeaComponentReleaseClient
    from .tea_discovery.client import AsyncTeaDiscoveryClient, TeaDiscoveryClient
    from .tea_product.client import AsyncTeaProductClient, TeaProductClient
    from .tea_product_release.client import AsyncTeaProductReleaseClient, TeaProductReleaseClient


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._tea_product: typing.Optional[TeaProductClient] = None
        self._tea_product_release: typing.Optional[TeaProductReleaseClient] = None
        self._cle: typing.Optional[CleClient] = None
        self._tea_component: typing.Optional[TeaComponentClient] = None
        self._tea_component_release: typing.Optional[TeaComponentReleaseClient] = None
        self._tea_artifact: typing.Optional[TeaArtifactClient] = None
        self._tea_discovery: typing.Optional[TeaDiscoveryClient] = None

    @property
    def tea_product(self):
        if self._tea_product is None:
            from .tea_product.client import TeaProductClient

            self._tea_product = TeaProductClient(client_wrapper=self._client_wrapper)
        return self._tea_product

    @property
    def tea_product_release(self):
        if self._tea_product_release is None:
            from .tea_product_release.client import TeaProductReleaseClient

            self._tea_product_release = TeaProductReleaseClient(client_wrapper=self._client_wrapper)
        return self._tea_product_release

    @property
    def cle(self):
        if self._cle is None:
            from .cle.client import CleClient

            self._cle = CleClient(client_wrapper=self._client_wrapper)
        return self._cle

    @property
    def tea_component(self):
        if self._tea_component is None:
            from .tea_component.client import TeaComponentClient

            self._tea_component = TeaComponentClient(client_wrapper=self._client_wrapper)
        return self._tea_component

    @property
    def tea_component_release(self):
        if self._tea_component_release is None:
            from .tea_component_release.client import TeaComponentReleaseClient

            self._tea_component_release = TeaComponentReleaseClient(client_wrapper=self._client_wrapper)
        return self._tea_component_release

    @property
    def tea_artifact(self):
        if self._tea_artifact is None:
            from .tea_artifact.client import TeaArtifactClient

            self._tea_artifact = TeaArtifactClient(client_wrapper=self._client_wrapper)
        return self._tea_artifact

    @property
    def tea_discovery(self):
        if self._tea_discovery is None:
            from .tea_discovery.client import TeaDiscoveryClient

            self._tea_discovery = TeaDiscoveryClient(client_wrapper=self._client_wrapper)
        return self._tea_discovery


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._tea_product: typing.Optional[AsyncTeaProductClient] = None
        self._tea_product_release: typing.Optional[AsyncTeaProductReleaseClient] = None
        self._cle: typing.Optional[AsyncCleClient] = None
        self._tea_component: typing.Optional[AsyncTeaComponentClient] = None
        self._tea_component_release: typing.Optional[AsyncTeaComponentReleaseClient] = None
        self._tea_artifact: typing.Optional[AsyncTeaArtifactClient] = None
        self._tea_discovery: typing.Optional[AsyncTeaDiscoveryClient] = None

    @property
    def tea_product(self):
        if self._tea_product is None:
            from .tea_product.client import AsyncTeaProductClient

            self._tea_product = AsyncTeaProductClient(client_wrapper=self._client_wrapper)
        return self._tea_product

    @property
    def tea_product_release(self):
        if self._tea_product_release is None:
            from .tea_product_release.client import AsyncTeaProductReleaseClient

            self._tea_product_release = AsyncTeaProductReleaseClient(client_wrapper=self._client_wrapper)
        return self._tea_product_release

    @property
    def cle(self):
        if self._cle is None:
            from .cle.client import AsyncCleClient

            self._cle = AsyncCleClient(client_wrapper=self._client_wrapper)
        return self._cle

    @property
    def tea_component(self):
        if self._tea_component is None:
            from .tea_component.client import AsyncTeaComponentClient

            self._tea_component = AsyncTeaComponentClient(client_wrapper=self._client_wrapper)
        return self._tea_component

    @property
    def tea_component_release(self):
        if self._tea_component_release is None:
            from .tea_component_release.client import AsyncTeaComponentReleaseClient

            self._tea_component_release = AsyncTeaComponentReleaseClient(client_wrapper=self._client_wrapper)
        return self._tea_component_release

    @property
    def tea_artifact(self):
        if self._tea_artifact is None:
            from .tea_artifact.client import AsyncTeaArtifactClient

            self._tea_artifact = AsyncTeaArtifactClient(client_wrapper=self._client_wrapper)
        return self._tea_artifact

    @property
    def tea_discovery(self):
        if self._tea_discovery is None:
            from .tea_discovery.client import AsyncTeaDiscoveryClient

            self._tea_discovery = AsyncTeaDiscoveryClient(client_wrapper=self._client_wrapper)
        return self._tea_discovery


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
