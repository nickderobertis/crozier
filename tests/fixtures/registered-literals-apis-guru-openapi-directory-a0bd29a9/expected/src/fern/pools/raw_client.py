

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.pool_status_response_body import PoolStatusResponseBody
from ..types.system_configuration_response import SystemConfigurationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPoolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_api_v1geneva_actions_pools_change_resource_deletion_setting(
        self,
        *,
        comment: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SystemConfigurationResponse]:
        """
        Parameters
        ----------
        comment : typing.Optional[str]

        enabled : typing.Optional[bool]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SystemConfigurationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Pools/change-resource-deletion-setting",
            method="POST",
            json={
                "comment": comment,
                "enabled": enabled,
                "poolCode": pool_code,
                "poolType": pool_type,
                "region": region,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemConfigurationResponse,
                    parse_obj_as(
                        type_=SystemConfigurationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_v1geneva_actions_pools_pool_code_rotate_pool(
        self, pool_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        pool_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Pools/{encode_path_param(pool_code)}/rotate-pool",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_v1geneva_actions_pools_target(
        self,
        target: str,
        *,
        comment: typing.Optional[str] = OMIT,
        max_target_count: typing.Optional[str] = OMIT,
        min_target_count: typing.Optional[str] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        target_count: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SystemConfigurationResponse]:
        """
        Parameters
        ----------
        target : str

        comment : typing.Optional[str]

        max_target_count : typing.Optional[str]

        min_target_count : typing.Optional[str]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        target_count : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SystemConfigurationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Pools/{encode_path_param(target)}",
            method="POST",
            json={
                "comment": comment,
                "maxTargetCount": max_target_count,
                "minTargetCount": min_target_count,
                "poolCode": pool_code,
                "poolType": pool_type,
                "region": region,
                "targetCount": target_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemConfigurationResponse,
                    parse_obj_as(
                        type_=SystemConfigurationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_api_v1pools_default(
        self,
        *,
        sku_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[PoolStatusResponseBody]]:
        """
        Parameters
        ----------
        sku_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PoolStatusResponseBody]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/pools/default",
            method="GET",
            params={
                "skuName": sku_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PoolStatusResponseBody],
                    parse_obj_as(
                        type_=typing.List[PoolStatusResponseBody],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawPoolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_api_v1geneva_actions_pools_change_resource_deletion_setting(
        self,
        *,
        comment: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SystemConfigurationResponse]:
        """
        Parameters
        ----------
        comment : typing.Optional[str]

        enabled : typing.Optional[bool]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SystemConfigurationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Pools/change-resource-deletion-setting",
            method="POST",
            json={
                "comment": comment,
                "enabled": enabled,
                "poolCode": pool_code,
                "poolType": pool_type,
                "region": region,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemConfigurationResponse,
                    parse_obj_as(
                        type_=SystemConfigurationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_v1geneva_actions_pools_pool_code_rotate_pool(
        self, pool_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        pool_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Pools/{encode_path_param(pool_code)}/rotate-pool",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_v1geneva_actions_pools_target(
        self,
        target: str,
        *,
        comment: typing.Optional[str] = OMIT,
        max_target_count: typing.Optional[str] = OMIT,
        min_target_count: typing.Optional[str] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        target_count: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SystemConfigurationResponse]:
        """
        Parameters
        ----------
        target : str

        comment : typing.Optional[str]

        max_target_count : typing.Optional[str]

        min_target_count : typing.Optional[str]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        target_count : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SystemConfigurationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Pools/{encode_path_param(target)}",
            method="POST",
            json={
                "comment": comment,
                "maxTargetCount": max_target_count,
                "minTargetCount": min_target_count,
                "poolCode": pool_code,
                "poolType": pool_type,
                "region": region,
                "targetCount": target_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemConfigurationResponse,
                    parse_obj_as(
                        type_=SystemConfigurationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_api_v1pools_default(
        self,
        *,
        sku_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[PoolStatusResponseBody]]:
        """
        Parameters
        ----------
        sku_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PoolStatusResponseBody]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/pools/default",
            method="GET",
            params={
                "skuName": sku_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PoolStatusResponseBody],
                    parse_obj_as(
                        type_=typing.List[PoolStatusResponseBody],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
