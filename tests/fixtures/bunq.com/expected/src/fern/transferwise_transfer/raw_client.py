

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
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.transferwise_quote import TransferwiseQuote
from ..types.transferwise_transfer_create import TransferwiseTransferCreate
from ..types.transferwise_transfer_listing import TransferwiseTransferListing
from ..types.transferwise_transfer_read import TransferwiseTransferRead


OMIT = typing.cast(typing.Any, ...)


class RawTransferwiseTransferClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_transferwise_transfer_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TransferwiseTransferListing]]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TransferwiseTransferListing]]
            Used to create Transferwise payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-transfer",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TransferwiseTransferListing],
                    parse_obj_as(
                        type_=typing.List[TransferwiseTransferListing],
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

    def create_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        monetary_account_id: str,
        recipient_id: str,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        pay_in_reference: typing.Optional[str] = OMIT,
        quote: typing.Optional[TransferwiseQuote] = OMIT,
        rate: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_transferwise: typing.Optional[str] = OMIT,
        status_transferwise_issue: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TransferwiseTransferCreate]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        monetary_account_id : str
            The id of the monetary account the payment should be made from.

        recipient_id : str
            The id of the target account.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        pay_in_reference : typing.Optional[str]
            The Pay-In reference of the payment.

        quote : typing.Optional[TransferwiseQuote]
            The quote details used to created the payment.

        rate : typing.Optional[str]
            The rate of the payment.

        reference : typing.Optional[str]
            The reference of the payment.

        status : typing.Optional[str]
            The status.

        status_transferwise : typing.Optional[str]
            The status as Transferwise reports it.

        status_transferwise_issue : typing.Optional[str]
            A status to indicatie if Transferwise has an issue with this payment and requires more information.

        sub_status : typing.Optional[str]
            The subStatus.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransferwiseTransferCreate]
            Used to create Transferwise payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-transfer",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "amount_source": convert_and_respect_annotation_metadata(
                    object_=amount_source, annotation=Amount, direction="write"
                ),
                "amount_target": convert_and_respect_annotation_metadata(
                    object_=amount_target, annotation=Amount, direction="write"
                ),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "monetary_account_id": monetary_account_id,
                "pay_in_reference": pay_in_reference,
                "quote": convert_and_respect_annotation_metadata(
                    object_=quote, annotation=TransferwiseQuote, direction="write"
                ),
                "rate": rate,
                "recipient_id": recipient_id,
                "reference": reference,
                "status": status,
                "status_transferwise": status_transferwise,
                "status_transferwise_issue": status_transferwise_issue,
                "sub_status": sub_status,
                "time_delivery_estimate": time_delivery_estimate,
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
                    TransferwiseTransferCreate,
                    parse_obj_as(
                        type_=TransferwiseTransferCreate,
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

    def read_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TransferwiseTransferRead]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransferwiseTransferRead]
            Used to create Transferwise payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-transfer/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferwiseTransferRead,
                    parse_obj_as(
                        type_=TransferwiseTransferRead,
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


class AsyncRawTransferwiseTransferClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_transferwise_transfer_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TransferwiseTransferListing]]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TransferwiseTransferListing]]
            Used to create Transferwise payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-transfer",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TransferwiseTransferListing],
                    parse_obj_as(
                        type_=typing.List[TransferwiseTransferListing],
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

    async def create_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        monetary_account_id: str,
        recipient_id: str,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        pay_in_reference: typing.Optional[str] = OMIT,
        quote: typing.Optional[TransferwiseQuote] = OMIT,
        rate: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_transferwise: typing.Optional[str] = OMIT,
        status_transferwise_issue: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TransferwiseTransferCreate]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        monetary_account_id : str
            The id of the monetary account the payment should be made from.

        recipient_id : str
            The id of the target account.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        pay_in_reference : typing.Optional[str]
            The Pay-In reference of the payment.

        quote : typing.Optional[TransferwiseQuote]
            The quote details used to created the payment.

        rate : typing.Optional[str]
            The rate of the payment.

        reference : typing.Optional[str]
            The reference of the payment.

        status : typing.Optional[str]
            The status.

        status_transferwise : typing.Optional[str]
            The status as Transferwise reports it.

        status_transferwise_issue : typing.Optional[str]
            A status to indicatie if Transferwise has an issue with this payment and requires more information.

        sub_status : typing.Optional[str]
            The subStatus.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransferwiseTransferCreate]
            Used to create Transferwise payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-transfer",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "amount_source": convert_and_respect_annotation_metadata(
                    object_=amount_source, annotation=Amount, direction="write"
                ),
                "amount_target": convert_and_respect_annotation_metadata(
                    object_=amount_target, annotation=Amount, direction="write"
                ),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "monetary_account_id": monetary_account_id,
                "pay_in_reference": pay_in_reference,
                "quote": convert_and_respect_annotation_metadata(
                    object_=quote, annotation=TransferwiseQuote, direction="write"
                ),
                "rate": rate,
                "recipient_id": recipient_id,
                "reference": reference,
                "status": status,
                "status_transferwise": status_transferwise,
                "status_transferwise_issue": status_transferwise_issue,
                "sub_status": sub_status,
                "time_delivery_estimate": time_delivery_estimate,
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
                    TransferwiseTransferCreate,
                    parse_obj_as(
                        type_=TransferwiseTransferCreate,
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

    async def read_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TransferwiseTransferRead]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransferwiseTransferRead]
            Used to create Transferwise payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-transfer/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferwiseTransferRead,
                    parse_obj_as(
                        type_=TransferwiseTransferRead,
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
