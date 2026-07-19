

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..types.error import Error
from ..types.field_element import FieldElement
from ..types.semaphore_proof import SemaphoreProof
from ..types.semaphore_proof_verification_result import SemaphoreProofVerificationResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSemaphoreProofClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def verify_semaphore_proof(
        self,
        *,
        root: FieldElement,
        signal_hash: FieldElement,
        nullifier_hash: FieldElement,
        external_nullifier_hash: FieldElement,
        proof: SemaphoreProof,
        max_root_age_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SemaphoreProofVerificationResult]:
        """
        Parameters
        ----------
        root : FieldElement

        signal_hash : FieldElement

        nullifier_hash : FieldElement

        external_nullifier_hash : FieldElement

        proof : SemaphoreProof

        max_root_age_seconds : typing.Optional[int]
            Maximum age of the root in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SemaphoreProofVerificationResult]
            Verification processed, check response for result
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/semaphore-proof/verify",
            method="POST",
            json={
                "root": root,
                "signalHash": signal_hash,
                "nullifierHash": nullifier_hash,
                "externalNullifierHash": external_nullifier_hash,
                "proof": proof,
                "maxRootAgeSeconds": max_root_age_seconds,
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
                    SemaphoreProofVerificationResult,
                    parse_obj_as(
                        type_=SemaphoreProofVerificationResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawSemaphoreProofClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def verify_semaphore_proof(
        self,
        *,
        root: FieldElement,
        signal_hash: FieldElement,
        nullifier_hash: FieldElement,
        external_nullifier_hash: FieldElement,
        proof: SemaphoreProof,
        max_root_age_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SemaphoreProofVerificationResult]:
        """
        Parameters
        ----------
        root : FieldElement

        signal_hash : FieldElement

        nullifier_hash : FieldElement

        external_nullifier_hash : FieldElement

        proof : SemaphoreProof

        max_root_age_seconds : typing.Optional[int]
            Maximum age of the root in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SemaphoreProofVerificationResult]
            Verification processed, check response for result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/semaphore-proof/verify",
            method="POST",
            json={
                "root": root,
                "signalHash": signal_hash,
                "nullifierHash": nullifier_hash,
                "externalNullifierHash": external_nullifier_hash,
                "proof": proof,
                "maxRootAgeSeconds": max_root_age_seconds,
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
                    SemaphoreProofVerificationResult,
                    parse_obj_as(
                        type_=SemaphoreProofVerificationResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
