

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .c.client import AsyncCClient, CClient
    from .datatype.client import AsyncDatatypeClient, DatatypeClient
    from .e.client import AsyncEClient, EClient
    from .g.client import AsyncGClient, GClient
    from .id_scheme.client import AsyncIdSchemeClient, IdSchemeClient
    from .invrel.client import AsyncInvrelClient, InvrelClient
    from .location.client import AsyncLocationClient, LocationClient
    from .m.client import AsyncMClient, MClient
    from .rel.client import AsyncRelClient, RelClient
    from .t.client import AsyncTClient, TClient
    from .thesaurus.client import AsyncThesaurusClient, ThesaurusClient
    from .type.client import AsyncTypeClient, TypeClient
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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._m: typing.Optional[MClient] = None
        self._g: typing.Optional[GClient] = None
        self._t: typing.Optional[TClient] = None
        self._c: typing.Optional[CClient] = None
        self._e: typing.Optional[EClient] = None
        self._rel: typing.Optional[RelClient] = None
        self._invrel: typing.Optional[InvrelClient] = None
        self._datatype: typing.Optional[DatatypeClient] = None
        self._type: typing.Optional[TypeClient] = None
        self._location: typing.Optional[LocationClient] = None
        self._id_scheme: typing.Optional[IdSchemeClient] = None
        self._thesaurus: typing.Optional[ThesaurusClient] = None
        self._user: typing.Optional[UserClient] = None

    @property
    def m(self):
        if self._m is None:
            from .m.client import MClient

            self._m = MClient(client_wrapper=self._client_wrapper)
        return self._m

    @property
    def g(self):
        if self._g is None:
            from .g.client import GClient

            self._g = GClient(client_wrapper=self._client_wrapper)
        return self._g

    @property
    def t(self):
        if self._t is None:
            from .t.client import TClient

            self._t = TClient(client_wrapper=self._client_wrapper)
        return self._t

    @property
    def c(self):
        if self._c is None:
            from .c.client import CClient

            self._c = CClient(client_wrapper=self._client_wrapper)
        return self._c

    @property
    def e(self):
        if self._e is None:
            from .e.client import EClient

            self._e = EClient(client_wrapper=self._client_wrapper)
        return self._e

    @property
    def rel(self):
        if self._rel is None:
            from .rel.client import RelClient

            self._rel = RelClient(client_wrapper=self._client_wrapper)
        return self._rel

    @property
    def invrel(self):
        if self._invrel is None:
            from .invrel.client import InvrelClient

            self._invrel = InvrelClient(client_wrapper=self._client_wrapper)
        return self._invrel

    @property
    def datatype(self):
        if self._datatype is None:
            from .datatype.client import DatatypeClient

            self._datatype = DatatypeClient(client_wrapper=self._client_wrapper)
        return self._datatype

    @property
    def type(self):
        if self._type is None:
            from .type.client import TypeClient

            self._type = TypeClient(client_wrapper=self._client_wrapper)
        return self._type

    @property
    def location(self):
        if self._location is None:
            from .location.client import LocationClient

            self._location = LocationClient(client_wrapper=self._client_wrapper)
        return self._location

    @property
    def id_scheme(self):
        if self._id_scheme is None:
            from .id_scheme.client import IdSchemeClient

            self._id_scheme = IdSchemeClient(client_wrapper=self._client_wrapper)
        return self._id_scheme

    @property
    def thesaurus(self):
        if self._thesaurus is None:
            from .thesaurus.client import ThesaurusClient

            self._thesaurus = ThesaurusClient(client_wrapper=self._client_wrapper)
        return self._thesaurus

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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._m: typing.Optional[AsyncMClient] = None
        self._g: typing.Optional[AsyncGClient] = None
        self._t: typing.Optional[AsyncTClient] = None
        self._c: typing.Optional[AsyncCClient] = None
        self._e: typing.Optional[AsyncEClient] = None
        self._rel: typing.Optional[AsyncRelClient] = None
        self._invrel: typing.Optional[AsyncInvrelClient] = None
        self._datatype: typing.Optional[AsyncDatatypeClient] = None
        self._type: typing.Optional[AsyncTypeClient] = None
        self._location: typing.Optional[AsyncLocationClient] = None
        self._id_scheme: typing.Optional[AsyncIdSchemeClient] = None
        self._thesaurus: typing.Optional[AsyncThesaurusClient] = None
        self._user: typing.Optional[AsyncUserClient] = None

    @property
    def m(self):
        if self._m is None:
            from .m.client import AsyncMClient

            self._m = AsyncMClient(client_wrapper=self._client_wrapper)
        return self._m

    @property
    def g(self):
        if self._g is None:
            from .g.client import AsyncGClient

            self._g = AsyncGClient(client_wrapper=self._client_wrapper)
        return self._g

    @property
    def t(self):
        if self._t is None:
            from .t.client import AsyncTClient

            self._t = AsyncTClient(client_wrapper=self._client_wrapper)
        return self._t

    @property
    def c(self):
        if self._c is None:
            from .c.client import AsyncCClient

            self._c = AsyncCClient(client_wrapper=self._client_wrapper)
        return self._c

    @property
    def e(self):
        if self._e is None:
            from .e.client import AsyncEClient

            self._e = AsyncEClient(client_wrapper=self._client_wrapper)
        return self._e

    @property
    def rel(self):
        if self._rel is None:
            from .rel.client import AsyncRelClient

            self._rel = AsyncRelClient(client_wrapper=self._client_wrapper)
        return self._rel

    @property
    def invrel(self):
        if self._invrel is None:
            from .invrel.client import AsyncInvrelClient

            self._invrel = AsyncInvrelClient(client_wrapper=self._client_wrapper)
        return self._invrel

    @property
    def datatype(self):
        if self._datatype is None:
            from .datatype.client import AsyncDatatypeClient

            self._datatype = AsyncDatatypeClient(client_wrapper=self._client_wrapper)
        return self._datatype

    @property
    def type(self):
        if self._type is None:
            from .type.client import AsyncTypeClient

            self._type = AsyncTypeClient(client_wrapper=self._client_wrapper)
        return self._type

    @property
    def location(self):
        if self._location is None:
            from .location.client import AsyncLocationClient

            self._location = AsyncLocationClient(client_wrapper=self._client_wrapper)
        return self._location

    @property
    def id_scheme(self):
        if self._id_scheme is None:
            from .id_scheme.client import AsyncIdSchemeClient

            self._id_scheme = AsyncIdSchemeClient(client_wrapper=self._client_wrapper)
        return self._id_scheme

    @property
    def thesaurus(self):
        if self._thesaurus is None:
            from .thesaurus.client import AsyncThesaurusClient

            self._thesaurus = AsyncThesaurusClient(client_wrapper=self._client_wrapper)
        return self._thesaurus

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
