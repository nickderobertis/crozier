

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.feature_flags_get_response import FeatureFlagsGetResponse
from .types.feature_flags_patch_request_enabled import FeatureFlagsPatchRequestEnabled
from .types.feature_flags_patch_response import FeatureFlagsPatchResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFeatureFlagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[FeatureFlagsGetResponse]:
        """
        Returns all feature flags with their current values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeatureFlagsGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/feature-flags",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureFlagsGetResponse,
                    parse_obj_as(
                        type_=FeatureFlagsGetResponse,
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

    def patch(
        self,
        flag_key: str,
        *,
        enabled: FeatureFlagsPatchRequestEnabled,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeatureFlagsPatchResponse]:
        """
        Set the enabled state of a single feature flag.

        Parameters
        ----------
        flag_key : str
            The kebab-case flag identifier

        enabled : FeatureFlagsPatchRequestEnabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeatureFlagsPatchResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feature-flags/{encode_path_param(flag_key)}",
            method="PATCH",
            json={
                "enabled": convert_and_respect_annotation_metadata(
                    object_=enabled, annotation=FeatureFlagsPatchRequestEnabled, direction="write"
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
                    FeatureFlagsPatchResponse,
                    parse_obj_as(
                        type_=FeatureFlagsPatchResponse,
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


class AsyncRawFeatureFlagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FeatureFlagsGetResponse]:
        """
        Returns all feature flags with their current values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeatureFlagsGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/feature-flags",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureFlagsGetResponse,
                    parse_obj_as(
                        type_=FeatureFlagsGetResponse,
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

    async def patch(
        self,
        flag_key: str,
        *,
        enabled: FeatureFlagsPatchRequestEnabled,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeatureFlagsPatchResponse]:
        """
        Set the enabled state of a single feature flag.

        Parameters
        ----------
        flag_key : str
            The kebab-case flag identifier

        enabled : FeatureFlagsPatchRequestEnabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeatureFlagsPatchResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feature-flags/{encode_path_param(flag_key)}",
            method="PATCH",
            json={
                "enabled": convert_and_respect_annotation_metadata(
                    object_=enabled, annotation=FeatureFlagsPatchRequestEnabled, direction="write"
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
                    FeatureFlagsPatchResponse,
                    parse_obj_as(
                        type_=FeatureFlagsPatchResponse,
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
