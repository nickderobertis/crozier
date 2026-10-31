# Reference
## consent
<details><summary><code>client.consent.<a href="src/fern/consent/client.py">create_consent_record</a>(...) -> ConsentRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Citizen-signed consent artifact. MUST include `dpa_reference` whenever any requested
scope touches a PII-bound tool (PIPA §26 위탁 documentation gap closure).
MUST include `synthesis_consent` as a separate boolean reflecting the LLM-synthesis
controller-level carve-out.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consent.create_consent_record(
    citizen_identity="citizen_identity",
    scopes=[
        "scopes"
    ],
    synthesis_consent=True,
    expires_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**request:** `ConsentRequest` 
    
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

## token
<details><summary><code>client.token.<a href="src/fern/token/client.py">issue_delegation_token</a>(...) -> DelegationToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issues a `DelegationToken` bound to a citizen authentication event.
Supports two grant flows:
  - Device Authorization Grant per RFC 8628 (agent-first flows).
  - Token Exchange per RFC 8693 (ministry-to-ministry hand-off).
PKCE per RFC 7636 is REQUIRED on all grant types. The issued token is a JWT
per RFC 9068 with `aal_asserted` claim carrying NIST SP 800-63-4 AAL.
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
from fern import FernApi, TokenRequestGrantType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.token.issue_delegation_token(
    grant_type=TokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE,
    code_verifier="code_verifier",
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

**request:** `TokenRequest` 
    
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

## introspection
<details><summary><code>client.introspection.<a href="src/fern/introspection/client.py">introspect_delegation_token</a>(...) -> IntrospectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

MUST be called by the permission pipeline before any invocation of a tool whose
`is_irreversible = True`, regardless of local cache state (FR-007).
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

client.introspection.introspect_delegation_token(
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

**request:** `IntrospectionRequest` 
    
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

## revocation
<details><summary><code>client.revocation.<a href="src/fern/revocation/client.py">revoke_delegation_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes a token immediately. The spec declares a maximum propagation window
(documented in the normative spec, not this skeleton) after which all downstream
caches MUST reject the token.
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

client.revocation.revoke_delegation_token(
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

**request:** `RevocationRequest` 
    
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

