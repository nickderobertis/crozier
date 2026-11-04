# Reference
<details><summary><code>client.<a href="src/fern/client.py">root_get</a>() -> str</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.root_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py">index_v1ping_get</a>() -> typing.Any</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.index_v1ping_get()

```
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

## Sandbox
<details><summary><code>client.sandbox.<a href="src/fern/sandbox/client.py">run_code</a>(...) -> RunCodeResponseOutput</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.sandbox.run_code(
    code="print(\"hello\")",
    language="python",
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

**code:** `str` — the code to run
    
</dd>
</dl>

<dl>
<dd>

**language:** `RunCodeRequestLanguage` — the language or execution mode to run the code
    
</dd>
</dl>

<dl>
<dd>

**compile_timeout:** `typing.Optional[float]` — compile timeout for compiled languages
    
</dd>
</dl>

<dl>
<dd>

**run_timeout:** `typing.Optional[float]` — code run timeout
    
</dd>
</dl>

<dl>
<dd>

**stdin:** `typing.Optional[str]` — optional string to pass into stdin
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.Dict[str, str]]` — a dict from file path to base64 encoded file content
    
</dd>
</dl>

<dl>
<dd>

**fetch_files:** `typing.Optional[typing.List[str]]` — a list of file paths to fetch after code execution
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox.<a href="src/fern/sandbox/client.py">run_code_in_jupyter</a>(...) -> RunJupyterResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.sandbox.run_code_in_jupyter(
    cells=[
        "a = 123",
        "a",
        "print(a)",
        "import sys; sys.stderr.write(\"stderr message\")",
        "raise RuntimeError(\"error message\")"
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

**cells:** `typing.List[str]` — list of code blocks to run in jupyter notebook
    
</dd>
</dl>

<dl>
<dd>

**cell_timeout:** `typing.Optional[float]` — max run time for each of the cells
    
</dd>
</dl>

<dl>
<dd>

**total_timeout:** `typing.Optional[float]` — max run time for all the cells
    
</dd>
</dl>

<dl>
<dd>

**kernel:** `typing.Optional[RunJupyterRequestKernel]` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.Dict[str, str]]` — a dict from file path to base64 encoded file content
    
</dd>
</dl>

<dl>
<dd>

**fetch_files:** `typing.Optional[typing.List[str]]` — a list of file paths to fetch after code execution
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Datasets
<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">list_datasets</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all registered datasets
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
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.list_datasets()

```
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

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">list_ids</a>(...) -> typing.List[ListIdsListIdsPostResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all ids of a dataset
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
from fern import FernApi, TestConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.list_ids(
    dataset="dataset",
    config=TestConfig(),
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

**request:** `GetPromptsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_prompt</a>(...) -> typing.List[Prompt]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get prompts of a dataset
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
from fern import FernApi, TestConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.get_prompt(
    dataset="dataset",
    config=TestConfig(),
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

**request:** `GetPromptsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_prompt_by_id</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single prompt given id in a dataset
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
from fern import FernApi, TestConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.get_prompt_by_id(
    dataset="dataset",
    config=TestConfig(),
    id=1,
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

**dataset:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `TestConfig` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `GetPromptByIdRequestId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">submit</a>(...) -> EvalResultOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a single problem in a dataset
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
from fern import FernApi, TestConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.submit(
    dataset="dataset",
    id=1,
    completion="completion",
    config=TestConfig(),
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

**dataset:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `SubmitRequestId` 
    
</dd>
</dl>

<dl>
<dd>

**completion:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `TestConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_metrics</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the metrics given all problem results in a dataset (partially supported)
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
from fern import FernApi, TestConfig, EvalResultInput, EvalTestCaseInput, RunCodeResponseInput

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.get_metrics(
    dataset="dataset",
    config=TestConfig(),
    results=[
        EvalResultInput(
            id=1,
            accepted=True,
            extracted_code="extracted_code",
            tests=[
                EvalTestCaseInput(
                    passed=True,
                    exec_info=RunCodeResponseInput(
                        status="Success",
                        message="message",
                    ),
                )
            ],
        )
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

**dataset:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `TestConfig` 
    
</dd>
</dl>

<dl>
<dd>

**results:** `typing.List[EvalResultInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_metrics_function</a>(...) -> GetMetricsFunctionResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the function to generate the metrics given results (partially supported)
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
from fern import FernApi, TestConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.get_metrics_function(
    dataset="dataset",
    config=TestConfig(),
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

**dataset:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `TestConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

