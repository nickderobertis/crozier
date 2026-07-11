

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper

if typing.TYPE_CHECKING:
    from .apikeyauth.client import ApikeyauthClient, AsyncApikeyauthClient
    from .basicauth.client import AsyncBasicauthClient, BasicauthClient
    from .bearerauth.client import AsyncBearerauthClient, BearerauthClient
    from .oauth.client import AsyncOauthClient, OauthClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._apikeyauth: typing.Optional[ApikeyauthClient] = None
        self._basicauth: typing.Optional[BasicauthClient] = None
        self._bearerauth: typing.Optional[BearerauthClient] = None
        self._oauth: typing.Optional[OauthClient] = None

    @property
    def apikeyauth(self):
        if self._apikeyauth is None:
            from .apikeyauth.client import ApikeyauthClient

            self._apikeyauth = ApikeyauthClient(client_wrapper=self._client_wrapper)
        return self._apikeyauth

    @property
    def basicauth(self):
        if self._basicauth is None:
            from .basicauth.client import BasicauthClient

            self._basicauth = BasicauthClient(client_wrapper=self._client_wrapper)
        return self._basicauth

    @property
    def bearerauth(self):
        if self._bearerauth is None:
            from .bearerauth.client import BearerauthClient

            self._bearerauth = BearerauthClient(client_wrapper=self._client_wrapper)
        return self._bearerauth

    @property
    def oauth(self):
        if self._oauth is None:
            from .oauth.client import OauthClient

            self._oauth = OauthClient(client_wrapper=self._client_wrapper)
        return self._oauth


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._apikeyauth: typing.Optional[AsyncApikeyauthClient] = None
        self._basicauth: typing.Optional[AsyncBasicauthClient] = None
        self._bearerauth: typing.Optional[AsyncBearerauthClient] = None
        self._oauth: typing.Optional[AsyncOauthClient] = None

    @property
    def apikeyauth(self):
        if self._apikeyauth is None:
            from .apikeyauth.client import AsyncApikeyauthClient

            self._apikeyauth = AsyncApikeyauthClient(client_wrapper=self._client_wrapper)
        return self._apikeyauth

    @property
    def basicauth(self):
        if self._basicauth is None:
            from .basicauth.client import AsyncBasicauthClient

            self._basicauth = AsyncBasicauthClient(client_wrapper=self._client_wrapper)
        return self._basicauth

    @property
    def bearerauth(self):
        if self._bearerauth is None:
            from .bearerauth.client import AsyncBearerauthClient

            self._bearerauth = AsyncBearerauthClient(client_wrapper=self._client_wrapper)
        return self._bearerauth

    @property
    def oauth(self):
        if self._oauth is None:
            from .oauth.client import AsyncOauthClient

            self._oauth = AsyncOauthClient(client_wrapper=self._client_wrapper)
        return self._oauth
