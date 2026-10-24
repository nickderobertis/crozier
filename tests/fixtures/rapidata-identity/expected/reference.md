# Reference
## RapidataIdentityApi
<details><summary><code>client.rapidata_identity_api.<a href="src/fern/rapidata_identity_api/client.py">get</a>()</code></summary>
<dl>
<dd>

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

client.rapidata_identity_api.get()

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

## Bidder
<details><summary><code>client.bidder.<a href="src/fern/bidder/client.py">lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time</a>(...) -> GetBidderRelationMembersEndpointCursorPagedResultOfOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every relation unless relation narrows it. Follow nextCursor to page.
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

client.bidder.lists_the_customers_holding_bidder_relations_one_cursor_page_at_a_time()

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

**relation:** `typing.Optional[AuthorizationRelationsBidder]` — Optional relation to filter by.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor from the previous page; omit for the first page.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
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

<details><summary><code>client.bidder.<a href="src/fern/bidder/client.py">grants_a_bidder_relation_to_a_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: re-granting an existing relation is a no-op.
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
from fern import FernApi, AuthorizationRelationsBidder
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bidder.grants_a_bidder_relation_to_a_customer(
    customer="customer",
    relation=AuthorizationRelationsBidder.ADMIN,
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

**customer:** `str` — The customer to grant the relation to.
    
</dd>
</dl>

<dl>
<dd>

**relation:** `AuthorizationRelationsBidder` 
    
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

<details><summary><code>client.bidder.<a href="src/fern/bidder/client.py">revokes_a_bidder_relation_from_a_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: revoking a relation that was never granted is a no-op.
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
from fern import FernApi, AuthorizationRelationsBidder
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bidder.revokes_a_bidder_relation_from_a_customer(
    customer="customer",
    relation=AuthorizationRelationsBidder.ADMIN,
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

**customer:** `str` — The customer to revoke the relation from.
    
</dd>
</dl>

<dl>
<dd>

**relation:** `AuthorizationRelationsBidder` 
    
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

## Capabilities
<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time</a>(...) -> GetCapabilityGranteesEndpointCursorPagedResultOfOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow nextCursor to page.
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
from fern import FernApi, Capability
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.capabilities.lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time(
    capability=Capability.SKIP_CONTENT_CHECK,
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

**capability:** `Capability` — The capability to inspect.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor from the previous page; omit for the first page.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
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

<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">lists_the_capabilities_a_customer_holds</a>(...) -> GetCustomerCapabilitiesEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

capabilities are granted to an organization, so these are the grants of the
 organization the customer is currently acting under — the same set enforced for them. A
 customer without an organization holds none.
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

client.capabilities.lists_the_capabilities_a_customer_holds(
    customer_id="customerId",
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

**customer_id:** `str` — The customer to inspect.
    
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

<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">lists_the_capabilities_granted_to_an_organization</a>(...) -> GetOrganizationCapabilitiesEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Readable by the organization's own members, so a client can light up the product surfaces its
 grants entitle it to; platform staff read any organization.
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

client.capabilities.lists_the_capabilities_granted_to_an_organization(
    organization_id="organizationId",
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

**organization_id:** `str` — The organization to inspect.
    
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

<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">grants_a_capability_to_an_organization</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: re-granting an existing grant is a no-op.
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
from fern import FernApi, Capability
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.capabilities.grants_a_capability_to_an_organization(
    organization_id="organizationId",
    capability=Capability.SKIP_CONTENT_CHECK,
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

**organization_id:** `str` — The organization to grant the capability to.
    
</dd>
</dl>

<dl>
<dd>

**capability:** `Capability` — The capability to grant.
    
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

<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">revokes_an_organizations_capability_grant</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: revoking a grant that does not exist is a no-op.
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
from fern import FernApi, Capability
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.capabilities.revokes_an_organizations_capability_grant(
    organization_id="organizationId",
    capability=Capability.SKIP_CONTENT_CHECK,
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

**organization_id:** `str` — The organization to revoke the capability from.
    
</dd>
</dl>

<dl>
<dd>

**capability:** `Capability` — The capability to revoke.
    
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

## Client
<details><summary><code>client.client.<a href="src/fern/client/client.py">creates_a_new_client_for_the_current_customer</a>(...) -> CreateClientEndpointOutput</code></summary>
<dl>
<dd>

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

client.client.creates_a_new_client_for_the_current_customer()

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

**display_name:** `typing.Optional[str]` — An optional display name for the client.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The organization to authorize the client for. Defaults to the caller's active organization.
    
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

<details><summary><code>client.client.<a href="src/fern/client/client.py">identity_get_client</a>(...) -> Client</code></summary>
<dl>
<dd>

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

client.client.identity_get_client(
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

**client_id:** `str` — The id of the client to retrieve.
    
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

<details><summary><code>client.client.<a href="src/fern/client/client.py">deletes_a_client</a>(...)</code></summary>
<dl>
<dd>

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

client.client.deletes_a_client(
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

**client_id:** `str` — The id of the client to delete.
    
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

<details><summary><code>client.client.<a href="src/fern/client/client.py">queries_clients_for_the_current_customer</a>(...) -> QueryClientsEndpointPagedResultOfOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clients are service credentials that allow automated processes to authenticate against the API.
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

client.client.queries_clients_for_the_current_customer()

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

**page:** `typing.Optional[int]` — The 1-based page index.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]]` — Sort fields. Prefix with - for descending order (e.g. -created_at).
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[GetClientsRequestClientId]` — Filter by client_id.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[GetClientsRequestDisplayName]` — Filter by display_name.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[GetClientsRequestCreatedAt]` — Filter by created_at.
    
</dd>
</dl>

<dl>
<dd>

**logic:** `typing.Optional[GetClientsRequestLogic]` — How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.
    
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

<details><summary><code>client.client.<a href="src/fern/client/client.py">registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follows RFC 7591.
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

client.client.registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol()

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

**redirect_uris:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**grant_types:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**response_types:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**logo_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` 

String containing a space-separated list of scope values
 that the client can use when requesting access tokens.
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Optional[typing.List[str]]` 

Array of strings representing ways to contact people responsible for this client,
 typically email addresses.
    
</dd>
</dl>

<dl>
<dd>

**tos_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policy_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**jwks_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**jwks:** `typing.Optional[JsonWebKeySet]` — Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys.
    
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

## Customer
<details><summary><code>client.customer.<a href="src/fern/customer/client.py">deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This cannot be undone. An organization the account is the only member of is deleted with it,
 along with everything it owns; invoices already raised are kept. Responds with 409 when the
 account is the last owner of an organization that has other members — transfer ownership
 first — or when such an organization still has an open invoice or a billing reconciliation in
 progress. Issuing it again for an account that is already deleted succeeds and changes
 nothing further. The same address and the same external login can be used to register a new
 account afterwards; none of the old account's data comes back with it.
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

client.customer.deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
    customer_id="customerId",
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

**customer_id:** `str` — The id of the customer to delete.
    
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

<details><summary><code>client.customer.<a href="src/fern/customer/client.py">queries_customers_with_filtering_and_pagination</a>(...) -> QueryCustomersEndpointPagedResultOfOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Results are scoped to customers that belong to the caller's organization.
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

client.customer.queries_customers_with_filtering_and_pagination()

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

**page:** `typing.Optional[int]` — The 1-based page index.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]]` — Sort fields. Prefix with - for descending order (e.g. -created_at).
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[GetCustomersRequestId]` — Filter by id.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[GetCustomersRequestEmail]` — Filter by email.
    
</dd>
</dl>

<dl>
<dd>

**organization_name:** `typing.Optional[GetCustomersRequestOrganizationName]` — Filter by organization_name.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[GetCustomersRequestOrganizationId]` — Filter by organization_id.
    
</dd>
</dl>

<dl>
<dd>

**logic:** `typing.Optional[GetCustomersRequestLogic]` — How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.
    
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

## ExternalApps
<details><summary><code>client.external_apps.<a href="src/fern/external_apps/client.py">lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time</a>(...) -> GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

app is required: each app is a separate object in the graph, so there is no combined
 listing. Returns every relation unless relation narrows it. Follow nextCursor to page.
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
from fern import FernApi, ExternalAppId
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_apps.lists_the_customers_holding_relations_on_one_app_one_cursor_page_at_a_time(
    app=ExternalAppId.ARGO_CD,
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

**app:** `ExternalAppId` — The app whose members to list.
    
</dd>
</dl>

<dl>
<dd>

**relation:** `typing.Optional[AuthorizationRelationsExternalApp]` — Optional relation to filter by.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor from the previous page; omit for the first page.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
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

<details><summary><code>client.external_apps.<a href="src/fern/external_apps/client.py">grants_an_external_app_relation_to_a_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: re-granting an existing relation is a no-op. The app must be one of the known
 values — an unrecognised app is rejected rather than written, since a grant against an object
 nothing reads would look like access was granted while conferring nothing.
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
from fern import FernApi, ExternalAppId, AuthorizationRelationsExternalApp
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_apps.grants_an_external_app_relation_to_a_customer(
    customer="customer",
    app=ExternalAppId.ARGO_CD,
    relation=AuthorizationRelationsExternalApp.ADMIN,
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

**customer:** `str` — The customer to grant the relation to.
    
</dd>
</dl>

<dl>
<dd>

**app:** `ExternalAppId` 
    
</dd>
</dl>

<dl>
<dd>

**relation:** `AuthorizationRelationsExternalApp` 
    
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

<details><summary><code>client.external_apps.<a href="src/fern/external_apps/client.py">revokes_an_external_app_relation_from_a_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: revoking a relation that was never granted is a no-op.
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
from fern import FernApi, ExternalAppId, AuthorizationRelationsExternalApp
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.external_apps.revokes_an_external_app_relation_from_a_customer(
    customer="customer",
    app=ExternalAppId.ARGO_CD,
    relation=AuthorizationRelationsExternalApp.ADMIN,
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

**customer:** `str` — The customer to revoke the relation from.
    
</dd>
</dl>

<dl>
<dd>

**app:** `ExternalAppId` 
    
</dd>
</dl>

<dl>
<dd>

**relation:** `AuthorizationRelationsExternalApp` 
    
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

## Identity
<details><summary><code>client.identity.<a href="src/fern/identity/client.py">reads_the_bridge_token_keys_for_a_given_read_key</a>(...) -> ReadBridgeTokenEndpointKeysOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns 200 with the keys when available, 202 when they are not yet available, or 404 when not found.
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

client.identity.reads_the_bridge_token_keys_for_a_given_read_key(
    read_key="readKey",
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

**read_key:** `str` — The read key to read the bridge token keys for.
    
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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client</a>(...) -> CreateBridgeTokenEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The write key stores the authentication result and the read key retrieves it.
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

client.identity.creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
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

**client_id:** `str` — The client ID to create the keys for.
    
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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">signs_in_a_user_using_a_token_received_from_google_one_tap</a>(...) -> GoogleOneTapLoginEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Redirects to the register confirmation page when the account requires email confirmation.
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

client.identity.signs_in_a_user_using_a_token_received_from_google_one_tap(
    id_token="idToken",
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

**id_token:** `str` — The id token received from the Google One Tap login.
    
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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">stores_the_referrer_in_a_cookie_for_later_use_during_sign_up</a>(...)</code></summary>
<dl>
<dd>

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

client.identity.stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
    referrer="referrer",
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

**referrer:** `str` — The referrer value to store.
    
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

## Newsletter
<details><summary><code>client.newsletter.<a href="src/fern/newsletter/client.py">signs_an_email_address_up_to_the_newsletter</a>(...)</code></summary>
<dl>
<dd>

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

client.newsletter.signs_an_email_address_up_to_the_newsletter(
    email="email",
    token="token",
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

**email:** `str` — The email of the user to subscribe.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The recaptcha token used to verify the caller is not a bot.
    
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

<details><summary><code>client.newsletter.<a href="src/fern/newsletter/client.py">removes_an_email_address_from_the_newsletter</a>(...)</code></summary>
<dl>
<dd>

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

client.newsletter.removes_an_email_address_from_the_newsletter(
    email="email",
    token="token",
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

**email:** `str` — The email of the user to unsubscribe.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The recaptcha token used to verify the caller is not a bot.
    
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

## Organization
<details><summary><code>client.organization.<a href="src/fern/organization/client.py">accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one</a>(...) -> AcceptOrgInvitationByIdEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Responds with 409 when the invitation is expired, already used, or was issued to a different
 email than the calling customer's.
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

client.organization.accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one(
    invitation_id="invitationId",
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

**invitation_id:** `str` — The id of the invitation to accept.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">accepts_the_invitation_identified_by_the_token</a>(...) -> AcceptOrgInvitationEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Responds with 409 when the invitation is expired, already used, or was issued to a different
 email than the calling customer's.
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

client.organization.accepts_the_invitation_identified_by_the_token(
    token="token",
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

**token:** `str` — The single-use invitation token.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">sets_the_given_members_org_scoped_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Responds with 404 when the customer is not a member and 409 when changing the role of the
 organization's last owner.
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
from fern import FernApi, OrgRole
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organization.sets_the_given_members_org_scoped_role(
    organization_id="organizationId",
    customer_id="customerId",
    role=OrgRole.OWNER,
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

**organization_id:** `str` — The id of the organization.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The id of the member whose role changes.
    
</dd>
</dl>

<dl>
<dd>

**role:** `OrgRole` — The org-scoped role to assign to the member.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role</a>(...) -> QueryOrganizationsEndpointPagedResultOfOutput</code></summary>
<dl>
<dd>

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

client.organization.returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role()

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

**page:** `typing.Optional[int]` — The 1-based page index.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[GetOrganizationsRequestSortItem, typing.Sequence[GetOrganizationsRequestSortItem]]]` — Sort fields. Prefix with - for descending order (e.g. -created_at).
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[GetOrganizationsRequestId]` — Filter by id.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[GetOrganizationsRequestName]` — Filter by name.
    
</dd>
</dl>

<dl>
<dd>

**logic:** `typing.Optional[GetOrganizationsRequestLogic]` — How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">creates_an_organization_and_makes_the_calling_customer_its_owner</a>(...) -> CreateOrganizationEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The calling customer becomes the organization's owner.
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

client.organization.creates_an_organization_and_makes_the_calling_customer_its_owner(
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

**name:** `str` — The human-readable name of the organization.
    
</dd>
</dl>

<dl>
<dd>

**primary_domain:** `typing.Optional[str]` — The primary email domain associated with the organization, if any.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">returns_the_organization_with_the_given_id</a>(...) -> GetOrganizationEndpointOutput</code></summary>
<dl>
<dd>

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

client.organization.returns_the_organization_with_the_given_id(
    organization_id="organizationId",
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

**organization_id:** `str` — The id of the organization to retrieve.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">deletes_the_organization_and_everything_it_owns_across_the_platform</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This cannot be undone. Every member loses access immediately and each service removes the
 organization's data; invoices already raised are kept. Responds with 409 when the
 organization still has an open invoice or a billing reconciliation in progress — settle those
 first.
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

client.organization.deletes_the_organization_and_everything_it_owns_across_the_platform(
    organization_id="organizationId",
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

**organization_id:** `str` — The id of the organization to delete.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">updates_the_given_organizations_provided_fields</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only the fields present in the body are changed, and only those the caller may change. An
 auto-join domain is rejected when it is malformed or already claimed by another organization;
 enabling auto-join without a claimed domain is rejected as well.
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

client.organization.updates_the_given_organizations_provided_fields(
    organization_id="organizationId",
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

**organization_id:** `str` — The id of the organization to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The new human-readable name, if changing it.
    
</dd>
</dl>

<dl>
<dd>

**auto_join_domain:** `typing.Optional[str]` 

The email domain to claim for auto-join, or null to release the claim. New customers who
 sign up with a confirmed email on this domain join this organization instead of getting a
 personal one, once auto-join is enabled. Existing customers are never moved.
    
</dd>
</dl>

<dl>
<dd>

**auto_join_enabled:** `typing.Optional[bool]` — Whether to auto-join new customers signing up on the claimed domain.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">returns_the_pending_invitations_of_the_given_organization</a>(...) -> ListOrgInvitationsEndpointOutput</code></summary>
<dl>
<dd>

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

client.organization.returns_the_pending_invitations_of_the_given_organization(
    organization_id="organizationId",
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

**organization_id:** `str` — The id of the organization whose invitations to list.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">creates_an_invitation_to_join_the_organization</a>(...) -> InviteOrgMemberEndpointOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An invitation mail with the accept link is sent to the invitee. The response still carries
 the single-use token the invitee presents to the accept-invitation endpoint, so the link can
 also be shared manually.
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
from fern import FernApi, OrgRole
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organization.creates_an_invitation_to_join_the_organization(
    organization_id="organizationId",
    email="email",
    role=OrgRole.OWNER,
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

**organization_id:** `str` — The id of the organization to invite into.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email address to invite.
    
</dd>
</dl>

<dl>
<dd>

**role:** `OrgRole` — The org-scoped role the resulting membership will confer.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address</a>() -> ListMyOrgInvitationsEndpointOutput</code></summary>
<dl>
<dd>

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

client.organization.returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address()

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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">returns_the_members_of_the_given_organization</a>(...) -> ListOrgMembersEndpointOutput</code></summary>
<dl>
<dd>

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

client.organization.returns_the_members_of_the_given_organization(
    organization_id="organizationId",
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

**organization_id:** `str` — The id of the organization whose members to list.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">returns_a_paged_list_of_every_organization</a>(...) -> QueryAllOrganizationsEndpointPagedResultOfOutput</code></summary>
<dl>
<dd>

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

client.organization.returns_a_paged_list_of_every_organization()

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

**page:** `typing.Optional[int]` — The 1-based page index.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[GetOrganizationsAllRequestSortItem, typing.Sequence[GetOrganizationsAllRequestSortItem]]]` — Sort fields. Prefix with - for descending order (e.g. -created_at).
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[GetOrganizationsAllRequestId]` — Filter by id.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[GetOrganizationsAllRequestName]` — Filter by name.
    
</dd>
</dl>

<dl>
<dd>

**owner_email:** `typing.Optional[GetOrganizationsAllRequestOwnerEmail]` — Filter by owner_email.
    
</dd>
</dl>

<dl>
<dd>

**logic:** `typing.Optional[GetOrganizationsAllRequestLogic]` — How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">declines_the_invitation_identified_by_invitation_id_no_membership_is_created</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Responds with 409 when the invitation is not pending or was issued to a different email than
 the calling customer's.
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

client.organization.declines_the_invitation_identified_by_invitation_id_no_membership_is_created(
    invitation_id="invitationId",
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

**invitation_id:** `str` — The id of the invitation to reject.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">removes_the_given_customers_membership_from_the_organization</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Responds with 404 when the customer is not a member and 409 when removing the organization's
 last owner.
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

client.organization.removes_the_given_customers_membership_from_the_organization(
    organization_id="organizationId",
    customer_id="customerId",
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

**organization_id:** `str` — The id of the organization.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The id of the customer to remove.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Responds with 404 when the invitation does not belong to the organization and 409 when it is
 not pending.
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

client.organization.revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted(
    organization_id="organizationId",
    invitation_id="invitationId",
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

**organization_id:** `str` — The id of the organization.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — The id of the invitation to revoke.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">sets_the_support_slack_channel_url_for_the_given_organization</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A null or empty URL clears the channel. Responds with 404 when no organization with the given id exists.
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

client.organization.sets_the_support_slack_channel_url_for_the_given_organization(
    organization_id="organizationId",
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

**organization_id:** `str` — The id of the organization.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The support Slack channel URL to set, or null/empty to clear it.
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py">switches_the_calling_customers_active_organization_to_the_given_one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The active organization determines the token's org claim; the change takes effect the next time
 the client refreshes its token. Responds with 403 when the caller is not a member of the target
 organization.
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

client.organization.switches_the_calling_customers_active_organization_to_the_given_one(
    organization_id="organizationId",
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

**organization_id:** `str` — The id of the organization to activate.
    
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

## Platform
<details><summary><code>client.platform.<a href="src/fern/platform/client.py">lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time</a>(...) -> GetPlatformRelationMembersEndpointCursorPagedResultOfOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every relation unless relation narrows it. Follow nextCursor to page.
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

client.platform.lists_the_customers_holding_platform_relations_one_cursor_page_at_a_time()

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

**relation:** `typing.Optional[AuthorizationRelationsPlatform]` — Optional relation to filter by.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor from the previous page; omit for the first page.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of items per page.
    
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

<details><summary><code>client.platform.<a href="src/fern/platform/client.py">grants_a_platform_relation_to_a_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: re-granting an existing relation is a no-op.
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
from fern import FernApi, AuthorizationRelationsPlatform
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.platform.grants_a_platform_relation_to_a_customer(
    customer="customer",
    relation=AuthorizationRelationsPlatform.ADMIN,
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

**customer:** `str` — The customer to grant the relation to.
    
</dd>
</dl>

<dl>
<dd>

**relation:** `AuthorizationRelationsPlatform` 
    
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

<details><summary><code>client.platform.<a href="src/fern/platform/client.py">revokes_a_platform_relation_from_a_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent: revoking a relation that was never granted is a no-op.
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
from fern import FernApi, AuthorizationRelationsPlatform
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.platform.revokes_a_platform_relation_from_a_customer(
    customer="customer",
    relation=AuthorizationRelationsPlatform.ADMIN,
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

**customer:** `str` — The customer to revoke the relation from.
    
</dd>
</dl>

<dl>
<dd>

**relation:** `AuthorizationRelationsPlatform` 
    
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

## Survey
<details><summary><code>client.survey.<a href="src/fern/survey/client.py">submits_a_survey_for_the_calling_customer</a>(...)</code></summary>
<dl>
<dd>

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

client.survey.submits_a_survey_for_the_calling_customer(
    fields={
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

**fields:** `typing.Dict[str, str]` 
    
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

