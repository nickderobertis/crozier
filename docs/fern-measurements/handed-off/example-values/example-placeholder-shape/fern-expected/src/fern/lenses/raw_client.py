

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.append_lens_logs_response import AppendLensLogsResponse
from .types.batch_lens_records_response import BatchLensRecordsResponse
from .types.update_lens_settings_response import UpdateLensSettingsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def update_lens_settings(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateLensSettingsResponse]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateLensSettingsResponse]
            Updated
        """
        _response = self._client_wrapper.httpx_client.request(
            "lenses/settings",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLensSettingsResponse,
                    parse_obj_as(
                        type_=UpdateLensSettingsResponse,
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

    def append_lens_logs(
        self,
        lens_id: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AppendLensLogsResponse]:
        """
        Parameters
        ----------
        lens_id : int

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AppendLensLogsResponse]
            Appended
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lenses/{encode_path_param(lens_id)}/logs",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppendLensLogsResponse,
                    parse_obj_as(
                        type_=AppendLensLogsResponse,
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

    def batch_lens_records(
        self,
        lens_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchLensRecordsResponse]:
        """
        Parameters
        ----------
        lens_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchLensRecordsResponse]
            Recorded
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lenses/{encode_path_param(lens_id)}/batch",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchLensRecordsResponse,
                    parse_obj_as(
                        type_=BatchLensRecordsResponse,
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


class AsyncRawLensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def update_lens_settings(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateLensSettingsResponse]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateLensSettingsResponse]
            Updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lenses/settings",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLensSettingsResponse,
                    parse_obj_as(
                        type_=UpdateLensSettingsResponse,
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

    async def append_lens_logs(
        self,
        lens_id: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AppendLensLogsResponse]:
        """
        Parameters
        ----------
        lens_id : int

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AppendLensLogsResponse]
            Appended
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lenses/{encode_path_param(lens_id)}/logs",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppendLensLogsResponse,
                    parse_obj_as(
                        type_=AppendLensLogsResponse,
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

    async def batch_lens_records(
        self,
        lens_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchLensRecordsResponse]:
        """
        Parameters
        ----------
        lens_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchLensRecordsResponse]
            Recorded
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lenses/{encode_path_param(lens_id)}/batch",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchLensRecordsResponse,
                    parse_obj_as(
                        type_=BatchLensRecordsResponse,
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
