

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.process_list import ProcessList
from pydantic import ValidationError


class RawProcessListClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_processes(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ProcessList]:
        """
        The list of processes contains a summary of each process the OGC API - Processes offers, including the link to a more detailed description of the process.

        For more information, see [OGC API — Processes — Part 1 Section 7.9](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProcessList]
            Information about the available processes
        """
        _response = self._client_wrapper.httpx_client.request(
            "processes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProcessList,
                    parse_obj_as(
                        type_=ProcessList,
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


class AsyncRawProcessListClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_processes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProcessList]:
        """
        The list of processes contains a summary of each process the OGC API - Processes offers, including the link to a more detailed description of the process.

        For more information, see [OGC API — Processes — Part 1 Section 7.9](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProcessList]
            Information about the available processes
        """
        _response = await self._client_wrapper.httpx_client.request(
            "processes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProcessList,
                    parse_obj_as(
                        type_=ProcessList,
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
