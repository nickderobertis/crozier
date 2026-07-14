

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.anchore_image_list import AnchoreImageList


OMIT = typing.cast(typing.Any, ...)


class RawImportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def image_archive(
        self, *, archive_file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AnchoreImageList]:
        """
        Parameters
        ----------
        archive_file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnchoreImageList]
            Successfully imported image to the engine
        """
        _response = self._client_wrapper.httpx_client.request(
            "import/images",
            method="POST",
            data={},
            files={
                "archive_file": archive_file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawImportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def image_archive(
        self, *, archive_file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AnchoreImageList]:
        """
        Parameters
        ----------
        archive_file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnchoreImageList]
            Successfully imported image to the engine
        """
        _response = await self._client_wrapper.httpx_client.request(
            "import/images",
            method="POST",
            data={},
            files={
                "archive_file": archive_file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
