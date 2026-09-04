

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.bad_request import BadRequest
from ..types.not_found import NotFound
from ..types.too_many_requests import TooManyRequests
from ..types.video import Video
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVideosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_videos_video_id_source(
        self,
        video_id: str,
        *,
        file: core.File,
        content_range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Video]:
        """
        Ingest a video from a source or file.

        Parameters
        ----------
        video_id : str
            Enter the videoId you want to use to upload your video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            `part <part>/<total_parts>` ; `bytes <from_byte>-<to_byte>/<total_bytes>`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Video]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"videos/{encode_path_param(video_id)}/source",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "Content-Range": str(content_range) if content_range is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Video,
                    parse_obj_as(
                        type_=Video,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFound,
                        parse_obj_as(
                            type_=NotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequests,
                        parse_obj_as(
                            type_=TooManyRequests,
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

    def post_upload(
        self,
        *,
        token: str,
        file: core.File,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Video]:
        """
        Uploading a video with the delegated upload token.

        Parameters
        ----------
        token : str
            The unique identifier for the token you want to use to upload a video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.

        video_id : typing.Optional[str]
            The video id returned by the first call to this endpoint in a large video upload scenario.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Video]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "upload",
            method="POST",
            params={
                "token": token,
            },
            data={
                "videoId": video_id,
            },
            files={
                "file": file,
            },
            headers={
                "Content-Range": str(content_range) if content_range is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Video,
                    parse_obj_as(
                        type_=Video,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequests,
                        parse_obj_as(
                            type_=TooManyRequests,
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


class AsyncRawVideosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_videos_video_id_source(
        self,
        video_id: str,
        *,
        file: core.File,
        content_range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Video]:
        """
        Ingest a video from a source or file.

        Parameters
        ----------
        video_id : str
            Enter the videoId you want to use to upload your video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            `part <part>/<total_parts>` ; `bytes <from_byte>-<to_byte>/<total_bytes>`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Video]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"videos/{encode_path_param(video_id)}/source",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "Content-Range": str(content_range) if content_range is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Video,
                    parse_obj_as(
                        type_=Video,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFound,
                        parse_obj_as(
                            type_=NotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequests,
                        parse_obj_as(
                            type_=TooManyRequests,
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

    async def post_upload(
        self,
        *,
        token: str,
        file: core.File,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Video]:
        """
        Uploading a video with the delegated upload token.

        Parameters
        ----------
        token : str
            The unique identifier for the token you want to use to upload a video.

        file : core.File
            See core.File for more documentation

        content_range : typing.Optional[str]
            Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.

        video_id : typing.Optional[str]
            The video id returned by the first call to this endpoint in a large video upload scenario.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Video]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "upload",
            method="POST",
            params={
                "token": token,
            },
            data={
                "videoId": video_id,
            },
            files={
                "file": file,
            },
            headers={
                "Content-Range": str(content_range) if content_range is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Video,
                    parse_obj_as(
                        type_=Video,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequests,
                        parse_obj_as(
                            type_=TooManyRequests,
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
