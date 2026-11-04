

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
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.create_template_result import CreateTemplateResult
from ..types.experimental_features_body import ExperimentalFeaturesBody
from ..types.prebuild_readiness_result import PrebuildReadinessResult
from ..types.prebuild_template_info import PrebuildTemplateInfo
from ..types.problem_details import ProblemDetails
from ..types.seed_info_body import SeedInfoBody
from ..types.storage_type import StorageType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPrebuildsVClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_api_v2prebuilds_delete(
        self,
        *,
        branch_name: str,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        prebuild_configuration_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : str

        repo_id : int

        dev_container_path : typing.Optional[str]

        prebuild_configuration_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/prebuilds/delete",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "prebuildConfigurationId": prebuild_configuration_id,
                "repoId": repo_id,
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

    def delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
        self, repo_id: int, branch_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        repo_id : int

        branch_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/prebuilds/repository/{encode_path_param(repo_id)}/branch/{encode_path_param(branch_name)}",
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

    def post_api_v2prebuilds_templates(
        self,
        *,
        friendly_name: str,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_prebuild_instance_endpoint: typing.Optional[str] = OMIT,
        git_hub_prebuild_template_endpoint: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        template_info: typing.Optional[PrebuildTemplateInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTemplateResult]:
        """
        Parameters
        ----------
        friendly_name : str

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_prebuild_instance_endpoint : typing.Optional[str]

        git_hub_prebuild_template_endpoint : typing.Optional[str]

        plan_id : typing.Optional[str]

        seed : typing.Optional[SeedInfoBody]

        storage_type : typing.Optional[StorageType]

        template_info : typing.Optional[PrebuildTemplateInfo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTemplateResult]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/prebuilds/templates",
            method="POST",
            json={
                "devContainerPath": dev_container_path,
                "experimentalFeatures": convert_and_respect_annotation_metadata(
                    object_=experimental_features, annotation=ExperimentalFeaturesBody, direction="write"
                ),
                "features": features,
                "friendlyName": friendly_name,
                "gitHubPrebuildInstanceEndpoint": git_hub_prebuild_instance_endpoint,
                "gitHubPrebuildTemplateEndpoint": git_hub_prebuild_template_endpoint,
                "planId": plan_id,
                "seed": convert_and_respect_annotation_metadata(
                    object_=seed, annotation=SeedInfoBody, direction="write"
                ),
                "storageType": storage_type,
                "templateInfo": convert_and_respect_annotation_metadata(
                    object_=template_info, annotation=PrebuildTemplateInfo, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTemplateResult,
                    parse_obj_as(
                        type_=CreateTemplateResult,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_prebuild_readiness_skus_route(
        self,
        repo_id: str,
        branch_name: str,
        prebuild_hash: str,
        location: str,
        dev_container_path: str,
        *,
        storage_type: typing.Optional[StorageType] = None,
        fast_path_enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PrebuildReadinessResult]:
        """
        Parameters
        ----------
        repo_id : str

        branch_name : str

        prebuild_hash : str

        location : str

        dev_container_path : str

        storage_type : typing.Optional[StorageType]

        fast_path_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrebuildReadinessResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/prebuilds/templates/skus/repo/{encode_path_param(repo_id)}/branch/{encode_path_param(branch_name)}/hash/{encode_path_param(prebuild_hash)}/location/{encode_path_param(location)}/devcontainerpath/{encode_path_param(dev_container_path)}",
            method="GET",
            params={
                "storageType": storage_type,
                "fastPathEnabled": fast_path_enabled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrebuildReadinessResult,
                    parse_obj_as(
                        type_=PrebuildReadinessResult,
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

    def post_api_v2prebuilds_templates_updatemaxversions(
        self,
        *,
        branch_name: str,
        max_prebuild_template_versions: int,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : str

        max_prebuild_template_versions : int

        repo_id : int

        dev_container_path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/prebuilds/templates/updatemaxversions",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "maxPrebuildTemplateVersions": max_prebuild_template_versions,
                "repoId": repo_id,
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

    def post_api_v2prebuilds_templates_template_id_updatestatus(
        self, template_id: str, *, is_success: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        template_id : str

        is_success : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/prebuilds/templates/{encode_path_param(template_id)}/updatestatus",
            method="POST",
            json={
                "isSuccess": is_success,
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


class AsyncRawPrebuildsVClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_api_v2prebuilds_delete(
        self,
        *,
        branch_name: str,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        prebuild_configuration_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : str

        repo_id : int

        dev_container_path : typing.Optional[str]

        prebuild_configuration_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/prebuilds/delete",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "prebuildConfigurationId": prebuild_configuration_id,
                "repoId": repo_id,
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

    async def delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
        self, repo_id: int, branch_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        repo_id : int

        branch_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/prebuilds/repository/{encode_path_param(repo_id)}/branch/{encode_path_param(branch_name)}",
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

    async def post_api_v2prebuilds_templates(
        self,
        *,
        friendly_name: str,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_prebuild_instance_endpoint: typing.Optional[str] = OMIT,
        git_hub_prebuild_template_endpoint: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        storage_type: typing.Optional[StorageType] = OMIT,
        template_info: typing.Optional[PrebuildTemplateInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTemplateResult]:
        """
        Parameters
        ----------
        friendly_name : str

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_prebuild_instance_endpoint : typing.Optional[str]

        git_hub_prebuild_template_endpoint : typing.Optional[str]

        plan_id : typing.Optional[str]

        seed : typing.Optional[SeedInfoBody]

        storage_type : typing.Optional[StorageType]

        template_info : typing.Optional[PrebuildTemplateInfo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTemplateResult]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/prebuilds/templates",
            method="POST",
            json={
                "devContainerPath": dev_container_path,
                "experimentalFeatures": convert_and_respect_annotation_metadata(
                    object_=experimental_features, annotation=ExperimentalFeaturesBody, direction="write"
                ),
                "features": features,
                "friendlyName": friendly_name,
                "gitHubPrebuildInstanceEndpoint": git_hub_prebuild_instance_endpoint,
                "gitHubPrebuildTemplateEndpoint": git_hub_prebuild_template_endpoint,
                "planId": plan_id,
                "seed": convert_and_respect_annotation_metadata(
                    object_=seed, annotation=SeedInfoBody, direction="write"
                ),
                "storageType": storage_type,
                "templateInfo": convert_and_respect_annotation_metadata(
                    object_=template_info, annotation=PrebuildTemplateInfo, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTemplateResult,
                    parse_obj_as(
                        type_=CreateTemplateResult,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_prebuild_readiness_skus_route(
        self,
        repo_id: str,
        branch_name: str,
        prebuild_hash: str,
        location: str,
        dev_container_path: str,
        *,
        storage_type: typing.Optional[StorageType] = None,
        fast_path_enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PrebuildReadinessResult]:
        """
        Parameters
        ----------
        repo_id : str

        branch_name : str

        prebuild_hash : str

        location : str

        dev_container_path : str

        storage_type : typing.Optional[StorageType]

        fast_path_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrebuildReadinessResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/prebuilds/templates/skus/repo/{encode_path_param(repo_id)}/branch/{encode_path_param(branch_name)}/hash/{encode_path_param(prebuild_hash)}/location/{encode_path_param(location)}/devcontainerpath/{encode_path_param(dev_container_path)}",
            method="GET",
            params={
                "storageType": storage_type,
                "fastPathEnabled": fast_path_enabled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrebuildReadinessResult,
                    parse_obj_as(
                        type_=PrebuildReadinessResult,
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

    async def post_api_v2prebuilds_templates_updatemaxversions(
        self,
        *,
        branch_name: str,
        max_prebuild_template_versions: int,
        repo_id: int,
        dev_container_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        branch_name : str

        max_prebuild_template_versions : int

        repo_id : int

        dev_container_path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/prebuilds/templates/updatemaxversions",
            method="POST",
            json={
                "branchName": branch_name,
                "devContainerPath": dev_container_path,
                "maxPrebuildTemplateVersions": max_prebuild_template_versions,
                "repoId": repo_id,
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

    async def post_api_v2prebuilds_templates_template_id_updatestatus(
        self, template_id: str, *, is_success: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        template_id : str

        is_success : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/prebuilds/templates/{encode_path_param(template_id)}/updatestatus",
            method="POST",
            json={
                "isSuccess": is_success,
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
