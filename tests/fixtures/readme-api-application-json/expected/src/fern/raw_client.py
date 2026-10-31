

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.post_anything_request_arr_mix_item import PostAnythingRequestArrMixItem
from .types.post_anything_request_nested import PostAnythingRequestNested
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_anything(
        self,
        *,
        number: typing.Optional[float] = OMIT,
        string: typing.Optional[str] = OMIT,
        arr: typing.Optional[typing.Sequence[float]] = OMIT,
        nested: typing.Optional[PostAnythingRequestNested] = OMIT,
        arr_mix: typing.Optional[typing.Sequence[PostAnythingRequestArrMixItem]] = OMIT,
        boolean: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        number : typing.Optional[float]

        string : typing.Optional[str]

        arr : typing.Optional[typing.Sequence[float]]

        nested : typing.Optional[PostAnythingRequestNested]

        arr_mix : typing.Optional[typing.Sequence[PostAnythingRequestArrMixItem]]

        boolean : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "anything",
            method="POST",
            json={
                "number": number,
                "string": string,
                "arr": arr,
                "nested": convert_and_respect_annotation_metadata(
                    object_=nested, annotation=PostAnythingRequestNested, direction="write"
                ),
                "arr_mix": convert_and_respect_annotation_metadata(
                    object_=arr_mix, annotation=typing.Sequence[PostAnythingRequestArrMixItem], direction="write"
                ),
                "boolean": boolean,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    async def post_anything(
        self,
        *,
        number: typing.Optional[float] = OMIT,
        string: typing.Optional[str] = OMIT,
        arr: typing.Optional[typing.Sequence[float]] = OMIT,
        nested: typing.Optional[PostAnythingRequestNested] = OMIT,
        arr_mix: typing.Optional[typing.Sequence[PostAnythingRequestArrMixItem]] = OMIT,
        boolean: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        number : typing.Optional[float]

        string : typing.Optional[str]

        arr : typing.Optional[typing.Sequence[float]]

        nested : typing.Optional[PostAnythingRequestNested]

        arr_mix : typing.Optional[typing.Sequence[PostAnythingRequestArrMixItem]]

        boolean : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "anything",
            method="POST",
            json={
                "number": number,
                "string": string,
                "arr": arr,
                "nested": convert_and_respect_annotation_metadata(
                    object_=nested, annotation=PostAnythingRequestNested, direction="write"
                ),
                "arr_mix": convert_and_respect_annotation_metadata(
                    object_=arr_mix, annotation=typing.Sequence[PostAnythingRequestArrMixItem], direction="write"
                ),
                "boolean": boolean,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
