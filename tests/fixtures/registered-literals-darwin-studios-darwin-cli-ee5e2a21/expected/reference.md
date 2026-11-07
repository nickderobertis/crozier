# Reference
<details><summary><code>client.<a href="src/fern/client.py">search</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find and rank public capabilities from the active Creora Product v2 index. Search is discovery, not execution authorization. No credential is required at the public anonymous limit. You may supply a Darwin API key or OAuth bearer with directory:read for the higher authenticated limit.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search(
    query="Find an AI that can compare SOC 2 vendors and return a cited recommendation under $500.",
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

**query:** `str` — Describe the capability or outcome you need in natural language. Include the task, important constraints, and success criteria that should affect ranking; use the dedicated AI and capability read endpoints for exact lookups.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional structured constraints applied in addition to the natural-language query. Use these fields for hard requirements instead of embedding machine-readable filters in query text.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of ranked capabilities to return. Defaults to 10 and cannot exceed 50.
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_account</a>(...) -> CreatedAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register an unverified Darwin account without creating an AI or API key. Verify the email address through Darwin sign-in, then complete account setup before issuing application credentials. An application key never identifies an end user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CreateAccountRequestType
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.create_account(
    email="email",
    password="password",
    name="name",
    type=CreateAccountRequestType.PERSONAL,
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

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateAccountRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**organization_name:** `typing.Optional[str]` — Required for business and software.
    
</dd>
</dl>

<dl>
<dd>

**organization_domain:** `typing.Optional[str]` — Required for business and software; not ownership proof.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_account</a>(...) -> AccountSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the account behind a user-bound legacy key or a user-scoped OAuth grant with account:read. Application-only keys cannot read or impersonate an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_account()

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

**ai_id:** `typing.Optional[str]` — Optional authorized AI context to select in the response; omit to use the active selection.
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_application</a>(...) -> ApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a developer application for the authenticated account. Requires applications:write on a user-scoped OAuth grant or a legacy user key. This does not grant access to another user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.create_application(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**website_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_uris:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_application</a>(...) -> ApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one application owned by the authenticated account. Requires applications:read on a user-scoped grant or legacy key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_application(
    application_id="applicationId",
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

**application_id:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_actions</a>(...) -> ActListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List current or ended human Actions with human:actions, or select an acting AI for an AI-scoped agent:read/goals:read grant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.list_actions()

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

**acting_ai_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_ai_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lifecycle:** `typing.Optional[ListActionsRequestLifecycle]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">start_action</a>(...) -> ActStartActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start durable work from an exact Search result. A consenting human OAuth user uses human:actions without an AI; an AI-scoped caller uses agent:write or goals:write and selects an authorized acting AI.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.start_action(
    capability_id="capabilityId",
    capability_revision=1,
    request_id="requestId",
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

**capability_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**capability_revision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.List[ActionAttachment]]` 
    
</dd>
</dl>

<dl>
<dd>

**intent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**acting_ai_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_ai_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search_attribution_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_action</a>(...) -> ActGetActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the truthful current status and required next step for one action. Requires the matching human:actions grant or an AI-scoped agent:read/goals:read grant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_action(
    action_id="actionId",
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

**action_id:** `str` — The Action identifier returned by Start action or List actions.
    
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

<details><summary><code>client.<a href="src/fern/client.py">continue_action</a>(...) -> ActUpdateActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Give an action more information without implicitly approving anything. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ActUpdateRequestAttachments
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.continue_action(
    action_id="actionId",
    request=ActUpdateRequestAttachments(
        request_id="requestId",
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

**action_id:** `str` — The Action identifier returned by Start action or List actions.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ActUpdateRequest` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">authenticate_session</a>(...) -> AuthenticateSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Establish or reuse one bounded authentication relationship between the caller and a destination AI. When the destination has no account for the user, the same hosted flow completes required first-time setup before connecting. The relationship can be reused across Actions until it expires or is revoked.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AuthenticateSessionRequestSource_OneTime
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authenticate_session(
    ai_id="aiId",
    method_id="oauth_github",
    source=AuthenticateSessionRequestSource_OneTime(),
    save_to_darwin_vault=False,
    request_id="request_auth_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
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

**ai_id:** `str` — The destination AI to authenticate with.
    
</dd>
</dl>

<dl>
<dd>

**method_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `AuthenticateSessionRequestSource` 
    
</dd>
</dl>

<dl>
<dd>

**save_to_darwin_vault:** `bool` — Explicit consent to persist a one-time credential in Darwin Vault after authorization.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">pay_action</a>(...) -> ActPayActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Choose a bound direct or Darwin Pay route without overriding the reviewed merchant, amount, currency, protocol, or scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ActPayRequestRoute, ActPayRequestSource_OneTime
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pay_action(
    action_id="actionId",
    interaction_id="interaction_pay_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
    expected_revision=4,
    route=ActPayRequestRoute.DARWIN_PAY,
    source=ActPayRequestSource_OneTime(),
    save=False,
    request_id="request_pay_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
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

**action_id:** `str` — The Action identifier returned by Start action or List actions.
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**route:** `ActPayRequestRoute` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `ActPayRequestSource` 
    
</dd>
</dl>

<dl>
<dd>

**save:** `bool` — Explicit consent to save a tokenized processor reference after a successful one-time flow.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">approve_action</a>(...) -> ActApproveActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply an exact reviewed approval decision with stale-preview protection. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ActApproveRequestDecision
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approve_action(
    action_id="actionId",
    approval_id="approvalId",
    decision=ActApproveRequestDecision.APPROVE,
    expected_revision=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    reviewed_payload_digest="reviewedPayloadDigest",
    request_id="requestId",
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

**action_id:** `str` — The Action identifier returned by Start action or List actions.
    
</dd>
</dl>

<dl>
<dd>

**approval_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**decision:** `ActApproveRequestDecision` 
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**reviewed_payload_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">stop_action</a>(...) -> ActStopActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compatibility operation that interrupts only the current queued or running turn. New integrations should use End action for one clear finish-or-cancel closure flow. Requires the matching human:actions or AI-scoped agent:write/goals:write grant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stop_action(
    action_id="actionId",
    request_id="requestId",
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

**action_id:** `str` — The Action identifier returned by Start action or List actions.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">end_action</a>(...) -> ActEndActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Freeze ordinary new work and request durable closure with finish or cancel intent. Darwin derives the final outcome; the caller cannot declare success.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ActEndRequestIntent
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.end_action(
    action_id="actionId",
    expected_revision=7,
    intent=ActEndRequestIntent.FINISH,
    request_id="request_end_01J9Y8M4Z7B9R6K2X3C5V1N0PQ",
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

**action_id:** `str` — The Action identifier returned by Start action or List actions.
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**intent:** `ActEndRequestIntent` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_api_keys</a>() -> ApiKeyList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List application keys and existing legacy user-bound keys for the signed-in account. Plaintext secrets are never included.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.list_api_keys()

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

<details><summary><code>client.<a href="src/fern/client.py">create_api_key</a>(...) -> CreatedApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an application-only key for an owned application. It can Search public capabilities but cannot impersonate a user or Act. The plaintext apiKey is returned once. Requires a verified account session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.create_api_key(
    application_id="applicationId",
    name="Production server",
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

**application_id:** `str` — An active application owned by the signed-in account.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — A recognizable name for the environment or integration that will use this key.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[CreateApiKeyRequestScopesItem]]` — Optional. New application keys are limited to directory:read; use OAuth for user-scoped Act.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — Optional future ISO 8601 expiration. Omit or set null for no scheduled expiration.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_api_usage</a>() -> ApiKeyUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get lifetime authenticated-request counts for the account and each API key. This is operational key usage, not billable Action spend. Requires an authenticated account session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_api_usage()

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

<details><summary><code>client.<a href="src/fern/client.py">delete_api_key</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an API key owned by the signed-in Darwin account. Revocation is immediate and keeps non-secret audit metadata. Requires an authenticated account session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_api_key(
    api_key_id="apiKeyId",
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

**api_key_id:** `str` — The API-key ID returned by Create API key or List API keys. This is not the secret key value.
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_search_history</a>(...) -> SearchHistoryPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Search-history entries retained for up to 90 days for a user-bound legacy key or user-scoped OAuth grant. Application-only keys cannot read a user’s history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.list_search_history()

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

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

