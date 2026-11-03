

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.record_reading_response import RecordReadingResponse
from .types.register_buoy_response import RegisterBuoyResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBuoysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_buoy(
        self,
        *,
        survey_ref: str,
        label: str,
        depth_metres: int,
        harbour: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RegisterBuoyResponse]:
        """
        Parameters
        ----------
        survey_ref : str

        label : str

        depth_metres : int

        harbour : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegisterBuoyResponse]
            Registered
        """
        _response = self._client_wrapper.httpx_client.request(
            "buoys",
            method="POST",
            data={
                "label": label,
                "depth_metres": depth_metres,
                "harbour": harbour,
            },
            files={},
            headers={
                "X-Survey-Ref": str(survey_ref) if survey_ref is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegisterBuoyResponse,
                    parse_obj_as(
                        type_=RegisterBuoyResponse,
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

    def record_reading(
        self,
        buoy_id: str,
        *,
        berth: int,
        note: str,
        swell: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecordReadingResponse]:
        """
        Parameters
        ----------
        buoy_id : str

        berth : int

        note : str

        swell : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RecordReadingResponse]
            Recorded
        """
        _response = self._client_wrapper.httpx_client.request(
            f"buoys/{encode_path_param(buoy_id)}/readings",
            method="POST",
            params={
                "berth": berth,
            },
            json={
                "note": note,
                "swell": swell,
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
                    RecordReadingResponse,
                    parse_obj_as(
                        type_=RecordReadingResponse,
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


class AsyncRawBuoysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_buoy(
        self,
        *,
        survey_ref: str,
        label: str,
        depth_metres: int,
        harbour: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RegisterBuoyResponse]:
        """
        Parameters
        ----------
        survey_ref : str

        label : str

        depth_metres : int

        harbour : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegisterBuoyResponse]
            Registered
        """
        _response = await self._client_wrapper.httpx_client.request(
            "buoys",
            method="POST",
            data={
                "label": label,
                "depth_metres": depth_metres,
                "harbour": harbour,
            },
            files={},
            headers={
                "X-Survey-Ref": str(survey_ref) if survey_ref is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegisterBuoyResponse,
                    parse_obj_as(
                        type_=RegisterBuoyResponse,
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

    async def record_reading(
        self,
        buoy_id: str,
        *,
        berth: int,
        note: str,
        swell: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecordReadingResponse]:
        """
        Parameters
        ----------
        buoy_id : str

        berth : int

        note : str

        swell : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RecordReadingResponse]
            Recorded
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"buoys/{encode_path_param(buoy_id)}/readings",
            method="POST",
            params={
                "berth": berth,
            },
            json={
                "note": note,
                "swell": swell,
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
                    RecordReadingResponse,
                    parse_obj_as(
                        type_=RecordReadingResponse,
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
