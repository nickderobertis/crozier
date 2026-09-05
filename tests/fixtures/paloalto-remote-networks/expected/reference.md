# Reference
## BandwidthAllocations
<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">get_v1bandwidth_allocations</a>(...) -> BandwidthAllocationSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of aggregated bandwidth regions and allocations, which includes a list of regions and allocations.
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

client.bandwidth_allocations.get_v1bandwidth_allocations(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">post_v1bandwidth_allocations</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allocate aggregated bandwidth for the regions based on location data.
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

client.bandwidth_allocations.post_v1bandwidth_allocations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BandwidthAllocationSet` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">put_v1bandwidth_allocations</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify an aggregated bandwidth regions.
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

client.bandwidth_allocations.put_v1bandwidth_allocations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BandwidthAllocationSet` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">delete_v1bandwidth_allocations</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows you to delete an aggregated bandwidth region.
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

client.bandwidth_allocations.delete_v1bandwidth_allocations(
    region="region",
    spn_name="SpnName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**region:** `str` — The aggregate bandwidth region.
    
</dd>
</dl>

<dl>
<dd>

**spn_name:** `str` — The IPSec termination node. 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">get_v1bandwidth_allocations_read</a>(...) -> BandwidthAllocationSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the bandwidth allocation configurations for a specified set of regions.
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

client.bandwidth_allocations.get_v1bandwidth_allocations_read(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">post_v1bandwidth_allocations_read</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request to read bandwidth allocation configuration.
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

client.bandwidth_allocations.post_v1bandwidth_allocations_read()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**bandwidth_allocation_region_names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">get_v2bandwidth_allocations</a>(...) -> BandwidthAllocationSetV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an aggregated bandwidth regions based on the location data.
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

client.bandwidth_allocations.get_v2bandwidth_allocations(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">post_v2bandwidth_allocations</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Status for the given request ID.
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

client.bandwidth_allocations.post_v2bandwidth_allocations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BandwidthAllocationSetV2` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">put_v2bandwidth_allocations</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify aggregated bandwidth regions.
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

client.bandwidth_allocations.put_v2bandwidth_allocations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BandwidthAllocationSetV2` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bandwidth_allocations.<a href="src/fern/bandwidth_allocations/client.py">delete_v2bandwidth_allocations</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an aggregated bandwidth region.
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

client.bandwidth_allocations.delete_v2bandwidth_allocations(
    region="region",
    spn_name="SpnName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**region:** `str` — The aggregate bandwidth region.
    
</dd>
</dl>

<dl>
<dd>

**spn_name:** `str` — The IPSec termination node. 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IkeCryptoProfiles
<details><summary><code>client.ike_crypto_profiles.<a href="src/fern/ike_crypto_profiles/client.py">get_v1ike_crypto_profiles</a>(...) -> IkeCryptoProfilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides a status of Internet Key Exchange(IKE) Crypto Profiles created along with the UUID. 
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

client.ike_crypto_profiles.get_v1ike_crypto_profiles(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ike_crypto_profiles.<a href="src/fern/ike_crypto_profiles/client.py">post_v1ike_crypto_profiles</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an IKE Crypto Profiles. 
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
from fern import FernApi, IkeCryptoProfilesDhGroupItem, IkeCryptoProfilesEncryptionItem, IkeCryptoProfilesHashItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ike_crypto_profiles.post_v1ike_crypto_profiles(
    dh_group=[
        IkeCryptoProfilesDhGroupItem.GROUP1
    ],
    encryption=[
        IkeCryptoProfilesEncryptionItem.DES
    ],
    hash=[
        IkeCryptoProfilesHashItem.MD5
    ],
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

**request:** `IkeCryptoProfiles` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ike_crypto_profiles.<a href="src/fern/ike_crypto_profiles/client.py">put_v1ike_crypto_profiles</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit an IKE Crypto Profiles. 
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
from fern import FernApi, IkeCryptoProfilesDhGroupItem, IkeCryptoProfilesEncryptionItem, IkeCryptoProfilesHashItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ike_crypto_profiles.put_v1ike_crypto_profiles(
    dh_group=[
        IkeCryptoProfilesDhGroupItem.GROUP1
    ],
    encryption=[
        IkeCryptoProfilesEncryptionItem.DES
    ],
    hash=[
        IkeCryptoProfilesHashItem.MD5
    ],
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

**request:** `IkeCryptoProfiles` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ike_crypto_profiles.<a href="src/fern/ike_crypto_profiles/client.py">delete_v1ike_crypto_profiles</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an IKE Crypto Profiles. 
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

client.ike_crypto_profiles.delete_v1ike_crypto_profiles(
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

**name:** `str` — IKE Crypto Profile name.
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ike_crypto_profiles.<a href="src/fern/ike_crypto_profiles/client.py">get_v1ike_crypto_profiles_read</a>(...) -> GetV1IkeCryptoProfilesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the list of IKE Crypto Profiles.
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

client.ike_crypto_profiles.get_v1ike_crypto_profiles_read(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ike_crypto_profiles.<a href="src/fern/ike_crypto_profiles/client.py">post_v1ike_crypto_profiles_read</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request to read the list of IKE Crypto Profiles.
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

client.ike_crypto_profiles.post_v1ike_crypto_profiles_read()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**ike_crypto_profiles_names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IkeGateway
<details><summary><code>client.ike_gateway.<a href="src/fern/ike_gateway/client.py">get_v1ike_gateways_read</a>(...) -> GetV1IkeGatewaysReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of IKE gateway configurations for the specified UUID.
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

client.ike_gateway.get_v1ike_gateways_read(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ike_gateway.<a href="src/fern/ike_gateway/client.py">post_v1ike_gateways_read</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request to read the remote network IKE gateways for the specified IKE gateway names.
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

client.ike_gateway.post_v1ike_gateways_read()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**ike_gateways_names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IpSecCryptoProfiles
<details><summary><code>client.ip_sec_crypto_profiles.<a href="src/fern/ip_sec_crypto_profiles/client.py">get_v1ipsec_crypto_profiles</a>(...) -> IpsecCryptoProfilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the status of IPSec Crypto Profiles. Shows results of create, modify, and delete actions with their associated UUIDs.
Users can perform these actions and then use this GET request to verify the status by referencing the UUID received during the initial action.
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

client.ip_sec_crypto_profiles.get_v1ipsec_crypto_profiles(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_sec_crypto_profiles.<a href="src/fern/ip_sec_crypto_profiles/client.py">post_v1ipsec_crypto_profiles</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an IPSec crypto profile.
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
from fern import FernApi, LifetimeSeconds
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ip_sec_crypto_profiles.post_v1ipsec_crypto_profiles(
    lifetime=LifetimeSeconds(),
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

**request:** `IpsecCryptoProfiles` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_sec_crypto_profiles.<a href="src/fern/ip_sec_crypto_profiles/client.py">put_v1ipsec_crypto_profiles</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit an IPSec crypto profile.
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
from fern import FernApi, LifetimeSeconds
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ip_sec_crypto_profiles.put_v1ipsec_crypto_profiles(
    lifetime=LifetimeSeconds(),
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

**request:** `IpsecCryptoProfiles` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_sec_crypto_profiles.<a href="src/fern/ip_sec_crypto_profiles/client.py">delete_v1ipsec_crypto_profiles</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an IPSec crypto profile.
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

client.ip_sec_crypto_profiles.delete_v1ipsec_crypto_profiles(
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

**name:** `str` — IPSEC Crypto Profile name.
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_sec_crypto_profiles.<a href="src/fern/ip_sec_crypto_profiles/client.py">get_v1ipsec_crypto_profiles_read</a>(...) -> GetV1IpsecCryptoProfilesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can read a list of Internet Protocol Security (IPSec) crypto profiles configurations that are created. 
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

client.ip_sec_crypto_profiles.get_v1ipsec_crypto_profiles_read(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_sec_crypto_profiles.<a href="src/fern/ip_sec_crypto_profiles/client.py">post_v1ipsec_crypto_profiles_read</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request to read a list IPSec Crypto Profile.
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

client.ip_sec_crypto_profiles.post_v1ipsec_crypto_profiles_read()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**ipsec_crypto_profiles_names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Location Information
<details><summary><code>client.location_information.<a href="src/fern/location_information/client.py">get_v1location_informations</a>(...) -> LocationInformationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the location information status of the given request ID.
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

client.location_information.get_v1location_informations(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.location_information.<a href="src/fern/location_information/client.py">post_v1location_informations</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve location-mapped information or configuration through a POST request and returns the request ID.
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

client.location_information.post_v1location_informations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**info_type:** `typing.Optional[str]` — Information type. For example, region information.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — optional user description
    
</dd>
</dl>

<dl>
<dd>

**locations:** `typing.Optional[typing.List[Location]]` — locations
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RemoteNetworks
<details><summary><code>client.remote_networks.<a href="src/fern/remote_networks/client.py">get_v1remote_networks</a>(...) -> RemoteNetworksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get remote networks IPSec tunnel details for create, modify, or delete by ID.
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

client.remote_networks.get_v1remote_networks(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote_networks.<a href="src/fern/remote_networks/client.py">post_v1remote_networks</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create  remote network IPSec tunnels.
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

client.remote_networks.post_v1remote_networks(
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

**request:** `RemoteNetworksIpsecTunnelSet` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote_networks.<a href="src/fern/remote_networks/client.py">put_v1remote_networks</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify remote network IPSec tunnels.
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

client.remote_networks.put_v1remote_networks(
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

**request:** `RemoteNetworksIpsecTunnelSet` 
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote_networks.<a href="src/fern/remote_networks/client.py">delete_v1remote_networks</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows you to delete the set of IPSec tunnels.
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

client.remote_networks.delete_v1remote_networks(
    remote_networks_prefix="remote_networks_prefix",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**remote_networks_prefix:** `str` — remote networks prefix for bulk deletion
    
</dd>
</dl>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of remote networks along with their names.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote_networks.<a href="src/fern/remote_networks/client.py">get_v1remote_networks_read</a>(...) -> RemoteNetworksReadResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the remote networks IPSec tunnel status by UUID.
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

client.remote_networks.get_v1remote_networks_read(
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

**id:** `str` — UUID for the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.remote_networks.<a href="src/fern/remote_networks/client.py">post_v1remote_networks_read</a>(...) -> UuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request to read remote network IPSec tunnels.
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

client.remote_networks.post_v1remote_networks_read()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_tenant_name:** `typing.Optional[str]` — Sub-tenant name in a panorama multi-tenancy setup.
    
</dd>
</dl>

<dl>
<dd>

**remote_networks_names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

