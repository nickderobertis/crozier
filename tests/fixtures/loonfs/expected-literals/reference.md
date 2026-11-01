# Reference
## Capabilities
<details><summary><code>client.capabilities.<a href="src/fern/capabilities/client.py">retrieve</a>() -> CapabilityDocument</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a summary of supported features and limits.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.capabilities.retrieve()

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

## namespaces
<details><summary><code>client.namespaces.<a href="src/fern/namespaces/client.py">create</a>(...) -> NamespaceMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new empty namespace.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.namespaces.create(
    namespace_id="demo",
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

**namespace_id:** `NamespaceId` — The durable ID of the new namespace.
    
</dd>
</dl>

<dl>
<dd>

**access:** `typing.Optional[NamespaceAccess]` 

The namespace's access mode, which can't be changed after the namespace is created. The
default is unrestricted.
    
</dd>
</dl>

<dl>
<dd>

**retention_window_ms:** `typing.Optional[int]` 

The namespace's retention window, in milliseconds, which must be positive. The reference
server's maintenance sweep then uses this window for the namespace instead of the server's
`retention_window_ms` setting. A `retention_window` maintenance run can change or clear the
window later.
    
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

<details><summary><code>client.namespaces.<a href="src/fern/namespaces/client.py">retrieve</a>(...) -> NamespaceMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current head and retention state for a namespace.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.namespaces.retrieve(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
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

<details><summary><code>client.namespaces.<a href="src/fern/namespaces/client.py">delete</a>(...) -> DeleteNamespaceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks a namespace as deleted. The namespace ID can never be used again to create or fork a namespace.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.namespaces.delete(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**expected_head_seq:** `typing.Optional[ChangeSeq]` — The head sequence that the namespace must still have for the delete to succeed.
    
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

<details><summary><code>client.namespaces.<a href="src/fern/namespaces/client.py">fork</a>(...) -> NamespaceMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new namespace from the source namespace's current head or from an unexpired snapshot.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.namespaces.fork(
    namespace_id="namespace_id",
    new_namespace_id="demo",
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

**namespace_id:** `str` — The source namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**new_namespace_id:** `NamespaceId` — The durable ID of the new namespace that the fork creates.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — An unexpired snapshot to fork from. Without it, the fork starts from the current head.
    
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

## Changes
<details><summary><code>client.changes.<a href="src/fern/changes/client.py">list</a>(...) -> ListChangesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns committed changes after a sequence. A snapshot limits the feed to its captured sequence.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.changes.list(
    namespace_id="namespace_id",
    after_seq=1000000,
    snapshot_id="pin_00000000000000000001-0000000000000002",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**after_seq:** `ChangeSeq` — The sequence after which to return committed changes.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — A snapshot to read the feed from. The feed ends at the sequence that the snapshot captured.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

## Commits
<details><summary><code>client.commits.<a href="src/fern/commits/client.py">create</a>(...) -> Commit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies one commit, which is an ordered, non-empty list of path operations that are committed together. The commit ID makes retries idempotent. The server checks the request's preconditions against the state before the commit, after it resolves any commit receipt and before it runs the operations. A failed precondition's position is reported in `details.precondition_index`. A request can contain a single operation. If an operation fails, the whole request fails, and for a request with more than one operation, `details.operation_index` reports the failed operation's position.
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
from fern import FernApi, FilesystemOperation_AppendFile

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.commits.create(
    namespace_id="namespace_id",
    commit_id="c_7kn71d9dq885x91hejz3gvf9p0",
    operations=[
        FilesystemOperation_AppendFile(
            inline_content="inline_content",
            path="/docs/report.txt",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**commit_id:** `CommitId` — The caller's idempotency key for the whole request.
    
</dd>
</dl>

<dl>
<dd>

**operations:** `typing.List[FilesystemOperation]` — The operations to commit atomically, in order. The list can't be empty.
    
</dd>
</dl>

<dl>
<dd>

**content_tokens:** `typing.Optional[typing.List[ContentToken]]` — One content token for each uploaded `content_ref` that the request uses.
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — An annotation from the caller. The message is part of the commit's identity.
    
</dd>
</dl>

<dl>
<dd>

**preconditions:** `typing.Optional[typing.List[CommitPrecondition]]` — The conditions that the server checks, in order, before it runs any operation.
    
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

## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py">content</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current file bytes, a retained revision, or the revision captured by an unexpired snapshot. A `Range` header asks for one byte range of the file instead.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.files.content(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The absolute path of the file to read.
    
</dd>
</dl>

<dl>
<dd>

**revision_no:** `typing.Optional[RevisionNo]` — An earlier revision to read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — The snapshot whose captured file revision to read.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` — One byte range of the file to read instead of the whole file, as `bytes=start-end`, where `end` is the offset of the last byte, or as `bytes=start-`. An `end` past the last byte reads to the end of the file. Any other value, including a suffix range or several ranges, returns 400 `invalid_request`.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">create_download</a>(...) -> CreateDownloadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns ordered, signed object ranges that cover exactly `[start_offset, size_bytes)` of the selected revision. Each range includes its signed headers in `access.headers`, and the client sends them unchanged. The client checks each range's length and the complete revision's checksum. To resume a download, a client asks for a new grant from its current offset. A deployment that can't presign URLs returns 501 `not_supported`. The proxied `GET /filesystem/content` route is still available, up to the `download.service_proxied.max_content_bytes` limit.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.files.create_download(
    namespace_id="namespace_id",
    path="/docs/report.txt",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**path:** `AbsolutePath` — The absolute path of the file to read.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency` set to `eventual`, how old the server's last confirmation of the head can
be, in milliseconds. The default is the server's `max_staleness_ms`.
    
</dd>
</dl>

<dl>
<dd>

**revision_no:** `typing.Optional[RevisionNo]` 

The revision to read. Omit it to read the path's current revision. It can't be combined with
`snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` 

A snapshot to read the file from. The download reads the revision that the snapshot
captured. It can't be combined with `revision_no`.
    
</dd>
</dl>

<dl>
<dd>

**start_offset:** `typing.Optional[int]` 

The first byte that the grant reads. The grant covers the revision's bytes from
`start_offset` up to `size_bytes`, so a client that resumes a download asks for a new grant
that starts after the bytes it already has. The offset must be less than the revision's
size. For a revision of zero bytes, it must be 0.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">list</a>(...) -> ListPathEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists a directory from the current state or an unexpired snapshot.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.files.list(
    namespace_id="namespace_id",
    path="path",
    snapshot_id="pin_00000000000000000001-0000000000000002",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The absolute path of the directory to list.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[bool]` 

Whether the response includes each entry's attribute map and attribute revision. The default
is `false`, because a page can have many entries and each map can be up to 64 KiB.
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `typing.Optional[bool]` 

Whether the listing includes the directory's whole subtree, depth first, with each
directory's entry before its descendants. The default is `false`, which lists the
directory's children only.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — The snapshot whose captured directory state to read.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">retrieve</a>(...) -> PathEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns path metadata from the current state or an unexpired snapshot.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.files.retrieve(
    namespace_id="namespace_id",
    path="path",
    snapshot_id="pin_00000000000000000001-0000000000000002",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The absolute path to read.
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[bool]` 

Whether the response includes the inode's attribute map and attribute revision. The default
is `true`, because a stat reads one path and a map is at most 64 KiB.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — The snapshot whose captured path state to read.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">list_revisions</a>(...) -> ListFileRevisionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolves the current path to a file inode and returns that file's revisions. If the file might be renamed, use the inode revisions route, which identifies the file by a stable ID.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.files.list_revisions(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The absolute path of the file.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">grep</a>(...) -> GrepResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches file content with a regular expression, using the namespace's grep index to narrow the candidates. The server checks each candidate against the full pattern and returns matches in ascending `(inode_id, byte_offset)` order. It scans every revision committed after the index watermark, unless `allow_stale` skips them. The deployment must serve grep, and the namespace must have a materialized, active grep index.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.files.grep(
    namespace_id="namespace_id",
    pattern="pattern",
    inode_id="ino_123",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**pattern:** `str` 

The search pattern, in the Rust `regex` crate's syntax. Its UTF-8 encoding must be at most
1024 bytes.
    
</dd>
</dl>

<dl>
<dd>

**case_insensitive:** `typing.Optional[bool]` — Whether matching ignores case. The default is `false`.
    
</dd>
</dl>

<dl>
<dd>

**path_prefix:** `typing.Optional[str]` 

A complete absolute path that limits matches to its descendants. It can't be combined with
`inode_id`.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `typing.Optional[str]` — An inode that limits matches to its descendants. It can't be combined with `path_prefix`.
    
</dd>
</dl>

<dl>
<dd>

**allow_scan:** `typing.Optional[bool]` 

Whether a pattern with no required literal bytes can use a capped exhaustive scan. The
default is `false`.
    
</dd>
</dl>

<dl>
<dd>

**allow_stale:** `typing.Optional[bool]` 

Whether the server returns results from the index alone when the unindexed tail exceeds the
scan budget. The default is `false`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of matches per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
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

## Trash
<details><summary><code>client.trash.<a href="src/fern/trash/client.py">list</a>(...) -> ListTrashResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the namespace's recoverable deletions, oldest first. A deletion leaves the list when it's undeleted, or when the namespace's writer expires it after the retention floor reaches its `deletion_seq`. Each entry includes the inode ID and deletion sequence that an undelete needs, and the directory binding that the delete removed.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.trash.list(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

## inodes
<details><summary><code>client.inodes.<a href="src/fern/inodes/client.py">retrieve</a>(...) -> PathEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the path entry for a visible inode, from the current state or an unexpired snapshot. An unknown or hidden inode returns `inode_not_found`.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.inodes.retrieve(
    namespace_id="namespace_id",
    inode_id="ino_123",
    snapshot_id="pin_00000000000000000001-0000000000000002",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `str` — The inode ID.
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[bool]` 

Whether the response includes the inode's attribute map and attribute revision. The default
is `true`, because a stat reads one path and a map is at most 64 KiB.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — The snapshot whose captured path state to read.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

<details><summary><code>client.inodes.<a href="src/fern/inodes/client.py">list_children</a>(...) -> ListInodeChildrenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists one page of a directory's children, in canonical name key order, from the current state or an unexpired snapshot. The request identifies the directory by its inode ID, so a listing and its later pages stay on the same directory even if the directory is renamed or moved at the same time.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.inodes.list_children(
    namespace_id="namespace_id",
    inode_id="ino_123",
    snapshot_id="pin_00000000000000000001-0000000000000002",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `str` — The directory's inode ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[bool]` 

Whether the response includes each entry's attribute map and attribute revision. The default
is `false`, because a page can have many entries and each map can be up to 64 KiB.
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `typing.Optional[bool]` 

Whether the listing includes the directory's whole subtree, depth first, with each
directory's entry before its descendants. The default is `false`, which lists the
directory's children only.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — The snapshot whose captured directory state to read.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

<details><summary><code>client.inodes.<a href="src/fern/inodes/client.py">content</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reads and verifies the current revision of a visible file inode, wherever the inode is bound, or the revision that an unexpired snapshot captured. A `Range` header asks for one byte range of the file instead. An unknown or hidden inode returns `inode_not_found`.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.inodes.content(
    namespace_id="namespace_id",
    inode_id="inode_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `str` — The file's inode ID.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` — The snapshot whose captured file revision to read.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` — One byte range of the file to read instead of the whole file, as `bytes=start-end`, where `end` is the offset of the last byte, or as `bytes=start-`. An `end` past the last byte reads to the end of the file. Any other value, including a suffix range or several ranges, returns 400 `invalid_request`.
    
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

<details><summary><code>client.inodes.<a href="src/fern/inodes/client.py">create_download</a>(...) -> CreateDownloadByInodeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authorizes a direct read of the current revision of a visible file inode, wherever the inode is bound, or of the revision that an unexpired snapshot captured. The capability reads exactly `[start_offset, size_bytes)`, as on the path route. The response doesn't include a path.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.inodes.create_download(
    namespace_id="namespace_id",
    inode_id="ino_123",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `str` — The file's inode ID.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read. It can't be combined with `snapshot_id`.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency` set to `eventual`, how old the server's last confirmation of the head can
be, in milliseconds. The default is the server's `max_staleness_ms`.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[PinId]` 

A snapshot to read the file from. The download reads the revision that the snapshot
captured.
    
</dd>
</dl>

<dl>
<dd>

**start_offset:** `typing.Optional[int]` 

The first byte that the grant reads. It defaults to 0 and must be less than the file's size.
For a file of zero bytes, it must be 0.
    
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

<details><summary><code>client.inodes.<a href="src/fern/inodes/client.py">list_revisions</a>(...) -> ListFileRevisionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the retained revisions of a file inode. The file doesn't need a current path.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.inodes.list_revisions(
    namespace_id="namespace_id",
    inode_id="ino_123",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `str` — The file's inode ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head. `eventual` (the default, unless the
server's `consistency` setting is `strong`) reads at the head that the server confirmed last
while that confirmation is younger than the maximum staleness, and `strong` confirms the
head before the read.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
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

<details><summary><code>client.inodes.<a href="src/fern/inodes/client.py">revision_content</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reads and verifies one retained file revision by inode ID and revision number. A `Range` header asks for one byte range of the revision instead.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.inodes.revision_content(
    namespace_id="namespace_id",
    inode_id="inode_id",
    revision_no=1000000,
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `str` — The file's inode ID.
    
</dd>
</dl>

<dl>
<dd>

**revision_no:** `RevisionNo` — The revision number.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head that it finds the revision in. `eventual`
(the default, unless the server's `consistency` setting is `strong`) reads at the head that
the server confirmed last while that confirmation is younger than the maximum staleness, and
`strong` confirms the head before the read.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency=eventual`, how old the server's last confirmation of the head can be, in
milliseconds. The default is the server's `max_staleness_ms`.
    
</dd>
</dl>

<dl>
<dd>

**range:** `typing.Optional[str]` — One byte range of the file to read instead of the whole file, as `bytes=start-end`, where `end` is the offset of the last byte, or as `bytes=start-`. An `end` past the last byte reads to the end of the file. Any other value, including a suffix range or several ranges, returns 400 `invalid_request`.
    
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

<details><summary><code>client.inodes.<a href="src/fern/inodes/client.py">create_revision_download</a>(...) -> CreateDownloadByInodeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authorizes a direct read of one retained inode revision. The capability reads exactly `[start_offset, size_bytes)`, as on the path route. The response doesn't include a path.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.inodes.create_revision_download(
    namespace_id="namespace_id",
    inode_id="ino_123",
    revision_no=1000000,
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**inode_id:** `str` — The file's inode ID.
    
</dd>
</dl>

<dl>
<dd>

**revision_no:** `RevisionNo` — The revision number.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[ReadConsistency]` 

How recently the read confirms the namespace head that it finds the revision in. `eventual`
(the default, unless the server's `consistency` setting is `strong`) reads at the head that
the server confirmed last while that confirmation is younger than the maximum staleness,
and `strong` confirms the head before the read.
    
</dd>
</dl>

<dl>
<dd>

**max_staleness_ms:** `typing.Optional[int]` 

With `consistency` set to `eventual`, how old the server's last confirmation of the head can
be, in milliseconds. The default is the server's `max_staleness_ms`.
    
</dd>
</dl>

<dl>
<dd>

**start_offset:** `typing.Optional[int]` 

The first byte that the grant reads. It defaults to 0 and must be less than the revision's
size. For a revision of zero bytes, it must be 0.
    
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

## Snapshots
<details><summary><code>client.snapshots.<a href="src/fern/snapshots/client.py">list</a>(...) -> ListSnapshotsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists snapshots in snapshot ID order. An expired snapshot stays in the list until garbage collection deletes it, after its expiry plus the grace window. The list leaves out fork pins, which the maintenance checkpoint inventory lists.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.snapshots.list(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
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

<details><summary><code>client.snapshots.<a href="src/fern/snapshots/client.py">create</a>(...) -> Snapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a snapshot of the current namespace state. The server first folds any WAL tail after the current manifest. Every accepted call creates a new snapshot with a new ID, and the name is a label, not a key. A snapshot with `ttl_ms` expires that many milliseconds from the server's current time, and a snapshot without it doesn't expire. The snapshot keeps its manifest until it's deleted, either explicitly or by garbage collection after it expires and its grace window passes.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.snapshots.create(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The snapshot's label, which doesn't need to be unique.
    
</dd>
</dl>

<dl>
<dd>

**ttl_ms:** `typing.Optional[int]` 

The snapshot's lifetime in milliseconds, counted from the server's current time. Omit it to
keep the snapshot until it's deleted.
    
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

<details><summary><code>client.snapshots.<a href="src/fern/snapshots/client.py">retrieve</a>(...) -> Snapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one snapshot, as the snapshot listing returns it, including an expired snapshot that garbage collection hasn't deleted. A missing ID, or the ID of a fork pin, returns `snapshot_not_found`.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.snapshots.retrieve(
    namespace_id="namespace_id",
    snapshot_id="pin_00000000000000000001-0000000000000002",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `PinId` — The snapshot ID.
    
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

<details><summary><code>client.snapshots.<a href="src/fern/snapshots/client.py">delete</a>(...) -> DeleteSnapshotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a snapshot. Garbage collection can then reclaim its unreferenced manifest and runs. Deleting a missing snapshot succeeds, so repeating the request has the same result. The ID of a fork pin returns `snapshot_not_found`. Deletion stays available after the namespace is deleted.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.snapshots.delete(
    namespace_id="namespace_id",
    snapshot_id="pin_00000000000000000001-0000000000000002",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `PinId` — The snapshot ID.
    
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

<details><summary><code>client.snapshots.<a href="src/fern/snapshots/client.py">extend</a>(...) -> Snapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Moves an unexpired snapshot's expiry to `ttl_ms` from the server's current time. The expiry never moves earlier, so a snapshot without an expiry is returned unchanged. A missing or expired snapshot returns `snapshot_not_found`. Repeating the request has the same result.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.snapshots.extend(
    namespace_id="namespace_id",
    snapshot_id="pin_00000000000000000001-0000000000000002",
    ttl_ms=1000000,
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `PinId` — The snapshot ID.
    
</dd>
</dl>

<dl>
<dd>

**ttl_ms:** `int` — The new lifetime in milliseconds, counted from the server's current time.
    
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

## uploads
<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">create</a>(...) -> UploadSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts an upload session for content that a later commit can reference. A service-proxied upload sends the bytes through the server, and a direct PUT upload returns a presigned upload capability.
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
from fern import FernApi, CreateUploadBody_DirectMultipart

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.uploads.create(
    namespace_id="namespace_id",
    request=CreateUploadBody_DirectMultipart(),
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateUploadBody` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">retrieve</a>(...) -> UploadSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an upload session. An open `direct_put` session includes a newly signed upload capability. A completed session includes a new content token, so the client can retry the commit without uploading the content again.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.uploads.retrieve(
    namespace_id="namespace_id",
    upload_id="upload_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload session ID.
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">abort</a>(...) -> UploadSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aborts an open upload session and deletes the object that the session was writing. Repeating the request succeeds, but a completed session can't be aborted.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.uploads.abort(
    namespace_id="namespace_id",
    upload_id="upload_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload session ID.
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">complete</a>(...) -> UploadSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes an upload. The request mode must match the mode that started the session. A direct upload includes a content claim, and a multipart upload also includes the completed parts.
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
from fern import FernApi, CompleteUploadBody_DirectMultipart, UploadContentClaim, Checksum, CompletedUploadPart

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.uploads.complete(
    namespace_id="namespace_id",
    upload_id="upload_id",
    request=CompleteUploadBody_DirectMultipart(
        content=UploadContentClaim(
            checksum=Checksum(
                algorithm="crc64nvme",
                value="value",
            ),
            size_bytes=1000000,
        ),
        parts=[
            CompletedUploadPart(
                checksum=Checksum(
                    algorithm="crc64nvme",
                    value="value",
                ),
                etag="etag",
                part_number=1,
            )
        ],
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload session ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CompleteUploadBody` 
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">put_content</a>(...) -> UploadSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads bytes into a service-proxied upload session and returns the open session with the staged content reference.
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
client.uploads.put_content(...)
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload session ID.
    
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

<details><summary><code>client.uploads.<a href="src/fern/uploads/client.py">sign_parts</a>(...) -> SignUploadPartsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one short-lived upload capability for each requested part of an open `direct_multipart` session. Each capability is bound to the part's checksum. To retry a part, a client asks for its capability again.
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
from fern import FernApi, UploadPartChecksumClaim, Checksum

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.uploads.sign_parts(
    namespace_id="namespace_id",
    upload_id="upload_id",
    parts=[
        UploadPartChecksumClaim(
            checksum=Checksum(
                algorithm="crc64nvme",
                value="value",
            ),
            part_number=1,
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload session ID.
    
</dd>
</dl>

<dl>
<dd>

**parts:** `typing.List[UploadPartChecksumClaim]` — The parts to authorize. A repeated part number replaces the earlier upload of that part.
    
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

## Maintenance Checkpoints
<details><summary><code>client.maintenance.checkpoints.<a href="src/fern/maintenance/checkpoints/client.py">list</a>(...) -> ListCheckpointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists every pin, snapshots and fork pins, in checkpoint ID order. This is the inventory of what keeps manifests from garbage collection. An expired snapshot stays in the list until garbage collection deletes it, after its expiry plus the grace window. A cursor continues the listing against the current set of pins.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.checkpoints.list(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum page size.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The opaque cursor that the previous page returned.
    
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

<details><summary><code>client.maintenance.checkpoints.<a href="src/fern/maintenance/checkpoints/client.py">retrieve</a>(...) -> Checkpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one existing pin, as the checkpoint listing returns it, including an expired snapshot that garbage collection hasn't deleted. A missing ID returns `snapshot_not_found`.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.checkpoints.retrieve(
    namespace_id="namespace_id",
    checkpoint_id="checkpoint_id",
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**checkpoint_id:** `str` — The checkpoint ID.
    
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

## Maintenance Diagnostics
<details><summary><code>client.maintenance.diagnostics.<a href="src/fern/maintenance/diagnostics/client.py">retrieve</a>(...) -> NamespaceDiagnostics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns namespace state together with the current manifest and visible WAL tail.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.diagnostics.retrieve(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
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

## Maintenance GrepIndex
<details><summary><code>client.maintenance.grep_index.<a href="src/fern/maintenance/grep_index/client.py">retrieve</a>(...) -> GrepIndex</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reports whether the namespace's grep index is `disabled`, `backfilling`, or `active`, with build progress when it's available. A namespace that has never enabled the index is `disabled`. A deployment that doesn't maintain grep indexes returns `not_supported`, and this operation doesn't change the index.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.grep_index.retrieve(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
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

<details><summary><code>client.maintenance.grep_index.<a href="src/fern/maintenance/grep_index/client.py">disable</a>(...) -> GrepIndex</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the namespace's grep index by publishing a manifest with the next number and no segment references. Index maintenance stops when a step reads the disabled manifest, and an explicit grep garbage collection run reclaims the segments later. Repeating the request has the same result. A deployment that doesn't maintain the grep index returns `not_supported`.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.grep_index.disable(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
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

<details><summary><code>client.maintenance.grep_index.<a href="src/fern/maintenance/grep_index/client.py">enable</a>(...) -> GrepIndex</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables the namespace's grep index. A deployment that runs maintenance starts the backfill on its next session tick and continues until the index is active. The response reports the index state read after the change. A new enable reports `backfilling`, with the sequence that its checkpoint captured, and an index that was already enabled reports its current status. Repeating the request has the same result. A deployment that doesn't maintain the grep index returns `not_supported`.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.grep_index.enable(
    namespace_id="namespace_id",
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

**namespace_id:** `str` — The namespace ID.
    
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

## Maintenance Runs
<details><summary><code>client.maintenance.runs.<a href="src/fern/maintenance/runs/client.py">create</a>(...) -> RunMaintenanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs one maintenance job for the namespace. The body's `kind` selects the job, which is one of `metadata`, `gc`, `retention`, `retention_window`, or `recover_administrator`. The response includes the same `kind` and the job's result. A deleted namespace accepts only `gc`. A `metadata` job folds the WAL tail and compacts metadata until nothing is due, or until it publishes 16 compaction units. A compaction unit can take minutes, so the call can too. When the result's `outcome` is `due`, another `metadata` run continues the work. A `gc` job reads the current manifest, lists the pins, and then sweeps every object family to the end. Each listing starts at the beginning, and the job doesn't keep a position to continue from. When the deployment maintains a grep index, the job then deletes aged, unreferenced grep index objects, and the result includes their counts in `extensions.grep`. A `retention` job advances the retention floor to the folded manifest head, or to the one target that `to_seq` or `cutoff_at_ms` sets. A `retention_window` job sets the namespace's retention window to `retention_window_ms`, or clears it when the body doesn't include that field.
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
from fern import FernApi, RunMaintenanceRequest_Gc

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.runs.create(
    namespace_id="namespace_id",
    request=RunMaintenanceRequest_Gc(),
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

**namespace_id:** `str` — The namespace ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `RunMaintenanceRequest` 
    
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

## Maintenance Store
<details><summary><code>client.maintenance.store.<a href="src/fern/maintenance/store/client.py">probe</a>(...) -> StoreProbeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks that the configured object store supports the create-if-absent, compare-and-swap, visibility, listing, and ranged-read behavior that LoonFS depends on, and reports the result of each check. The probe runs only when a client calls this route, because it writes and deletes objects. It writes them all under a scratch prefix that isn't a durable object family, and its last check deletes them and confirms that the prefix is empty. If the store fails a check, the response is still 200, and it reports that check as `failed`. If the store declares that it doesn't support an optional capability, the response reports that check as `unsupported`, which isn't a failure. The probe doesn't control whether the deployment can serve presigned direct uploads. The endpoint allowlist controls that, because the probe tests only the server's own requests and never a presigned capability issued to a client.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.maintenance.store.probe(
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

**request:** `StoreProbeRequest` 
    
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

