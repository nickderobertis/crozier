

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.pool import Pool
from ..types.prebuild_environment_options import PrebuildEnvironmentOptions
from ..types.prebuild_template_info_result import PrebuildTemplateInfoResult
from ..types.problem_details import ProblemDetails
from ..types.secret_data_body import SecretDataBody
from ..types.storage_type import StorageType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPrebuildsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Prebuilds/pools/createorupdatesettings",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "pools": convert_and_respect_annotation_metadata(
                    object_=pools, annotation=typing.Optional[typing.Sequence[Pool]], direction="write"
                ),
                "repoId": repo_id,
                "storageType": storage_type,
                "subscription": subscription,
            },
            request_options=request_options,
            omit=OMIT,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_v1geneva_actions_prebuilds_pools_delete(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Prebuilds/pools/delete",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "pools": convert_and_respect_annotation_metadata(
                    object_=pools, annotation=typing.Optional[typing.Sequence[Pool]], direction="write"
                ),
                "repoId": repo_id,
                "storageType": storage_type,
                "subscription": subscription,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Prebuilds/pools/{encode_path_param(pool_id)}/instances",
            method="POST",
            json={
                "environmentOptions": convert_and_respect_annotation_metadata(
                    object_=environment_options, annotation=PrebuildEnvironmentOptions, direction="write"
                ),
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Prebuilds/pools/{encode_path_param(pool_id)}/instances",
            method="PUT",
            json={
                "environmentOptions": convert_and_respect_annotation_metadata(
                    object_=environment_options, annotation=PrebuildEnvironmentOptions, direction="write"
                ),
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_template_info_route(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PrebuildTemplateInfoResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrebuildTemplateInfoResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Prebuilds/template/{encode_path_param(environment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrebuildTemplateInfoResult,
                    parse_obj_as(
                        type_=PrebuildTemplateInfoResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPrebuildsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Prebuilds/pools/createorupdatesettings",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "pools": convert_and_respect_annotation_metadata(
                    object_=pools, annotation=typing.Optional[typing.Sequence[Pool]], direction="write"
                ),
                "repoId": repo_id,
                "storageType": storage_type,
                "subscription": subscription,
            },
            request_options=request_options,
            omit=OMIT,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_v1geneva_actions_prebuilds_pools_delete(
        self,
        *,
        branch_name: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        pools: typing.Optional[typing.Sequence[Pool]] = OMIT,
        repo_id: typing.Optional[str] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        subscription: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        pools : typing.Optional[typing.Sequence[Pool]]

        repo_id : typing.Optional[str]

        storage_type : typing.Optional[StorageType]

        subscription : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Prebuilds/pools/delete",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "pools": convert_and_respect_annotation_metadata(
                    object_=pools, annotation=typing.Optional[typing.Sequence[Pool]], direction="write"
                ),
                "repoId": repo_id,
                "storageType": storage_type,
                "subscription": subscription,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Prebuilds/pools/{encode_path_param(pool_id)}/instances",
            method="POST",
            json={
                "environmentOptions": convert_and_respect_annotation_metadata(
                    object_=environment_options, annotation=PrebuildEnvironmentOptions, direction="write"
                ),
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_api_v1prebuilds_pools_pool_id_instances(
        self,
        pool_id: str,
        *,
        environment_options: typing.Optional[PrebuildEnvironmentOptions] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        pool_id : str

        environment_options : typing.Optional[PrebuildEnvironmentOptions]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Prebuilds/pools/{encode_path_param(pool_id)}/instances",
            method="PUT",
            json={
                "environmentOptions": convert_and_respect_annotation_metadata(
                    object_=environment_options, annotation=PrebuildEnvironmentOptions, direction="write"
                ),
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_template_info_route(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PrebuildTemplateInfoResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrebuildTemplateInfoResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Prebuilds/template/{encode_path_param(environment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrebuildTemplateInfoResult,
                    parse_obj_as(
                        type_=PrebuildTemplateInfoResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
