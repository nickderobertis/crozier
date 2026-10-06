# Reference
## ModuleFederation
<details><summary><code>client.module_federation.<a href="src/fern/module_federation/client.py">get_manifest_for_client_app</a>() -> typing.Dict[str, ModuleFederationDto]</code></summary>
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

client.module_federation.get_manifest_for_client_app()

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

<details><summary><code>client.module_federation.<a href="src/fern/module_federation/client.py">registry_module</a>(...)</code></summary>
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

client.module_federation.registry_module()

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

**name:** `typing.Optional[str]` — See 'name' in webpack.config.js
    
</dd>
</dl>

<dl>
<dd>

**remote_entry:** `typing.Optional[str]` — Remote entry
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `typing.Optional[str]` — Base Url
    
</dd>
</dl>

<dl>
<dd>

**export_module:** `typing.Optional[ModuleFederationDto]` 
    
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

