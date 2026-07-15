

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .contentpro_search.client import AsyncContentproSearchClient, ContentproSearchClient
    from .contentpro_similar_text.client import AsyncContentproSimilarTextClient, ContentproSimilarTextClient
    from .search.client import AsyncSearchClient, SearchClient
    from .similar.client import AsyncSimilarClient, SimilarClient


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
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
        )
        self._contentpro_search: typing.Optional[ContentproSearchClient] = None
        self._contentpro_similar_text: typing.Optional[ContentproSimilarTextClient] = None
        self._search: typing.Optional[SearchClient] = None
        self._similar: typing.Optional[SimilarClient] = None

    @property
    def contentpro_search(self):
        if self._contentpro_search is None:
            from .contentpro_search.client import ContentproSearchClient

            self._contentpro_search = ContentproSearchClient(client_wrapper=self._client_wrapper)
        return self._contentpro_search

    @property
    def contentpro_similar_text(self):
        if self._contentpro_similar_text is None:
            from .contentpro_similar_text.client import ContentproSimilarTextClient

            self._contentpro_similar_text = ContentproSimilarTextClient(client_wrapper=self._client_wrapper)
        return self._contentpro_similar_text

    @property
    def search(self):
        if self._search is None:
            from .search.client import SearchClient

            self._search = SearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def similar(self):
        if self._similar is None:
            from .similar.client import SimilarClient

            self._similar = SimilarClient(client_wrapper=self._client_wrapper)
        return self._similar


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._contentpro_search: typing.Optional[AsyncContentproSearchClient] = None
        self._contentpro_similar_text: typing.Optional[AsyncContentproSimilarTextClient] = None
        self._search: typing.Optional[AsyncSearchClient] = None
        self._similar: typing.Optional[AsyncSimilarClient] = None

    @property
    def contentpro_search(self):
        if self._contentpro_search is None:
            from .contentpro_search.client import AsyncContentproSearchClient

            self._contentpro_search = AsyncContentproSearchClient(client_wrapper=self._client_wrapper)
        return self._contentpro_search

    @property
    def contentpro_similar_text(self):
        if self._contentpro_similar_text is None:
            from .contentpro_similar_text.client import AsyncContentproSimilarTextClient

            self._contentpro_similar_text = AsyncContentproSimilarTextClient(client_wrapper=self._client_wrapper)
        return self._contentpro_similar_text

    @property
    def search(self):
        if self._search is None:
            from .search.client import AsyncSearchClient

            self._search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def similar(self):
        if self._similar is None:
            from .similar.client import AsyncSimilarClient

            self._similar = AsyncSimilarClient(client_wrapper=self._client_wrapper)
        return self._similar


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
