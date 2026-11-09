

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.error_response import ErrorResponse
from ..types.signed_bundle_v2 import SignedBundleV2
from ..types.verification_result import VerificationResult
from .types.verify_bundle_request_signed_bundle import VerifyBundleRequestSignedBundle
from .types.verify_bundle_v2response import VerifyBundleV2Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVerificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def verify_bundle(
        self,
        *,
        signed_bundle: VerifyBundleRequestSignedBundle,
        public_key_b64: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VerificationResult]:
        """
        Performs full DCP verification with automatic version detection:

        V1: Schema validation, Ed25519 signature, bundle hash integrity,
        Merkle root, intent hash chain, and previous hash chain verification.

        V2: Composite signature structure, session nonce consistency,
        manifest integrity, tier-aware policy enforcement.

        Parameters
        ----------
        signed_bundle : VerifyBundleRequestSignedBundle

        public_key_b64 : typing.Optional[str]
            Optional Ed25519 public key (base64) for V1. Falls back to signer.public_key_b64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VerificationResult]
            Verification result
        """
        _response = self._client_wrapper.httpx_client.request(
            "verify",
            method="POST",
            json={
                "signed_bundle": convert_and_respect_annotation_metadata(
                    object_=signed_bundle, annotation=VerifyBundleRequestSignedBundle, direction="write"
                ),
                "public_key_b64": public_key_b64,
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
                    VerificationResult,
                    parse_obj_as(
                        type_=VerificationResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def verify_bundle_v2(
        self,
        *,
        signed_bundle: typing.Optional[SignedBundleV2] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VerifyBundleV2Response]:
        """
        Performs tier-aware V2 bundle verification including composite signature
        validation, session binding, manifest integrity, and security tier enforcement.

        Parameters
        ----------
        signed_bundle : typing.Optional[SignedBundleV2]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VerifyBundleV2Response]
            V2 verification result
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bundle/verify",
            method="POST",
            json={
                "signed_bundle": convert_and_respect_annotation_metadata(
                    object_=signed_bundle, annotation=SignedBundleV2, direction="write"
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
                    VerifyBundleV2Response,
                    parse_obj_as(
                        type_=VerifyBundleV2Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawVerificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def verify_bundle(
        self,
        *,
        signed_bundle: VerifyBundleRequestSignedBundle,
        public_key_b64: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VerificationResult]:
        """
        Performs full DCP verification with automatic version detection:

        V1: Schema validation, Ed25519 signature, bundle hash integrity,
        Merkle root, intent hash chain, and previous hash chain verification.

        V2: Composite signature structure, session nonce consistency,
        manifest integrity, tier-aware policy enforcement.

        Parameters
        ----------
        signed_bundle : VerifyBundleRequestSignedBundle

        public_key_b64 : typing.Optional[str]
            Optional Ed25519 public key (base64) for V1. Falls back to signer.public_key_b64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VerificationResult]
            Verification result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "verify",
            method="POST",
            json={
                "signed_bundle": convert_and_respect_annotation_metadata(
                    object_=signed_bundle, annotation=VerifyBundleRequestSignedBundle, direction="write"
                ),
                "public_key_b64": public_key_b64,
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
                    VerificationResult,
                    parse_obj_as(
                        type_=VerificationResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def verify_bundle_v2(
        self,
        *,
        signed_bundle: typing.Optional[SignedBundleV2] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VerifyBundleV2Response]:
        """
        Performs tier-aware V2 bundle verification including composite signature
        validation, session binding, manifest integrity, and security tier enforcement.

        Parameters
        ----------
        signed_bundle : typing.Optional[SignedBundleV2]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VerifyBundleV2Response]
            V2 verification result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bundle/verify",
            method="POST",
            json={
                "signed_bundle": convert_and_respect_annotation_metadata(
                    object_=signed_bundle, annotation=SignedBundleV2, direction="write"
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
                    VerifyBundleV2Response,
                    parse_obj_as(
                        type_=VerifyBundleV2Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
