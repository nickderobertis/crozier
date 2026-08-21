

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_medication_request_filter import GetMedicationRequestFilter
from .types.get_medication_response import GetMedicationResponse
from pydantic import ValidationError


class RawMedicationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def route_for_getting_filtered_medication_requests(
        self,
        *,
        filter: typing.Optional[GetMedicationRequestFilter] = None,
        value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetMedicationResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[GetMedicationRequestFilter]
            Pass the filter parameter you want to filter by

        value : typing.Optional[str]
            The value for the filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMedicationResponse]
            Success response from medication API
        """
        _response = self._client_wrapper.httpx_client.request(
            "medication",
            method="GET",
            params={
                "filter": filter,
                "value": value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMedicationResponse,
                    parse_obj_as(
                        type_=GetMedicationResponse,
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


class AsyncRawMedicationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def route_for_getting_filtered_medication_requests(
        self,
        *,
        filter: typing.Optional[GetMedicationRequestFilter] = None,
        value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetMedicationResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[GetMedicationRequestFilter]
            Pass the filter parameter you want to filter by

        value : typing.Optional[str]
            The value for the filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMedicationResponse]
            Success response from medication API
        """
        _response = await self._client_wrapper.httpx_client.request(
            "medication",
            method="GET",
            params={
                "filter": filter,
                "value": value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMedicationResponse,
                    parse_obj_as(
                        type_=GetMedicationResponse,
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
