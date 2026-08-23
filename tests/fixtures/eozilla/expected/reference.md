# Reference
## Capabilities
<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">get_capabilities</a>() -> Capabilities</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The landing page provides links to the:
  * The OpenAPI-definition (no fixed path),
  * The Conformance statements (path /conformance),
  * The processes metadata (path /processes),
  * The endpoint for job monitoring (path /jobs).

For more information, see [OGC API — Processes — Part 1 Section 7.2](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_landing_page).
</dd>
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

client.capabilities.get_capabilities()

```
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

## ConformanceDeclaration
<details><summary><code>client.conformance_declaration.<a href="src/fern/conformance_declaration/client.py">get_conformance</a>() -> ConformanceDeclaration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A list of all conformance classes, specified in a standard, that the server conforms to.

| Conformance class | URI |
|-----------|-------|
|Core|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core|
|OGC Process Description|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description|
|JSON|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json|
|HTML|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/html|
|OpenAPI Specification 3.0|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30|
|Job list|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/job-list|
|Callback|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/callback|
|Dismiss|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/dismiss|

For more information, see [OGC API — Processes — Part 1 Section 7.4](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_conformance_classes).
</dd>
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

client.conformance_declaration.get_conformance()

```
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

## ProcessList
<details><summary><code>client.process_list.<a href="src/fern/process_list/client.py">get_processes</a>() -> ProcessList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The list of processes contains a summary of each process the OGC API - Processes offers, including the link to a more detailed description of the process.

For more information, see [OGC API — Processes — Part 1 Section 7.9](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_list).
</dd>
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

client.process_list.get_processes()

```
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

## ProcessDescription
<details><summary><code>client.process_description.<a href="src/fern/process_description/client.py">get_process</a>(...) -> ProcessDescription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The process description contains information about inputs and outputs and a link to the execution-endpoint for the process. The Core does not mandate the use of a specific process description to specify the interface of a process. That said, the Core requirements class makes the following recommendation:

Implementations **should** consider supporting the OGC process description.

For more information, see [OGC API — Processes — Part 1 Section 7.10](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_description).
</dd>
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

client.process_description.get_process(
    process_id="processID",
)

```
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

## ProcessRequest
<details><summary><code>client.process_request.<a href="src/fern/process_request/client.py">execute_process</a>(...) -> JobInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new job.

For more information, see [OGC API — Processes — Part 1 Section 7.11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_create_job).
</dd>
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

client.process_request.execute_process(
    process_id="processID",
)

```
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

**inputs:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**outputs:** `typing.Optional[typing.Dict[str, Output]]` 
    
</dd>
</dl>

<dl>
<dd>

**response:** `typing.Optional[ResponseType]` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber:** `typing.Optional[Subscriber]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## JobList
<details><summary><code>client.job_list.<a href="src/fern/job_list/client.py">get_jobs</a>() -> JobList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available jobs.

For more information, see [OGC API — Processes — Part 1 Section 11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_job_list).
</dd>
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

client.job_list.get_jobs()

```
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

## JobStatus
<details><summary><code>client.job_status.<a href="src/fern/job_status/client.py">get_job</a>(...) -> JobInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Show the status of a job.

For more information, see [OGC API — Processes — Part 1 Section 7.12](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_status_info).
</dd>
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

client.job_status.get_job(
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

**job_id:** `str` — Local identifier of a job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Dismiss
<details><summary><code>client.dismiss.<a href="src/fern/dismiss/client.py">job</a>(...) -> JobInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a job execution and removes it from the jobs list.

For more information, see [OGC API — Processes — Part 1 Section 13](https://docs.ogc.org/is/18-062r2/18-062r2.html#Dismiss).
</dd>
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

client.dismiss.job(
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

**job_id:** `str` — Local identifier of a job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## JobResults
<details><summary><code>client.job_results.<a href="src/fern/job_results/client.py">get_job_results</a>(...) -> JobResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available results of a job. In case of a failure, list errors instead.

For more information, see [OGC API — Processes — Part 1 Section 7.13](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_job_results).
</dd>
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

client.job_results.get_job_results(
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

**job_id:** `str` — Local identifier of a job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

