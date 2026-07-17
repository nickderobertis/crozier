

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_skewness_request_assets_item import PostAssetsSkewnessRequestAssetsItem
from .types.post_assets_skewness_response import PostAssetsSkewnessResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssetsSkewnessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def skewness(
        self,
        *,
        assets: typing.Sequence[PostAssetsSkewnessRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsSkewnessResponse]:
        """
        Compute the skewness of one or several asset(s), from the asset returns.

        References
        * [Wikipedia, Skewness](https://en.wikipedia.org/wiki/Skewness)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsSkewnessRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsSkewnessResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/skewness",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets, annotation=typing.Sequence[PostAssetsSkewnessRequestAssetsItem], direction="write"
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
                    PostAssetsSkewnessResponse,
                    parse_obj_as(
                        type_=PostAssetsSkewnessResponse,
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


class AsyncRawAssetsSkewnessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def skewness(
        self,
        *,
        assets: typing.Sequence[PostAssetsSkewnessRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsSkewnessResponse]:
        """
        Compute the skewness of one or several asset(s), from the asset returns.

        References
        * [Wikipedia, Skewness](https://en.wikipedia.org/wiki/Skewness)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsSkewnessRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsSkewnessResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/skewness",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets, annotation=typing.Sequence[PostAssetsSkewnessRequestAssetsItem], direction="write"
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
                    PostAssetsSkewnessResponse,
                    parse_obj_as(
                        type_=PostAssetsSkewnessResponse,
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
