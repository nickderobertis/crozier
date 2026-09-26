# Reference
## Internal
<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_integration_connections_refresh_resource</a>(...) -> PostInternalIntegrationConnectionsRefreshResourceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_integration_connections_refresh_resource(
    organization_id="organizationId",
    connection_id="connectionId",
    kind="kind",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_integration_credentials_resolve</a>(...) -> PostInternalIntegrationCredentialsResolveResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_integration_credentials_resolve(
    connection_id="connectionId",
    secret_type="secretType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**binding_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**force_refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**slot_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resolver_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_integration_credentials_resolve_target_secrets</a>(...) -> PostInternalIntegrationCredentialsResolveTargetSecretsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.internal import PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**targets:** `typing.List[PostInternalIntegrationCredentialsResolveTargetSecretsRequestTargetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_identity_linking_resolve_principal_credential</a>(...) -> PostInternalIdentityLinkingResolvePrincipalCredentialResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_identity_linking_resolve_principal_credential(
    organization_id="organizationId",
    acting_user_id="actingUserId",
    provider_family="providerFamily",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**acting_user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider_family:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integration_connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**credential_kind:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_identity_linking_sign_commit_payload</a>(...) -> PostInternalIdentityLinkingSignCommitPayloadResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.internal import PostInternalIdentityLinkingSignCommitPayloadRequestFormat, PostInternalIdentityLinkingSignCommitPayloadRequestEncoding

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sandbox_instance_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**acting_user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider_family:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integration_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `PostInternalIdentityLinkingSignCommitPayloadRequestFormat` 
    
</dd>
</dl>

<dl>
<dd>

**key_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**grant:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**encoding:** `PostInternalIdentityLinkingSignCommitPayloadRequestEncoding` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_provider_resource_associations_register</a>(...) -> PostInternalProviderResourceAssociationsRegisterResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**integration_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_kind:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider_resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sandbox_instance_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_schedules_dispatch</a>() -> InternalDispatchSchedulesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_schedules_dispatch()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_snapshot_jobs_job_id_claim</a>(...) -> PostInternalSnapshotJobsJobIdClaimResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_snapshot_jobs_job_id_claim(
    job_id="jobId",
    workflow_run_id="workflowRunId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_snapshot_jobs_job_id_succeed</a>(...) -> PostInternalSnapshotJobsJobIdSucceedResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.internal import PostInternalSnapshotJobsJobIdSucceedRequestImage

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `PostInternalSnapshotJobsJobIdSucceedRequestImage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_snapshot_jobs_job_id_fail</a>(...) -> PostInternalSnapshotJobsJobIdFailResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**error_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**error_message:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_sandbox_runtime_compile_plan</a>(...) -> PostInternalSandboxRuntimeCompilePlanResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.internal import PostInternalSandboxRuntimeCompilePlanRequestImage, PostInternalSandboxRuntimeCompilePlanRequestImageKind

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**profile_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `PostInternalSandboxRuntimeCompilePlanRequestImage` 
    
</dd>
</dl>

<dl>
<dd>

**snapshot_preparation_script_kind:** `typing.Optional[PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_sandbox_runtime_start_profile_instance</a>(...) -> PostInternalSandboxRuntimeStartProfileInstanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.internal import PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy, PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKindZero, PostInternalSandboxRuntimeStartProfileInstanceRequestSourceZero

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**profile_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**started_by:** `PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `PostInternalSandboxRuntimeStartProfileInstanceRequestSource` 
    
</dd>
</dl>

<dl>
<dd>

**primary_repository_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**acting_user:** `typing.Optional[PostInternalSandboxRuntimeStartProfileInstanceRequestActingUser]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_sandbox_runtime_get_sandbox_instance</a>(...) -> PostInternalSandboxRuntimeGetSandboxInstanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_sandbox_runtime_get_sandbox_instance(
    organization_id="organizationId",
    instance_id="instanceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_sandbox_runtime_resume_sandbox_instance</a>(...) -> PostInternalSandboxRuntimeResumeSandboxInstanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_sandbox_runtime_resume_sandbox_instance(
    organization_id="organizationId",
    instance_id="instanceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**acting_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_sandbox_runtime_mint_connection_token</a>(...) -> PostInternalSandboxRuntimeMintConnectionTokenResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_sandbox_runtime_mint_connection_token(
    organization_id="organizationId",
    instance_id="instanceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**acting_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_event_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**delivery_task_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_delivery_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**trigger_run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_sandbox_runtime_resolve_credentials</a>(...) -> PostInternalSandboxRuntimeResolveCredentialsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.internal import PostInternalSandboxRuntimeResolveCredentialsRequestProvider

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_sandbox_runtime_resolve_credentials(
    organization_id="organizationId",
    provider=PostInternalSandboxRuntimeResolveCredentialsRequestProvider.DOCKER,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `PostInternalSandboxRuntimeResolveCredentialsRequestProvider` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.<a href="src/fern/internal/client.py">post_internal_sandbox_runtime_resolve_designer_runtime_egress_route</a>(...) -> PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.internal import PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.internal.post_internal_sandbox_runtime_resolve_designer_runtime_egress_route(
    organization_id="organizationId",
    sandbox_instance_id="sandboxInstanceId",
    integration_connection_id="integrationConnectionId",
    provider_tool_ids=[
        "providerToolIds"
    ],
    target_url="targetUrl",
    method="method",
    transport=PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport.HTTP,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sandbox_instance_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integration_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider_tool_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transport:** `PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

