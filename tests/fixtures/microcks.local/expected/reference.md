# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_resources_by_service</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.get_resources_by_service(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — Unique identifier of the Service or API the resources are attached to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_resource</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.get_resource(
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

**name:** `str` — Unique name/business identifier of the Service or API resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## job
<details><summary><code>client.job.<a href="src/fern/job/client.py">get_import_jobs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of ImportJobs
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.get_import_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page of ImportJobs to retrieve (starts at and defaults to 0)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name like criterion for query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">create_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new ImportJob
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.create_import_job(
    name="name",
    repository_url="repositoryUrl",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Unique distinct name of this ImportJob
    
</dd>
</dl>

<dl>
<dd>

**repository_url:** `str` — URL of mocks and tests repository artifact
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether this ImportJob is active (ie. scheduled for execution)
    
</dd>
</dl>

<dl>
<dd>

**created_date:** `typing.Optional[dt.datetime]` — Creation date for this ImportJob
    
</dd>
</dl>

<dl>
<dd>

**etag:** `typing.Optional[str]` — Etag of repository URL during previous import. Is used for not re-importing if no recent changes
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `typing.Optional[str]` — Reserved for future usage
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier of ImportJob
    
</dd>
</dl>

<dl>
<dd>

**last_import_date:** `typing.Optional[dt.datetime]` — Date last import was done
    
</dd>
</dl>

<dl>
<dd>

**last_import_error:** `typing.Optional[str]` — Error message of last import (if any)
    
</dd>
</dl>

<dl>
<dd>

**main_artifact:** `typing.Optional[bool]` — Flag telling if considered as primary or secondary artifact. Default to `true`
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[Metadata]` — Metadata of ImportJob
    
</dd>
</dl>

<dl>
<dd>

**repository_disable_ssl_validation:** `typing.Optional[bool]` — Whether to disable SSL certificate verification when checking repository
    
</dd>
</dl>

<dl>
<dd>

**secret_ref:** `typing.Optional[SecretRef]` — Reference of a Secret to used when checking repository
    
</dd>
</dl>

<dl>
<dd>

**service_refs:** `typing.Optional[typing.Sequence[ServiceRef]]` — References of Services discovered when checking repository
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_import_job_counter</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.get_import_job_counter()

```
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

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an ImportJob using its identifier
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.get_import_job(
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

**id:** `str` — Unique identifier of ImportJob to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">update_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an ImportJob
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.update_import_job(
    id_="id",
    name="name",
    repository_url="repositoryUrl",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `str` — Unique identifier of ImportJob to manage
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Unique distinct name of this ImportJob
    
</dd>
</dl>

<dl>
<dd>

**repository_url:** `str` — URL of mocks and tests repository artifact
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether this ImportJob is active (ie. scheduled for execution)
    
</dd>
</dl>

<dl>
<dd>

**created_date:** `typing.Optional[dt.datetime]` — Creation date for this ImportJob
    
</dd>
</dl>

<dl>
<dd>

**etag:** `typing.Optional[str]` — Etag of repository URL during previous import. Is used for not re-importing if no recent changes
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `typing.Optional[str]` — Reserved for future usage
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier of ImportJob
    
</dd>
</dl>

<dl>
<dd>

**last_import_date:** `typing.Optional[dt.datetime]` — Date last import was done
    
</dd>
</dl>

<dl>
<dd>

**last_import_error:** `typing.Optional[str]` — Error message of last import (if any)
    
</dd>
</dl>

<dl>
<dd>

**main_artifact:** `typing.Optional[bool]` — Flag telling if considered as primary or secondary artifact. Default to `true`
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[Metadata]` — Metadata of ImportJob
    
</dd>
</dl>

<dl>
<dd>

**repository_disable_ssl_validation:** `typing.Optional[bool]` — Whether to disable SSL certificate verification when checking repository
    
</dd>
</dl>

<dl>
<dd>

**secret_ref:** `typing.Optional[SecretRef]` — Reference of a Secret to used when checking repository
    
</dd>
</dl>

<dl>
<dd>

**service_refs:** `typing.Optional[typing.Sequence[ServiceRef]]` — References of Services discovered when checking repository
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">delete_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an ImportJob
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.delete_import_job(
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

**id:** `str` — Unique identifier of ImportJob to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">activate_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Make an ImportJob active, so that it is executed
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.activate_import_job(
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

**id:** `str` — Unique identifier of ImportJob to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">start_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starting an ImportJob forces it to immediatly import mock definitions
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.start_import_job(
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

**id:** `str` — Unique identifier of ImportJob to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">stop_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stopping an ImportJob desactivate it, so that it won't execute at next schedule
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.job.stop_import_job(
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

**id:** `str` — Unique identifier of ImportJob to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## mock
<details><summary><code>client.mock.<a href="src/fern/mock/client.py">import_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import a repository snapshot previsouly exported into Microcks
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.import_snapshot()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">get_services</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.get_services()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page of Services to retrieve (starts at and defaults to 0)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size of a page. Maximum number of Services to include in a response (defaults to 20)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">get_services_counter</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.get_services_counter()

```
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

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">get_services_labels</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.get_services_labels()

```
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

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">search_services</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.search_services(
    query_map={"queryMap": "queryMap"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query_map:** `typing.Dict[str, str]` — Map of criterion. Key can be simply 'name' with value as the searched string. You can also search by label using keys like 'labels.x' where 'x' is the label and value the label value
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">get_service</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.get_service(
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

**id:** `str` — Unique identifier of Service to managed
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[bool]` — Whether to include details on services messages into result. Default is false
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">delete_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Service
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.delete_service(
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

**id:** `str` — Unique identifier of Service to managed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">update_service_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.update_service_metadata(
    id="id",
    created_on=1,
    last_update=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of Service to managed
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `int` — Creation date of attached object
    
</dd>
</dl>

<dl>
<dd>

**last_update:** `int` — Last update of attached object
    
</dd>
</dl>

<dl>
<dd>

**annotations:** `typing.Optional[typing.Dict[str, str]]` — Annotations of attached object
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Dict[str, str]]` — Labels put on attached object
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mock.<a href="src/fern/mock/client.py">override_service_operation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.mock.override_service_operation(
    id="id",
    operation_name="operationName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of Service to managed
    
</dd>
</dl>

<dl>
<dd>

**operation_name:** `str` — Name of operation to update
    
</dd>
</dl>

<dl>
<dd>

**default_delay:** `typing.Optional[int]` — Default delay in milliseconds to apply to mock responses on this operation
    
</dd>
</dl>

<dl>
<dd>

**dispatcher:** `typing.Optional[str]` — Type of dispatcher to apply for this operation
    
</dd>
</dl>

<dl>
<dd>

**dispatcher_rules:** `typing.Optional[str]` — Rules of dispatcher for this operation
    
</dd>
</dl>

<dl>
<dd>

**parameter_constraints:** `typing.Optional[typing.Sequence[ParameterConstraint]]` — Constraints that may apply to incoming parameters on this operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## config
<details><summary><code>client.config.<a href="src/fern/config/client.py">get_features_configuration</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.get_features_configuration()

```
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

<details><summary><code>client.config.<a href="src/fern/config/client.py">get_keycloak_config</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.get_keycloak_config()

```
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

<details><summary><code>client.config.<a href="src/fern/config/client.py">get_secrets</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.get_secrets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page of Secrets to retrieve (starts at and defaults to 0)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size of a page. Maximum number of Secrets to include in a response (defaults to 20)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.config.<a href="src/fern/config/client.py">create_secret</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.create_secret(
    description="description",
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

**description:** `str` — Description of this Secret
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Unique distinct name of Secret
    
</dd>
</dl>

<dl>
<dd>

**ca_cert_pem:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier of Secret
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**token_header:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.config.<a href="src/fern/config/client.py">get_secrets_counter</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.get_secrets_counter()

```
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

<details><summary><code>client.config.<a href="src/fern/config/client.py">get_secret</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a Secret
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.get_secret(
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

**id:** `str` — Unique identifier of Secret to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.config.<a href="src/fern/config/client.py">update_secret</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Secret
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.update_secret(
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

**id:** `str` — Unique identifier of Secret to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.config.<a href="src/fern/config/client.py">delete_secret</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Secret
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.config.delete_secret(
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

**id:** `str` — Unique identifier of Secret to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## metrics
<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_conformance_metrics_aggregation</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.metrics.get_conformance_metrics_aggregation()

```
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

<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_service_test_conformance_metric</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.metrics.get_service_test_conformance_metric(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — Unique Services identifier this metrics are related to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_aggregated_invocations_stats</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.metrics.get_aggregated_invocations_stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**day:** `typing.Optional[str]` — The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_latest_aggregated_invocations_stats</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.metrics.get_latest_aggregated_invocations_stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of days to get back in time. Default is 20.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_top_ivnocations_stats_by_day</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.metrics.get_top_ivnocations_stats_by_day()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**day:** `typing.Optional[str]` — The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of top invoked mocks to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_invocation_stats_by_service</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.metrics.get_invocation_stats_by_service(
    service_name="serviceName",
    service_version="serviceVersion",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_name:** `str` — Name of service to get statistics for
    
</dd>
</dl>

<dl>
<dd>

**service_version:** `str` — Version of service to get statistics for
    
</dd>
</dl>

<dl>
<dd>

**day:** `typing.Optional[str]` — The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_latest_test_results</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.metrics.get_latest_test_results()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of days to consider for test results to return. Default is 7 (one week)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## test
<details><summary><code>client.test.<a href="src/fern/test/client.py">create_test</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TestRunnerType

client = FernApi(
    token="YOUR_TOKEN",
)
client.test.create_test(
    runner_type=TestRunnerType.HTTP,
    service_id="serviceId",
    test_endpoint="testEndpoint",
    timeout=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**runner_type:** `TestRunnerType` — Runner used for this test
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Unique identifier of service to test
    
</dd>
</dl>

<dl>
<dd>

**test_endpoint:** `str` — Endpoint to test for this service
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `int` — The maximum time (in milliseconds) to wait for this test ends
    
</dd>
</dl>

<dl>
<dd>

**filtered_operations:** `typing.Optional[typing.Sequence[str]]` — A restriction on service operations to test
    
</dd>
</dl>

<dl>
<dd>

**operation_headers:** `typing.Optional[OperationHeaders]` — This test operations headers override
    
</dd>
</dl>

<dl>
<dd>

**secret_name:** `typing.Optional[str]` — The name of Secret to use for connecting the test endpoint
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test.<a href="src/fern/test/client.py">get_test_results_by_service</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.test.get_test_results_by_service(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — Unique identifier of Service to manage TestResults for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test.<a href="src/fern/test/client.py">get_test_results_by_service_counter</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.test.get_test_results_by_service_counter(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — Unique identifier of Service to manage TestResults for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test.<a href="src/fern/test/client.py">get_test_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.test.get_test_result(
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

**id:** `str` — Unique identifier of TestResult to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test.<a href="src/fern/test/client.py">get_events_by_test_case</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.test.get_events_by_test_case(
    id="id",
    test_case_id="testCaseId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of TestResult to manage
    
</dd>
</dl>

<dl>
<dd>

**test_case_id:** `str` — Unique identifier of TetsCaseResult to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test.<a href="src/fern/test/client.py">get_messages_by_test_case</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.test.get_messages_by_test_case(
    id="id",
    test_case_id="testCaseId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of TestResult to manage
    
</dd>
</dl>

<dl>
<dd>

**test_case_id:** `str` — Unique identifier of TetsCaseResult to manage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test.<a href="src/fern/test/client.py">report_test_case_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Report a TestCaseResult (typically used by a Test runner)
</dd>
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

client = FernApi(
    token="YOUR_TOKEN",
)
client.test.report_test_case_result(
    id="id",
    operation_name="operationName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of TestResult to manage
    
</dd>
</dl>

<dl>
<dd>

**operation_name:** `str` — Name of related operation for this TestCase
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

