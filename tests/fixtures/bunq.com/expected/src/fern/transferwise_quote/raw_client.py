

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
from ..types.transferwise_quote_create import TransferwiseQuoteCreate
from ..types.transferwise_quote_read import TransferwiseQuoteRead


OMIT = typing.cast(typing.Any, ...)


class RawTransferwiseQuoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_transferwise_quote_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_fee: typing.Optional[Amount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        created: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        quote_id: typing.Optional[str] = OMIT,
        rate: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TransferwiseQuoteCreate]:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_fee : typing.Optional[Amount]
            The fee amount.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        created : typing.Optional[str]
            The timestamp of the quote's creation.

        id : typing.Optional[int]
            The id of the quote.

        quote_id : typing.Optional[str]
            The quote id Transferwise needs.

        rate : typing.Optional[str]
            The rate.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        time_expiry : typing.Optional[str]
            The expiration timestamp of the quote.

        updated : typing.Optional[str]
            The timestamp of the quote's last update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransferwiseQuoteCreate]
            Used to get quotes from Transferwise. These can be used to initiate payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote",
            method="POST",
            json={
                "amount_fee": convert_and_respect_annotation_metadata(
                    object_=amount_fee, annotation=Amount, direction="write"
                ),
                "amount_source": convert_and_respect_annotation_metadata(
                    object_=amount_source, annotation=Amount, direction="write"
                ),
                "amount_target": convert_and_respect_annotation_metadata(
                    object_=amount_target, annotation=Amount, direction="write"
                ),
                "created": created,
                "currency_source": currency_source,
                "currency_target": currency_target,
                "id": id,
                "quote_id": quote_id,
                "rate": rate,
                "time_delivery_estimate": time_delivery_estimate,
                "time_expiry": time_expiry,
                "updated": updated,
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
                    TransferwiseQuoteCreate,
                    parse_obj_as(
                        type_=TransferwiseQuoteCreate,
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

    def read_transferwise_quote_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TransferwiseQuoteRead]:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransferwiseQuoteRead]
            Used to get quotes from Transferwise. These can be used to initiate payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferwiseQuoteRead,
                    parse_obj_as(
                        type_=TransferwiseQuoteRead,
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


class AsyncRawTransferwiseQuoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_transferwise_quote_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_fee: typing.Optional[Amount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        created: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        quote_id: typing.Optional[str] = OMIT,
        rate: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TransferwiseQuoteCreate]:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_fee : typing.Optional[Amount]
            The fee amount.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        created : typing.Optional[str]
            The timestamp of the quote's creation.

        id : typing.Optional[int]
            The id of the quote.

        quote_id : typing.Optional[str]
            The quote id Transferwise needs.

        rate : typing.Optional[str]
            The rate.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        time_expiry : typing.Optional[str]
            The expiration timestamp of the quote.

        updated : typing.Optional[str]
            The timestamp of the quote's last update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransferwiseQuoteCreate]
            Used to get quotes from Transferwise. These can be used to initiate payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote",
            method="POST",
            json={
                "amount_fee": convert_and_respect_annotation_metadata(
                    object_=amount_fee, annotation=Amount, direction="write"
                ),
                "amount_source": convert_and_respect_annotation_metadata(
                    object_=amount_source, annotation=Amount, direction="write"
                ),
                "amount_target": convert_and_respect_annotation_metadata(
                    object_=amount_target, annotation=Amount, direction="write"
                ),
                "created": created,
                "currency_source": currency_source,
                "currency_target": currency_target,
                "id": id,
                "quote_id": quote_id,
                "rate": rate,
                "time_delivery_estimate": time_delivery_estimate,
                "time_expiry": time_expiry,
                "updated": updated,
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
                    TransferwiseQuoteCreate,
                    parse_obj_as(
                        type_=TransferwiseQuoteCreate,
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

    async def read_transferwise_quote_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TransferwiseQuoteRead]:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransferwiseQuoteRead]
            Used to get quotes from Transferwise. These can be used to initiate payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferwiseQuoteRead,
                    parse_obj_as(
                        type_=TransferwiseQuoteRead,
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
