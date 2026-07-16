

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_returns_average_request_assets_item import PostAssetsReturnsAverageRequestAssetsItem
from .types.post_assets_returns_average_response import PostAssetsReturnsAverageResponse
from .types.post_assets_returns_request_assets_item import PostAssetsReturnsRequestAssetsItem
from .types.post_assets_returns_response import PostAssetsReturnsResponse


OMIT = typing.cast(typing.Any, ...)


class RawAssetsReturnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def arithmetic_returns(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsReturnsResponse]:
        """
        Compute the arithmetic return(s) of one or several asset(s) for one or several time period(s).

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsReturnsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/returns",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets, annotation=typing.Sequence[PostAssetsReturnsRequestAssetsItem], direction="write"
                ),
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
                    PostAssetsReturnsResponse,
                    parse_obj_as(
                        type_=PostAssetsReturnsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def arithmetic_average_return(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsReturnsAverageResponse]:
        """
        Compute the arithmetic average of the return(s) of one or several asset(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsReturnsAverageResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/returns/average",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem],
                    direction="write",
                ),
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
                    PostAssetsReturnsAverageResponse,
                    parse_obj_as(
                        type_=PostAssetsReturnsAverageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAssetsReturnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def arithmetic_returns(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsReturnsResponse]:
        """
        Compute the arithmetic return(s) of one or several asset(s) for one or several time period(s).

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsReturnsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/returns",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets, annotation=typing.Sequence[PostAssetsReturnsRequestAssetsItem], direction="write"
                ),
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
                    PostAssetsReturnsResponse,
                    parse_obj_as(
                        type_=PostAssetsReturnsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def arithmetic_average_return(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsReturnsAverageResponse]:
        """
        Compute the arithmetic average of the return(s) of one or several asset(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsReturnsAverageResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/returns/average",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem],
                    direction="write",
                ),
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
                    PostAssetsReturnsAverageResponse,
                    parse_obj_as(
                        type_=PostAssetsReturnsAverageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
