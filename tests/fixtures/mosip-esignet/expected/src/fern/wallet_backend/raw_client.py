

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_binding_otp_request_request import PostBindingOtpRequestRequest
from .types.post_binding_otp_response import PostBindingOtpResponse
from .types.post_binding_otp_v2request_request import PostBindingOtpV2RequestRequest
from .types.post_binding_otp_v2response import PostBindingOtpV2Response
from .types.post_wallet_binding_request_request import PostWalletBindingRequestRequest
from .types.post_wallet_binding_response import PostWalletBindingResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWalletBackendClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_binding_otp(
        self,
        *,
        request_time: str,
        request: PostBindingOtpRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostBindingOtpResponse]:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostBindingOtpResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "binding/binding-otp",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostBindingOtpRequestRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "partner-api-key": str(partner_api_key) if partner_api_key is not None else None,
                "partner-id": str(partner_id) if partner_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostBindingOtpResponse,
                    parse_obj_as(
                        type_=PostBindingOtpResponse,
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

    def post_binding_otp_v2(
        self,
        *,
        request_time: str,
        request: PostBindingOtpV2RequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostBindingOtpV2Response]:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpV2RequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostBindingOtpV2Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "binding/v2/binding-otp",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostBindingOtpV2RequestRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "partner-api-key": str(partner_api_key) if partner_api_key is not None else None,
                "partner-id": str(partner_id) if partner_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostBindingOtpV2Response,
                    parse_obj_as(
                        type_=PostBindingOtpV2Response,
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

    def post_wallet_binding(
        self,
        *,
        request_time: str,
        request: PostWalletBindingRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostWalletBindingResponse]:
        """
        Wallet binding endpoint is invoked by Mimoto server.

        1. This request is invoked from wallet-app with authChallenge.
        2. Integrated keybinder implementation validates the authChallenge.
        3. Public key registry is updated with the key binding details for the provided individualId.
        4. Binded walletUserId (WUID) is returned with keybinder signed certificate.

        **Note**: Binding entry uniqueness is combination of these 3 values -> (PSUT, public-key, auth-factor-type)

        Parameters
        ----------
        request_time : str

        request : PostWalletBindingRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the Binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostWalletBindingResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "binding/wallet-binding",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostWalletBindingRequestRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "partner-api-key": str(partner_api_key) if partner_api_key is not None else None,
                "partner-id": str(partner_id) if partner_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostWalletBindingResponse,
                    parse_obj_as(
                        type_=PostWalletBindingResponse,
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


class AsyncRawWalletBackendClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_binding_otp(
        self,
        *,
        request_time: str,
        request: PostBindingOtpRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostBindingOtpResponse]:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostBindingOtpResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "binding/binding-otp",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostBindingOtpRequestRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "partner-api-key": str(partner_api_key) if partner_api_key is not None else None,
                "partner-id": str(partner_id) if partner_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostBindingOtpResponse,
                    parse_obj_as(
                        type_=PostBindingOtpResponse,
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

    async def post_binding_otp_v2(
        self,
        *,
        request_time: str,
        request: PostBindingOtpV2RequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostBindingOtpV2Response]:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpV2RequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostBindingOtpV2Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "binding/v2/binding-otp",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostBindingOtpV2RequestRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "partner-api-key": str(partner_api_key) if partner_api_key is not None else None,
                "partner-id": str(partner_id) if partner_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostBindingOtpV2Response,
                    parse_obj_as(
                        type_=PostBindingOtpV2Response,
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

    async def post_wallet_binding(
        self,
        *,
        request_time: str,
        request: PostWalletBindingRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostWalletBindingResponse]:
        """
        Wallet binding endpoint is invoked by Mimoto server.

        1. This request is invoked from wallet-app with authChallenge.
        2. Integrated keybinder implementation validates the authChallenge.
        3. Public key registry is updated with the key binding details for the provided individualId.
        4. Binded walletUserId (WUID) is returned with keybinder signed certificate.

        **Note**: Binding entry uniqueness is combination of these 3 values -> (PSUT, public-key, auth-factor-type)

        Parameters
        ----------
        request_time : str

        request : PostWalletBindingRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the Binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostWalletBindingResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "binding/wallet-binding",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostWalletBindingRequestRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "partner-api-key": str(partner_api_key) if partner_api_key is not None else None,
                "partner-id": str(partner_id) if partner_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostWalletBindingResponse,
                    parse_obj_as(
                        type_=PostWalletBindingResponse,
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
