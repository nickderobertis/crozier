

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .api_key.client import ApiKeyClient, AsyncApiKeyClient
    from .document.client import AsyncDocumentClient, DocumentClient
    from .index.client import AsyncIndexClient, IndexClient
    from .info.client import AsyncInfoClient, InfoClient
    from .iterator.client import AsyncIteratorClient, IteratorClient
    from .pdf_file.client import AsyncPdfFileClient, PdfFileClient
    from .query.client import AsyncQueryClient, QueryClient


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



    apikey : typing.Optional[str]
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
        apikey="YOUR_APIKEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apikey: typing.Optional[str] = None,
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
            apikey=apikey,
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
        self._api_key: typing.Optional[ApiKeyClient] = None
        self._index: typing.Optional[IndexClient] = None
        self._iterator: typing.Optional[IteratorClient] = None
        self._document: typing.Optional[DocumentClient] = None
        self._pdf_file: typing.Optional[PdfFileClient] = None
        self._query: typing.Optional[QueryClient] = None

    @property
    def info(self):
        if self._info is None:
            from .info.client import InfoClient

            self._info = InfoClient(client_wrapper=self._client_wrapper)
        return self._info

    @property
    def api_key(self):
        if self._api_key is None:
            from .api_key.client import ApiKeyClient

            self._api_key = ApiKeyClient(client_wrapper=self._client_wrapper)
        return self._api_key

    @property
    def index(self):
        if self._index is None:
            from .index.client import IndexClient

            self._index = IndexClient(client_wrapper=self._client_wrapper)
        return self._index

    @property
    def iterator(self):
        if self._iterator is None:
            from .iterator.client import IteratorClient

            self._iterator = IteratorClient(client_wrapper=self._client_wrapper)
        return self._iterator

    @property
    def document(self):
        if self._document is None:
            from .document.client import DocumentClient

            self._document = DocumentClient(client_wrapper=self._client_wrapper)
        return self._document

    @property
    def pdf_file(self):
        if self._pdf_file is None:
            from .pdf_file.client import PdfFileClient

            self._pdf_file = PdfFileClient(client_wrapper=self._client_wrapper)
        return self._pdf_file

    @property
    def query(self):
        if self._query is None:
            from .query.client import QueryClient

            self._query = QueryClient(client_wrapper=self._client_wrapper)
        return self._query


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



    apikey : typing.Optional[str]
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
        apikey="YOUR_APIKEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apikey: typing.Optional[str] = None,
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
            apikey=apikey,
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
        self._info: typing.Optional[AsyncInfoClient] = None
        self._api_key: typing.Optional[AsyncApiKeyClient] = None
        self._index: typing.Optional[AsyncIndexClient] = None
        self._iterator: typing.Optional[AsyncIteratorClient] = None
        self._document: typing.Optional[AsyncDocumentClient] = None
        self._pdf_file: typing.Optional[AsyncPdfFileClient] = None
        self._query: typing.Optional[AsyncQueryClient] = None

    @property
    def info(self):
        if self._info is None:
            from .info.client import AsyncInfoClient

            self._info = AsyncInfoClient(client_wrapper=self._client_wrapper)
        return self._info

    @property
    def api_key(self):
        if self._api_key is None:
            from .api_key.client import AsyncApiKeyClient

            self._api_key = AsyncApiKeyClient(client_wrapper=self._client_wrapper)
        return self._api_key

    @property
    def index(self):
        if self._index is None:
            from .index.client import AsyncIndexClient

            self._index = AsyncIndexClient(client_wrapper=self._client_wrapper)
        return self._index

    @property
    def iterator(self):
        if self._iterator is None:
            from .iterator.client import AsyncIteratorClient

            self._iterator = AsyncIteratorClient(client_wrapper=self._client_wrapper)
        return self._iterator

    @property
    def document(self):
        if self._document is None:
            from .document.client import AsyncDocumentClient

            self._document = AsyncDocumentClient(client_wrapper=self._client_wrapper)
        return self._document

    @property
    def pdf_file(self):
        if self._pdf_file is None:
            from .pdf_file.client import AsyncPdfFileClient

            self._pdf_file = AsyncPdfFileClient(client_wrapper=self._client_wrapper)
        return self._pdf_file

    @property
    def query(self):
        if self._query is None:
            from .query.client import AsyncQueryClient

            self._query = AsyncQueryClient(client_wrapper=self._client_wrapper)
        return self._query


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
