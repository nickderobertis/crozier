

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_authorization_link_transaction_request_request import PostAuthorizationLinkTransactionRequestRequest
from .types.post_authorization_link_transaction_response import PostAuthorizationLinkTransactionResponse
from .types.post_authorization_link_transaction_v2request_request import (
    PostAuthorizationLinkTransactionV2RequestRequest,
)
from .types.post_authorization_link_transaction_v2response import PostAuthorizationLinkTransactionV2Response
from .types.post_linked_authenticate_request_request import PostLinkedAuthenticateRequestRequest
from .types.post_linked_authenticate_response import PostLinkedAuthenticateResponse
from .types.post_linked_authenticate_v2request_request import PostLinkedAuthenticateV2RequestRequest
from .types.post_linked_authenticate_v2response import PostLinkedAuthenticateV2Response
from .types.post_linked_consent_request_request import PostLinkedConsentRequestRequest
from .types.post_linked_consent_response import PostLinkedConsentResponse
from .types.post_linked_consent_v2request_request import PostLinkedConsentV2RequestRequest
from .types.post_linked_consent_v2response import PostLinkedConsentV2Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWalletClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_authorization_link_transaction(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAuthorizationLinkTransactionResponse]:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAuthorizationLinkTransactionResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "linked-authorization/link-transaction",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostAuthorizationLinkTransactionRequestRequest, direction="write"
                ),
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
                    PostAuthorizationLinkTransactionResponse,
                    parse_obj_as(
                        type_=PostAuthorizationLinkTransactionResponse,
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

    def post_authorization_link_transaction_v2(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAuthorizationLinkTransactionV2Response]:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAuthorizationLinkTransactionV2Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "linked-authorization/v2/link-transaction",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostAuthorizationLinkTransactionV2RequestRequest, direction="write"
                ),
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
                    PostAuthorizationLinkTransactionV2Response,
                    parse_obj_as(
                        type_=PostAuthorizationLinkTransactionV2Response,
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

    def post_linked_authenticate(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinkedAuthenticateResponse]:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: Only linkTransactionId is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinkedAuthenticateResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "linked-authorization/authenticate",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedAuthenticateRequestRequest, direction="write"
                ),
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
                    PostLinkedAuthenticateResponse,
                    parse_obj_as(
                        type_=PostLinkedAuthenticateResponse,
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

    def post_linked_authenticate_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinkedAuthenticateV2Response]:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.
        6. It validates stored userconsent against the requested claims and scopes

        On Authentication Success: linkTransactionId and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinkedAuthenticateV2Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "linked-authorization/v2/authenticate",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedAuthenticateV2RequestRequest, direction="write"
                ),
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
                    PostLinkedAuthenticateV2Response,
                    parse_obj_as(
                        type_=PostLinkedAuthenticateV2Response,
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

    def post_linked_consent(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinkedConsentResponse]:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request.
        3. If valid, stores the accepted claims and permitted scopes in the cache.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinkedConsentResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "linked-authorization/consent",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedConsentRequestRequest, direction="write"
                ),
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
                    PostLinkedConsentResponse,
                    parse_obj_as(
                        type_=PostLinkedConsentResponse,
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

    def post_linked_consent_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinkedConsentV2Response]:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request and the signature.
        3. If valid, stores the accepted claims, permitted scopes and signature in the consent registry.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinkedConsentV2Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "linked-authorization/v2/consent",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedConsentV2RequestRequest, direction="write"
                ),
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
                    PostLinkedConsentV2Response,
                    parse_obj_as(
                        type_=PostLinkedConsentV2Response,
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


class AsyncRawWalletClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_authorization_link_transaction(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAuthorizationLinkTransactionResponse]:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAuthorizationLinkTransactionResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "linked-authorization/link-transaction",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostAuthorizationLinkTransactionRequestRequest, direction="write"
                ),
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
                    PostAuthorizationLinkTransactionResponse,
                    parse_obj_as(
                        type_=PostAuthorizationLinkTransactionResponse,
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

    async def post_authorization_link_transaction_v2(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAuthorizationLinkTransactionV2Response]:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAuthorizationLinkTransactionV2Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "linked-authorization/v2/link-transaction",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostAuthorizationLinkTransactionV2RequestRequest, direction="write"
                ),
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
                    PostAuthorizationLinkTransactionV2Response,
                    parse_obj_as(
                        type_=PostAuthorizationLinkTransactionV2Response,
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

    async def post_linked_authenticate(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinkedAuthenticateResponse]:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: Only linkTransactionId is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinkedAuthenticateResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "linked-authorization/authenticate",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedAuthenticateRequestRequest, direction="write"
                ),
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
                    PostLinkedAuthenticateResponse,
                    parse_obj_as(
                        type_=PostLinkedAuthenticateResponse,
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

    async def post_linked_authenticate_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinkedAuthenticateV2Response]:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.
        6. It validates stored userconsent against the requested claims and scopes

        On Authentication Success: linkTransactionId and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinkedAuthenticateV2Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "linked-authorization/v2/authenticate",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedAuthenticateV2RequestRequest, direction="write"
                ),
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
                    PostLinkedAuthenticateV2Response,
                    parse_obj_as(
                        type_=PostLinkedAuthenticateV2Response,
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

    async def post_linked_consent(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinkedConsentResponse]:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request.
        3. If valid, stores the accepted claims and permitted scopes in the cache.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinkedConsentResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "linked-authorization/consent",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedConsentRequestRequest, direction="write"
                ),
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
                    PostLinkedConsentResponse,
                    parse_obj_as(
                        type_=PostLinkedConsentResponse,
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

    async def post_linked_consent_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinkedConsentV2Response]:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request and the signature.
        3. If valid, stores the accepted claims, permitted scopes and signature in the consent registry.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinkedConsentV2Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "linked-authorization/v2/consent",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostLinkedConsentV2RequestRequest, direction="write"
                ),
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
                    PostLinkedConsentV2Response,
                    parse_obj_as(
                        type_=PostLinkedConsentV2Response,
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
