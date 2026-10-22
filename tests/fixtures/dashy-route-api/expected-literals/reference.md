# Reference
## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py">list_config_files</a>() -> FileList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists every YAML config file in the user-data directory.
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

client.files.list_config_files()

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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_config_file</a>(...) -> Config</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the parsed config file as JSON.
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

client.files.get_config_file(
    filename="conf.yml",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">replace_config_file</a>(...) -> WriteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Overwrites the whole file. Writes to `conf.yml` are validated against the
config schema; sub-pages are not. A timestamped backup is taken first.
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
from fern import FernApi, PageInfo, Section
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.replace_config_file(
    filename="conf.yml",
    page_info=PageInfo(
        title="My Dashboard",
    ),
    sections=[
        Section(
            name="name",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Config` 
    
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

## Keys
<details><summary><code>client.keys.<a href="src/fern/keys/client.py">get_config_key</a>(...) -> KeyValue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single top-level key from the config.
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

client.keys.get_config_key(
    filename="conf.yml",
    key="pageInfo",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**key:** `GetConfigKeyRequestKey` — A top-level config key.
    
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

<details><summary><code>client.keys.<a href="src/fern/keys/client.py">replace_config_key</a>(...) -> WriteResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces a single top-level key, leaving the rest of the file untouched.
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
from fern import FernApi, AppConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.keys.replace_config_key(
    filename="conf.yml",
    key="pageInfo",
    request=AppConfig(
        theme="nord-frost",
        layout="auto",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**key:** `ReplaceConfigKeyRequestKey` — A top-level config key.
    
</dd>
</dl>

<dl>
<dd>

**request:** `KeyValue` 
    
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

## Sections
<details><summary><code>client.sections.<a href="src/fern/sections/client.py">add_section</a>(...) -> SectionResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Appends a new section. A `name` is required.
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
from fern import FernApi, Item
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sections.add_section(
    filename="conf.yml",
    name="Monitoring",
    icon="fas fa-chart-line",
    items=[
        Item(
            title="title",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Section` 
    
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

<details><summary><code>client.sections.<a href="src/fern/sections/client.py">get_section</a>(...) -> Section</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sections.get_section(
    filename="conf.yml",
    sid="0",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
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

<details><summary><code>client.sections.<a href="src/fern/sections/client.py">delete_section</a>(...) -> WriteResult</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sections.delete_section(
    filename="conf.yml",
    sid="0",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
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

<details><summary><code>client.sections.<a href="src/fern/sections/client.py">update_section</a>(...) -> UpdateSectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Shallow-merges the supplied fields. Sending `items` replaces the whole array.
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

client.sections.update_section(
    filename="conf.yml",
    sid="0",
    name="Renamed Section",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
</dd>
</dl>

<dl>
<dd>

**request:** `SectionFields` 
    
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

## Items
<details><summary><code>client.items.<a href="src/fern/items/client.py">list_items</a>(...) -> typing.List[Item]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.items.list_items(
    filename="conf.yml",
    sid="0",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
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

<details><summary><code>client.items.<a href="src/fern/items/client.py">add_item</a>(...) -> ItemResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Appends a new item to the section. A `title` is required.
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

client.items.add_item(
    filename="conf.yml",
    sid="0",
    title="Grafana",
    icon="hl-grafana",
    url="https://grafana.local",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
</dd>
</dl>

<dl>
<dd>

**request:** `Item` 
    
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

<details><summary><code>client.items.<a href="src/fern/items/client.py">get_item</a>(...) -> Item</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.items.get_item(
    filename="conf.yml",
    sid="0",
    iid="0",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
</dd>
</dl>

<dl>
<dd>

**iid:** `str` — Item index (zero-based) or exact `title` (URL-encoded).
    
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

<details><summary><code>client.items.<a href="src/fern/items/client.py">delete_item</a>(...) -> WriteResult</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.items.delete_item(
    filename="conf.yml",
    sid="0",
    iid="0",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
</dd>
</dl>

<dl>
<dd>

**iid:** `str` — Item index (zero-based) or exact `title` (URL-encoded).
    
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

<details><summary><code>client.items.<a href="src/fern/items/client.py">update_item</a>(...) -> UpdateItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Shallow-merges the supplied fields onto the item.
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

client.items.update_item(
    filename="conf.yml",
    sid="0",
    iid="0",
    url="https://grafana.example.com",
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

**filename:** `str` — A YAML config file in your user-data directory.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — Section index (zero-based) or exact `name` (URL-encoded).
    
</dd>
</dl>

<dl>
<dd>

**iid:** `str` — Item index (zero-based) or exact `title` (URL-encoded).
    
</dd>
</dl>

<dl>
<dd>

**request:** `ItemFields` 
    
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

