

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.capsule import Capsule
from ..types.verification_result import VerificationResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCapsulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_capsule(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Capsule]:
        """
        Create a time capsule (immutable artifact) from a completed run

        Parameters
        ----------
        run_id : str
            The run ID to create a capsule from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Capsule]
            Capsule created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "capsules",
            method="POST",
            json={
                "run_id": run_id,
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
                    Capsule,
                    parse_obj_as(
                        type_=Capsule,
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

    def verify_capsule(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VerificationResult]:
        """
        Verify the integrity of a capsule file

        Parameters
        ----------
        path : str
            Path to the capsule file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VerificationResult]
            Verification result
        """
        _response = self._client_wrapper.httpx_client.request(
            "capsules/verify",
            method="POST",
            json={
                "path": path,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCapsulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_capsule(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Capsule]:
        """
        Create a time capsule (immutable artifact) from a completed run

        Parameters
        ----------
        run_id : str
            The run ID to create a capsule from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Capsule]
            Capsule created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "capsules",
            method="POST",
            json={
                "run_id": run_id,
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
                    Capsule,
                    parse_obj_as(
                        type_=Capsule,
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

    async def verify_capsule(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VerificationResult]:
        """
        Verify the integrity of a capsule file

        Parameters
        ----------
        path : str
            Path to the capsule file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VerificationResult]
            Verification result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "capsules/verify",
            method="POST",
            json={
                "path": path,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
