

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.job_list import JobList
from pydantic import ValidationError


class RawJobListClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[JobList]:
        """
        List available jobs.

        For more information, see [OGC API — Processes — Part 1 Section 11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_job_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobList]
            A list of jobs for this process.
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobList,
                    parse_obj_as(
                        type_=JobList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )


class AsyncRawJobListClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[JobList]:
        """
        List available jobs.

        For more information, see [OGC API — Processes — Part 1 Section 11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_job_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobList]
            A list of jobs for this process.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobList,
                    parse_obj_as(
                        type_=JobList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )
