

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.sign_token_payload_payload import SignTokenPayloadPayload
from .types.token import Token
from .types.token_response import TokenResponse
from .types.token_response_legacy import TokenResponseLegacy


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    okapi_tenant : str
    okapi_url : str
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
        okapi_tenant="YOUR_OKAPI_TENANT",
        okapi_url="YOUR_OKAPI_URL",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        okapi_tenant: str,
        okapi_url: str,
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
            okapi_tenant=okapi_tenant,
            okapi_url=okapi_url,
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

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def token_legacy(
        self, *, payload: SignTokenPayloadPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponseLegacy:
        """
        Deprecated. Will be removed in a future release. Please use /token/sign instead. Returns a signed, non-expiring legacy access token.

        Parameters
        ----------
        payload : SignTokenPayloadPayload
            The payload of the token signing request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponseLegacy
            Created and signed token successfully

        Examples
        --------
        from fern import FernApi, SignTokenPayloadPayload

        client = FernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )
        client.token_legacy(
            payload=SignTokenPayloadPayload(
                sub="sub",
            ),
        )
        """
        _response = self._raw_client.token_legacy(payload=payload, request_options=request_options)
        return _response.data

    def token_sign_legacy(
        self, *, user_id: str, sub: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Returns a signed, expiring refresh token. This is a legacy endpoint and should not be
        called by new code and will soon be fully depreciated.

        Parameters
        ----------
        user_id : str
            The user id of the request

        sub : str
            The subject (user id) of the request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Created and signed token successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )
        client.token_sign_legacy(
            user_id="userId",
            sub="sub",
        )
        """
        _response = self._raw_client.token_sign_legacy(user_id=user_id, sub=sub, request_options=request_options)
        return _response.data

    def token_sign(
        self, *, payload: SignTokenPayloadPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Returns a signed, expiring access token and refresh token. Also returns the expiration
        of each token in the body of the response. The access token time to live is 10 minutes and
        the refresh token is one week.

        Parameters
        ----------
        payload : SignTokenPayloadPayload
            The payload of the token signing request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Created and signed tokens successfully

        Examples
        --------
        from fern import FernApi, SignTokenPayloadPayload

        client = FernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )
        client.token_sign(
            payload=SignTokenPayloadPayload(
                sub="sub",
            ),
        )
        """
        _response = self._raw_client.token_sign(payload=payload, request_options=request_options)
        return _response.data

    def token_refresh(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Returns a new refresh token and a new access token. Also returns the expiration of each token
        in the body of the response. Time to live is 10 minutes for the access token and one week for
        the refresh token.

        Parameters
        ----------
        refresh_token : str
            The JWE refresh token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Refreshed tokens successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )
        client.token_refresh(
            refresh_token="refreshToken",
        )
        """
        _response = self._raw_client.token_refresh(refresh_token=refresh_token, request_options=request_options)
        return _response.data

    def token_invalidate(self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidate a single refresh token. An access token cannot be invalidated and remains valid until its expiration time; this is by design because the access token is stateless.

        Parameters
        ----------
        refresh_token : str
            The JWE refresh token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )
        client.token_invalidate(
            refresh_token="refreshToken",
        )
        """
        _response = self._raw_client.token_invalidate(refresh_token=refresh_token, request_options=request_options)
        return _response.data

    def token_invalidate_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidate all refresh tokens for a user. An access token cannot be invalidated and remains valid until its expiration time; this is by design because the access token is stateless.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )
        client.token_invalidate_all()
        """
        _response = self._raw_client.token_invalidate_all(request_options=request_options)
        return _response.data


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

    okapi_tenant : str
    okapi_url : str
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
        okapi_tenant="YOUR_OKAPI_TENANT",
        okapi_url="YOUR_OKAPI_URL",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        okapi_tenant: str,
        okapi_url: str,
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
            okapi_tenant=okapi_tenant,
            okapi_url=okapi_url,
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

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def token_legacy(
        self, *, payload: SignTokenPayloadPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponseLegacy:
        """
        Deprecated. Will be removed in a future release. Please use /token/sign instead. Returns a signed, non-expiring legacy access token.

        Parameters
        ----------
        payload : SignTokenPayloadPayload
            The payload of the token signing request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponseLegacy
            Created and signed token successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SignTokenPayloadPayload

        client = AsyncFernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.token_legacy(
                payload=SignTokenPayloadPayload(
                    sub="sub",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_legacy(payload=payload, request_options=request_options)
        return _response.data

    async def token_sign_legacy(
        self, *, user_id: str, sub: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Returns a signed, expiring refresh token. This is a legacy endpoint and should not be
        called by new code and will soon be fully depreciated.

        Parameters
        ----------
        user_id : str
            The user id of the request

        sub : str
            The subject (user id) of the request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Created and signed token successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.token_sign_legacy(
                user_id="userId",
                sub="sub",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_sign_legacy(user_id=user_id, sub=sub, request_options=request_options)
        return _response.data

    async def token_sign(
        self, *, payload: SignTokenPayloadPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Returns a signed, expiring access token and refresh token. Also returns the expiration
        of each token in the body of the response. The access token time to live is 10 minutes and
        the refresh token is one week.

        Parameters
        ----------
        payload : SignTokenPayloadPayload
            The payload of the token signing request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Created and signed tokens successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SignTokenPayloadPayload

        client = AsyncFernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.token_sign(
                payload=SignTokenPayloadPayload(
                    sub="sub",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_sign(payload=payload, request_options=request_options)
        return _response.data

    async def token_refresh(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Returns a new refresh token and a new access token. Also returns the expiration of each token
        in the body of the response. Time to live is 10 minutes for the access token and one week for
        the refresh token.

        Parameters
        ----------
        refresh_token : str
            The JWE refresh token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Refreshed tokens successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.token_refresh(
                refresh_token="refreshToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_refresh(refresh_token=refresh_token, request_options=request_options)
        return _response.data

    async def token_invalidate(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Invalidate a single refresh token. An access token cannot be invalidated and remains valid until its expiration time; this is by design because the access token is stateless.

        Parameters
        ----------
        refresh_token : str
            The JWE refresh token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.token_invalidate(
                refresh_token="refreshToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_invalidate(
            refresh_token=refresh_token, request_options=request_options
        )
        return _response.data

    async def token_invalidate_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidate all refresh tokens for a user. An access token cannot be invalidated and remains valid until its expiration time; this is by design because the access token is stateless.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            okapi_tenant="YOUR_OKAPI_TENANT",
            okapi_url="YOUR_OKAPI_URL",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.token_invalidate_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.token_invalidate_all(request_options=request_options)
        return _response.data
