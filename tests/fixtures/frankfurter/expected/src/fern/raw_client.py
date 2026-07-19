

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .errors.not_found_error import NotFoundError
from .errors.unprocessable_entity_error import UnprocessableEntityError
from .types.currency import Currency
from .types.currency_detail import CurrencyDetail
from .types.get_currencies_request_scope import GetCurrenciesRequestScope
from .types.get_rates_request_expand import GetRatesRequestExpand
from .types.get_rates_request_group import GetRatesRequestGroup
from .types.provider import Provider
from .types.rate import Rate
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[typing.List[Rate]]:
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
        HttpResponse[typing.List[Rate]]
            Exchange rates
        """
        _response = self._client_wrapper.httpx_client.request(
            "rates",
            method="GET",
            params={
                "date": str(date) if date is not None else None,
                "from": str(from_) if from_ is not None else None,
                "to": str(to) if to is not None else None,
                "base": base,
                "quotes": quotes,
                "providers": providers,
                "group": group,
                "expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Rate],
                    parse_obj_as(
                        type_=typing.List[Rate],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_rate(
        self,
        base: str,
        quote: str,
        *,
        date: typing.Optional[dt.date] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Rate]:
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
        HttpResponse[Rate]
            Exchange rate
        """
        _response = self._client_wrapper.httpx_client.request(
            f"rate/{encode_path_param(base)}/{encode_path_param(quote)}",
            method="GET",
            params={
                "date": str(date) if date is not None else None,
                "providers": providers,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rate,
                    parse_obj_as(
                        type_=Rate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_currency(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CurrencyDetail]:
        """
        Returns details for a single currency, including provider information or peg metadata.

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CurrencyDetail]
            Currency details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"currency/{encode_path_param(code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyDetail,
                    parse_obj_as(
                        type_=CurrencyDetail,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_currencies(
        self,
        *,
        scope: typing.Optional[GetCurrenciesRequestScope] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Currency]]:
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
        HttpResponse[typing.List[Currency]]
            Available currencies
        """
        _response = self._client_wrapper.httpx_client.request(
            "currencies",
            method="GET",
            params={
                "scope": scope,
                "providers": providers,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Currency],
                    parse_obj_as(
                        type_=typing.List[Currency],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Provider]]:
        """
        Returns available exchange rate data providers with their base currency.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Provider]]
            Available providers
        """
        _response = self._client_wrapper.httpx_client.request(
            "providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Provider],
                    parse_obj_as(
                        type_=typing.List[Provider],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[typing.List[Rate]]:
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
        AsyncHttpResponse[typing.List[Rate]]
            Exchange rates
        """
        _response = await self._client_wrapper.httpx_client.request(
            "rates",
            method="GET",
            params={
                "date": str(date) if date is not None else None,
                "from": str(from_) if from_ is not None else None,
                "to": str(to) if to is not None else None,
                "base": base,
                "quotes": quotes,
                "providers": providers,
                "group": group,
                "expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Rate],
                    parse_obj_as(
                        type_=typing.List[Rate],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_rate(
        self,
        base: str,
        quote: str,
        *,
        date: typing.Optional[dt.date] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Rate]:
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
        AsyncHttpResponse[Rate]
            Exchange rate
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"rate/{encode_path_param(base)}/{encode_path_param(quote)}",
            method="GET",
            params={
                "date": str(date) if date is not None else None,
                "providers": providers,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rate,
                    parse_obj_as(
                        type_=Rate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_currency(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CurrencyDetail]:
        """
        Returns details for a single currency, including provider information or peg metadata.

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CurrencyDetail]
            Currency details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"currency/{encode_path_param(code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyDetail,
                    parse_obj_as(
                        type_=CurrencyDetail,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_currencies(
        self,
        *,
        scope: typing.Optional[GetCurrenciesRequestScope] = None,
        providers: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Currency]]:
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
        AsyncHttpResponse[typing.List[Currency]]
            Available currencies
        """
        _response = await self._client_wrapper.httpx_client.request(
            "currencies",
            method="GET",
            params={
                "scope": scope,
                "providers": providers,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Currency],
                    parse_obj_as(
                        type_=typing.List[Currency],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Provider]]:
        """
        Returns available exchange rate data providers with their base currency.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Provider]]
            Available providers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Provider],
                    parse_obj_as(
                        type_=typing.List[Provider],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
