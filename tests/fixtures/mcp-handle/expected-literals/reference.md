# Reference
## McpServer
<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">call_server_tool</a>(...) -> CallToolResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calls a tool on a specific remote MCP server, used for function calling. Eliminates the need for manual MCP code implementation.
Under the hood, MCP Handle will instantiates an MCP client and establishes a connection with the remote MCP server to call the tool.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.call_server_tool(
    server_url="serverUrl",
    tool_name="toolName",
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

**server_url:** `str` — The full URL for connecting to the MCP server
    
</dd>
</dl>

<dl>
<dd>

**tool_name:** `str` — The name of the tool to call
    
</dd>
</dl>

<dl>
<dd>

**tool_args:** `typing.Optional[typing.Dict[str, typing.Any]]` — The input parameters for the tool
    
</dd>
</dl>

<dl>
<dd>

**connection_type:** `typing.Optional[ConnectionType]` — The connection type to use for the MCP server. Default is STREAMABLE_HTTP.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Optional HTTP headers to include when connecting to the server
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">list_server_tools</a>(...) -> ListToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all tools available for a specific remote MCP server in various AI model formats.

This eliminates the need for manual MCP code implementation and format conversion.
Under the hood, MCP Handle instantiates an MCP client and establishes a connection 
with the remote MCP server to retrieve available tools.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.list_server_tools(
    server_url="serverUrl",
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

**server_url:** `str` — The full URL for connecting to the MCP server
    
</dd>
</dl>

<dl>
<dd>

**connection_type:** `typing.Optional[ConnectionType]` — The connection type to use for the MCP server. Default is STREAMABLE_HTTP.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ToolFormat]` — The format to return tools in. Default is MCP Native format for maximum compatibility.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Optional HTTP headers to include when connecting to the server
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">create_strata_server</a>(...) -> StrataCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Strata MCP server.

Parameters:
- servers: Can be 'ALL' to add all available MCP Handle integration, a list of specific server names, or null to add no servers
- externalServers: Optional list of external MCP servers to validate and add
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.create_strata_server(
    user_id="userId",
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

**user_id:** `str` — The unique identifier for the user. The server instance along with the all the authentication data will belong to that specific user only. It can be a UUID from the database, a unique email address from the user, etc.
    
</dd>
</dl>

<dl>
<dd>

**servers:** `typing.Optional[StrataCreateRequestServers]` — List of MCP Handle MCP servers to enable (e.g., 'jira', 'linear'), 'ALL' to add all MCP Handle MCP servers, or null to add no servers.
    
</dd>
</dl>

<dl>
<dd>

**external_servers:** `typing.Optional[typing.List[ExternalServerRequest]]` — Optional list of external MCP servers to add with their URLs. Each server will be validated before being added.
    
</dd>
</dl>

<dl>
<dd>

**enable_auth_handling:** `typing.Optional[bool]` — Whether to enable authentication handling. Default is True.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">add_servers_to_strata</a>(...) -> StrataAddServersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add servers to an existing Strata MCP server.

Note: After adding servers, you need to reconnect the MCP server so that list_tool can be updated with the new servers.

Parameters:
- servers: Can be 'ALL' to add all available servers, a list of specific server names, or null to add no servers
- externalServers: Optional list of external MCP servers to validate and add
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.add_servers_to_strata(
    strata_id="strataId",
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

**strata_id:** `str` — The strata server ID
    
</dd>
</dl>

<dl>
<dd>

**servers:** `typing.Optional[StrataAddServersRequestServers]` — List of MCP Handle integration to add (e.g., 'jira', 'linear'), 'ALL' to add all MCP Handle integration, or null to add no servers.
    
</dd>
</dl>

<dl>
<dd>

**external_servers:** `typing.Optional[typing.List[ExternalServerRequest]]` — Optional list of external MCP servers to add with their URLs. Each server will be validated before being added.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">delete_servers_from_strata</a>(...) -> StrataDeleteServersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete servers from an existing Strata MCP server.

Note: After deleting servers, you need to reconnect the MCP server so that list_tool can be updated to reflect the removed servers.

Parameters:
- strataId: The strata server ID (path parameter)
- servers: Can be 'ALL' to delete all available MCP Handle integration, a list of specific server names, or null to delete no servers
- externalServers: Query parameter - comma-separated list of external server names to delete

Returns separate lists for deleted MCP Handle servers and deleted external servers.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.delete_servers_from_strata(
    strata_id="strataId",
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

**strata_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**servers:** `typing.Optional[typing.List[DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItem]]` — List of MCP Handle integration to delete (e.g., 'jira', 'linear'), 'ALL' to delete all MCP Handle integration, or null to delete no servers.
    
</dd>
</dl>

<dl>
<dd>

**external_servers:** `typing.Optional[str]` — Comma-separated list of external server names to delete
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">get_strata_server</a>(...) -> StrataGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about an existing Strata MCP server instance.

Returns the strata URL, connected mcp_handle servers, connected external servers (with URLs), 
and authentication URLs for mcp_handle servers.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.get_strata_server(
    strata_id="strataId",
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

**strata_id:** `str` 
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">list_strata_raw_actions</a>(...) -> StrataRawActionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch raw actions (all underlying actions) for a specific integration within a Strata MCP instance.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.list_strata_raw_actions(
    strata_id="strataId",
    server="Affinity",
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

**strata_id:** `str` — The strata server ID
    
</dd>
</dl>

<dl>
<dd>

**server:** `McpServerName` — The name of the server to fetch raw actions for
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">get_strata_auth</a>(...) -> StrataGetAuthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves authentication data for a specific integration within a Strata MCP server.

Returns the authentication data if available, along with authentication status.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.get_strata_auth(
    strata_id="strataId",
    server_name="Affinity",
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

**strata_id:** `str` — The strata server ID
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `McpServerName` — The name of the MCP Handle MCP server to get authentication for (e.g., 'GitHub', 'Jira')
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">delete_strata_auth</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes authentication data for a specific integration within a Strata MCP server.

This will clear the stored authentication credentials, effectively unauthenticating the server.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.delete_strata_auth(
    strata_id="strataId",
    server_name="Affinity",
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

**strata_id:** `str` — The strata server ID
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `McpServerName` — The name of the MCP Handle MCP server to delete authentication for (e.g., 'github', 'jira')
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">set_strata_auth</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets authentication data for a specific integration within a Strata MCP server.

Accepts either API key authentication or general authentication data.
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
from fern import FernApi, ApiKeyAuth
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.set_strata_auth(
    strata_id="strataId",
    server_name="Affinity",
    auth_data=ApiKeyAuth(),
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

**strata_id:** `str` — The strata server ID
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `McpServerName` — The name of the MCP Handle MCP server to set authentication for (e.g., 'GitHub', 'Jira')
    
</dd>
</dl>

<dl>
<dd>

**auth_data:** `StrataSetAuthRequestAuthData` — Authentication data
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">create_server_instance</a>(...) -> CreateServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a URL for a specified MCP server,
validating the request with an API key and user details.
Returns the existing server URL if it already exists for the user.
If OAuth is configured for the server, also returns the base OAuth authorization URL.
Note that some servers have hundreds of tools and therefore only expose the Strata tools.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.create_server_instance(
    server_name="Affinity",
    user_id="userId",
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

**server_name:** `McpServerName` — The name of the target MCP server. Case-insensitive (e.g., 'google calendar', 'GOOGLE_CALENDAR', 'Google Calendar' are all valid).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier for the user. The server instance along with the all the authentication data will belong to that specific user only. It can be a UUID from the database, a unique email address from the user, etc.
    
</dd>
</dl>

<dl>
<dd>

**platform_name:** `typing.Optional[str]` — The name of the platform associated with the user. Optional.
    
</dd>
</dl>

<dl>
<dd>

**connection_type:** `typing.Optional[ConnectionType]` — The connection type to use for the MCP server. Default is STREAMABLE_HTTP.
    
</dd>
</dl>

<dl>
<dd>

**legacy:** `typing.Optional[bool]` — Whether to use the legacy server. Default is False.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">create_self_hosted_server_instance</a>(...) -> CreateSelfHostedServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an instance id for a self-hosted MCP server,
validating the request with an API key and user details.
The main purpose of this endpoint is to create an instance id for a self-hosted MCP server.
The instance id is used to identify and store the auth metadata in the database.
Returns the existing instance id if it already exists for the user.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.create_self_hosted_server_instance(
    server_name="Affinity",
    user_id="userId",
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

**server_name:** `McpServerName` — The name of the target MCP server. Case-insensitive (e.g., 'google calendar', 'GOOGLE_CALENDAR', 'Google Calendar' are all valid).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier for the user. The server instance along with the all the authentication data will belong to that specific user only. It can be a UUID from the database, a unique email address from the user, etc.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">get_server_instance</a>(...) -> GetInstanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks the details of a specific server connection instance using its unique ID and API key,
returning server details like authentication status and associated server/platform info.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.get_server_instance(
    instance_id="instanceId",
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

**instance_id:** `str` — The ID of the connection integration instance whose status is being checked. This is returned by the Create API.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">delete_server_instance</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completely removes a server connection instance using its unique ID,
deleting all associated data from the system.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.delete_server_instance(
    instance_id="instanceId",
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

**instance_id:** `str` — The ID of the connection instance to delete.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">get_instance_auth_data</a>(...) -> GetAuthDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the auth data for a specific integration instance that the API key owner controls.
Includes access token, refresh token, and other authentication data.

This endpoint includes proper ownership verification to ensure users can only access
authentication data for integration instances they own. It also handles token refresh if needed.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.get_instance_auth_data(
    instance_id="instanceId",
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

**instance_id:** `str` — The ID of the connection integration instance to get auth data for.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">delete_instance_auth</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes authentication data for a specific server connection instance.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.delete_instance_auth(
    instance_id="instanceId",
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

**instance_id:** `str` — The ID of the connection instance to delete auth for.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">get_server_tools</a>(...) -> ListToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get tools information for any MCP server.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.get_server_tools(
    server_name="Affinity",
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

**server_name:** `McpServerName` — The name of the target MCP server. Case-insensitive (e.g., 'google calendar', 'GOOGLE_CALENDAR', 'Google Calendar' are all valid).
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ToolFormat]` — The format to return tools in. Default is MCP Native format for maximum compatibility.
    
</dd>
</dl>

<dl>
<dd>

**legacy:** `typing.Optional[bool]` — Whether to use the legacy server. Default is False.
    
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">get_all_mcp_servers</a>() -> GetMcpServersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all MCP servers with their basic information including id, name, description, and tools.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.get_all_mcp_servers()

```
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

<details><summary><code>client.mcp_server.<a href="src/fern/mcp_server/client.py">set_instance_auth</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets authentication data for a specific integration instance.
Accepts either API key authentication or general authentication data.
This updates the auth_metadata for the specified integration instance.
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
from fern import FernApi, ApiKeyAuth
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_server.set_instance_auth(
    instance_id="instanceId",
    auth_data=ApiKeyAuth(),
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

**instance_id:** `str` — The unique identifier for the connection instance
    
</dd>
</dl>

<dl>
<dd>

**auth_data:** `SetAuthRequestAuthData` — Authentication data
    
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

## WhiteLabeling
<details><summary><code>client.white_labeling.<a href="src/fern/white_labeling/client.py">create_white_labeling</a>(...) -> WhiteLabelingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Saves OAuth white labeling information, or updates existing information if the `client_id` matches.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.white_labeling.create_white_labeling(
    client_id="client_id",
    client_secret="client_secret",
    server_name="Airtable",
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

**client_id:** `str` — OAuth client ID
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — OAuth client secret
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `OAuthServerName` — Optional. The name of the server
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — Optional. OAuth callback URL
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — Optional. The UUID of the account
    
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

<details><summary><code>client.white_labeling.<a href="src/fern/white_labeling/client.py">get_white_labeling_by_client_id</a>(...) -> WhiteLabelingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves white labeling information for a specific OAuth client ID.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.white_labeling.get_white_labeling_by_client_id(
    client_id="client_id",
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

**client_id:** `str` 
    
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

## User
<details><summary><code>client.user.<a href="src/fern/user/client.py">get_user_integrations</a>(...) -> GetUserIntegrationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all available integrations (MCP server names) by user ID.
Returns a list of integration names as McpServerName types.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_user_integrations(
    user_id="userId",
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

**user_id:** `str` — The external user ID
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_user_by_user_id</a>(...) -> GetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get user information by user_id.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_user_by_user_id(
    user_id="userId",
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

**user_id:** `str` — The identifier for the user to fetch.
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">delete_user_by_user_id</a>(...) -> DeleteUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a user and all associated data by user_id.
Users cannot delete their own accounts.
This operation will permanently remove all user data.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.delete_user_by_user_id(
    user_id="userId",
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

**user_id:** `str` — The identifier for the user to delete.
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_all_users</a>(...) -> GetAllUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all users that have been created under your account, with support for pagination.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_all_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page (max 1000)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Page number to retrieve (starting from 1)
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">set_user_auth</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets authentication data for a specific integration for a user.

Accepts either API key authentication or general authentication data.
This updates the auth_metadata for the specified user's integration instance.
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
from fern import FernApi, ApiKeyAuth
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.set_user_auth(
    user_id="userId",
    server_name="Affinity",
    auth_data=ApiKeyAuth(),
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

**user_id:** `str` — The unique identifier for the user
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `McpServerName` — The name of the MCP server to set authentication for (e.g., 'GitHub', 'Jira')
    
</dd>
</dl>

<dl>
<dd>

**auth_data:** `SetUserAuthRequestAuthData` — Authentication data
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_user_auth</a>(...) -> GetUserAuthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves authentication data for a specific integration for a user.

Returns the authentication data if available, along with authentication status.
Includes token refresh handling if needed.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_user_auth(
    user_id="userId",
    server_name="Affinity",
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

**user_id:** `str` — The identifier for the user
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `McpServerName` — The name of the MCP server (e.g., 'GitHub', 'Jira')
    
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">delete_user_auth</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes authentication data for a specific integration for a user.

This will clear the stored authentication credentials, effectively unauthenticating the integration.
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.delete_user_auth(
    user_id="userId",
    server_name="Affinity",
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

**user_id:** `str` — The unique identifier for the user
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `McpServerName` — The name of the MCP server to delete authentication for (e.g., 'github', 'jira')
    
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

## SlackOauth
<details><summary><code>client.slack_oauth.<a href="src/fern/slack_oauth/client.py">authorize_slack</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Slack OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- user_scope: Optional user-specific scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slack_oauth.authorize_slack(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**user_scope:** `typing.Optional[str]` — Optional user-specific OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## GithubOauth
<details><summary><code>client.github_oauth.<a href="src/fern/github_oauth/client.py">authorize_github</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start GitHub OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.github_oauth.authorize_github(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## GitlabOauth
<details><summary><code>client.gitlab_oauth.<a href="src/fern/gitlab_oauth/client.py">authorize_gitlab</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start GitLab OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.gitlab_oauth.authorize_gitlab(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## SupabaseOauth
<details><summary><code>client.supabase_oauth.<a href="src/fern/supabase_oauth/client.py">authorize_supabase</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Supabase OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.supabase_oauth.authorize_supabase(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## NotionOauth
<details><summary><code>client.notion_oauth.<a href="src/fern/notion_oauth/client.py">authorize_notion</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Notion OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notion_oauth.authorize_notion(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## JiraOauth
<details><summary><code>client.jira_oauth.<a href="src/fern/jira_oauth/client.py">authorize_jira</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Jira OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jira_oauth.authorize_jira(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## ConfluenceOauth
<details><summary><code>client.confluence_oauth.<a href="src/fern/confluence_oauth/client.py">authorize_confluence</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Confluence OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.confluence_oauth.authorize_confluence(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## WordpressOauth
<details><summary><code>client.wordpress_oauth.<a href="src/fern/wordpress_oauth/client.py">authorize_wordpress</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start WordPress OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.wordpress_oauth.authorize_wordpress(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## GmailOauth
<details><summary><code>client.gmail_oauth.<a href="src/fern/gmail_oauth/client.py">authorize_gmail</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Gmail OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.gmail_oauth.authorize_gmail(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## GdriveOauth
<details><summary><code>client.gdrive_oauth.<a href="src/fern/gdrive_oauth/client.py">authorize_g_drive</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Google Drive OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.gdrive_oauth.authorize_g_drive(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## GcalendarOauth
<details><summary><code>client.gcalendar_oauth.<a href="src/fern/gcalendar_oauth/client.py">authorize_g_calendar</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Google Calendar OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.gcalendar_oauth.authorize_g_calendar(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## GsheetsOauth
<details><summary><code>client.gsheets_oauth.<a href="src/fern/gsheets_oauth/client.py">authorize_g_sheets</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Google Sheets OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.gsheets_oauth.authorize_g_sheets(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## GdocsOauth
<details><summary><code>client.gdocs_oauth.<a href="src/fern/gdocs_oauth/client.py">authorize_g_docs</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Google Docs OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.gdocs_oauth.authorize_g_docs(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## AttioOauth
<details><summary><code>client.attio_oauth.<a href="src/fern/attio_oauth/client.py">authorize_attio</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Attio OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.attio_oauth.authorize_attio(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## SalesforceOauth
<details><summary><code>client.salesforce_oauth.<a href="src/fern/salesforce_oauth/client.py">authorize_salesforce</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Salesforce OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
- instance_url: Optional Salesforce instance URL for sandbox or custom domains
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.salesforce_oauth.authorize_salesforce(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
</dd>
</dl>

<dl>
<dd>

**instance_url:** `typing.Optional[str]` — Salesforce instance URL (e.g., https://mycompany.salesforce.com). If not provided, will use default login.salesforce.com
    
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

## AsanaOauth
<details><summary><code>client.asana_oauth.<a href="src/fern/asana_oauth/client.py">authorize_asana</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Asana OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.asana_oauth.authorize_asana(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## LinearOauth
<details><summary><code>client.linear_oauth.<a href="src/fern/linear_oauth/client.py">authorize_linear</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Linear OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.linear_oauth.authorize_linear(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## CloseOauth
<details><summary><code>client.close_oauth.<a href="src/fern/close_oauth/client.py">authorize_close</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Close OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.close_oauth.authorize_close(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## ClickupOauth
<details><summary><code>client.clickup_oauth.<a href="src/fern/clickup_oauth/client.py">authorize_click_up</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start ClickUp OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.clickup_oauth.authorize_click_up(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## AirtableOauth
<details><summary><code>client.airtable_oauth.<a href="src/fern/airtable_oauth/client.py">authorize_airtable</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Airtable OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.airtable_oauth.authorize_airtable(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## HubspotOauth
<details><summary><code>client.hubspot_oauth.<a href="src/fern/hubspot_oauth/client.py">authorize_hubspot</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start HubSpot OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.hubspot_oauth.authorize_hubspot(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## LinkedinOauth
<details><summary><code>client.linkedin_oauth.<a href="src/fern/linkedin_oauth/client.py">authorize_linked_in</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start LinkedIn OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.linkedin_oauth.authorize_linked_in(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## CanvaOauth
<details><summary><code>client.canva_oauth.<a href="src/fern/canva_oauth/client.py">authorize_canva</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Canva OAuth flow with PKCE

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated, e.g., "design:meta:read profile:read")
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.canva_oauth.authorize_canva(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## XeroOauth
<details><summary><code>client.xero_oauth.<a href="src/fern/xero_oauth/client.py">authorize_xero</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Xero OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.xero_oauth.authorize_xero(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## DropboxOauth
<details><summary><code>client.dropbox_oauth.<a href="src/fern/dropbox_oauth/client.py">authorize_dropbox</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Dropbox OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dropbox_oauth.authorize_dropbox(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## BoxOauth
<details><summary><code>client.box_oauth.<a href="src/fern/box_oauth/client.py">authorize_box</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Box OAuth 2.0 flow
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.box_oauth.authorize_box(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## QuickbooksOauth
<details><summary><code>client.quickbooks_oauth.<a href="src/fern/quickbooks_oauth/client.py">authorize_quick_books</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start QuickBooks OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- environment: QuickBooks environment to authorize ('sandbox' default)
- scope: Optional scopes to request (space-separated). Default is 'com.intuit.quickbooks.accounting'
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quickbooks_oauth.authorize_quick_books(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[AuthorizeQuickBooksRequestEnvironment]` — QuickBooks environment to authorize ('sandbox' or 'production')
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## ZendeskOauth
<details><summary><code>client.zendesk_oauth.<a href="src/fern/zendesk_oauth/client.py">authorize_zendesk</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Zendesk OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
- subdomain: Zendesk subdomain for the account being connected
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.zendesk_oauth.authorize_zendesk(
    instance_id="instance_id",
    subdomain="subdomain",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**subdomain:** `str` — Zendesk subdomain for the account being connected (e.g., 'mycompany' for mycompany.zendesk.com)
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## StripeConnectOauth
<details><summary><code>client.stripe_connect_oauth.<a href="src/fern/stripe_connect_oauth/client.py">authorize_stripe_connect</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Stripe Connect OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stripe_connect_oauth.authorize_stripe_connect(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## CalcomOauth
<details><summary><code>client.calcom_oauth.<a href="src/fern/calcom_oauth/client.py">authorize_calcom</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Cal.com OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.calcom_oauth.authorize_calcom(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## VercelOauth
<details><summary><code>client.vercel_oauth.<a href="src/fern/vercel_oauth/client.py">authorize_vercel</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Vercel OAuth flow using integration pattern

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- client_slug: Vercel integration slug (required for integration-based OAuth)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vercel_oauth.authorize_vercel(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**client_slug:** `typing.Optional[str]` — Vercel integration slug (required for integration-based OAuth)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## PipedriveOauth
<details><summary><code>client.pipedrive_oauth.<a href="src/fern/pipedrive_oauth/client.py">authorize_pipedrive</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Pipedrive OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipedrive_oauth.authorize_pipedrive(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## FigmaOauth
<details><summary><code>client.figma_oauth.<a href="src/fern/figma_oauth/client.py">authorize_figma</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Figma OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.figma_oauth.authorize_figma(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## KlaviyoOauth
<details><summary><code>client.klaviyo_oauth.<a href="src/fern/klaviyo_oauth/client.py">authorize_klaviyo</a>(...) -> typing.Any</code></summary>
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.klaviyo_oauth.authorize_klaviyo(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## PagerdutyOauth
<details><summary><code>client.pagerduty_oauth.<a href="src/fern/pagerduty_oauth/client.py">authorize_pager_duty</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start PagerDuty OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pagerduty_oauth.authorize_pager_duty(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## DocusignOauth
<details><summary><code>client.docusign_oauth.<a href="src/fern/docusign_oauth/client.py">authorize_docu_sign</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start DocuSign OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.docusign_oauth.authorize_docu_sign(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## DialpadOauth
<details><summary><code>client.dialpad_oauth.<a href="src/fern/dialpad_oauth/client.py">authorize_dialpad</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Dialpad OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
- code_challenge: PKCE code challenge for enhanced security
- code_challenge_method: PKCE code challenge method
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dialpad_oauth.authorize_dialpad(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `typing.Optional[str]` — PKCE code challenge for enhanced security
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `typing.Optional[str]` — PKCE code challenge method (default: S256)
    
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

## ShopifyOauth
<details><summary><code>client.shopify_oauth.<a href="src/fern/shopify_oauth/client.py">authorize_shopify</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Shopify OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- shop: Shopify shop domain (e.g., mystore.myshopify.com)
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (comma-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shopify_oauth.authorize_shopify(
    instance_id="instance_id",
    shop="shop",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**shop:** `str` — Shopify shop domain (e.g., mystore.myshopify.com)
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (comma-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## OnedriveOauth
<details><summary><code>client.onedrive_oauth.<a href="src/fern/onedrive_oauth/client.py">authorize_one_drive</a>(...) -> typing.Any</code></summary>
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.onedrive_oauth.authorize_one_drive(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

<details><summary><code>client.onedrive_oauth.<a href="src/fern/onedrive_oauth/client.py">refresh_token</a>(...) -> AzureAdoAuthSuccessResponse</code></summary>
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.onedrive_oauth.refresh_token(
    instance_id="instance_id",
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

**instance_id:** `str` — Instance ID for which to refresh the token
    
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

## OutlookOauth
<details><summary><code>client.outlook_oauth.<a href="src/fern/outlook_oauth/client.py">authorize_outlook</a>(...) -> typing.Any</code></summary>
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.outlook_oauth.authorize_outlook(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

<details><summary><code>client.outlook_oauth.<a href="src/fern/outlook_oauth/client.py">refresh_token</a>(...) -> AzureAdoAuthSuccessResponse</code></summary>
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.outlook_oauth.refresh_token(
    instance_id="instance_id",
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

**instance_id:** `str` — Instance ID for which to refresh the token
    
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

## TeamsOauth
<details><summary><code>client.teams_oauth.<a href="src/fern/teams_oauth/client.py">authorize_teams</a>(...) -> typing.Any</code></summary>
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.teams_oauth.authorize_teams(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

<details><summary><code>client.teams_oauth.<a href="src/fern/teams_oauth/client.py">refresh_token</a>(...) -> AzureAdoAuthSuccessResponse</code></summary>
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.teams_oauth.refresh_token(
    instance_id="instance_id",
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

**instance_id:** `str` — Instance ID for which to refresh the token
    
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

## FathomOauth
<details><summary><code>client.fathom_oauth.<a href="src/fern/fathom_oauth/client.py">authorize_fathom</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Fathom OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fathom_oauth.authorize_fathom(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

## MondayOauth
<details><summary><code>client.monday_oauth.<a href="src/fern/monday_oauth/client.py">authorize_monday</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start Monday OAuth flow

Parameters:
- instance_id: Identifier for the instance requesting authorization
- client_id: Optional client ID for white labeling
- scope: Optional scopes to request (space-separated)
- redirect_url: Optional URL to redirect to after authorization completes
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
    api_key="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monday_oauth.authorize_monday(
    instance_id="instance_id",
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

**instance_id:** `str` — Unique identifier for the client instance requesting authorization
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client ID for white labeling, if not provided will use default credentials
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional OAuth scopes to request (space-separated string)
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Optional URL to redirect to after authorization completes
    
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

