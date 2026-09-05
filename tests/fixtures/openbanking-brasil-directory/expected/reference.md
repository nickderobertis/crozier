# Reference
## Organisations
<details><summary><code>client.organisations.<a href="src/fern/organisations/client.py">get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services</a>(...) -> OrganisationsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisations.get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
</dd>
</dl>

<dl>
<dd>

**display_mine:** `typing.Optional[str]` — Set to an email value to instruct the backend to only return organisations related to the user
    
</dd>
</dl>

<dl>
<dd>

**filter_by:** `typing.Optional[str]` — Will return organisations with data like the provided value
    
</dd>
</dl>

<dl>
<dd>

**hide_inactive:** `typing.Optional[bool]` — Will return only active organisations
    
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

<details><summary><code>client.organisations.<a href="src/fern/organisations/client.py">get_the_given_organisations_details</a>(...) -> OrganisationWithTnc</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisations.get_the_given_organisations_details(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
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

<details><summary><code>client.organisations.<a href="src/fern/organisations/client.py">get_all_tn_c_data_of_the_given_organisation</a>(...) -> OrgTermsAndConditionsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisations.get_all_tn_c_data_of_the_given_organisation(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

## AuthorisationServers
<details><summary><code>client.authorisation_servers.<a href="src/fern/authorisation_servers/client.py">get_all_authorisation_servers_for_the_given_organisation</a>(...) -> AuthorisationServers</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_servers.get_all_authorisation_servers_for_the_given_organisation(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.authorisation_servers.<a href="src/fern/authorisation_servers/client.py">get_an_authorisation_server_by_id</a>(...) -> AuthorisationServer</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_servers.get_an_authorisation_server_by_id(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
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

## AuthorisationServersApiResources
<details><summary><code>client.authorisation_servers_api_resources.<a href="src/fern/authorisation_servers_api_resources/client.py">get_all_api_resources_for_the_given_authorisation_server</a>(...) -> ApiResources</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_servers_api_resources.get_all_api_resources_for_the_given_authorisation_server(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.authorisation_servers_api_resources.<a href="src/fern/authorisation_servers_api_resources/client.py">get_an_authorisation_server_api_resource_by_id</a>(...) -> ApiResource</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_servers_api_resources.get_an_authorisation_server_api_resource_by_id(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
    api_resource_id="ApiResourceId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
</dd>
</dl>

<dl>
<dd>

**api_resource_id:** `ApiResourceId` — The api version Id
    
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

<details><summary><code>client.authorisation_servers_api_resources.<a href="src/fern/authorisation_servers_api_resources/client.py">get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status</a>(...) -> ApiResources</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_servers_api_resources.get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
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

## AuthorisationServersApiDiscoveryEndpoints
<details><summary><code>client.authorisation_servers_api_discovery_endpoints.<a href="src/fern/authorisation_servers_api_discovery_endpoints/client.py">get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version</a>(...) -> ApiDiscoveryEndpoints</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_servers_api_discovery_endpoints.get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
    api_resource_id="ApiResourceId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
</dd>
</dl>

<dl>
<dd>

**api_resource_id:** `ApiResourceId` — The api version Id
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.authorisation_servers_api_discovery_endpoints.<a href="src/fern/authorisation_servers_api_discovery_endpoints/client.py">get_an_authorisation_server_api_discovery_endpoint_by_id</a>(...) -> ApiDiscoveryEndpoint</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_servers_api_discovery_endpoints.get_an_authorisation_server_api_discovery_endpoint_by_id(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
    api_resource_id="ApiResourceId",
    api_discovery_endpoint_id="ApiDiscoveryEndpointId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
</dd>
</dl>

<dl>
<dd>

**api_resource_id:** `ApiResourceId` — The api version Id
    
</dd>
</dl>

<dl>
<dd>

**api_discovery_endpoint_id:** `ApiEndpointId` — The api discovery endpoint Id
    
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

## AuthorisationServerCertifications
<details><summary><code>client.authorisation_server_certifications.<a href="src/fern/authorisation_server_certifications/client.py">get_all_certifications_for_given_authorisation_server</a>(...) -> AuthorisationServerCertifications</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_server_certifications.get_all_certifications_for_given_authorisation_server(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
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

<details><summary><code>client.authorisation_server_certifications.<a href="src/fern/authorisation_server_certifications/client.py">get_a_certification_by_id</a>(...) -> AuthorisationServerCertification</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorisation_server_certifications.get_a_certification_by_id(
    organisation_id="OrganisationId",
    authorisation_server_id="AuthorisationServerId",
    authorisation_server_certification_id="AuthorisationServerCertificationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_id:** `AuthorisationServerId` — The authorisation server Id
    
</dd>
</dl>

<dl>
<dd>

**authorisation_server_certification_id:** `AuthorisationServerCertificationId` — Auth server certification Id
    
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

## OrganisationAuthorityClaims
<details><summary><code>client.organisation_authority_claims.<a href="src/fern/organisation_authority_claims/client.py">get_the_authority_claims_for_the_given_organisation</a>(...) -> OrganisationAuthorityClaims</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_authority_claims.get_the_authority_claims_for_the_given_organisation(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
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

<details><summary><code>client.organisation_authority_claims.<a href="src/fern/organisation_authority_claims/client.py">get_an_authority_claim_by_id</a>(...) -> OrganisationAuthorityClaim</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_authority_claims.get_an_authority_claim_by_id(
    organisation_id="OrganisationId",
    organisation_authority_claim_id="OrganisationAuthorityClaimId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**organisation_authority_claim_id:** `OrganisationAuthorityClaimId` — The Authority claims ID for an organisation
    
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

## OrganisationAuthorityClaimsAuthorisations
<details><summary><code>client.organisation_authority_claims_authorisations.<a href="src/fern/organisation_authority_claims_authorisations/client.py">get_an_authority_claims_authorisations</a>(...) -> OrganisationAuthorityClaimAuthorisations</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_authority_claims_authorisations.get_an_authority_claims_authorisations(
    organisation_id="OrganisationId",
    organisation_authority_claim_id="OrganisationAuthorityClaimId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**organisation_authority_claim_id:** `OrganisationAuthorityClaimId` — The Authority claims ID for an organisation
    
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

<details><summary><code>client.organisation_authority_claims_authorisations.<a href="src/fern/organisation_authority_claims_authorisations/client.py">get_a_claim_authorisation</a>(...) -> OrganisationAuthorityClaimAuthorisation</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_authority_claims_authorisations.get_a_claim_authorisation(
    organisation_id="OrganisationId",
    organisation_authority_claim_id="OrganisationAuthorityClaimId",
    organisation_authorisation_id="OrganisationAuthorisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**organisation_authority_claim_id:** `OrganisationAuthorityClaimId` — The Authority claims ID for an organisation
    
</dd>
</dl>

<dl>
<dd>

**organisation_authorisation_id:** `OrganisationAuthorisationId` — The authorisation ID for an organisation's authority claims
    
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

## OrganisationAuthorityDomainClaims
<details><summary><code>client.organisation_authority_domain_claims.<a href="src/fern/organisation_authority_domain_claims/client.py">get_the_authority_domain_claims_for_the_given_organisation</a>(...) -> OrganisationAuthorityDomainClaimsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_authority_domain_claims.get_the_authority_domain_claims_for_the_given_organisation(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.organisation_authority_domain_claims.<a href="src/fern/organisation_authority_domain_claims/client.py">get_an_authority_domain_claim_by_id</a>(...) -> OrganisationAuthorityDomainClaim</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_authority_domain_claims.get_an_authority_domain_claim_by_id(
    organisation_id="OrganisationId",
    organisation_authority_domain_claim_id="OrganisationAuthorityDomainClaimId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**organisation_authority_domain_claim_id:** `OrganisationAuthorityDomainClaimId` — Organisation Authority Domain Claim Id
    
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

## OrganisationCertificates
<details><summary><code>client.organisation_certificates.<a href="src/fern/organisation_certificates/client.py">get_the_certificates_for_the_given_organisation</a>(...) -> CertificatesOrKeys</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_certificates.get_the_certificates_for_the_given_organisation(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
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

<details><summary><code>client.organisation_certificates.<a href="src/fern/organisation_certificates/client.py">retrieve_a_certificate_with_the_given_certificate_or_key_id</a>(...) -> CertificateOrKey</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_certificates.retrieve_a_certificate_with_the_given_certificate_or_key_id(
    organisation_id="OrganisationId",
    certificate_or_key_id="CertificateOrKeyId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**certificate_or_key_id:** `CertificateOrKeyId` — The certificate or key Id
    
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

<details><summary><code>client.organisation_certificates.<a href="src/fern/organisation_certificates/client.py">get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation</a>(...) -> CertificatesOrKeys</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OrganisationCertificateType
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_certificates.get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation(
    organisation_id="OrganisationId",
    organisation_certificate_type=OrganisationCertificateType.QWAC,
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**organisation_certificate_type:** `OrganisationCertificateType` — The certificate type
    
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
<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">get_the_contacts_for_the_given_organisation</a>(...) -> ContactsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.get_the_contacts_for_the_given_organisation(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">get_a_contact_by_id</a>(...) -> Contact</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.get_a_contact_by_id(
    organisation_id="OrganisationId",
    contact_id="ContactId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `ContactId` — The contact id
    
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

## SoftwareStatementsForAnOrganisation
<details><summary><code>client.software_statements_for_an_organisation.<a href="src/fern/software_statements_for_an_organisation/client.py">get_all_software_statements_for_the_given_organisation</a>(...) -> SoftwareStatements</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statements_for_an_organisation.get_all_software_statements_for_the_given_organisation(
    organisation_id="OrganisationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
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

<details><summary><code>client.software_statements_for_an_organisation.<a href="src/fern/software_statements_for_an_organisation/client.py">get_a_software_statement</a>(...) -> SoftwareStatement</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statements_for_an_organisation.get_a_software_statement(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
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

<details><summary><code>client.software_statements_for_an_organisation.<a href="src/fern/software_statements_for_an_organisation/client.py">update_a_software_statement_by_id</a>(...) -> SoftwareStatement</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statements_for_an_organisation.update_a_software_statement_by_id(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
    client_name="ClientName",
    client_uri="ClientUri",
    logo_uri="LogoUri",
    redirect_uri=[
        "RedirectUri"
    ],
    version=1.1,
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
</dd>
</dl>

<dl>
<dd>

**client_name:** `str` — Software Statement client name
    
</dd>
</dl>

<dl>
<dd>

**client_uri:** `str` — The Software Statement compliant client URI
    
</dd>
</dl>

<dl>
<dd>

**logo_uri:** `str` — The Software Statement compliant logo URI
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.List[str]` — The Software Statement redirect URIs
    
</dd>
</dl>

<dl>
<dd>

**version:** `float` — Software Statement version as provided by the organisation's PTC
    
</dd>
</dl>

<dl>
<dd>

**additional_software_metadata:** `typing.Optional[str]` — Extra metadata defined by the org admins to be loaded into the software statement and made avaiable during introspection
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Software Statement description
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` — The additional check for software statement, this field can avoid environment checks.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[SoftwareStatementRequestMode]` — The additional check to see if the environment reflected above is live or test.
    
</dd>
</dl>

<dl>
<dd>

**notification_webhook:** `typing.Optional[SnsNotificationWebhookUri]` 
    
</dd>
</dl>

<dl>
<dd>

**notification_webhook_status:** `typing.Optional[NotificationWebhookStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**on_behalf_of:** `typing.Optional[str]` — A reference to fourth party organisation resource on the RTS Directory if the registering Org is acting on behalf of another
    
</dd>
</dl>

<dl>
<dd>

**policy_uri:** `typing.Optional[str]` — The Software Statement compliant policy URI
    
</dd>
</dl>

<dl>
<dd>

**terms_of_service_uri:** `typing.Optional[str]` — The Software Statement terms of service compliant URI
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SoftwareStatementUpdateRequestStatus]` — Should this software statement be active or suspended?
    
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

<details><summary><code>client.software_statements_for_an_organisation.<a href="src/fern/software_statements_for_an_organisation/client.py">unlock_a_software_statement</a>(...) -> SoftwareStatement</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statements_for_an_organisation.unlock_a_software_statement(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
</dd>
</dl>

<dl>
<dd>

**unlock:** `typing.Optional[bool]` — Unlock Software Statement
    
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

## SoftwareStatementAssertions
<details><summary><code>client.software_statement_assertions.<a href="src/fern/software_statement_assertions/client.py">get_a_software_statement_assertion_for_the_given_software_statement_id</a>(...) -> SoftwareStatementAssertion</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_assertions.get_a_software_statement_assertion_for_the_given_software_statement_id(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
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

## SoftwareStatementAuthorityClaims
<details><summary><code>client.software_statement_authority_claims.<a href="src/fern/software_statement_authority_claims/client.py">get_the_authority_claims_for_the_given_software_statement</a>(...) -> SoftwareAuthorityClaims</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_authority_claims.get_the_authority_claims_for_the_given_software_statement(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
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

<details><summary><code>client.software_statement_authority_claims.<a href="src/fern/software_statement_authority_claims/client.py">get_an_authority_claim_by_id</a>(...) -> SoftwareAuthorityClaim</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_authority_claims.get_an_authority_claim_by_id(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
    software_authority_claim_id="SoftwareAuthorityClaimId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
</dd>
</dl>

<dl>
<dd>

**software_authority_claim_id:** `SoftwareAuthorityClaimId` — The software statement's authority claim ID
    
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

## SoftwareStatementCertificates
<details><summary><code>client.software_statement_certificates.<a href="src/fern/software_statement_certificates/client.py">get_certificates_for_the_given_software_statement</a>(...) -> CertificatesOrKeys</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_certificates.get_certificates_for_the_given_software_statement(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
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

<details><summary><code>client.software_statement_certificates.<a href="src/fern/software_statement_certificates/client.py">get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement</a>(...) -> CertificateOrKey</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SoftwareStatementCertificateOrKeyType
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_certificates.get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
    software_statement_certificate_or_key_type=SoftwareStatementCertificateOrKeyType.RTSTRANSPORT,
    certificate_or_key_id="CertificateOrKeyId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_certificate_or_key_type:** `SoftwareStatementCertificateOrKeyType` — The certificate or key type that can be associated with a software statement
    
</dd>
</dl>

<dl>
<dd>

**certificate_or_key_id:** `CertificateOrKeyId` — The certificate or key Id
    
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

<details><summary><code>client.software_statement_certificates.<a href="src/fern/software_statement_certificates/client.py">update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SoftwareStatementCertificateOrKeyType
from fern.environment import FernApiEnvironment
from fern.software_statement_certificates import AmendCertificateRequestRevokeReason

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_certificates.update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
    software_statement_certificate_or_key_type=SoftwareStatementCertificateOrKeyType.RTSTRANSPORT,
    certificate_or_key_id="CertificateOrKeyId",
    revoke_reason=AmendCertificateRequestRevokeReason.UNSPECIFIED,
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_certificate_or_key_type:** `SoftwareStatementCertificateOrKeyType` — The certificate or key type that can be associated with a software statement
    
</dd>
</dl>

<dl>
<dd>

**certificate_or_key_id:** `CertificateOrKeyId` — The certificate or key Id
    
</dd>
</dl>

<dl>
<dd>

**revoke_reason:** `AmendCertificateRequestRevokeReason` — Specify a reason for revokation of the certificate.
    
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

## SoftwareStatementCertifications
<details><summary><code>client.software_statement_certifications.<a href="src/fern/software_statement_certifications/client.py">get_all_certifications_for_given_software_statement</a>(...) -> SoftwareStatementCertifications</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_certifications.get_all_certifications_for_given_software_statement(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
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

<details><summary><code>client.software_statement_certifications.<a href="src/fern/software_statement_certifications/client.py">get_a_certification_by_id</a>(...) -> SoftwareStatementCertification</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_certifications.get_a_certification_by_id(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
    software_statement_certification_id="SoftwareStatementCertificationId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_certification_id:** `SoftwareStatementCertificationId` — Software Statement certification Id
    
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

## SoftwareStatementMetadata
<details><summary><code>client.software_statement_metadata.<a href="src/fern/software_statement_metadata/client.py">get_all_metadata_associated_with_a_software_statement</a>(...) -> MetadataListResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.software_statement_metadata.get_all_metadata_associated_with_a_software_statement(
    organisation_id="OrganisationId",
    software_statement_id="SoftwareStatementId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**software_statement_id:** `SoftwareStatementId` — The software statement ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Get all metadata of a specific type
    
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

## OrganisationDomainUsers
<details><summary><code>client.organisation_domain_users.<a href="src/fern/organisation_domain_users/client.py">all_users_for_the_given_authorisation_domain</a>(...) -> AuthorisationDomainUsersPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_domain_users.all_users_for_the_given_authorisation_domain(
    organisation_id="OrganisationId",
    authorisation_domain_name="AuthorisationDomainName",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_domain_name:** `AuthorisationDomainName` — Authorisation Domain Name. Eg:PSD2
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.organisation_domain_users.<a href="src/fern/organisation_domain_users/client.py">authorisation_domain_user_details</a>(...) -> AuthorisationDomainUsersPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organisation_domain_users.authorisation_domain_user_details(
    organisation_id="OrganisationId",
    authorisation_domain_name="AuthorisationDomainName",
    user_email_id="UserEmailId",
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

**organisation_id:** `OrganisationId` — The organisation ID
    
</dd>
</dl>

<dl>
<dd>

**authorisation_domain_name:** `AuthorisationDomainName` — Authorisation Domain Name. Eg:PSD2
    
</dd>
</dl>

<dl>
<dd>

**user_email_id:** `UserEmailId` — Email address of the super user
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

## ReferencesAuthorisationDomainRole
<details><summary><code>client.references_authorisation_domain_role.<a href="src/fern/references_authorisation_domain_role/client.py">reference_data_of_all_authorisation_domain_roles</a>(...) -> AuthorisationDomainRolesPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authorisation_domain_role.reference_data_of_all_authorisation_domain_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.references_authorisation_domain_role.<a href="src/fern/references_authorisation_domain_role/client.py">get_an_authorisation_domain_role_by_name</a>(...) -> AuthorisationDomainRole</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authorisation_domain_role.get_an_authorisation_domain_role_by_name(
    authorisation_domain_role_name="PAGTO",
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

**authorisation_domain_role_name:** `AuthorisationDomainRoleName` — Authorisation Domain Role Name. Eg:TPP
    
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

## ReferencesAuthorisationDomainRoleMetadata
<details><summary><code>client.references_authorisation_domain_role_metadata.<a href="src/fern/references_authorisation_domain_role_metadata/client.py">get_metadata_associated_with_an_authorisation_domain_role</a>(...) -> MetadataResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authorisation_domain_role_metadata.get_metadata_associated_with_an_authorisation_domain_role(
    authorisation_domain_role_name="PAGTO",
    metadata_id="MetadataId",
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

**authorisation_domain_role_name:** `AuthorisationDomainRoleName` — Authorisation Domain Role Name. Eg:TPP
    
</dd>
</dl>

<dl>
<dd>

**metadata_id:** `MetadataId` — The metadata id object
    
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

## ReferencesAuthorisationDomain
<details><summary><code>client.references_authorisation_domain.<a href="src/fern/references_authorisation_domain/client.py">reference_data_of_all_authorisation_domains</a>(...) -> AuthorisationDomainsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authorisation_domain.reference_data_of_all_authorisation_domains()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.references_authorisation_domain.<a href="src/fern/references_authorisation_domain/client.py">get_an_authorisation_domain_by_name</a>(...) -> AuthorisationDomain</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authorisation_domain.get_an_authorisation_domain_by_name(
    authorisation_domain_name="AuthorisationDomainName",
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

**authorisation_domain_name:** `AuthorisationDomainName` — Authorisation Domain Name. Eg:PSD2
    
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

## ReferencesAuthority
<details><summary><code>client.references_authority.<a href="src/fern/references_authority/client.py">reference_data_of_all_authorities</a>(...) -> Authorities</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authority.reference_data_of_all_authorities()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.references_authority.<a href="src/fern/references_authority/client.py">get_a_reference_authority_by_id</a>(...) -> Authority</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authority.get_a_reference_authority_by_id(
    authority_id="AuthorityId",
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

**authority_id:** `AuthorityId` — The reference authority Id
    
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

## ReferencesAuthorityAuthorisationDomain
<details><summary><code>client.references_authority_authorisation_domain.<a href="src/fern/references_authority_authorisation_domain/client.py">reference_data_of_all_authorisation_domains_for_an_authority_id</a>(...) -> AuthorityAuthorisationDomainsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authority_authorisation_domain.reference_data_of_all_authorisation_domains_for_an_authority_id(
    authority_id="AuthorityId",
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

**authority_id:** `AuthorityId` — The reference authority Id
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

<details><summary><code>client.references_authority_authorisation_domain.<a href="src/fern/references_authority_authorisation_domain/client.py">get_an_authority_authorisation_domain_by_id</a>(...) -> AuthorityAuthorisationDomain</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authority_authorisation_domain.get_an_authority_authorisation_domain_by_id(
    authority_id="AuthorityId",
    authority_authorisation_domain_id="AuthorityAuthorisationDomainId",
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

**authority_id:** `AuthorityId` — The reference authority Id
    
</dd>
</dl>

<dl>
<dd>

**authority_authorisation_domain_id:** `AuthorityAuthorisationDomainId` — ID of the Authority mapped with Authorisation Domain
    
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

<details><summary><code>client.references_authority_authorisation_domain.<a href="src/fern/references_authority_authorisation_domain/client.py">mappings_of_authorities_with_authorisation_domains</a>(...) -> AuthorityAuthorisationDomainsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_authority_authorisation_domain.mappings_of_authorities_with_authorisation_domains()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

## ReferencesTermsAndConditions
<details><summary><code>client.references_terms_and_conditions.<a href="src/fern/references_terms_and_conditions/client.py">all_terms_and_conditions</a>(...) -> TermsAndConditionsPage</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.references_terms_and_conditions.all_terms_and_conditions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number to return of the result set
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the pages to return
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field name to sort
    
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

