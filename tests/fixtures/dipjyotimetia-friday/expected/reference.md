# Reference
## TestGeneration
<details><summary><code>client.test_generation.<a href="src/fern/test_generation/client.py">generate_tests</a>(...) -> GenerateResponse</code></summary>
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

client.test_generation.generate_tests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**jira_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gh_issue:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gh_repo:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**confluence_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` 
    
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

## WebCrawling
<details><summary><code>client.web_crawling.<a href="src/fern/web_crawling/client.py">crawl_site</a>(...) -> typing.Any</code></summary>
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

client.web_crawling.crawl_site(
    url="url",
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

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_pages:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**same_domain:** `typing.Optional[bool]` 
    
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

## HealthCheck
<details><summary><code>client.health_check.<a href="src/fern/health_check/client.py">health_check</a>() -> typing.Any</code></summary>
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

client.health_check.health_check()

```
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

## ApiTesting
<details><summary><code>client.api_testing.<a href="src/fern/api_testing/client.py">test_api</a>(...) -> ApiTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run API tests using either a spec file path or uploaded spec file
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

client.api_testing.test_api(
    spec_upload="example_spec_upload",
    base_url="base_url",
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

**base_url:** `str` — Base URL for API testing
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — Output file path
    
</dd>
</dl>

<dl>
<dd>

**spec_file:** `typing.Optional[str]` — Path to OpenAPI spec file
    
</dd>
</dl>

<dl>
<dd>

**spec_upload:** `typing.Optional[core.File]` — OpenAPI spec file upload
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[TestApiApiV1TestapiPostRequestProvider]` — LLM Provider
    
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

