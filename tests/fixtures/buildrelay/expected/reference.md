# Reference
## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">submit_filesystem_job</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a build job from files on the filesystem to be uploaded to configured channels
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.submit_filesystem_job(
    project="Test Project",
    platform="windows",
    ingest_path="build",
    cdn_channel_labels=[
        "CDN Label"
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

**project:** `str` — Name of the project being built
    
</dd>
</dl>

<dl>
<dd>

**platform:** `str` — Target platform (e.g., windows, linux, macos)
    
</dd>
</dl>

<dl>
<dd>

**ingest_path:** `str` — Relative path within /builds directory containing build files. Cannot be absolute or contain '..'
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the build (e.g., version number)
    
</dd>
</dl>

<dl>
<dd>

**steam_channel_labels:** `typing.Optional[typing.List[str]]` — Labels of Steam channels to upload to
    
</dd>
</dl>

<dl>
<dd>

**cdn_channel_labels:** `typing.Optional[typing.List[str]]` — Labels of CDN channels to upload to
    
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

