# Reference
## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py">create_playback</a>(...) -> PlaybackSession</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.create_playback(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">stream_playback</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.stream_playback(
    ticket="blackcurrant....................",
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

**ticket:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[StreamPlaybackRequestMode]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**audio:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**video:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtitle:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[StreamPlaybackRequestDownload]` — Force a browser download instead of inline display.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_playback_diagnostics</a>(...) -> PlaybackDiagnostics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Owner-session-only, bounded in-memory statistics for one playback ticket. No Telegram credentials, internal addresses or ticket values are included. The edge merges authorized primary and secondary snapshots.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_playback_diagnostics(
    ticket="ticket",
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

**ticket:** `str` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_playback_tracks</a>(...) -> MediaTracks</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_playback_tracks(
    ticket="ticket",
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

**ticket:** `str` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_playback_subtitles</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_playback_subtitles(
    ticket="blackcurrant....................",
    track=1024,
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

**ticket:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**track:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[float]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">create_casting_relay</a>(...) -> CastingRelay</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.create_casting_relay(
    ticket="ticket",
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

**ticket:** `str` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">list_casting_devices</a>() -> CastingDevices</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.list_casting_devices()

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

<details><summary><code>client.files.<a href="src/fern/files/client.py">play_on_casting_device</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.play_on_casting_device(
    device_id="deviceId",
    ticket="ticket",
    server_url="serverUrl",
    mode="original",
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

**device_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ticket:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**server_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `CastingStartMode` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**audio:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtitle:** `typing.Optional[int]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">control_casting_device</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.control_casting_device(
    device_id="deviceId",
    command="play",
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

**device_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**command:** `ControlCastingDeviceRequestCommand` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">list_files</a>(...) -> ListFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List one folder or search within the authenticated user's drive.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.list_files()

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

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[FileListScope]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[Uuid]` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Resolve the listing root relative to the user's drive root.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[FileKind]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[FileStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — File-name search. Text search is case-insensitive; regex uses PostgreSQL-compatible regular expressions.
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[FileSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[typing.Union[FileCategory, typing.Sequence[FileCategory]]]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[FileSort]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SortOrder]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_file</a>(...) -> FileEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return file or folder metadata.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_file(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">trash_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move a file or folder to trash.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.trash_file(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">update_file</a>(...) -> FileEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename a file/folder or update its modification time.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.update_file(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">move_file</a>(...) -> FileEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move a file or folder using metadata only.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.move_file(
    file_id="fileId",
    idempotency_key="Idempotency-Key",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[ETag]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[Uuid]` 
    
</dd>
</dl>

<dl>
<dd>

**conflict_policy:** `typing.Optional[NameConflictPolicy]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">copy_file</a>(...) -> FileEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Copy a file or folder to another destination.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.copy_file(
    file_id="fileId",
    idempotency_key="Idempotency-Key",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[Uuid]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**conflict_policy:** `typing.Optional[NameConflictPolicy]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">restore_file</a>(...) -> FileEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore a trashed file or folder.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.restore_file(
    file_id="fileId",
    idempotency_key="Idempotency-Key",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">purge_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a trashed file or folder from the catalog.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.purge_file(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">clean_trash</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move every trashed file and folder owned by the authenticated user to deletion pending.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.clean_trash()

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

<details><summary><code>client.files.<a href="src/fern/files/client.py">download_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream complete or partial file content. The filename path segment gives command-line clients a useful output name.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.download_file(
    file_id="fileId",
    file_name="fileName",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[DownloadFileRequestDownload]` — Force a browser download instead of inline display.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">head_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return content metadata without streaming the file.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.head_file(
    file_id="fileId",
    file_name="fileName",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">download_file_legacy</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream file content using the legacy URL without a filename segment.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.download_file_legacy(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[DownloadFileLegacyRequestDownload]` — Force a browser download instead of inline display.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">head_file_legacy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return file metadata using the legacy URL without a filename segment.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.head_file_legacy(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_file_view_state</a>(...) -> typing.Optional[FileViewState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the authenticated user's synchronized viewer state for a file.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_file_view_state(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">put_file_view_state</a>(...) -> FileViewState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace the authenticated user's synchronized viewer state.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.put_file_view_state(
    file_id="fileId",
    kind="image",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `ViewerKind` 
    
</dd>
</dl>

<dl>
<dd>

**position:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**preferences:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**bookmarks:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">delete_file_view_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clear the authenticated user's synchronized viewer state.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.delete_file_view_state(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">bulk_move_files</a>(...) -> FileBulkResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transactionally move multiple files or folders.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.bulk_move_files(
    idempotency_key="Idempotency-Key",
    file_ids=[
        "fileIds"
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**file_ids:** `typing.List[Uuid]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[Uuid]` 
    
</dd>
</dl>

<dl>
<dd>

**conflict_policy:** `typing.Optional[NameConflictPolicy]` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">bulk_spam_files</a>(...) -> FileBulkResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Quarantine owned files and folders and revoke their sharing.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.bulk_spam_files(
    idempotency_key="Idempotency-Key",
    file_ids=[
        "fileIds"
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileBulkTrashRequest` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">bulk_trash_files</a>(...) -> FileBulkResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transactionally move multiple files or folders to trash.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.bulk_trash_files(
    idempotency_key="Idempotency-Key",
    file_ids=[
        "fileIds"
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileBulkTrashRequest` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_file_category_statistics</a>() -> typing.List[FileCategoryStatistics]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aggregate active file counts and bytes by category.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_file_category_statistics()

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

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_drive_statistics</a>() -> DriveStatistics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aggregate drive-level counters for the authenticated user.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_drive_statistics()

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

## Public shares
<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">create_public_playback</a>(...) -> PlaybackSession</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.create_public_playback(
    token="token",
    file_id="fileId",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">get_public_share</a>(...) -> PublicShare</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.get_public_share(
    token="token",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">list_public_share_files</a>(...) -> ListPublicShareFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List children within a publicly shared folder.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.list_public_share_files(
    token="token",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Folder path relative to the shared folder root.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">download_public_share_file</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.download_public_share_file(
    token="token",
    file_id="fileId",
    file_name="fileName",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[DownloadPublicShareFileRequestDownload]` — Force a browser download instead of inline display.
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">head_public_share_file</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.head_public_share_file(
    token="token",
    file_id="fileId",
    file_name="fileName",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">download_public_share</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.download_public_share(
    token="token",
    file_name="fileName",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[DownloadPublicShareRequestDownload]` — Force a browser download instead of inline display.
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">head_public_share</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.head_public_share(
    token="token",
    file_name="fileName",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">download_public_share_file_legacy</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.download_public_share_file_legacy(
    token="token",
    file_id="fileId",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[DownloadPublicShareFileLegacyRequestDownload]` — Force a browser download instead of inline display.
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">head_public_share_file_legacy</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.head_public_share_file_legacy(
    token="token",
    file_id="fileId",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">download_public_share_legacy</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.download_public_share_legacy(
    token="token",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[DownloadPublicShareLegacyRequestDownload]` — Force a browser download instead of inline display.
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[ETag]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">head_public_share_legacy</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.head_public_share_legacy(
    token="token",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">create_public_share_folder</a>(...) -> FileEntry</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.create_public_share_folder(
    token="token",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `FolderCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">trash_public_share_file</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.trash_public_share_file(
    token="token",
    file_id="fileId",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">update_public_share_file</a>(...) -> FileEntry</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.update_public_share_file(
    token="token",
    file_id="fileId",
    if_match="If-Match",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `ETag` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">create_public_share_upload</a>(...) -> UploadSession</code></summary>
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
import datetime

client = FernApi(
    token="<token>",
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.create_public_share_upload(
    token="token",
    idempotency_key="Idempotency-Key",
    name="name",
    size=1000000,
    mod_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UploadCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">put_public_share_upload_part</a>(...) -> UploadPart</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.public_shares.put_public_share_upload_part(...)
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**part_no:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">complete_public_share_upload</a>(...) -> FileEntry</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.complete_public_share_upload(
    token="token",
    upload_id="uploadId",
    idempotency_key="Idempotency-Key",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">abort_public_share_upload</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.abort_public_share_upload(
    token="token",
    upload_id="uploadId",
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

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**share_password:** `typing.Optional[str]` 
    
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

## System
<details><summary><code>client.system.<a href="src/fern/system/client.py">health_live</a>() -> HealthStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process liveness check.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.system.health_live()

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

<details><summary><code>client.system.<a href="src/fern/system/client.py">health_ready</a>() -> HealthStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Readiness check for PostgreSQL, migrations, and required runtime state.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.system.health_ready()

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

## Authentication
<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">telegram_login_start</a>(...) -> TelegramLoginStartResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Begin Telegram authentication and send a login code.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.telegram_login_start(
    idempotency_key="Idempotency-Key",
    phone_number="phoneNumber",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` — Phone number in E.164 format.
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">telegram_qr_login_start</a>(...) -> TelegramQrLoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Begin a resumable Telegram QR login flow.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.telegram_qr_login_start(
    idempotency_key="Idempotency-Key",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">telegram_qr_login_poll</a>(...) -> TokenPair</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Poll a Telegram QR login flow. Any API replica can resume the encrypted flow state.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.telegram_qr_login_poll(
    idempotency_key="Idempotency-Key",
    flow_id="flowId",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TelegramQrLoginPollRequest` 
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">telegram_login_verify_code</a>(...) -> TokenPair</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify the Telegram login code.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.telegram_login_verify_code(
    idempotency_key="Idempotency-Key",
    flow_id="flowId",
    code="code",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TelegramCodeVerifyRequest` 
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">telegram_login_verify_password</a>(...) -> TokenPair</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Complete Telegram two-step verification.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.telegram_login_verify_password(
    idempotency_key="Idempotency-Key",
    flow_id="flowId",
    password="password",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TelegramPasswordVerifyRequest` 
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">refresh_session</a>(...) -> TokenPair</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotate an access/refresh token pair.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.refresh_session(
    refresh_token="refreshToken",
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

**refresh_token:** `str` 
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">cookie_telegram_login_verify_code</a>(...) -> CookieSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Complete Telegram code verification and establish an HttpOnly cookie session.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.cookie_telegram_login_verify_code(
    idempotency_key="Idempotency-Key",
    flow_id="flowId",
    code="code",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TelegramCodeVerifyRequest` 
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">cookie_telegram_login_verify_password</a>(...) -> CookieSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Complete Telegram password verification and establish an HttpOnly cookie session.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.cookie_telegram_login_verify_password(
    idempotency_key="Idempotency-Key",
    flow_id="flowId",
    password="password",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TelegramPasswordVerifyRequest` 
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">cookie_telegram_qr_login_poll</a>(...) -> CookieSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Poll Telegram QR login and establish an HttpOnly cookie session when authorized.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.cookie_telegram_qr_login_poll(
    idempotency_key="Idempotency-Key",
    flow_id="flowId",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TelegramQrLoginPollRequest` 
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">refresh_cookie_session</a>() -> CookieSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotate session cookies using the HttpOnly refresh cookie.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.refresh_cookie_session()

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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">logout_cookie_session</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke the cookie session and clear its HttpOnly cookies.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.logout_cookie_session()

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

## Account
<details><summary><code>client.account.<a href="src/fern/account/client.py">get_current_user</a>() -> UserProfile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the authenticated user profile.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.account.get_current_user()

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

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_profile_photo</a>() -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the authenticated Telegram user's small profile photo.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.account.get_profile_photo()

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

<details><summary><code>client.account.<a href="src/fern/account/client.py">logout_session</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke the current session.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.account.logout_session()

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

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py">search_users</a>(...) -> typing.List[UserSearchResult]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.search_users(
    search="search",
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

**search:** `str` 
    
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

## Administration
<details><summary><code>client.administration.<a href="src/fern/administration/client.py">list_admin_users</a>(...) -> typing.List[AdminUserSummary]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.administration.list_admin_users()

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

**search:** `typing.Optional[str]` 
    
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

<details><summary><code>client.administration.<a href="src/fern/administration/client.py">update_admin_user</a>(...) -> AdminUserSummary</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.administration.update_admin_user(
    user_id=1000000,
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

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[UserRole]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.administration.<a href="src/fern/administration/client.py">revoke_admin_user_access</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.administration.revoke_admin_user_access(
    user_id=1000000,
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

**user_id:** `int` 
    
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

## API keys
<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">list_api_keys</a>(...) -> ListApiKeysResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.list_api_keys()

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

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">create_api_key</a>(...) -> ApiKeyCreated</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.create_api_key(
    idempotency_key="Idempotency-Key",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">revoke_api_key</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.revoke_api_key(
    api_key_id="apiKeyId",
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

**api_key_id:** `Uuid` 
    
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

## Sessions
<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">list_sessions</a>(...) -> ListSessionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all TelDrive sessions for the authenticated Telegram account.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sessions.list_sessions()

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

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">revoke_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke one TelDrive session. Revoking the current session invalidates its bearer token immediately.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sessions.revoke_session(
    session_id="sessionId",
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

**session_id:** `Uuid` 
    
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

## Channels
<details><summary><code>client.channels.<a href="src/fern/channels/client.py">list_channels</a>(...) -> ListChannelsResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.list_channels()

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

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">create_channel</a>(...) -> ChannelSummary</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.create_channel(
    idempotency_key="Idempotency-Key",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional display name. Telegram may choose the final title.
    
</dd>
</dl>

<dl>
<dd>

**selected:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">discover_channels</a>() -> typing.List[DiscoveredChannel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Telegram channels where the authenticated user can add administrators.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.discover_channels()

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

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">sync_channels</a>(...) -> typing.List[ChannelSummary]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discover and upsert manageable Telegram channels without deleting missing rows.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.sync_channels(
    idempotency_key="Idempotency-Key",
    channel_ids=[
        1000000
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**channel_ids:** `typing.List[int]` 
    
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

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">select_channel</a>(...) -> ChannelSummary</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.select_channel(
    channel_id=1000000,
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

**channel_id:** `int` 
    
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

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">delete_channel</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.delete_channel(
    channel_id=1000000,
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

**channel_id:** `int` 
    
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

## Bots
<details><summary><code>client.bots.<a href="src/fern/bots/client.py">list_bots</a>(...) -> ListBotsResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.list_bots()

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

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.bots.<a href="src/fern/bots/client.py">create_bots</a>(...) -> BotCreateResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.create_bots(
    idempotency_key="Idempotency-Key",
    tokens=[
        "tokens"
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**tokens:** `typing.List[str]` — Telegram bot tokens. Tokens are never returned by the API.
    
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

<details><summary><code>client.bots.<a href="src/fern/bots/client.py">get_bot_manager</a>() -> BotManagerResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.get_bot_manager()

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

<details><summary><code>client.bots.<a href="src/fern/bots/client.py">select_bot_manager</a>(...) -> BotManagerResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.select_bot_manager(
    idempotency_key="Idempotency-Key",
    bot_id=1000000,
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**bot_id:** `int` 
    
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

<details><summary><code>client.bots.<a href="src/fern/bots/client.py">clear_bot_manager</a>() -> BotManagerResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.clear_bot_manager()

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

<details><summary><code>client.bots.<a href="src/fern/bots/client.py">check_managed_bot_username</a>(...) -> CheckManagedBotUsernameResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.check_managed_bot_username(
    username="username",
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

**username:** `str` 
    
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

<details><summary><code>client.bots.<a href="src/fern/bots/client.py">create_managed_bot</a>(...) -> ManagedBotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a user-owned bot, exports its token without rotation and registers it in the chosen private channel. Retrying the same username recovers setup instead of creating another bot.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.create_managed_bot(
    idempotency_key="Idempotency-Key",
    name="name",
    username="username",
    channel_id="channelId",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` 
    
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

<details><summary><code>client.bots.<a href="src/fern/bots/client.py">delete_bot</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bots.delete_bot(
    bot_id=1000000,
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

**bot_id:** `int` 
    
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

## Events
<details><summary><code>client.events.<a href="src/fern/events/client.py">create_event_stream_ticket</a>() -> EventStreamTicket</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a short-lived browser-compatible event stream credential.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.create_event_stream_ticket()

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

<details><summary><code>client.events.<a href="src/fern/events/client.py">stream_events</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribe to ordered, replayable events for the authenticated user.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.stream_events()

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

**after:** `typing.Optional[int]` — Header-equivalent cursor for clients that cannot set Last-Event-ID.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional comma-separated event types to include.
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` — Resume after the last successfully processed event.
    
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

## Folders
<details><summary><code>client.folders.<a href="src/fern/folders/client.py">create_folder</a>(...) -> FileEntry</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.create_folder(
    idempotency_key="Idempotency-Key",
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FolderCreateRequest` 
    
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

## Uploads
<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">list_uploads</a>(...) -> ListUploadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List resumable upload sessions owned by the authenticated user.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.list_uploads()

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

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[UploadState]` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">create_upload</a>(...) -> UploadSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a durable upload session.
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
import datetime

client = FernApi(
    token="<token>",
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.create_upload(
    idempotency_key="Idempotency-Key",
    name="name",
    size=1000000,
    mod_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UploadCreateRequest` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">get_upload_statistics</a>(...) -> typing.List[UploadDailyStatistics]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return completed upload volume grouped by UTC day.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.get_upload_statistics()

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

**days:** `typing.Optional[int]` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">create_upload_import</a>(...) -> Job</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue local paths, recursive folders, and HTTP URLs for server-side upload.
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
from fern import FernApi, UploadImportSource
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.create_upload_import(
    destination="destination",
    sources=[
        UploadImportSource(
            type="local",
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

**destination:** `str` — Destination folder UUID or absolute drive path from root.
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.List[UploadImportSource]` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**exclude:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**min_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**part_concurrency:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**chunk_size:** `typing.Optional[int]` — Preferred upload part size. Values are aligned to the nearest 16 MiB.
    
</dd>
</dl>

<dl>
<dd>

**encryption:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">get_upload</a>(...) -> UploadSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect an upload for resume and conflict handling.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.get_upload(
    upload_id="uploadId",
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

**upload_id:** `Uuid` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">abort_upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Abort an upload and schedule physical Telegram cleanup.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.abort_upload(
    upload_id="uploadId",
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

**upload_id:** `Uuid` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">list_upload_parts</a>(...) -> ListUploadPartsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List parts already known to the upload session.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.list_upload_parts(
    upload_id="uploadId",
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

**upload_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">put_upload_part</a>(...) -> UploadPart</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload one part. The `(uploadId, partNo)` pair is the idempotency key.
An exact retry returns the existing stored part; conflicting size/checksum returns 409.
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
client.uploads.put_upload_part(...)
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

**upload_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**part_no:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">complete_upload</a>(...) -> FileEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate all parts and transactionally publish the file. A successful response
guarantees immediate read-after-write visibility.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.uploads.complete_upload(
    upload_id="uploadId",
    idempotency_key="Idempotency-Key",
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

**upload_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
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

## Shares
<details><summary><code>client.shares.<a href="src/fern/shares/client.py">list_file_shares</a>(...) -> ListFileSharesResponse</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.list_file_shares(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">create_share</a>(...) -> ShareCreated</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.create_share(
    file_id="fileId",
    idempotency_key="Idempotency-Key",
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `Uuid` — Stable UUID generated by the caller for safe request retries.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Optional password. The server stores only a password hash.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**max_downloads:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**permission:** `typing.Optional[SharePermission]` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">revoke_share</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.revoke_share(
    share_id="shareId",
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

**share_id:** `Uuid` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">update_share</a>(...) -> ShareSummary</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.update_share(
    share_id="shareId",
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

**share_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**clear_password:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**clear_expires_at:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**max_downloads:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**clear_max_downloads:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**permission:** `typing.Optional[SharePermission]` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">list_file_access_grants</a>(...) -> typing.List[FileAccessGrantSummary]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.list_file_access_grants(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">create_file_access_grant</a>(...) -> FileAccessGrantSummary</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.create_file_access_grant(
    file_id="fileId",
    grantee_user_id=1000000,
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

**file_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**grantee_user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**permission:** `typing.Optional[SharePermission]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">revoke_file_access_grant</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.revoke_file_access_grant(
    grant_id="grantId",
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

**grant_id:** `Uuid` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">update_file_access_grant</a>(...) -> FileAccessGrantSummary</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.update_file_access_grant(
    grant_id="grantId",
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

**grant_id:** `Uuid` 
    
</dd>
</dl>

<dl>
<dd>

**permission:** `typing.Optional[SharePermission]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**clear_expires_at:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">list_shared</a>() -> typing.List[FileEntry]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.list_shared()

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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">list_shared_with_me</a>() -> typing.List[SharedWithMeEntry]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.list_shared_with_me()

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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">list_incoming_spam</a>() -> typing.List[FileEntry]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.list_incoming_spam()

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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">mark_incoming_spam</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.mark_incoming_spam(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">restore_incoming_spam</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.restore_incoming_spam(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">dismiss_incoming_spam</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shares.dismiss_incoming_spam(
    file_id="fileId",
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

**file_id:** `Uuid` 
    
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

## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">list_jobs</a>(...) -> JobPage</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.list_jobs()

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

**cursor:** `typing.Optional[Cursor]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[JobState]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**queue:** `typing.Optional[str]` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">create_job</a>(...) -> Job</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.create_job(
    type="type",
    args={
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

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**args:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**queue:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_attempts:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job_statistics</a>() -> JobStatistics</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_job_statistics()

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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">list_job_queues</a>() -> JobQueueList</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.list_job_queues()

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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">pause_job_queue</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.pause_job_queue(
    queue="queue",
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

**queue:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">resume_job_queue</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.resume_job_queue(
    queue="queue",
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

**queue:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">purge_jobs</a>(...) -> JobPurgeResult</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.purge_jobs(
    status="available",
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

**status:** `JobState` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job</a>(...) -> Job</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_job(
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

**job_id:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">delete_job</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.delete_job(
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

**job_id:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">cancel_job</a>(...) -> Job</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.cancel_job(
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

**job_id:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">retry_job</a>(...) -> Job</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.retry_job(
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

**job_id:** `str` 
    
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

## Periodic Jobs
<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">list_periodic_jobs</a>() -> PeriodicJobList</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.list_periodic_jobs()

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

<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">create_periodic_job</a>(...) -> PeriodicJob</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.create_periodic_job(
    id="id",
    kind="kind",
    args={
        "key": "value"
    },
    queue="queue",
    priority=1,
    max_attempts=1,
    tags=[
        "tags"
    ],
    cron_expression="cronExpression",
    cron_timezone="cronTimezone",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**args:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**queue:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**max_attempts:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cron_expression:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cron_timezone:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">get_periodic_job_catalog</a>() -> PeriodicJobCatalog</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.get_periodic_job_catalog()

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

<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">reset_periodic_jobs</a>() -> PeriodicJobList</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.reset_periodic_jobs()

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

<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">update_periodic_job</a>(...) -> PeriodicJob</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.update_periodic_job(
    periodic_job_id="periodicJobId",
    kind="kind",
    args={
        "key": "value"
    },
    queue="queue",
    priority=1,
    max_attempts=1,
    tags=[
        "tags"
    ],
    cron_expression="cronExpression",
    cron_timezone="cronTimezone",
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

**periodic_job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**args:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**queue:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**max_attempts:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cron_expression:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cron_timezone:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">delete_periodic_job</a>(...)</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.delete_periodic_job(
    periodic_job_id="periodicJobId",
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

**periodic_job_id:** `str` 
    
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

<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">pause_periodic_job</a>(...) -> PeriodicJob</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.pause_periodic_job(
    periodic_job_id="periodicJobId",
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

**periodic_job_id:** `str` 
    
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

<details><summary><code>client.periodic_jobs.<a href="src/fern/periodic_jobs/client.py">resume_periodic_job</a>(...) -> PeriodicJob</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.periodic_jobs.resume_periodic_job(
    periodic_job_id="periodicJobId",
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

**periodic_job_id:** `str` 
    
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

## Storage
<details><summary><code>client.storage.<a href="src/fern/storage/client.py">get_storage_stats</a>() -> StorageDashboard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the authenticated user's storage statistics.
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.storage.get_storage_stats()

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

## Rclone
<details><summary><code>client.rclone.<a href="src/fern/rclone/client.py">action</a>(...) -> typing.Any</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.rclone.action(
    method="method",
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

**method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.rclone.<a href="src/fern/rclone/client.py">stage</a>(...) -> RcloneStageResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.rclone.stage(...)
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

**filename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
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

<details><summary><code>client.rclone.<a href="src/fern/rclone/client.py">local_content</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<X-Api-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.rclone.local_content(
    path="path",
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

**path:** `str` 
    
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

