

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.internal_dispatch_schedules_response import InternalDispatchSchedulesResponse
from .raw_client import AsyncRawInternalClient, RawInternalClient
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


OMIT = typing.cast(typing.Any, ...)


class InternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalClient
        """
        return self._raw_client

    def post_internal_integration_connections_refresh_resource(
        self,
        *,
        organization_id: str,
        connection_id: str,
        kind: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalIntegrationConnectionsRefreshResourceResponse:
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
        PostInternalIntegrationConnectionsRefreshResourceResponse
            Request integration connection resource refresh for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_integration_connections_refresh_resource(
            organization_id="organizationId",
            connection_id="connectionId",
            kind="kind",
        )
        """
        _response = self._raw_client.post_internal_integration_connections_refresh_resource(
            organization_id=organization_id, connection_id=connection_id, kind=kind, request_options=request_options
        )
        return _response.data

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
    ) -> PostInternalIntegrationCredentialsResolveResponse:
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
        PostInternalIntegrationCredentialsResolveResponse
            Resolve integration credential for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_integration_credentials_resolve(
            connection_id="connectionId",
            secret_type="secretType",
        )
        """
        _response = self._raw_client.post_internal_integration_credentials_resolve(
            connection_id=connection_id,
            secret_type=secret_type,
            binding_id=binding_id,
            force_refresh=force_refresh,
            slot_key=slot_key,
            resolver_key=resolver_key,
            request_options=request_options,
        )
        return _response.data

    def post_internal_integration_credentials_resolve_target_secrets(
        self,
        *,
        targets: typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalIntegrationCredentialsResolveTargetSecretsResponse:
        """
        Parameters
        ----------
        targets : typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostInternalIntegrationCredentialsResolveTargetSecretsResponse
            Resolve integration target secrets for internal callers.

        Examples
        --------
        from fern.internal import (
            PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_integration_credentials_resolve_target_secrets(
            targets=[
                PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem(
                    target_key="targetKey",
                )
            ],
        )
        """
        _response = self._raw_client.post_internal_integration_credentials_resolve_target_secrets(
            targets=targets, request_options=request_options
        )
        return _response.data

    def post_internal_identity_linking_resolve_principal_credential(
        self,
        *,
        organization_id: str,
        acting_user_id: str,
        provider_family: str,
        integration_connection_id: typing.Optional[str] = OMIT,
        credential_kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalIdentityLinkingResolvePrincipalCredentialResponse:
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
        PostInternalIdentityLinkingResolvePrincipalCredentialResponse
            Resolve linked-principal credential for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_identity_linking_resolve_principal_credential(
            organization_id="organizationId",
            acting_user_id="actingUserId",
            provider_family="providerFamily",
        )
        """
        _response = self._raw_client.post_internal_identity_linking_resolve_principal_credential(
            organization_id=organization_id,
            acting_user_id=acting_user_id,
            provider_family=provider_family,
            integration_connection_id=integration_connection_id,
            credential_kind=credential_kind,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalIdentityLinkingSignCommitPayloadResponse:
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
        PostInternalIdentityLinkingSignCommitPayloadResponse
            Sign a Git commit payload for a linked-principal credential.

        Examples
        --------
        from fern.internal import (
            PostInternalIdentityLinkingSignCommitPayloadRequestEncoding,
            PostInternalIdentityLinkingSignCommitPayloadRequestFormat,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_identity_linking_sign_commit_payload(
            organization_id="organizationId",
            sandbox_instance_id="sandboxInstanceId",
            acting_user_id="actingUserId",
            provider_family="providerFamily",
            integration_connection_id="integrationConnectionId",
            format=PostInternalIdentityLinkingSignCommitPayloadRequestFormat.SSH,
            key_ref="keyRef",
            grant="grant",
            payload="payload",
            encoding=PostInternalIdentityLinkingSignCommitPayloadRequestEncoding.BASE64,
        )
        """
        _response = self._raw_client.post_internal_identity_linking_sign_commit_payload(
            organization_id=organization_id,
            sandbox_instance_id=sandbox_instance_id,
            acting_user_id=acting_user_id,
            provider_family=provider_family,
            integration_connection_id=integration_connection_id,
            format=format,
            key_ref=key_ref,
            grant=grant,
            payload=payload,
            encoding=encoding,
            request_options=request_options,
        )
        return _response.data

    def post_internal_provider_resource_associations_register(
        self,
        *,
        integration_connection_id: str,
        resource_kind: str,
        provider_resource_id: str,
        sandbox_instance_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalProviderResourceAssociationsRegisterResponse:
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
        PostInternalProviderResourceAssociationsRegisterResponse
            Register a provider resource association for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_provider_resource_associations_register(
            integration_connection_id="integrationConnectionId",
            resource_kind="resourceKind",
            provider_resource_id="providerResourceId",
            sandbox_instance_id="sandboxInstanceId",
        )
        """
        _response = self._raw_client.post_internal_provider_resource_associations_register(
            integration_connection_id=integration_connection_id,
            resource_kind=resource_kind,
            provider_resource_id=provider_resource_id,
            sandbox_instance_id=sandbox_instance_id,
            request_options=request_options,
        )
        return _response.data

    def post_internal_schedules_dispatch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalDispatchSchedulesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalDispatchSchedulesResponse
            Enqueue scheduled workflow dispatch for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_schedules_dispatch()
        """
        _response = self._raw_client.post_internal_schedules_dispatch(request_options=request_options)
        return _response.data

    def post_internal_snapshot_jobs_job_id_claim(
        self, job_id: str, *, workflow_run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostInternalSnapshotJobsJobIdClaimResponse:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostInternalSnapshotJobsJobIdClaimResponse
            Claim a queued snapshot job for workflow execution.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_snapshot_jobs_job_id_claim(
            job_id="jobId",
            workflow_run_id="workflowRunId",
        )
        """
        _response = self._raw_client.post_internal_snapshot_jobs_job_id_claim(
            job_id, workflow_run_id=workflow_run_id, request_options=request_options
        )
        return _response.data

    def post_internal_snapshot_jobs_job_id_succeed(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        image: PostInternalSnapshotJobsJobIdSucceedRequestImage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSnapshotJobsJobIdSucceedResponse:
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
        PostInternalSnapshotJobsJobIdSucceedResponse
            Mark a running snapshot job succeeded.

        Examples
        --------
        from fern.internal import PostInternalSnapshotJobsJobIdSucceedRequestImage

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_snapshot_jobs_job_id_succeed(
            job_id="jobId",
            workflow_run_id="workflowRunId",
            image=PostInternalSnapshotJobsJobIdSucceedRequestImage(
                provider="provider",
                image_id="imageId",
            ),
        )
        """
        _response = self._raw_client.post_internal_snapshot_jobs_job_id_succeed(
            job_id, workflow_run_id=workflow_run_id, image=image, request_options=request_options
        )
        return _response.data

    def post_internal_snapshot_jobs_job_id_fail(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        error_code: str,
        error_message: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSnapshotJobsJobIdFailResponse:
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
        PostInternalSnapshotJobsJobIdFailResponse
            Mark a running snapshot job failed.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_snapshot_jobs_job_id_fail(
            job_id="jobId",
            workflow_run_id="workflowRunId",
            error_code="errorCode",
            error_message="errorMessage",
        )
        """
        _response = self._raw_client.post_internal_snapshot_jobs_job_id_fail(
            job_id,
            workflow_run_id=workflow_run_id,
            error_code=error_code,
            error_message=error_message,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeCompilePlanResponse:
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
        PostInternalSandboxRuntimeCompilePlanResponse
            Compile a sandbox profile version runtime plan for internal callers.

        Examples
        --------
        from fern.internal import (
            PostInternalSandboxRuntimeCompilePlanRequestImage,
            PostInternalSandboxRuntimeCompilePlanRequestImageKind,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_sandbox_runtime_compile_plan(
            organization_id="organizationId",
            profile_id="profileId",
            profile_version=1,
            image=PostInternalSandboxRuntimeCompilePlanRequestImage(
                image_id="imageId",
                kind=PostInternalSandboxRuntimeCompilePlanRequestImageKind.BASE,
            ),
        )
        """
        _response = self._raw_client.post_internal_sandbox_runtime_compile_plan(
            organization_id=organization_id,
            profile_id=profile_id,
            profile_version=profile_version,
            image=image,
            snapshot_preparation_script_kind=snapshot_preparation_script_kind,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeStartProfileInstanceResponse:
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
        PostInternalSandboxRuntimeStartProfileInstanceResponse
            Start sandbox profile instance provisioning for internal callers.

        Examples
        --------
        from fern.internal import (
            PostInternalSandboxRuntimeStartProfileInstanceRequestSourceZero,
            PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy,
            PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKindZero,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_sandbox_runtime_start_profile_instance(
            organization_id="organizationId",
            profile_id="profileId",
            profile_version=1,
            started_by=PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy(
                kind=PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKindZero.USER,
                id="id",
            ),
            source=PostInternalSandboxRuntimeStartProfileInstanceRequestSourceZero.DASHBOARD,
        )
        """
        _response = self._raw_client.post_internal_sandbox_runtime_start_profile_instance(
            organization_id=organization_id,
            profile_id=profile_id,
            profile_version=profile_version,
            started_by=started_by,
            source=source,
            primary_repository_id=primary_repository_id,
            acting_user=acting_user,
            request_options=request_options,
        )
        return _response.data

    def post_internal_sandbox_runtime_get_sandbox_instance(
        self, *, organization_id: str, instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostInternalSandboxRuntimeGetSandboxInstanceResponse:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostInternalSandboxRuntimeGetSandboxInstanceResponse
            Get sandbox instance status for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_sandbox_runtime_get_sandbox_instance(
            organization_id="organizationId",
            instance_id="instanceId",
        )
        """
        _response = self._raw_client.post_internal_sandbox_runtime_get_sandbox_instance(
            organization_id=organization_id, instance_id=instance_id, request_options=request_options
        )
        return _response.data

    def post_internal_sandbox_runtime_resume_sandbox_instance(
        self,
        *,
        organization_id: str,
        instance_id: str,
        acting_user_id: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSandboxRuntimeResumeSandboxInstanceResponse:
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
        PostInternalSandboxRuntimeResumeSandboxInstanceResponse
            Queue sandbox instance resume for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_sandbox_runtime_resume_sandbox_instance(
            organization_id="organizationId",
            instance_id="instanceId",
        )
        """
        _response = self._raw_client.post_internal_sandbox_runtime_resume_sandbox_instance(
            organization_id=organization_id,
            instance_id=instance_id,
            acting_user_id=acting_user_id,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeMintConnectionTokenResponse:
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
        PostInternalSandboxRuntimeMintConnectionTokenResponse
            Mint a sandbox connection token for internal callers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_sandbox_runtime_mint_connection_token(
            organization_id="organizationId",
            instance_id="instanceId",
        )
        """
        _response = self._raw_client.post_internal_sandbox_runtime_mint_connection_token(
            organization_id=organization_id,
            instance_id=instance_id,
            acting_user_id=acting_user_id,
            webhook_event_id=webhook_event_id,
            delivery_task_id=delivery_task_id,
            external_delivery_id=external_delivery_id,
            trigger_run_id=trigger_run_id,
            conversation_id=conversation_id,
            request_options=request_options,
        )
        return _response.data

    def post_internal_sandbox_runtime_resolve_credentials(
        self,
        *,
        organization_id: str,
        provider: PostInternalSandboxRuntimeResolveCredentialsRequestProvider,
        connection_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSandboxRuntimeResolveCredentialsResponse:
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
        PostInternalSandboxRuntimeResolveCredentialsResponse
            Resolve sandbox provider credentials for internal data-plane callers.

        Examples
        --------
        from fern.internal import (
            PostInternalSandboxRuntimeResolveCredentialsRequestProvider,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_sandbox_runtime_resolve_credentials(
            organization_id="organizationId",
            provider=PostInternalSandboxRuntimeResolveCredentialsRequestProvider.DOCKER,
        )
        """
        _response = self._raw_client.post_internal_sandbox_runtime_resolve_credentials(
            organization_id=organization_id,
            provider=provider,
            connection_id=connection_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse:
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
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse
            Resolve a Designer runtime provider egress route for internal gateway callers.

        Examples
        --------
        from fern.internal import (
            PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.post_internal_sandbox_runtime_resolve_designer_runtime_egress_route(
            organization_id="organizationId",
            sandbox_instance_id="sandboxInstanceId",
            integration_connection_id="integrationConnectionId",
            provider_tool_ids=["providerToolIds"],
            target_url="targetUrl",
            method="method",
            transport=PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport.HTTP,
        )
        """
        _response = self._raw_client.post_internal_sandbox_runtime_resolve_designer_runtime_egress_route(
            organization_id=organization_id,
            sandbox_instance_id=sandbox_instance_id,
            integration_connection_id=integration_connection_id,
            provider_tool_ids=provider_tool_ids,
            target_url=target_url,
            method=method,
            transport=transport,
            request_options=request_options,
        )
        return _response.data


class AsyncInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalClient
        """
        return self._raw_client

    async def post_internal_integration_connections_refresh_resource(
        self,
        *,
        organization_id: str,
        connection_id: str,
        kind: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalIntegrationConnectionsRefreshResourceResponse:
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
        PostInternalIntegrationConnectionsRefreshResourceResponse
            Request integration connection resource refresh for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_integration_connections_refresh_resource(
                organization_id="organizationId",
                connection_id="connectionId",
                kind="kind",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_integration_connections_refresh_resource(
            organization_id=organization_id, connection_id=connection_id, kind=kind, request_options=request_options
        )
        return _response.data

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
    ) -> PostInternalIntegrationCredentialsResolveResponse:
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
        PostInternalIntegrationCredentialsResolveResponse
            Resolve integration credential for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_integration_credentials_resolve(
                connection_id="connectionId",
                secret_type="secretType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_integration_credentials_resolve(
            connection_id=connection_id,
            secret_type=secret_type,
            binding_id=binding_id,
            force_refresh=force_refresh,
            slot_key=slot_key,
            resolver_key=resolver_key,
            request_options=request_options,
        )
        return _response.data

    async def post_internal_integration_credentials_resolve_target_secrets(
        self,
        *,
        targets: typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalIntegrationCredentialsResolveTargetSecretsResponse:
        """
        Parameters
        ----------
        targets : typing.Sequence[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostInternalIntegrationCredentialsResolveTargetSecretsResponse
            Resolve integration target secrets for internal callers.

        Examples
        --------
        import asyncio

        from fern.internal import (
            PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_integration_credentials_resolve_target_secrets(
                targets=[
                    PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem(
                        target_key="targetKey",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_integration_credentials_resolve_target_secrets(
            targets=targets, request_options=request_options
        )
        return _response.data

    async def post_internal_identity_linking_resolve_principal_credential(
        self,
        *,
        organization_id: str,
        acting_user_id: str,
        provider_family: str,
        integration_connection_id: typing.Optional[str] = OMIT,
        credential_kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalIdentityLinkingResolvePrincipalCredentialResponse:
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
        PostInternalIdentityLinkingResolvePrincipalCredentialResponse
            Resolve linked-principal credential for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_identity_linking_resolve_principal_credential(
                organization_id="organizationId",
                acting_user_id="actingUserId",
                provider_family="providerFamily",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_identity_linking_resolve_principal_credential(
            organization_id=organization_id,
            acting_user_id=acting_user_id,
            provider_family=provider_family,
            integration_connection_id=integration_connection_id,
            credential_kind=credential_kind,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalIdentityLinkingSignCommitPayloadResponse:
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
        PostInternalIdentityLinkingSignCommitPayloadResponse
            Sign a Git commit payload for a linked-principal credential.

        Examples
        --------
        import asyncio

        from fern.internal import (
            PostInternalIdentityLinkingSignCommitPayloadRequestEncoding,
            PostInternalIdentityLinkingSignCommitPayloadRequestFormat,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_identity_linking_sign_commit_payload(
                organization_id="organizationId",
                sandbox_instance_id="sandboxInstanceId",
                acting_user_id="actingUserId",
                provider_family="providerFamily",
                integration_connection_id="integrationConnectionId",
                format=PostInternalIdentityLinkingSignCommitPayloadRequestFormat.SSH,
                key_ref="keyRef",
                grant="grant",
                payload="payload",
                encoding=PostInternalIdentityLinkingSignCommitPayloadRequestEncoding.BASE64,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_identity_linking_sign_commit_payload(
            organization_id=organization_id,
            sandbox_instance_id=sandbox_instance_id,
            acting_user_id=acting_user_id,
            provider_family=provider_family,
            integration_connection_id=integration_connection_id,
            format=format,
            key_ref=key_ref,
            grant=grant,
            payload=payload,
            encoding=encoding,
            request_options=request_options,
        )
        return _response.data

    async def post_internal_provider_resource_associations_register(
        self,
        *,
        integration_connection_id: str,
        resource_kind: str,
        provider_resource_id: str,
        sandbox_instance_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalProviderResourceAssociationsRegisterResponse:
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
        PostInternalProviderResourceAssociationsRegisterResponse
            Register a provider resource association for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_provider_resource_associations_register(
                integration_connection_id="integrationConnectionId",
                resource_kind="resourceKind",
                provider_resource_id="providerResourceId",
                sandbox_instance_id="sandboxInstanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_provider_resource_associations_register(
            integration_connection_id=integration_connection_id,
            resource_kind=resource_kind,
            provider_resource_id=provider_resource_id,
            sandbox_instance_id=sandbox_instance_id,
            request_options=request_options,
        )
        return _response.data

    async def post_internal_schedules_dispatch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalDispatchSchedulesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalDispatchSchedulesResponse
            Enqueue scheduled workflow dispatch for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_schedules_dispatch()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_schedules_dispatch(request_options=request_options)
        return _response.data

    async def post_internal_snapshot_jobs_job_id_claim(
        self, job_id: str, *, workflow_run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostInternalSnapshotJobsJobIdClaimResponse:
        """
        Parameters
        ----------
        job_id : str

        workflow_run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostInternalSnapshotJobsJobIdClaimResponse
            Claim a queued snapshot job for workflow execution.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_snapshot_jobs_job_id_claim(
                job_id="jobId",
                workflow_run_id="workflowRunId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_snapshot_jobs_job_id_claim(
            job_id, workflow_run_id=workflow_run_id, request_options=request_options
        )
        return _response.data

    async def post_internal_snapshot_jobs_job_id_succeed(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        image: PostInternalSnapshotJobsJobIdSucceedRequestImage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSnapshotJobsJobIdSucceedResponse:
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
        PostInternalSnapshotJobsJobIdSucceedResponse
            Mark a running snapshot job succeeded.

        Examples
        --------
        import asyncio

        from fern.internal import PostInternalSnapshotJobsJobIdSucceedRequestImage

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_snapshot_jobs_job_id_succeed(
                job_id="jobId",
                workflow_run_id="workflowRunId",
                image=PostInternalSnapshotJobsJobIdSucceedRequestImage(
                    provider="provider",
                    image_id="imageId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_snapshot_jobs_job_id_succeed(
            job_id, workflow_run_id=workflow_run_id, image=image, request_options=request_options
        )
        return _response.data

    async def post_internal_snapshot_jobs_job_id_fail(
        self,
        job_id: str,
        *,
        workflow_run_id: str,
        error_code: str,
        error_message: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSnapshotJobsJobIdFailResponse:
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
        PostInternalSnapshotJobsJobIdFailResponse
            Mark a running snapshot job failed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_snapshot_jobs_job_id_fail(
                job_id="jobId",
                workflow_run_id="workflowRunId",
                error_code="errorCode",
                error_message="errorMessage",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_snapshot_jobs_job_id_fail(
            job_id,
            workflow_run_id=workflow_run_id,
            error_code=error_code,
            error_message=error_message,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeCompilePlanResponse:
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
        PostInternalSandboxRuntimeCompilePlanResponse
            Compile a sandbox profile version runtime plan for internal callers.

        Examples
        --------
        import asyncio

        from fern.internal import (
            PostInternalSandboxRuntimeCompilePlanRequestImage,
            PostInternalSandboxRuntimeCompilePlanRequestImageKind,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_sandbox_runtime_compile_plan(
                organization_id="organizationId",
                profile_id="profileId",
                profile_version=1,
                image=PostInternalSandboxRuntimeCompilePlanRequestImage(
                    image_id="imageId",
                    kind=PostInternalSandboxRuntimeCompilePlanRequestImageKind.BASE,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_sandbox_runtime_compile_plan(
            organization_id=organization_id,
            profile_id=profile_id,
            profile_version=profile_version,
            image=image,
            snapshot_preparation_script_kind=snapshot_preparation_script_kind,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeStartProfileInstanceResponse:
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
        PostInternalSandboxRuntimeStartProfileInstanceResponse
            Start sandbox profile instance provisioning for internal callers.

        Examples
        --------
        import asyncio

        from fern.internal import (
            PostInternalSandboxRuntimeStartProfileInstanceRequestSourceZero,
            PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy,
            PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKindZero,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_sandbox_runtime_start_profile_instance(
                organization_id="organizationId",
                profile_id="profileId",
                profile_version=1,
                started_by=PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy(
                    kind=PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKindZero.USER,
                    id="id",
                ),
                source=PostInternalSandboxRuntimeStartProfileInstanceRequestSourceZero.DASHBOARD,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_sandbox_runtime_start_profile_instance(
            organization_id=organization_id,
            profile_id=profile_id,
            profile_version=profile_version,
            started_by=started_by,
            source=source,
            primary_repository_id=primary_repository_id,
            acting_user=acting_user,
            request_options=request_options,
        )
        return _response.data

    async def post_internal_sandbox_runtime_get_sandbox_instance(
        self, *, organization_id: str, instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostInternalSandboxRuntimeGetSandboxInstanceResponse:
        """
        Parameters
        ----------
        organization_id : str

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostInternalSandboxRuntimeGetSandboxInstanceResponse
            Get sandbox instance status for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_sandbox_runtime_get_sandbox_instance(
                organization_id="organizationId",
                instance_id="instanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_sandbox_runtime_get_sandbox_instance(
            organization_id=organization_id, instance_id=instance_id, request_options=request_options
        )
        return _response.data

    async def post_internal_sandbox_runtime_resume_sandbox_instance(
        self,
        *,
        organization_id: str,
        instance_id: str,
        acting_user_id: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSandboxRuntimeResumeSandboxInstanceResponse:
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
        PostInternalSandboxRuntimeResumeSandboxInstanceResponse
            Queue sandbox instance resume for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_sandbox_runtime_resume_sandbox_instance(
                organization_id="organizationId",
                instance_id="instanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_sandbox_runtime_resume_sandbox_instance(
            organization_id=organization_id,
            instance_id=instance_id,
            acting_user_id=acting_user_id,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeMintConnectionTokenResponse:
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
        PostInternalSandboxRuntimeMintConnectionTokenResponse
            Mint a sandbox connection token for internal callers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_sandbox_runtime_mint_connection_token(
                organization_id="organizationId",
                instance_id="instanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_sandbox_runtime_mint_connection_token(
            organization_id=organization_id,
            instance_id=instance_id,
            acting_user_id=acting_user_id,
            webhook_event_id=webhook_event_id,
            delivery_task_id=delivery_task_id,
            external_delivery_id=external_delivery_id,
            trigger_run_id=trigger_run_id,
            conversation_id=conversation_id,
            request_options=request_options,
        )
        return _response.data

    async def post_internal_sandbox_runtime_resolve_credentials(
        self,
        *,
        organization_id: str,
        provider: PostInternalSandboxRuntimeResolveCredentialsRequestProvider,
        connection_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostInternalSandboxRuntimeResolveCredentialsResponse:
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
        PostInternalSandboxRuntimeResolveCredentialsResponse
            Resolve sandbox provider credentials for internal data-plane callers.

        Examples
        --------
        import asyncio

        from fern.internal import (
            PostInternalSandboxRuntimeResolveCredentialsRequestProvider,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_sandbox_runtime_resolve_credentials(
                organization_id="organizationId",
                provider=PostInternalSandboxRuntimeResolveCredentialsRequestProvider.DOCKER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_sandbox_runtime_resolve_credentials(
            organization_id=organization_id,
            provider=provider,
            connection_id=connection_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse:
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
        PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse
            Resolve a Designer runtime provider egress route for internal gateway callers.

        Examples
        --------
        import asyncio

        from fern.internal import (
            PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.post_internal_sandbox_runtime_resolve_designer_runtime_egress_route(
                organization_id="organizationId",
                sandbox_instance_id="sandboxInstanceId",
                integration_connection_id="integrationConnectionId",
                provider_tool_ids=["providerToolIds"],
                target_url="targetUrl",
                method="method",
                transport=PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport.HTTP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_internal_sandbox_runtime_resolve_designer_runtime_egress_route(
            organization_id=organization_id,
            sandbox_instance_id=sandbox_instance_id,
            integration_connection_id=integration_connection_id,
            provider_tool_ids=provider_tool_ids,
            target_url=target_url,
            method=method,
            transport=transport,
            request_options=request_options,
        )
        return _response.data
