

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.feature import Feature


class RawFeaturesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_feature_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Feature]:
        """
        # Feature

        When you gain a new level in a class, you get its features for that level.
        You don’t, however, receive the class’s starting Equipment, and a few
        features have additional rules when you’re multiclassing: Channel Divinity,
        Extra Attack, Unarmored Defense, and Spellcasting.

        Parameters
        ----------
        index : str
            The `index` of the feature to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `features`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Feature]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/features/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Feature,
                    parse_obj_as(
                        type_=Feature,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFeaturesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_feature_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Feature]:
        """
        # Feature

        When you gain a new level in a class, you get its features for that level.
        You don’t, however, receive the class’s starting Equipment, and a few
        features have additional rules when you’re multiclassing: Channel Divinity,
        Extra Attack, Unarmored Defense, and Spellcasting.

        Parameters
        ----------
        index : str
            The `index` of the feature to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `features`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Feature]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/features/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Feature,
                    parse_obj_as(
                        type_=Feature,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
