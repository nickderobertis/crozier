# Reference
## core/avatar
<details><summary><code>client.core_avatar.<a href="src/fern/core_avatar/client.py">get_avatar_dark</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.core_avatar.get_avatar_dark(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**size:** `int` — Size of the avatar
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_avatar.<a href="src/fern/core_avatar/client.py">get_avatar</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.core_avatar.get_avatar(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**size:** `int` — Size of the avatar
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## core/guest_avatar
<details><summary><code>client.core_guest_avatar.<a href="src/fern/core_guest_avatar/client.py">get_avatar_dark</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.core_guest_avatar.get_avatar_dark(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_name:** `str` — The guest name, e.g. "Albert"
    
</dd>
</dl>

<dl>
<dd>

**size:** `str` — The desired avatar size, e.g. 64 for 64x64px
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_guest_avatar.<a href="src/fern/core_guest_avatar/client.py">get_avatar</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.core_guest_avatar.get_avatar(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_name:** `str` — The guest name, e.g. "Albert"
    
</dd>
</dl>

<dl>
<dd>

**size:** `str` — The desired avatar size, e.g. 64 for 64x64px
    
</dd>
</dl>

<dl>
<dd>

**dark_theme:** `typing.Optional[int]` — Return dark avatar
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreClientFlowLoginV2
<details><summary><code>client.core_client_flow_login_v2.<a href="src/fern/core_client_flow_login_v2/client.py">poll</a>(...) -> CoreLoginFlowV2Credentials</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_client_flow_login_v2.poll(
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

**token:** `str` — Token of the flow
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_client_flow_login_v2.<a href="src/fern/core_client_flow_login_v2/client.py">init</a>() -> CoreLoginFlowV2</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_client_flow_login_v2.init()

```
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

## CorePreview
<details><summary><code>client.core_preview.<a href="src/fern/core_preview/client.py">get_preview_by_file_id</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.core_preview.get_preview_by_file_id(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `typing.Optional[int]` — ID of the file
    
</dd>
</dl>

<dl>
<dd>

**x:** `typing.Optional[int]` — Width of the preview
    
</dd>
</dl>

<dl>
<dd>

**y:** `typing.Optional[int]` — Height of the preview
    
</dd>
</dl>

<dl>
<dd>

**a:** `typing.Optional[int]` — Not crop the preview
    
</dd>
</dl>

<dl>
<dd>

**force_icon:** `typing.Optional[int]` — Force returning an icon
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[str]` — How to crop the image
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_preview.<a href="src/fern/core_preview/client.py">get_preview</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.core_preview.get_preview(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[str]` — Path of the file
    
</dd>
</dl>

<dl>
<dd>

**x:** `typing.Optional[int]` — Width of the preview
    
</dd>
</dl>

<dl>
<dd>

**y:** `typing.Optional[int]` — Height of the preview
    
</dd>
</dl>

<dl>
<dd>

**a:** `typing.Optional[int]` — Not crop the preview
    
</dd>
</dl>

<dl>
<dd>

**force_icon:** `typing.Optional[int]` — Force returning an icon
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[str]` — How to crop the image
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreReference
<details><summary><code>client.core_reference.<a href="src/fern/core_reference/client.py">preview</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.core_reference.preview(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reference_id:** `str` — the reference cache key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreWipe
<details><summary><code>client.core_wipe.<a href="src/fern/core_wipe/client.py">check_wipe</a>(...) -> CoreWipeCheckWipe200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_wipe.check_wipe(
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

**token:** `str` — App password
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_wipe.<a href="src/fern/core_wipe/client.py">wipe_done</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_wipe.wipe_done(
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

**token:** `str` — App password
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreOcs
<details><summary><code>client.core_ocs.<a href="src/fern/core_ocs/client.py">get_capabilities</a>() -> CoreOcsGetCapabilities200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_ocs.get_capabilities()

```
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

## CoreNavigation
<details><summary><code>client.core_navigation.<a href="src/fern/core_navigation/client.py">get_apps_navigation</a>(...) -> CoreNavigationGetAppsNavigation200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_navigation.get_apps_navigation()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**absolute:** `typing.Optional[int]` — Rewrite URLs to absolute ones
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_navigation.<a href="src/fern/core_navigation/client.py">get_settings_navigation</a>(...) -> CoreNavigationGetAppsNavigation200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_navigation.get_settings_navigation()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**absolute:** `typing.Optional[int]` — Rewrite URLs to absolute ones
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreAutoComplete
<details><summary><code>client.core_auto_complete.<a href="src/fern/core_auto_complete/client.py">get</a>(...) -> CoreAutoCompleteGet200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_auto_complete.get(
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

**search:** `str` — Text to search for
    
</dd>
</dl>

<dl>
<dd>

**item_type:** `typing.Optional[str]` — Type of the items to search for
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `typing.Optional[str]` — ID of the items to search for
    
</dd>
</dl>

<dl>
<dd>

**sorter:** `typing.Optional[str]` — can be piped, top prio first, e.g.: "commenters|share-recipients"
    
</dd>
</dl>

<dl>
<dd>

**share_types:** `typing.Optional[str]` — Types of shares to search for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreWhatsNew
<details><summary><code>client.core_whats_new.<a href="src/fern/core_whats_new/client.py">get</a>() -> CoreWhatsNewGet200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_whats_new.get()

```
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

<details><summary><code>client.core_whats_new.<a href="src/fern/core_whats_new/client.py">dismiss</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_whats_new.dismiss(
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

**version:** `str` — Version to dismiss the changes for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreAppPassword
<details><summary><code>client.core_app_password.<a href="src/fern/core_app_password/client.py">get_app_password</a>() -> CoreAppPasswordGetAppPassword200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_app_password.get_app_password()

```
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

<details><summary><code>client.core_app_password.<a href="src/fern/core_app_password/client.py">rotate_app_password</a>() -> CoreAppPasswordGetAppPassword200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_app_password.rotate_app_password()

```
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

<details><summary><code>client.core_app_password.<a href="src/fern/core_app_password/client.py">delete_app_password</a>() -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_app_password.delete_app_password()

```
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

## CoreHoverCard
<details><summary><code>client.core_hover_card.<a href="src/fern/core_hover_card/client.py">get_user</a>(...) -> CoreHoverCardGetUser200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_hover_card.get_user(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreCollaborationResources
<details><summary><code>client.core_collaboration_resources.<a href="src/fern/core_collaboration_resources/client.py">search_collections</a>(...) -> CoreCollaborationResourcesSearchCollections200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_collaboration_resources.search_collections(
    filter="filter",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `str` — Filter collections
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_collaboration_resources.<a href="src/fern/core_collaboration_resources/client.py">list_collection</a>(...) -> CoreCollaborationResourcesListCollection200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_collaboration_resources.list_collection(
    collection_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `int` — ID of the collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_collaboration_resources.<a href="src/fern/core_collaboration_resources/client.py">add_resource</a>(...) -> CoreCollaborationResourcesListCollection200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_collaboration_resources.add_resource(
    collection_id=1000000,
    resource_type="resourceType",
    resource_id="resourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `int` — ID of the collection
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` — Name of the resource
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_collaboration_resources.<a href="src/fern/core_collaboration_resources/client.py">rename_collection</a>(...) -> CoreCollaborationResourcesListCollection200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_collaboration_resources.rename_collection(
    collection_id=1000000,
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `int` — ID of the collection
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — New name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_collaboration_resources.<a href="src/fern/core_collaboration_resources/client.py">remove_resource</a>(...) -> CoreCollaborationResourcesListCollection200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_collaboration_resources.remove_resource(
    collection_id=1000000,
    resource_type="resourceType",
    resource_id="resourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `int` — ID of the collection
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` — Name of the resource
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_collaboration_resources.<a href="src/fern/core_collaboration_resources/client.py">get_collections_by_resource</a>(...) -> CoreCollaborationResourcesSearchCollections200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_collaboration_resources.get_collections_by_resource(
    resource_type="resourceType",
    resource_id="resourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_type:** `str` — Type of the resource
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_collaboration_resources.<a href="src/fern/core_collaboration_resources/client.py">create_collection_on_resource</a>(...) -> CoreCollaborationResourcesListCollection200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_collaboration_resources.create_collection_on_resource(
    base_resource_type="baseResourceType",
    base_resource_id="baseResourceId",
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

**base_resource_type:** `str` — Type of the base resource
    
</dd>
</dl>

<dl>
<dd>

**base_resource_id:** `str` — ID of the base resource
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreReferenceApi
<details><summary><code>client.core_reference_api.<a href="src/fern/core_reference_api/client.py">resolve_one</a>(...) -> CoreReferenceApiResolveOne200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_reference_api.resolve_one(
    reference="reference",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reference:** `str` — Reference to resolve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_reference_api.<a href="src/fern/core_reference_api/client.py">resolve</a>(...) -> CoreReferenceApiResolveOne200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_reference_api.resolve(
    references="references",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**references:** `str` — References to resolve
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum amount of references to resolve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_reference_api.<a href="src/fern/core_reference_api/client.py">extract</a>(...) -> CoreReferenceApiResolveOne200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_reference_api.extract(
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `str` — Text to extract from
    
</dd>
</dl>

<dl>
<dd>

**resolve:** `typing.Optional[int]` — Resolve the references
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum amount of references to extract
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_reference_api.<a href="src/fern/core_reference_api/client.py">get_providers_info</a>() -> CoreReferenceApiGetProvidersInfo200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_reference_api.get_providers_info()

```
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

<details><summary><code>client.core_reference_api.<a href="src/fern/core_reference_api/client.py">touch_provider</a>(...) -> CoreReferenceApiTouchProvider200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_reference_api.touch_provider(
    provider_id="providerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_id:** `str` — ID of the provider
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `typing.Optional[int]` — Timestamp of the last usage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreProfileApi
<details><summary><code>client.core_profile_api.<a href="src/fern/core_profile_api/client.py">set_visibility</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_profile_api.set_visibility(
    target_user_id="targetUserId",
    param_id="paramId",
    visibility="visibility",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**param_id:** `str` — ID of the parameter
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `str` — New visibility
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreUnifiedSearch
<details><summary><code>client.core_unified_search.<a href="src/fern/core_unified_search/client.py">get_providers</a>(...) -> CoreUnifiedSearchGetProviders200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_unified_search.get_providers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from:** `typing.Optional[str]` — the url the user is currently at
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.core_unified_search.<a href="src/fern/core_unified_search/client.py">search</a>(...) -> CoreUnifiedSearchSearch200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_unified_search.search(
    provider_id="providerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_id:** `str` — ID of the provider
    
</dd>
</dl>

<dl>
<dd>

**term:** `typing.Optional[str]` — Term to search
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[int]` — Order of entries
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum amount of entries
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Offset for searching
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — The current user URL
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CoreTranslationApi
<details><summary><code>client.core_translation_api.<a href="src/fern/core_translation_api/client.py">languages</a>() -> CoreTranslationApiLanguages200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_translation_api.languages()

```
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

<details><summary><code>client.core_translation_api.<a href="src/fern/core_translation_api/client.py">translate</a>(...) -> CoreTranslationApiTranslate200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core_translation_api.translate(
    text="text",
    to_language="toLanguage",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `str` — Text to be translated
    
</dd>
</dl>

<dl>
<dd>

**to_language:** `str` — Language to translate to
    
</dd>
</dl>

<dl>
<dd>

**from_language:** `typing.Optional[str]` — Language to translate from
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Core
<details><summary><code>client.core.<a href="src/fern/core/client.py">get_status</a>() -> CoreStatus</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.core.get_status()

```
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

## cloud_federation_api/request_handler
<details><summary><code>client.cloud_federation_api_request_handler.<a href="src/fern/cloud_federation_api_request_handler/client.py">add_share</a>(...) -> CloudFederationApiAddShare</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cloud_federation_api_request_handler.add_share(
    share_with="shareWith",
    name="name",
    provider_id="providerId",
    owner="owner",
    protocol="protocol",
    share_type="shareType",
    resource_type="resourceType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**share_with:** `str` — The user who the share will be shared with
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The resource name (e.g. document.odt)
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `str` — Resource UID on the provider side
    
</dd>
</dl>

<dl>
<dd>

**owner:** `str` — Provider specific UID of the user who owns the resource
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `str` — e,.g. ['name' => 'webdav', 'options' => ['username' => 'john', 'permissions' => 31]]
    
</dd>
</dl>

<dl>
<dd>

**share_type:** `str` — 'group' or 'user' share
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` — 'file', 'calendar',...
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Share description
    
</dd>
</dl>

<dl>
<dd>

**owner_display_name:** `typing.Optional[str]` — Display name of the user who shared the item
    
</dd>
</dl>

<dl>
<dd>

**shared_by:** `typing.Optional[str]` — Provider specific UID of the user who shared the resource
    
</dd>
</dl>

<dl>
<dd>

**shared_by_display_name:** `typing.Optional[str]` — Display name of the user who shared the resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_federation_api_request_handler.<a href="src/fern/cloud_federation_api_request_handler/client.py">receive_notification</a>(...) -> typing.List[typing.Dict[str, typing.Any]]</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.cloud_federation_api_request_handler.receive_notification(
    notification_type="notificationType",
    resource_type="resourceType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notification_type:** `str` — Notification type, e.g. SHARE_ACCEPTED
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` — calendar, file, contact,...
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `typing.Optional[str]` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**notification:** `typing.Optional[str]` — The actual payload of the notification
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DashboardDashboardApi
<details><summary><code>client.dashboard_dashboard_api.<a href="src/fern/dashboard_dashboard_api/client.py">get_widgets</a>() -> DashboardDashboardApiGetWidgets200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dashboard_dashboard_api.get_widgets()

```
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

<details><summary><code>client.dashboard_dashboard_api.<a href="src/fern/dashboard_dashboard_api/client.py">get_widget_items</a>(...) -> DashboardDashboardApiGetWidgetItems200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dashboard_dashboard_api.get_widget_items()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since_ids:** `typing.Optional[str]` — Array indexed by widget Ids, contains date/id from which we want the new items
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit number of result items per widget
    
</dd>
</dl>

<dl>
<dd>

**widgets:** `typing.Optional[str]` — Limit results to specific widgets
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DavDirect
<details><summary><code>client.dav_direct.<a href="src/fern/dav_direct/client.py">get_url</a>(...) -> DavDirectGetUrl200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dav_direct.get_url(
    file_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `int` — ID of the file
    
</dd>
</dl>

<dl>
<dd>

**expiration_time:** `typing.Optional[int]` — Duration until the link expires
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FilesSharingShareInfo
<details><summary><code>client.files_sharing_share_info.<a href="src/fern/files_sharing_share_info/client.py">info</a>(...) -> FilesSharingShareInfo</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_share_info.info(
    t="t",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**t:** `str` — Token of the share
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password of the share
    
</dd>
</dl>

<dl>
<dd>

**dir:** `typing.Optional[str]` — Subdirectory to get info about
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — Maximum depth to get info about
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FilesSharingShareapi
<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">get_shares</a>(...) -> FilesSharingShareapiGetShares200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.get_shares()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shared_with_me:** `typing.Optional[str]` — Only get shares with the current user
    
</dd>
</dl>

<dl>
<dd>

**reshares:** `typing.Optional[str]` — Only get shares by the current user and reshares
    
</dd>
</dl>

<dl>
<dd>

**subfiles:** `typing.Optional[str]` — Only get all shares in a folder
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Get shares for a specific path
    
</dd>
</dl>

<dl>
<dd>

**include_tags:** `typing.Optional[str]` — Include tags in the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">create_share</a>(...) -> FilesSharingShareapiCreateShare200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.create_share()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `typing.Optional[str]` — Path of the share
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[int]` — Permissions for the share
    
</dd>
</dl>

<dl>
<dd>

**share_type:** `typing.Optional[int]` — Type of the share
    
</dd>
</dl>

<dl>
<dd>

**share_with:** `typing.Optional[str]` — The entity this should be shared with
    
</dd>
</dl>

<dl>
<dd>

**public_upload:** `typing.Optional[str]` — If public uploading is allowed
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password for the share
    
</dd>
</dl>

<dl>
<dd>

**send_password_by_talk:** `typing.Optional[str]` — Send the password for the share over Talk
    
</dd>
</dl>

<dl>
<dd>

**expire_date:** `typing.Optional[str]` — Expiry date of the share
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Note for the share
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label for the share (only used in link and email)
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[str]` — Additional attributes for the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">get_inherited_shares</a>(...) -> FilesSharingShareapiGetShares200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.get_inherited_shares(
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

**path:** `str` — Path all shares will be relative to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">pending_shares</a>() -> FilesSharingShareapiGetShares200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.pending_shares()

```
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

<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">get_share</a>(...) -> FilesSharingShareapiCreateShare200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.get_share(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**include_tags:** `typing.Optional[int]` — Include tags in the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">update_share</a>(...) -> FilesSharingShareapiCreateShare200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.update_share(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[int]` — New permissions
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — New password
    
</dd>
</dl>

<dl>
<dd>

**send_password_by_talk:** `typing.Optional[str]` — New condition if the password should be send over Talk
    
</dd>
</dl>

<dl>
<dd>

**public_upload:** `typing.Optional[str]` — New condition if public uploading is allowed
    
</dd>
</dl>

<dl>
<dd>

**expire_date:** `typing.Optional[str]` — New expiry date
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — New note
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — New label
    
</dd>
</dl>

<dl>
<dd>

**hide_download:** `typing.Optional[str]` — New condition if the download should be hidden
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[str]` — New additional attributes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">delete_share</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.delete_share(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_shareapi.<a href="src/fern/files_sharing_shareapi/client.py">accept_share</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareapi.accept_share(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FilesSharingDeletedShareapi
<details><summary><code>client.files_sharing_deleted_shareapi.<a href="src/fern/files_sharing_deleted_shareapi/client.py">list</a>() -> FilesSharingDeletedShareapiList200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_deleted_shareapi.list()

```
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

<details><summary><code>client.files_sharing_deleted_shareapi.<a href="src/fern/files_sharing_deleted_shareapi/client.py">undelete</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_deleted_shareapi.undelete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FilesSharingShareesapi
<details><summary><code>client.files_sharing_shareesapi.<a href="src/fern/files_sharing_shareesapi/client.py">search</a>(...) -> FilesSharingShareesapiSearch200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareesapi.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for
    
</dd>
</dl>

<dl>
<dd>

**item_type:** `typing.Optional[str]` — Limit to specific item types
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page offset for searching
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Limit amount of search results per page
    
</dd>
</dl>

<dl>
<dd>

**share_type:** `typing.Optional[str]` — Limit to specific share types
    
</dd>
</dl>

<dl>
<dd>

**lookup:** `typing.Optional[int]` — If a global lookup should be performed too
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_shareesapi.<a href="src/fern/files_sharing_shareesapi/client.py">find_recommended</a>(...) -> FilesSharingShareesapiFindRecommended200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_shareesapi.find_recommended(
    item_type="itemType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_type:** `str` — Limit to specific item types
    
</dd>
</dl>

<dl>
<dd>

**share_type:** `typing.Optional[str]` — Limit to specific share types
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FilesSharingRemote
<details><summary><code>client.files_sharing_remote.<a href="src/fern/files_sharing_remote/client.py">get_shares</a>() -> FilesSharingRemoteGetShares200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_remote.get_shares()

```
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

<details><summary><code>client.files_sharing_remote.<a href="src/fern/files_sharing_remote/client.py">get_open_shares</a>() -> FilesSharingRemoteGetShares200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_remote.get_open_shares()

```
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

<details><summary><code>client.files_sharing_remote.<a href="src/fern/files_sharing_remote/client.py">accept_share</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_remote.accept_share(
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

**id:** `int` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_remote.<a href="src/fern/files_sharing_remote/client.py">decline_share</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_remote.decline_share(
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

**id:** `int` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_remote.<a href="src/fern/files_sharing_remote/client.py">get_share</a>(...) -> FilesSharingRemoteGetShare200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_remote.get_share(
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

**id:** `int` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files_sharing_remote.<a href="src/fern/files_sharing_remote/client.py">unshare</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files_sharing_remote.unshare(
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

**id:** `int` — ID of the share
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Oauth2LoginRedirector
<details><summary><code>client.oauth2login_redirector.<a href="src/fern/oauth2login_redirector/client.py">authorize</a>(...) -> str</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.oauth2login_redirector.authorize(
    client_id="client_id",
    state="state",
    response_type="response_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — Client ID
    
</dd>
</dl>

<dl>
<dd>

**state:** `str` — State of the flow
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `str` — Response type for the flow
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Oauth2OauthApi
<details><summary><code>client.oauth2oauth_api.<a href="src/fern/oauth2oauth_api/client.py">get_token</a>(...) -> Oauth2OauthApiGetToken200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.oauth2oauth_api.get_token(
    grant_type="grant_type",
    code="code",
    refresh_token="refresh_token",
    client_id="client_id",
    client_secret="client_secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**grant_type:** `str` — Token type that should be granted
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — Code of the flow
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `str` — Refresh token
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — Client ID
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — Client secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProvisioningApiApps
<details><summary><code>client.provisioning_api_apps.<a href="src/fern/provisioning_api_apps/client.py">get_apps</a>(...) -> ProvisioningApiAppsGetApps200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_apps.get_apps()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Filter for enabled or disabled apps
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_apps.<a href="src/fern/provisioning_api_apps/client.py">get_app_info</a>(...) -> ProvisioningApiAppsGetAppInfo200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_apps.get_app_info(
    app="app",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_apps.<a href="src/fern/provisioning_api_apps/client.py">enable</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_apps.enable(
    app="app",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_apps.<a href="src/fern/provisioning_api_apps/client.py">disable</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_apps.disable(
    app="app",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProvisioningApiGroups
<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">get_groups</a>(...) -> ProvisioningApiGroupsGetGroups200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.get_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the amount of groups returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for searching for groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">add_group</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.add_group(
    groupid="groupid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**groupid:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**displayname:** `typing.Optional[str]` — Display name of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">get_groups_details</a>(...) -> ProvisioningApiGroupsGetGroupsDetails200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.get_groups_details()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the amount of groups returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for searching for groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">get_group_users</a>(...) -> ProvisioningApiGroupsGetGroupUsers200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.get_group_users(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">get_group_users_details</a>(...) -> ProvisioningApiGroupsGetGroupUsersDetails200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.get_group_users_details(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the amount of groups returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for searching for groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">get_sub_admins_of_group</a>(...) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.get_sub_admins_of_group(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">get_group</a>(...) -> ProvisioningApiGroupsGetGroupUsers200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.get_group(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">update_group</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.update_group(
    group_id="groupId",
    key="key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key to update, only 'displayname'
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — New value for the key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_groups.<a href="src/fern/provisioning_api_groups/client.py">delete_group</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_groups.delete_group(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProvisioningApiUsers
<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_users</a>(...) -> ProvisioningApiGroupsGetGroupUsers200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the amount of groups returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for searching for groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">add_user</a>(...) -> ProvisioningApiUsersAddUser200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.add_user(
    userid="userid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**userid:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password of the user
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Display name of the user
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email of the user
    
</dd>
</dl>

<dl>
<dd>

**groups:** `typing.Optional[str]` — Groups of the user
    
</dd>
</dl>

<dl>
<dd>

**subadmin:** `typing.Optional[str]` — Groups where the user is subadmin
    
</dd>
</dl>

<dl>
<dd>

**quota:** `typing.Optional[str]` — Quota of the user
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Language of the user
    
</dd>
</dl>

<dl>
<dd>

**manager:** `typing.Optional[str]` — Manager of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_users_details</a>(...) -> ProvisioningApiGroupsGetGroupUsersDetails200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_users_details()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the amount of groups returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for searching for groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">search_by_phone_numbers</a>(...) -> ProvisioningApiUsersSearchByPhoneNumbers200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.search_by_phone_numbers(
    location="location",
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

**location:** `str` — Location of the phone number (for country code)
    
</dd>
</dl>

<dl>
<dd>

**search:** `str` — Phone numbers to search for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_user</a>(...) -> ProvisioningApiUsersGetUser200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_user(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">edit_user</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.edit_user(
    user_id="userId",
    key="key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key that will be updated
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — New value for the key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">delete_user</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.delete_user(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_current_user</a>() -> ProvisioningApiUsersGetUser200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_current_user()

```
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

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_editable_fields</a>() -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_editable_fields()

```
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

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_editable_fields_for_user</a>(...) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_editable_fields_for_user(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">edit_user_multi_value</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.edit_user_multi_value(
    user_id="userId",
    collection_name="collectionName",
    key="key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Collection to update
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key that will be updated
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — New value for the key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">wipe_user_devices</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.wipe_user_devices(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">enable_user</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.enable_user(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">disable_user</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.disable_user(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_users_groups</a>(...) -> ProvisioningApiGroupsGetGroups200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_users_groups(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">add_to_group</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.add_to_group(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**groupid:** `typing.Optional[str]` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">remove_from_group</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.remove_from_group(
    user_id="userId",
    groupid="groupid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**groupid:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">get_user_sub_admin_groups</a>(...) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.get_user_sub_admin_groups(
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

**user_id:** `str` — ID if the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">add_sub_admin</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.add_sub_admin(
    user_id="userId",
    groupid="groupid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**groupid:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">remove_sub_admin</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.remove_sub_admin(
    user_id="userId",
    groupid="groupid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**groupid:** `str` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_users.<a href="src/fern/provisioning_api_users/client.py">resend_welcome_message</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_users.resend_welcome_message(
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

**user_id:** `str` — ID if the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProvisioningApiAppConfig
<details><summary><code>client.provisioning_api_app_config.<a href="src/fern/provisioning_api_app_config/client.py">get_apps</a>() -> ProvisioningApiAppConfigGetApps200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_app_config.get_apps()

```
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

<details><summary><code>client.provisioning_api_app_config.<a href="src/fern/provisioning_api_app_config/client.py">get_keys</a>(...) -> ProvisioningApiAppConfigGetApps200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_app_config.get_keys(
    app="app",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_app_config.<a href="src/fern/provisioning_api_app_config/client.py">get_value</a>(...) -> ProvisioningApiAppConfigGetValue200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_app_config.get_value(
    app="app",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID if the app
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key
    
</dd>
</dl>

<dl>
<dd>

**default_value:** `typing.Optional[str]` — Default returned value if the value is empty
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_app_config.<a href="src/fern/provisioning_api_app_config/client.py">set_value</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_app_config.set_value(
    app="app",
    key="key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key to update
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — New value for the key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_app_config.<a href="src/fern/provisioning_api_app_config/client.py">delete_key</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_app_config.delete_key(
    app="app",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProvisioningApiPreferences
<details><summary><code>client.provisioning_api_preferences.<a href="src/fern/provisioning_api_preferences/client.py">set_preference</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_preferences.set_preference(
    app_id="appId",
    config_key="configKey",
    config_value="configValue",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**config_key:** `str` — Key of the preference
    
</dd>
</dl>

<dl>
<dd>

**config_value:** `str` — New value
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_preferences.<a href="src/fern/provisioning_api_preferences/client.py">delete_preference</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_preferences.delete_preference(
    app_id="appId",
    config_key="configKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**config_key:** `str` — Key to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_preferences.<a href="src/fern/provisioning_api_preferences/client.py">set_multiple_preferences</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_preferences.set_multiple_preferences(
    app_id="appId",
    configs="configs",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**configs:** `str` — Key-value pairs of the preferences
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.provisioning_api_preferences.<a href="src/fern/provisioning_api_preferences/client.py">delete_multiple_preference</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.provisioning_api_preferences.delete_multiple_preference(
    app_id="appId",
    config_keys="configKeys",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**config_keys:** `str` — Keys to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SettingsLogSettings
<details><summary><code>client.settings_log_settings.<a href="src/fern/settings_log_settings/client.py">download</a>() -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint requires admin access
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.settings_log_settings.download()
```
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

## theming/theming
<details><summary><code>client.theming_theming.<a href="src/fern/theming_theming/client.py">get_theme_stylesheet</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.theming_theming.get_theme_stylesheet(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**theme_id:** `str` — ID of the theme
    
</dd>
</dl>

<dl>
<dd>

**plain:** `typing.Optional[int]` — Let the browser decide the CSS priority
    
</dd>
</dl>

<dl>
<dd>

**with_custom_css:** `typing.Optional[int]` — Include custom CSS
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theming_theming.<a href="src/fern/theming_theming/client.py">get_image</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.theming_theming.get_image(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the image
    
</dd>
</dl>

<dl>
<dd>

**use_svg:** `typing.Optional[int]` — Return image as SVG
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theming_theming.<a href="src/fern/theming_theming/client.py">get_manifest</a>(...) -> ThemingThemingGetManifest200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.theming_theming.get_manifest(
    app="app",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ThemingIcon
<details><summary><code>client.theming_icon.<a href="src/fern/theming_icon/client.py">get_favicon</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.theming_icon.get_favicon(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theming_icon.<a href="src/fern/theming_icon/client.py">get_touch_icon</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.theming_icon.get_touch_icon(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theming_icon.<a href="src/fern/theming_icon/client.py">get_themed_icon</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.theming_icon.get_themed_icon(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app:** `str` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**image:** `str` — image file name (svg required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ThemingUserTheme
<details><summary><code>client.theming_user_theme.<a href="src/fern/theming_user_theme/client.py">get_background</a>() -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.theming_user_theme.get_background()
```
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

<details><summary><code>client.theming_user_theme.<a href="src/fern/theming_user_theme/client.py">set_background</a>(...) -> ThemingBackground</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.theming_user_theme.set_background(
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — Type of background
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Path of the background image
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Color for the background
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theming_user_theme.<a href="src/fern/theming_user_theme/client.py">delete_background</a>() -> ThemingBackground</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.theming_user_theme.delete_background()

```
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

<details><summary><code>client.theming_user_theme.<a href="src/fern/theming_user_theme/client.py">enable_theme</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.theming_user_theme.enable_theme(
    theme_id="themeId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**theme_id:** `str` — the theme ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theming_user_theme.<a href="src/fern/theming_user_theme/client.py">disable_theme</a>(...) -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.theming_user_theme.disable_theme(
    theme_id="themeId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**theme_id:** `str` — the theme ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserStatusStatuses
<details><summary><code>client.user_status_statuses.<a href="src/fern/user_status_statuses/client.py">find_all</a>(...) -> UserStatusStatusesFindAll200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_statuses.find_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of statuses to find
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for finding statuses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_status_statuses.<a href="src/fern/user_status_statuses/client.py">find</a>(...) -> UserStatusStatusesFind200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_statuses.find(
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

**user_id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserStatusUserStatus
<details><summary><code>client.user_status_user_status.<a href="src/fern/user_status_user_status/client.py">get_status</a>() -> UserStatusUserStatusGetStatus200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_user_status.get_status()

```
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

<details><summary><code>client.user_status_user_status.<a href="src/fern/user_status_user_status/client.py">set_status</a>(...) -> UserStatusUserStatusGetStatus200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_user_status.set_status(
    status_type="statusType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status_type:** `str` — The new status type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_status_user_status.<a href="src/fern/user_status_user_status/client.py">set_predefined_message</a>(...) -> UserStatusUserStatusGetStatus200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_user_status.set_predefined_message(
    message_id="messageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `str` — ID of the predefined message
    
</dd>
</dl>

<dl>
<dd>

**clear_at:** `typing.Optional[int]` — When the message should be cleared
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_status_user_status.<a href="src/fern/user_status_user_status/client.py">set_custom_message</a>(...) -> UserStatusUserStatusGetStatus200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_user_status.set_custom_message()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status_icon:** `typing.Optional[str]` — Icon of the status
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — Message of the status
    
</dd>
</dl>

<dl>
<dd>

**clear_at:** `typing.Optional[int]` — When the message should be cleared
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_status_user_status.<a href="src/fern/user_status_user_status/client.py">clear_message</a>() -> CoreWhatsNewDismiss200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_user_status.clear_message()

```
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

<details><summary><code>client.user_status_user_status.<a href="src/fern/user_status_user_status/client.py">revert_status</a>(...) -> UserStatusUserStatusGetStatus200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_user_status.revert_status(
    message_id="messageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `str` — ID of the message to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserStatusPredefinedStatus
<details><summary><code>client.user_status_predefined_status.<a href="src/fern/user_status_predefined_status/client.py">find_all</a>() -> UserStatusPredefinedStatusFindAll200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_predefined_status.find_all()

```
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

## UserStatusHeartbeat
<details><summary><code>client.user_status_heartbeat.<a href="src/fern/user_status_heartbeat/client.py">heartbeat</a>(...) -> UserStatusUserStatusGetStatus200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_status_heartbeat.heartbeat(
    status="status",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status:** `str` — Only online, away
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WeatherStatusWeatherStatus
<details><summary><code>client.weather_status_weather_status.<a href="src/fern/weather_status_weather_status/client.py">set_mode</a>(...) -> CoreReferenceApiTouchProvider200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.weather_status_weather_status.set_mode(
    mode=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mode:** `int` — New mode
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.weather_status_weather_status.<a href="src/fern/weather_status_weather_status/client.py">use_personal_address</a>() -> WeatherStatusWeatherStatusUsePersonalAddress200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.weather_status_weather_status.use_personal_address()

```
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

<details><summary><code>client.weather_status_weather_status.<a href="src/fern/weather_status_weather_status/client.py">get_location</a>() -> WeatherStatusWeatherStatusGetLocation200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.weather_status_weather_status.get_location()

```
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

<details><summary><code>client.weather_status_weather_status.<a href="src/fern/weather_status_weather_status/client.py">set_location</a>(...) -> WeatherStatusWeatherStatusUsePersonalAddress200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.weather_status_weather_status.set_location()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `typing.Optional[str]` — Any approximative or exact address
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude in decimal degree format
    
</dd>
</dl>

<dl>
<dd>

**lon:** `typing.Optional[float]` — Longitude in decimal degree format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.weather_status_weather_status.<a href="src/fern/weather_status_weather_status/client.py">get_forecast</a>() -> WeatherStatusWeatherStatusGetForecast200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.weather_status_weather_status.get_forecast()

```
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

<details><summary><code>client.weather_status_weather_status.<a href="src/fern/weather_status_weather_status/client.py">get_favorites</a>() -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.weather_status_weather_status.get_favorites()

```
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

<details><summary><code>client.weather_status_weather_status.<a href="src/fern/weather_status_weather_status/client.py">set_favorites</a>(...) -> CoreReferenceApiTouchProvider200Response</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.weather_status_weather_status.set_favorites(
    favorites="favorites",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**favorites:** `str` — Favorite addresses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

