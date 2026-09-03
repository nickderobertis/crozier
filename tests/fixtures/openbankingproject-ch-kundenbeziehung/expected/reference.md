# Reference
## OAuth21Oidc
<details><summary><code>client.o_auth21oidc.<a href="src/fern/o_auth21oidc/client.py">authorize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

FAPI 2.0 compliant OAuth 2.1 authorization endpoint. Supports PAR (Pushed Authorization Requests)
and requires PKCE for all authorization flows.
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
from fern.o_auth21oidc import AuthorizeRequestResponseType, AuthorizeRequestCodeChallengeMethod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth21oidc.authorize(
    response_type=AuthorizeRequestResponseType.CODE,
    client_id="client_id",
    redirect_uri="redirect_uri",
    scope="scope",
    state="state",
    code_challenge="code_challenge",
    code_challenge_method=AuthorizeRequestCodeChallengeMethod.S256,
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

**response_type:** `AuthorizeRequestResponseType` — Must be 'code' for authorization code flow
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — OAuth client identifier
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — Client redirect URI
    
</dd>
</dl>

<dl>
<dd>

**scope:** `str` — Requested OAuth scopes
    
</dd>
</dl>

<dl>
<dd>

**state:** `str` — Client state parameter for CSRF protection
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `str` — PKCE code challenge (S256)
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `AuthorizeRequestCodeChallengeMethod` — PKCE code challenge method
    
</dd>
</dl>

<dl>
<dd>

**nonce:** `typing.Optional[str]` — OpenID Connect nonce
    
</dd>
</dl>

<dl>
<dd>

**request_uri:** `typing.Optional[str]` — PAR request URI (urn:ietf:params:oauth:request_uri:*)
    
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

<details><summary><code>client.o_auth21oidc.<a href="src/fern/o_auth21oidc/client.py">token</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

FAPI 2.0 compliant token endpoint supporting authorization_code and refresh_token grants.
Requires mTLS or private_key_jwt client authentication.
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
from fern.o_auth21oidc import TokenRequestGrantType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth21oidc.token(
    grant_type=TokenRequestGrantType.AUTHORIZATION_CODE,
    client_id="bank-client-001",
    code="auth_code_123",
    redirect_uri="https://client.examples.com/callback",
    code_verifier="pkce_verifier_123",
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

**grant_type:** `TokenRequestGrantType` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Required for authorization_code grant
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.Optional[str]` — Required for authorization_code grant
    
</dd>
</dl>

<dl>
<dd>

**code_verifier:** `typing.Optional[str]` — PKCE code verifier
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `typing.Optional[str]` — Required for refresh_token grant
    
</dd>
</dl>

<dl>
<dd>

**client_assertion_type:** `typing.Optional[TokenRequestClientAssertionType]` — For private_key_jwt authentication
    
</dd>
</dl>

<dl>
<dd>

**client_assertion:** `typing.Optional[str]` — JWT assertion for private_key_jwt authentication
    
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

<details><summary><code>client.o_auth21oidc.<a href="src/fern/o_auth21oidc/client.py">userinfo</a>() -> UserInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns user information for the authenticated user. Supports DPoP token binding.
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

client.o_auth21oidc.userinfo()

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

<details><summary><code>client.o_auth21oidc.<a href="src/fern/o_auth21oidc/client.py">introspect</a>(...) -> IntrospectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

RFC 7662 compliant token introspection endpoint for resource servers.
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

client.o_auth21oidc.introspect(
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

**token:** `str` — Token to introspect
    
</dd>
</dl>

<dl>
<dd>

**token_type_hint:** `typing.Optional[IntrospectRequestTokenTypeHint]` — Hint about token type
    
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

<details><summary><code>client.o_auth21oidc.<a href="src/fern/o_auth21oidc/client.py">pushed_authorization_request</a>(...) -> PushedAuthorizationRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

FAPI 2.0 compliant PAR endpoint for securely submitting authorization request parameters.
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
from fern.o_auth21oidc import PushedAuthorizationRequestRequestResponseType, PushedAuthorizationRequestRequestCodeChallengeMethod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth21oidc.pushed_authorization_request(
    client_id="client_id",
    response_type=PushedAuthorizationRequestRequestResponseType.CODE,
    scope="scope",
    redirect_uri="redirect_uri",
    code_challenge="code_challenge",
    code_challenge_method=PushedAuthorizationRequestRequestCodeChallengeMethod.S256,
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

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `PushedAuthorizationRequestRequestResponseType` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `PushedAuthorizationRequestRequestCodeChallengeMethod` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**nonce:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[PushedAuthorizationRequestRequestPurpose]` 
    
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

## ClientManagement
<details><summary><code>client.client_management.<a href="src/fern/client_management/client.py">register_client</a>(...) -> ClientRegistrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

RFC 7591 compliant dynamic client registration with FAPI 2.0 enhancements.
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

client.client_management.register_client(
    redirect_uris=[
        "redirect_uris"
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

**redirect_uris:** `typing.List[str]` — Authorized redirect URIs
    
</dd>
</dl>

<dl>
<dd>

**client_name:** `typing.Optional[str]` — Human-readable client name
    
</dd>
</dl>

<dl>
<dd>

**client_uri:** `typing.Optional[str]` — Client website URL
    
</dd>
</dl>

<dl>
<dd>

**grant_types:** `typing.Optional[typing.List[ClientRegistrationRequestGrantTypesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**response_types:** `typing.Optional[typing.List[ClientRegistrationRequestResponseTypesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**token_endpoint_auth_method:** `typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**token_endpoint_auth_signing_alg:** `typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg]` 
    
</dd>
</dl>

<dl>
<dd>

**require_pushed_authorization_requests:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**require_signed_request_object:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**id_token_signed_response_alg:** `typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg]` 
    
</dd>
</dl>

<dl>
<dd>

**jwks_uri:** `typing.Optional[str]` — URL for client's JWK Set
    
</dd>
</dl>

<dl>
<dd>

**industry_type:** `typing.Optional[ClientRegistrationRequestIndustryType]` 
    
</dd>
</dl>

<dl>
<dd>

**finma_license:** `typing.Optional[str]` — FINMA license number if applicable
    
</dd>
</dl>

<dl>
<dd>

**swiss_qr_support:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.client_management.<a href="src/fern/client_management/client.py">get_client_configuration</a>(...) -> ClientConfiguration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve client configuration using registration access token
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

client.client_management.get_client_configuration(
    client_id="client_id",
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

**client_id:** `str` — OAuth client identifier
    
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

<details><summary><code>client.client_management.<a href="src/fern/client_management/client.py">update_client_configuration</a>(...) -> ClientConfiguration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update client configuration using registration access token
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

client.client_management.update_client_configuration(
    client_id="client_id",
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

**client_id:** `str` — OAuth client identifier
    
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

**redirect_uris:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**jwks_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**industry_type:** `typing.Optional[ClientUpdateRequestIndustryType]` 
    
</dd>
</dl>

<dl>
<dd>

**finma_license:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**swiss_qr_support:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.client_management.<a href="src/fern/client_management/client.py">delete_client</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete client registration using registration access token
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

client.client_management.delete_client(
    client_id="client_id",
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

**client_id:** `str` — OAuth client identifier
    
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

## Discovery
<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py">openid_configuration</a>() -> OidcDiscovery</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OpenID Connect Discovery 1.0 compliant discovery document with FAPI 2.0 metadata.
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

client.discovery.openid_configuration()

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

<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py">fapi_configuration</a>() -> FapiConfiguration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

FAPI 2.0 specific configuration metadata for Swiss financial services.
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

client.discovery.fapi_configuration()

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

<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py">jwks</a>() -> JwkSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public keys for JWT signature verification (RFC 7517).
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

client.discovery.jwks()

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

<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py">swiss_banking_metadata</a>() -> SwissBankingMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Swiss Open Banking specific metadata including supported use cases and standards.
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

client.discovery.swiss_banking_metadata()

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

## ConsentManagement
<details><summary><code>client.consent_management.<a href="src/fern/consent_management/client.py">create_consent</a>(...) -> ConsentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiiert einen Consent-Flow für Datenaustausch zwischen Institutionen
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
from fern import FernApi, DataCategory
from fern.environment import FernApiEnvironment
from fern.consent_management import ConsentRequestPurpose, ConsentRequestCustomerContactMethod
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consent_management.create_consent(
    customer_id="sha256:a1b2c3d4e5f6...",
    requesting_institution="CH-BANK-001",
    providing_institution="CH-BANK-002",
    data_categories=[
        DataCategory.BASIC_DATA,
        DataCategory.IDENTIFICATION,
        DataCategory.KYC_DATA
    ],
    purpose=ConsentRequestPurpose.ACCOUNT_OPENING,
    expiry_date=datetime.datetime.fromisoformat("2024-12-31T23:59:59+00:00"),
    customer_contact_method=ConsentRequestCustomerContactMethod.EMAIL,
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

**customer_id:** `str` — Eindeutige Kunden-ID (sharedCustomerHash)
    
</dd>
</dl>

<dl>
<dd>

**requesting_institution:** `str` — Institution die Daten anfordert
    
</dd>
</dl>

<dl>
<dd>

**data_categories:** `typing.List[DataCategory]` — Angeforderte Datenkategorien
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `ConsentRequestPurpose` — Zweck der Datenverwendung
    
</dd>
</dl>

<dl>
<dd>

**expiry_date:** `datetime.datetime` — Ablaufzeitpunkt des Consents
    
</dd>
</dl>

<dl>
<dd>

**providing_institution:** `typing.Optional[str]` — Institution die Daten bereitstellt
    
</dd>
</dl>

<dl>
<dd>

**customer_contact_method:** `typing.Optional[ConsentRequestCustomerContactMethod]` — Bevorzugter Kontaktweg für Consent-Bestätigung
    
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

<details><summary><code>client.consent_management.<a href="src/fern/consent_management/client.py">get_consent_status</a>(...) -> ConsentStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ruft den aktuellen Status eines Consent-Requests ab
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

client.consent_management.get_consent_status(
    consent_id="123e4567-e89b-12d3-a456-426614174000",
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

**consent_id:** `str` 
    
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

<details><summary><code>client.consent_management.<a href="src/fern/consent_management/client.py">revoke_consent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Widerruft einen bestehenden Consent
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

client.consent_management.revoke_consent(
    consent_id="consentId",
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

**consent_id:** `str` 
    
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

## Referenzprozess
<details><summary><code>client.referenzprozess.<a href="src/fern/referenzprozess/client.py">initialize_process</a>(...) -> ProcessInitializationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiiert den universellen 10-Stufen-Referenzprozess für Customer Onboarding
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
from fern.referenzprozess import ProcessInitializationRequestIndustry, ProcessInitializationRequestUseCase, ProcessInitializationRequestCustomerContext

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.referenzprozess.initialize_process(
    industry=ProcessInitializationRequestIndustry.BANKING,
    use_case=ProcessInitializationRequestUseCase.KUNDENBEZIEHUNGSEROFFNUNG,
    customer_context=ProcessInitializationRequestCustomerContext(),
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

**industry:** `ProcessInitializationRequestIndustry` — Ziel-Ecosystem für den Prozess
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `ProcessInitializationRequestUseCase` — Spezifischer Use Case
    
</dd>
</dl>

<dl>
<dd>

**customer_context:** `ProcessInitializationRequestCustomerContext` 
    
</dd>
</dl>

<dl>
<dd>

**process_configuration:** `typing.Optional[ProcessInitializationRequestProcessConfiguration]` 
    
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

<details><summary><code>client.referenzprozess.<a href="src/fern/referenzprozess/client.py">execute_process_step</a>(...) -> ProcessStepResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Führt einen spezifischen Schritt (1-10) des Referenzprozesses aus
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

client.referenzprozess.execute_process_step(
    process_id="processId",
    step_number=1,
    step_data={
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

**process_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**step_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**step_data:** `typing.Dict[str, typing.Any]` — Step-spezifische Daten
    
</dd>
</dl>

<dl>
<dd>

**skip_to_step:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_consent:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.referenzprozess.<a href="src/fern/referenzprozess/client.py">get_process_status</a>(...) -> ProcessStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ruft den aktuellen Status und Fortschritt des Referenzprozesses ab
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

client.referenzprozess.get_process_status(
    process_id="processId",
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

**process_id:** `str` 
    
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

## CustomerData
<details><summary><code>client.customer_data.<a href="src/fern/customer_data/client.py">check_customer</a>(...) -> CustomerCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prüft ob ein Kunde bereits bei einer Institution identifiziert wurde (MVP Identifikation)
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
from fern import FernApi, BasicCustomerData
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customer_data.check_customer(
    shared_customer_hash="sha256:abc123def456...",
    basic_data=BasicCustomerData(
        last_name="Müller",
        given_name="Hans",
        birth_date=datetime.date.fromisoformat("1985-03-15"),
        nationality=[
            "CH"
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

**shared_customer_hash:** `str` — SHA-256 Hash der Grunddaten für Matching
    
</dd>
</dl>

<dl>
<dd>

**basic_data:** `BasicCustomerData` 
    
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

<details><summary><code>client.customer_data.<a href="src/fern/customer_data/client.py">request_full_customer_data</a>(...) -> FullCustomerDataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fordert das vollständige Kundendatenset an (erfordert gültigen Consent)
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
from fern.customer_data import FullDataRequestPurpose

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customer_data.request_full_customer_data(
    shared_customer_hash="sharedCustomerHash",
    purpose=FullDataRequestPurpose.ACCOUNT_OPENING,
    consent_token="consentToken",
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

**shared_customer_hash:** `str` — SHA-256 Hash des Kunden
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `FullDataRequestPurpose` 
    
</dd>
</dl>

<dl>
<dd>

**consent_token:** `str` — JWT-Token mit Consent-Nachweis
    
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

<details><summary><code>client.customer_data.<a href="src/fern/customer_data/client.py">get_customer_data</a>(...) -> CustomerDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ruft spezifische Kundendatenmodule basierend auf gewährtem Consent ab
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
from fern.customer_data import CustomerDataRequestRequestedModulesItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customer_data.get_customer_data(
    shared_customer_hash="sharedCustomerHash",
    requested_modules=[
        CustomerDataRequestRequestedModulesItem.BASISDATEN_MODULE
    ],
    consent_token="consentToken",
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

**shared_customer_hash:** `str` — SHA-256 Hash des Kunden
    
</dd>
</dl>

<dl>
<dd>

**requested_modules:** `typing.List[CustomerDataRequestRequestedModulesItem]` — Angeforderte Datenbausteine
    
</dd>
</dl>

<dl>
<dd>

**consent_token:** `str` — JWT-Token mit Consent-Nachweis
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[CustomerDataRequestPurpose]` 
    
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

## PortfolioServices
<details><summary><code>client.portfolio_services.<a href="src/fern/portfolio_services/client.py">sync_portfolio_data</a>(...) -> PortfolioSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Synchronisiert Portfolio-Daten zwischen verschiedenen Wealth Management Providern
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
from fern import FernApi, ProviderRelationship
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_services.sync_portfolio_data(
    customer_id="customerId",
    source_providers=[
        ProviderRelationship()
    ],
    target_provider="targetProvider",
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

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_providers:** `typing.List[ProviderRelationship]` 
    
</dd>
</dl>

<dl>
<dd>

**target_provider:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transfer_type:** `typing.Optional[PortfolioSyncRequestTransferType]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_categories:** `typing.Optional[typing.List[PortfolioSyncRequestAssetCategoriesItem]]` 
    
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

## Compliance
<details><summary><code>client.compliance.<a href="src/fern/compliance/client.py">perform_mi_fid_assessment</a>(...) -> MiFidAssessmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Führt MiFID II konforme Anlageeignungsprüfung durch
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

client.compliance.perform_mi_fid_assessment(
    customer_id="customerId",
    investment_objectives=[
        "investmentObjectives"
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

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**investment_objectives:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**existing_assessments:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**investment_experience:** `typing.Optional[MiFidAssessmentRequestInvestmentExperience]` 
    
</dd>
</dl>

<dl>
<dd>

**financial_situation:** `typing.Optional[MiFidAssessmentRequestFinancialSituation]` 
    
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

## AgeVerification
<details><summary><code>client.age_verification.<a href="src/fern/age_verification/client.py">verify_age</a>(...) -> AgeVerificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Privacy-preserving Altersverifikation ohne vollständige Identitätspreisgabe
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

client.age_verification.verify_age(
    customer_id="customerId",
    required_attribute="age_minimum_18",
    minimum_age=1,
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

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**required_attribute:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**minimum_age:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[AgeVerificationRequestPurpose]` 
    
</dd>
</dl>

<dl>
<dd>

**requesting_service:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attribute_only:** `typing.Optional[bool]` — Nur Attribut (ja/nein) zurückgeben
    
</dd>
</dl>

<dl>
<dd>

**data_minimization:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**existing_verification_id:** `typing.Optional[str]` 
    
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

## Identification
<details><summary><code>client.identification.<a href="src/fern/identification/client.py">get_identification_status</a>(...) -> IdentificationStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ruft den Status einer bestehenden Identifikation ab (für UC2 Re-identification)
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

client.identification.get_identification_status(
    verification_id="VER-20240115-001",
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

**verification_id:** `str` 
    
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

<details><summary><code>client.identification.<a href="src/fern/identification/client.py">verify_identification</a>(...) -> IdentificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifiziert Identifikationsdaten gegen E-ID oder andere Quellen
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
from fern.identification import IdentificationRequestIdentificationType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.identification.verify_identification(
    customer_id="customerId",
    identification_type=IdentificationRequestIdentificationType.EID_VERIFICATION,
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

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identification_type:** `IdentificationRequestIdentificationType` 
    
</dd>
</dl>

<dl>
<dd>

**document_data:** `typing.Optional[DocumentData]` 
    
</dd>
</dl>

<dl>
<dd>

**biometric_data:** `typing.Optional[BiometricData]` 
    
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

## BackgroundChecks
<details><summary><code>client.background_checks.<a href="src/fern/background_checks/client.py">perform_background_checks</a>(...) -> BackgroundChecksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Führt spezifische Background Checks (Sanctions, PEP, etc.) durch
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
from fern.background_checks import BackgroundChecksRequestCheckTypesItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.background_checks.perform_background_checks(
    customer_id="customerId",
    check_types=[
        BackgroundChecksRequestCheckTypesItem.SANCTIONS
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

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**check_types:** `typing.List[BackgroundChecksRequestCheckTypesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_data:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**baseline_date:** `typing.Optional[datetime.datetime]` — Datum für inkrementelle Updates
    
</dd>
</dl>

<dl>
<dd>

**risk_profile:** `typing.Optional[BackgroundChecksRequestRiskProfile]` 
    
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

<details><summary><code>client.background_checks.<a href="src/fern/background_checks/client.py">perform_comprehensive_checks</a>(...) -> ComprehensiveCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Führt KYC, AML, PEP und andere regulatorische Checks durch
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
from fern.background_checks import ComprehensiveCheckRequestCheckTypesItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.background_checks.perform_comprehensive_checks(
    customer_id="customerId",
    check_types=[
        ComprehensiveCheckRequestCheckTypesItem.SANCTIONS
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

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**check_types:** `typing.List[ComprehensiveCheckRequestCheckTypesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_data:** `typing.Optional[BasicCustomerData]` 
    
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

## SignatureServices
<details><summary><code>client.signature_services.<a href="src/fern/signature_services/client.py">initiate_signature</a>(...) -> SignatureResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Startet einen QES- oder eSignatur-Prozess
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
from fern import FernApi, DocumentToSign
from fern.environment import FernApiEnvironment
from fern.signature_services import SignatureRequestSignatureType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.signature_services.initiate_signature(
    customer_id="customerId",
    documents=[
        DocumentToSign(
            document_id="documentId",
            document_name="documentName",
            document_hash="documentHash",
        )
    ],
    signature_type=SignatureRequestSignatureType.QES,
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

**customer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.List[DocumentToSign]` 
    
</dd>
</dl>

<dl>
<dd>

**signature_type:** `SignatureRequestSignatureType` 
    
</dd>
</dl>

<dl>
<dd>

**notification_method:** `typing.Optional[SignatureRequestNotificationMethod]` 
    
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

<details><summary><code>client.signature_services.<a href="src/fern/signature_services/client.py">get_signature_status</a>(...) -> SignatureStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ruft den Status eines Signatur-Prozesses ab
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

client.signature_services.get_signature_status(
    signature_id="signatureId",
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

**signature_id:** `str` 
    
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

## Registry
<details><summary><code>client.registry.<a href="src/fern/registry/client.py">list_participants</a>() -> ParticipantList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listet alle aktiven Teilnehmer im föderierten System auf
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

client.registry.list_participants()

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

## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py">check</a>() -> HealthStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Überprüft die Verfügbarkeit der API
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

client.health.check()

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

