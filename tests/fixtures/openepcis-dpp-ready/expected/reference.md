# Reference
## Life Cycle API
<details><summary><code>client.life_cycle_api.<a href="src/fern/life_cycle_api/client.py">read_dpp_by_id</a>(...) -> DigitalProductPassport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the DPP with the specified DPP ID. Conformance: shall.
</dd>
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
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.life_cycle_api.read_dpp_by_id(
    dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dpp_id:** `Identifier` — The DPP's unique identifier (EN 18223), percent-encoded in the path.
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[ReadDppByIdRequestRepresentation]` — Payload form per EN 18222 clause 8.1. Absent implies `compressed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.life_cycle_api.<a href="src/fern/life_cycle_api/client.py">delete_dpp_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the DPP with the specified DPP ID (end of life). Conformance: should.
</dd>
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
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.life_cycle_api.delete_dpp_by_id(
    dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dpp_id:** `Identifier` — The DPP's unique identifier (EN 18223), percent-encoded in the path.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.life_cycle_api.<a href="src/fern/life_cycle_api/client.py">update_dpp_by_id</a>(...) -> DigitalProductPassport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partial update of a DPP. The body carries only the parts to update or extend
(RFC 7396 JSON Merge Patch may be used). If any part fails, the whole update
fails and no change is adopted. All changes are archived per EN 18221.
Conformance: shall where authorized third parties hold write access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DigitalProductPassportCompressed, Granularity
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.life_cycle_api.update_dpp_by_id(
    dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
    request=DigitalProductPassportCompressed(
        digital_product_passport_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
        unique_product_identifier="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
        granularity=Granularity.MODEL,
        dpp_schema_version="EN 18223:2026",
        dpp_status="active",
        last_updated=datetime.datetime.fromisoformat("2026-06-08T15:30:00+00:00"),
        economic_operator_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
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

**dpp_id:** `Identifier` — The DPP's unique identifier (EN 18223), percent-encoded in the path.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DigitalProductPassport` 
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[UpdateDppByIdRequestRepresentation]` — Payload form per EN 18222 clause 8.1. Absent implies `compressed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.life_cycle_api.<a href="src/fern/life_cycle_api/client.py">read_dpp_by_product_id</a>(...) -> DigitalProductPassport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current active DPP (latest version) for the unique product identifier (EN 18219 GS1 Digital Link). Conformance: shall.
</dd>
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
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.life_cycle_api.read_dpp_by_product_id(
    product_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `Identifier` — Unique product identifier (EN 18219 GS1 Digital Link), percent-encoded.
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[ReadDppByProductIdRequestRepresentation]` — Payload form per EN 18222 clause 8.1. Absent implies `compressed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.life_cycle_api.<a href="src/fern/life_cycle_api/client.py">read_dpp_version_by_id_and_date</a>(...) -> DigitalProductPassport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the DPP version current at the given date (archived versions per EN 18221). Conformance: should.
</dd>
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
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.life_cycle_api.read_dpp_version_by_id_and_date(
    dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
    date=datetime.datetime.fromisoformat("2026-06-08T15:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dpp_id:** `Identifier` — The DPP's unique identifier (EN 18223), percent-encoded in the path.
    
</dd>
</dl>

<dl>
<dd>

**date:** `Timestamp` — UTC-based timestamp (ISO 8601-1) for which the version is requested.
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation]` — Payload form per EN 18222 clause 8.1. Absent implies `compressed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.life_cycle_api.<a href="src/fern/life_cycle_api/client.py">read_dpp_ids_by_product_ids</a>(...) -> DppIdPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the DPP identifiers matching a set of product identifiers (discovery). Paginated by `limit` and `cursor` (the cursor shall not be empty). Conformance: shall.
</dd>
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
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.life_cycle_api.read_dpp_ids_by_product_ids(
    product_ids=[
        "https://id.gs1.org/01/09521002005004/21/BAT2024-001"
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

**product_ids:** `typing.List[Identifier]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of identifiers to return in this page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque, non-empty pagination token from a prior response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.life_cycle_api.<a href="src/fern/life_cycle_api/client.py">create_dpp</a>(...) -> CreateDppResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new DPP and returns its DPP ID. Conformance: should.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DigitalProductPassportCompressed, Granularity
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.life_cycle_api.create_dpp(
    request=DigitalProductPassportCompressed(
        digital_product_passport_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
        unique_product_identifier="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
        granularity=Granularity.MODEL,
        dpp_schema_version="EN 18223:2026",
        dpp_status="active",
        last_updated=datetime.datetime.fromisoformat("2026-06-08T15:30:00+00:00"),
        economic_operator_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
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

**request:** `DigitalProductPassport` 
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[CreateDppRequestRepresentation]` — Payload form per EN 18222 clause 8.1. Absent implies `compressed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Registry API
<details><summary><code>client.registry_api.<a href="src/fern/registry_api/client.py">register_product_dpp</a>(...) -> RegisterResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a new DPP at the DPP registry (served by the registry server) and returns a unique registration identifier.
</dd>
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
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry_api.register_product_dpp(
    unique_product_identifier="uniqueProductIdentifier",
    digital_product_passport_id="digitalProductPassportId",
    unique_economic_operator_identifier="uniqueEconomicOperatorIdentifier",
    dpp_api_endpoint="dppApiEndpoint",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unique_product_identifier:** `str` — Unique product identifier per EN 18219.
    
</dd>
</dl>

<dl>
<dd>

**digital_product_passport_id:** `str` — The DPP instance identifier.
    
</dd>
</dl>

<dl>
<dd>

**unique_economic_operator_identifier:** `str` — Economic operator identifier per EN 18219.
    
</dd>
</dl>

<dl>
<dd>

**dpp_api_endpoint:** `str` — URL of the DPP API service hosting this DPP.
    
</dd>
</dl>

<dl>
<dd>

**backup_unique_economic_operator_identifier:** `typing.Optional[str]` — Economic operator identifier of the back-up operator per EN 18219.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Fine Granular API
<details><summary><code>client.fine_granular_api.<a href="src/fern/fine_granular_api/client.py">read_data_element</a>(...) -> DataElement</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single data element of a DPP by its absolute path. `elementIdPath` follows RFC 9535 JSONPath and is percent-encoded. Conformance: should.
</dd>
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
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fine_granular_api.read_data_element(
    dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
    element_id_path="elementIdPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dpp_id:** `Identifier` — The DPP's unique identifier (EN 18223), percent-encoded in the path.
    
</dd>
</dl>

<dl>
<dd>

**element_id_path:** `str` — RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[ReadDataElementRequestRepresentation]` — Payload form per EN 18222 clause 8.1. Absent implies `compressed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fine_granular_api.<a href="src/fern/fine_granular_api/client.py">update_data_element</a>(...) -> DataElement</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates, amends, or removes a single data element of a DPP at the given RFC 9535 JSONPath. Changes are archived per EN 18221. Conformance: should where authorized third parties hold write access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DataElement_SingleValuedDataElement
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    api_key="<X-API-KEY>",
    api_key="<API-KEY>",
    api_key_secret="<API-KEY-SECRET>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fine_granular_api.update_data_element(
    dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
    element_id_path="elementIdPath",
    request=DataElement_SingleValuedDataElement(
        element_id="elementId",
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

**dpp_id:** `Identifier` — The DPP's unique identifier (EN 18223), percent-encoded in the path.
    
</dd>
</dl>

<dl>
<dd>

**element_id_path:** `str` — RFC 9535 JSONPath to the element (e.g. `$.netWeight.value`), percent-encoded.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataElement` 
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[UpdateDataElementRequestRepresentation]` — Payload form per EN 18222 clause 8.1. Absent implies `compressed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

