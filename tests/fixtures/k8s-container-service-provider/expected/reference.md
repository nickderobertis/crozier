# Reference
## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py">get_health</a>() -> Health</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the health status of the service
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

client.health.get_health()

```
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

## Containers
<details><summary><code>client.containers.<a href="src/fern/containers/client.py">list_containers</a>(...) -> ContainerList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of containers with pagination support
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

client.containers.list_containers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**max_page_size:** `typing.Optional[int]` — Maximum number of resources to return in a single page
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Token indicating the starting point for the page
    
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

<details><summary><code>client.containers.<a href="src/fern/containers/client.py">create_container</a>(...) -> Container</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new container instance
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
from fern import FernApi, ContainerSpec, ContainerSpecServiceType, ContainerMetadata, ContainerImage, ContainerResources, ContainerCpu, ContainerMemory
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.containers.create_container(
    id="my-nginx-container",
    spec=ContainerSpec(
        service_type=ContainerSpecServiceType.CONTAINER,
        metadata=ContainerMetadata(
            name="name",
        ),
        image=ContainerImage(
            reference="quay.io/myapp:v1.2",
        ),
        resources=ContainerResources(
            cpu=ContainerCpu(
                min=1,
                max=1,
            ),
            memory=ContainerMemory(
                min="min",
                max="max",
            ),
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

**request:** `Container` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 

Optional client-specified ID for the container. If not provided,
the server will generate an ID.

Requirements (per AEP-122):
- 1-63 characters long
- Start with a lowercase letter or digit
- Contain only lowercase letters, numbers, and hyphens
- End with letter or number
    
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

<details><summary><code>client.containers.<a href="src/fern/containers/client.py">get_container</a>(...) -> Container</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific container instance by ID
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

client.containers.get_container(
    container_id="my-nginx-container",
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

**container_id:** `str` — Unique identifier for the container
    
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

<details><summary><code>client.containers.<a href="src/fern/containers/client.py">delete_container</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific container instance
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

client.containers.delete_container(
    container_id="my-nginx-container",
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

**container_id:** `str` — Unique identifier for the container
    
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

