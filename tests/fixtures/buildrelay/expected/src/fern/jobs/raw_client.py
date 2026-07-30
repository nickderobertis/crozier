

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
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.job_response import JobResponse
from ..types.unauthorized_response import UnauthorizedResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def submit_filesystem_job(
        self,
        *,
        project: str,
        platform: str,
        ingest_path: str,
        description: typing.Optional[str] = OMIT,
        steam_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        cdn_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResponse]:
        """
        Submit a build job from files on the filesystem to be uploaded to configured channels

        Parameters
        ----------
        project : str
            Name of the project being built

        platform : str
            Target platform (e.g., windows, linux, macos)

        ingest_path : str
            Relative path within /builds directory containing build files. Cannot be absolute or contain '..'

        description : typing.Optional[str]
            Description of the build (e.g., version number)

        steam_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of Steam channels to upload to

        cdn_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of CDN channels to upload to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResponse]
            Job successfully created
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/jobs/filesystem",
            method="POST",
            json={
                "project": project,
                "description": description,
                "platform": platform,
                "ingestPath": ingest_path,
                "steam_channel_labels": steam_channel_labels,
                "cdn_channel_labels": cdn_channel_labels,
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
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def submit_filesystem_job(
        self,
        *,
        project: str,
        platform: str,
        ingest_path: str,
        description: typing.Optional[str] = OMIT,
        steam_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        cdn_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResponse]:
        """
        Submit a build job from files on the filesystem to be uploaded to configured channels

        Parameters
        ----------
        project : str
            Name of the project being built

        platform : str
            Target platform (e.g., windows, linux, macos)

        ingest_path : str
            Relative path within /builds directory containing build files. Cannot be absolute or contain '..'

        description : typing.Optional[str]
            Description of the build (e.g., version number)

        steam_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of Steam channels to upload to

        cdn_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of CDN channels to upload to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResponse]
            Job successfully created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/jobs/filesystem",
            method="POST",
            json={
                "project": project,
                "description": description,
                "platform": platform,
                "ingestPath": ingest_path,
                "steam_channel_labels": steam_channel_labels,
                "cdn_channel_labels": cdn_channel_labels,
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
                    JobResponse,
                    parse_obj_as(
                        type_=JobResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
