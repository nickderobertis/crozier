

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.payment_service_provider_credential_create import PaymentServiceProviderCredentialCreate
from ..types.payment_service_provider_credential_read import PaymentServiceProviderCredentialRead


OMIT = typing.cast(typing.Any, ...)


class RawPaymentServiceProviderCredentialClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_payment_service_provider_credential(
        self,
        *,
        client_payment_service_provider_certificate: str,
        client_payment_service_provider_certificate_chain: str,
        client_public_key_signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentServiceProviderCredentialCreate]:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        client_payment_service_provider_certificate : str
            Payment Services Directive 2 compatible QSEAL certificate

        client_payment_service_provider_certificate_chain : str
            Intermediate and root certificate belonging to the provided certificate.

        client_public_key_signature : str
            The Base64 encoded signature of the public key provided during installation and with the installation token appended as a nonce. Signed with the private key belonging to the QSEAL certificate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentServiceProviderCredentialCreate]
            Register a Payment Service Provider and provide credentials
        """
        _response = self._client_wrapper.httpx_client.request(
            "payment-service-provider-credential",
            method="POST",
            json={
                "client_payment_service_provider_certificate": client_payment_service_provider_certificate,
                "client_payment_service_provider_certificate_chain": client_payment_service_provider_certificate_chain,
                "client_public_key_signature": client_public_key_signature,
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
                    PaymentServiceProviderCredentialCreate,
                    parse_obj_as(
                        type_=PaymentServiceProviderCredentialCreate,
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

    def read_payment_service_provider_credential(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PaymentServiceProviderCredentialRead]:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentServiceProviderCredentialRead]
            Register a Payment Service Provider and provide credentials
        """
        _response = self._client_wrapper.httpx_client.request(
            f"payment-service-provider-credential/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentServiceProviderCredentialRead,
                    parse_obj_as(
                        type_=PaymentServiceProviderCredentialRead,
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


class AsyncRawPaymentServiceProviderCredentialClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_payment_service_provider_credential(
        self,
        *,
        client_payment_service_provider_certificate: str,
        client_payment_service_provider_certificate_chain: str,
        client_public_key_signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentServiceProviderCredentialCreate]:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        client_payment_service_provider_certificate : str
            Payment Services Directive 2 compatible QSEAL certificate

        client_payment_service_provider_certificate_chain : str
            Intermediate and root certificate belonging to the provided certificate.

        client_public_key_signature : str
            The Base64 encoded signature of the public key provided during installation and with the installation token appended as a nonce. Signed with the private key belonging to the QSEAL certificate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentServiceProviderCredentialCreate]
            Register a Payment Service Provider and provide credentials
        """
        _response = await self._client_wrapper.httpx_client.request(
            "payment-service-provider-credential",
            method="POST",
            json={
                "client_payment_service_provider_certificate": client_payment_service_provider_certificate,
                "client_payment_service_provider_certificate_chain": client_payment_service_provider_certificate_chain,
                "client_public_key_signature": client_public_key_signature,
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
                    PaymentServiceProviderCredentialCreate,
                    parse_obj_as(
                        type_=PaymentServiceProviderCredentialCreate,
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

    async def read_payment_service_provider_credential(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PaymentServiceProviderCredentialRead]:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentServiceProviderCredentialRead]
            Register a Payment Service Provider and provide credentials
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"payment-service-provider-credential/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentServiceProviderCredentialRead,
                    parse_obj_as(
                        type_=PaymentServiceProviderCredentialRead,
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
