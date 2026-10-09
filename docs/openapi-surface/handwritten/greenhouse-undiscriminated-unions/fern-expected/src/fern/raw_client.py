

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.origin import Origin
from .types.propagation import Propagation
from .types.schedule_planting_request import SchedulePlantingRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def schedule_planting(
        self, *, request: SchedulePlantingRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Propagation]:
        """
        Parameters
        ----------
        request : SchedulePlantingRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Propagation]
            The planting as recorded
        """
        _response = self._client_wrapper.httpx_client.request(
            "plantings",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=SchedulePlantingRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Propagation,
                    parse_obj_as(
                        type_=Propagation,
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

    def get_origin(
        self, planting_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Origin]:
        """
        Parameters
        ----------
        planting_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Origin]
            How the planting was started
        """
        _response = self._client_wrapper.httpx_client.request(
            f"plantings/{encode_path_param(planting_id)}/origin",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Origin,
                    parse_obj_as(
                        type_=Origin,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def schedule_planting(
        self, *, request: SchedulePlantingRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Propagation]:
        """
        Parameters
        ----------
        request : SchedulePlantingRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Propagation]
            The planting as recorded
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plantings",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=SchedulePlantingRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Propagation,
                    parse_obj_as(
                        type_=Propagation,
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

    async def get_origin(
        self, planting_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Origin]:
        """
        Parameters
        ----------
        planting_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Origin]
            How the planting was started
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"plantings/{encode_path_param(planting_id)}/origin",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Origin,
                    parse_obj_as(
                        type_=Origin,
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
