# Reference
## Workspace
<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">api_ocs_find_all</a>(...) -> WorkspaceApiOcsFindAllResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace.api_ocs_find_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional filter to return workspaces by name
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional limit of workspaces per page
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">api_ocs_create</a>(...) -> WorkspaceApiOcsCreateResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace.api_ocs_create(
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

**name:** `str` — Workspace name
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">api_ocs_find</a>(...) -> WorkspaceApiOcsFindResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace.api_ocs_find(
    id=1000000,
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

**id:** `int` — Represents the ID of a workspace
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">api_ocs_delete</a>(...)</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace.api_ocs_delete(
    id=1000000,
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

**id:** `int` — of a workspace to delete
    
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">api_ocs_edit</a>(...) -> WorkspaceApiOcsEditResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace.api_ocs_edit(
    id=1000000,
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

**id:** `int` — Represents the ID of a workspace
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional - Workspace name.
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Optional - Workspace color in hexadecimal format (example: #f91616).
    
</dd>
</dl>

<dl>
<dd>

**quota:** `typing.Optional[int]` — Optional - Workspace quota in bytes; e.g., 5368709120 for 5GB, or -3 for unlimited.
    
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

## WorkspaceUsers
<details><summary><code>client.workspace_users.<a href="src/fern/workspace_users/client.py">workspace_api_ocs_find_users_by_id</a>(...) -> WorkspaceApiOcsFindUsersByIdResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_users.workspace_api_ocs_find_users_by_id(
    id=1000000,
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

**id:** `int` — Represents the ID of the workspace
    
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

<details><summary><code>client.workspace_users.<a href="src/fern/workspace_users/client.py">workspace_api_ocs_add_users_in_workspace</a>(...) -> WorkspaceApiOcsAddUsersInWorkspaceResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_users.workspace_api_ocs_add_users_in_workspace(
    id=1000000,
    uids=[
        "uids"
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

**id:** `int` — Represents the ID of the workspace
    
</dd>
</dl>

<dl>
<dd>

**uids:** `typing.List[str]` — Represents the user uids to add to the workspace
    
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

<details><summary><code>client.workspace_users.<a href="src/fern/workspace_users/client.py">workspace_api_ocs_remove_users_in_workspace</a>(...)</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_users.workspace_api_ocs_remove_users_in_workspace(
    id=1000000,
    uids_array=[
        "uids[]"
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

**id:** `int` — Represents the ID of the workspace
    
</dd>
</dl>

<dl>
<dd>

**uids_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Represents the user uids to remove to the workspace
    
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

<details><summary><code>client.workspace_users.<a href="src/fern/workspace_users/client.py">workspace_api_ocs_add_user_as_workspace_manager</a>(...) -> WorkspaceApiOcsAddUserAsWorkspaceManagerResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_users.workspace_api_ocs_add_user_as_workspace_manager(
    id=1000000,
    uid="uid",
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

**id:** `int` — Represents the ID of the workspace
    
</dd>
</dl>

<dl>
<dd>

**uid:** `str` — Represents the user uid to add as a workspace manager
    
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

<details><summary><code>client.workspace_users.<a href="src/fern/workspace_users/client.py">workspace_api_ocs_remove_user_as_workspace_manager</a>(...)</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_users.workspace_api_ocs_remove_user_as_workspace_manager(
    id=1000000,
    uid="uid",
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

**id:** `int` — Represents the ID of the workspace
    
</dd>
</dl>

<dl>
<dd>

**uid:** `str` — Represents the user uid to remove as a workspace manager
    
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

<details><summary><code>client.workspace_users.<a href="src/fern/workspace_users/client.py">workspace_api_ocs_add_users_to_group</a>(...) -> WorkspaceApiOcsAddUsersToGroupResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_users.workspace_api_ocs_add_users_to_group(
    id=1000000,
    gid="gid",
    uids=[
        "uids"
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

**id:** `int` — Represents the ID of the workspace
    
</dd>
</dl>

<dl>
<dd>

**gid:** `str` — The subgroup id
    
</dd>
</dl>

<dl>
<dd>

**uids:** `typing.List[str]` — Represents the user uids to add to the subgroup
    
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

<details><summary><code>client.workspace_users.<a href="src/fern/workspace_users/client.py">workspace_api_ocs_remove_users_from_group</a>(...)</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_users.workspace_api_ocs_remove_users_from_group(
    id=1000000,
    gid="gid",
    uids_array=[
        "uids[]"
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

**id:** `int` — Represents the ID of the workspace
    
</dd>
</dl>

<dl>
<dd>

**gid:** `str` — The subgroup id
    
</dd>
</dl>

<dl>
<dd>

**uids_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Represents the user uids to remove from the subgroup
    
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

## WorkspaceGroups
<details><summary><code>client.workspace_groups.<a href="src/fern/workspace_groups/client.py">workspace_api_ocs_find_groups_by_space_id</a>(...) -> WorkspaceApiOcsFindGroupsBySpaceIdResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_groups.workspace_api_ocs_find_groups_by_space_id(
    id=1000000,
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

**id:** `int` — Represents the ID of the workspace
    
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

<details><summary><code>client.workspace_groups.<a href="src/fern/workspace_groups/client.py">workspace_api_ocs_create_sub_group</a>(...) -> WorkspaceApiOcsCreateSubGroupResponse</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_groups.workspace_api_ocs_create_sub_group(
    id=1000000,
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

**id:** `int` — Represents the ID of the workspace
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The subgroup name
    
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

<details><summary><code>client.workspace_groups.<a href="src/fern/workspace_groups/client.py">workspace_api_ocs_remove_group</a>(...)</code></summary>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspace_groups.workspace_api_ocs_remove_group(
    id=1000000,
    gid="gid",
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

**id:** `int` — Id of the workspace
    
</dd>
</dl>

<dl>
<dd>

**gid:** `str` — id of the subgroup to delete
    
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

