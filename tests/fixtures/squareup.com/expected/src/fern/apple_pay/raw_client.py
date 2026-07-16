

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.register_domain_response import RegisterDomainResponse


OMIT = typing.cast(typing.Any, ...)


class RawApplePayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_domain(
        self, *, domain_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegisterDomainResponse]:
        """
        Activates a domain for use with Apple Pay on the Web and Square. A validation
        is performed on this domain by Apple to ensure that it is properly set up as
        an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate
        Apple Pay on the Web with Square for merchants using their platform.

        To learn more about Web Apple Pay, see
        [Add the Apple Pay on the Web Button](https://developer.squareup.com/docs/payment-form/add-digital-wallets/apple-pay).

        Parameters
        ----------
        domain_name : str
            A domain name as described in RFC-1034 that will be registered with ApplePay.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegisterDomainResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/apple-pay/domains",
            method="POST",
            json={
                "domain_name": domain_name,
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
                    RegisterDomainResponse,
                    parse_obj_as(
                        type_=RegisterDomainResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawApplePayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_domain(
        self, *, domain_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegisterDomainResponse]:
        """
        Activates a domain for use with Apple Pay on the Web and Square. A validation
        is performed on this domain by Apple to ensure that it is properly set up as
        an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate
        Apple Pay on the Web with Square for merchants using their platform.

        To learn more about Web Apple Pay, see
        [Add the Apple Pay on the Web Button](https://developer.squareup.com/docs/payment-form/add-digital-wallets/apple-pay).

        Parameters
        ----------
        domain_name : str
            A domain name as described in RFC-1034 that will be registered with ApplePay.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegisterDomainResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/apple-pay/domains",
            method="POST",
            json={
                "domain_name": domain_name,
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
                    RegisterDomainResponse,
                    parse_obj_as(
                        type_=RegisterDomainResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
