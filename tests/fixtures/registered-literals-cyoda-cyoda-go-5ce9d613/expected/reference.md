# Reference
## User, Account
<details><summary><code>client.user_account.<a href="src/fern/user_account/client.py#L27-L51">account_get</a>() -> UserAccountInfoResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch information related to the current user's account, such as legal entity, roles, and current subscription.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_account.account_get()

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

<details><summary><code>client.user_account.<a href="src/fern/user_account/client.py#L53-L79">account_subscriptions_get</a>() -> SubscriptionsResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all subscription details associated with the legal entity of the current user.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_account.account_subscriptions_get()

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

## Entity, Audit
<details><summary><code>client.entity_audit.<a href="src/fern/entity_audit/client.py#L30-L109">search_entity_audit_events</a>(...) -> EntityAuditEventsResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves audit events for a specific entity with cursor-based pagination.
Results are ordered by event utc time (newest first).
Maximum search period is 180 days. Default period is 10 days when one of the boundaries is not defined.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_audit.search_entity_audit_events(
    entity_id="entityId",
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

**entity_id:** `str` — Identifier of the entity to retrieve audit events for
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[typing.Union[SearchEntityAuditEventsRequestEventTypeItem, typing.Sequence[SearchEntityAuditEventsRequestEventTypeItem]]]` — Filter by specific audit event types. If not specified, defaults to all event types except System. Note: Including System events may increase latency and load on the system. Use System events filtering with caution. 
    
</dd>
</dl>

<dl>
<dd>

**severity:** `typing.Optional[SearchEntityAuditEventsRequestSeverity]` — Filter by event severity level
    
</dd>
</dl>

<dl>
<dd>

**from_utc_time:** `typing.Optional[datetime.datetime]` — Filter events from this timestamp (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**to_utc_time:** `typing.Optional[datetime.datetime]` — Filter events until this timestamp (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Filter by transaction identifier
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination. Use the `nextCursor` value from the previous response to fetch the next page of results. Omit for the first page. 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` — Maximum number of audit events to return per page
    
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

<details><summary><code>client.entity_audit.<a href="src/fern/entity_audit/client.py#L111-L152">get_state_machine_finished_event</a>(...) -> StateMachineFinishedDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the StateMachine Finished event for a specific entity and transaction.
This endpoint provides quick access to the workflow outcome for that transaction without needing to
search through all audit events.

Both entityId and transactionId must be valid time-based UUIDs (version 1).
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_audit.get_state_machine_finished_event(
    entity_id="entityId",
    transaction_id="transactionId",
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

**entity_id:** `str` — Identifier of the entity. Must be a valid time-based UUID (version 1). 
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — Identifier of the transaction. Must be a valid time-based UUID (version 1). 
    
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

## User, Machine
<details><summary><code>client.user_machine.<a href="src/fern/user_machine/client.py#L34-L66">list_technical_users</a>() -> typing.List[TechnicalUserDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all active machine-to-machine (M2M) clients (OAuth 2.0 clients) to the current legal entity.
These users authenticate via client credentials and act on behalf of applications, not humans.

Returns the client IDs of all M2M clients that are currently active
and available for authentication.

**Authorization Required:** SUPER_USER role
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_machine.list_technical_users()

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

<details><summary><code>client.user_machine.<a href="src/fern/user_machine/client.py#L68-L108">create_technical_user</a>(...) -> TechnicalUserCredentialsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new machine-to-machine (M2M) client for API authentication via OAuth 2.0.

The created user will have M2M role permissions, necessary for getting the bearer token.

When `withAdminRole` is set to `true`, the M2M client will additionally receive the ADMIN role,
granting it full access to all ADMIN-level endpoints (e.g., trusted key registration).
This requires the `cyoda.security.web.jwt.m2m.admin-role-enabled` feature flag to be enabled;
otherwise, a 401 Unauthorized response is returned.

**Authorization Required:** SUPER_USER role
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_machine.create_technical_user()

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

**with_admin_role:** `typing.Optional[str]` — When true, the created M2M client will additionally receive the ADMIN role. Requires the M2M admin role feature flag to be enabled. 
    
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

<details><summary><code>client.user_machine.<a href="src/fern/user_machine/client.py#L110-L146">delete_technical_user</a>(...) -> DeleteTechnicalUser200ResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a M2M client and invalidates all associated credentials.

This operation cannot be undone without a support ticket. Any applications using this client's
credentials will immediately lose access and must be reconfigured with new credentials.

**Authorization Required:** SUPER_USER role
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_machine.delete_technical_user(
    client_id="clientId",
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

**client_id:** `str` — The client ID of the M2M client to delete
    
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

<details><summary><code>client.user_machine.<a href="src/fern/user_machine/client.py#L148-L184">reset_technical_user_secret</a>(...) -> TechnicalUserCredentialsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a new client secret for an existing M2M client.

This operation invalidates the current client secret and generates a new one.
Any applications using the old secret will need to be updated with the new credentials.

**Authorization Required:** SUPER_USER role
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_machine.reset_technical_user_secret(
    client_id="clientId",
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

**client_id:** `str` — The client ID of the M2M client whose secret should be reset
    
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

<details><summary><code>client.user_machine.<a href="src/fern/user_machine/client.py#L186-L242">get_technical_user_token</a>(...) -> TokenResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authenticates a M2M client and returns an access token.

Supports two grant types:

1. **client_credentials** — Standard OAuth 2.0 Client Credentials Grant for M2M authentication.
2. **urn:ietf:params:oauth:grant-type:token-exchange** — RFC 8693 Token Exchange.
   The M2M client acts on behalf of a user by presenting the user's JWT as `subject_token`.

In both cases the M2M client authenticates via HTTP Basic Authentication
(client_id and client_secret in the Authorization header).

**Note:** This endpoint does not require an existing access token, as it serves as the authentication entry point.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_machine.get_technical_user_token()

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

**grant_type:** `typing.Optional[GetTechnicalUserTokenRequestGrantType]` — The OAuth 2.0 grant type
    
</dd>
</dl>

<dl>
<dd>

**subject_token:** `typing.Optional[str]` — The subject token to exchange
    
</dd>
</dl>

<dl>
<dd>

**subject_token_type:** `typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType]` — The type of the subject token
    
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

## Entity Management
<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L42-L74">get_entity_statistics</a>(...) -> ModelStatsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns statistics for entities grouped by model name and version.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.get_entity_statistics()

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

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L76-L114">get_entity_statistics_by_state</a>(...) -> ModelStateStatsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns statistics for entities grouped by model name, version, and state.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.get_entity_statistics_by_state()

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

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional list of states for which to calculate statistics. If not provided, statistics will be calculated for all current workflow states
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L116-L165">get_entity_statistics_by_state_for_model</a>(...) -> ModelStateStatsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns statistics for entities of a specific model name and version, grouped by state.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.get_entity_statistics_by_state_for_model(
    entity_name="entityName",
    model_version=1,
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

**entity_name:** `str` — Name of the entity model
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version number of the entity model
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional list of states for which to calculate statistics. If not provided, statistics will be calculated for all current workflow states
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L167-L212">get_entity_statistics_for_model</a>(...) -> ModelStatsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns statistics for entities of a specific model name and version.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.get_entity_statistics_for_model(
    entity_name="entityName",
    model_version=1,
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

**entity_name:** `str` — Name of the entity model
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version number of the entity model
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L214-L259">get_one_entity</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single entity by id
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.get_one_entity(
    entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
    transaction_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
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

**entity_id:** `str` — The unique identifier (UUID) of the entity to get
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for loading the entity, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Load the entity as it was at the end of the specified transaction with the given transactionId
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L261-L292">delete_single_entity</a>(...) -> SingleDeleteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single entity by Id
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.delete_single_entity(
    entity_id="123e4567-e89b-12d3-a456-426614174000",
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

**entity_id:** `str` — The unique identifier (UUID) of the entity to delete
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L294-L353">get_entity_changes_metadata</a>(...) -> EntityChangeMeta</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Retrieves the change history metadata for a specific entity.

Returns a stream of metadata records describing each change made to the entity, including:
- Transaction ID that made the change
- Timestamp when the change occurred
- User who made the change
- Type of change (CREATE, UPDATE, DELETE)
- Number of fields changed

Common use cases:
- Audit trail review
- Change tracking
- Compliance reporting
- Debugging entity state changes

Note:
- Changes are returned in chronological order
- The pointInTime parameter allows viewing the change history as it existed at a specific time
        
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.get_entity_changes_metadata(
    entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
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

**entity_id:** `str` — The unique identifier (UUID) of the entity to get change history for
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for loading the entity changes, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L355-L425">get_all_entities</a>(...) -> JsonNode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Retrieves all entities for a given model name and version, with pagination support.
Results are returned as a stream of JSON objects.

Common use cases:
- Bulk data retrieval
- Data migration
- Reporting

Note:
- For large datasets, consider using the search API with snapshots instead.
- To find out how many entities there are, use the entity statistics endpoints.
        
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.get_all_entities(
    entity_name="entityName",
    model_version=1,
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

**entity_name:** `str` — Name of the entity model to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version number of the entity model
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of entities to return per page. Must be greater than 0.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Page number to retrieve, starting from 0. Must be greater than or equal to 0.
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for loading the entities, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L427-L490">delete_entities</a>(...) -> StreamDeleteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes entities for a given model name and version which existed at the consistency time of the system when the request is launched by provided condition or all entities if condition is not provided.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.delete_entities(
    entity_name="nobel-prize",
    model_version=1,
    type="group",
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

**entity_name:** `str` — Name of the entity model to delete
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version number of the entity model
    
</dd>
</dl>

<dl>
<dd>

**request:** `AbstractConditionDto` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_size:** `typing.Optional[int]` — Maximum number of entities to delete in a single transaction. Higher values may improve performance but increase memory usage.
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for selecting the entities for deletion, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the consistency time of the system if not provided.
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — Include the list of deleted entity IDs in the response. When false, only returns statistics.
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L492-L581">create_collection</a>(...) -> EntityTransactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Saves a collection of entities. Each entity can be from a different model and version.

Path Parameters:
- format: The format of the input payload (e.g., JSON, XML)

Request Body:
- A list of CreatePayload objects, each containing entity data and model information
        
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
from fern.entity_management import CreateCollectionRequestFormat

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.create_collection(
    format=CreateCollectionRequestFormat.JSON,
    request={
        "0": {"model": {"name": "family", "version": 1}, "payload": "{\n  \"firstName\" : \"John\",\n  \"middleName\" : \"Henry\",\n  \"lastName\" : \"Doe\",\n  \"birthdate\" : \"1964-04-18\",\n  \"married\" : true,\n  \"children\" : [ {\n    \"firstName\" : \"Jane\",\n    \"middleName\" : \"Marie\",\n    \"lastName\" : \"Doe\",\n    \"birthdate\" : \"1990-08-25\",\n    \"married\" : false\n  }, {\n    \"firstName\" : \"James\",\n    \"middleName\" : \"Robert\",\n    \"lastName\" : \"Doe\",\n    \"birthdate\" : \"1992-03-15\",\n    \"married\" : true\n  } ]\n}"},
        "1": {"model": {"name": "nobel-prize", "version": 1}, "payload": "{\n  \"category\" : \"economics\",\n  \"laureates\" : [ {\n    \"firstname\" : \"Daron\",\n    \"surname\" : \"Acemoglu\",\n    \"id\" : \"1044\",\n    \"motivation\" : \"\\\"for studies of how institutions are formed and affect prosperity\\\"\",\n    \"share\" : \"3\"\n  }, {\n    \"firstname\" : \"Simon\",\n    \"surname\" : \"Johnson\",\n    \"id\" : \"1045\",\n    \"motivation\" : \"\\\"for studies of how institutions are formed and affect prosperity\\\"\",\n    \"share\" : \"3\"\n  }, {\n    \"firstname\" : \"James\",\n    \"surname\" : \"Robinson\",\n    \"id\" : \"1046\",\n    \"motivation\" : \"\\\"for studies of how institutions are formed and affect prosperity\\\"\",\n    \"share\" : \"3\"\n  } ],\n  \"year\" : \"2024\"\n}"}
    },
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

**format:** `CreateCollectionRequestFormat` — Format of the input payload
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_window:** `typing.Optional[int]` 

Maximum number of entities per transactional batch. Default 100,
maximum 1000; values outside (0, 1000] are rejected with 400
BAD_REQUEST. Collections exceeding the window are split into
multiple transactional batches committed sequentially. The
response is an array with one element per chunk in commit order;
chunks committed before any later failure remain durable.
    
</dd>
</dl>

<dl>
<dd>

**transaction_timeout_millis:** `typing.Optional[int]` 

Maximum time in milliseconds allowed for transaction completion.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
</dd>
</dl>

<dl>
<dd>

**wait_for_consistency_after:** `typing.Optional[bool]` 

If true, waits for consistency after operation completes.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L583-L672">update_collection</a>(...) -> EntityTransactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Updates a collection of entities. If any of the entities are not found,
the request will fail and no entities will be updated.
        
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
from fern.entity_management import UpdateCollectionRequestFormat, UpdateCollectionRequestBodyItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.update_collection(
    format=UpdateCollectionRequestFormat.JSON,
    request=[
        UpdateCollectionRequestBodyItem(
            id="8824c480-c166-11ee-9e63-ae468cd3ed16",
            payload="{\n  \"firstName\" : \"John\",\n  \"middleName\" : \"Henry\",\n  \"lastName\" : \"Doe\",\n  \"birthdate\" : \"1964-04-18\",\n  \"married\" : true,\n  \"children\" : [ {\n    \"firstName\" : \"Jane\",\n    \"middleName\" : \"Marie\",\n    \"lastName\" : \"Doe\",\n    \"birthdate\" : \"1990-08-25\",\n    \"married\" : false\n  }, {\n    \"firstName\" : \"James\",\n    \"middleName\" : \"Robert\",\n    \"lastName\" : \"Doe\",\n    \"birthdate\" : \"1992-03-15\",\n    \"married\" : true\n  } ]\n}",
            transition="UPDATE",
        ),
        UpdateCollectionRequestBodyItem(
            id="31134900-d9cb-11ee-9e63-ae468cd3ed16",
            payload="{\n  \"category\" : \"economics\",\n  \"laureates\" : [ {\n    \"firstname\" : \"Daron\",\n    \"surname\" : \"Acemoglu\",\n    \"id\" : \"1044\",\n    \"motivation\" : \"\\\"for studies of how institutions are formed and affect prosperity\\\"\",\n    \"share\" : \"3\"\n  }, {\n    \"firstname\" : \"Simon\",\n    \"surname\" : \"Johnson\",\n    \"id\" : \"1045\",\n    \"motivation\" : \"\\\"for studies of how institutions are formed and affect prosperity\\\"\",\n    \"share\" : \"3\"\n  }, {\n    \"firstname\" : \"James\",\n    \"surname\" : \"Robinson\",\n    \"id\" : \"1046\",\n    \"motivation\" : \"\\\"for studies of how institutions are formed and affect prosperity\\\"\",\n    \"share\" : \"3\"\n  } ],\n  \"year\" : \"2024\"\n}",
            transition="UPDATE",
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

**format:** `UpdateCollectionRequestFormat` — Format of the input payload
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[UpdateCollectionRequestBodyItem]` 

Array of update items. Each item carries the entity's UUID,
a JSON-encoded `payload` string, an optional named
`transition`, and an optional `ifMatch` cross-request
precondition (cyoda-go extension #228; not yet in Cloud).
    
</dd>
</dl>

<dl>
<dd>

**transaction_window:** `typing.Optional[int]` 

Maximum number of entities per transactional batch. Default 100,
maximum 1000; values outside (0, 1000] are rejected with 400
BAD_REQUEST. Collections exceeding the window are split into
multiple transactional batches committed sequentially. The
response is an array with one element per chunk in commit order;
chunks committed before any later failure remain durable.
    
</dd>
</dl>

<dl>
<dd>

**transaction_timeout_millis:** `typing.Optional[int]` 

Maximum time in milliseconds allowed for transaction completion.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
</dd>
</dl>

<dl>
<dd>

**wait_for_consistency_after:** `typing.Optional[bool]` 

If true, waits for consistency after operation completes.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L674-L778">update_single_with_loopback</a>(...) -> EntityTransactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Updates a single entity with a loopback transition.

Path Parameters:
- format: The format of the input payload (e.g., JSON, XML)
- entityId: The UUID of the entity to update

Request Body:
- Entity data in the specified format
            
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
from fern.entity_management import UpdateSingleWithLoopbackRequestFormat

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.update_single_with_loopback(
    format=UpdateSingleWithLoopbackRequestFormat.JSON,
    entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
    request={
        "category": "physics",
        "laureates": [{"firstname": "John", "surname": "Hopfield", "id": "1037", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}, {"firstname": "Geoffrey", "surname": "Hinton", "id": "1038", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}],
        "year": "2024"
    },
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

**format:** `UpdateSingleWithLoopbackRequestFormat` — Format of the input payload
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` — The unique identifier (UUID) of the entity to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_timeout_millis:** `typing.Optional[int]` 

Maximum time in milliseconds allowed for transaction completion.
Operation will fail if it takes longer than this timeout.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
</dd>
</dl>

<dl>
<dd>

**wait_for_consistency_after:** `typing.Optional[bool]` 

If true, waits for the consistency time to pass before responding.
May increase response time but guarantees data consistency when
returning, so that subsequent calls will see the updated data.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — Transaction ID of the entity version the client last read. If the entity has been modified since, returns 412 Precondition Failed.
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L780-L891">update_single</a>(...) -> EntityTransactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Updates a single entity.

Path Parameters:
- format: The format of the input payload (e.g., JSON, XML)
- entityId: The UUID of the entity to update
- transition: The transition to apply to the entity

Request Body:
- Entity data in the specified format
            
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
from fern.entity_management import UpdateSingleRequestFormat

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.update_single(
    format=UpdateSingleRequestFormat.JSON,
    entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
    transition="UPDATE",
    request={
        "category": "physics",
        "laureates": [{"firstname": "John", "surname": "Hopfield", "id": "1037", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}, {"firstname": "Geoffrey", "surname": "Hinton", "id": "1038", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}],
        "year": "2024"
    },
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

**format:** `UpdateSingleRequestFormat` — Format of the input payload
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` — The unique identifier (UUID) of the entity to update
    
</dd>
</dl>

<dl>
<dd>

**transition:** `str` — The transition state to apply to the entity (e.g., 'UPDATE', 'PUBLISH')
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_timeout_millis:** `typing.Optional[int]` 

Maximum time in milliseconds allowed for transaction completion.
Operation will fail if it takes longer than this timeout.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
</dd>
</dl>

<dl>
<dd>

**wait_for_consistency_after:** `typing.Optional[bool]` 

If true, waits for the consistency time to pass before responding.
May increase response time but guarantees data consistency when
returning, so that subsequent calls will see the updated data.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — Transaction ID of the entity version the client last read. If the entity has been modified since, returns 412 Precondition Failed.
    
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

<details><summary><code>client.entity_management.<a href="src/fern/entity_management/client.py#L893-L1008">create</a>(...) -> EntityTransactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Saves a new entity or a collection of entities of the same type.

Path Parameters:
* format: The format of the input payload (e.g., JSON, XML)
* entityName: The name of the entity model
* modelVersion: The version number of the entity model

Request Body:
- A string containing the entity data in the specified format
        
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
from fern.entity_management import CreateRequestFormat

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_management.create(
    format=CreateRequestFormat.JSON,
    entity_name="entityName",
    model_version=1,
    request={
        "category": "physics",
        "laureates": [{"firstname": "John", "surname": "Hopfield", "id": "1037", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}, {"firstname": "Geoffrey", "surname": "Hinton", "id": "1038", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}],
        "year": "2024"
    },
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

**format:** `CreateRequestFormat` — Format of the input payload
    
</dd>
</dl>

<dl>
<dd>

**entity_name:** `str` — Name of the entity model
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version number of the entity model
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_window:** `typing.Optional[int]` 

Maximum number of entities per transactional batch. Applies only
when the request body is a JSON array; ignored for single-object
bodies. Default 100, maximum 1000; values outside (0, 1000] are
rejected with 400 BAD_REQUEST. Array bodies exceeding the window
are split into multiple transactional batches committed
sequentially. The response is then an array with one element per
chunk in commit order; chunks committed before any later failure
remain durable.
    
</dd>
</dl>

<dl>
<dd>

**transaction_timeout_millis:** `typing.Optional[int]` 

Maximum time in milliseconds for transaction completion.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
</dd>
</dl>

<dl>
<dd>

**wait_for_consistency_after:** `typing.Optional[bool]` 

If true, waits for consistency after the operation completes.
Accepted for Cyoda Cloud API parity. Behavior is
storage-engine-plugin dependent — not every plugin honors this
field; consult the runtime plugin's documentation for the
supported behavior.
    
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

## EdgeMessage
<details><summary><code>client.edge_message.<a href="src/fern/edge_message/client.py#L30-L69">delete_messages</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes multiple stored edge messages using their unique identifiers, including the associated payload blobs. Messages are deleted in batches according to the specified transaction size.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.edge_message.delete_messages(
    request="string",
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

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_size:** `typing.Optional[int]` — Number of messages to delete per transaction batch
    
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

<details><summary><code>client.edge_message.<a href="src/fern/edge_message/client.py#L71-L143">new_message</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates and stores a new edge message with the provided payload and AMQP-aligned headers. The message is processed according to the specified parsing configuration and stored with a unique identifier.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.edge_message.new_message(
    subject="subject",
    request="string",
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

**subject:** `str` — Message subject identifier
    
</dd>
</dl>

<dl>
<dd>

**content_encoding:** `typing.Literal` — Character encoding of the payload
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_timeout_millis:** `typing.Optional[int]` — Maximum time in milliseconds to wait for transaction completion
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `typing.Optional[str]` — Custom message identifier
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — ID of the message sender
    
</dd>
</dl>

<dl>
<dd>

**recipient:** `typing.Optional[str]` — Intended message recipient
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Reply-to address for responses
    
</dd>
</dl>

<dl>
<dd>

**correlation_id:** `typing.Optional[str]` — Correlation ID for message tracking
    
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

<details><summary><code>client.edge_message.<a href="src/fern/edge_message/client.py#L145-L176">get_message</a>(...) -> EdgeMessageDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a stored edge message using its unique identifier, including all message metadata and payload
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.edge_message.get_message(
    message_id="825ba31c-0b5b-11f0-91f5-667325248341",
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

**message_id:** `str` — Unique identifier of the message to retrieve
    
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

<details><summary><code>client.edge_message.<a href="src/fern/edge_message/client.py#L178-L209">delete_message</a>(...) -> EntityTransactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a stored edge message using its unique identifier, including the associated payload blob
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.edge_message.delete_message(
    message_id="825ba31c-0b5b-11f0-91f5-667325248341",
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

**message_id:** `str` — Unique identifier of the message to delete
    
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

## Entity model
<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L34-L65">get_available_entity_models</a>() -> EntityModelDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Retrieves a list of all available entity models in the system.

Each model in the response includes its identifier, name, version,
current state (LOCKED/UNLOCKED), and last modification timestamp.

Paging and searching are not yet supported.
        
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.get_available_entity_models()

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

<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L67-L126">export_metadata</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Exports an entity model's metadata in the specified format.

Path Parameters:
- converter: The format to export to (e.g., JSON_SCHEMA, SIMPLE_VIEW)
- entityName: The name of the entity model to export
- modelVersion: The version number of the model

The response format depends on the chosen converter:
- JSON_SCHEMA: Returns a JSON Schema representation
- SIMPLE_VIEW: Returns a simplified view of the model structure
        
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
from fern.entity_model import ExportMetadataRequestConverter

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.export_metadata(
    converter=ExportMetadataRequestConverter.JSON_SCHEMA,
    entity_name="nobel-prize",
    model_version=1,
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

**converter:** `ExportMetadataRequestConverter` — The type converter to use
    
</dd>
</dl>

<dl>
<dd>

**entity_name:** `str` — The model name of the entity
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — The model version
    
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

<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L128-L217">import_entity_model</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Imports or updates an entity model from the provided data.

Path Parameters:
- dataFormat: The format of the input data (e.g., JSON, XML)
- converter: The type converter to use for processing the data (SAMPLE_DATA, JSON_SCHEMA, SIMPLE_VIEW)
- entityName: The name for the entity model
- modelVersion: The version number for the model

Returns the UUID of the created/updated entity model.
        
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
from fern.entity_model import ImportEntityModelRequestDataFormat, ImportEntityModelRequestConverter

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.import_entity_model(
    data_format=ImportEntityModelRequestDataFormat.JSON,
    converter=ImportEntityModelRequestConverter.SAMPLE_DATA,
    entity_name="nobel-prize",
    model_version=1,
    request={
        "category": "physics",
        "laureates": [{"firstname": "John", "surname": "Hopfield", "id": "1037", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}, {"firstname": "Geoffrey", "surname": "Hinton", "id": "1038", "motivation": "\"for foundational discoveries and inventions that enable machine learning with artificial neural networks\"", "share": "2"}],
        "year": "2024"
    },
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

**data_format:** `ImportEntityModelRequestDataFormat` — The format of the input data
    
</dd>
</dl>

<dl>
<dd>

**converter:** `ImportEntityModelRequestConverter` — The type converter to use for processing the data
    
</dd>
</dl>

<dl>
<dd>

**entity_name:** `str` — The model name of the entity
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — The version number for the model
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L219-L264">validate_entity_model</a>(...) -> EntityModelActionResultDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a JSON payload against the entity model's discovered schema. Returns whether the data conforms to the model.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.validate_entity_model(
    entity_name="entityName",
    model_version=1,
    request={
        "key": "value"
    },
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

**entity_name:** `str` — Name of the entity model
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version of the entity model
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L266-L312">delete_entity_model</a>(...) -> EntityModelActionResultDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Deletes an entity model if it meets deletion criteria.

Requirements for deletion:
- Model must be in UNLOCKED state
- No entities can reference this model in the database

Path Parameters:
- entityName: The name of the entity model to delete
- modelVersion: The version number of the model

Returns a confirmation message upon successful deletion.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.delete_entity_model(
    entity_name="nobel-prize",
    model_version=1,
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

**entity_name:** `str` — The model name of the entity
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — The version number of the model
    
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

<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L314-L381">set_entity_model_change_level</a>(...) -> EntityModelActionResultDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Sets or updates the allowed change level for a locked entity model.

Path Parameters:
- entityName: The name of the entity model
- modelVersion: The version number of the model
- changeLevel: The desired change level (ARRAY_LENGTH, ARRAY_ELEMENTS, TYPE, STRUCTURAL) or null to disallow changes

Change levels are hierarchical - allowing a specific level automatically allows all less impactful levels:
1. ARRAY_LENGTH: Only permits increases in UniTypeArray width
2. ARRAY_ELEMENTS: Allows MultiTypeArray changes without new types
3. TYPE: Permits modifications to existing types
4. STRUCTURAL: Allows fundamental model changes

Note: Setting a change level is only meaningful for locked models. An unlocked model always allows all changes.
        
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
from fern.entity_model import SetEntityModelChangeLevelRequestChangeLevel

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.set_entity_model_change_level(
    entity_name="nobel-prize",
    model_version=1,
    change_level=SetEntityModelChangeLevelRequestChangeLevel.ARRAY_LENGTH,
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

**entity_name:** `str` — The model name of the entity
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — The version number of the model
    
</dd>
</dl>

<dl>
<dd>

**change_level:** `SetEntityModelChangeLevelRequestChangeLevel` 


The allowed change level for the model.
Set to null to disallow all changes.
Valid values: ARRAY_LENGTH, ARRAY_ELEMENTS, TYPE, STRUCTURAL
            
    
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

<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L383-L427">lock_entity_model</a>(...) -> EntityModelActionResultDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Locks an entity model to prevent further modifications.

Path Parameters:
- entityName: The name of the entity model to lock
- modelVersion: The version number of the model

Returns a confirmation message upon successful locking.
Once locked, a model cannot be modified unless explicitly unlocked or a change level is set.
        
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.lock_entity_model(
    entity_name="nobel-prize",
    model_version=1,
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

**entity_name:** `str` — The model name of the entity
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — The version number of the model
    
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

<details><summary><code>client.entity_model.<a href="src/fern/entity_model/client.py#L429-L476">unlock_entity_model</a>(...) -> EntityModelActionResultDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Attempts to unlock a locked entity model.

Requirements for unlocking:
- No entities can reference this model in the database
- Model must be in LOCKED state

Path Parameters:
- entityName: The name of the entity model to unlock
- modelVersion: The version number of the model

The operation will fail if there are any entities in the database using this model.
        
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model.unlock_entity_model(
    entity_name="nobel-prize",
    model_version=1,
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

**entity_name:** `str` — The model name of the entity
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — The version number of the model
    
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

## Entity Model, Workflow
<details><summary><code>client.entity_model_workflow.<a href="src/fern/entity_model_workflow/client.py#L31-L71">export_entity_model_workflow</a>(...) -> WorkflowExportResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports all workflow configurations for a specific entity type.

Since one entity type can have multiple workflows (selected by workflow-level conditions),
this endpoint returns a collection of all workflows configured for the entity type.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model_workflow.export_entity_model_workflow(
    entity_name="entityName",
    model_version=1,
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

**entity_name:** `str` — Name of the entity model
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version of the entity model
    
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

<details><summary><code>client.entity_model_workflow.<a href="src/fern/entity_model_workflow/client.py#L73-L135">import_entity_model_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Imports or updates workflow configurations for a specific entity type.

Since workflow name must be unique per entity model, this endpoint will either create
new workflow or update existing workflow with the same name.

The workflow configuration structure is defined by versioned schemas and may vary
depending on the version specified in the configuration.
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
from fern import FernApi, WorkflowConfigurationDto, StateDefinitionDto
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.entity_model_workflow.import_entity_model_workflow(
    entity_name="entityName",
    model_version=1,
    workflows=[
        WorkflowConfigurationDto(
            version="version",
            name="name",
            initial_state="initialState",
            states={
                "key": StateDefinitionDto()
            },
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

**entity_name:** `str` — Name of the entity model
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version of the entity model
    
</dd>
</dl>

<dl>
<dd>

**workflows:** `typing.List[WorkflowConfigurationDto]` — Array of workflow configurations to import
    
</dd>
</dl>

<dl>
<dd>

**import_mode:** `typing.Optional[WorkflowImportRequestDtoImportMode]` — Import mode for handling existing workflows
    
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

## OAuth, Keys
<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L35-L102">issue_jwt_key_pair</a>(...) -> JwtKeyPairResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates and stores a new asymmetric key-pair (public/private) for signing and validating OAuth 2.0 JWT
access tokens.
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
from fern.o_auth_keys import IssueJwtKeyPairRequestDtoAudience, IssueJwtKeyPairRequestDtoAlgorithm

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.issue_jwt_key_pair(
    audience=IssueJwtKeyPairRequestDtoAudience.HUMAN,
    algorithm=IssueJwtKeyPairRequestDtoAlgorithm.RS256,
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

**audience:** `IssueJwtKeyPairRequestDtoAudience` 
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `IssueJwtKeyPairRequestDtoAlgorithm` 
    
</dd>
</dl>

<dl>
<dd>

**valid_from:** `typing.Optional[datetime.datetime]` — When the key-pair becomes valid. Defaults to current date-time if not specified.
    
</dd>
</dl>

<dl>
<dd>

**valid_to:** `typing.Optional[datetime.datetime]` — When the key-pair expires. Defaults to validFrom + <configured validity, default is 365 days> if not specified.
    
</dd>
</dl>

<dl>
<dd>

**invalidate_current:** `typing.Optional[bool]` — If true, invalidates the currently active key-pair for this audience.
    
</dd>
</dl>

<dl>
<dd>

**invalidate_grace_period_sec:** `typing.Optional[int]` — Number of seconds to keep the old key valid after invalidation. Only applicable when invalidateCurrent is true.
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L104-L136">get_current_jwt_key_pair</a>(...) -> JwtKeyPairResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves information about the currently active JWT signing key-pair for the specified audience.
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
from fern.o_auth_keys import GetCurrentJwtKeyPairRequestAudience

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.get_current_jwt_key_pair(
    audience=GetCurrentJwtKeyPairRequestAudience.HUMAN,
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

**audience:** `GetCurrentJwtKeyPairRequestAudience` 
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L138-L167">delete_jwt_key_pair</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a JWT signing key-pair. The key will first be invalidated (if not already)
and then removed from storage.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.delete_jwt_key_pair(
    key_id="keyId",
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

**key_id:** `str` — The unique identifier (kid) of the key-pair to delete
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L169-L210">invalidate_jwt_key_pair</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidates a specific JWT signing key-pair.
After invalidation, the key will no longer be used for signing new tokens,
and existing tokens signed with this key pair would not be accepted.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.invalidate_jwt_key_pair(
    key_id="keyId",
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

**key_id:** `str` — The unique identifier (kid) of the key-pair to invalidate
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvalidateKeyRequestDto` 
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L212-L245">reactivate_jwt_key_pair</a>(...) -> JwtKeyPairResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reactivates a previously invalidated JWT signing key-pair.
This allows the key to be used for signing and validating tokens again.
This operation is idempotent - if the key-pair is already active, it returns the current state.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.reactivate_jwt_key_pair(
    key_id="keyId",
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

**key_id:** `str` — The unique identifier (kid) of the key-pair to reactivate
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L247-L274">list_trusted_keys</a>() -> typing.List[TrustedKeyResponseDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all trusted public keys registered for the caller's tenant.
Requires ADMIN or SUPER_USER role.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.list_trusted_keys()

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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L276-L365">register_trusted_key</a>(...) -> TrustedKeyResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a pre-shared public key for JWT validation. This enables external applications
to sign user JWTs that Cyoda can verify without requiring a reachable OIDC discovery endpoint.
The key is bound to the caller's tenant (legalEntityId).

If a key with the same `keyId` already exists and belongs to the caller's tenant, it is
replaced atomically (upsert semantics). This makes the endpoint retry-safe during key
rotation — a retried request after a partial failure will succeed rather than conflict.
If the key belongs to a different tenant, the request is rejected with `409 Conflict`.

Use `invalidatePrevious` to retire all other active trusted keys for this tenant
in a single atomic operation, with an optional grace period (`invalidateGracePeriodSec`)
during which the old keys continue to be accepted.

Requires ADMIN or SUPER_USER role. Disabled by default — enable via
`cyoda.security.web.iam.trustedKeyRegistrationEnabled`.
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
from fern.o_auth_keys import RegisterTrustedKeyRequestDtoAudience

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.register_trusted_key(
    key_id="my-app-key-1",
    jwk={
        "key": {
            "key": "value"
        }
    },
    audience=RegisterTrustedKeyRequestDtoAudience.HUMAN,
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

**key_id:** `str` — Unique key identifier. Will be matched against the `kid` header in JWTs.
    
</dd>
</dl>

<dl>
<dd>

**jwk:** `typing.Dict[str, typing.Dict[str, typing.Any]]` — A JSON Web Key (JWK) as defined in RFC 7517. Must contain the public key components only. Supported key types: RSA (`kty: "RSA"`), EC (`kty: "EC"`), and OKP/EdDSA (`kty: "OKP"`). See RFC 7517, RFC 7518, and RFC 8037 for field definitions. 
    
</dd>
</dl>

<dl>
<dd>

**audience:** `RegisterTrustedKeyRequestDtoAudience` 
    
</dd>
</dl>

<dl>
<dd>

**issuers:** `typing.Optional[typing.List[str]]` — List of allowed issuer URIs. When this parameter is configured, the JWT must contain an iss claim, and its value must match one of the entries in this list. 
    
</dd>
</dl>

<dl>
<dd>

**valid_from:** `typing.Optional[datetime.datetime]` — When the key becomes valid. Defaults to current time if not specified. 
    
</dd>
</dl>

<dl>
<dd>

**valid_to:** `typing.Optional[datetime.datetime]` — When the key expires. Defaults to the system-configured maximum validity. 
    
</dd>
</dl>

<dl>
<dd>

**invalidate_previous:** `typing.Optional[bool]` — If true, invalidates all other keys for the same audience belonging to the caller's tenant. Enables atomic key rotation. 
    
</dd>
</dl>

<dl>
<dd>

**invalidate_grace_period_sec:** `typing.Optional[int]` — Grace period in seconds for invalidating previous keys (only used when invalidatePrevious is true). Default is 0 (immediate invalidation). 
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L367-L396">delete_trusted_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a registered trusted public key. The key must belong to the caller's tenant.
Requires ADMIN or SUPER_USER role.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.delete_trusted_key(
    key_id="keyId",
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

**key_id:** `str` — The key ID of the trusted key to delete
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L398-L439">invalidate_trusted_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidates a registered trusted public key. After invalidation, JWTs signed with the
corresponding private key will no longer be accepted for validation (after the grace period).
Requires ADMIN or SUPER_USER role.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.invalidate_trusted_key(
    key_id="keyId",
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

**key_id:** `str` — The key ID of the trusted key to invalidate
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvalidateKeyRequestDto` 
    
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

<details><summary><code>client.o_auth_keys.<a href="src/fern/o_auth_keys/client.py#L441-L478">reactivate_trusted_key</a>(...) -> TrustedKeyResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reactivates a previously invalidated trusted public key, allowing JWTs signed with it to
be accepted again. This operation is idempotent.
Requires ADMIN or SUPER_USER role.

**Important**: Reactivation removes the key's expiration entirely (`validTo` is cleared to null),
regardless of the original `validTo` value the key was registered with. The key will remain valid
indefinitely until explicitly invalidated or deleted again.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_keys.reactivate_trusted_key(
    key_id="keyId",
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

**key_id:** `str` — The key ID of the trusted key to reactivate
    
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

## OAuth, OIDC Providers
<details><summary><code>client.o_auth_oidc_providers.<a href="src/fern/o_auth_oidc_providers/client.py#L29-L58">list_oidc_providers</a>(...) -> typing.List[OidcProviderResponseDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all registered OIDC providers, including both active and inactive providers.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_oidc_providers.list_oidc_providers()

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

**active_only:** `typing.Optional[str]` — If true, returns only active providers
    
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

<details><summary><code>client.o_auth_oidc_providers.<a href="src/fern/o_auth_oidc_providers/client.py#L60-L101">register_oidc_provider</a>(...) -> OidcProviderResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a new external OIDC provider for JWT validation. The provider's public keys will be
discovered from the well-known configuration endpoint and used to validate JWT tokens.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_oidc_providers.register_oidc_provider(
    well_known_config_uri="https://oidc-domain.local/.well-known/openid-configuration",
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

**well_known_config_uri:** `str` — URI to the OIDC provider's well-known configuration endpoint
    
</dd>
</dl>

<dl>
<dd>

**issuers:** `typing.Optional[typing.List[str]]` — Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped. 
    
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

<details><summary><code>client.o_auth_oidc_providers.<a href="src/fern/o_auth_oidc_providers/client.py#L103-L135">reload_oidc_providers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reloads all active OIDC provider configurations from the database and synchronizes
cached keys with the remote JWKS endpoints.

Key synchronization: For each provider, this operation fetches the current keys from
the remote JWKS endpoint and invalidates any locally cached keys that no longer exist
in the remote JWKS. This is useful for security when OIDC providers have rotated or
revoked keys.

This operation is useful when you want to ensure all nodes have the latest OIDC provider
configurations and that any revoked keys are no longer trusted.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_oidc_providers.reload_oidc_providers()

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

<details><summary><code>client.o_auth_oidc_providers.<a href="src/fern/o_auth_oidc_providers/client.py#L137-L166">delete_oidc_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an OIDC provider and all its associated JWK keys.
The provider will first be invalidated (if not already) and then removed from storage.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_oidc_providers.delete_oidc_provider(
    id="id",
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

**id:** `str` — The ID of the OIDC provider to delete
    
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

<details><summary><code>client.o_auth_oidc_providers.<a href="src/fern/o_auth_oidc_providers/client.py#L168-L211">update_oidc_provider</a>(...) -> OidcProviderResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates configuration for an OIDC provider.

Note: Updating the issuers list immediately deletes all cached keys for this provider.
This ensures that JWTs from issuers that are no longer trusted cannot be validated using
previously cached keys. The keys will be re-fetched from the remote JWKS endpoint with the
new issuer configuration when they are next needed for JWT validation.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_oidc_providers.update_oidc_provider(
    id="id",
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

**id:** `str` — The ID of the OIDC provider
    
</dd>
</dl>

<dl>
<dd>

**issuers:** `typing.Optional[typing.List[str]]` — Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped. 
    
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

<details><summary><code>client.o_auth_oidc_providers.<a href="src/fern/o_auth_oidc_providers/client.py#L213-L243">invalidate_oidc_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidates an OIDC provider, marking it as inactive and invalidating all loaded public keys
associated with this provider. The provider configuration is retained but will no longer be
used for JWT validation.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_oidc_providers.invalidate_oidc_provider(
    id="id",
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

**id:** `str` — The ID of the OIDC provider to invalidate
    
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

<details><summary><code>client.o_auth_oidc_providers.<a href="src/fern/o_auth_oidc_providers/client.py#L245-L287">reactivate_oidc_provider</a>(...) -> OidcProviderResponseDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reactivates a previously invalidated OIDC provider. The provider will be marked as active
and can be used for JWT validation again.
This operation is idempotent - if the provider is already active, it returns the current state.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth_oidc_providers.reactivate_oidc_provider(
    id="id",
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

**id:** `str` — The ID of the OIDC provider to reactivate
    
</dd>
</dl>

<dl>
<dd>

**reactivate_keys:** `typing.Optional[bool]` — If true, also reactivates all related JWK keys that were invalidated with this provider
    
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

## Stream Data
<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L38-L69">get_stream_data_config</a>(...) -> StreamDataConfigDef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific stream data configuration by its UUID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.get_stream_data_config(
    config_id="configId",
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

**config_id:** `str` — UUID of the configuration to retrieve
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L71-L125">save_stream_data_config</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates and persists a new stream data configuration definition.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.save_stream_data_config()

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

**request:** `StreamDataConfigDef` 
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L127-L180">update_stream_data_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing stream data configuration definition.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.update_stream_data_config()

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

**request:** `StreamDataConfigDef` 
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L182-L212">delete_stream_data_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a stream data configuration by its UUID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.delete_stream_data_config(
    config_id="configId",
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

**config_id:** `str` — UUID of the configuration to delete
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L214-L240">get_all_configs</a>() -> typing.List[StreamDataConfigDef]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all available stream data configurations.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.get_all_configs()

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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L242-L292">delete</a>(...) -> StreamDataDeleteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes entities matching the stream data request criteria.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.delete()

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

**request:** `StreamDataRequest` 
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L294-L318">export_all1</a>() -> StreamDataConfigDefContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports all stream data configurations as a container for backup or transfer.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.export_all1()

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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L320-L351">export_all</a>(...) -> StreamDataConfigDefContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports all stream data configurations associated with a specific entity class.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.export_all(
    entity_class="com.example.MyEntity",
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

**entity_class:** `str` — Fully qualified class name of the entity
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L353-L387">export_by_ids</a>(...) -> StreamDataConfigDefContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports specific stream data configurations identified by their UUIDs.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.export_by_ids(
    include_ids=[
        "includeIds"
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

**include_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of configuration UUIDs to export
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L389-L439">get_stream_data</a>(...) -> StreamDataFetchResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves paginated stream data based on the provided request definition, including conditions, columns, and pagination parameters.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.get_stream_data()

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

**request:** `StreamDataRequest` 
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L441-L477">import_container</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Imports stream data configurations from a container. Can optionally fail if configurations already exist.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.import_container()

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

**request:** `StreamDataConfigDefContainer` 
    
</dd>
</dl>

<dl>
<dd>

**fail_on_exists:** `typing.Optional[bool]` — If true, fail when a configuration already exists; if false, skip existing configurations
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L479-L510">get_indexs</a>(...) -> typing.List[IndexConfigurationDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all index configurations available for the specified entity class.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.get_indexs(
    entity_class="com.example.MyEntity",
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

**entity_class:** `str` — Fully qualified class name of the entity
    
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

<details><summary><code>client.stream_data.<a href="src/fern/stream_data/client.py#L512-L548">get_query_plan</a>(...) -> QueryPlanDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the original and optimized query execution plan for the given entity class, condition, and alias definitions.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stream_data.get_query_plan()

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

**condition:** `typing.Optional[AbstractCondition]` 
    
</dd>
</dl>

<dl>
<dd>

**alias_defs:** `typing.Optional[typing.List[ReportAliasDef]]` 
    
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

## CQL Execution Statistics
<details><summary><code>client.cql_execution_statistics.<a href="src/fern/cql_execution_statistics/client.py#L26-L50">get_all</a>() -> typing.List[TableTimeStatsDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns detailed execution statistics for all tracked tables, including per-operation breakdowns and minute-by-minute statistics.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cql_execution_statistics.get_all()

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

<details><summary><code>client.cql_execution_statistics.<a href="src/fern/cql_execution_statistics/client.py#L52-L78">get_all_brief</a>() -> typing.List[TableTimeStatsDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary execution statistics for all tracked tables without per-operation or minute-level details.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cql_execution_statistics.get_all_brief()

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

<details><summary><code>client.cql_execution_statistics.<a href="src/fern/cql_execution_statistics/client.py#L80-L103">clear</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clears all accumulated CQL execution statistics for all tables. This operation cannot be undone.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cql_execution_statistics.clear()

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

<details><summary><code>client.cql_execution_statistics.<a href="src/fern/cql_execution_statistics/client.py#L105-L134">get_table</a>(...) -> TableTimeStatsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns detailed execution statistics for a specific Cassandra table, including timing distributions and operation breakdowns.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cql_execution_statistics.get_table(
    table="ENTITY_DATA",
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

**table:** `str` — Name of the Cassandra table, case sensitive, including quotes if needed
    
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

<details><summary><code>client.cql_execution_statistics.<a href="src/fern/cql_execution_statistics/client.py#L136-L160">get_tables</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a sorted list of all Cassandra table names that have execution statistics tracked.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cql_execution_statistics.get_tables()

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

## Search
<details><summary><code>client.search.<a href="src/fern/search/client.py#L35-L143">submit_async_search_job</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous search job for creating a persistent search result set for large datasets.

This endpoint initiates an asynchronous search operation that:
1. Validates the search criteria against the specified entity model
2. Creates a persistent search result set of matching entities
3. Returns a UUID that can be used to:
   - Monitor the search job progress (/search/async/{jobId}/status)
   - Retrieve paginated results (/search/async/{jobId})
   - Cancel the search job if needed (/search/async/{jobId}/cancel)

Search jobs are temporary and have a limited lifetime:
- Each search job has an automatic expiration date
- Expired search jobs are automatically deleted by the system
- The expiration date can be retrieved using GET /search/async/{jobId}/status
- Plan to retrieve your data before the search job expires

The search job runs in the background, allowing handling of large datasets
without timeout concerns.

If no request body is provided or an empty request body is sent, all entities of the specified model and version will be included in the search results.

Query Structure:
The search condition is a tree of predicates that can include:
1. Simple conditions - search within entity data using JSONPath
2. Lifecycle conditions - search based on entity lifecycle (state, creationDate, previousTransition)
3. Group conditions - combine multiple conditions with AND/OR operators

Operator Types (Predicates)
Available Operations:

1. Basic Comparison
- EQUALS: Exact match
- NOT_EQUAL: Non-matching values
- IS_NULL, NOT_NULL: Null checks
- GREATER_THAN, LESS_THAN: Numeric/date comparisons
- GREATER_OR_EQUAL, LESS_OR_EQUAL: Inclusive comparisons
- BETWEEN, BETWEEN_INCLUSIVE: Range checks

2. String Operations (Case-Sensitive)
- CONTAINS: Substring match
- NOT_CONTAINS: Negative substring match
- STARTS_WITH, NOT_STARTS_WITH: Prefix matching
- ENDS_WITH, NOT_ENDS_WITH: Suffix matching
- MATCHES_PATTERN: Regular expression match
- LIKE: SQL-style pattern matching

3. Case-Insensitive String Operations
- IEQUALS, INOT_EQUAL: Case-insensitive equality
- ICONTAINS, INOT_CONTAINS: Case-insensitive substring
- ISTARTS_WITH, INOT_STARTS_WITH: Case-insensitive prefix
- IENDS_WITH, INOT_ENDS_WITH: Case-insensitive suffix

4. State Tracking
- IS_UNCHANGED: Field hasn't changed
- IS_CHANGED: Field has changed
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
from fern import FernApi, ArrayConditionDto, ArrayConditionDtoOperatorType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.submit_async_search_job(
    entity_name="entityName",
    model_version=1,
    request=ArrayConditionDto(
        type="type",
        json_path="jsonPath",
        operator_type=ArrayConditionDtoOperatorType.EQUALS,
        value=[
            "value"
        ],
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

**entity_name:** `str` — Name of the entity model to search
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version of the entity model
    
</dd>
</dl>

<dl>
<dd>

**request:** `SubmitAsyncSearchJobRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for the report, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided. 
    
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

<details><summary><code>client.search.<a href="src/fern/search/client.py#L145-L205">get_async_search_results</a>(...) -> PagedEntityResultsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a page of results from a previously submitted async search job.
To find out how many entities were found, call the search job status endpoint.

By default results are ordered by entity id ascending. Pass one or more `sort` keys to order by scalar data or meta fields; entity id is always the final tiebreaker.

The results are returned in a paginated format, with:
- Configurable page size (default: 10)
- Zero-based page numbering
- Optional point-in-time specification for the data being retrieved
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.get_async_search_results(
    job_id="jobId",
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

**job_id:** `str` — UUID of the search job to retrieve results from
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[str]` — Zero-based page number
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for loading the entities, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the point-in-time of the report if not provided. 
    
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

<details><summary><code>client.search.<a href="src/fern/search/client.py#L207-L241">cancel_async_search</a>(...) -> CancelAsyncSearchDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attempts to cancel a running async search job. The operation:
- Only succeeds if the search job is in RUNNING state
- Returns the cancellation result and final status
- Invalidates the search job entry if cancellation succeeds
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.cancel_async_search(
    job_id="jobId",
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

**job_id:** `str` — UUID of the search job to cancel
    
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

<details><summary><code>client.search.<a href="src/fern/search/client.py#L243-L282">get_async_search_status</a>(...) -> AsyncSearchStatusDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the current status of an async search job. The response includes:
- Current status (one of: RUNNING, FAILED, CANCELLED, SUCCESSFUL, NOT_FOUND)
- Number of entities collected
- Calculation time
- Creation timestamp
- Finish timestamp (if completed)
- Expiration date

Note: The NOT_FOUND status occurs in rare race conditions where the search job exists when the endpoint is called but is deleted during data retrieval.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.get_async_search_status(
    job_id="jobId",
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

**job_id:** `str` — UUID of the search job to check status for
    
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

<details><summary><code>client.search.<a href="src/fern/search/client.py#L284-L371">entities</a>(...) -> typing.List[EntityResultDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Executes a direct, in-memory search for entities without creating a persistent search job. This endpoint:
- Returns results immediately as a streaming response
- Is optimized for smaller result sets
- Has configurable timeout and result limits
- Supports point-in-time querying

By default results are ordered by entity id ascending. Pass one or more `sort` keys to order by scalar data or meta fields; entity id is always the final tiebreaker.

If no request body is provided or an empty request body is sent, all entities of the specified model and version
will be returned (subject to the limit parameter).

Best suited for:
- Interactive searches requiring immediate results
- Queries expected to return limited number of entities
- UI components with real-time search functionality

Limitations:
- Maximum result limit: 10000 entities (this will silently limit the result to 10000)
- Default result limit: 1000 entities
- Default timeout: 60000 milliseconds
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
from fern import FernApi, ArrayConditionDto, ArrayConditionDtoOperatorType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search.entities(
    entity_name="entityName",
    model_version=1,
    request=ArrayConditionDto(
        type="type",
        json_path="jsonPath",
        operator_type=ArrayConditionDtoOperatorType.EQUALS,
        value=[
            "value"
        ],
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

**entity_name:** `str` — Name of the entity model to search
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `int` — Version of the entity model
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchEntitiesRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**point_in_time:** `typing.Optional[datetime.datetime]` — The point-in-time for searching the entities, in ISO 8601 format. Defaults to the consistency time of the system if not provided. 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` — The maximum number of rows to return. You can specify a limit of up to 10000 and defaults to 1000 if not provided. 
    
</dd>
</dl>

<dl>
<dd>

**timeout_millis:** `typing.Optional[str]` — The maximum time to wait for the query to complete, in milliseconds, and defaults to 60000 if not provided. 
    
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

## SQL-Schema
<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L30-L61">get_schema_by_name</a>(...) -> SchemaConfigDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a schema configuration using its name
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.get_schema_by_name(
    schema_name="schemaName",
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

**schema_name:** `str` — Name of the schema to retrieve
    
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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L63-L323">save_schema</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Saves a new or updates an existing schema configuration
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
from fern import FernApi, TableConfigDto, FieldConfigDto
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.save_schema(
    schema_name="NOBEL_PRIZES",
    tables=[
        TableConfigDto(
            table_name="nobel-prize",
            metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
            uniformed_path="$",
            fields=[
                FieldConfigDto(
                    field_name="entity_id",
                    field_key="ENTITY_ID",
                    field_category="SPECIAL",
                    data_type="UUID_TYPE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="point_time",
                    field_key="POINT_TIME",
                    field_category="SPECIAL",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="creation_date",
                    field_key="creationDate",
                    field_category="ROOT",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="last_update_date",
                    field_key="lastUpdateTime",
                    field_category="ROOT",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="state",
                    field_key="state",
                    field_category="ROOT",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="category",
                    field_key=".category",
                    field_category="DATA",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="year",
                    field_key=".year",
                    field_category="DATA",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                )
            ],
            hidden=False,
        ),
        TableConfigDto(
            table_name="nobel-prize_laureates",
            metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
            uniformed_path="$.laureates[*]",
            fields=[
                FieldConfigDto(
                    field_name="entity_id",
                    field_key="ENTITY_ID",
                    field_category="SPECIAL",
                    data_type="UUID_TYPE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="point_time",
                    field_key="POINT_TIME",
                    field_category="SPECIAL",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="creation_date",
                    field_key="creationDate",
                    field_category="ROOT",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="last_update_date",
                    field_key="lastUpdateTime",
                    field_category="ROOT",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="state",
                    field_key="state",
                    field_category="ROOT",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="index",
                    field_key="",
                    field_category="INDEX",
                    data_type="INTEGER",
                    is_array=True,
                    hidden=True,
                    flatten=True,
                ),
                FieldConfigDto(
                    field_name="firstname",
                    field_key=".firstname",
                    field_category="DATA",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="surname",
                    field_key=".surname",
                    field_category="DATA",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="id",
                    field_key=".id",
                    field_category="DATA",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="motivation",
                    field_key=".motivation",
                    field_category="DATA",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="share",
                    field_key=".share",
                    field_category="DATA",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                )
            ],
            hidden=False,
        ),
        TableConfigDto(
            table_name="nobel-prize_json",
            metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
            uniformed_path="json",
            fields=[
                FieldConfigDto(
                    field_name="entity_id",
                    field_key="ENTITY_ID",
                    field_category="SPECIAL",
                    data_type="UUID_TYPE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="point_time",
                    field_key="POINT_TIME",
                    field_category="SPECIAL",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="creation_date",
                    field_key="creationDate",
                    field_category="ROOT",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="last_update_date",
                    field_key="lastUpdateTime",
                    field_category="ROOT",
                    data_type="DATE",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="state",
                    field_key="state",
                    field_category="ROOT",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                ),
                FieldConfigDto(
                    field_name="entity",
                    field_key="JSON",
                    field_category="SPECIAL",
                    data_type="STRING",
                    is_array=True,
                    hidden=True,
                )
            ],
            hidden=False,
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

**request:** `SchemaConfigDto` 
    
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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L325-L356">delete_schema_by_name</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing schema configuration using its name
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.delete_schema_by_name(
    schema_name="schemaName",
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

**schema_name:** `str` — Name of the schema to delete
    
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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L358-L389">gen_tables</a>(...) -> TableConfigDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates table configurations based on entity model ID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.gen_tables(
    entity_model_id="entityModelId",
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

**entity_model_id:** `str` — The entity model id to generate tables from
    
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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L391-L415">get_schemas</a>() -> SchemaConfigDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all available schema configurations
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.get_schemas()

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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L417-L448">put_schema</a>(...) -> SchemaConfigDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new schema configuration that includes all available entity models with their complete field structures
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.put_schema(
    schema_name="schemaName",
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

**schema_name:** `str` — Name for the new schema. The name can have a maximum of 1024 characters
    
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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L450-L484">update_tables</a>(...) -> TableConfigDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Synchronizes given table configurations with the current entity model structure, preserving custom settings while incorporating any model changes
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.update_tables(
    entity_model_id="entityModelId",
    request="string",
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

**entity_model_id:** `str` — The entity model ID to update tables from
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L486-L515">get_schema</a>(...) -> SchemaConfigDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a schema configuration using its UUID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.get_schema(
    schema_id="schemaId",
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

**schema_id:** `str` — UUID of the schema to retrieve
    
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

<details><summary><code>client.sql_schema.<a href="src/fern/sql_schema/client.py#L517-L546">delete_schema</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a schema configuration using its UUID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sql_schema.delete_schema(
    schema_id="schemaId",
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

**schema_id:** `str` — UUID of the schema to delete
    
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

