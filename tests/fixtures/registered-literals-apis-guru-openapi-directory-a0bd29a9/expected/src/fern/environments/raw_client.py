

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.billable_owner_body import BillableOwnerBody
from ..types.cloud_environment_result import CloudEnvironmentResult
from ..types.connection_info_body import ConnectionInfoBody
from ..types.environment_registration_callback_payload_body import EnvironmentRegistrationCallbackPayloadBody
from ..types.experimental_features_body import ExperimentalFeaturesBody
from ..types.failover_details import FailoverDetails
from ..types.identity_body import IdentityBody
from ..types.netmon_correlation_data_body import NetmonCorrelationDataBody
from ..types.personalization_info_body import PersonalizationInfoBody
from ..types.privacy_enum import PrivacyEnum
from ..types.problem_details import ProblemDetails
from ..types.runtime_constraints_body import RuntimeConstraintsBody
from ..types.secret_data_body import SecretDataBody
from ..types.seed_info_body import SeedInfoBody
from ..types.tunnel_type import TunnelType
from ..types.unfiltered_cloud_environment_result import UnfilteredCloudEnvironmentResult
from ..types.vm_logs_upload_info import VmLogsUploadInfo
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEnvironmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_api_v1environments(
        self,
        *,
        name: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CloudEnvironmentResult]]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        plan_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CloudEnvironmentResult]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/Environments",
            method="GET",
            params={
                "name": name,
                "planId": plan_id,
                "deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CloudEnvironmentResult],
                    parse_obj_as(
                        type_=typing.List[CloudEnvironmentResult],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_v1environments(
        self,
        *,
        friendly_name: str,
        type: str,
        access: typing.Optional[bool] = None,
        analytics_tracking_id: typing.Optional[str] = OMIT,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        billable_owner: typing.Optional[BillableOwnerBody] = OMIT,
        connection: typing.Optional[ConnectionInfoBody] = OMIT,
        container_image: typing.Optional[str] = OMIT,
        create_as_prebuild: typing.Optional[bool] = OMIT,
        dev_container_json: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_api_url: typing.Optional[str] = OMIT,
        git_hub_app_url: typing.Optional[str] = OMIT,
        git_hub_pfs_auth_endpoint: typing.Optional[str] = OMIT,
        github_environment_endpoint: typing.Optional[str] = OMIT,
        has_devcontainer_json: typing.Optional[bool] = OMIT,
        identity: typing.Optional[IdentityBody] = OMIT,
        label: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        netmon_correlation_data: typing.Optional[NetmonCorrelationDataBody] = OMIT,
        personalization: typing.Optional[PersonalizationInfoBody] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        runtime_constraints: typing.Optional[RuntimeConstraintsBody] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        test_account: typing.Optional[bool] = OMIT,
        user_tier: typing.Optional[str] = OMIT,
        working_directory: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        friendly_name : str

        type : str

        access : typing.Optional[bool]

        analytics_tracking_id : typing.Optional[str]

        auto_shutdown_delay_minutes : typing.Optional[int]

        billable_owner : typing.Optional[BillableOwnerBody]

        connection : typing.Optional[ConnectionInfoBody]

        container_image : typing.Optional[str]

        create_as_prebuild : typing.Optional[bool]

        dev_container_json : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_api_url : typing.Optional[str]

        git_hub_app_url : typing.Optional[str]

        git_hub_pfs_auth_endpoint : typing.Optional[str]

        github_environment_endpoint : typing.Optional[str]

        has_devcontainer_json : typing.Optional[bool]

        identity : typing.Optional[IdentityBody]

        label : typing.Optional[str]

        location : typing.Optional[str]

        netmon_correlation_data : typing.Optional[NetmonCorrelationDataBody]

        personalization : typing.Optional[PersonalizationInfoBody]

        plan_id : typing.Optional[str]

        platform : typing.Optional[str]

        runtime_constraints : typing.Optional[RuntimeConstraintsBody]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        seed : typing.Optional[SeedInfoBody]

        sku_name : typing.Optional[str]

        test_account : typing.Optional[bool]

        user_tier : typing.Optional[str]

        working_directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/Environments",
            method="POST",
            params={
                "access": access,
            },
            json={
                "analyticsTrackingId": analytics_tracking_id,
                "autoShutdownDelayMinutes": auto_shutdown_delay_minutes,
                "billableOwner": convert_and_respect_annotation_metadata(
                    object_=billable_owner, annotation=BillableOwnerBody, direction="write"
                ),
                "connection": convert_and_respect_annotation_metadata(
                    object_=connection, annotation=ConnectionInfoBody, direction="write"
                ),
                "containerImage": container_image,
                "createAsPrebuild": create_as_prebuild,
                "devContainerJson": dev_container_json,
                "devContainerPath": dev_container_path,
                "experimentalFeatures": convert_and_respect_annotation_metadata(
                    object_=experimental_features, annotation=ExperimentalFeaturesBody, direction="write"
                ),
                "features": features,
                "friendlyName": friendly_name,
                "gitHubApiUrl": git_hub_api_url,
                "gitHubAppUrl": git_hub_app_url,
                "gitHubPfsAuthEndpoint": git_hub_pfs_auth_endpoint,
                "githubEnvironmentEndpoint": github_environment_endpoint,
                "hasDevcontainerJson": has_devcontainer_json,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=IdentityBody, direction="write"
                ),
                "label": label,
                "location": location,
                "netmonCorrelationData": convert_and_respect_annotation_metadata(
                    object_=netmon_correlation_data, annotation=NetmonCorrelationDataBody, direction="write"
                ),
                "personalization": convert_and_respect_annotation_metadata(
                    object_=personalization, annotation=PersonalizationInfoBody, direction="write"
                ),
                "planId": plan_id,
                "platform": platform,
                "runtimeConstraints": convert_and_respect_annotation_metadata(
                    object_=runtime_constraints, annotation=RuntimeConstraintsBody, direction="write"
                ),
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
                "seed": convert_and_respect_annotation_metadata(
                    object_=seed, annotation=SeedInfoBody, direction="write"
                ),
                "skuName": sku_name,
                "testAccount": test_account,
                "type": type,
                "userTier": user_tier,
                "workingDirectory": working_directory,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_environment_route(
        self,
        environment_id: str,
        *,
        connect: typing.Optional[bool] = None,
        pf_connect: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        connect : typing.Optional[bool]

        pf_connect : typing.Optional[bool]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}",
            method="GET",
            params={
                "connect": connect,
                "pfConnect": pf_connect,
                "deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def delete_api_v1environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}",
            method="DELETE",
            request_options=request_options,
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

    def patch_api_v1environments_environment_id(
        self,
        environment_id: str,
        *,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        failover_details: typing.Optional[FailoverDetails] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        plan_access_token: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        auto_shutdown_delay_minutes : typing.Optional[int]

        failover_details : typing.Optional[FailoverDetails]

        friendly_name : typing.Optional[str]

        plan_access_token : typing.Optional[str]

        plan_id : typing.Optional[str]

        sku_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}",
            method="PATCH",
            json={
                "autoShutdownDelayMinutes": auto_shutdown_delay_minutes,
                "failoverDetails": convert_and_respect_annotation_metadata(
                    object_=failover_details, annotation=FailoverDetails, direction="write"
                ),
                "friendlyName": friendly_name,
                "planAccessToken": plan_access_token,
                "planId": plan_id,
                "skuName": sku_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def update_environment_route(
        self,
        environment_id: str,
        *,
        type: str,
        payload: typing.Optional[EnvironmentRegistrationCallbackPayloadBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        type : str

        payload : typing.Optional[EnvironmentRegistrationCallbackPayloadBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/_callback",
            method="POST",
            json={
                "payload": convert_and_respect_annotation_metadata(
                    object_=payload, annotation=EnvironmentRegistrationCallbackPayloadBody, direction="write"
                ),
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def get_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UnfilteredCloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnfilteredCloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/archive",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnfilteredCloudEnvironmentResult,
                    parse_obj_as(
                        type_=UnfilteredCloudEnvironmentResult,
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

    def post_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/archive",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def post_api_v1environments_environment_id_export(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/export",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def patch_api_v1environments_environment_id_folder(
        self,
        environment_id: str,
        *,
        recent_folder_paths: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        recent_folder_paths : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/folder",
            method="PATCH",
            json={
                "recentFolderPaths": recent_folder_paths,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def get_api_v1environments_environment_id_heartbeattoken(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/heartbeattoken",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def post_api_v1environments_environment_id_notify(
        self,
        environment_id: str,
        *,
        details: typing.Optional[str] = OMIT,
        display_mode: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        modal: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        environment_id : str

        details : typing.Optional[str]

        display_mode : typing.Optional[str]

        message : typing.Optional[str]

        modal : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/notify",
            method="POST",
            json={
                "details": details,
                "displayMode": display_mode,
                "message": message,
                "modal": modal,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_api_v1environments_environment_id_ports_port(
        self,
        environment_id: str,
        port: int,
        *,
        privacy: typing.Optional[PrivacyEnum] = OMIT,
        tunnel_type: typing.Optional[TunnelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        port : int

        privacy : typing.Optional[PrivacyEnum]

        tunnel_type : typing.Optional[TunnelType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/ports/{encode_path_param(port)}",
            method="PUT",
            json={
                "privacy": privacy,
                "tunnelType": tunnel_type,
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

    def delete_api_v1environments_environment_id_ports_port(
        self, environment_id: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/ports/{encode_path_param(port)}",
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

    def patch_api_v1environments_environment_id_restore(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/restore",
            method="PATCH",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_api_v1environments_environment_id_secrets(
        self,
        environment_id: str,
        *,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            No Content
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/secrets",
            method="PUT",
            json={
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def post_api_v1environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/shutdown",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_v1environments_environment_id_start(
        self,
        environment_id: str,
        *,
        access: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        access : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/start",
            method="POST",
            params={
                "access": access,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def get_api_v1environments_environment_id_state(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def get_api_v1environments_environment_id_updates(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/updates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    def get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
        self,
        environment_id_or_friendly_name: str,
        target_blob: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        environment_id_or_friendly_name : str

        target_blob : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/storage/{encode_path_param(environment_id_or_friendly_name)}/{encode_path_param(target_blob)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def get_api_v1geneva_actions_environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def delete_api_v1geneva_actions_environments_environment_id(
        self,
        environment_id: str,
        *,
        deletion_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        deletion_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}",
            method="DELETE",
            params={
                "deletionType": deletion_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def put_api_v1geneva_actions_environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}/archive",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def put_api_v1geneva_actions_environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}/shutdown",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VmLogsUploadInfo]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VmLogsUploadInfo]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}/upload/running/vm/logs",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmLogsUploadInfo,
                    parse_obj_as(
                        type_=VmLogsUploadInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawEnvironmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_api_v1environments(
        self,
        *,
        name: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CloudEnvironmentResult]]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        plan_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CloudEnvironmentResult]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/Environments",
            method="GET",
            params={
                "name": name,
                "planId": plan_id,
                "deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CloudEnvironmentResult],
                    parse_obj_as(
                        type_=typing.List[CloudEnvironmentResult],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_v1environments(
        self,
        *,
        friendly_name: str,
        type: str,
        access: typing.Optional[bool] = None,
        analytics_tracking_id: typing.Optional[str] = OMIT,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        billable_owner: typing.Optional[BillableOwnerBody] = OMIT,
        connection: typing.Optional[ConnectionInfoBody] = OMIT,
        container_image: typing.Optional[str] = OMIT,
        create_as_prebuild: typing.Optional[bool] = OMIT,
        dev_container_json: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_api_url: typing.Optional[str] = OMIT,
        git_hub_app_url: typing.Optional[str] = OMIT,
        git_hub_pfs_auth_endpoint: typing.Optional[str] = OMIT,
        github_environment_endpoint: typing.Optional[str] = OMIT,
        has_devcontainer_json: typing.Optional[bool] = OMIT,
        identity: typing.Optional[IdentityBody] = OMIT,
        label: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        netmon_correlation_data: typing.Optional[NetmonCorrelationDataBody] = OMIT,
        personalization: typing.Optional[PersonalizationInfoBody] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        runtime_constraints: typing.Optional[RuntimeConstraintsBody] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        test_account: typing.Optional[bool] = OMIT,
        user_tier: typing.Optional[str] = OMIT,
        working_directory: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        friendly_name : str

        type : str

        access : typing.Optional[bool]

        analytics_tracking_id : typing.Optional[str]

        auto_shutdown_delay_minutes : typing.Optional[int]

        billable_owner : typing.Optional[BillableOwnerBody]

        connection : typing.Optional[ConnectionInfoBody]

        container_image : typing.Optional[str]

        create_as_prebuild : typing.Optional[bool]

        dev_container_json : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_api_url : typing.Optional[str]

        git_hub_app_url : typing.Optional[str]

        git_hub_pfs_auth_endpoint : typing.Optional[str]

        github_environment_endpoint : typing.Optional[str]

        has_devcontainer_json : typing.Optional[bool]

        identity : typing.Optional[IdentityBody]

        label : typing.Optional[str]

        location : typing.Optional[str]

        netmon_correlation_data : typing.Optional[NetmonCorrelationDataBody]

        personalization : typing.Optional[PersonalizationInfoBody]

        plan_id : typing.Optional[str]

        platform : typing.Optional[str]

        runtime_constraints : typing.Optional[RuntimeConstraintsBody]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        seed : typing.Optional[SeedInfoBody]

        sku_name : typing.Optional[str]

        test_account : typing.Optional[bool]

        user_tier : typing.Optional[str]

        working_directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/Environments",
            method="POST",
            params={
                "access": access,
            },
            json={
                "analyticsTrackingId": analytics_tracking_id,
                "autoShutdownDelayMinutes": auto_shutdown_delay_minutes,
                "billableOwner": convert_and_respect_annotation_metadata(
                    object_=billable_owner, annotation=BillableOwnerBody, direction="write"
                ),
                "connection": convert_and_respect_annotation_metadata(
                    object_=connection, annotation=ConnectionInfoBody, direction="write"
                ),
                "containerImage": container_image,
                "createAsPrebuild": create_as_prebuild,
                "devContainerJson": dev_container_json,
                "devContainerPath": dev_container_path,
                "experimentalFeatures": convert_and_respect_annotation_metadata(
                    object_=experimental_features, annotation=ExperimentalFeaturesBody, direction="write"
                ),
                "features": features,
                "friendlyName": friendly_name,
                "gitHubApiUrl": git_hub_api_url,
                "gitHubAppUrl": git_hub_app_url,
                "gitHubPfsAuthEndpoint": git_hub_pfs_auth_endpoint,
                "githubEnvironmentEndpoint": github_environment_endpoint,
                "hasDevcontainerJson": has_devcontainer_json,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=IdentityBody, direction="write"
                ),
                "label": label,
                "location": location,
                "netmonCorrelationData": convert_and_respect_annotation_metadata(
                    object_=netmon_correlation_data, annotation=NetmonCorrelationDataBody, direction="write"
                ),
                "personalization": convert_and_respect_annotation_metadata(
                    object_=personalization, annotation=PersonalizationInfoBody, direction="write"
                ),
                "planId": plan_id,
                "platform": platform,
                "runtimeConstraints": convert_and_respect_annotation_metadata(
                    object_=runtime_constraints, annotation=RuntimeConstraintsBody, direction="write"
                ),
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
                "seed": convert_and_respect_annotation_metadata(
                    object_=seed, annotation=SeedInfoBody, direction="write"
                ),
                "skuName": sku_name,
                "testAccount": test_account,
                "type": type,
                "userTier": user_tier,
                "workingDirectory": working_directory,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_environment_route(
        self,
        environment_id: str,
        *,
        connect: typing.Optional[bool] = None,
        pf_connect: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        connect : typing.Optional[bool]

        pf_connect : typing.Optional[bool]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}",
            method="GET",
            params={
                "connect": connect,
                "pfConnect": pf_connect,
                "deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def delete_api_v1environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def patch_api_v1environments_environment_id(
        self,
        environment_id: str,
        *,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        failover_details: typing.Optional[FailoverDetails] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        plan_access_token: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        auto_shutdown_delay_minutes : typing.Optional[int]

        failover_details : typing.Optional[FailoverDetails]

        friendly_name : typing.Optional[str]

        plan_access_token : typing.Optional[str]

        plan_id : typing.Optional[str]

        sku_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}",
            method="PATCH",
            json={
                "autoShutdownDelayMinutes": auto_shutdown_delay_minutes,
                "failoverDetails": convert_and_respect_annotation_metadata(
                    object_=failover_details, annotation=FailoverDetails, direction="write"
                ),
                "friendlyName": friendly_name,
                "planAccessToken": plan_access_token,
                "planId": plan_id,
                "skuName": sku_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def update_environment_route(
        self,
        environment_id: str,
        *,
        type: str,
        payload: typing.Optional[EnvironmentRegistrationCallbackPayloadBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        type : str

        payload : typing.Optional[EnvironmentRegistrationCallbackPayloadBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/_callback",
            method="POST",
            json={
                "payload": convert_and_respect_annotation_metadata(
                    object_=payload, annotation=EnvironmentRegistrationCallbackPayloadBody, direction="write"
                ),
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def get_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UnfilteredCloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnfilteredCloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/archive",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnfilteredCloudEnvironmentResult,
                    parse_obj_as(
                        type_=UnfilteredCloudEnvironmentResult,
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

    async def post_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/archive",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def post_api_v1environments_environment_id_export(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/export",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def patch_api_v1environments_environment_id_folder(
        self,
        environment_id: str,
        *,
        recent_folder_paths: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        recent_folder_paths : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/folder",
            method="PATCH",
            json={
                "recentFolderPaths": recent_folder_paths,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def get_api_v1environments_environment_id_heartbeattoken(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/heartbeattoken",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def post_api_v1environments_environment_id_notify(
        self,
        environment_id: str,
        *,
        details: typing.Optional[str] = OMIT,
        display_mode: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        modal: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        environment_id : str

        details : typing.Optional[str]

        display_mode : typing.Optional[str]

        message : typing.Optional[str]

        modal : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/notify",
            method="POST",
            json={
                "details": details,
                "displayMode": display_mode,
                "message": message,
                "modal": modal,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_api_v1environments_environment_id_ports_port(
        self,
        environment_id: str,
        port: int,
        *,
        privacy: typing.Optional[PrivacyEnum] = OMIT,
        tunnel_type: typing.Optional[TunnelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        port : int

        privacy : typing.Optional[PrivacyEnum]

        tunnel_type : typing.Optional[TunnelType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/ports/{encode_path_param(port)}",
            method="PUT",
            json={
                "privacy": privacy,
                "tunnelType": tunnel_type,
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

    async def delete_api_v1environments_environment_id_ports_port(
        self, environment_id: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/ports/{encode_path_param(port)}",
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

    async def patch_api_v1environments_environment_id_restore(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/restore",
            method="PATCH",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_api_v1environments_environment_id_secrets(
        self,
        environment_id: str,
        *,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            No Content
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/secrets",
            method="PUT",
            json={
                "secrets": convert_and_respect_annotation_metadata(
                    object_=secrets, annotation=typing.Optional[typing.Sequence[SecretDataBody]], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def post_api_v1environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/shutdown",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_v1environments_environment_id_start(
        self,
        environment_id: str,
        *,
        access: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        access : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/start",
            method="POST",
            params={
                "access": access,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def get_api_v1environments_environment_id_state(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def get_api_v1environments_environment_id_updates(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Environments/{encode_path_param(environment_id)}/updates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
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

    async def get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
        self,
        environment_id_or_friendly_name: str,
        target_blob: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        environment_id_or_friendly_name : str

        target_blob : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/storage/{encode_path_param(environment_id_or_friendly_name)}/{encode_path_param(target_blob)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def get_api_v1geneva_actions_environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def delete_api_v1geneva_actions_environments_environment_id(
        self,
        environment_id: str,
        *,
        deletion_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        environment_id : str

        deletion_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}",
            method="DELETE",
            params={
                "deletionType": deletion_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def put_api_v1geneva_actions_environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}/archive",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def put_api_v1geneva_actions_environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudEnvironmentResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}/shutdown",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudEnvironmentResult,
                    parse_obj_as(
                        type_=CloudEnvironmentResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VmLogsUploadInfo]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VmLogsUploadInfo]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Environments/{encode_path_param(environment_id)}/upload/running/vm/logs",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmLogsUploadInfo,
                    parse_obj_as(
                        type_=VmLogsUploadInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
