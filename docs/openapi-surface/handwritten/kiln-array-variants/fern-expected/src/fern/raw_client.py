

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.create_profile_request_phase import CreateProfileRequestPhase
from .types.create_profile_request_unit import CreateProfileRequestUnit
from .types.create_profile_request_zone import CreateProfileRequestZone
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_profile(
        self,
        *,
        phase: typing.Optional[CreateProfileRequestPhase] = OMIT,
        unit: typing.Optional[CreateProfileRequestUnit] = OMIT,
        zone: typing.Optional[CreateProfileRequestZone] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        phase : typing.Optional[CreateProfileRequestPhase]

        unit : typing.Optional[CreateProfileRequestUnit]

        zone : typing.Optional[CreateProfileRequestZone]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "profiles",
            method="POST",
            json={
                "phase": convert_and_respect_annotation_metadata(
                    object_=phase, annotation=CreateProfileRequestPhase, direction="write"
                ),
                "unit": convert_and_respect_annotation_metadata(
                    object_=unit, annotation=CreateProfileRequestUnit, direction="write"
                ),
                "zone": convert_and_respect_annotation_metadata(
                    object_=zone, annotation=CreateProfileRequestZone, direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_profile(
        self,
        *,
        phase: typing.Optional[CreateProfileRequestPhase] = OMIT,
        unit: typing.Optional[CreateProfileRequestUnit] = OMIT,
        zone: typing.Optional[CreateProfileRequestZone] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        phase : typing.Optional[CreateProfileRequestPhase]

        unit : typing.Optional[CreateProfileRequestUnit]

        zone : typing.Optional[CreateProfileRequestZone]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "profiles",
            method="POST",
            json={
                "phase": convert_and_respect_annotation_metadata(
                    object_=phase, annotation=CreateProfileRequestPhase, direction="write"
                ),
                "unit": convert_and_respect_annotation_metadata(
                    object_=unit, annotation=CreateProfileRequestUnit, direction="write"
                ),
                "zone": convert_and_respect_annotation_metadata(
                    object_=zone, annotation=CreateProfileRequestZone, direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
