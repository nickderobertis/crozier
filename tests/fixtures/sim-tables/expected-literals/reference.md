# Reference
## Tables
<details><summary><code>client.tables.<a href="src/fern/tables/client.py">list_tables</a>(...) -> V2TableListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List active tables with folder filtering, search, sorting, and cursor pagination. Use `scope=archived` to find tables available for restoration. Workspace folder trees exceeding 10,000 folders return `413`.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.list_tables(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — Workspace whose tables should be listed.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[ListTablesRequestScope]` — Which lifecycle set to list: `active` (default) for live tables, `archived` for tables a delete archived and a table restore can bring back. `folderPath` resolves against active folders only, so pairing it with `scope=archived` returns an empty page when the containing folder was archived too.
    
</dd>
</dl>

<dl>
<dd>

**folder_path:** `typing.Optional[FolderPathInput]` — Restrict results to tables in this folder. Unknown folder paths contribute no matches.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Case-insensitive substring match against the resource name.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListTablesRequestSortBy]` — Field used to sort the result. Sorting by `name` is case-sensitive and follows the storage collation, so do not rely on a case-insensitive order.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListTablesRequestSortOrder]` — Sort direction.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum tables to return per page. Values outside 1–1000 are truncated and clamped into that range rather than rejected. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_table</a>(...) -> V2CreateTableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a table with a typed column schema and optional folder placement.

OAuth scope: `api:write`.
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
from fern.tables import CreateTableRequestSchema, CreateTableRequestSchemaColumnsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_table(
    name="name",
    workspace_id="workspaceId",
    schema=CreateTableRequestSchema(
        columns=[
            CreateTableRequestSchemaColumnsItem(
                name="name",
                type="string",
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

**name:** `str` — Table name.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `CreateTableRequestSchema` — Initial table column definitions.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional table description.
    
</dd>
</dl>

<dl>
<dd>

**folder_path:** `typing.Optional[FolderPathInput]` — Folder in which to create the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">get_table</a>(...) -> V2TableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a table with its metadata, column schema, locks, and current job. Workspace folder trees exceeding 10,000 folders return `413`.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.get_table(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">delete_table</a>(...) -> V2DeleteTableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive a table while retaining its rows. Use List Tables with `scope=archived` to find it and Restore Table to recover it.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.delete_table(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">update_table</a>(...) -> V2UpdateTableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename a table, edit its description, or move it to a folder. Fields are saved independently: a failed request may leave partial changes. `error.details.applied` lists saved fields; retry only the remaining fields. If absent, nothing changed. Lock flags are read-only. Workspace folder trees exceeding 10,000 folders return `413`.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.update_table(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Replacement table name.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Replacement table description, or null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**folder_path:** `typing.Optional[FolderPathInput]` 
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">add_table_column</a>(...) -> V2TableColumnsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a typed column and return the complete resulting table schema.

OAuth scope: `api:write`.
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
from fern.tables import AddTableColumnRequestColumn

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.add_table_column(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    column=AddTableColumnRequestColumn(
        name="plan",
        type="string",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
</dd>
</dl>

<dl>
<dd>

**column:** `AddTableColumnRequestColumn` — Column definition to add.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">delete_table_column</a>(...) -> V2TableColumnsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a column by name while preserving at least one table column.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.delete_table_column(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    column_name="legacyStatus",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**column_name:** `str` — Name of the column to delete.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">update_table_column</a>(...) -> V2TableColumnsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a column by name and return the complete resulting table schema.

OAuth scope: `api:write`.
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
from fern.tables import UpdateTableColumnRequestUpdates

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.update_table_column(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    column_name="plan",
    updates=UpdateTableColumnRequestUpdates(
        name="subscriptionPlan",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
</dd>
</dl>

<dl>
<dd>

**column_name:** `str` — Current name of the column to update.
    
</dd>
</dl>

<dl>
<dd>

**updates:** `UpdateTableColumnRequestUpdates` — Mutable column fields.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">list_table_rows</a>(...) -> V2TableRowListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List rows in default order with cursor pagination. Pages default to a 5 MB limit and may contain fewer rows than requested; continue until `nextCursor` is null. Use Query Rows for filtering and sorting. `includeRunState=true` adds per-group run outcomes and reduces the row limit.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.list_table_rows(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum rows to return per page. Must be a whole number from 1 to 1000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.
    
</dd>
</dl>

<dl>
<dd>

**include_run_state:** `typing.Optional[bool]` — Include per-workflow-group run state on every returned row. Off by default: run state is a separate sidecar read and its `blockErrors` are unbounded, so a full page carries it only when asked. Caps `limit` at 200.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_table_rows</a>(...) -> V2CreateTableRowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert one row with a data object or insert a bounded batch with a rows array. Cell keys are column names.

OAuth scope: `api:write`.
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
from fern import FernApi, CreateTableRowsRequestRows
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_table_rows(
    table_id="tableId",
    request=CreateTableRowsRequestRows(
        workspace_id="workspaceId",
        rows=[
            {
                "key": "value"
            }
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateTableRowsRequest` 
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">delete_table_rows</a>(...) -> V2DeleteTableRowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete rows by a non-empty predicate or an explicit bounded list of row identifiers.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.delete_table_rows(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    row_ids=[
        "row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93"
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TablePredicate]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum matching rows to delete.
    
</dd>
</dl>

<dl>
<dd>

**row_ids:** `typing.Optional[typing.List[str]]` — Explicit row identifiers to delete.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">update_table_rows</a>(...) -> V2UpdateTableRowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply the same partial data patch to every row matching a non-empty predicate.

OAuth scope: `api:write`.
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
from fern import FernApi, TablePredicateAll
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.update_table_rows(
    table_id="tableId",
    workspace_id="workspaceId",
    filter=TablePredicateAll(
        all_=[],
    ),
    data={
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `TablePredicate` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `V2TableRowData` — Row-data patch applied to every matching row.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum matching rows to update.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">get_table_row</a>(...) -> V2TableRowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one row by identifier. Set `includeRunState=true` to attach the row's per-workflow-group run outcomes.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.get_table_row(
    table_id="tableId",
    row_id="rowId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**row_id:** `str` — Unique table row identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
</dd>
</dl>

<dl>
<dd>

**include_run_state:** `typing.Optional[bool]` — Include per-workflow-group run state on the returned row. Off by default.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">delete_table_row</a>(...) -> V2DeleteTableRowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one row by identifier.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.delete_table_row(
    table_id="tableId",
    row_id="rowId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**row_id:** `str` — Unique table row identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">update_table_row</a>(...) -> V2TableRowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merge a partial data patch into one row by identifier.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.update_table_row(
    table_id="tableId",
    row_id="rowId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    data={
        "status": "active"
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**row_id:** `str` — Unique table row identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**data:** `V2TableRowData` — Partial row-data patch keyed by column name.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">upsert_table_row</a>(...) -> V2UpsertTableRowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a row or replace the row matching a selected unique column. On replacement, omitted columns are cleared; send the complete row. Use Update Row for a partial patch.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.upsert_table_row(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    data={
        "email": "jane@example.com",
        "status": "active"
    },
    conflict_target="email",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**data:** `V2TableRowData` — Complete set of row cells keyed by column name. On the update branch this REPLACES the matched row: any column not present here is cleared, unlike a single-row update, which merges.
    
</dd>
</dl>

<dl>
<dd>

**conflict_target:** `typing.Optional[str]` — Unique column used to detect a conflict.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">query_table_rows</a>(...) -> V2QueryTableRowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query rows with typed predicates, sorting, and cursor pagination. Omit the predicate to match all rows. Pages default to a 5 MB limit; continue until `nextCursor` is null. Oversized predicates return `413`. `includeRunState` adds per-group outcomes and reduces the row limit. Counts are read separately and can differ from paged results if rows change.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.query_table_rows(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**predicate:** `typing.Optional[TablePredicateInput]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.List[QueryTableRowsRequestSortItem]]` — Ordered table-row sort specification.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum rows to return; zero requests an unbounded result.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor returned by the previous query page.
    
</dd>
</dl>

<dl>
<dd>

**include_run_state:** `typing.Optional[bool]` — Include per-workflow-group run state on every returned row. Off by default: run state is a separate sidecar read and its `blockErrors` are unbounded, so a full page carries it only when asked. Incompatible with `limit: 0`, and caps `limit` at 200.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">count_table_rows</a>(...) -> V2CountTableRowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Count rows matching a typed predicate, or omit the predicate to count all rows. The count is read separately from row pages and can change between requests. Oversized predicates return `413`.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.count_table_rows(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**predicate:** `typing.Optional[TablePredicateInput]` 
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">list_table_views</a>(...) -> V2TableViewListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List saved table views, omitting references to removed columns. Returns the complete set in one page; `nextCursor` is always null.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.list_table_views(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_table_view</a>(...) -> V2CreateTableViewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save a filter, sort, and column layout as a named presentation of a table.

OAuth scope: `api:write`.
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
from fern.tables import CreateTableViewRequestConfig

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_table_view(
    table_id="tableId",
    workspace_id="workspaceId",
    name="name",
    config=CreateTableViewRequestConfig(),
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Saved-view display name.
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateTableViewRequestConfig` — Saved filter, sort, and column-layout configuration.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">get_table_view</a>(...) -> V2TableViewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one saved table view by identifier.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.get_table_view(
    table_id="tableId",
    view_id="viewId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**view_id:** `str` — Unique saved-view identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">delete_table_view</a>(...) -> V2DeleteTableViewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a saved presentation without changing any table rows.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.delete_table_view(
    table_id="tableId",
    view_id="viewId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**view_id:** `str` — Unique saved-view identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">update_table_view</a>(...) -> V2TableViewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename a view, replace or shallow-merge its configuration, or promote it to the table default.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.update_table_view(
    table_id="tableId",
    view_id="viewId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**view_id:** `str` — Unique saved-view identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Replacement saved-view display name.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[UpdateTableViewRequestConfig]` — Complete replacement saved-view configuration.
    
</dd>
</dl>

<dl>
<dd>

**config_patch:** `typing.Optional[UpdateTableViewRequestConfigPatch]` — Saved-view configuration fields to shallow-merge.
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` — Whether to promote this view to the table default.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">list_table_workflow_groups</a>(...) -> V2TableWorkflowGroupListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the workflow and enrichment groups that can be dispatched for a table. Returns the complete set in one page; `nextCursor` is always null.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.list_table_workflow_groups(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">add_table_workflow_group</a>(...) -> V2AddTableWorkflowGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bind a workflow or enrichment to the table and create the columns populated by its outputs.

OAuth scope: `api:write`.
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
from fern.tables import AddTableWorkflowGroupRequestGroup, AddTableWorkflowGroupRequestGroupOutputsItem, AddTableWorkflowGroupRequestOutputColumnsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.add_table_workflow_group(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    group=AddTableWorkflowGroupRequestGroup(
        workflow_id="3b1f7c92-8d4e-4a6b-9c0d-5e2f8a714b36",
        name="Enrich company",
        outputs=[
            AddTableWorkflowGroupRequestGroupOutputsItem(
                block_id="block_lookup",
                path="output.revenue",
                column_name="revenue",
            )
        ],
    ),
    output_columns=[
        AddTableWorkflowGroupRequestOutputColumnsItem(
            name="revenue",
            type="number",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**group:** `AddTableWorkflowGroupRequestGroup` — Workflow or enrichment producer definition.
    
</dd>
</dl>

<dl>
<dd>

**output_columns:** `typing.List[AddTableWorkflowGroupRequestOutputColumnsItem]` — Columns created for producer outputs.
    
</dd>
</dl>

<dl>
<dd>

**auto_run:** `typing.Optional[bool]` — Whether to schedule existing rows after group creation.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">delete_table_workflow_group</a>(...) -> V2DeleteTableWorkflowGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a workflow group and every table column populated by that group.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.delete_table_workflow_group(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    group_id="grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — Workflow group to delete.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">update_table_workflow_group</a>(...) -> V2UpdateTableWorkflowGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restructure a workflow group, its producer, outputs, or execution behavior. Repointing the group at a different workflow concurrently invalidates the resolved output types and returns `409` — retry the update.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.update_table_workflow_group(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    group_id="grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204",
    name="Company profile enrichment",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — Workflow group to update.
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` — Replacement backing workflow identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Replacement workflow-group display name.
    
</dd>
</dl>

<dl>
<dd>

**dependencies:** `typing.Optional[UpdateTableWorkflowGroupRequestDependencies]` — Replacement input dependencies.
    
</dd>
</dl>

<dl>
<dd>

**outputs:** `typing.Optional[typing.List[UpdateTableWorkflowGroupRequestOutputsItem]]` — Replacement producer outputs.
    
</dd>
</dl>

<dl>
<dd>

**new_output_columns:** `typing.Optional[typing.List[UpdateTableWorkflowGroupRequestNewOutputColumnsItem]]` — Columns to add for new outputs.
    
</dd>
</dl>

<dl>
<dd>

**mapping_updates:** `typing.Optional[typing.List[UpdateTableWorkflowGroupRequestMappingUpdatesItem]]` — Existing output-column mapping changes.
    
</dd>
</dl>

<dl>
<dd>

**input_mappings:** `typing.Optional[typing.List[UpdateTableWorkflowGroupRequestInputMappingsItem]]` — Replacement workflow input mappings.
    
</dd>
</dl>

<dl>
<dd>

**deployment_mode:** `typing.Optional[UpdateTableWorkflowGroupRequestDeploymentMode]` — Replacement workflow execution mode.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateTableWorkflowGroupRequestType]` — Workflow-group producer type. Must match the group's stored type — a group's producer cannot be changed after creation.
    
</dd>
</dl>

<dl>
<dd>

**auto_run:** `typing.Optional[bool]` — Replacement automatic-run setting.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">list_table_dispatches</a>(...) -> V2TableRunDispatchListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List in-flight run dispatches for a table in one page; `nextCursor` is always null. Use Get Run Dispatch to read a settled dispatch.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.list_table_dispatches(
    table_id="tableId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_table_dispatch</a>(...) -> V2CreateTableDispatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start workflow or enrichment groups across all rows or selected rows. Poll Get Run Dispatch until `complete` or `canceled`. A null `dispatchId` means no dispatch is available to poll; check row outcomes with `includeRunState`. Use Cancel Run Dispatch to stop further scheduling.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_table_dispatch(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    group_ids=[
        "grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204"
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**group_ids:** `typing.List[str]` — Workflow or enrichment groups to run.
    
</dd>
</dl>

<dl>
<dd>

**run_mode:** `typing.Optional[CreateTableDispatchRequestRunMode]` — Whether to run all or only incomplete cells.
    
</dd>
</dl>

<dl>
<dd>

**row_ids:** `typing.Optional[typing.List[str]]` — Explicit row subset to run.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TablePredicate]` 
    
</dd>
</dl>

<dl>
<dd>

**exclude_row_ids:** `typing.Optional[typing.List[str]]` — Rows excluded from a select-all run scope.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[CreateTableDispatchRequestLimit]` — Optional cap on eligible rows to run.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">get_row_enrichment</a>(...) -> V2RowEnrichmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an enrichment cell's provider attempts, statuses, hosted-key costs, durations, and matching provider. Null means no run detail was recorded; `404` means the table, row, or group does not exist.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.get_row_enrichment(
    table_id="tableId",
    row_id="rowId",
    group_id="groupId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**row_id:** `str` — Unique table row identifier.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — Workflow or enrichment group to run.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">run_row_enrichment</a>(...) -> V2RunRowEnrichmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start one workflow or enrichment group for a table row. Poll Get Run Dispatch using the returned `dispatchId`. A null `dispatchId` means no dispatch is available to poll; check row outcomes with `includeRunState`.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.run_row_enrichment(
    table_id="tableId",
    row_id="rowId",
    group_id="groupId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**row_id:** `str` — Unique table row identifier.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — Workflow or enrichment group to run.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">search_table_rows</a>(...) -> V2SearchTableRowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search cell text for a case-insensitive substring within an optional filtered and sorted view. Returns cell coordinates, not row data; `ordinal` matches the view used by Query Rows. Results are unpaginated and capped at 1000. If `truncated` is true, narrow the search or predicate.

OAuth scope: `api:read`.
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
from fern import FernApi, TablePredicateAll, TablePredicateAllAllItemField
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.search_table_rows(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    q="acme",
    predicate=TablePredicateAll(
        all_=[
            TablePredicateAllAllItemField(
                field="status",
                op="eq",
                value="active",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**q:** `str` — Case-insensitive cell substring to find.
    
</dd>
</dl>

<dl>
<dd>

**predicate:** `typing.Optional[TablePredicate]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.List[SearchTableRowsRequestSortItem]]` — Ordered table-row sort specification.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_table_import</a>(...) -> V2CreateTableImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a CSV import. Upload sources receive signed transfer instructions; workspace-file sources start processing directly.

OAuth scope: `api:write`.
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
from fern.tables import CreateTableImportRequestSource_Upload, CreateTableImportRequestTarget_New

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_table_import(
    workspace_id="workspaceId",
    source=CreateTableImportRequestSource_Upload(
        name="name",
        content_type="contentType",
        size=1,
        type="upload",
    ),
    target=CreateTableImportRequestTarget_New(
        name="name",
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

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**source:** `CreateTableImportRequestSource` — CSV source for the import.
    
</dd>
</dl>

<dl>
<dd>

**target:** `CreateTableImportRequestTarget` — New or existing table import target.
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — CSV headers mapped to existing table columns.
    
</dd>
</dl>

<dl>
<dd>

**create_columns:** `typing.Optional[typing.List[str]]` — CSV headers for which new columns should be created.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — IANA timezone used to interpret local date values.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">get_table_import</a>(...) -> V2TableImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an import's progress and status. During `uploading`, the signed upload token is required; omitting it returns `404`.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.get_table_import(
    import_id="importId",
    workspace_id="workspaceId",
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

**import_id:** `str` — Unique table-import identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
</dd>
</dl>

<dl>
<dd>

**upload_token:** `typing.Optional[str]` — Signed upload control token returned when an upload-backed import was created.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">cancel_table_import</a>(...) -> V2CancelTableImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel an upload or processing import. Committed row batches remain. Non-cancelable states, including `expired`, return `409`; unknown or purged imports return `404`.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.cancel_table_import(
    import_id="importId",
    workspace_id="workspaceId",
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

**import_id:** `str` — Unique table-import identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
</dd>
</dl>

<dl>
<dd>

**upload_token:** `typing.Optional[str]` — Signed upload control token returned when an upload-backed import was created.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_table_import_part_urls</a>(...) -> V2CreateTableImportPartUrlsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create signed URLs for multipart upload parts. Requires the `uploading` state; other states return `409`. Unknown or purged imports return `404`.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_table_import_part_urls(
    import_id="importId",
    workspace_id="workspaceId",
    upload_token="upload-token",
    part_numbers=[
        1,
        2,
        3
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

**import_id:** `str` — Unique table-import identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
</dd>
</dl>

<dl>
<dd>

**upload_token:** `str` — Signed upload control token returned when the upload session was created.
    
</dd>
</dl>

<dl>
<dd>

**part_numbers:** `typing.List[int]` — Multipart part numbers for which signed URLs should be created.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">complete_table_import_upload</a>(...) -> V2CompleteTableImportUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify or assemble uploaded CSV bytes and start processing under the same import ID. Requires an import awaiting upload completion; other states return `409`. Unknown or purged imports return `404`.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.complete_table_import_upload(
    import_id="importId",
    workspace_id="workspaceId",
    upload_token="upload-token",
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

**import_id:** `str` — Unique table-import identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
</dd>
</dl>

<dl>
<dd>

**upload_token:** `str` — Signed upload control token returned when the upload session was created.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_table_export</a>(...) -> V2CreateTableExportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a CSV or JSON export. Exports of small tables finish during the request; larger exports run asynchronously.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_table_export(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    format="csv",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CreateTableExportRequestFormat]` — Export file format.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">get_table_export</a>(...) -> V2TableExportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a table export's progress and status.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.get_table_export(
    table_id="tableId",
    export_id="exportId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**export_id:** `str` — Unique table-export identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">cancel_table_export</a>(...) -> V2CancelTableExportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel an export that is still in progress.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.cancel_table_export(
    table_id="tableId",
    export_id="exportId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**export_id:** `str` — Unique table-export identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">download_table_export</a>(...) -> V2DownloadTableExportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a short-lived signed download URL for a completed export. Other states return `409`; an unavailable export file returns `404`.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.download_table_export(
    table_id="tableId",
    export_id="exportId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**export_id:** `str` — Unique table-export identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">cancel_table_runs</a>(...) -> V2CancelTableRunsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop in-flight and pending workflow or enrichment cell runs across the table or one selected row.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.cancel_table_runs(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    scope="row",
    row_id="row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `CancelTableRunsRequestScope` — Whether to cancel across the table or one row.
    
</dd>
</dl>

<dl>
<dd>

**row_id:** `typing.Optional[str]` — Row whose runs should be canceled for row scope.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TablePredicate]` 
    
</dd>
</dl>

<dl>
<dd>

**exclude_row_ids:** `typing.Optional[typing.List[str]]` — Rows excluded from an all-scope cancellation.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">list_tables_folders</a>(...) -> V2TableFolderListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List table folders, optionally limiting results to direct children of a parent path. Returns the complete set in one page; `nextCursor` is always null.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.list_tables_folders(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — Workspace whose folders should be listed.
    
</dd>
</dl>

<dl>
<dd>

**parent_path:** `typing.Optional[FolderPathInput]` — Restrict results to direct children of this parent path. Unknown folder paths contribute no matches.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Case-insensitive substring match against the folder name.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListTablesFoldersRequestSortBy]` — Field used to sort the result. Sorting by `name` is case-sensitive and follows the storage collation, so do not rely on a case-insensitive order.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListTablesFoldersRequestSortOrder]` — Sort direction.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">create_tables_folder</a>(...) -> V2CreateTableFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one table-folder leaf whose parent path already exists.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.create_tables_folder(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — Workspace in which to create the folder.
    
</dd>
</dl>

<dl>
<dd>

**path:** `NonRootFolderPathInput` — Path of the folder to create.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">delete_tables_folder</a>(...) -> V2DeleteTableFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive an empty folder, or set `recursive=true` to archive its tables and subfolders. Use Restore Folder to recover the archived contents.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.delete_tables_folder(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — Workspace containing the folder.
    
</dd>
</dl>

<dl>
<dd>

**path:** `NonRootFolderPathInput` — Path of the folder to delete.
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `typing.Optional[DeleteTablesFolderRequestRecursive]` — Delete the folder's nested files and folders too. An empty folder deletes either way; a non-empty one needs this. The listed spellings are the whole accepted vocabulary and are case-sensitive; any other value is rejected.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">relocate_tables_folder</a>(...) -> V2RelocateTableFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename or move a table folder and update all descendant paths.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.relocate_tables_folder(
    workspace_id="workspaceId",
    path="path",
    destination_path="destinationPath",
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

**workspace_id:** `str` — Workspace containing the folder.
    
</dd>
</dl>

<dl>
<dd>

**path:** `NonRootFolderPathInput` — Current folder path.
    
</dd>
</dl>

<dl>
<dd>

**destination_path:** `NonRootFolderPathInput` — New full path for the folder and its descendants.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">restore_tables_folder</a>(...) -> V2RestoreTableFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore an archived table folder, its descendants, and tables using its former path. An archived parent moves it to the root; name conflicts may change the returned `path`. Non-archived paths return `404`. Save the path from Delete Folder, because List Folders does not include archived table folders.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.restore_tables_folder(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — Workspace that owns the archived folder.
    
</dd>
</dl>

<dl>
<dd>

**path:** `NonRootFolderPathInput` — Path the folder held when a folder delete archived it.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">restore_table</a>(...) -> V2RestoreTableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore a table and its archived rows, views, and workflow groups. Active tables return unchanged without a new audit event. Name conflicts may change the returned `name`. Find archived tables with List Tables and `scope=archived`.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.restore_table(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Unique workspace identifier.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">bulk_update_table_rows</a>(...) -> V2BulkUpdateTableRowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply separate partial patches to up to 1,000 rows, preserving omitted columns. A row outside the table rejects the entire request with `400` and lists missing IDs. Use Update Rows by Filter to apply one patch to every matching row.

OAuth scope: `api:write`.
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
from fern.tables import BulkUpdateTableRowsRequestUpdatesItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.bulk_update_table_rows(
    table_id="tableId",
    workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
    updates=[
        BulkUpdateTableRowsRequestUpdatesItem(
            row_id="row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93",
            data={
                "status": "active"
            },
        ),
        BulkUpdateTableRowsRequestUpdatesItem(
            row_id="row_2b4d6f8a0c1e3759b8d0f2a4c6e80193",
            data={
                "status": "churned"
            },
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the table.
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.List[BulkUpdateTableRowsRequestUpdatesItem]` — One merge patch per row. Each row identifier may appear at most once.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">get_table_dispatch</a>(...) -> V2TableRunDispatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dispatch's current state. Poll until `complete` or `canceled`; use row reads with `includeRunState` for per-cell outcomes.

OAuth scope: `api:read`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.get_table_dispatch(
    table_id="tableId",
    dispatch_id="dispatchId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**dispatch_id:** `str` — Unique table run-dispatch identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">cancel_table_dispatch</a>(...) -> V2CancelTableDispatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop a dispatch from scheduling more cells. Already queued or running cells continue; use Cancel Column Runs to stop them. Completed or canceled dispatches return unchanged.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.cancel_table_dispatch(
    table_id="tableId",
    dispatch_id="dispatchId",
    workspace_id="workspaceId",
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

**table_id:** `str` — Unique table identifier.
    
</dd>
</dl>

<dl>
<dd>

**dispatch_id:** `str` — Unique table run-dispatch identifier.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace that owns the transfer resource.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">move_tables</a>(...) -> V2MoveTablesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move up to 100 tables and folders to one destination. Items succeed or fail independently: covered tables are `skipped`, missing items are `notFound`, and lock or cycle failures include reasons in `failed`. An invalid destination rejects the request before any move.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.move_tables(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — Workspace that owns every selected item.
    
</dd>
</dl>

<dl>
<dd>

**table_ids:** `typing.Optional[typing.List[str]]` — Tables to move, by identifier.
    
</dd>
</dl>

<dl>
<dd>

**folder_paths:** `typing.Optional[typing.List[FolderPathInput]]` — Table folders to re-parent, by canonical path.
    
</dd>
</dl>

<dl>
<dd>

**target_folder_path:** `typing.Optional[FolderPathInput]` — Destination folder path. Omit to move the selection to the workspace root.
    
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

<details><summary><code>client.tables.<a href="src/fern/tables/client.py">bulk_delete_tables</a>(...) -> V2BulkDeleteTablesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive up to 100 selected tables and folders, including folder contents. Items succeed or fail independently, with `skipped`, `notFound`, and `failed` outcomes. `deletedItems` includes all descendants. Use Restore Table or Restore Folder to recover archived items.

OAuth scope: `api:write`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.tables.bulk_delete_tables(
    workspace_id="workspaceId",
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

**workspace_id:** `str` — Workspace that owns every selected item.
    
</dd>
</dl>

<dl>
<dd>

**table_ids:** `typing.Optional[typing.List[str]]` — Tables to archive, by identifier.
    
</dd>
</dl>

<dl>
<dd>

**folder_paths:** `typing.Optional[typing.List[FolderPathInput]]` — Table folders to delete, by canonical path. Each cascades to everything inside it.
    
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

