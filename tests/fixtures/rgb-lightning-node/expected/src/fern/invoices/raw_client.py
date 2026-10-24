

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.decode_ln_invoice_response import DecodeLnInvoiceResponse
from ..types.invoice_status_response import InvoiceStatusResponse
from ..types.ln_invoice_response import LnInvoiceResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def decode_a_ln_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DecodeLnInvoiceResponse]:
        """
        Decode the provided LN invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DecodeLnInvoiceResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "decodelninvoice",
            method="POST",
            json={
                "invoice": invoice,
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
                    DecodeLnInvoiceResponse,
                    parse_obj_as(
                        type_=DecodeLnInvoiceResponse,
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

    def get_an_invoice_status(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InvoiceStatusResponse]:
        """
        Get the status of the provided LN invoice

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InvoiceStatusResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "invoicestatus",
            method="POST",
            json={
                "invoice": invoice,
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
                    InvoiceStatusResponse,
                    parse_obj_as(
                        type_=InvoiceStatusResponse,
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

    def get_a_ln_invoice(
        self,
        *,
        expiry_sec: int,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LnInvoiceResponse]:
        """
        Get a LN invoice to receive a payment. The description and description_hash fields are mutually exclusive.

        Parameters
        ----------
        expiry_sec : int

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        description : typing.Optional[str]

        description_hash : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LnInvoiceResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "lninvoice",
            method="POST",
            json={
                "amt_msat": amt_msat,
                "expiry_sec": expiry_sec,
                "asset_id": asset_id,
                "asset_amount": asset_amount,
                "description": description,
                "description_hash": description_hash,
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
                    LnInvoiceResponse,
                    parse_obj_as(
                        type_=LnInvoiceResponse,
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


class AsyncRawInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def decode_a_ln_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DecodeLnInvoiceResponse]:
        """
        Decode the provided LN invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DecodeLnInvoiceResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "decodelninvoice",
            method="POST",
            json={
                "invoice": invoice,
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
                    DecodeLnInvoiceResponse,
                    parse_obj_as(
                        type_=DecodeLnInvoiceResponse,
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

    async def get_an_invoice_status(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InvoiceStatusResponse]:
        """
        Get the status of the provided LN invoice

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InvoiceStatusResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "invoicestatus",
            method="POST",
            json={
                "invoice": invoice,
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
                    InvoiceStatusResponse,
                    parse_obj_as(
                        type_=InvoiceStatusResponse,
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

    async def get_a_ln_invoice(
        self,
        *,
        expiry_sec: int,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LnInvoiceResponse]:
        """
        Get a LN invoice to receive a payment. The description and description_hash fields are mutually exclusive.

        Parameters
        ----------
        expiry_sec : int

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        description : typing.Optional[str]

        description_hash : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LnInvoiceResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lninvoice",
            method="POST",
            json={
                "amt_msat": amt_msat,
                "expiry_sec": expiry_sec,
                "asset_id": asset_id,
                "asset_amount": asset_amount,
                "description": description,
                "description_hash": description_hash,
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
                    LnInvoiceResponse,
                    parse_obj_as(
                        type_=LnInvoiceResponse,
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
