

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
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.domain_user_credentials import DomainUserCredentials
from ..types.hot_pool_settings import HotPoolSettings
from ..types.pool_result import PoolResult
from ..types.problem_details import ProblemDetails
from ..types.vm_specs import VmSpecs
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPoolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PoolResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PoolResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PoolResult,
                    parse_obj_as(
                        type_=PoolResult,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def put_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PoolResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PoolResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="PUT",
            json={
                "domainUserCredentials": convert_and_respect_annotation_metadata(
                    object_=domain_user_credentials, annotation=DomainUserCredentials, direction="write"
                ),
                "hotPoolSettings": convert_and_respect_annotation_metadata(
                    object_=hot_pool_settings, annotation=HotPoolSettings, direction="write"
                ),
                "poolGroupName": pool_group_name,
                "tags": tags,
                "userGroupName": user_group_name,
                "vmSpecs": convert_and_respect_annotation_metadata(
                    object_=vm_specs, annotation=VmSpecs, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PoolResult,
                    parse_obj_as(
                        type_=PoolResult,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="DELETE",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def patch_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PoolResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PoolResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="PATCH",
            json={
                "domainUserCredentials": convert_and_respect_annotation_metadata(
                    object_=domain_user_credentials, annotation=DomainUserCredentials, direction="write"
                ),
                "hotPoolSettings": convert_and_respect_annotation_metadata(
                    object_=hot_pool_settings, annotation=HotPoolSettings, direction="write"
                ),
                "poolGroupName": pool_group_name,
                "tags": tags,
                "userGroupName": user_group_name,
                "vmSpecs": convert_and_respect_annotation_metadata(
                    object_=vm_specs, annotation=VmSpecs, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PoolResult,
                    parse_obj_as(
                        type_=PoolResult,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawPoolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PoolResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PoolResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PoolResult,
                    parse_obj_as(
                        type_=PoolResult,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def put_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PoolResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PoolResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="PUT",
            json={
                "domainUserCredentials": convert_and_respect_annotation_metadata(
                    object_=domain_user_credentials, annotation=DomainUserCredentials, direction="write"
                ),
                "hotPoolSettings": convert_and_respect_annotation_metadata(
                    object_=hot_pool_settings, annotation=HotPoolSettings, direction="write"
                ),
                "poolGroupName": pool_group_name,
                "tags": tags,
                "userGroupName": user_group_name,
                "vmSpecs": convert_and_respect_annotation_metadata(
                    object_=vm_specs, annotation=VmSpecs, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PoolResult,
                    parse_obj_as(
                        type_=PoolResult,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="DELETE",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def patch_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PoolResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PoolResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/tenant/{encode_path_param(tenant_id)}/Pool/{encode_path_param(pool_name)}",
            method="PATCH",
            json={
                "domainUserCredentials": convert_and_respect_annotation_metadata(
                    object_=domain_user_credentials, annotation=DomainUserCredentials, direction="write"
                ),
                "hotPoolSettings": convert_and_respect_annotation_metadata(
                    object_=hot_pool_settings, annotation=HotPoolSettings, direction="write"
                ),
                "poolGroupName": pool_group_name,
                "tags": tags,
                "userGroupName": user_group_name,
                "vmSpecs": convert_and_respect_annotation_metadata(
                    object_=vm_specs, annotation=VmSpecs, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PoolResult,
                    parse_obj_as(
                        type_=PoolResult,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
