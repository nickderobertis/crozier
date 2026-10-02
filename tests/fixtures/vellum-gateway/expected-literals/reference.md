# Reference
## Permissions
<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">thresholds_get</a>() -> PermissionsThresholdsGetResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.thresholds_get()

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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">thresholds_put</a>(...) -> PermissionsThresholdsPutResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partial update — omitted modes keep their current value. Returns the full post-update set.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.thresholds_put()

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

**interactive:** `typing.Optional[PermissionsThresholdsPutRequestInteractive]` 
    
</dd>
</dl>

<dl>
<dd>

**autonomous:** `typing.Optional[PermissionsThresholdsPutRequestAutonomous]` 
    
</dd>
</dl>

<dl>
<dd>

**headless:** `typing.Optional[PermissionsThresholdsPutRequestHeadless]` 
    
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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">conversation_threshold_get</a>(...) -> ConversationThresholdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns { threshold: null } when no override exists. (Gateways predating that behavior returned 404 for the same condition; clients tolerate both during rollout.)
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.conversation_threshold_get(
    conversation_id="conversation_id",
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

**conversation_id:** `str` — The conversation id
    
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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">conversation_threshold_put</a>(...) -> ConversationThresholdPutResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.conversation_threshold_put(
    conversation_id="conversation_id",
    threshold="none",
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

**conversation_id:** `str` — The conversation id
    
</dd>
</dl>

<dl>
<dd>

**threshold:** `ConversationThresholdPutRequestThreshold` 
    
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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">conversation_threshold_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Idempotent — succeeds even when no override exists.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.conversation_threshold_delete(
    conversation_id="conversation_id",
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

**conversation_id:** `str` — The conversation id
    
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

## ChannelAdmissionPolicy
<details><summary><code>client.channel_admission_policy.<a href="src/fern/channel_admission_policy/client.py">list</a>() -> ChannelAdmissionPolicyListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one entry per enforced channel (exempt and hidden channels are omitted), seeded with defaults for channels without a stored row.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_admission_policy.list()

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

<details><summary><code>client.channel_admission_policy.<a href="src/fern/channel_admission_policy/client.py">set</a>(...) -> ChannelAdmissionPolicySetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upserts the channel's admission policy. Exempt and hidden channels return 403.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_admission_policy.set(
    channel_type="channel_type",
    policy="no_one",
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

**channel_type:** `str` — The channel type (e.g. slack)
    
</dd>
</dl>

<dl>
<dd>

**policy:** `ChannelAdmissionPolicySetRequestPolicy` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
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

## ChannelIngress
<details><summary><code>client.channel_ingress.<a href="src/fern/channel_ingress/client.py">list</a>() -> ChannelIngressListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Every declaration the gateway can see, each with the digest a guardian would approve, the public paths it would open, and the credential its signatures are verified against. This is the only way to learn that a declaration is waiting: on the public surface a route held back by approval 404s exactly like one nobody declared.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_ingress.list()

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

<details><summary><code>client.channel_ingress.<a href="src/fern/channel_ingress/client.py">approve</a>(...) -> ChannelIngressApproveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records the guardian's approval of the declaration identified by the body's digest, after which the gateway serves its routes. Returns 409 when the digest is not what the source currently declares, and 404 when it declares nothing servable.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_ingress.approve(
    source="source",
    digest="digest",
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

**source:** `str` — The declaring ingress source (today, a plugin name)
    
</dd>
</dl>

<dl>
<dd>

**digest:** `str` 
    
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

<details><summary><code>client.channel_ingress.<a href="src/fern/channel_ingress/client.py">revoke</a>(...) -> ChannelIngressRevokeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Withdraws the source's grant, after which its routes stop being served. Reports whether there was a grant to withdraw. Succeeds even when the declaration itself has become unreadable.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_ingress.revoke(
    source="source",
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

**source:** `str` — The declaring ingress source (today, a plugin name)
    
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

## ChannelPermissionOverrides
<details><summary><code>client.channel_permission_overrides.<a href="src/fern/channel_permission_overrides/client.py">list</a>() -> ChannelPermissionOverridesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every persisted cell (cascade selector × contact-type → RiskThreshold). Unset cells fall through the cascade; the list contains only explicit overrides.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_permission_overrides.list()

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

<details><summary><code>client.channel_permission_overrides.<a href="src/fern/channel_permission_overrides/client.py">channel_permission_override_set</a>(...) -> ChannelPermissionOverrideSetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upserts one cell, identified by the selector × contact-type in the body. The adapter must be a known channel id.
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
from fern.channel_permission_overrides import ChannelPermissionOverrideSetRequestSelector_Workspace

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_permission_overrides.channel_permission_override_set(
    selector=ChannelPermissionOverrideSetRequestSelector_Workspace(),
    contact_type="guardian",
    threshold="none",
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

**selector:** `ChannelPermissionOverrideSetRequestSelector` 
    
</dd>
</dl>

<dl>
<dd>

**contact_type:** `ChannelPermissionOverrideSetRequestContactType` 
    
</dd>
</dl>

<dl>
<dd>

**threshold:** `ChannelPermissionOverrideSetRequestThreshold` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
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

<details><summary><code>client.channel_permission_overrides.<a href="src/fern/channel_permission_overrides/client.py">channel_permission_resolve</a>(...) -> ChannelPermissionResolveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read-only cascade resolution for one coordinate: walks channel → channel_type → adapter → workspace for the given selector keys and contact-type, returning the winning cell's threshold and scope, or null when no cell matches (the caller then falls through to the global thresholds). Same resolver the runtime evaluator uses over IPC.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_permission_overrides.channel_permission_resolve(
    adapter="adapter",
    contact_type="guardian",
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

**adapter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**contact_type:** `ChannelPermissionResolveRequestContactType` 
    
</dd>
</dl>

<dl>
<dd>

**channel_type:** `typing.Optional[ChannelPermissionResolveRequestChannelType]` 
    
</dd>
</dl>

<dl>
<dd>

**channel_external_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.channel_permission_overrides.<a href="src/fern/channel_permission_overrides/client.py">channel_permission_override_delete</a>(...) -> ChannelPermissionOverrideDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one cell by its composite key (selector × contact-type), letting the next cascade tier up win. Returns whether a cell was removed.
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
from fern.channel_permission_overrides import ChannelPermissionOverrideDeleteRequestSelector_Workspace

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_permission_overrides.channel_permission_override_delete(
    selector=ChannelPermissionOverrideDeleteRequestSelector_Workspace(),
    contact_type="guardian",
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

**selector:** `ChannelPermissionOverrideDeleteRequestSelector` 
    
</dd>
</dl>

<dl>
<dd>

**contact_type:** `ChannelPermissionOverrideDeleteRequestContactType` 
    
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

## Contacts
<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">upsert</a>(...) -> ContactsUpsertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gateway-native contact upsert (dual-writes the gateway ACL store and the assistant info mirror). Matches by id, then by any provided (type, address) channel, else creates.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.upsert(
    display_name="displayName",
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

**display_name:** `str` — Required on every upsert, including updates by id
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Existing contact id to update; omit to create or match by channel
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_approve_threshold:** `typing.Optional[ContactsUpsertRequestAutoApproveThreshold]` — Per-contact auto-approve ceiling. Omit to preserve; null clears.
    
</dd>
</dl>

<dl>
<dd>

**contact_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**assistant_metadata:** `typing.Optional[ContactsUpsertRequestAssistantMetadata]` — Required when contactType is 'assistant'
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.List[ContactsUpsertRequestChannelsItem]]` 
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">contact_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a non-guardian contact from the gateway ACL store and the assistant mirror. 404 when the contact exists in neither; 403 for guardian contacts.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.contact_delete(
    contact_id="contact_id",
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

**contact_id:** `str` — The contact id
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">prompt_submit</a>(...) -> ContactsPromptSubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes a contact_request the assistant broadcast: writes the contact and channel gateway-first, then unblocks the waiting prompt.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.prompt_submit(
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

**request_id:** `str` — The contact_request id broadcast by the assistant
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[str]` — Required unless cancelled is true
    
</dd>
</dl>

<dl>
<dd>

**channel_type:** `typing.Optional[str]` — Required unless cancelled is true
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — The contact the parked form targets, echoed back from the broadcast. The parked form is authoritative.
    
</dd>
</dl>

<dl>
<dd>

**verify:** `typing.Optional[bool]` — The form's 'mark verified' checkbox as the guardian left it. Omit only from clients that predate the checkbox; the parked command's flag is then used instead.
    
</dd>
</dl>

<dl>
<dd>

**cancelled:** `typing.Optional[bool]` — The guardian dismissed the form. Unblocks the waiting command without writing.
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">record_submit</a>(...) -> ContactsRecordSubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes a contact_record_request the assistant broadcast: writes the record the guardian confirmed, then unblocks the waiting command. A create or update writes display name and notes, never a channel; a merge moves the donor's channels to the survivor and deletes the donor. A cancelled submission unblocks the command without writing.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.record_submit(
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

**request_id:** `str` — The contact_record_request id broadcast by the assistant
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[ContactsRecordSubmitRequestOperation]` — Required unless cancelled is true
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — Required to update or delete, and the survivor of a merge
    
</dd>
</dl>

<dl>
<dd>

**donor_contact_id:** `typing.Optional[str]` — The contact merged away. Required for a merge.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expected_channels:** `typing.Optional[typing.List[ContactsRecordSubmitRequestExpectedChannelsItem]]` — The channels the delete confirmation listed. The delete is refused if the contact's channels changed since.
    
</dd>
</dl>

<dl>
<dd>

**cancelled:** `typing.Optional[bool]` — The guardian dismissed the form. Unblocks the waiting command without writing.
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">contact_channel_verify</a>(...) -> ContactChannelVerifyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guardian-only manual attestation: marks the channel active/verified in the gateway store (source of truth) with a best-effort assistant mirror. Idempotent.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.contact_channel_verify(
    channel_id="channel_id",
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

**channel_id:** `str` — The contact-channel id
    
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

## CredentialRequests
<details><summary><code>client.credential_requests.<a href="src/fern/credential_requests/client.py">peek</a>(...) -> CredentialRequestsPeekResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the service/field/label the link collects. The token travels in the body so it never appears in URLs or access logs.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.credential_requests.peek(
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

**token:** `str` 
    
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

<details><summary><code>client.credential_requests.<a href="src/fern/credential_requests/client.py">submit</a>(...) -> CredentialRequestsSubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Single-use: atomically claims the link, forwards the value to the assistant's credential store, and marks the link redeemed.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.credential_requests.submit(
    token="token",
    value="value",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 
    
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

## FeatureFlags
<details><summary><code>client.feature_flags.<a href="src/fern/feature_flags/client.py">get</a>() -> FeatureFlagsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all feature flags with their current values.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feature_flags.get()

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

<details><summary><code>client.feature_flags.<a href="src/fern/feature_flags/client.py">patch</a>(...) -> FeatureFlagsPatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the enabled state of a single feature flag.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.feature_flags.patch(
    flag_key="flag_key",
    enabled=True,
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

**flag_key:** `str` — The kebab-case flag identifier
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `FeatureFlagsPatchRequestEnabled` 
    
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

## TrustRules
<details><summary><code>client.trust_rules.<a href="src/fern/trust_rules/client.py">list</a>(...) -> TrustRulesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns trust rules, filtered to user-relevant rules by default. Pass include_all=true for the full set or origin/tool to filter.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.trust_rules.list()

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

**origin:** `typing.Optional[str]` — Filter by origin (default | user_defined)
    
</dd>
</dl>

<dl>
<dd>

**tool:** `typing.Optional[str]` — Filter by tool name
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[str]` — "true" to include soft-deleted rules
    
</dd>
</dl>

<dl>
<dd>

**include_all:** `typing.Optional[str]` — "true" to disable the user-relevant filter
    
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

<details><summary><code>client.trust_rules.<a href="src/fern/trust_rules/client.py">trust_rule_create</a>(...) -> TrustRuleCreateResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.trust_rules.trust_rule_create(
    tool="tool",
    pattern="pattern",
    risk="low",
    description="description",
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

**tool:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pattern:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**risk:** `TrustRuleCreateRequestRisk` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[TrustRuleCreateRequestScope]` — Compatibility field. Trust rules apply workspace-wide: the engine matches on (tool, pattern) only, so a narrower scope cannot be honored and any value other than "everywhere" is rejected rather than stored broader than the consent it records.
    
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

<details><summary><code>client.trust_rules.<a href="src/fern/trust_rules/client.py">trust_rule_suggest</a>(...) -> TrustRuleSuggestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

LLM-backed suggestion for a rule matching the given tool invocation. Returns 503 when the daemon suggestion relay is unavailable.
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
from fern.trust_rules import TrustRuleSuggestRequestRiskAssessment, TrustRuleSuggestRequestScopeOptionsItem

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.trust_rules.trust_rule_suggest(
    tool="tool",
    command="command",
    risk_assessment=TrustRuleSuggestRequestRiskAssessment(
        risk="risk",
        reasoning="reasoning",
        reason_description="reasonDescription",
    ),
    scope_options=[
        TrustRuleSuggestRequestScopeOptionsItem(
            pattern="pattern",
            label="label",
        )
    ],
    intent="auto_approve",
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

**tool:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**command:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**risk_assessment:** `TrustRuleSuggestRequestRiskAssessment` 
    
</dd>
</dl>

<dl>
<dd>

**scope_options:** `typing.List[TrustRuleSuggestRequestScopeOptionsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**intent:** `TrustRuleSuggestRequestIntent` 
    
</dd>
</dl>

<dl>
<dd>

**directory_scope_options:** `typing.Optional[typing.List[TrustRuleSuggestRequestDirectoryScopeOptionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**existing_rule:** `typing.Optional[TrustRuleSuggestRequestExistingRule]` 
    
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

<details><summary><code>client.trust_rules.<a href="src/fern/trust_rules/client.py">trust_rule_delete</a>(...) -> TrustRuleDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-deletes the rule. Default-origin rules can be reset later.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.trust_rules.trust_rule_delete(
    rule_id="rule_id",
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

**rule_id:** `str` — The trust rule id
    
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

<details><summary><code>client.trust_rules.<a href="src/fern/trust_rules/client.py">trust_rule_update</a>(...) -> TrustRuleUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates risk and/or description. Updating a default-origin rule marks it userModified.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.trust_rules.trust_rule_update(
    rule_id="rule_id",
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

**rule_id:** `str` — The trust rule id
    
</dd>
</dl>

<dl>
<dd>

**risk:** `typing.Optional[TrustRuleUpdateRequestRisk]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.trust_rules.<a href="src/fern/trust_rules/client.py">trust_rule_reset</a>(...) -> TrustRuleResetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores a default-origin rule to its registry risk and description, clearing userModified and deleted.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.trust_rules.trust_rule_reset(
    rule_id="rule_id",
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

**rule_id:** `str` — The trust rule id
    
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

