

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
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bad_gateway_error_body import BadGatewayErrorBody
from ..types.internal_dispatch_schedules_response import InternalDispatchSchedulesResponse
from .types.post_internal_identity_linking_resolve_principal_credential_response import (
    PostInternalIdentityLinkingResolvePrincipalCredentialResponse,
)
from .types.post_internal_identity_linking_sign_commit_payload_request_encoding import (
    PostInternalIdentityLinkingSignCommitPayloadRequestEncoding,
)
from .types.post_internal_identity_linking_sign_commit_payload_request_format import (
    PostInternalIdentityLinkingSignCommitPayloadRequestFormat,
)
from .types.post_internal_identity_linking_sign_commit_payload_response import (
    PostInternalIdentityLinkingSignCommitPayloadResponse,
)
from .types.post_internal_integration_connections_refresh_resource_response import (
    PostInternalIntegrationConnectionsRefreshResourceResponse,
)
from .types.post_internal_integration_credentials_resolve_response import (
    PostInternalIntegrationCredentialsResolveResponse,
)
from .types.post_internal_integration_credentials_resolve_target_secrets_request_targets_item import (
    PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem,
)
from .types.post_internal_integration_credentials_resolve_target_secrets_response import (
    PostInternalIntegrationCredentialsResolveTargetSecretsResponse,
)
from .types.post_internal_provider_resource_associations_register_response import (
    PostInternalProviderResourceAssociationsRegisterResponse,
)
from .types.post_internal_sandbox_runtime_compile_plan_request_image import (
    PostInternalSandboxRuntimeCompilePlanRequestImage,
)
from .types.post_internal_sandbox_runtime_compile_plan_request_snapshot_preparation_script_kind import (
    PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind,
)
from .types.post_internal_sandbox_runtime_compile_plan_response import PostInternalSandboxRuntimeCompilePlanResponse
from .types.post_internal_sandbox_runtime_get_sandbox_instance_response import (
    PostInternalSandboxRuntimeGetSandboxInstanceResponse,
)
from .types.post_internal_sandbox_runtime_mint_connection_token_response import (
    PostInternalSandboxRuntimeMintConnectionTokenResponse,
)
from .types.post_internal_sandbox_runtime_resolve_credentials_request_provider import (
    PostInternalSandboxRuntimeResolveCredentialsRequestProvider,
)
from .types.post_internal_sandbox_runtime_resolve_credentials_response import (
    PostInternalSandboxRuntimeResolveCredentialsResponse,
)
from .types.post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_request_transport import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport,
)
from .types.post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse,
)
from .types.post_internal_sandbox_runtime_resume_sandbox_instance_response import (
    PostInternalSandboxRuntimeResumeSandboxInstanceResponse,
)
from .types.post_internal_sandbox_runtime_start_profile_instance_request_acting_user import (
    PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser,
)
from .types.post_internal_sandbox_runtime_start_profile_instance_request_source import (
    PostInternalSandboxRuntimeStartProfileInstanceRequestSource,
)
from .types.post_internal_sandbox_runtime_start_profile_instance_request_started_by import (
    PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy,
)
from .types.post_internal_sandbox_runtime_start_profile_instance_response import (
    PostInternalSandboxRuntimeStartProfileInstanceResponse,
)
from .types.post_internal_snapshot_jobs_job_id_claim_response import PostInternalSnapshotJobsJobIdClaimResponse
from .types.post_internal_snapshot_jobs_job_id_fail_response import PostInternalSnapshotJobsJobIdFailResponse
from .types.post_internal_snapshot_jobs_job_id_succeed_request_image import (
    PostInternalSnapshotJobsJobIdSucceedRequestImage,
)
from .types.post_internal_snapshot_jobs_job_id_succeed_response import PostInternalSnapshotJobsJobIdSucceedResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_internal_integration_connections_refresh_resource(
        self,
        *,
        organization_id: str,
        connection_id: str,
        kind: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalIntegrationConnectionsRefreshResourceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        connection_id : str

        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalIntegrationConnectionsRefreshResourceResponse]
            Request integration connection resource refresh for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/integration-connections/refresh-resource",
            method="POST",
            json={
                "organizationId": organization_id,
                "connectionId": connection_id,
                "kind": kind,
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
                    PostInternalIntegrationConnectionsRefreshResourceResponse,
                    parse_obj_as(
                        type_=PostInternalIntegrationConnectionsRefreshResourceResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_integration_credentials_resolve(
        self,
        *,
        connection_id: str,
        secret_type: str,
        binding_id: typing.Optional[str] = OMIT,
        force_refresh: typing.Optional[bool] = OMIT,
        slot_key: typing.Optional[str] = OMIT,
        resolver_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalIntegrationCredentialsResolveResponse]:
        """
        Parameters
        ----------
        connection_id : str

        secret_type : str

        binding_id : typing.Optional[str]

        force_refresh : typing.Optional[bool]

        slot_key : typing.Optional[str]

        resolver_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalIntegrationCredentialsResolveResponse]
            Resolve integration credential for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/integration-credentials/resolve",
            method="POST",
            json={
                "connectionId": connection_id,
                "bindingId": binding_id,
                "forceRefresh": force_refresh,
                "secretType": secret_type,
                "slotKey": slot_key,
                "resolverKey": resolver_key,
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
                    PostInternalIntegrationCredentialsResolveResponse,
                    parse_obj_as(
                        type_=PostInternalIntegrationCredentialsResolveResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    def post_internal_integration_credentials_resolve_target_secrets(
        self,
        *,
        targets: typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalIntegrationCredentialsResolveTargetSecretsResponse]:
        """
        Parameters
        ----------
        targets : typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalIntegrationCredentialsResolveTargetSecretsResponse]
            Resolve integration target secrets for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/integration-credentials/resolve-target-secrets",
            method="POST",
            json={
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets,
                    annotation=typing.Sequence[
                        PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem
                    ],
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
                    PostInternalIntegrationCredentialsResolveTargetSecretsResponse,
                    parse_obj_as(
                        type_=PostInternalIntegrationCredentialsResolveTargetSecretsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_identity_linking_resolve_principal_credential(
        self,
        *,
        organization_id: str,
        acting_user_id: str,
        provider_family: str,
        integration_connection_id: typing.Optional[str] = OMIT,
        credential_kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalIdentityLinkingResolvePrincipalCredentialResponse]:
        """
        Parameters
        ----------
        organization_id : str

        acting_user_id : str

        provider_family : str

        integration_connection_id : typing.Optional[str]

        credential_kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalIdentityLinkingResolvePrincipalCredentialResponse]
            Resolve linked-principal credential for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/identity-linking/resolve-principal-credential",
            method="POST",
            json={
                "organizationId": organization_id,
                "actingUserId": acting_user_id,
                "providerFamily": provider_family,
                "integrationConnectionId": integration_connection_id,
                "credentialKind": credential_kind,
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
                    PostInternalIdentityLinkingResolvePrincipalCredentialResponse,
                    parse_obj_as(
                        type_=PostInternalIdentityLinkingResolvePrincipalCredentialResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_identity_linking_sign_commit_payload(
        self,
        *,
        organization_id: str,
        sandbox_instance_id: str,
        acting_user_id: str,
        provider_family: str,
        integration_connection_id: str,
        format: PostInternalIdentityLinkingSignCommitPayloadRequestFormat,
        key_ref: str,
        grant: str,
        payload: str,
        encoding: PostInternalIdentityLinkingSignCommitPayloadRequestEncoding,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalIdentityLinkingSignCommitPayloadResponse]:
        """
        Parameters
        ----------
        organization_id : str

        sandbox_instance_id : str

        acting_user_id : str

        provider_family : str

        integration_connection_id : str

        format : PostInternalIdentityLinkingSignCommitPayloadRequestFormat

        key_ref : str

        grant : str

        payload : str

        encoding : PostInternalIdentityLinkingSignCommitPayloadRequestEncoding

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalIdentityLinkingSignCommitPayloadResponse]
            Sign a Git commit payload for a linked-principal credential.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/identity-linking/sign-commit-payload",
            method="POST",
            json={
                "organizationId": organization_id,
                "sandboxInstanceId": sandbox_instance_id,
                "actingUserId": acting_user_id,
                "providerFamily": provider_family,
                "integrationConnectionId": integration_connection_id,
                "format": format,
                "keyRef": key_ref,
                "grant": grant,
                "payload": payload,
                "encoding": encoding,
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
                    PostInternalIdentityLinkingSignCommitPayloadResponse,
                    parse_obj_as(
                        type_=PostInternalIdentityLinkingSignCommitPayloadResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_provider_resource_associations_register(
        self,
        *,
        integration_connection_id: str,
        resource_kind: str,
        provider_resource_id: str,
        sandbox_instance_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalProviderResourceAssociationsRegisterResponse]:
        """
        Parameters
        ----------
        integration_connection_id : str

        resource_kind : str

        provider_resource_id : str

        sandbox_instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalProviderResourceAssociationsRegisterResponse]
            Register a provider resource association for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/provider-resource-associations/register",
            method="POST",
            json={
                "integrationConnectionId": integration_connection_id,
                "resourceKind": resource_kind,
                "providerResourceId": provider_resource_id,
                "sandboxInstanceId": sandbox_instance_id,
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
                    PostInternalProviderResourceAssociationsRegisterResponse,
                    parse_obj_as(
                        type_=PostInternalProviderResourceAssociationsRegisterResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_schedules_dispatch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InternalDispatchSchedulesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InternalDispatchSchedulesResponse]
            Enqueue scheduled workflow dispatch for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/schedules/dispatch",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InternalDispatchSchedulesResponse,
                    parse_obj_as(
                        type_=InternalDispatchSchedulesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_snapshot_jobs_job_id_claim(
        self, job_id: str, *, workflow_run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostInternalSnapshotJobsJobIdClaimResponse]:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSnapshotJobsJobIdClaimResponse]
            Claim a queued snapshot job for workflow execution.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"internal/snapshot-jobs/{encode_path_param(job_id)}/claim",
            method="POST",
            json={
                "workflowRunId": workflow_run_id,
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
                    PostInternalSnapshotJobsJobIdClaimResponse,
                    parse_obj_as(
                        type_=PostInternalSnapshotJobsJobIdClaimResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_snapshot_jobs_job_id_succeed(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        image: PostInternalSnapshotJobsJobIdSucceedRequestImage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSnapshotJobsJobIdSucceedResponse]:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        image : PostInternalSnapshotJobsJobIdSucceedRequestImage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSnapshotJobsJobIdSucceedResponse]
            Mark a running snapshot job succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"internal/snapshot-jobs/{encode_path_param(job_id)}/succeed",
            method="POST",
            json={
                "workflowRunId": workflow_run_id,
                "image": convert_and_respect_annotation_metadata(
                    object_=image, annotation=PostInternalSnapshotJobsJobIdSucceedRequestImage, direction="write"
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
                    PostInternalSnapshotJobsJobIdSucceedResponse,
                    parse_obj_as(
                        type_=PostInternalSnapshotJobsJobIdSucceedResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_snapshot_jobs_job_id_fail(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        error_code: str,
        error_message: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSnapshotJobsJobIdFailResponse]:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        error_code : str

        error_message : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSnapshotJobsJobIdFailResponse]
            Mark a running snapshot job failed.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"internal/snapshot-jobs/{encode_path_param(job_id)}/fail",
            method="POST",
            json={
                "workflowRunId": workflow_run_id,
                "errorCode": error_code,
                "errorMessage": error_message,
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
                    PostInternalSnapshotJobsJobIdFailResponse,
                    parse_obj_as(
                        type_=PostInternalSnapshotJobsJobIdFailResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_sandbox_runtime_compile_plan(
        self,
        *,
        organization_id: str,
        profile_id: str,
        profile_version: int,
        image: PostInternalSandboxRuntimeCompilePlanRequestImage,
        snapshot_preparation_script_kind: typing.Optional[
            PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSandboxRuntimeCompilePlanResponse]:
        """
        Parameters
        ----------
        organization_id : str

        profile_id : str

        profile_version : int

        image : PostInternalSandboxRuntimeCompilePlanRequestImage

        snapshot_preparation_script_kind : typing.Optional[PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSandboxRuntimeCompilePlanResponse]
            Compile a sandbox profile version runtime plan for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/compile-plan",
            method="POST",
            json={
                "organizationId": organization_id,
                "profileId": profile_id,
                "profileVersion": profile_version,
                "snapshotPreparationScriptKind": snapshot_preparation_script_kind,
                "image": convert_and_respect_annotation_metadata(
                    object_=image, annotation=PostInternalSandboxRuntimeCompilePlanRequestImage, direction="write"
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
                    PostInternalSandboxRuntimeCompilePlanResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeCompilePlanResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_sandbox_runtime_start_profile_instance(
        self,
        *,
        organization_id: str,
        profile_id: str,
        profile_version: int,
        started_by: PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy,
        source: PostInternalSandboxRuntimeStartProfileInstanceRequestSource,
        primary_repository_id: typing.Optional[str] = OMIT,
        acting_user: typing.Optional[PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSandboxRuntimeStartProfileInstanceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        profile_id : str

        profile_version : int

        started_by : PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy

        source : PostInternalSandboxRuntimeStartProfileInstanceRequestSource

        primary_repository_id : typing.Optional[str]

        acting_user : typing.Optional[PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSandboxRuntimeStartProfileInstanceResponse]
            Start sandbox profile instance provisioning for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/start-profile-instance",
            method="POST",
            json={
                "organizationId": organization_id,
                "profileId": profile_id,
                "profileVersion": profile_version,
                "primaryRepositoryId": primary_repository_id,
                "startedBy": convert_and_respect_annotation_metadata(
                    object_=started_by,
                    annotation=PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy,
                    direction="write",
                ),
                "actingUser": convert_and_respect_annotation_metadata(
                    object_=acting_user,
                    annotation=PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser,
                    direction="write",
                ),
                "source": convert_and_respect_annotation_metadata(
                    object_=source,
                    annotation=PostInternalSandboxRuntimeStartProfileInstanceRequestSource,
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
                    PostInternalSandboxRuntimeStartProfileInstanceResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeStartProfileInstanceResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_sandbox_runtime_get_sandbox_instance(
        self, *, organization_id: str, instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostInternalSandboxRuntimeGetSandboxInstanceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSandboxRuntimeGetSandboxInstanceResponse]
            Get sandbox instance status for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/get-sandbox-instance",
            method="POST",
            json={
                "organizationId": organization_id,
                "instanceId": instance_id,
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
                    PostInternalSandboxRuntimeGetSandboxInstanceResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeGetSandboxInstanceResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_sandbox_runtime_resume_sandbox_instance(
        self,
        *,
        organization_id: str,
        instance_id: str,
        acting_user_id: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSandboxRuntimeResumeSandboxInstanceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        acting_user_id : typing.Optional[str]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSandboxRuntimeResumeSandboxInstanceResponse]
            Queue sandbox instance resume for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/resume-sandbox-instance",
            method="POST",
            json={
                "organizationId": organization_id,
                "instanceId": instance_id,
                "actingUserId": acting_user_id,
                "idempotencyKey": idempotency_key,
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
                    PostInternalSandboxRuntimeResumeSandboxInstanceResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeResumeSandboxInstanceResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_sandbox_runtime_mint_connection_token(
        self,
        *,
        organization_id: str,
        instance_id: str,
        acting_user_id: typing.Optional[str] = OMIT,
        webhook_event_id: typing.Optional[str] = OMIT,
        delivery_task_id: typing.Optional[str] = OMIT,
        external_delivery_id: typing.Optional[str] = OMIT,
        trigger_run_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSandboxRuntimeMintConnectionTokenResponse]:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        acting_user_id : typing.Optional[str]

        webhook_event_id : typing.Optional[str]

        delivery_task_id : typing.Optional[str]

        external_delivery_id : typing.Optional[str]

        trigger_run_id : typing.Optional[str]

        conversation_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSandboxRuntimeMintConnectionTokenResponse]
            Mint a sandbox connection token for internal callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/mint-connection-token",
            method="POST",
            json={
                "organizationId": organization_id,
                "instanceId": instance_id,
                "actingUserId": acting_user_id,
                "webhookEventId": webhook_event_id,
                "deliveryTaskId": delivery_task_id,
                "externalDeliveryId": external_delivery_id,
                "triggerRunId": trigger_run_id,
                "conversationId": conversation_id,
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
                    PostInternalSandboxRuntimeMintConnectionTokenResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeMintConnectionTokenResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_sandbox_runtime_resolve_credentials(
        self,
        *,
        organization_id: str,
        provider: PostInternalSandboxRuntimeResolveCredentialsRequestProvider,
        connection_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSandboxRuntimeResolveCredentialsResponse]:
        """
        Parameters
        ----------
        organization_id : str

        provider : PostInternalSandboxRuntimeResolveCredentialsRequestProvider

        connection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSandboxRuntimeResolveCredentialsResponse]
            Resolve sandbox provider credentials for internal data-plane callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/resolve-credentials",
            method="POST",
            json={
                "organizationId": organization_id,
                "provider": provider,
                "connectionId": connection_id,
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
                    PostInternalSandboxRuntimeResolveCredentialsResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeResolveCredentialsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_internal_sandbox_runtime_resolve_designer_runtime_egress_route(
        self,
        *,
        organization_id: str,
        sandbox_instance_id: str,
        integration_connection_id: str,
        provider_tool_ids: typing.Sequence[str],
        target_url: str,
        method: str,
        transport: PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse]:
        """
        Parameters
        ----------
        organization_id : str

        sandbox_instance_id : str

        integration_connection_id : str

        provider_tool_ids : typing.Sequence[str]

        target_url : str

        method : str

        transport : PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse]
            Resolve a Designer runtime provider egress route for internal gateway callers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/resolve-designer-runtime-egress-route",
            method="POST",
            json={
                "organizationId": organization_id,
                "sandboxInstanceId": sandbox_instance_id,
                "integrationConnectionId": integration_connection_id,
                "providerToolIds": provider_tool_ids,
                "targetUrl": target_url,
                "method": method,
                "transport": transport,
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
                    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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


class AsyncRawInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_internal_integration_connections_refresh_resource(
        self,
        *,
        organization_id: str,
        connection_id: str,
        kind: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalIntegrationConnectionsRefreshResourceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        connection_id : str

        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalIntegrationConnectionsRefreshResourceResponse]
            Request integration connection resource refresh for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/integration-connections/refresh-resource",
            method="POST",
            json={
                "organizationId": organization_id,
                "connectionId": connection_id,
                "kind": kind,
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
                    PostInternalIntegrationConnectionsRefreshResourceResponse,
                    parse_obj_as(
                        type_=PostInternalIntegrationConnectionsRefreshResourceResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_integration_credentials_resolve(
        self,
        *,
        connection_id: str,
        secret_type: str,
        binding_id: typing.Optional[str] = OMIT,
        force_refresh: typing.Optional[bool] = OMIT,
        slot_key: typing.Optional[str] = OMIT,
        resolver_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalIntegrationCredentialsResolveResponse]:
        """
        Parameters
        ----------
        connection_id : str

        secret_type : str

        binding_id : typing.Optional[str]

        force_refresh : typing.Optional[bool]

        slot_key : typing.Optional[str]

        resolver_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalIntegrationCredentialsResolveResponse]
            Resolve integration credential for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/integration-credentials/resolve",
            method="POST",
            json={
                "connectionId": connection_id,
                "bindingId": binding_id,
                "forceRefresh": force_refresh,
                "secretType": secret_type,
                "slotKey": slot_key,
                "resolverKey": resolver_key,
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
                    PostInternalIntegrationCredentialsResolveResponse,
                    parse_obj_as(
                        type_=PostInternalIntegrationCredentialsResolveResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    async def post_internal_integration_credentials_resolve_target_secrets(
        self,
        *,
        targets: typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalIntegrationCredentialsResolveTargetSecretsResponse]:
        """
        Parameters
        ----------
        targets : typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalIntegrationCredentialsResolveTargetSecretsResponse]
            Resolve integration target secrets for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/integration-credentials/resolve-target-secrets",
            method="POST",
            json={
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets,
                    annotation=typing.Sequence[
                        PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem
                    ],
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
                    PostInternalIntegrationCredentialsResolveTargetSecretsResponse,
                    parse_obj_as(
                        type_=PostInternalIntegrationCredentialsResolveTargetSecretsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_identity_linking_resolve_principal_credential(
        self,
        *,
        organization_id: str,
        acting_user_id: str,
        provider_family: str,
        integration_connection_id: typing.Optional[str] = OMIT,
        credential_kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalIdentityLinkingResolvePrincipalCredentialResponse]:
        """
        Parameters
        ----------
        organization_id : str

        acting_user_id : str

        provider_family : str

        integration_connection_id : typing.Optional[str]

        credential_kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalIdentityLinkingResolvePrincipalCredentialResponse]
            Resolve linked-principal credential for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/identity-linking/resolve-principal-credential",
            method="POST",
            json={
                "organizationId": organization_id,
                "actingUserId": acting_user_id,
                "providerFamily": provider_family,
                "integrationConnectionId": integration_connection_id,
                "credentialKind": credential_kind,
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
                    PostInternalIdentityLinkingResolvePrincipalCredentialResponse,
                    parse_obj_as(
                        type_=PostInternalIdentityLinkingResolvePrincipalCredentialResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_identity_linking_sign_commit_payload(
        self,
        *,
        organization_id: str,
        sandbox_instance_id: str,
        acting_user_id: str,
        provider_family: str,
        integration_connection_id: str,
        format: PostInternalIdentityLinkingSignCommitPayloadRequestFormat,
        key_ref: str,
        grant: str,
        payload: str,
        encoding: PostInternalIdentityLinkingSignCommitPayloadRequestEncoding,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalIdentityLinkingSignCommitPayloadResponse]:
        """
        Parameters
        ----------
        organization_id : str

        sandbox_instance_id : str

        acting_user_id : str

        provider_family : str

        integration_connection_id : str

        format : PostInternalIdentityLinkingSignCommitPayloadRequestFormat

        key_ref : str

        grant : str

        payload : str

        encoding : PostInternalIdentityLinkingSignCommitPayloadRequestEncoding

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalIdentityLinkingSignCommitPayloadResponse]
            Sign a Git commit payload for a linked-principal credential.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/identity-linking/sign-commit-payload",
            method="POST",
            json={
                "organizationId": organization_id,
                "sandboxInstanceId": sandbox_instance_id,
                "actingUserId": acting_user_id,
                "providerFamily": provider_family,
                "integrationConnectionId": integration_connection_id,
                "format": format,
                "keyRef": key_ref,
                "grant": grant,
                "payload": payload,
                "encoding": encoding,
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
                    PostInternalIdentityLinkingSignCommitPayloadResponse,
                    parse_obj_as(
                        type_=PostInternalIdentityLinkingSignCommitPayloadResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_provider_resource_associations_register(
        self,
        *,
        integration_connection_id: str,
        resource_kind: str,
        provider_resource_id: str,
        sandbox_instance_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalProviderResourceAssociationsRegisterResponse]:
        """
        Parameters
        ----------
        integration_connection_id : str

        resource_kind : str

        provider_resource_id : str

        sandbox_instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalProviderResourceAssociationsRegisterResponse]
            Register a provider resource association for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/provider-resource-associations/register",
            method="POST",
            json={
                "integrationConnectionId": integration_connection_id,
                "resourceKind": resource_kind,
                "providerResourceId": provider_resource_id,
                "sandboxInstanceId": sandbox_instance_id,
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
                    PostInternalProviderResourceAssociationsRegisterResponse,
                    parse_obj_as(
                        type_=PostInternalProviderResourceAssociationsRegisterResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_schedules_dispatch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InternalDispatchSchedulesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InternalDispatchSchedulesResponse]
            Enqueue scheduled workflow dispatch for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/schedules/dispatch",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InternalDispatchSchedulesResponse,
                    parse_obj_as(
                        type_=InternalDispatchSchedulesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_snapshot_jobs_job_id_claim(
        self, job_id: str, *, workflow_run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostInternalSnapshotJobsJobIdClaimResponse]:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSnapshotJobsJobIdClaimResponse]
            Claim a queued snapshot job for workflow execution.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"internal/snapshot-jobs/{encode_path_param(job_id)}/claim",
            method="POST",
            json={
                "workflowRunId": workflow_run_id,
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
                    PostInternalSnapshotJobsJobIdClaimResponse,
                    parse_obj_as(
                        type_=PostInternalSnapshotJobsJobIdClaimResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_snapshot_jobs_job_id_succeed(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        image: PostInternalSnapshotJobsJobIdSucceedRequestImage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSnapshotJobsJobIdSucceedResponse]:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        image : PostInternalSnapshotJobsJobIdSucceedRequestImage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSnapshotJobsJobIdSucceedResponse]
            Mark a running snapshot job succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"internal/snapshot-jobs/{encode_path_param(job_id)}/succeed",
            method="POST",
            json={
                "workflowRunId": workflow_run_id,
                "image": convert_and_respect_annotation_metadata(
                    object_=image, annotation=PostInternalSnapshotJobsJobIdSucceedRequestImage, direction="write"
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
                    PostInternalSnapshotJobsJobIdSucceedResponse,
                    parse_obj_as(
                        type_=PostInternalSnapshotJobsJobIdSucceedResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_snapshot_jobs_job_id_fail(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        error_code: str,
        error_message: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSnapshotJobsJobIdFailResponse]:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        error_code : str

        error_message : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSnapshotJobsJobIdFailResponse]
            Mark a running snapshot job failed.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"internal/snapshot-jobs/{encode_path_param(job_id)}/fail",
            method="POST",
            json={
                "workflowRunId": workflow_run_id,
                "errorCode": error_code,
                "errorMessage": error_message,
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
                    PostInternalSnapshotJobsJobIdFailResponse,
                    parse_obj_as(
                        type_=PostInternalSnapshotJobsJobIdFailResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_sandbox_runtime_compile_plan(
        self,
        *,
        organization_id: str,
        profile_id: str,
        profile_version: int,
        image: PostInternalSandboxRuntimeCompilePlanRequestImage,
        snapshot_preparation_script_kind: typing.Optional[
            PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSandboxRuntimeCompilePlanResponse]:
        """
        Parameters
        ----------
        organization_id : str

        profile_id : str

        profile_version : int

        image : PostInternalSandboxRuntimeCompilePlanRequestImage

        snapshot_preparation_script_kind : typing.Optional[PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSandboxRuntimeCompilePlanResponse]
            Compile a sandbox profile version runtime plan for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/compile-plan",
            method="POST",
            json={
                "organizationId": organization_id,
                "profileId": profile_id,
                "profileVersion": profile_version,
                "snapshotPreparationScriptKind": snapshot_preparation_script_kind,
                "image": convert_and_respect_annotation_metadata(
                    object_=image, annotation=PostInternalSandboxRuntimeCompilePlanRequestImage, direction="write"
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
                    PostInternalSandboxRuntimeCompilePlanResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeCompilePlanResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_sandbox_runtime_start_profile_instance(
        self,
        *,
        organization_id: str,
        profile_id: str,
        profile_version: int,
        started_by: PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy,
        source: PostInternalSandboxRuntimeStartProfileInstanceRequestSource,
        primary_repository_id: typing.Optional[str] = OMIT,
        acting_user: typing.Optional[PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSandboxRuntimeStartProfileInstanceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        profile_id : str

        profile_version : int

        started_by : PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy

        source : PostInternalSandboxRuntimeStartProfileInstanceRequestSource

        primary_repository_id : typing.Optional[str]

        acting_user : typing.Optional[PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSandboxRuntimeStartProfileInstanceResponse]
            Start sandbox profile instance provisioning for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/start-profile-instance",
            method="POST",
            json={
                "organizationId": organization_id,
                "profileId": profile_id,
                "profileVersion": profile_version,
                "primaryRepositoryId": primary_repository_id,
                "startedBy": convert_and_respect_annotation_metadata(
                    object_=started_by,
                    annotation=PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy,
                    direction="write",
                ),
                "actingUser": convert_and_respect_annotation_metadata(
                    object_=acting_user,
                    annotation=PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser,
                    direction="write",
                ),
                "source": convert_and_respect_annotation_metadata(
                    object_=source,
                    annotation=PostInternalSandboxRuntimeStartProfileInstanceRequestSource,
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
                    PostInternalSandboxRuntimeStartProfileInstanceResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeStartProfileInstanceResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_sandbox_runtime_get_sandbox_instance(
        self, *, organization_id: str, instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostInternalSandboxRuntimeGetSandboxInstanceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSandboxRuntimeGetSandboxInstanceResponse]
            Get sandbox instance status for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/get-sandbox-instance",
            method="POST",
            json={
                "organizationId": organization_id,
                "instanceId": instance_id,
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
                    PostInternalSandboxRuntimeGetSandboxInstanceResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeGetSandboxInstanceResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_sandbox_runtime_resume_sandbox_instance(
        self,
        *,
        organization_id: str,
        instance_id: str,
        acting_user_id: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSandboxRuntimeResumeSandboxInstanceResponse]:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        acting_user_id : typing.Optional[str]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSandboxRuntimeResumeSandboxInstanceResponse]
            Queue sandbox instance resume for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/resume-sandbox-instance",
            method="POST",
            json={
                "organizationId": organization_id,
                "instanceId": instance_id,
                "actingUserId": acting_user_id,
                "idempotencyKey": idempotency_key,
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
                    PostInternalSandboxRuntimeResumeSandboxInstanceResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeResumeSandboxInstanceResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_sandbox_runtime_mint_connection_token(
        self,
        *,
        organization_id: str,
        instance_id: str,
        acting_user_id: typing.Optional[str] = OMIT,
        webhook_event_id: typing.Optional[str] = OMIT,
        delivery_task_id: typing.Optional[str] = OMIT,
        external_delivery_id: typing.Optional[str] = OMIT,
        trigger_run_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSandboxRuntimeMintConnectionTokenResponse]:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        acting_user_id : typing.Optional[str]

        webhook_event_id : typing.Optional[str]

        delivery_task_id : typing.Optional[str]

        external_delivery_id : typing.Optional[str]

        trigger_run_id : typing.Optional[str]

        conversation_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSandboxRuntimeMintConnectionTokenResponse]
            Mint a sandbox connection token for internal callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/mint-connection-token",
            method="POST",
            json={
                "organizationId": organization_id,
                "instanceId": instance_id,
                "actingUserId": acting_user_id,
                "webhookEventId": webhook_event_id,
                "deliveryTaskId": delivery_task_id,
                "externalDeliveryId": external_delivery_id,
                "triggerRunId": trigger_run_id,
                "conversationId": conversation_id,
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
                    PostInternalSandboxRuntimeMintConnectionTokenResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeMintConnectionTokenResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_sandbox_runtime_resolve_credentials(
        self,
        *,
        organization_id: str,
        provider: PostInternalSandboxRuntimeResolveCredentialsRequestProvider,
        connection_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSandboxRuntimeResolveCredentialsResponse]:
        """
        Parameters
        ----------
        organization_id : str

        provider : PostInternalSandboxRuntimeResolveCredentialsRequestProvider

        connection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSandboxRuntimeResolveCredentialsResponse]
            Resolve sandbox provider credentials for internal data-plane callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/resolve-credentials",
            method="POST",
            json={
                "organizationId": organization_id,
                "provider": provider,
                "connectionId": connection_id,
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
                    PostInternalSandboxRuntimeResolveCredentialsResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeResolveCredentialsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_internal_sandbox_runtime_resolve_designer_runtime_egress_route(
        self,
        *,
        organization_id: str,
        sandbox_instance_id: str,
        integration_connection_id: str,
        provider_tool_ids: typing.Sequence[str],
        target_url: str,
        method: str,
        transport: PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse]:
        """
        Parameters
        ----------
        organization_id : str

        sandbox_instance_id : str

        integration_connection_id : str

        provider_tool_ids : typing.Sequence[str]

        target_url : str

        method : str

        transport : PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse]
            Resolve a Designer runtime provider egress route for internal gateway callers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/sandbox-runtime/resolve-designer-runtime-egress-route",
            method="POST",
            json={
                "organizationId": organization_id,
                "sandboxInstanceId": sandbox_instance_id,
                "integrationConnectionId": integration_connection_id,
                "providerToolIds": provider_tool_ids,
                "targetUrl": target_url,
                "method": method,
                "transport": transport,
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
                    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse,
                    parse_obj_as(
                        type_=PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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
