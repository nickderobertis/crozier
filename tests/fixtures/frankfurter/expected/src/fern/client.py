

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.currency import Currency
from .types.currency_detail import CurrencyDetail
from .types.get_currencies_request_scope import GetCurrenciesRequestScope
from .types.get_rates_request_expand import GetRatesRequestExpand
from .types.get_rates_request_group import GetRatesRequestGroup
from .types.provider import Provider
from .types.rate import Rate


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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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

    def get_rates(
        self,
        *,
        date: typing.Optional[dt.date] = None,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        base: typing.Optional[str] = None,
        quotes: typing.Optional[str] = None,
        providers: typing.Optional[str] = None,
        group: typing.Optional[GetRatesRequestGroup] = None,
        expand: typing.Optional[GetRatesRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Rate]:
        """
        Returns exchange rates blended across providers. Without date params, returns the latest rates. Each record is a single currency pair. The response includes an identity record for the base currency (base equals quote, rate 1), subject to the quotes filter like any other record.

        Parameters
        ----------
        date : typing.Optional[dt.date]
            Specific date (YYYY-MM-DD). Cannot be combined with from/to.

        from_ : typing.Optional[dt.date]
            Start of date range (YYYY-MM-DD)

        to : typing.Optional[dt.date]
            End of date range (YYYY-MM-DD). Defaults to today.

        base : typing.Optional[str]
            Base currency (default: EUR)

        quotes : typing.Optional[str]
            Comma-separated list of quote currencies to include

        providers : typing.Optional[str]
            Comma-separated list of data providers to include

        group : typing.Optional[GetRatesRequestGroup]
            Downsample rates by time period. Only applies to date ranges.

        expand : typing.Optional[GetRatesRequestExpand]
            Comma-separated list of optional fields to include per record. Currently supports `providers`, which adds an array of `{ key, date, rate }` objects per record showing each provider's individual observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by a currency peg) are flagged with `excluded: true`. The field is omitted on synthesized peg rows where no provider published the quote. In CSV output, the `providers` column is encoded as `KEY:RATE` pairs joined by `|`, with a trailing `*` on excluded entries (e.g. `ECB:0.92|FED:1.50*`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Rate]
            Exchange rates

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi()
        client.get_rates(
            date=datetime.date.fromisoformat(
                "2024-01-15",
            ),
            from_=datetime.date.fromisoformat(
                "2024-01-01",
            ),
            to=datetime.date.fromisoformat(
                "2024-01-31",
            ),
            base="USD",
            quotes="USD,GBP,JPY",
            providers="ECB,TCMB",
        )
        """
        _response = self._raw_client.get_rates(
            date=date,
            from_=from_,
            to=to,
            base=base,
            quotes=quotes,
            providers=providers,
            group=group,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

    def get_rate(
        self,
        base: str,
        quote: str,
        *,
        date: typing.Optional[dt.date] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rate:
        """
        Returns the blended exchange rate for a single currency pair. Without a date param, returns the latest rate. A same-currency pair returns the identity rate of 1.

        Parameters
        ----------
        base : str

        quote : str

        date : typing.Optional[dt.date]
            Specific date (YYYY-MM-DD). Cannot be combined with from/to.

        providers : typing.Optional[str]
            Comma-separated list of data providers to include

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rate
            Exchange rate

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi()
        client.get_rate(
            base="EUR",
            quote="USD",
            date=datetime.date.fromisoformat(
                "2024-01-15",
            ),
            providers="ECB,TCMB",
        )
        """
        _response = self._raw_client.get_rate(
            base, quote, date=date, providers=providers, request_options=request_options
        )
        return _response.data

    def get_currency(self, code: str, *, request_options: typing.Optional[RequestOptions] = None) -> CurrencyDetail:
        """
        Returns details for a single currency, including provider information or peg metadata.

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyDetail
            Currency details

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_currency(
            code="USD",
        )
        """
        _response = self._raw_client.get_currency(code, request_options=request_options)
        return _response.data

    def get_currencies(
        self,
        *,
        scope: typing.Optional[GetCurrenciesRequestScope] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Currency]:
        """
        Returns available currencies with their names and date ranges. By default, only active currencies are included.

        Parameters
        ----------
        scope : typing.Optional[GetCurrenciesRequestScope]
            Set to 'all' to include legacy currencies

        providers : typing.Optional[str]
            Comma-separated list of data providers to include

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Currency]
            Available currencies

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_currencies(
            providers="ECB,TCMB",
        )
        """
        _response = self._raw_client.get_currencies(scope=scope, providers=providers, request_options=request_options)
        return _response.data

    def get_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Provider]:
        """
        Returns available exchange rate data providers with their base currency.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Provider]
            Available providers

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_providers()
        """
        _response = self._raw_client.get_providers(request_options=request_options)
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
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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

    async def get_rates(
        self,
        *,
        date: typing.Optional[dt.date] = None,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        base: typing.Optional[str] = None,
        quotes: typing.Optional[str] = None,
        providers: typing.Optional[str] = None,
        group: typing.Optional[GetRatesRequestGroup] = None,
        expand: typing.Optional[GetRatesRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Rate]:
        """
        Returns exchange rates blended across providers. Without date params, returns the latest rates. Each record is a single currency pair. The response includes an identity record for the base currency (base equals quote, rate 1), subject to the quotes filter like any other record.

        Parameters
        ----------
        date : typing.Optional[dt.date]
            Specific date (YYYY-MM-DD). Cannot be combined with from/to.

        from_ : typing.Optional[dt.date]
            Start of date range (YYYY-MM-DD)

        to : typing.Optional[dt.date]
            End of date range (YYYY-MM-DD). Defaults to today.

        base : typing.Optional[str]
            Base currency (default: EUR)

        quotes : typing.Optional[str]
            Comma-separated list of quote currencies to include

        providers : typing.Optional[str]
            Comma-separated list of data providers to include

        group : typing.Optional[GetRatesRequestGroup]
            Downsample rates by time period. Only applies to date ranges.

        expand : typing.Optional[GetRatesRequestExpand]
            Comma-separated list of optional fields to include per record. Currently supports `providers`, which adds an array of `{ key, date, rate }` objects per record showing each provider's individual observation date and rate. Outliers excluded from the blend (and providers whose rate was overridden by a currency peg) are flagged with `excluded: true`. The field is omitted on synthesized peg rows where no provider published the quote. In CSV output, the `providers` column is encoded as `KEY:RATE` pairs joined by `|`, with a trailing `*` on excluded entries (e.g. `ECB:0.92|FED:1.50*`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Rate]
            Exchange rates

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_rates(
                date=datetime.date.fromisoformat(
                    "2024-01-15",
                ),
                from_=datetime.date.fromisoformat(
                    "2024-01-01",
                ),
                to=datetime.date.fromisoformat(
                    "2024-01-31",
                ),
                base="USD",
                quotes="USD,GBP,JPY",
                providers="ECB,TCMB",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rates(
            date=date,
            from_=from_,
            to=to,
            base=base,
            quotes=quotes,
            providers=providers,
            group=group,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

    async def get_rate(
        self,
        base: str,
        quote: str,
        *,
        date: typing.Optional[dt.date] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rate:
        """
        Returns the blended exchange rate for a single currency pair. Without a date param, returns the latest rate. A same-currency pair returns the identity rate of 1.

        Parameters
        ----------
        base : str

        quote : str

        date : typing.Optional[dt.date]
            Specific date (YYYY-MM-DD). Cannot be combined with from/to.

        providers : typing.Optional[str]
            Comma-separated list of data providers to include

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rate
            Exchange rate

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_rate(
                base="EUR",
                quote="USD",
                date=datetime.date.fromisoformat(
                    "2024-01-15",
                ),
                providers="ECB,TCMB",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rate(
            base, quote, date=date, providers=providers, request_options=request_options
        )
        return _response.data

    async def get_currency(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrencyDetail:
        """
        Returns details for a single currency, including provider information or peg metadata.

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyDetail
            Currency details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_currency(
                code="USD",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_currency(code, request_options=request_options)
        return _response.data

    async def get_currencies(
        self,
        *,
        scope: typing.Optional[GetCurrenciesRequestScope] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Currency]:
        """
        Returns available currencies with their names and date ranges. By default, only active currencies are included.

        Parameters
        ----------
        scope : typing.Optional[GetCurrenciesRequestScope]
            Set to 'all' to include legacy currencies

        providers : typing.Optional[str]
            Comma-separated list of data providers to include

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Currency]
            Available currencies

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_currencies(
                providers="ECB,TCMB",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_currencies(
            scope=scope, providers=providers, request_options=request_options
        )
        return _response.data

    async def get_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Provider]:
        """
        Returns available exchange rate data providers with their base currency.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Provider]
            Available providers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_providers(request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
