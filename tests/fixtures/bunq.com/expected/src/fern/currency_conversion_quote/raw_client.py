

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.amount import Amount
from ..types.currency_conversion_quote_create import CurrencyConversionQuoteCreate
from ..types.currency_conversion_quote_read import CurrencyConversionQuoteRead
from ..types.currency_conversion_quote_update import CurrencyConversionQuoteUpdate
from ..types.pointer import Pointer


OMIT = typing.cast(typing.Any, ...)


class RawCurrencyConversionQuoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CurrencyConversionQuoteCreate]:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CurrencyConversionQuoteCreate]
            Endpoint to create a quote for currency conversions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/currency-conversion-quote",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=Pointer, direction="write"
                ),
                "currency_source": currency_source,
                "currency_target": currency_target,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyConversionQuoteCreate,
                    parse_obj_as(
                        type_=CurrencyConversionQuoteCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CurrencyConversionQuoteRead]:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CurrencyConversionQuoteRead]
            Endpoint to create a quote for currency conversions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/currency-conversion-quote/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyConversionQuoteRead,
                    parse_obj_as(
                        type_=CurrencyConversionQuoteRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CurrencyConversionQuoteUpdate]:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CurrencyConversionQuoteUpdate]
            Endpoint to create a quote for currency conversions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/currency-conversion-quote/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=Pointer, direction="write"
                ),
                "currency_source": currency_source,
                "currency_target": currency_target,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyConversionQuoteUpdate,
                    parse_obj_as(
                        type_=CurrencyConversionQuoteUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCurrencyConversionQuoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CurrencyConversionQuoteCreate]:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CurrencyConversionQuoteCreate]
            Endpoint to create a quote for currency conversions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/currency-conversion-quote",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=Pointer, direction="write"
                ),
                "currency_source": currency_source,
                "currency_target": currency_target,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyConversionQuoteCreate,
                    parse_obj_as(
                        type_=CurrencyConversionQuoteCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CurrencyConversionQuoteRead]:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CurrencyConversionQuoteRead]
            Endpoint to create a quote for currency conversions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/currency-conversion-quote/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyConversionQuoteRead,
                    parse_obj_as(
                        type_=CurrencyConversionQuoteRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CurrencyConversionQuoteUpdate]:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CurrencyConversionQuoteUpdate]
            Endpoint to create a quote for currency conversions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/currency-conversion-quote/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=Pointer, direction="write"
                ),
                "currency_source": currency_source,
                "currency_target": currency_target,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyConversionQuoteUpdate,
                    parse_obj_as(
                        type_=CurrencyConversionQuoteUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
