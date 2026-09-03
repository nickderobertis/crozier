# Reference
## Management
<details><summary><code>client.management.<a href="src/fern/management/client.py">post_client</a>(...) -> PostClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to add new open ID connect (OIDC) clients, it can be invoked by other modules which manages the relying parties / partners.

Each relying party can associate to one or multiple OIDC client ids.

On create, OIDC client status will be by default set to "**active**".
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
from fern.management import PostClientRequestRequest, PostClientRequestRequestAuthContextRefsItem, PostClientRequestRequestUserClaimsItem, PostClientRequestRequestGrantTypesItem, PostClientRequestRequestClientAuthMethodsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management.post_client(
    request_time=datetime.datetime.fromisoformat("2011-10-05T14:48:00+00:00"),
    request=PostClientRequestRequest(
        client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
        client_name="Fastlane e-Sim Service",
        relying_party_id="Fastlane",
        logo_uri="https://fastlane.com/fastline-esim.png",
        redirect_uris=[
            "https://fastlane.com/homepage"
        ],
        auth_context_refs=[
            PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
            PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
            PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET
        ],
        public_key={
            "kty": "RSA",
            "e": "AQAB",
            "use": "sig",
            "alg": "RS256",
            "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ"
        },
        user_claims=[
            PostClientRequestRequestUserClaimsItem.NAME,
            PostClientRequestRequestUserClaimsItem.EMAIL,
            PostClientRequestRequestUserClaimsItem.PHONE_NUMBER,
            PostClientRequestRequestUserClaimsItem.ADDRESS
        ],
        grant_types=[
            PostClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
        ],
        client_auth_methods=[
            PostClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
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

**request_time:** `datetime.datetime` — Current date and time when the request is sent
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostClientRequestRequest` 
    
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

<details><summary><code>client.management.<a href="src/fern/management/client.py">post_oauth_client</a>(...) -> PostOauthClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

Each relying party can associate with one or more client ids.

On create, client status will be by default set to "**ACTIVE**".
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
from fern.management import PostOauthClientRequestRequest, PostOauthClientRequestRequestAuthContextRefsItem, PostOauthClientRequestRequestUserClaimsItem, PostOauthClientRequestRequestGrantTypesItem, PostOauthClientRequestRequestClientAuthMethodsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management.post_oauth_client(
    request_time=datetime.datetime.fromisoformat("2011-10-05T14:48:00+00:00"),
    request=PostOauthClientRequestRequest(
        client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
        client_name="Fastlane e-Sim Service",
        client_name_lang_map={
            "fra": "Service e-Sim de Fastlane",
            "ara": "خدمة فاست لين e-SIM"
        },
        relying_party_id="Fastlane",
        logo_uri="https://fastlane.com/fastlane-esim.png",
        redirect_uris=[
            "https://fastlane.com/homepage",
            "io.mosip.residentapp://oauth"
        ],
        auth_context_refs=[
            PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
            PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
            PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET
        ],
        public_key={
            "kty": "RSA",
            "e": "AQAB",
            "use": "sig",
            "alg": "RS256",
            "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ"
        },
        user_claims=[
            PostOauthClientRequestRequestUserClaimsItem.NAME,
            PostOauthClientRequestRequestUserClaimsItem.EMAIL,
            PostOauthClientRequestRequestUserClaimsItem.PHONE_NUMBER,
            PostOauthClientRequestRequestUserClaimsItem.ADDRESS
        ],
        grant_types=[
            PostOauthClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
        ],
        client_auth_methods=[
            PostOauthClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
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

**request_time:** `datetime.datetime` — Current date and time when the request is sent
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostOauthClientRequestRequest` 
    
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

<details><summary><code>client.management.<a href="src/fern/management/client.py">post_client_mgmt_client</a>(...) -> PostClientMgmtClientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

Each relying party can associate with one or more client ids.

On create, client status will be by default set to "**ACTIVE**".
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
from fern import FernApi, Purpose, PurposeType
from fern.environment import FernApiEnvironment
import datetime
from fern.management import PostClientMgmtClientRequestRequest, PostClientMgmtClientRequestRequestAuthContextRefsItem, PostClientMgmtClientRequestRequestUserClaimsItem, PostClientMgmtClientRequestRequestGrantTypesItem, PostClientMgmtClientRequestRequestClientAuthMethodsItem, PostClientMgmtClientRequestRequestAdditionalConfig, PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management.post_client_mgmt_client(
    request_time=datetime.datetime.fromisoformat("2011-10-05T14:48:00+00:00"),
    request=PostClientMgmtClientRequestRequest(
        client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
        client_name="Fastlane e-Sim Service",
        client_name_lang_map={
            "fra": "Service e-Sim de Fastlane",
            "ara": "خدمة فاست لين e-SIM"
        },
        relying_party_id="Fastlane",
        logo_uri="https://fastlane.com/fastlane-esim.png",
        redirect_uris=[
            "https://fastlane.com/homepage",
            "io.mosip.residentapp://oauth"
        ],
        auth_context_refs=[
            PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
            PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
            PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET
        ],
        public_key={
            "kty": "RSA",
            "e": "AQAB",
            "use": "sig",
            "alg": "RS256",
            "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ"
        },
        user_claims=[
            PostClientMgmtClientRequestRequestUserClaimsItem.NAME,
            PostClientMgmtClientRequestRequestUserClaimsItem.EMAIL,
            PostClientMgmtClientRequestRequestUserClaimsItem.PHONE_NUMBER,
            PostClientMgmtClientRequestRequestUserClaimsItem.ADDRESS
        ],
        grant_types=[
            PostClientMgmtClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
        ],
        client_auth_methods=[
            PostClientMgmtClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
        ],
        additional_config=PostClientMgmtClientRequestRequestAdditionalConfig(
            userinfo_response_type=PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType.JWS,
            purpose=Purpose(
                type=PurposeType.VERIFY,
                title={
                    "@none": "Title"
                },
                sub_title={
                    "@none": "subTitle"
                },
            ),
            signup_banner_required=True,
            forgot_pwd_link_required=True,
            consent_expire_in_mins=30,
            require_pushed_authorization_requests=True,
            dpop_bound_access_tokens=True,
        ),
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

**request_time:** `datetime.datetime` — Current date and time when the request is sent
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostClientMgmtClientRequestRequest` 
    
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

<details><summary><code>client.management.<a href="src/fern/management/client.py">put_oidc_client_client_id</a>(...) -> PutOidcClientClientIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to update existing Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

**Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.
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
from fern.management import PutOidcClientClientIdRequestRequest, PutOidcClientClientIdRequestRequestStatus, PutOidcClientClientIdRequestRequestUserClaimsItem, PutOidcClientClientIdRequestRequestAuthContextRefsItem, PutOidcClientClientIdRequestRequestGrantTypesItem, PutOidcClientClientIdRequestRequestClientAuthMethodsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management.put_oidc_client_client_id(
    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
    request_time="2011-10-05T14:48:00.000Z",
    request=PutOidcClientClientIdRequestRequest(
        client_name="Fastlane e-Sim Service",
        status=PutOidcClientClientIdRequestRequestStatus.ACTIVE,
        logo_uri="https://fastline.com/logo.png",
        redirect_uris=[
            "https://fastlane.com/homepage",
            "https://fastlane-dev.com/*",
            "fastlaneapp://oauth/*"
        ],
        user_claims=[
            PutOidcClientClientIdRequestRequestUserClaimsItem.NAME,
            PutOidcClientClientIdRequestRequestUserClaimsItem.EMAIL,
            PutOidcClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
            PutOidcClientClientIdRequestRequestUserClaimsItem.ADDRESS
        ],
        auth_context_refs=[
            PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
            PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
            PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET
        ],
        grant_types=[
            PutOidcClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
        ],
        client_auth_methods=[
            PutOidcClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
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

**client_id:** `str` — Client Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` — Current date and time when the request is sent
    
</dd>
</dl>

<dl>
<dd>

**request:** `PutOidcClientClientIdRequestRequest` 
    
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

<details><summary><code>client.management.<a href="src/fern/management/client.py">put_oauth_client_client_id</a>(...) -> PutOauthClientClientIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

**Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.
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
from fern.management import PutOauthClientClientIdRequestRequest, PutOauthClientClientIdRequestRequestStatus, PutOauthClientClientIdRequestRequestUserClaimsItem, PutOauthClientClientIdRequestRequestAuthContextRefsItem, PutOauthClientClientIdRequestRequestGrantTypesItem, PutOauthClientClientIdRequestRequestClientAuthMethodsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management.put_oauth_client_client_id(
    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
    request_time="2011-10-05T14:48:00.000Z",
    request=PutOauthClientClientIdRequestRequest(
        client_name="Fastlane e-Sim Service",
        client_name_lang_map={
            "fra": "Service e-Sim de Fastlane",
            "ara": "خدمة فاست لين e-SIM"
        },
        status=PutOauthClientClientIdRequestRequestStatus.ACTIVE,
        logo_uri="https://fastlane.com/logo.png",
        redirect_uris=[
            "https://fastlane.com/homepage",
            "http://fastlane-dev.com/*",
            "fastlaneapp://oauth/*"
        ],
        user_claims=[
            PutOauthClientClientIdRequestRequestUserClaimsItem.NAME,
            PutOauthClientClientIdRequestRequestUserClaimsItem.EMAIL,
            PutOauthClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
            PutOauthClientClientIdRequestRequestUserClaimsItem.ADDRESS
        ],
        auth_context_refs=[
            PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
            PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
            PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET
        ],
        grant_types=[
            PutOauthClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
        ],
        client_auth_methods=[
            PutOauthClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
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

**client_id:** `str` — Client Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` — Current date and time when the request is sent
    
</dd>
</dl>

<dl>
<dd>

**request:** `PutOauthClientClientIdRequestRequest` 
    
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

<details><summary><code>client.management.<a href="src/fern/management/client.py">put_client_client_id</a>(...) -> PutClientClientIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

**Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.
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
from fern import FernApi, Purpose, PurposeType
from fern.environment import FernApiEnvironment
from fern.management import PutClientClientIdRequestRequest, PutClientClientIdRequestRequestStatus, PutClientClientIdRequestRequestUserClaimsItem, PutClientClientIdRequestRequestAuthContextRefsItem, PutClientClientIdRequestRequestGrantTypesItem, PutClientClientIdRequestRequestClientAuthMethodsItem, PutClientClientIdRequestRequestAdditionalConfig, PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management.put_client_client_id(
    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
    request_time="2011-10-05T14:48:00.000Z",
    request=PutClientClientIdRequestRequest(
        client_name="Fastlane e-Sim Service",
        client_name_lang_map={
            "fra": "Service e-Sim de Fastlane",
            "ara": "خدمة فاست لين e-SIM"
        },
        status=PutClientClientIdRequestRequestStatus.ACTIVE,
        logo_uri="https://fastlane.com/logo.png",
        redirect_uris=[
            "https://fastlane.com/homepage",
            "http://fastlane-dev.com/*",
            "fastlaneapp://oauth/*"
        ],
        user_claims=[
            PutClientClientIdRequestRequestUserClaimsItem.NAME,
            PutClientClientIdRequestRequestUserClaimsItem.EMAIL,
            PutClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
            PutClientClientIdRequestRequestUserClaimsItem.ADDRESS
        ],
        auth_context_refs=[
            PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
            PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
            PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET
        ],
        grant_types=[
            PutClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
        ],
        client_auth_methods=[
            PutClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
        ],
        additional_config=PutClientClientIdRequestRequestAdditionalConfig(
            userinfo_response_type=PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType.JWS,
            purpose=Purpose(
                type=PurposeType.VERIFY,
                title={
                    "@none": "Title"
                },
                sub_title={
                    "@none": "subTitle"
                },
            ),
            signup_banner_required=True,
            forgot_pwd_link_required=True,
            consent_expire_in_mins=30,
            require_pushed_authorization_requests=False,
            dpop_bound_access_tokens=True,
        ),
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

**client_id:** `str` — Client Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` — Current date and time when the request is sent
    
</dd>
</dl>

<dl>
<dd>

**request:** `PutClientClientIdRequestRequest` 
    
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

<details><summary><code>client.management.<a href="src/fern/management/client.py">patch_client_client_id</a>(...) -> PatchClientClientIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API to partially update existing OAuth/Open ID Connect (OIDC) client. Only provided fields will be updated.

**Special handling for encPublicKey:**
- When set/updated: validates format and computes enc_public_key_hash
- When explicitly set to null: clears both enc_public_key and enc_public_key_hash
- When not present in request: leaves both fields unchanged

**Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.
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
from fern.management import PatchClientClientIdRequestRequest, PatchClientClientIdRequestRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management.patch_client_client_id(
    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
    request_time="2024-01-15T10:30:00.000Z",
    request=PatchClientClientIdRequestRequest(
        status=PatchClientClientIdRequestRequestStatus.INACTIVE,
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

**client_id:** `str` — Client Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` — Current date and time when the request is sent
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchClientClientIdRequestRequest` — All fields are optional. Only provided fields will be updated.
    
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

## OIDC
<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">get_authorize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is the authorize endpoint of Open ID Connect (OIDC). The relying party applications will do a browser redirect to this endpoint with all required details passed as query parameters.

This endpoint will respond with a basic HTML page to load a JS application in the browser. UI JS application will then echo all the query parameters received in this endpoint to the "/authorization/oauth-details" endpoint as the request body.

All the validations on the query parameter values will be performed in the "/authorization/oauth-details" endpoint.

**Authentication & Authroization**: None
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
from fern.oidc import GetAuthorizeRequestScope, GetAuthorizeRequestResponseType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.oidc.get_authorize(
    scope=GetAuthorizeRequestScope.OPENID,
    response_type=GetAuthorizeRequestResponseType.CODE,
    client_id="client_id",
    redirect_uri="redirect_uri",
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

**scope:** `GetAuthorizeRequestScope` — Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `GetAuthorizeRequestResponseType` — The value set here determines the authorization processing flow. To use the Authorization Code Flow, the value should be configured to "code".
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — Valid OAuth 2.0 Client Identifier in the Authorization Server.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — Redirection URI to which the response would be sent. This URI must match one of the redirection URI values during the client ID creation.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — Opaque value used to maintain state between the request and the callback. Typically, Cross-Site Request Forgery (CSRF, XSRF) mitigation is done by cryptographically binding the value of this parameter with a browser cookie.
    
</dd>
</dl>

<dl>
<dd>

**nonce:** `typing.Optional[str]` — String value used to associate a Client session with an ID Token, and to mitigate replay attacks. The value is passed through unmodified from the Authentication Request to the ID Token.
    
</dd>
</dl>

<dl>
<dd>

**display:** `typing.Optional[GetAuthorizeRequestDisplay]` — ASCII string value that specifies how the Authorization Server displays the authentication and consent user interface pages to the end user.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[GetAuthorizeRequestPrompt]` — Space delimited case-sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent.
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[float]` — Maximum Authentication Age. This specifies the allowable elapsed time in seconds since the last time the end user was actively authenticated by the OP. If the elapsed time is greater than this value, then the OP MUST attempt to actively re-authenticate the end user. The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter. When max_age is used, the ID Token returned MUST include an auth_time claim value.
    
</dd>
</dl>

<dl>
<dd>

**ui_locales:** `typing.Optional[str]` — End user's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.
    
</dd>
</dl>

<dl>
<dd>

**acr_values:** `typing.Optional[GetAuthorizeRequestAcrValues]` — Requested Authentication Context Class Reference values. Space-separated string that specifies the acr values that the Authorization Server is being requested to use for processing this Authentication Request, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value, as specified in Section 2. The acr Claim is requested as a Voluntary Claim by this parameter.
    
</dd>
</dl>

<dl>
<dd>

**claims_locales:** `typing.Optional[str]` — End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.
    
</dd>
</dl>

<dl>
<dd>

**claims:** `typing.Optional[str]` — This parameter is used to request specific claims to be returned. The value is a JSON object listing the requested claims. The claims parameter value is represented in an OAuth 2.0 request as UTF-8 encoded JSON.
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `typing.Optional[str]` — A challenge derived from the code_verifier, This is required if its a VC scoped request.
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `typing.Optional[str]` — A method that was used to derive code challenge, This will be required if code_challenge is provided.
    
</dd>
</dl>

<dl>
<dd>

**id_token_hint:** `typing.Optional[str]` — ID Token previously issued by the Authorization Server being passed as a hint about the End-User's current or past authenticated session with the Client.
    
</dd>
</dl>

<dl>
<dd>

**request_uri:** `typing.Optional[str]` — The request URI corresponding to the pushed authorization request posted. This URI is a single-use reference to the respective request data in the subsequent authorization request.
    
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

<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">post_token</a>(...) -> PostTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once the client / relying party application receives the authorization code through redirect, this OIDC complaint endpoint will be called from the relying party backend application to get the ID and access token.

1. The only supported client authentication methods : <b>private_key_jwt</b>
2. clientAssertion is a signed JWT with Clients private key, corresponding public key should be shared with IdP during the OIDC client registration process.
3. clientAssertion JWT payload must be as below: 

The JWT MUST contain the following REQUIRED Claim Values and MAY contain the additional OPTIONAL Claim Values:

**iss**<span style="color:#FF0000">*</span> (Issuer): This MUST contain the client_id of the OAuth Client.

**sub**<span style="color:#FF0000">*</span> (Subject): This MUST contain the client_id of the OAuth Client.

**aud**<span style="color:#FF0000">*</span> (Audience): Value that identifies the authorization server as an intended audience. The authorization server MUST verify that it is an intended audience for the token. The audience SHOULD be the URL of the authorization server's token endpoint.

**exp**<span style="color:#FF0000">*</span> (Expiration): Time on or after which the ID token MUST NOT be accepted for processing.

**iat**<span style="color:#FF0000">*</span>: Time at which the JWT was issued.</p>

**jti**<span style="color:#FF0000">*</span> (JWT ID): This MUST be unique random string for each client assertion generated.

**Note**: The Client Assertion JWT can contain other Claims. Any Claims used that are not understood WILL be ignored.</p>
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
from fern.oidc import PostTokenRequestGrantType, PostTokenRequestClientAssertionType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.oidc.post_token(
    grant_type=PostTokenRequestGrantType.AUTHORIZATION_CODE,
    code="tyemdnjdfornfedg",
    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv-kV7VBcnzvY",
    client_assertion_type=PostTokenRequestClientAssertionType.URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER,
    client_assertion="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTg2MzE0NjAsIm5iZiI6MTY5ODYzMTQ2MCwiZXhwIjoxNjk4NjMxNTI1LCJqdGkiOiI1ZFFjaWhtb2lfQTlXMmlERGpYcDgiLCJzdWIiOiJXTVg1cE82ZFlkQ0ZSM2lhVldHY2xWUE54VE5TQUREdi1rVjdWQmNuenZZIiwiaXNzIjoiV01YNXBPNmRZZENGUjNpYVZXR2NsVlBOeFROU0FERHYta1Y3VkJjbnp2WSIsImF1ZCI6Imh0dHBzOi8vZXNpZ25ldC5jb2xsYWIubW9zaXAubmV0L3YxL2VzaWduZXQvb2F1dGgvdG9rZW4ifQ.G-OxPmb2wBq7R52PELNss9FCwvv_i2456FE4oag25BuZjwH6CgB8LDLmfCJdzeLGRuFp_MrKskGTkpsWI0RWLNtqZ7jvQTvSq8zQICusIFh9kcciWbkMsOZQqN91gPtdrn3WRS6xD7TxzwvrAeuqx4lTBbWNYTF2GQ3Zagq0t6ogOtPWg0wNioW3m11jWIdwooJ8jI2Z5oN772Lerrs1AXMnipLxQm4rdMM54taeHFrrXyxqFjoiq-bglrpHtCqeG6QFqhpQrRlIsLLoli8F1LU8Mu3Fw7ifCd6KEj9JNM_sPHjAy-JRg_dgjNdHL5tqtHzUsD5sSmLop33U4WH3Ow",
    redirect_uri="https://fastlane.com/homepage",
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

**grant_type:** `PostTokenRequestGrantType` — Authorization code grant type.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — Authorization code, sent as query param in the client's redirect URI.
    
</dd>
</dl>

<dl>
<dd>

**client_assertion_type:** `PostTokenRequestClientAssertionType` — Type of the client assertion part of this request.
    
</dd>
</dl>

<dl>
<dd>

**client_assertion:** `str` — Private key signed JWT, This JWT payload structure is defined above as part of request description.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — Valid client redirect_uri. Must be same as the one sent in the authorize call.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client Id of the OIDC client.
    
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

<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">post_token_v2</a>(...) -> PostTokenV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once the client / relying party application receives the authorization code through redirect, this OIDC complaint endpoint will be called from the relying party backend application to get the ID and access token.

1. The only supported client authentication methods : <b>private_key_jwt</b>
2. clientAssertion is a signed JWT with Clients private key, corresponding public key should be shared with IdP during the OIDC client registration process.
3. clientAssertion JWT payload must be as below: 

The JWT MUST contain the following REQUIRED Claim Values and MAY contain the additional OPTIONAL Claim Values:

**iss**<span style="color:#FF0000">*</span> (Issuer): This MUST contain the client_id of the OAuth Client.

**sub**<span style="color:#FF0000">*</span> (Subject): This MUST contain the client_id of the OAuth Client.

**aud**<span style="color:#FF0000">*</span> (Audience): Value that identifies the authorization server as an intended audience. The authorization server MUST verify that it is an intended audience for the token. The audience SHOULD be the URL of the authorization server's token endpoint.

**exp**<span style="color:#FF0000">*</span> (Expiration): Time on or after which the ID token MUST NOT be accepted for processing.

**iat**<span style="color:#FF0000">*</span>: Time at which the JWT was issued.</p>

**jti**<span style="color:#FF0000">*</span> (JWT ID): This MUST be unique for each client assertion generated.

**Note**: The Client Assertion JWT can contain other Claims. Any Claims used that are not understood WILL be ignored.</p>
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
from fern.oidc import PostTokenV2RequestGrantType, PostTokenV2RequestClientAssertionType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.oidc.post_token_v2(
    grant_type=PostTokenV2RequestGrantType.AUTHORIZATION_CODE,
    code="tyemdnjdfornfedg",
    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv-kV7VBcnzvY",
    client_assertion_type=PostTokenV2RequestClientAssertionType.URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER,
    client_assertion="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTg2MzE0NjAsIm5iZiI6MTY5ODYzMTQ2MCwiZXhwIjoxNjk4NjMxNTI1LCJqdGkiOiI1ZFFjaWhtb2lfQTlXMmlERGpYcDgiLCJzdWIiOiJXTVg1cE82ZFlkQ0ZSM2lhVldHY2xWUE54VE5TQUREdi1rVjdWQmNuenZZIiwiaXNzIjoiV01YNXBPNmRZZENGUjNpYVZXR2NsVlBOeFROU0FERHYta1Y3VkJjbnp2WSIsImF1ZCI6Imh0dHBzOi8vZXNpZ25ldC5jb2xsYWIubW9zaXAubmV0L3YxL2VzaWduZXQvb2F1dGgvdG9rZW4ifQ.G-OxPmb2wBq7R52PELNss9FCwvv_i2456FE4oag25BuZjwH6CgB8LDLmfCJdzeLGRuFp_MrKskGTkpsWI0RWLNtqZ7jvQTvSq8zQICusIFh9kcciWbkMsOZQqN91gPtdrn3WRS6xD7TxzwvrAeuqx4lTBbWNYTF2GQ3Zagq0t6ogOtPWg0wNioW3m11jWIdwooJ8jI2Z5oN772Lerrs1AXMnipLxQm4rdMM54taeHFrrXyxqFjoiq-bglrpHtCqeG6QFqhpQrRlIsLLoli8F1LU8Mu3Fw7ifCd6KEj9JNM_sPHjAy-JRg_dgjNdHL5tqtHzUsD5sSmLop33U4WH3Ow",
    redirect_uri="https://fastlane.com/homepage",
    code_verifier="MN1Q0nNAKkqOu5EaNBKf2gYD4maYv9ZxLd-48N2_kTM",
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

**grant_type:** `PostTokenV2RequestGrantType` — Authorization code grant type.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — Authorization code, sent as query param in the client's redirect URI.
    
</dd>
</dl>

<dl>
<dd>

**client_assertion_type:** `PostTokenV2RequestClientAssertionType` — Type of the client assertion part of this request.
    
</dd>
</dl>

<dl>
<dd>

**client_assertion:** `str` — Private key signed JWT, This JWT payload structure is defined above as part of request description.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — Valid client redirect_uri. Must be same as the one sent in the authorize call.
    
</dd>
</dl>

<dl>
<dd>

**d_po_p:** `typing.Optional[str]` — A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client Id of the OIDC client.
    
</dd>
</dl>

<dl>
<dd>

**code_verifier:** `typing.Optional[str]` 

A cryptographically random string that is used to correlate the
      authorization request to the token request.
    
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

<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">get_userinfo</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once the access token is received via the token endpoint, relying party backend application can call this OIDC compliant endpoint to request for the user claims.

Consented user claims will be returned as a JWT. This JWT will be a nested JWT which is a signed using JWS and then encrypted using JWE. 


**Example**: Assuming the below are the requested claims by the relying party

name : { "essential" : true }

phone: { "essential" : true }

**Response 1**: When consent is provided for both name and phone number:

{ "name" : "John Doe", "phone" : "033456743" }

**Response 2**: When consent is provided for only name:

{ "name" : "John Doe" }

**Response 3**: When Claims are requested with claims_locales : "en fr"

{ "name#en" : "John Doe", "name#fr" : "Jean Doe", "phone" : "033456743" } 

**Supported User Info Claims**
<ul>
<li>sub - Partner Specific User Token (PSUT)</li>
<li>name</li>
<li>address</li>
<li>gender</li>
<li>birthdate</li>
<li>profile photo</li>
<li>email</li>
<li>phone</li>
<li>locale</li>
<li>Custom - individual_id (You share this claim as a system-level config and it can be UIN, perceptual VID or temporary VID)</li>
</ul>
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

client.oidc.get_userinfo()

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

**d_po_p:** `typing.Optional[str]` — A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2
    
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

<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">get_certs</a>() -> GetCertsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to fetch all the public keys of the eSignet server. Returns public key set in the JWKS format.
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

client.oidc.get_certs()

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

<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">get_well_known_openid_configuration</a>() -> GetWellKnownOpenidConfigurationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open ID Connect dynamic provider discovery is not supported currently, this endpoint is only for facilitating the OIDC provider details in a standard way.

**Reference**: https://openid.net/specs/openid-connect-discovery-1_0.html
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

client.oidc.get_well_known_openid_configuration()

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

<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">get_introspect</a>(...) -> GetIntrospectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint takes an access token or ID token and returns a boolean that indicates whether it is active. If the token is active, additional data about the token is also returned. If the token is invalid, expired, or revoked, it is considered inactive.

**Reference**: https://www.rfc-editor.org/rfc/rfc7662.html
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
from fern.oidc import GetIntrospectRequestTokenTypeHint

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.oidc.get_introspect(
    token="token",
    token_type_hint=GetIntrospectRequestTokenTypeHint.ACCESS_TOKEN,
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

**token:** `str` — An access token or ID token
    
</dd>
</dl>

<dl>
<dd>

**token_type_hint:** `GetIntrospectRequestTokenTypeHint` — Indicates the type of token being passed. Valid values: access_token, id_token
    
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

<details><summary><code>client.oidc.<a href="src/fern/oidc/client.py">post_oauth_par</a>(...) -> PostOauthParResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**PAR - Pushed Authorization Request**

1. Message body of an this request with parameters formatted with x-www-form-urlencoded using a character encoding of UTF-8
2. Add "pushed_authorization_request_endpoint" in the authorization server metadata.
3. Client must adds its authentication credentials to the request body using the same rules as for token endpoint request.
4. Authenticate the client in the same way as at the token endpoint.
5. Reject the request if the request_uri authorization request parameter is provided.
6. Validate the request parmeters in the body as it would be validated in oauth-details request.
7. Upon successful verification, the server MUST generate a request URI and provide it in the response with a 201 HTTP status code.

**request_uri** should be in this format: 'urn:ietf:params:oauth:request_uri:<secure random alpha-numeric string with max length of 25>'

Successfully verified request parameters should be stored in the "par" cache with request_uri as the key. Objects in the "par" cache are set with TTL.
TTL should be configurable and the expires_in parameter in the response should return same value.

**Not supported:**
  1. client authentication parameters in the PAR request header.
  2. The request parameter as defined in JAR [RFC9101].
  3. API rate limit is left to the infra to handle.
  4. Use of non-registered redirect_uri's are not allowed.
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
from fern import FernApi, Claim, ClaimUserinfo, ClaimDetail
from fern.environment import FernApiEnvironment
from fern.oidc import PostOauthParRequestScope, PostOauthParRequestResponseType, PostOauthParRequestCodeChallengeMethod, PostOauthParRequestClientAssertionType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.oidc.post_oauth_par(
    scope=PostOauthParRequestScope.OPENID,
    response_type=PostOauthParRequestResponseType.CODE,
    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
    redirect_uri="https://fastlane.com/homepage",
    state="eree2311",
    nonce="973eieljzng",
    display="popup",
    prompt="login",
    acr_values="mosip:idp:acr:generated-code",
    claims=Claim(
        userinfo=ClaimUserinfo(
            name=ClaimDetail(
                essential=True,
            ),
            email=ClaimDetail(
                essential=False,
            ),
            phone_number=ClaimDetail(
                essential=True,
            ),
            address=ClaimDetail(
                essential=True,
            ),
        ),
    ),
    claims_locales="en",
    code_challenge="UK95aVX_y3R44DF3hssd3wATvtZmO_WejE0P33-pwTs",
    code_challenge_method=PostOauthParRequestCodeChallengeMethod.S256,
    client_assertion_type=PostOauthParRequestClientAssertionType.URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER,
    client_assertion="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJXTVg1cE82ZFlkQ0ZSM2lhVldHY2xWUE54VE5TQUREdiIsImlzcyI6IldNWDVwTzZkWWRDRlIzaWFWV0djbFZQTnhUTlNBRER2IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6ODA4MC92MS9lc2lnbmV0L29hdXRoL3BhciIsImlhdCI6MTUxNjIzOTAyMn0.B250eeJsmBesAlYXhK-QUSi6bLOFqHCaKgXocGgUJvp5XjaiWLH1H722pjaXRaK3Eczs3HTW8RxDKQefiT6AIm4ZgQjacNZzlzca_tIc8-5_WWzVUAIfvv6NJ9SLTKJdlvXJKFhhCeLrCsvENJsfZRborkrh-cVMod3iLTK3lPFz0ylwhZ5NV1L9mgVM-0-HQO3HnG0UI0zokmZXDzkmrJsnMV_NPkSnJsaxpGsw9R9Ma5RTGqg7_l-okB5EadUoOMV8OKnloqzja1NXrBGCQZoAq2GDg9bchgHaQoTnZXpaVLgGWxlHOkLXGj15aK_JzGf_JOBRg12mamatWj_ZYA",
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

**scope:** `PostOauthParRequestScope` — Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `PostOauthParRequestResponseType` — Value that determines the authorization processing flow to be used. When using the Authorization Code Flow, this value is code.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — OAuth 2.0 Client Identifier valid at the Authorization Server
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — Redirection URI to which the response will be sent. This URI MUST exactly match one of the Redirection URI values for the Client pre-registered
    
</dd>
</dl>

<dl>
<dd>

**client_assertion_type:** `PostOauthParRequestClientAssertionType` — Type of the client assertion part of this request.
    
</dd>
</dl>

<dl>
<dd>

**client_assertion:** `str` — The value of the "client_assertion" parameter contains a single JWT.
    
</dd>
</dl>

<dl>
<dd>

**d_po_p:** `typing.Optional[str]` — A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — client state value echoed.
    
</dd>
</dl>

<dl>
<dd>

**nonce:** `typing.Optional[str]` — Client's nonce value echoed.
    
</dd>
</dl>

<dl>
<dd>

**display:** `typing.Optional[str]` — ASCII string value that specifies how the Authorization Server displays the authentication and consent user interface pages to the End-User.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Space delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent.
    
</dd>
</dl>

<dl>
<dd>

**acr_values:** `typing.Optional[str]` 

Space separated ACR values, Unknown ACR are ignored. Only registered ACR values will be considered.
If none of the provided acr value is among the registered values, all the registered ACR's will be considered.
    
</dd>
</dl>

<dl>
<dd>

**claims:** `typing.Optional[Claim]` 
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[float]` — Maximum Authentication Age. Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OP. If the elapsed time is greater than this value, the OP MUST attempt to actively re-authenticate the End-User. (The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter.) When max_age is used, the ID Token returned MUST include an auth_time Claim Value.
    
</dd>
</dl>

<dl>
<dd>

**claims_locales:** `typing.Optional[str]` — End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.
    
</dd>
</dl>

<dl>
<dd>

**ui_locales:** `typing.Optional[str]` — End-User's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `typing.Optional[str]` — A challenge derived from the code verifier, to be verified against later.
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `typing.Optional[PostOauthParRequestCodeChallengeMethod]` — A method that was used to derive code challenge.
    
</dd>
</dl>

<dl>
<dd>

**id_token_hint:** `typing.Optional[str]` — ID Token previously issued by the Authorization Server being passed as a hint about the End-User's current or past authenticated session with the Client.
    
</dd>
</dl>

<dl>
<dd>

**dpop_jkt:** `typing.Optional[str]` — The value of the dpop_jkt authorization request parameter is the JWK Thumbprint [RFC7638] of the proof-of-possession public key using the SHA-256 hash function.
    
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

## UI
<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_oauth_details</a>(...) -> PostOauthDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OAuth details request is raised from the UI JS application on page load.

OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

1. Validates the clientId.
2. validates redirectUri is one of the redirectUri during client create/update.
3. validates display,responseType,prompts values are part of supported values in Idp properties.
4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
7. Claims considered only if part of registered claims.
8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.
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
from fern import FernApi, Claim, ClaimUserinfo, ClaimDetail
from fern.environment import FernApiEnvironment
from fern.ui import PostOauthDetailsRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_oauth_details(
    xsrf_token="X-XSRF-TOKEN",
    request_time="2022-09-22T08:01:10.000Z",
    request=PostOauthDetailsRequestRequest(
        scope="openid profile",
        response_type="code",
        client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
        redirect_uri="https://fastlane.com/homepage",
        state="eree2311",
        nonce="973eieljzng",
        display="popup",
        prompt="login",
        acr_values="mosip:idp:acr:generated-code",
        claims=Claim(
            userinfo=ClaimUserinfo(
                name=ClaimDetail(
                    essential=True,
                ),
                email=ClaimDetail(
                    essential=False,
                ),
                phone_number=ClaimDetail(
                    essential=True,
                ),
                address=ClaimDetail(
                    essential=True,
                ),
            ),
        ),
        claims_locales="en",
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

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostOauthDetailsRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_oauth_details_v2</a>(...) -> PostOauthDetailsV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OAuth details request is raised from the UI JS application on page load.

OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

1. Validates the clientId.
2. validates redirectUri is one of the redirectUri during client create/update.
3. validates display,responseType,prompts values are part of supported values in Idp properties.
4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
7. claims considered only if part of registered claims.
8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.
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
from fern import FernApi, Claim, ClaimUserinfo, ClaimDetail
from fern.environment import FernApiEnvironment
from fern.ui import PostOauthDetailsV2RequestRequest, PostOauthDetailsV2RequestRequestCodeChallengeMethod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_oauth_details_v2(
    xsrf_token="X-XSRF-TOKEN",
    request_time="2022-09-22T08:01:10.000Z",
    request=PostOauthDetailsV2RequestRequest(
        scope="openid profile",
        response_type="code",
        client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
        redirect_uri="https://fastlane.com/homepage",
        state="eree2311",
        nonce="973eieljzng",
        display="popup",
        prompt="login",
        acr_values="mosip:idp:acr:generated-code",
        claims=Claim(
            userinfo=ClaimUserinfo(
                name=ClaimDetail(
                    essential=True,
                ),
                email=ClaimDetail(
                    essential=False,
                ),
                phone_number=ClaimDetail(
                    essential=True,
                ),
                address=ClaimDetail(
                    essential=True,
                ),
            ),
        ),
        claims_locales="en",
        code_challenge="UK95aVX_y3R44DF3hssd3wATvtZmO_WejE0P33-pwTs",
        code_challenge_method=PostOauthDetailsV2RequestRequestCodeChallengeMethod.S256,
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

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostOauthDetailsV2RequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_oauth_details_v3</a>(...) -> PostOauthDetailsV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OAuth details request is raised from the UI JS application on page load.

OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

1. Validates the clientId.
2. validates redirectUri is one of the redirectUri during client create/update.
3. validates display,responseType,prompts values are part of supported values in Idp properties.
4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
7. claims considered only if part of registered claims.
8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.
9. Unknown or unsupported claims in the verified_claims parameter are ignored. 
10. idTokenHint is optional, if provided then it MUST be a valid JWT. 'sub' claim in the idTokenHint JWT payload must match the cookie name(set on the domain).If the cookie is not found with same name as of 'sub' claim, then the error is thrown.
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
from fern import FernApi, Claim, ClaimUserinfo, ClaimDetail
from fern.environment import FernApiEnvironment
from fern.ui import PostOauthDetailsV3RequestRequest, PostOauthDetailsV3RequestRequestCodeChallengeMethod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_oauth_details_v3(
    xsrf_token="X-XSRF-TOKEN",
    request_time="2022-09-22T08:01:10.000Z",
    request=PostOauthDetailsV3RequestRequest(
        scope="openid profile",
        response_type="code",
        client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
        redirect_uri="https://fastlane.com/homepage",
        state="eree2311",
        nonce="973eieljzng",
        display="popup",
        prompt="login",
        acr_values="mosip:idp:acr:generated-code",
        claims=Claim(
            userinfo=ClaimUserinfo(
                name=ClaimDetail(
                    essential=True,
                ),
                email=ClaimDetail(
                    essential=False,
                ),
                phone_number=ClaimDetail(
                    essential=True,
                ),
                address=ClaimDetail(
                    essential=True,
                ),
            ),
        ),
        claims_locales="en",
        code_challenge="UK95aVX_y3R44DF3hssd3wATvtZmO_WejE0P33-pwTs",
        code_challenge_method=PostOauthDetailsV3RequestRequestCodeChallengeMethod.S256,
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

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostOauthDetailsV3RequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_send_otp</a>(...) -> PostSendOtpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

When end user want to authenticate using OTP auth factor, he/she will enter their individual id (UIN/VID) and click on the "Generate OTP" button on the UI application. Then this endpoint will be invoked by the JS UI application.

Since the OTP generation and delivery to end user is to be handled by the integrated authentication system, the request will be relayed to the same.

1. Validates the transactionId.
2. Validates null / empty individualId.
3. Validates captchaToken, if enabled.
3. Delegates the call to integrated authentication system.
4. Relays error from authentication system to UI on failure.
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
from fern.ui import PostSendOtpRequestRequest, PostSendOtpRequestRequestOtpChannelsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_send_otp(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostSendOtpRequestRequest(
        transaction_id="vKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        individual_id="464737289558",
        otp_channels=[
            PostSendOtpRequestRequestOtpChannelsItem.PHONE,
            PostSendOtpRequestRequestOtpChannelsItem.EMAIL
        ],
        captcha_token="ALSKDJFURIEOQPZMKFURHFVBH",
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostSendOtpRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_send_linked_otp</a>(...) -> PostSendLinkedOtpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

When end user want to authenticate using OTP auth factor, he/she will enter their individual id (UIN/VID) and click on the "Generate OTP" button on the UI application. Then this endpoint will be invoked by wallet app with linked transactionId.

Since the OTP generation and delivery to end user is to be handled by the integrated authentication system, the request will be relayed to the same.

1. Validates the linked transactionId.
2. Validates null / empty individualId.
3. Delegates the call to integrated authentication system.
4. Relays error from authentication system to UI on failure.
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
from fern.ui import PostSendLinkedOtpRequestRequest, PostSendLinkedOtpRequestRequestOtpChannelsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_send_linked_otp(
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostSendLinkedOtpRequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        individual_id="464737289558",
        otp_channels=[
            PostSendLinkedOtpRequestRequestOtpChannelsItem.PHONE,
            PostSendLinkedOtpRequestRequestOtpChannelsItem.EMAIL
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

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostSendLinkedOtpRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_authenticate</a>(...) -> PostAuthenticateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

Supported auth-challenge depends on the integrated authentication server.

1. Validates transactionId/linkTransactionId.
2. Validates null / empty individualId.
3. Invokes kyc-auth call to integrated authentication server (IDA).
4. Relays error from integrated authentication server to UI on failure.

On Authentication Success: Only transaction Id is returned in the below response without any errors.

On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.
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
from fern import FernApi, AuthChallenge, AuthChallengeAuthFactorType, AuthChallengeFormat
from fern.environment import FernApiEnvironment
import datetime
from fern.ui import PostAuthenticateRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_authenticate(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostAuthenticateRequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        individual_id="464737289558",
        challenge_list=[
            AuthChallenge(
                auth_factor_type=AuthChallengeAuthFactorType.OTP,
                challenge="111111",
                format=AuthChallengeFormat.ALPHA_NUMERIC,
            )
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction ID
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthenticateRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_authenticate_v2</a>(...) -> PostAuthenticateV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

Supported auth-challenge depends on the integrated authentication server.

1. Validates transactionId/linkTransactionId.
2. Validates null / empty individualId.
3. Invokes kyc-auth call to integrated authentication server (IDA).
4. It validates stored userconsent against the requested claims and scopes
5. Relays error from integrated authentication server to UI on failure.

On Authentication Success: transaction Id and consentAction is returned in the below response without any errors.

On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.
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
from fern import FernApi, AuthChallenge, AuthChallengeAuthFactorType, AuthChallengeFormat
from fern.environment import FernApiEnvironment
import datetime
from fern.ui import PostAuthenticateV2RequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_authenticate_v2(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostAuthenticateV2RequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        individual_id="464737289558",
        challenge_list=[
            AuthChallenge(
                auth_factor_type=AuthChallengeAuthFactorType.OTP,
                challenge="111111",
                format=AuthChallengeFormat.ALPHA_NUMERIC,
            )
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction ID
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthenticateV2RequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_authenticate_v3</a>(...) -> PostAuthenticateV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

Supported auth-challenge depends on the integrated authentication server.

1. Validates transactionId/linkTransactionId.
2. Validated the provided captcha token - if the provided auth-factor is configured to be with captcha.
3. Validates null / empty individualId.
4. Invokes kyc-auth call to integrated authentication server (IDA).
5. It validates stored userconsent against the requested claims and scopes
6. Relays error from integrated authentication server to UI on failure.

On Authentication Success: transaction Id and consentAction is returned in the below response without any errors.

On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.
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
from fern import FernApi, AuthChallenge, AuthChallengeAuthFactorType, AuthChallengeFormat
from fern.environment import FernApiEnvironment
import datetime
from fern.ui import PostAuthenticateV3RequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_authenticate_v3(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostAuthenticateV3RequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        individual_id="464737289558",
        challenge_list=[
            AuthChallenge(
                auth_factor_type=AuthChallengeAuthFactorType.OTP,
                challenge="111111",
                format=AuthChallengeFormat.ALPHA_NUMERIC,
            )
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction ID
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthenticateV3RequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_auth_code</a>(...) -> PostAuthCodeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the UI application to send the accepted consent and permitted scopes.

Then UI application will receive the authorization code and few other details required for redirecting to the client / relying party application.

1. Validates transactionId. If valid, stores the accepted claims and permitted scopes in the cache and returns back the authorization code.
2. Validate accepted claims and permitted scopes in the request.
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
from fern.ui import PostAuthCodeRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_auth_code(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostAuthCodeRequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        permitted_authorize_scopes=[
            "permittedAuthorizeScopes"
        ],
        accepted_claims=[
            "name",
            "email",
            "phone_number"
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthCodeRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">get_authorization_generate_link_code</a>(...) -> GetAuthorizationGenerateLinkCodeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate link code request is raised from JS application.

1. JS application creates a deeplink with this link-code as parameter.
2. This deeplink is embedded in a Machine-readable-code and the same is rendered in the UI.
3. End user scans this machine-readable-code to open wallet app.
4. On open of wallet-app, wallet-app invokes /link-transaction endpoint.
5. In the JS application, once machine-readable-code is rendered, at the same time /link-status endpoint is invoked as a polling request.

**Configuration to decide the expire date time of linkCode**: mosip.idp.link-code-expire-in-secs
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
from fern.ui import GetAuthorizationGenerateLinkCodeRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.get_authorization_generate_link_code(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time="2023-09-22T08:01:10.000Z",
    request=GetAuthorizationGenerateLinkCodeRequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GetAuthorizationGenerateLinkCodeRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_authorization_link_status</a>(...) -> PostAuthorizationLinkStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The link transaction endpoint is invoked from Wallet-app.

1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

**Note:**
Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.
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
from fern.ui import PostAuthorizationLinkStatusRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_authorization_link_status(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time="2023-09-22T08:01:10.000Z",
    request=PostAuthorizationLinkStatusRequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        link_code="xl4cnYtLQkGRxUj",
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthorizationLinkStatusRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_authorization_link_auth</a>(...) -> PostAuthorizationLinkAuthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Link authorization code endpoint is invoked from JS application.

1. This is a Long polling request to IdP-service.
2. validates the transactionId
3. validates the linkCode if its LINKED.
4. checks the cache to see if the auth-code is generated, if yes returns the response.
5. If the auth-code is not yet generated, polling request waits for the configured time.
6. On successful response, IdP-UI should redirect to the provided redirectUri and auth-code or errors.


**Configuration to decide the wait interval**: mosip.idp.link-auth-code-deferred-response-timeout-secs
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
from fern.ui import PostAuthorizationLinkAuthRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_authorization_link_auth(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time="2023-09-22T08:01:13.000Z",
    request=PostAuthorizationLinkAuthRequestRequest(
        transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
        linked_code="xl4cnYtLQkGRxUj",
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthorizationLinkAuthRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">get_consent_details</a>(...) -> GetConsentDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Prerequisites:**
1. Request should have valid authenticated transaction id in the header `oauth-details-key`

**Validations:**
1. validate the transaction ID in the header.

Once the end user is successfully authenticated, GET consent-details endpoint is invoked to get details about the claims and consent action.


**Background:**
During kyc-auth, integrated ID system should return the list of claim details for the authenticated end user.
We have introduced new method in the `Authenticator` plugin. New kycAuth method will be invoked only when verified claims are requested by the relying party.
Claims details returned during the kcy-auth is cached in the `OIDCTransaction` to give out during fetch claim details call.
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

client.ui.get_consent_details(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction ID
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_authorization_prepare_signup_redirect</a>(...) -> PostAuthorizationPrepareSignupRedirectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Prerequisite**: 
1. User should be authenticated to invoke prepare-signup-redirect endpoint.
2. signup-service should be registered as OAUTH client with esignet. And the signup-service's OAuth client id should be configured in this property `mosip.esignet.signup-id-token-audience` and the expire time of the generated ID token depends on below property `mosip.esignet.signup-id-token-expire-seconds`.


**Validations:**
1. Validates the input transactionID.
2. Validates if the transaction requires profile update.


When this endpoint is invoked, generates the ID-token for "singup-service". and sets the cookie header is also set with cookie name as UUID same as the subject of the ID token ( eg: "d898375b-c883-4408-a9e3-f629f15c1298") and the cookie value is a encoded json: 
  `{"code" :"secret code to match with the server", "path-fragment": "path to resume after profile update"}`

ID token payload is as below
 `{ "iss": "https://esignet.dev.mosip.net", "iat": 1715047546, "exp": 1746583546, "aud": "signup-service-client-id", "sub": "d898375b-c883-4408-a9e3-f629f15c1298" }`

 **Note**: Cookie created expire time should be equal to the expire time if generated ID token.
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
from fern.ui import PostAuthorizationPrepareSignupRedirectRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_authorization_prepare_signup_redirect(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time="requestTime",
    request=PostAuthorizationPrepareSignupRedirectRequestRequest(
        transaction_id="transactionId",
        path_fragment="pathFragment",
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction ID
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` — <yyyy-MM-dd'T'HH:mm:ss.SSS'Z'>
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthorizationPrepareSignupRedirectRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_complete_signup_redirect</a>(...) -> PostCompleteSignupRedirectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint resumes the halted OIDC transactions halted and marks the completion of the identify verification process.
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
from fern.ui import PostCompleteSignupRedirectRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_complete_signup_redirect(
    oauth_details_hash="oauth-details-hash",
    oauth_details_key="oauth-details-key",
    xsrf_token="X-XSRF-TOKEN",
    request_time="2023-09-22T08:01:10.000Z",
    request=PostCompleteSignupRedirectRequestRequest(
        transaction_id="vKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
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

**oauth_details_hash:** `str` — Base64 encoded SHA-256 hash of the oauth-details endpoint response.
    
</dd>
</dl>

<dl>
<dd>

**oauth_details_key:** `str` — Transaction Id
    
</dd>
</dl>

<dl>
<dd>

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` — <yyyy-MM-dd'T'HH:mm:ss.SSS'Z'>
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostCompleteSignupRedirectRequestRequest` 
    
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

<details><summary><code>client.ui.<a href="src/fern/ui/client.py">post_par_oauth_details</a>(...) -> PostParOauthDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

PAR OAuth details request is raised from the UI JS application on page load, only when request_uri is part of the authorize URL.
OAuth details endpoint validates the provided request parameters. 

Resolved authentication factors and the consent details are sent back as response with a unique transactionId.

The transcationId in the response is used to identify/maintain the end user pre-auth session. 
This pre-auth session has timeout (configurable).

1. Validates the clientId. 
2. Validate the request_uri, if an entry is not found in the "par" cache, reject the request. 
3. Upon successful validation, move the object from "par" cache to "preauth" cache. 
4. Ignore unknown parameters in the request. 
5. In the existing oauth-details(v1,v2 & v3) endpoint, clients with **mandate_par_flow** set to true, but still using authorize without request_uri should be rejected.
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
from fern.ui import PostParOauthDetailsRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ui.post_par_oauth_details(
    xsrf_token="X-XSRF-TOKEN",
    request_time="2022-09-22T08:01:10.000Z",
    request=PostParOauthDetailsRequestRequest(
        request_uri="urn:ietf:params:oauth:request_uri:XiaVWGcLVPNxTNSAddv",
        client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
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

**xsrf_token:** `str` — CSRF token as set in cookie key 'XSRF-TOKEN'
    
</dd>
</dl>

<dl>
<dd>

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostParOauthDetailsRequestRequest` 
    
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

## WALLET
<details><summary><code>client.wallet.<a href="src/fern/wallet/client.py">post_authorization_link_transaction</a>(...) -> PostAuthorizationLinkTransactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The link transaction endpoint is invoked from Wallet-app.

1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

**Note:**
Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.
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
from fern.wallet import PostAuthorizationLinkTransactionRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet.post_authorization_link_transaction(
    request_time="2023-09-22T08:01:10.000Z",
    request=PostAuthorizationLinkTransactionRequestRequest(
        link_code="xl4cnYtLQkGRxUj",
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

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthorizationLinkTransactionRequestRequest` 
    
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

<details><summary><code>client.wallet.<a href="src/fern/wallet/client.py">post_authorization_link_transaction_v2</a>(...) -> PostAuthorizationLinkTransactionV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The link transaction endpoint is invoked from Wallet-app.

1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

**Note:**
Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.
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
from fern.wallet import PostAuthorizationLinkTransactionV2RequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet.post_authorization_link_transaction_v2(
    request_time="2023-09-22T08:01:10.000Z",
    request=PostAuthorizationLinkTransactionV2RequestRequest(
        link_code="xl4cnYtLQkGRxUj",
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

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostAuthorizationLinkTransactionV2RequestRequest` 
    
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

<details><summary><code>client.wallet.<a href="src/fern/wallet/client.py">post_linked_authenticate</a>(...) -> PostLinkedAuthenticateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

Supported auth-challenge depends on the integrated authentication server.

1. Validates linkedTransactionId.
2. Validates null / empty individualId.
4. Invokes kyc-auth call to integrated authentication server (IDA).
5. Relays error from integrated authentication server to UI on failure.

On Authentication Success: Only linkTransactionId is returned in the below response without any errors.

On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.
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
from fern import FernApi, AuthChallenge, AuthChallengeAuthFactorType, AuthChallengeFormat
from fern.environment import FernApiEnvironment
import datetime
from fern.wallet import PostLinkedAuthenticateRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet.post_linked_authenticate(
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostLinkedAuthenticateRequestRequest(
        linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
        individual_id="34543276756",
        challenge_list=[
            AuthChallenge(
                auth_factor_type=AuthChallengeAuthFactorType.OTP,
                challenge="111111",
                format=AuthChallengeFormat.ALPHA_NUMERIC,
            )
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

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostLinkedAuthenticateRequestRequest` 
    
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

<details><summary><code>client.wallet.<a href="src/fern/wallet/client.py">post_linked_authenticate_v2</a>(...) -> PostLinkedAuthenticateV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

Supported auth-challenge depends on the integrated authentication server.

1. Validates linkedTransactionId.
2. Validates null / empty individualId.
4. Invokes kyc-auth call to integrated authentication server (IDA).
5. Relays error from integrated authentication server to UI on failure.
6. It validates stored userconsent against the requested claims and scopes

On Authentication Success: linkTransactionId and consentAction is returned in the below response without any errors.

On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.
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
from fern import FernApi, AuthChallenge, AuthChallengeAuthFactorType, AuthChallengeFormat
from fern.environment import FernApiEnvironment
import datetime
from fern.wallet import PostLinkedAuthenticateV2RequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet.post_linked_authenticate_v2(
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostLinkedAuthenticateV2RequestRequest(
        linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
        individual_id="34543276756",
        challenge_list=[
            AuthChallenge(
                auth_factor_type=AuthChallengeAuthFactorType.OTP,
                challenge="111111",
                format=AuthChallengeFormat.ALPHA_NUMERIC,
            )
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

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostLinkedAuthenticateV2RequestRequest` 
    
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

<details><summary><code>client.wallet.<a href="src/fern/wallet/client.py">post_linked_consent</a>(...) -> PostLinkedConsentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

1. Validates linkedTransactionId.
2. Validate accepted claims and permitted scopes in the request.
3. If valid, stores the accepted claims and permitted scopes in the cache.
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
from fern.wallet import PostLinkedConsentRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet.post_linked_consent(
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:10+00:00"),
    request=PostLinkedConsentRequestRequest(
        linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
        permitted_authorize_scopes=[
            "permittedAuthorizeScopes"
        ],
        accepted_claims=[
            "name",
            "email",
            "phone_number",
            "address"
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

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostLinkedConsentRequestRequest` 
    
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

<details><summary><code>client.wallet.<a href="src/fern/wallet/client.py">post_linked_consent_v2</a>(...) -> PostLinkedConsentV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

1. Validates linkedTransactionId.
2. Validate accepted claims and permitted scopes in the request and the signature.
3. If valid, stores the accepted claims, permitted scopes and signature in the consent registry.
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
from fern.wallet import PostLinkedConsentV2RequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet.post_linked_consent_v2(
    request_time=datetime.datetime.fromisoformat("2023-09-22T08:01:13+00:00"),
    request=PostLinkedConsentV2RequestRequest(
        linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
        permitted_authorize_scopes=[
            "permittedAuthorizeScopes"
        ],
        accepted_claims=[
            "name",
            "email",
            "phone_number",
            "address"
        ],
        signature="<detached signature>",
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

**request_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostLinkedConsentV2RequestRequest` 
    
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

## WALLET BACKEND
<details><summary><code>client.wallet_backend.<a href="src/fern/wallet_backend/client.py">post_binding_otp</a>(...) -> PostBindingOtpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send wallet binding OTP endpoint is invoked by Mimoto server.
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
from fern.wallet_backend import PostBindingOtpRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet_backend.post_binding_otp(
    request_time="2023-09-22T08:01:13.000Z",
    request=PostBindingOtpRequestRequest(
        individual_id="24554655645",
        otp_channels=[
            "sms",
            "email"
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

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostBindingOtpRequestRequest` 
    
</dd>
</dl>

<dl>
<dd>

**partner_api_key:** `typing.Optional[str]` — API key of the binding partner, this will be passed to binder implementation to interact with authentication system.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.
    
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

<details><summary><code>client.wallet_backend.<a href="src/fern/wallet_backend/client.py">post_binding_otp_v2</a>(...) -> PostBindingOtpV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send wallet binding OTP endpoint is invoked by Mimoto server.
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
from fern.wallet_backend import PostBindingOtpV2RequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet_backend.post_binding_otp_v2(
    request_time="2023-09-22T08:01:13.000Z",
    request=PostBindingOtpV2RequestRequest(
        individual_id="24554655645",
        otp_channels=[
            "sms",
            "email"
        ],
        captcha_token="ALSKDJFURIEOQPZMKFURHFVBH",
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

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostBindingOtpV2RequestRequest` 
    
</dd>
</dl>

<dl>
<dd>

**partner_api_key:** `typing.Optional[str]` — API key of the binding partner, this will be passed to binder implementation to interact with authentication system.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.
    
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

<details><summary><code>client.wallet_backend.<a href="src/fern/wallet_backend/client.py">post_wallet_binding</a>(...) -> PostWalletBindingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Wallet binding endpoint is invoked by Mimoto server.

1. This request is invoked from wallet-app with authChallenge.
2. Integrated keybinder implementation validates the authChallenge.
3. Public key registry is updated with the key binding details for the provided individualId.
4. Binded walletUserId (WUID) is returned with keybinder signed certificate. 

**Note**: Binding entry uniqueness is combination of these 3 values -> (PSUT, public-key, auth-factor-type)
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
from fern import FernApi, AuthChallenge, AuthChallengeAuthFactorType, AuthChallengeFormat
from fern.environment import FernApiEnvironment
from fern.wallet_backend import PostWalletBindingRequestRequest

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wallet_backend.post_wallet_binding(
    request_time="2023-09-22T08:01:15.000Z",
    request=PostWalletBindingRequestRequest(
        individual_id="24554655645",
        auth_factor_type="WLA",
        format="jwt",
        challenge_list=[
            AuthChallenge(
                auth_factor_type=AuthChallengeAuthFactorType.OTP,
                challenge="111111",
                format=AuthChallengeFormat.ALPHA_NUMERIC,
            )
        ],
        public_key={
            "kty": "RSA",
            "e": "AQAB",
            "use": "sig",
            "alg": "RS256",
            "n": "sfIT-5o9ZSr8lJuBsRTzodJYvEgNeIayJRd9WLip6tU9NZ_5VvVS_jq5STza9WELs127xH7e6rgGJ31B6VLBbrRRgLm2sz2_0s1p9ilRSrae0P3cJHK7aIgY0c-E1SwbzrKmV4FQKzARfHG-M-DmAD8V38LclxZycAu7gXWFVS7RPW_NpmjtVGDpnx0pKYgfJb8QgzGEbSKUGB39GRWNA2ij-6tEPQQwYSO5akyFup-bVaJrKKaIWn37iiB9T7umXnmzp-3HuP1SQp6cPQLkeWp64lozxTq4To12gbietIKyfJto7r9sra1wRyq0XNKhQvswLmuQcORJKhEMJWVCpQ"
        },
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

**request_time:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostWalletBindingRequestRequest` 
    
</dd>
</dl>

<dl>
<dd>

**partner_api_key:** `typing.Optional[str]` — API key of the Binding partner, this will be passed to binder implementation to interact with authentication system.
    
</dd>
</dl>

<dl>
<dd>

**partner_id:** `typing.Optional[str]` — Binding partner identifier, this will be passed to binder implementation to interact with authentication system.
    
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

