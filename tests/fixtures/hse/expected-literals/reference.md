# Reference
## global
<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L35-L62">events_get</a>(...) -> Events</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all event counter information.
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

client.global_.events_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L64-L100">events_in_file_get</a>(...) -> Events</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all event counter information for file.
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

client.global_.events_in_file_get(
    file="cn.c",
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

**file:** `str` — Basename of file.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L102-L145">events_in_file_in_function_get</a>(...) -> Events</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all event counter information for function in file.
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

client.global_.events_in_file_in_function_get(
    file="cn.c",
    function="table_create",
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

**file:** `str` — Basename of file.
    
</dd>
</dl>

<dl>
<dd>

**function:** `str` — Function name.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L147-L195">events_in_file_in_function_on_lineno_get</a>(...) -> Events</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all event counter information for function on line number of file.
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

client.global_.events_in_file_in_function_on_lineno_get(
    file="cn.c",
    function="table_create",
    lineno="420",
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

**file:** `str` — Basename of file.
    
</dd>
</dl>

<dl>
<dd>

**function:** `str` — Function name.
    
</dd>
</dl>

<dl>
<dd>

**lineno:** `str` — Line number.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L197-L224">kmc_vmstat_get</a>(...) -> typing.List[KmcVmstatGetResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get virtual memory statistics.
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

client.global_.kmc_vmstat_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L226-L253">params_get</a>(...) -> ParamsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all global parameters.
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

client.global_.params_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L255-L291">param_get</a>(...) -> ParamGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the value of the global parameter.
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

client.global_.param_get(
    param="logging.enabled",
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

**param:** `str` — Parameter to interact with.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L293-L324">param_set</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the value of the global parameter.
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

client.global_.param_set(
    param="logging.enabled",
    request={
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

**param:** `str` — Parameter to interact with.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ParamSetRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L326-L353">perfc_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information.
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

client.global_.perfc_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L355-L391">perfc_in_group_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information for group.
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

client.global_.perfc_in_group_get(
    group="global",
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

**group:** `str` — Performance counter group.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L393-L436">perfc_in_group_in_set_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information for group in set.
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

client.global_.perfc_in_group_in_set_get(
    group="global",
    set_="CNCOMP",
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

**group:** `str` — Performance counter group.
    
</dd>
</dl>

<dl>
<dd>

**set:** `str` — Performance counter set.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L438-L486">perfc_in_group_in_set_with_name_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information for group in set with name.
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

client.global_.perfc_in_group_in_set_with_name_get(
    group="global",
    set_="CNCOMP",
    counter_name="kcompact",
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

**group:** `str` — Performance counter group.
    
</dd>
</dl>

<dl>
<dd>

**set:** `str` — Performance counter set.
    
</dd>
</dl>

<dl>
<dd>

**counter_name:** `str` — Performance counter name.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_.<a href="src/fern/global_/client.py#L488-L515">workqueues_get</a>(...) -> typing.List[WorkqueuesGetResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the process' `/proc/self/task/[tid]/stat` information.
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

client.global_.workqueues_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## kvdb
<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L36-L72">compact_status_get</a>(...) -> KvdbCompactStatusGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current KVDB compaction status.
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

client.kvdb.compact_status_get(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L74-L100">compact_request</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a KVDB compaction request.
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

client.kvdb.compact_request(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L102-L128">compact_cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a KVDB compaction request.
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

client.kvdb.compact_cancel(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L130-L166">csched_get</a>(...) -> typing.List[KvdbCschedGetResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about all current KVDB compaction jobs.
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

client.kvdb.csched_get(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L168-L204">home_get</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get KVDB home.
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

client.kvdb.home_get(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L206-L242">params_get</a>(...) -> KvdbParamsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all KVDB parameters.
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

client.kvdb.params_get(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L244-L285">param_get</a>(...) -> KvdbParamGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the value of the KVDB parameter.
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

client.kvdb.param_get(
    alias="0",
    param="logging.enabled",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**param:** `str` — Parameter to interact with.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L287-L327">param_set</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the value of the KVDB parameter.
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

client.kvdb.param_set(
    alias="0",
    param="logging.enabled",
    request={
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**param:** `str` — Parameter to interact with.
    
</dd>
</dl>

<dl>
<dd>

**request:** `KvdbParamSetRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L329-L365">media_classes_get</a>(...) -> typing.List[Mclass]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of configured media classes and their paths.
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

client.kvdb.media_classes_get(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L367-L408">media_class_get</a>(...) -> KvdbMediaClassGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a media class.
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

client.kvdb.media_class_get(
    alias="0",
    mclass="capacity",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**mclass:** `Mclass` — Media class name.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L410-L446">kvs_get</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all KVS names.
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

client.kvdb.kvs_get(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L448-L484">perfc_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information.
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

client.kvdb.perfc_get(
    alias="0",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L486-L527">perfc_in_set_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information.
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

client.kvdb.perfc_in_set_get(
    alias="0",
    set_="CNCOMP",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**set:** `str` — Performance counter set.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvdb.<a href="src/fern/kvdb/client.py#L529-L577">perfc_in_set_with_name_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information.
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

client.kvdb.perfc_in_set_with_name_get(
    alias="0",
    set_="CNCOMP",
    counter_name="kcompact",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**set:** `str` — Performance counter set.
    
</dd>
</dl>

<dl>
<dd>

**counter_name:** `str` — Performance counter name.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## kvs
<details><summary><code>client.kvs.<a href="src/fern/kvs/client.py#L33-L84">cn_tree_get</a>(...) -> KvsCnTreeGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the KVS's cN tree.
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

client.kvs.cn_tree_get(
    alias="0",
    kvs_name="kvs1",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**kvs_name:** `str` — Name of the KVS.
    
</dd>
</dl>

<dl>
<dd>

**human:** `typing.Optional[bool]` — Humanize certain values.
    
</dd>
</dl>

<dl>
<dd>

**kvsets:** `typing.Optional[bool]` — Include kvset details in output.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvs.<a href="src/fern/kvs/client.py#L86-L127">params_get</a>(...) -> KvsParamsGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all KVS parameters.
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

client.kvs.params_get(
    alias="0",
    kvs_name="kvs1",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**kvs_name:** `str` — Name of the KVS.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvs.<a href="src/fern/kvs/client.py#L129-L175">param_get</a>(...) -> KvsParamGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the value of the KVS parameter.
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

client.kvs.param_get(
    alias="0",
    kvs_name="kvs1",
    param="logging.enabled",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**kvs_name:** `str` — Name of the KVS.
    
</dd>
</dl>

<dl>
<dd>

**param:** `str` — Parameter to interact with.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvs.<a href="src/fern/kvs/client.py#L177-L222">param_set</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the value of the KVS parameter.
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

client.kvs.param_set(
    alias="0",
    kvs_name="kvs1",
    param="logging.enabled",
    request={
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**kvs_name:** `str` — Name of the KVS.
    
</dd>
</dl>

<dl>
<dd>

**param:** `str` — Parameter to interact with.
    
</dd>
</dl>

<dl>
<dd>

**request:** `KvsParamSetRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvs.<a href="src/fern/kvs/client.py#L224-L265">perfc_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information.
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

client.kvs.perfc_get(
    alias="0",
    kvs_name="kvs1",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**kvs_name:** `str` — Name of the KVS.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvs.<a href="src/fern/kvs/client.py#L267-L315">perfc_in_set_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information.
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

client.kvs.perfc_in_set_get(
    alias="0",
    kvs_name="kvs1",
    set_="CNCOMP",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**kvs_name:** `str` — Name of the KVS.
    
</dd>
</dl>

<dl>
<dd>

**set:** `str` — Performance counter set.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kvs.<a href="src/fern/kvs/client.py#L317-L370">perfc_in_set_with_name_get</a>(...) -> PerformanceCounters</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all performance counter information.
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

client.kvs.perfc_in_set_with_name_get(
    alias="0",
    kvs_name="kvs1",
    set_="CNCOMP",
    counter_name="kcompact",
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

**alias:** `str` — Alias for a KVDB.
    
</dd>
</dl>

<dl>
<dd>

**kvs_name:** `str` — Name of the KVS.
    
</dd>
</dl>

<dl>
<dd>

**set:** `str` — Performance counter set.
    
</dd>
</dl>

<dl>
<dd>

**counter_name:** `str` — Performance counter name.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Pretty print the response body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

