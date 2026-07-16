

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_volatility_request import PostAssetsVolatilityRequest
from .types.post_assets_volatility_response import PostAssetsVolatilityResponse


OMIT = typing.cast(typing.Any, ...)


class RawAssetsVolatilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def volatility(
        self, *, request: PostAssetsVolatilityRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostAssetsVolatilityResponse]:
        """
        Compute the volatility (i.e., standard deviation) of one or several asset(s) from either:
        * The asset returns
        * The asset covariance matrix
        * The asset variance(s)

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation)

        Parameters
        ----------
        request : PostAssetsVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsVolatilityResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/volatility",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsVolatilityRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsVolatilityResponse,
                    parse_obj_as(
                        type_=PostAssetsVolatilityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAssetsVolatilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def volatility(
        self, *, request: PostAssetsVolatilityRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostAssetsVolatilityResponse]:
        """
        Compute the volatility (i.e., standard deviation) of one or several asset(s) from either:
        * The asset returns
        * The asset covariance matrix
        * The asset variance(s)

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation)

        Parameters
        ----------
        request : PostAssetsVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsVolatilityResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/volatility",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsVolatilityRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsVolatilityResponse,
                    parse_obj_as(
                        type_=PostAssetsVolatilityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
