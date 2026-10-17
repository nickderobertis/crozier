# Reference
## Beacons
<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py">upload_firmware</a>(...)</code></summary>
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

client.beacons.upload_firmware(
    version="2.4.1",
    firmware_manifest_version="version",
    image="image",
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

**firmware_manifest_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**signed:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_manifest_signed:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py">update_firmware</a>(...)</code></summary>
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

client.beacons.update_firmware(
    beacon_id="beacon_id",
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

**beacon_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_patch_channel:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
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

