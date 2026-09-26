

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.saved_payment_method import SavedPaymentMethod
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAcksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def acknowledge_payment(
        self,
        payment_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        provider_payment_id: typing.Optional[str] = OMIT,
        invoice_url: typing.Optional[str] = OMIT,
        invoice_pdf: typing.Optional[str] = OMIT,
        stripe_invoice_id: typing.Optional[str] = OMIT,
        stripe_customer_id: typing.Optional[str] = OMIT,
        saved: typing.Optional[SavedPaymentMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        completes (ie. ack) request initiated by `/init` on the payments-gateway API

        Parameters
        ----------
        payment_id : str

        success : bool

        message : typing.Optional[str]

        provider_payment_id : typing.Optional[str]
            Payment ID from the provider (e.g. stripe payment ID)

        invoice_url : typing.Optional[str]
            Link to invoice is required when success=true

        invoice_pdf : typing.Optional[str]
            Link to invoice PDF

        stripe_invoice_id : typing.Optional[str]
            Stripe invoice ID

        stripe_customer_id : typing.Optional[str]
            Stripe customer ID

        saved : typing.Optional[SavedPaymentMethod]
            Gets the payment-method if user opted to save it during payment.If used did not opt to save of payment-method was already saved, then it defaults to None

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/payments/{encode_path_param(payment_id)}:ack",
            method="POST",
            json={
                "success": success,
                "message": message,
                "provider_payment_id": provider_payment_id,
                "invoice_url": invoice_url,
                "invoice_pdf": invoice_pdf,
                "stripe_invoice_id": stripe_invoice_id,
                "stripe_customer_id": stripe_customer_id,
                "saved": convert_and_respect_annotation_metadata(
                    object_=saved, annotation=typing.Optional[SavedPaymentMethod], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def acknowledge_payment_method(
        self,
        payment_method_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        completes (ie. ack) request initiated by `/payments-methods:init` on the payments-gateway API

        Parameters
        ----------
        payment_method_id : str

        success : bool

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/payments-methods/{encode_path_param(payment_method_id)}:ack",
            method="POST",
            json={
                "success": success,
                "message": message,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawAcksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def acknowledge_payment(
        self,
        payment_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        provider_payment_id: typing.Optional[str] = OMIT,
        invoice_url: typing.Optional[str] = OMIT,
        invoice_pdf: typing.Optional[str] = OMIT,
        stripe_invoice_id: typing.Optional[str] = OMIT,
        stripe_customer_id: typing.Optional[str] = OMIT,
        saved: typing.Optional[SavedPaymentMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        completes (ie. ack) request initiated by `/init` on the payments-gateway API

        Parameters
        ----------
        payment_id : str

        success : bool

        message : typing.Optional[str]

        provider_payment_id : typing.Optional[str]
            Payment ID from the provider (e.g. stripe payment ID)

        invoice_url : typing.Optional[str]
            Link to invoice is required when success=true

        invoice_pdf : typing.Optional[str]
            Link to invoice PDF

        stripe_invoice_id : typing.Optional[str]
            Stripe invoice ID

        stripe_customer_id : typing.Optional[str]
            Stripe customer ID

        saved : typing.Optional[SavedPaymentMethod]
            Gets the payment-method if user opted to save it during payment.If used did not opt to save of payment-method was already saved, then it defaults to None

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/payments/{encode_path_param(payment_id)}:ack",
            method="POST",
            json={
                "success": success,
                "message": message,
                "provider_payment_id": provider_payment_id,
                "invoice_url": invoice_url,
                "invoice_pdf": invoice_pdf,
                "stripe_invoice_id": stripe_invoice_id,
                "stripe_customer_id": stripe_customer_id,
                "saved": convert_and_respect_annotation_metadata(
                    object_=saved, annotation=typing.Optional[SavedPaymentMethod], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def acknowledge_payment_method(
        self,
        payment_method_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        completes (ie. ack) request initiated by `/payments-methods:init` on the payments-gateway API

        Parameters
        ----------
        payment_method_id : str

        success : bool

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/payments-methods/{encode_path_param(payment_method_id)}:ack",
            method="POST",
            json={
                "success": success,
                "message": message,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
