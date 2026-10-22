

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_payment_response import GetPaymentResponse
from ..types.keysend_response import KeysendResponse
from ..types.list_payments_response import ListPaymentsResponse
from ..types.send_payment_response import SendPaymentResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_payment(
        self, *, payment_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPaymentResponse]:
        """
        Get a payment by its payment hash

        Parameters
        ----------
        payment_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPaymentResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "getpayment",
            method="POST",
            json={
                "payment_hash": payment_hash,
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
                    GetPaymentResponse,
                    parse_obj_as(
                        type_=GetPaymentResponse,
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

    def send_to_a_peer_spontaneously(
        self,
        *,
        dest_pubkey: str,
        amt_msat: int,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[KeysendResponse]:
        """
        Send bitcoins and RGB assets to a LN peer spontaneously (without a LN invoice)

        Parameters
        ----------
        dest_pubkey : str

        amt_msat : int

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KeysendResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "keysend",
            method="POST",
            json={
                "dest_pubkey": dest_pubkey,
                "amt_msat": amt_msat,
                "asset_id": asset_id,
                "asset_amount": asset_amount,
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
                    KeysendResponse,
                    parse_obj_as(
                        type_=KeysendResponse,
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

    def list_payments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListPaymentsResponse]:
        """
        List the node's LN payments

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPaymentsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "listpayments",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentsResponse,
                    parse_obj_as(
                        type_=ListPaymentsResponse,
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

    def send_a_payment(
        self,
        *,
        invoice: str,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SendPaymentResponse]:
        """
        Pay the provided LN invoice

        Parameters
        ----------
        invoice : str

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendPaymentResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "sendpayment",
            method="POST",
            json={
                "invoice": invoice,
                "amt_msat": amt_msat,
                "asset_id": asset_id,
                "asset_amount": asset_amount,
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
                    SendPaymentResponse,
                    parse_obj_as(
                        type_=SendPaymentResponse,
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


class AsyncRawPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_payment(
        self, *, payment_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPaymentResponse]:
        """
        Get a payment by its payment hash

        Parameters
        ----------
        payment_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPaymentResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "getpayment",
            method="POST",
            json={
                "payment_hash": payment_hash,
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
                    GetPaymentResponse,
                    parse_obj_as(
                        type_=GetPaymentResponse,
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

    async def send_to_a_peer_spontaneously(
        self,
        *,
        dest_pubkey: str,
        amt_msat: int,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[KeysendResponse]:
        """
        Send bitcoins and RGB assets to a LN peer spontaneously (without a LN invoice)

        Parameters
        ----------
        dest_pubkey : str

        amt_msat : int

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KeysendResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "keysend",
            method="POST",
            json={
                "dest_pubkey": dest_pubkey,
                "amt_msat": amt_msat,
                "asset_id": asset_id,
                "asset_amount": asset_amount,
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
                    KeysendResponse,
                    parse_obj_as(
                        type_=KeysendResponse,
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

    async def list_payments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListPaymentsResponse]:
        """
        List the node's LN payments

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPaymentsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listpayments",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentsResponse,
                    parse_obj_as(
                        type_=ListPaymentsResponse,
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

    async def send_a_payment(
        self,
        *,
        invoice: str,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SendPaymentResponse]:
        """
        Pay the provided LN invoice

        Parameters
        ----------
        invoice : str

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendPaymentResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sendpayment",
            method="POST",
            json={
                "invoice": invoice,
                "amt_msat": amt_msat,
                "asset_id": asset_id,
                "asset_amount": asset_amount,
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
                    SendPaymentResponse,
                    parse_obj_as(
                        type_=SendPaymentResponse,
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
