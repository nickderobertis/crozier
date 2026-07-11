

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.shape import Shape


OMIT = typing.cast(typing.Any, ...)


class RawShapesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def createshape(
        self, *, request: Shape, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Shape]:
        """
        Parameters
        ----------
        request : Shape

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Shape]

        """
        _response = self._client_wrapper.httpx_client.request(
            "shape",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Shape, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Shape,
                    parse_obj_as(
                        type_=Shape,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawShapesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def createshape(
        self, *, request: Shape, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Shape]:
        """
        Parameters
        ----------
        request : Shape

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Shape]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "shape",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Shape, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Shape,
                    parse_obj_as(
                        type_=Shape,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
