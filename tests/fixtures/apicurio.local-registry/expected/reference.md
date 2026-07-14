# Reference
## ArtifactType
<details><summary><code>client.artifact_type.<a href="src/fern/artifact_type/client.py">list_artifact_types</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of all the configured artifact types.

This operation can fail for the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifact_type.list_artifact_types()

```
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

## Admin
<details><summary><code>client.admin.<a href="src/fern/admin/client.py">list_config_properties</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all configuration properties that have been set.  The list is not paged.

This operation may fail for one of the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.admin.list_config_properties()

```
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">get_config_property</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the value of a single configuration property.

This operation may fail for one of the following reasons:

* Property not found or not configured (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.admin.get_config_property(
    property_name="propertyName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**property_name:** `str` — The name of a configuration property.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">update_config_property</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the value of a single configuration property.

This operation may fail for one of the following reasons:

* Property not found or not configured (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.admin.update_config_property(
    property_name="propertyName",
    value="true",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**property_name:** `str` — The name of a configuration property.
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">reset_config_property</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resets the value of a single configuration property.  This will return the property to
its default value (see external documentation for supported properties and their default
values).

This operation may fail for one of the following reasons:

* Property not found or not configured (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.admin.reset_config_property(
    property_name="propertyName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**property_name:** `str` — The name of a configuration property.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">export_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports registry data as a ZIP archive.
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

client = FernApi()
client.admin.export_data()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**for_browser:** `typing.Optional[bool]` — Indicates if the operation is done for a browser.  If true, the response will be a JSON payload with a property called `href`.  This `href` will be a single-use, naked download link suitable for use by a web browser to download the content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">list_log_configurations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all of the configured logging levels.  These override the default
logging configuration.
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

client = FernApi()
client.admin.list_log_configurations()

```
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">get_log_configuration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the configured logger configuration for the provided logger name, if no logger configuration is persisted it will return the current default log configuration in the system.
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

client = FernApi()
client.admin.get_log_configuration(
    logger="logger",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logger:** `str` — The name of a single logger.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">set_log_configuration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configures the logger referenced by the provided logger name with the given configuration.
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
from fern import FernApi, LogLevel

client = FernApi()
client.admin.set_log_configuration(
    logger="logger",
    level=LogLevel.DEBUG,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logger:** `str` — The name of a single logger.
    
</dd>
</dl>

<dl>
<dd>

**level:** `LogLevel` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">remove_log_configuration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the configured logger configuration (if any) for the given logger.
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

client = FernApi()
client.admin.remove_log_configuration(
    logger="logger",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logger:** `str` — The name of a single logger.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">list_role_mappings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of all role mappings configured in the registry (if any).

This operation can fail for the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.admin.list_role_mappings()

```
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">create_role_mapping</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new mapping between a user/principal and a role.

This operation can fail for the following reasons:

* A server error occurred (HTTP error `500`)

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
from fern import FernApi, RoleType

client = FernApi()
client.admin.create_role_mapping(
    principal_id="svc_account_84874587_123484",
    principal_name="famartin-svc-account",
    role=RoleType.READ_ONLY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**principal_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**role:** `RoleType` — 
    
</dd>
</dl>

<dl>
<dd>

**principal_name:** `typing.Optional[str]` — A friendly name for the principal.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">get_role_mapping</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the details of a single role mapping (by `principalId`).

This operation can fail for the following reasons:

* No role mapping for the `principalId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.admin.get_role_mapping(
    principal_id="principalId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**principal_id:** `str` — Unique id of a principal (typically either a user or service account).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">update_role_mapping</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a single role mapping for one user/principal.

This operation can fail for the following reasons:

* No role mapping for the principalId exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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
from fern import FernApi, RoleType

client = FernApi()
client.admin.update_role_mapping(
    principal_id="principalId",
    role=RoleType.READ_ONLY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**principal_id:** `str` — Unique id of a principal (typically either a user or service account).
    
</dd>
</dl>

<dl>
<dd>

**role:** `RoleType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">delete_role_mapping</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single role mapping, effectively denying access to a user/principal.

This operation can fail for the following reasons:

* No role mapping for the principalId exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.admin.delete_role_mapping(
    principal_id="principalId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**principal_id:** `str` — Unique id of a principal (typically either a user or service account).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Global rules
<details><summary><code>client.global_rules.<a href="src/fern/global_rules/client.py">list_global_rules</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of all the currently configured global rules (if any).

This operation can fail for the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.global_rules.list_global_rules()

```
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

<details><summary><code>client.global_rules.<a href="src/fern/global_rules/client.py">create_global_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a rule to the list of globally configured rules.

This operation can fail for the following reasons:

* The rule type is unknown (HTTP error `400`)
* The rule already exists (HTTP error `409`)
* A server error occurred (HTTP error `500`)
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
from fern import FernApi, RuleType

client = FernApi()
client.global_rules.create_global_rule(
    config="FULL",
    type=RuleType.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[RuleType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_rules.<a href="src/fern/global_rules/client.py">delete_all_global_rules</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all globally configured rules.

This operation can fail for the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.global_rules.delete_all_global_rules()

```
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

<details><summary><code>client.global_rules.<a href="src/fern/global_rules/client.py">get_global_rule_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the named globally configured rule.

This operation can fail for the following reasons:

* Invalid rule name/type (HTTP error `400`)
* No rule with name/type `rule` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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
from fern import FernApi, RuleType

client = FernApi()
client.global_rules.get_global_rule_config(
    rule=RuleType.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule:** `RuleType` — The unique name/type of a rule.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_rules.<a href="src/fern/global_rules/client.py">update_global_rule_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the configuration for a globally configured rule.

This operation can fail for the following reasons:

* Invalid rule name/type (HTTP error `400`)
* No rule with name/type `rule` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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
from fern import FernApi, RuleType

client = FernApi()
client.global_rules.update_global_rule_config(
    rule=RuleType.VALIDITY,
    config="FULL",
    type=RuleType.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule:** `RuleType` — The unique name/type of a rule.
    
</dd>
</dl>

<dl>
<dd>

**config:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[RuleType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_rules.<a href="src/fern/global_rules/client.py">delete_global_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single global rule.  If this is the only rule configured, this is the same
as deleting **all** rules.

This operation can fail for the following reasons:

* Invalid rule name/type (HTTP error `400`)
* No rule with name/type `rule` exists (HTTP error `404`)
* Rule cannot be deleted (HTTP error `409`)
* A server error occurred (HTTP error `500`)
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
from fern import FernApi, RuleType

client = FernApi()
client.global_rules.delete_global_rule(
    rule=RuleType.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule:** `RuleType` — The unique name/type of a rule.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Groups
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">list_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all groups.  This list is paged.
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

client = FernApi()
client.groups.list_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of groups to return.  Defaults to 20.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of groups to skip before starting the result set.  Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SortOrder]` — Sort order, ascending (`asc`) or descending (`desc`).
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `typing.Optional[SortBy]` 

The field to sort by.  Can be one of:

* `name`
* `createdOn`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">create_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new group.

This operation can fail for the following reasons:

* A server error occurred (HTTP error `500`)
* The group already exist (HTTP error `409`)
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

client = FernApi()
client.groups.create_group(
    description="The description of the artifact.",
    id="group-identifier",
    properties={"custom-1": "foo", "custom-2": "bar"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[Properties]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_group_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a group using the specified id.

This operation can fail for the following reasons:

* No group exists with the specified ID (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.groups.get_group_by_id(
    group_id='"my-group"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_group_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a group by identifier.

This operation can fail for the following reasons:

* A server error occurred (HTTP error `500`)
* The group does not exist (HTTP error `404`)
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

client = FernApi()
client.groups.delete_group_by_id(
    group_id='"my-group"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Artifacts
<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">list_artifacts_in_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all artifacts in the group.  This list is paged.
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

client = FernApi()
client.artifacts.list_artifacts_in_group(
    group_id='"my-group"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of artifacts to return.  Defaults to 20.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of artifacts to skip before starting the result set.  Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SortOrder]` — Sort order, ascending (`asc`) or descending (`desc`).
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `typing.Optional[SortBy]` 

The field to sort by.  Can be one of:

* `name`
* `createdOn`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">create_artifact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new artifact by posting the artifact content.  The body of the request should
be the raw content of the artifact.  This is typically in JSON format for *most* of the 
supported types, but may be in another format for a few (for example, `PROTOBUF`).

The registry attempts to figure out what kind of artifact is being added from the
following supported list:

* Avro (`AVRO`)
* Protobuf (`PROTOBUF`)
* JSON Schema (`JSON`)
* Kafka Connect (`KCONNECT`)
* OpenAPI (`OPENAPI`)
* AsyncAPI (`ASYNCAPI`)
* GraphQL (`GRAPHQL`)
* Web Services Description Language (`WSDL`)
* XML Schema (`XSD`)

Alternatively, you can specify the artifact type using the `X-Registry-ArtifactType` 
HTTP request header, or include a hint in the request's `Content-Type`.  For example:

```
Content-Type: application/json; artifactType=AVRO
```

An artifact is created using the content provided in the body of the request.  This
content is created under a unique artifact ID that can be provided in the request
using the `X-Registry-ArtifactId` request header.  If not provided in the request,
the server generates a unique ID for the artifact.  It is typically recommended
that callers provide the ID, because this is typically a meaningful identifier, 
and for most use cases should be supplied by the caller.

If an artifact with the provided artifact ID already exists, the default behavior
is for the server to reject the content with a 409 error.  However, the caller can
supply the `ifExists` query parameter to alter this default behavior. The `ifExists`
query parameter can have one of the following values:

* `FAIL` (*default*) - server rejects the content with a 409 error
* `UPDATE` - server updates the existing artifact and returns the new metadata
* `RETURN` - server does not create or add content to the server, but instead 
returns the metadata for the existing artifact
* `RETURN_OR_UPDATE` - server returns an existing **version** that matches the 
provided content if such a version exists, otherwise a new version is created

This operation may fail for one of the following reasons:

* An invalid `ArtifactType` was indicated (HTTP error `400`)
* No `ArtifactType` was indicated and the server could not determine one from the content (HTTP error `400`)
* Provided content (request body) was empty (HTTP error `400`)
* An artifact with the provided ID already exists (HTTP error `409`)
* The content violates one of the configured global rules (HTTP error `409`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.create_artifact(
    group_id='"my-group"',
    registry_artifact_type="AVRO",
    registry_version='"3.1.6"',
    registry_description='"Artifact description"',
    registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
    registry_name='"Artifact name"',
    registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileContent` 
    
</dd>
</dl>

<dl>
<dd>

**if_exists:** `typing.Optional[IfExists]` — Set this option to instruct the server on what to do if the artifact already exists.
    
</dd>
</dl>

<dl>
<dd>

**canonical:** `typing.Optional[bool]` — Used only when the `ifExists` query parameter is set to `RETURN_OR_UPDATE`, this parameter can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner.
    
</dd>
</dl>

<dl>
<dd>

**registry_artifact_type:** `typing.Optional[ArtifactType]` 

Specifies the type of the artifact being added. Possible values include:

* Avro (`AVRO`)
* Protobuf (`PROTOBUF`)
* JSON Schema (`JSON`)
* Kafka Connect (`KCONNECT`)
* OpenAPI (`OPENAPI`)
* AsyncAPI (`ASYNCAPI`)
* GraphQL (`GRAPHQL`)
* Web Services Description Language (`WSDL`)
* XML Schema (`XSD`)
    
</dd>
</dl>

<dl>
<dd>

**registry_artifact_id:** `typing.Optional[str]` — A client-provided, globally unique identifier for the new artifact.
    
</dd>
</dl>

<dl>
<dd>

**registry_version:** `typing.Optional[Version]` 

Specifies the version number of this initial version of the artifact content.  This would typically
be a simple integer or a SemVer value.  If not provided, the server will assign a version number
automatically (starting with version `1`).
    
</dd>
</dl>

<dl>
<dd>

**registry_description:** `typing.Optional[ArtifactDescription]` — Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_description_encoded:** `typing.Optional[EncodedArtifactDescription]` — Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_name:** `typing.Optional[ArtifactName]` — Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_name_encoded:** `typing.Optional[EncodedArtifactName]` — Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_content_hash:** `typing.Optional[str]` — Specifies the (optional) hash of the artifact to be verified.
    
</dd>
</dl>

<dl>
<dd>

**registry_hash_algorithm:** `typing.Optional[CreateArtifactRequestXRegistryHashAlgorithm]` — The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">delete_artifacts_in_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all of the artifacts that exist in a given group.
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

client = FernApi()
client.artifacts.delete_artifacts_in_group(
    group_id='"my-group"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">get_latest_artifact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest version of the artifact in its raw form.  The `Content-Type` of the
response depends on the artifact type.  In most cases, this is `application/json`, but 
for some types it may be different (for example, `PROTOBUF`).

This operation may fail for one of the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.get_latest_artifact(
    group_id="groupId",
    artifact_id="artifactId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**dereference:** `typing.Optional[bool]` — Allows the user to specify if the content should be dereferenced when being returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">update_artifact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an artifact by uploading new content.  The body of the request can
be the raw content of the artifact or a JSON object containing both the raw content and
a set of references to other artifacts..  This is typically in JSON format for *most*
of the supported types, but may be in another format for a few (for example, `PROTOBUF`).
The type of the content should be compatible with the artifact's type (it would be
an error to update an `AVRO` artifact with new `OPENAPI` content, for example).

The update could fail for a number of reasons including:

* Provided content (request body) was empty (HTTP error `400`)
* No artifact with the `artifactId` exists (HTTP error `404`)
* The new content violates one of the rules configured for the artifact (HTTP error `409`)
* A server error occurred (HTTP error `500`)

When successful, this creates a new version of the artifact, making it the most recent
(and therefore official) version of the artifact.
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

client = FernApi()
client.artifacts.update_artifact(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    registry_version='"3.1.6"',
    registry_name='"Artifact name"',
    registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
    registry_description='"Artifact description"',
    registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileContent` 
    
</dd>
</dl>

<dl>
<dd>

**registry_version:** `typing.Optional[Version]` 

Specifies the version number of this new version of the artifact content.  This would typically
be a simple integer or a SemVer value.  If not provided, the server will assign a version number
automatically.
    
</dd>
</dl>

<dl>
<dd>

**registry_name:** `typing.Optional[ArtifactName]` 

Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
provided, the server will extract the name from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_name_encoded:** `typing.Optional[EncodedArtifactName]` — Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_description:** `typing.Optional[ArtifactDescription]` — Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_description_encoded:** `typing.Optional[EncodedArtifactDescription]` — Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">delete_artifact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an artifact completely, resulting in all versions of the artifact also being
deleted.  This may fail for one of the following reasons:

* No artifact with the `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.delete_artifact(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">update_artifact_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the state of the artifact.  For example, you can use this to mark the latest
version of an artifact as `DEPRECATED`.  The operation changes the state of the latest 
version of the artifact.  If multiple versions exist, only the most recent is changed.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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
from fern import ArtifactState, FernApi

client = FernApi()
client.artifacts.update_artifact_state(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    state=ArtifactState.DISABLED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**state:** `ArtifactState` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">get_content_by_hash</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the content for an artifact version in the registry using the 
SHA-256 hash of the content.  This content hash may be shared by multiple artifact
versions in the case where the artifact versions have identical content.

This operation may fail for one of the following reasons:

* No content with this `contentHash` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.get_content_by_hash(
    content_hash="contentHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_hash:** `str` — SHA-256 content hash for a single artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">references_by_content_hash</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list containing all the artifact references using the artifact content hash.

This operation may fail for one of the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.references_by_content_hash(
    content_hash="contentHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_hash:** `str` — SHA-256 content hash for a single artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">get_content_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the content for an artifact version in the registry using the unique content
identifier for that content.  This content ID may be shared by multiple artifact
versions in the case where the artifact versions are identical.

This operation may fail for one of the following reasons:

* No content with this `contentId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.get_content_by_id(
    content_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_id:** `int` — Global identifier for a single artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">references_by_content_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list containing all the artifact references using the artifact content ID.

This operation may fail for one of the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.references_by_content_id(
    content_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_id:** `int` — Global identifier for a single artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">get_content_by_global_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the content for an artifact version in the registry using its globally unique
identifier.

This operation may fail for one of the following reasons:

* No artifact version with this `globalId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.get_content_by_global_id(
    global_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**global_id:** `int` — Global identifier for an artifact version.
    
</dd>
</dl>

<dl>
<dd>

**dereference:** `typing.Optional[bool]` — Allows the user to specify if the content should be dereferenced when being returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">references_by_global_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list containing all the artifact references using the artifact global ID.

This operation may fail for one of the following reasons:

* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifacts.references_by_global_id(
    global_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**global_id:** `int` — Global identifier for an artifact version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metadata
<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">get_artifact_meta_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the metadata for an artifact in the registry.  The returned metadata includes
both generated (read-only) and editable metadata (such as name and description).

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.get_artifact_meta_data(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">get_artifact_version_meta_data_by_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the metadata for an artifact that matches the raw content.  Searches the registry
for a version of the given artifact matching the content provided in the body of the
POST.

This operation can fail for the following reasons:

* Provided content (request body) was empty (HTTP error `400`)
* No artifact with the `artifactId` exists (HTTP error `404`)
* No artifact version matching the provided content exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.get_artifact_version_meta_data_by_content(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileContent` 
    
</dd>
</dl>

<dl>
<dd>

**canonical:** `typing.Optional[bool]` — Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">update_artifact_meta_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the editable parts of the artifact's metadata.  Not all metadata fields can
be updated.  For example, `createdOn` and `createdBy` are both read-only properties.

This operation can fail for the following reasons:

* No artifact with the `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.update_artifact_meta_data(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    description="The description of the artifact.",
    labels=["regional", "global"],
    name="Artifact Name",
    properties={"custom-1": "foo", "custom-2": "bar"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[Properties]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">get_artifact_owner</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the owner of an artifact in the registry.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.get_artifact_owner(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">update_artifact_owner</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes the ownership of an artifact.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.update_artifact_owner(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    owner="bwayne",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">get_artifact_version_meta_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the metadata for a single version of the artifact.  The version metadata is 
a subset of the artifact metadata and only includes the metadata that is specific to
the version (for example, this doesn't include `modifiedOn`).

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No version with this `version` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.get_artifact_version_meta_data(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    version='"3.1.6"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**version:** `Version` — The unique identifier of a specific version of the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">update_artifact_version_meta_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the user-editable portion of the artifact version's metadata.  Only some of 
the metadata fields are editable by the user.  For example, `description` is editable, 
but `createdOn` is not.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No version with this `version` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.update_artifact_version_meta_data(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    version='"3.1.6"',
    description="The description of the artifact.",
    labels=["regional", "global"],
    name="Artifact Name",
    properties={"custom-1": "foo", "custom-2": "bar"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**version:** `Version` — The unique identifier of a specific version of the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[Properties]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">delete_artifact_version_meta_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the user-editable metadata properties of the artifact version.  Any properties
that are not user-editable are preserved.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No version with this `version` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.metadata.delete_artifact_version_meta_data(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    version='"3.1.6"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**version:** `Version` — The unique identifier of a specific version of the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Artifact rules
<details><summary><code>client.artifact_rules.<a href="src/fern/artifact_rules/client.py">list_artifact_rules</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all rules configured for the artifact.  The set of rules determines
how the content of an artifact can evolve over time.  If no rules are configured for
an artifact, the set of globally configured rules are used.  If no global rules 
are defined, there are no restrictions on content evolution.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifact_rules.list_artifact_rules(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_rules.<a href="src/fern/artifact_rules/client.py">create_artifact_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a rule to the list of rules that get applied to the artifact when adding new
versions.  All configured rules must pass to successfully add a new artifact version.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* Rule (named in the request body) is unknown (HTTP error `400`)
* A server error occurred (HTTP error `500`)
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
from fern import FernApi, RuleType

client = FernApi()
client.artifact_rules.create_artifact_rule(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    config="FULL",
    type=RuleType.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**config:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[RuleType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_rules.<a href="src/fern/artifact_rules/client.py">delete_artifact_rules</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all of the rules configured for the artifact.  After this is done, the global
rules apply to the artifact again.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.artifact_rules.delete_artifact_rules(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_rules.<a href="src/fern/artifact_rules/client.py">get_artifact_rule_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a single rule configured for an artifact.  This is useful
when you want to know what the current configuration settings are for a specific rule.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No rule with this name/type is configured for this artifact (HTTP error `404`)
* Invalid rule type (HTTP error `400`)
* A server error occurred (HTTP error `500`)
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
from fern.artifact_rules import GetArtifactRuleConfigRequestRule

from fern import FernApi

client = FernApi()
client.artifact_rules.get_artifact_rule_config(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    rule=GetArtifactRuleConfigRequestRule.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**rule:** `GetArtifactRuleConfigRequestRule` — The unique name/type of a rule.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_rules.<a href="src/fern/artifact_rules/client.py">update_artifact_rule_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the configuration of a single rule for the artifact.  The configuration data
is specific to each rule type, so the configuration of the `COMPATIBILITY` rule 
is in a different format from the configuration of the `VALIDITY` rule.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No rule with this name/type is configured for this artifact (HTTP error `404`)
* Invalid rule type (HTTP error `400`)
* A server error occurred (HTTP error `500`)
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
from fern.artifact_rules import UpdateArtifactRuleConfigRequestRule

from fern import FernApi, RuleType

client = FernApi()
client.artifact_rules.update_artifact_rule_config(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    rule=UpdateArtifactRuleConfigRequestRule.VALIDITY,
    config="FULL",
    type=RuleType.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**rule:** `UpdateArtifactRuleConfigRequestRule` — The unique name/type of a rule.
    
</dd>
</dl>

<dl>
<dd>

**config:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[RuleType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_rules.<a href="src/fern/artifact_rules/client.py">delete_artifact_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a rule from the artifact.  This results in the rule no longer applying for
this artifact.  If this is the only rule configured for the artifact, this is the 
same as deleting **all** rules, and the globally configured rules now apply to
this artifact.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No rule with this name/type is configured for this artifact (HTTP error `404`)
* Invalid rule type (HTTP error `400`)
* A server error occurred (HTTP error `500`)
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
from fern.artifact_rules import DeleteArtifactRuleRequestRule

from fern import FernApi

client = FernApi()
client.artifact_rules.delete_artifact_rule(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    rule=DeleteArtifactRuleRequestRule.VALIDITY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**rule:** `DeleteArtifactRuleRequestRule` — The unique name/type of a rule.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_rules.<a href="src/fern/artifact_rules/client.py">test_update_artifact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tests whether an update to the artifact's content *would* succeed for the provided content.
Ultimately, this applies any rules configured for the artifact against the given content
to determine whether the rules would pass or fail, but without actually updating the artifact
content.

The body of the request should be the raw content of the artifact.  This is typically in 
JSON format for *most* of the supported types, but may be in another format for a few 
(for example, `PROTOBUF`).

The update could fail for a number of reasons including:

* Provided content (request body) was empty (HTTP error `400`)
* No artifact with the `artifactId` exists (HTTP error `404`)
* The new content violates one of the rules configured for the artifact (HTTP error `409`)
* The provided artifact type is not recognized (HTTP error `404`)
* A server error occurred (HTTP error `500`)

When successful, this operation simply returns a *No Content* response.  This response
indicates that the content is valid against the configured content rules for the 
artifact (or the global rules if no artifact rules are enabled).
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

client = FernApi()
client.artifact_rules.test_update_artifact(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Versions
<details><summary><code>client.versions.<a href="src/fern/versions/client.py">list_artifact_versions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all versions of the artifact.  The result set is paged.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.versions.list_artifact_versions(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of versions to skip before starting to collect the result set.  Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of versions to return.  Defaults to 20.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.versions.<a href="src/fern/versions/client.py">create_artifact_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new version of the artifact by uploading new content.  The configured rules for
the artifact are applied, and if they all pass, the new content is added as the most recent 
version of the artifact.  If any of the rules fail, an error is returned.

The body of the request can be the raw content of the new artifact version, or the raw content 
and a set of references pointing to other artifacts, and the type
of that content should match the artifact's type (for example if the artifact type is `AVRO`
then the content of the request should be an Apache Avro document).

This operation can fail for the following reasons:

* Provided content (request body) was empty (HTTP error `400`)
* No artifact with this `artifactId` exists (HTTP error `404`)
* The new content violates one of the rules configured for the artifact (HTTP error `409`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.versions.create_artifact_version(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    registry_version='"3.1.6"',
    registry_name='"Artifact name"',
    registry_description='"Artifact description"',
    registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
    registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FileContent` 
    
</dd>
</dl>

<dl>
<dd>

**registry_version:** `typing.Optional[Version]` 

Specifies the version number of this new version of the artifact content.  This would typically
be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not
provided, the server will generate a new, unique version number for this new updated content.
    
</dd>
</dl>

<dl>
<dd>

**registry_name:** `typing.Optional[ArtifactName]` 

Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
provided, the server will extract the name from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_description:** `typing.Optional[ArtifactDescription]` — Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_description_encoded:** `typing.Optional[EncodedArtifactDescription]` — Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**registry_name_encoded:** `typing.Optional[EncodedArtifactName]` — Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.versions.<a href="src/fern/versions/client.py">get_artifact_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a single version of the artifact content.  Both the `artifactId` and the
unique `version` number must be provided.  The `Content-Type` of the response depends 
on the artifact type.  In most cases, this is `application/json`, but for some types 
it may be different (for example, `PROTOBUF`).

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No version with this `version` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.versions.get_artifact_version(
    group_id="groupId",
    artifact_id="artifactId",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**version:** `Version` — The unique identifier of a specific version of the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**dereference:** `typing.Optional[bool]` — Allows the user to specify if the content should be dereferenced when being returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.versions.<a href="src/fern/versions/client.py">get_artifact_version_references</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a single version of the artifact content.  Both the `artifactId` and the
unique `version` number must be provided.  The `Content-Type` of the response depends 
on the artifact type.  In most cases, this is `application/json`, but for some types 
it may be different (for example, `PROTOBUF`).

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No version with this `version` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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

client = FernApi()
client.versions.get_artifact_version_references(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    version='"3.1.6"',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**version:** `Version` — The unique identifier of a specific version of the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.versions.<a href="src/fern/versions/client.py">update_artifact_version_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the state of a specific version of an artifact.  For example, you can use 
this operation to disable a specific version.

This operation can fail for the following reasons:

* No artifact with this `artifactId` exists (HTTP error `404`)
* No version with this `version` exists (HTTP error `404`)
* A server error occurred (HTTP error `500`)
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
from fern import ArtifactState, FernApi

client = FernApi()
client.versions.update_artifact_version_state(
    group_id='"my-group"',
    artifact_id='"example-artifact"',
    version='"3.1.6"',
    state=ArtifactState.DISABLED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupId` — The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `ArtifactId` — The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    
</dd>
</dl>

<dl>
<dd>

**version:** `Version` — The unique identifier of a specific version of the artifact content.
    
</dd>
</dl>

<dl>
<dd>

**state:** `ArtifactState` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Search
<details><summary><code>client.search.<a href="src/fern/search/client.py">artifacts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of all artifacts that match the provided filter criteria.
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

client = FernApi()
client.search.artifacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by artifact name.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of artifacts to return.  Defaults to 20.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SortOrder]` — Sort order, ascending (`asc`) or descending (`desc`).
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `typing.Optional[SortBy]` 

The field to sort by.  Can be one of:

* `name`
* `createdOn`
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter by label.  Include one or more label to only return artifacts containing all of the
specified labels.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter by one or more name/value property.  Separate each name/value pair using a colon.  For
example `properties=foo:bar` will return only artifacts with a custom property named `foo`
and value `bar`.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Filter by description.
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[str]` — Filter by artifact group.
    
</dd>
</dl>

<dl>
<dd>

**global_id:** `typing.Optional[int]` — Filter by globalId.
    
</dd>
</dl>

<dl>
<dd>

**content_id:** `typing.Optional[int]` — Filter by contentId.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search.<a href="src/fern/search/client.py">artifacts_by_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of all artifacts with at least one version that matches the
posted content.
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

client = FernApi()
client.search.artifacts_by_content(
    artifact_type="AVRO",
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `FileContent` 
    
</dd>
</dl>

<dl>
<dd>

**canonical:** `typing.Optional[bool]` — Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the `artifactType` query parameter.
    
</dd>
</dl>

<dl>
<dd>

**artifact_type:** `typing.Optional[ArtifactType]` — Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the `canonical` query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of artifacts to return.  Defaults to 20.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SearchArtifactsByContentRequestOrder]` — Sort order, ascending (`asc`) or descending (`desc`).
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `typing.Optional[SearchArtifactsByContentRequestOrderby]` 

The field to sort by.  Can be one of:

* `name`
* `createdOn`
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.system.<a href="src/fern/system/client.py">get_system_info</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation retrieves information about the running registry system, such as the version
of the software and when it was built.
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

client = FernApi()
client.system.get_system_info()

```
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_resource_limits</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation retrieves the list of limitations on used resources, that are applied on the current instance of Registry.
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

client = FernApi()
client.system.get_resource_limits()

```
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_current_user_info</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the currently authenticated user.
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

client = FernApi()
client.users.get_current_user_info()

```
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

