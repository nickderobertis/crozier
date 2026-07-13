

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
from ..types.transferwise_quote_temporary_create import TransferwiseQuoteTemporaryCreate
from ..types.transferwise_quote_temporary_read import TransferwiseQuoteTemporaryRead


OMIT = typing.cast(typing.Any, ...)


class RawTransferwiseQuoteTemporaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_transferwise_quote_temporary_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TransferwiseQuoteTemporaryCreate]:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_source : typing.Optional[Amount]
            The source amount. Required if target amount is left empty.

        amount_target : typing.Optional[Amount]
            The target amount. Required if source amount is left empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransferwiseQuoteTemporaryCreate]
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote-temporary",
            method="POST",
            json={
                "amount_source": convert_and_respect_annotation_metadata(
                    object_=amount_source, annotation=Amount, direction="write"
                ),
                "amount_target": convert_and_respect_annotation_metadata(
                    object_=amount_target, annotation=Amount, direction="write"
                ),
                "currency_source": currency_source,
                "currency_target": currency_target,
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
                    TransferwiseQuoteTemporaryCreate,
                    parse_obj_as(
                        type_=TransferwiseQuoteTemporaryCreate,
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

    def read_transferwise_quote_temporary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TransferwiseQuoteTemporaryRead]:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransferwiseQuoteTemporaryRead]
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote-temporary/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferwiseQuoteTemporaryRead,
                    parse_obj_as(
                        type_=TransferwiseQuoteTemporaryRead,
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


class AsyncRawTransferwiseQuoteTemporaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_transferwise_quote_temporary_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TransferwiseQuoteTemporaryCreate]:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_source : typing.Optional[Amount]
            The source amount. Required if target amount is left empty.

        amount_target : typing.Optional[Amount]
            The target amount. Required if source amount is left empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransferwiseQuoteTemporaryCreate]
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote-temporary",
            method="POST",
            json={
                "amount_source": convert_and_respect_annotation_metadata(
                    object_=amount_source, annotation=Amount, direction="write"
                ),
                "amount_target": convert_and_respect_annotation_metadata(
                    object_=amount_target, annotation=Amount, direction="write"
                ),
                "currency_source": currency_source,
                "currency_target": currency_target,
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
                    TransferwiseQuoteTemporaryCreate,
                    parse_obj_as(
                        type_=TransferwiseQuoteTemporaryCreate,
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

    async def read_transferwise_quote_temporary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TransferwiseQuoteTemporaryRead]:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransferwiseQuoteTemporaryRead]
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote-temporary/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferwiseQuoteTemporaryRead,
                    parse_obj_as(
                        type_=TransferwiseQuoteTemporaryRead,
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
