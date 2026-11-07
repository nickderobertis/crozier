# Reference
## Base
<details><summary><code>client.base.<a href="src/fern/base/client.py">read</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

#### Returns
A JSON object with `meta` and `links` keys.

The `meta` key contains information such as a welcome message from the API, the specified version of the request, and the full representation of the current user, if authentication credentials were provided in the request.

The `links` key contains links to the following entity collections: [addons](#tag/Addons), [collections](), [institutions](#tag/Institutions), [licenses](#tag/Licenses), [registration schemas](#tag/Registration Schemas), [nodes](#tag/Nodes), [registrations](#tag/Registrations), [users](#tag/Users)
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.base.read()

```
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

## Logs
<details><summary><code>client.logs.<a href="src/fern/logs/client.py">actions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A log can have one of many actions. The complete list of loggable actions (in the format {identifier}: {description}) is as follows:
* `project_created`: A Node is created
* `project_registered`: A Node is registered
* `project_deleted`: A Node is deleted
* `created_from`: A Node is created using an existing Node as a template
* `pointer_created`: A Pointer is created
* `pointer_forked`: A Pointer is forked
* `pointer_removed`: A Pointer is removed
* `node_removed`: A component is deleted
* `node_forked`: A Node is forked
---
* `made_public`: A Node is made public
* `made_private`: A Node is made private
* `tag_added`: A tag is added to a Node
* `tag_removed`: A tag is removed from a Node
* `edit_title`: A Node's title is changed
* `edit_description`: A Node's description is changed
* `updated_fields`: One or more of a Node's fields are changed
* `external_ids_added`: An external identifier is added to a Node (e.g. DOI, ARK)
* `view_only_link_added`: A view-only link was added to a Node
* `view_only_link_removed`:  A view-only link was removed from a Node
---
* `contributor_added`: A Contributor is added to a Node
* `contributor_removed`: A Contributor is removed from a Node
* `contributors_reordered`: A Contributor's position in a Node's bibliography is changed
* `permissions_updated`: A Contributor`s permissions on a Node are changed
* `made_contributor_visible`: A Contributor is made bibliographically visible on a Node
* `made_contributor_invisible`: A Contributor is made bibliographically invisible on a Node
---
* `wiki_updated`: A Node's wiki is updated
* `wiki_deleted`: A Node's wiki is deleted
* `wiki_renamed`: A Node's wiki is renamed
* `made_wiki_public`: A Node's wiki is made public
* `made_wiki_private`: A Node's wiki is made private
---
* `addon_added`: An add-on is linked to a Node
* `addon_removed`: An add-on is unlinked from a Node
* `addon_file_moved`: A File in a Node's linked add-on is moved
* `addon_file_copied`: A File in a Node's linked add-on is copied
* `addon_file_renamed`: A File in a Node's linked add-on is renamed
* `node_authorized`: An addon is authorized for a project
* `node_deauthorized`: An addon is deauthorized for a project
* `folder_created`: A Folder is created in a Node's linked add-on
* `file_added`: A File is added to a Node's linked add-on
* `file_updated`: A File is updated on a Node's linked add-on
* `file_removed`: A File is removed from a Node's linked add-on
* `file_restored`: A File is restored in a Node's linked add-on
---
* `comment_added`: A Comment is added to some item
* `comment_removed`: A Comment is removed from some item
* `comment_updated`: A Comment is updated on some item
---
* `embargo_initiated`: An embargoed Registration is proposed on a Node
* `embargo_approved`: A proposed Embargo of a Node is approved
* `embargo_cancelled`: A proposed Embargo of a Node is cancelled
* `embargo_completed`: A proposed Embargo of a Node is completed
* `retraction_initiated`: A Withdrawal of a Registration is proposed
* `retraction_approved`: A Withdrawal of a Registration is approved
* `retraction_cancelled`: A Withdrawal of a Registration is cancelled
* `registration_initiated`: A Registration of a Node is proposed
* `registration_approved`: A proposed Registration is approved
* `registration_cancelled`: A proposed Registration is cancelled
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.actions()

```
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

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">read</a>(...) -> LogsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a log.
A log is permanent immutable record of a node's history. A log is created when a user performs one of many actions. See the [actions](#Logs_logs_actions) section for more details.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested log, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.read(
    log_id="log_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**log_id:** `str` — The unique identifier of the log you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Addons
<details><summary><code>client.addons.<a href="src/fern/addons/client.py">list</a>() -> typing.List[AddonsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of addons configurable with the OSF, for read purposes only.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Errors
This request should never return an error.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.addons.list()

```
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

## Citations
<details><summary><code>client.citations.<a href="src/fern/citations/client.py">styles_list</a>() -> typing.List[CitationsStylesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of all standard citation styles available for rendering citations.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 citation styles. Each resource in the array is a separate citation syle and contains the full representation of the citation style object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/citations/styles/?filter[title]=open.

Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`.
#### Errors
This request should never return an error.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.citations.styles_list()

```
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

<details><summary><code>client.citations.<a href="src/fern/citations/client.py">styles_read</a>(...) -> CitationsStylesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a citation style.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested citation style, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.citations.styles_read(
    style_id="style_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**style_id:** `str` — The unique identifier of the citation style.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collections
<details><summary><code>client.collections.<a href="src/fern/collections/client.py">list</a>() -> typing.List[CollectionsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list collections, either public or related to the user
#### Permissions
Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.

Comments on private nodes are only visible to contributors and administrators on the parent node.
#### Returns
Returns a JSON object containing `data` and `links` keys.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.list()

```
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

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">create</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list collections, either public or related to the user
#### Permissions
Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.

Comments on private nodes are only visible to contributors and administrators on the parent node.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.create(
    request={
        "data": {"attributes": {"title": "An Excellent Collection Title"}, "type": "collections"}
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

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">detail</a>(...) -> typing.List[CollectionsDetailResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a collection, if the user has appropriate permissions.

#### Permissions
Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.detail(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a collection, if the user has appropriate permissions.
#### Permissions
Users must have write permissions on a collection in order to delete it
#### Returns
Nothing is returned in the body
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.delete(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">metadata_registrations_list</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of user created metadata for entities within a collection.
#### Permissions
In order to view this metadata it must be public or a user must have read permissions for collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Errors
This request should never return an error.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.metadata_registrations_list(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">add_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of user created metadata for entities within a collection.
#### Permissions
To edit this collection a user must have collections write permissions
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.add_metadata(
    collection_id="collection_id",
    request={
        "application/json": {"data": {"attributes": {"guid": "test0", "subjects": "5fd228b7e64e1300aa99ee15", "volume": "test"}, "type": "collected-metadata"}}
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

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">metadata_registrations_detail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


#### Permissions
In order to view this metadata it must be public or a user must have read permissions for collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Errors
This request should never return an error.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.metadata_registrations_detail(
    collection_id="collection_id",
    cgm_id="cgm_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**cgm_id:** `str` — A short id for that piece of metadata
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">metadata_detail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of user created metadata for entities within a collection.
#### Permissions
To edit this collection a user must have collections write permissions
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.metadata_detail(
    collection_id="collection_id",
    cgm_id="cgm_id",
    request={
        "application/json": {"data": {"attributes": {"guid": "test0", "subjects": "5fd228b7e64e1300aa99ee15", "volume": "test"}, "type": "collected-metadata"}}
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

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**cgm_id:** `str` — A short id for that piece of metadata
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">metadata_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


#### Permissions
Only a user with collection admin permissions can delete collected metadata
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.metadata_delete(
    collection_id="collection_id",
    cgm_id="cgm_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**cgm_id:** `str` — A short id for that piece of metadata
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">metadata_subjects_relationships</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


#### Permissions
This is public for a logged out user when an entity is public.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.metadata_subjects_relationships(
    collection_id="collection_id",
    cgm_id="cgm_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**cgm_id:** `str` — A short id for that piece of metadata
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">metadata_subjects_relationships_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


#### Permissions
This is editable for a user with a write permission for this collection.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.metadata_subjects_relationships_update(
    collection_id="collection_id",
    cgm_id="cgm_id",
    request={
        "application/json": {"data": {"id": "5fd228b7e64e1300aa99ee15", "type": "subjects"}}
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

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**cgm_id:** `str` — A short id for that piece of metadata
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">collected_metadata</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


#### Permissions
In order to view these subject it must be a public collection or a user must have read permissions for collection.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Errors
This request should never return an error, other then permissions errors.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.collected_metadata(
    collection_id="collection_id",
    cgm_id="cgm_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**cgm_id:** `str` — A short id for that piece of metadata
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_nodes_list</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all nodes linked to the given collection.
#### Permissions
This returns all public nodes associated with this collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_nodes_list(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_nodes_relationships_create</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all the node ids linked to the given collection.
#### Permissions
This returns all public nodes associated with this collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_nodes_relationships_create(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_nodes_relationships</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allow users to a add a node to a collection by issuing a POST request.
#### Permissions
This returns all public nodes associated with this collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_nodes_relationships(
    collection_id="collection_id",
    request={
        "data": [{"id": "guid0", "type": "linked_nodes"}, {"id": "newid", "type": "linked_nodes"}, {"id": "test2", "type": "linked_nodes"}, {"id": "guid4", "type": "linked_nodes"}]
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

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_nodes_relationships_delete</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


This removes associated nodes from a collection
#### Permissions
Any user with write permissions on this collection should be to remove nodes from this collection.
#### Returns
Nothing in the response body.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_nodes_relationships_delete(
    collection_id="collection_id",
    request={
        "data": [{"id": "guid0", "type": "linked_nodes"}, {"id": "newid", "type": "linked_nodes"}, {"id": "test2", "type": "linked_nodes"}, {"id": "guid4", "type": "linked_nodes"}]
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

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_preprints_list</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all preprints linked to the given collection.
#### Permissions
This returns all public preprints associated with this collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_preprints_list(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_registrations_list</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all registrations linked to the given collection.
#### Permissions
This returns all public registrations associated with this collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_registrations_list(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_registrations_relationships_create</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all the registration ids linked to the given collection.
#### Permissions
This returns all public registrations associated with this collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of nodes ids.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_registrations_relationships_create(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_registrations_relationships</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allow users to a add a registration to a collection by issuing a POST request.
#### Permissions
This returns all public registrations associated with this collection.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_registrations_relationships(
    collection_id="collection_id",
    request={
        "data": [{"id": "guid0", "type": "linked_registrations"}, {"id": "newid", "type": "linked_registrations"}, {"id": "test2", "type": "linked_registrations"}, {"id": "guid4", "type": "linked_registrations"}]
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

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">linked_registrations_relationships_delete</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


This removes associated registrations from a collection
#### Permissions
Any user with write permissions on this collection should be to remove registrations from this collection.
#### Returns
Nothing in the response body.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.linked_registrations_relationships_delete(
    collection_id="collection_id",
    request={
        "data": [{"id": "guid0", "type": "linked_registrations"}, {"id": "newid", "type": "linked_registrations"}, {"id": "test2", "type": "linked_registrations"}, {"id": "guid4", "type": "linked_registrations"}]
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

**collection_id:** `str` — A short id for that collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Comments
<details><summary><code>client.comments.<a href="src/fern/comments/client.py">read</a>(...) -> CommentsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a comment
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested comment, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.comments.read(
    comment_id="comment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment_id:** `str` — The unique identifier of the comment you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified comment by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
#### Returns
Returns JSON with a `data` key containing the new representation of the updated comment, if the request is successful.

If the request is unsuccessful, JSON with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.comments.put(
    comment_id="comment_id",
    request={
        "data": {"attributes": {"content": "changed comment content"}, "id": "{comment_id}", "type": "comments"}
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

**comment_id:** `str` — The unique identifier of the comment you wish to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a comment. This action can be undone by setting deleted to False in a comment update request.
#### Returns
If the request is successful, no content is returned.

If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.comments.delete(
    comment_id="comment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment_id:** `str` — The unique identifier of the comment you wish to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Draft Registrations
<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">read</a>() -> DraftRegistrationsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all currently available Draft Registrations for that user.
#### Permissions
Only Draft Registration contributors may view draft registrations.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.read()

```
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

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">create</a>(...) -> DraftRegistrationsCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This creates a Draft Registration that can be used to edit and register research.
Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.
A Draft Registration created by this endpoint will not have a Project linked with it by default, but if the user includes a `branched_from` attribute in their Draft Registration creation payload with the value of the `branched_from` being guid of a Project they have permissions for the Draft Registration will be linked to the Project. If you linked your Draft Registration on a Project, your original Project remains editable and will now have the Draft Registration linked to it. 
#### Permissions
Any user can create a Draft Registration. If the `branched_from` attribute is provided, then the user must be an ADMIN contributor on the Project being registered.
#### Required
Required fields for creating a Draft Registration include:

&nbsp;&nbsp;&nbsp;&nbsp;`schema_id`
#### Returns
Returns a JSON object with a `data` key containing the representation of the created Draft Registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.draft_registrations import DraftRegistrationsCreateRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.create(
    attributes=DraftRegistrationsCreateRequestAttributes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `DraftRegistrationsCreateRequestAttributes` — The properties of the Draft Registration entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">retrieve_a_draft_registration</a>(...) -> GetDraftRegistrationsDraftIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a given Draft Registration
Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

If you based your Draft Registration on a Project, your original Project remains editable but will now have the Draft Registration linked to it.
#### Permissions
Only draft registration contributors may view draft registrations.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.retrieve_a_draft_registration(
    draft_id="draft_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">delete_a_draft_registration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a draft registration. A draft that has already been registered cannot be deleted.
#### Permissions
Only draft registration contributors with ADMIN permissions may delete draft registrations
#### Returns
If the request is successful, no content is returned.
If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.delete_a_draft_registration(
    draft_id="draft_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">update_a_draft_registration</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Draft Registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged. Note this will not register or change the machine state of a Draft Registration, it can only edit the Draft Registration's attributes prior to its registration.
#### Permissions
Only draft registration contributors may view draft registrations and only draft registration contributors with WRITE or ADMIN permissions may update draft registrations.
#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated draft registration, if the request is successful.
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.update_a_draft_registration(
    draft_id="draft_id",
    request={
        "data": {"attributes": {"registration_responses": {"summary": "Test Value"}, "title": "test title change"}, "id": "626ffc1ad90ebe0011fc7601", "type": "draft_registrations"}
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

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">draft_registration_contributors_list</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of all given Contributors for a Draft Registration.
Contributors are users who can make changes to the Draft Registration.
Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.draft_registration_contributors_list(
    draft_id="draft_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the Draft Registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">draft_registration_contributors_create</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a contributor to a Draft Registration, contributors can view, edit, register or delete a Draft Registration depending on their permissions.
Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
#### Permissions
Only project administrators can add contributors to a Draft Registration.
#### Required
A relationship object with a `data` key, containing the `users` type and valid user ID is required.
All attributes describing the relationship between the node and the user are optional.
#### Returns
Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.draft_registrations import DraftRegistrationContributorsCreateRequestRelationships

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.draft_registration_contributors_create(
    draft_id="draft_id",
    relationships=DraftRegistrationContributorsCreateRequestRelationships(
        user="user",
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

**draft_id:** `str` — The unique identifier of the Draft Registration.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `DraftRegistrationContributorsCreateRequestRelationships` — URLs to other entities or entity collections that have a relationship to the contributor entity.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[DraftRegistrationContributorsCreateRequestAttributes]` — The properties of the contributor entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">retreive_a_contributor_from_a_draft_registration</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a given contributor.

Contributors are users who can view or edit to the Draft Registrations.

Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.retreive_a_contributor_from_a_draft_registration(
    draft_id="draft_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the Draft Registration.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the Contributor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">retrieve_institutions_afilliated_with_a_draft_registration</a>(...) -> GetDraftRegistrationsDraftIdInstitutionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Once a properly authenticated user has marked their registration as affiliated with an institution, that institution and any others added will appear in this list.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.retrieve_institutions_afilliated_with_a_draft_registration(
    draft_id="draft_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">nodes_draft_registrations_subjects</a>(...) -> NodesDraftRegistrationsSubjectsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This retrieves a list of subjects associated with a Draft Registration. Subjects are formatted here in a flat paginated list, but are hierarchical and nested by specificity of subject matter.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.nodes_draft_registrations_subjects(
    draft_id="draft_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_registrations.<a href="src/fern/draft_registrations/client.py">nodes_draft_registrations_read</a>(...) -> NodesDraftRegistrationsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a given draft registration.
Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

Your original project remains editable but will now have the draft registration linked to it.
#### Permissions
Only project administrators may view draft registrations.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_registrations.nodes_draft_registrations_read(
    node_id="node_id",
    draft_id="draft_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.files.<a href="src/fern/files/client.py">detail</a>(...) -> typing.List[FilesDetailResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a file (or folder)
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
### Waterbutler API actions

Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).

#### Download (files)

To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.

#### Create Subfolder (folders)

You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.

#### Upload New File (folders)


  To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.


#### Update Existing File (file)

To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.

#### Rename (files, folders)

To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.

#### Move & Copy (files, folders)

Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name.
Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers.
If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.

#### Delete (file, folders)

To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.detail(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The unique identifier of the file you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified file by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
#### Returns
Returns JSON with a `data` key containing the new representation of the updated file, if the request is successful.

If the request is unsuccessful, JSON with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.patch(
    file_id="file_id",
    request={
        "data": {"attributes": {"name": "new file name.jpg"}, "id": "{file_id}", "type": "files"}
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

**file_id:** `str` — The unique identifier of the file you wish to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">versions</a>(...) -> typing.List[FilesVersionsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of all file versions.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 file versions. Each resource in the array is a separate file version object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.versions(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The unique identifier of the file from which you want to retrieve versions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">version_detail</a>(...) -> typing.List[FilesVersionDetailResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a file version
#### Returns

Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.version_detail(
    file_id="file_id",
    version_id="version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The unique identifier of the file from which you want to retrieve versions.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `str` — The file version number you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Institutions
<details><summary><code>client.institutions.<a href="src/fern/institutions/client.py">list</a>() -> typing.List[InstitutionsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of all verified institutions.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 institutions. Each resource in the array is a separate institution object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include institutions that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/?filter[id]=cos.

Institutions may be filtered by their `id`, `name`, and `auth_url`
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.institutions.list()

```
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

<details><summary><code>client.institutions.<a href="src/fern/institutions/client.py">detail</a>(...) -> typing.List[InstitutionsDetailResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of an institution
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested institution, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.institutions.detail(
    institution_id="institution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**institution_id:** `str` — The unique identifier of the institution you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.institutions.<a href="src/fern/institutions/client.py">node_list</a>(...) -> typing.List[InstitutionsNodeListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of all nodes affiliated with an institution.
#### Versioning
As of version `2.2`, affiliated components (in addition to affiliated top-level projects) are returned from this endpoint.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 nodes. Each resource in the array is a separate nodes object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
#### Filtering
You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/nodes?filter[title]=science.

Nodes may be filtered by their `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.institutions.node_list(
    institution_id="institution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**institution_id:** `str` — The unique identifier of the institution you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.institutions.<a href="src/fern/institutions/client.py">registration_list</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of all registrations affiliated with an institution.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 registrations. Each resource in the array is a separate users object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
#### Filtering
You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/registrations?filter[title]=science.

Registrations may be filtered by their  `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.institutions.registration_list(
    institution_id="institution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**institution_id:** `str` — The unique identifier of the institution you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.institutions.<a href="src/fern/institutions/client.py">users_list</a>(...) -> typing.List[InstitutionsUsersListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of all users affiliated with an institution.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 users. Each resource in the array is a separate users object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
#### Filtering
You can optionally request that the response only include users that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/users?filter[family_name]=Nosek.

Users may be filtered by their `id`, `full_name`, `given_name`, `middle_names`, and `family_name`
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.institutions.users_list(
    institution_id="institution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**institution_id:** `str` — The unique identifier of the institution you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Licenses
<details><summary><code>client.licenses.<a href="src/fern/licenses/client.py">read</a>(...) -> LicensesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a license.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested license, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.licenses.read(
    license_id="license_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**license_id:** `str` — The unique identifier of the license.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.licenses.<a href="src/fern/licenses/client.py">license_list</a>() -> typing.List[LicenseListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of licenses. The returned licenses are sorted by their name.
#### Returns
Returns a JSON object containing `data` and `links` keys.
The `data` key contains an array of 10 licenses. Each resource in the array is a separate license object and contains the full representation of the license, meaning additional requests to a license's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include licenses that match your filters by utilizing the `filter` query parameter, e.g. [https://api.osf.io/v2/licenses/?filter[name]=apache](https://api.osf.io/v2/licenses/?filter[name]=apache).

Licenses may be filtered by their `id`, and `name`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.licenses.license_list()

```
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

## Nodes
<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">list</a>() -> typing.List[NodesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of nodes, representing projects and components, on the OSF.

The returned nodes are those which are public or which the user has access to view.

The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.

Registrations cannot be accessed through this endpoint (use the [registrations](#tag/Registrations) endpoints instead).
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.

Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.list()

```
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

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new node.

On the OSF, nodes are considered **projects** or **components**. The difference between a project and a component is that a project is a top-level node, and a component is a child of a project.

Additionally, nodes have a `category` field that includes **project** as an option. The categorization determines what icon is displayed with the node on the OSF, and helps with search organization. Projects (top-level nodes) may have a category other than project, and components (children) may have a category of **project**.
#### Required
Required fields for creating a node include:

&nbsp;&nbsp;&nbsp;&nbsp`title`

&nbsp;&nbsp;&nbsp;&nbsp`category`

Note: Nodes default to **private** unless the `public` field is explicitly set to **true** in the request payload.
#### Returns
Returns a JSON object with a `data` key containing the representation of the created node, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.nodes import NodesCreateRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.create(
    attributes=NodesCreateRequestAttributes(
        category="analysis",
        title="title",
    ),
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

**attributes:** `NodesCreateRequestAttributes` — The properties of the node entity.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type identifier of the node entity (`nodes`).
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[NodesCreateRequestRelationships]` — URLs to other entities or entity collections that have a relationship to the node entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">read</a>(...) -> NodesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a given node (project or component).
#### Permissions
Only project contributors may retrieve the details of a private node. Attempting to retreive a private node for which you are not a contributor will result in a **403 Forbidden** response.

Authentication is not required to view the details of a public node, as public nodes give read-only access to everyone.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested node, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.read(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Permanently deletes a node. This action cannot be undone.
#### Permissions
Only project administrators may delete a node. Attempting to delete a node for which you are not an administrator will result in a **403 Forbidden** response.
#### Returns
If the request is successful, no content is returned.

If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.delete(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a node by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

Nodes can be updated with either a **PUT** or **PATCH** request. The `title` and `category` fields are mandatory in a **PUT** request, and optional in a **PATCH**.
#### Permissions
Only write contributors may update a node. Attempting to update a node for which you do not have write access will result in a **403 Forbidden** response.
#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated node, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.partial_update(
    node_id="node_id",
    request={
        "data": {"attributes": {"description": "An updated abstract.", "public": True, "tags": ["cancer biology", "reproducibility"]}, "id": "{node_id}", "type": "nodes"}
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

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">addons_list</a>(...) -> typing.List[NodesAddonsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of addons connected to the given node or project.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of at most 10 addon objects. Each resource in the array is a separate addon object and contains the full representation of the addon, meaning additional requests to a addon's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.addons_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">addon_read</a>(...) -> NodesAddonReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of an individual addon connected to this node.
#### Permissions
NodeSettings that are attached to public nodes will give read-only access to everyone. Private nodes require explicit read permission. Write and admin access are the same for public and private nodes. Administrators on a parent node have implicit read permissions for all child nodes.
Any users with write or admin access to the node are able to deauthorize an enabled addon, but only the addon authorizer is able to change the configuration (i.e. selected folder) of an already-configured NodeSettings entity.
#### Returns
Returns a JSON object with a `data` key containing the details of the requested addon, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.addon_read(
    node_id="node_id",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the addon.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">node_addon_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a node addon by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

Node addon can be updated with either a **PUT** or **PATCH** request. The `external_account_id`, `enabled`, and `folder_id` fields are mandatory in a **PUT**, and optional in **PATCH**. Non-string values will be accepted and stringified, however we make no promises about the stringification output.

To delete or deauthorize a node addon, issue a **PUT** with all fields set to `null` or `False`, or a **PATCH** with enabled set `False`.
#### Permissions
NodeSettings that are attached to public nodes will give read-only access to everyone. Private nodes require explicit read permission. Write and admin access are the same for public and private nodes. Administrators on a parent node have implicit read permissions for all child nodes.
Any users with write or admin access to the node are able to deauthorize an enabled addon, but only the addon authorizer is able to change the configuration (i.e. selected folder) of an already-configured NodeSettings entity.

#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated node addon, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.node_addon_update(
    node_id="node_id",
    provider="provider",
    request={
        "data": {"attributes": {"external_account_id": "{account_id}", "folder_id": "{folder_id}", "folder_path": "{folder_path}", "label": "{label}", "url": "{url}"}, "id": "{provider}", "type": "node_addons"}
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

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the addon.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">addons_folders_list</a>(...) -> typing.List[NodesAddonsFoldersListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of folders retrieved from the associated third-party (provider) service.
#### Permissions
Folders are visible only to the user that authorized the addon.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of addon folder objects. Each resource in the array is a separate addon folder object and contains the full representation of the addon folder, meaning additional requests to a addon folder's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.addons_folders_list(
    node_id="node_id",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">children_list</a>(...) -> typing.List[NodesChildrenListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of the next level child nodes for the given node. The returned nodes are sorted by their `date_modified`, with the most recently updated child nodes appearing first.

The list will include child nodes that are public, as well as child nodes that are private, if the authenticated user has permission to view them.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 child nodes. If the given node has zero child nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the child node, meaning additional requests to the child node's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/children/?filter[title]=reproducibility.

Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.children_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">children_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new child node.

Note: Creating a child node via this endpoint will function the same as creating a node via the node list endpoint, but the child node will have the given node set as its parent.
#### Permissions
Only write contributors may create children nodes.
#### Required
Required fields for creating a node include:

&nbsp;&nbsp;&nbsp;&nbsp`title`

&nbsp;&nbsp;&nbsp;&nbsp`category`

Note: nodes default to **private** unless the `public` field is explicitly set to **true** in the request payload.
#### Returns
Returns a JSON object with a `data` key containing the representation of the created node, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.nodes import NodesChildrenCreateRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.children_create(
    node_id="node_id",
    attributes=NodesChildrenCreateRequestAttributes(
        category="analysis",
        title="title",
    ),
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

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `NodesChildrenCreateRequestAttributes` — The properties of the node entity.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type identifier of the node entity (`nodes`).
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[NodesChildrenCreateRequestRelationships]` — URLs to other entities or entity collections that have a relationship to the node entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">citation_list</a>(...) -> NodesCitationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The citation details for a node, in CSL format.
#### Returns
Returns a JSON object with a `data` key that contains the representation of the details necessary for the node citation.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.citation_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">citation_read</a>(...) -> NodesCitationReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The citation for a node in a specific style.
#### Returns
Returns a JSON object with a `data` key that contains the representation of the node citation, in the requested style.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.citation_read(
    node_id="node_id",
    style_id="style_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**style_id:** `str` — The unique identifier of the citation style.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">comments_list</a>(...) -> typing.List[NodesCommentsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of comments related to a given node.

The returned comments are sorted by their creation date, with the most recent comments appearing first.
#### Permissions
Comments on public nodes are given read-only access to everyone.

If the node comment-level is `private`, only contributors have permission to comment.

If the comment-level is `public`, any logged-in OSF user can comment.

Comments on private nodes are only visible to contributors and administrators on the parent node.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/comments/?filter[target_id]=jg7sezmdnt93

Nodes may be filtered by their `deleted`, `target_id`, `date_created`, `date_modified`.

Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.comments_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">comment_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a comment on a given node overview page or a reply to a comment on that node.

To create a comment on the node overview page, the target `type` would be "nodes" and the target `id` would be the node `id`.

To reply to a comment on this node, the target `type` would be "comments" and the target `id` would be the `id` of the comment to reply to.
#### Required
A relationship object with a `data` key, containing the target (`comments` or `nodes`) type and a target `id` is required.
In addition, the `content` attribute describing the relationship between the node and the comment is required.
#### Returns
Returns a JSON object with a data key containing the representation of the new comment, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.comment_create(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node you want to comment on.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[NodesCommentCreateRequestAttributes]` — The properties of the comment entity.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[NodesCommentCreateRequestRelationships]` — URLs to other entities or entity collections that have a relationship to the comment entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">contributors_list</a>(...) -> typing.List[NodesContributorsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of the node's contributors, sorted by their index.

Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/y9jdt/contributors/?filter[bibliographic]=true.

Contributors may be filtered by their `bibliographic` and `permission` attributes.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.contributors_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">contributors_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a contributor to a node, effectively creating a relationship between the node and a user.

Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
#### Permissions
Only project administrators can add contributors to a node.
#### Required
A relationship object with a `data` key, containing the `users` type and valid user ID is required.

All attributes describing the relationship between the node and the user are optional.
#### Returns
Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.nodes import NodesContributorsCreateRequestRelationships

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.contributors_create(
    node_id="node_id",
    relationships=NodesContributorsCreateRequestRelationships(
        user="user",
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

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `NodesContributorsCreateRequestRelationships` — URLs to other entities or entity collections that have a relationship to the contributor entity.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[NodesContributorsCreateRequestAttributes]` — The properties of the contributor entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">contributors_read</a>(...) -> typing.List[NodesContributorsReadResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a given contributor.

Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.contributors_read(
    node_id="node_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">contributors_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a contributor from a node. This request only removes the relationship between the node and the user, it does not delete the user itself.

A node must always have at least one admin, and attempting to remove the only admin from a node will result in a **400 Bad Request** response.
#### Permissions
A user can remove themselves as a node contributor. Otherwise, only project administrators can remove contributors.
#### Returns
If the request is successful, no content is returned.

If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.contributors_delete(
    node_id="node_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">contributors_partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a contributor by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

Contributors can be updated with either a **PUT** or **PATCH** request. Since this endpoint has no mandatory attributes, PUT and PATCH are functionally the same.
#### Permissions
Only project administrators can update the contributors on a node.
#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated contributor, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

If the given user is not already in the contributor list, a 404 Not Found error will be returned. A node must always have at least one admin, and any attempt to downgrade the permissions of a sole admin will result in a 400 Bad Request error.
</dd>
</dl>
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
from fern.nodes import NodesContributorsPartialUpdateRequestRelationships

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.contributors_partial_update(
    node_id="node_id",
    user_id="user_id",
    relationships=NodesContributorsPartialUpdateRequestRelationships(
        user="user",
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

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `NodesContributorsPartialUpdateRequestRelationships` — URLs to other entities or entity collections that have a relationship to the contributor entity.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[NodesContributorsPartialUpdateRequestAttributes]` — The properties of the contributor entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">draft_registrations_list</a>(...) -> typing.List[NodesDraftRegistrationsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of all of the draft registrations of a given node.

Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

Your original project remains editable but will now have the draft registration linked to it.
#### Permissions
Only project administrators may view draft registrations.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 draft registrations. Each resource in the array is a separate draft registration object and contains the full representation of the draft registration, meaning additional requests to a draft registration's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.draft_registrations_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">draft_registrations_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate a draft registration of the current node.
Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

Your original project remains editable but will now have the draft registration linked to it.
#### Permissions
Only project administrators may view create registrations.
#### Required
Required fields for creating a draft registration include:

&nbsp;&nbsp;&nbsp;&nbsp;`schema_id`
#### Returns
Returns a JSON object with a `data` key containing the representation of the created draft registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.nodes import NodesDraftRegistrationsCreateRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.draft_registrations_create(
    node_id="node_id",
    attributes=NodesDraftRegistrationsCreateRequestAttributes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `NodesDraftRegistrationsCreateRequestAttributes` — The properties of the Draft Registration entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">draft_registrations_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a draft registration. A draft that has already been registered cannot be deleted.
#### Permissions
Only project administrators may delete draft registrations.
#### Returns
If the request is successful, no content is returned.

If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.draft_registrations_delete(
    node_id="node_id",
    draft_id="draft_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">draft_registrations_partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a draft registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

Draft Registrations contain Registration questions that will become part of the Registration. Answer the questions in the draft registration supplement by sending update requests until you are ready to submit the draft.

The registration supplement of a draft registration cannot be updated after the draft has been created.

When updating a draft registration, `registration_metadata` is required. It must be a dictionary with keys as question ids in the registration form, and values as nested dictionaries matching the specific format in the [registration schema](TODO: link me pls).

If a question is multiple-choice, the question response must exactly match one of the possible choices.
#### Permissions
Only project administrators may update draft registrations.
#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated draft registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.nodes import NodesDraftRegistrationsPartialUpdateRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.draft_registrations_partial_update(
    node_id="node_id",
    draft_id="draft_id",
    attributes=NodesDraftRegistrationsPartialUpdateRequestAttributes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**draft_id:** `str` — The unique identifier of the draft registration.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `NodesDraftRegistrationsPartialUpdateRequestAttributes` — The properties of the Draft Registration entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">providers_list</a>(...) -> typing.List[NodesProvidersListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all storage providers that are configured for this node

Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.


#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of files. Each resource in the array is a separate file object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.providers_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">providers_read</a>(...) -> NodesProvidersReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a storage provider enabled on this node.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.providers_read(
    node_id="node_id",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the storage provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">files_list</a>(...) -> typing.List[NodesFilesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all the files/folders that are attached to your project for a given storage provider.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

#### Filtering

You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/files/osfstorage/?filter[kind]=file

Node files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.

### Waterbutler API actions

Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).

#### Download (files)

To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.

#### Create Subfolder (folders)

You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.

#### Upload New File (folders)

To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.

#### Update Existing File (file)

To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.

#### Rename (files, folders)

To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.

#### Move & Copy (files, folders)

Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name.
Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers.
If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.

#### Delete (file, folders)

To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.files_list(
    node_id="node_id",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the storage provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">files_read</a>(...) -> NodesFilesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a file attached to given node (project or component) for the given storage provider.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.files_read(
    node_id="node_id",
    provider="provider",
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

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the storage provider.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The unique identifier of the file path.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">forks_list</a>(...) -> typing.List[NodesForksListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of the current node's forks. The returned fork nodes are sorted by their `forked_date`, with the most recently forked nodes appearing first.

Forking a project creates a copy of an existing node and all of its contents. The fork always points back to the original node, forming a network of nodes.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 forked nodes. If the current node has zero forked nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the forked node, meaning additional requests to the forked node's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.forks_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">forks_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a fork of the given node.

Forking a project creates a copy of an existing node and all of its contents. The fork always points back to the original node, forming a network of nodes.

You might use a fork to copy another's work to build on and extend. For example, a professor may create an OSF project of materials for individual student use. Each student forks the project to have his or her own copy of the materials to start his/her own work.

When creating a fork, your fork will only contain public components of the current node and components for which you are a contributor. Private components that you do not have access to will not be forked.
#### Required
There are no required attributes when creating a fork, as all of the forked node's attributes will be copied from the current node.

The `title` field is optional, with the default title being "Fork of " prepended to the current node's title.
#### Returns
Returns a JSON object with a `data` key containing the complete srepresentation of the forked node, if the request is successful.
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.nodes import NodesForksCreateRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.forks_create(
    node_id="node_id",
    attributes=NodesForksCreateRequestAttributes(
        category="analysis",
        title="title",
    ),
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

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `NodesForksCreateRequestAttributes` — The properties of the node entity.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type identifier of the node entity (`nodes`).
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[NodesForksCreateRequestRelationships]` — URLs to other entities or entity collections that have a relationship to the node entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">identifiers_list</a>(...) -> typing.List[NodesIdentifiersListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all identifiers associated with a given node.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering

You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/identifiers/?filter[category]=ark

Identifiers may be filtered by their `category` e.g `ark` or `doi`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.identifiers_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">institutions_list</a>(...) -> typing.List[NodesInstitutionsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all institutions affiliated with this node.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 affilited institutions. Each resource in the array is a separate institution object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.institutions_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">linked_nodes_list</a>(...) -> typing.List[NodesLinkedNodesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all nodes linked to the given node.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.

Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.linked_nodes_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">logs_list</a>(...) -> typing.List[NodesLogsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of all logs associated with a given node.

The returned logs are sorted by their `date`, with the most recents logs appearing first.

This list includes the logs of the specified node as well as the logs of that node's children to which the current user has read-only access.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/logs/?filter[action]=made_private.

Nodes may be filtered by their `action`, and `date`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.logs_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">preprints_list</a>(...) -> typing.List[NodesPreprintsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of preprints related to a given node. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.

**Note: This API endpoint is under active development, and is subject to change in the future.**
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 preprints. Each resource in the array is a separate preprint object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.preprints_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">registrations_list</a>(...) -> typing.List[NodesRegistrationsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all registrations of the given node.
#### Returns

Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 registrations. Each resource in the array is a separate registrations object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering

You can optionally request that the response only include registrations that match your filters by utilizing the filter query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.

Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.registrations_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">view_only_links_list</a>(...) -> typing.List[NodesViewOnlyLinksListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of view only links on a node.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

#### Permissions

View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.

#### Filtering

You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/view_only_links/?filter[anonymous]=true.

View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.view_only_links_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">view_only_links_read</a>(...) -> NodesViewOnlyLinksReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a view only link on a node.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
#### Permissions

View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.view_only_links_read(
    node_id="node_id",
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` — The unique identifier of the view only link.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">wikis_list</a>(...) -> typing.List[NodesWikisListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of wiki pages on a node.
#### Returns
Paginated list of the node's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.

Note that if an anonymous view_only key is being used, the user relationship will not be exposed.

If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
#### Filtering
Wiki pages can be filtered based on their `name` and `date_modified` fields.
+ `filter[name]=<Str>` -- filter wiki pages by name
+ `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.

Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.nodes.wikis_list(
    node_id="node_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — The unique identifier of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreprintProviders
<details><summary><code>client.preprint_providers.<a href="src/fern/preprint_providers/client.py">preprint_provider_list</a>() -> PreprintProviderListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of all preprint providers. The returned preprint providers are sorted by their creation date, with the most recent preprints appearing first.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include preprint providers that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/?filter[id]=osf.

Preprint Providers may be filtered by their `id`, `name`,  and `description`
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprint_providers.preprint_provider_list()

```
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

<details><summary><code>client.preprint_providers.<a href="src/fern/preprint_providers/client.py">preprint_provider_detail</a>(...) -> PreprintProviderDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a preprint provider.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested preprint provider, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

#### Acceptable Subjects Structure
Each preprint provider specifies acceptable subjects.
`subjects_acceptable` is an array found in `attributes`.
Subjects consist of general parent subjects (e.g., Engineering), more specific child subjects (e.g., Aerospace Engineering), and even more specific grandchild subjects (e.g., Aerodynamics and Fluid Mechanics). Subjects can only be nested 3 deep.


    "subjects_acceptable": [
        [
            [
                # Parent Subject:
                # Architecture
                "584240d954be81056ceca9e5",

                # Child Subject:
                # Architectural Engineering
                "584240da54be81056cecac87"
            ],
            # Include all Architectural Engineering's children:
            true
        ],
        [
            [
                # Parent Subject:
                # Engineering
                "584240da54be81056cecaca9",

                # Child Subject:
                # Aerospace Engineering
                "584240db54be81056cecacd6",

                # Grandchild Subject:
                # Aerodynamics and Fluid Mechanics
                "584240da54be81056cecaa74"
            ],
            # All nestings 3 deep must be false
            false
        ]
    ]

The above structure would allow Architecture, Architectural Engineering, all of Architectural Engineering's children, Engineering, Aerospace Engineering, and Aerodynamics and Fluid Mechanics.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprint_providers.preprint_provider_detail(
    preprint_provider_id="preprint_provider_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_provider_id:** `str` — The unique identifier of the preprint provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprint_providers.<a href="src/fern/preprint_providers/client.py">preprint_provider_licenses_list</a>(...) -> PreprintProviderLicensesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of the licenses allowed by a preprint provider.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprint_providers.preprint_provider_licenses_list(
    preprint_provider_id="preprint_provider_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_provider_id:** `str` — The unique identifier of the preprint provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprint_providers.<a href="src/fern/preprint_providers/client.py">preprints_list</a>(...) -> typing.List[PreprintProvidersPreprintsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of preprints from the specified preprint provider. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

The `links` key contains a dictionary with keys that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

#### Filtering
You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/osf/preprints/?filter[is_published]=true.

Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprint_providers.preprints_list(
    preprint_provider_id="preprint_provider_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_provider_id:** `str` — The unique identifier of the preprint provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprint_providers.<a href="src/fern/preprint_providers/client.py">preprint_provider_taxonomies_list</a>(...) -> PreprintProviderTaxonomiesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of the taxonomies for a preprint provider. The returned preprint providers taxonomies are sorted by their creation date, with the most recent preprints appearing first.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprint_providers.preprint_provider_taxonomies_list(
    preprint_provider_id="preprint_provider_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_provider_id:** `str` — The unique identifier of the preprint provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Preprints
<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">list</a>() -> typing.List[PreprintsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]=socarxiv.

Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.list()

```
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

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new preprint.
#### Returns
Returns a JSON object with a `data` key containing the representation of the created preprint, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.
</dd>
</dl>
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
from fern.preprints import PreprintsCreateRequestRelationships

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.create(
    relationships=PreprintsCreateRequestRelationships(
        node="node",
        primary_file="primary_file",
        provider="provider",
    ),
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

**relationships:** `PreprintsCreateRequestRelationships` — URLs to other entities or entity collections that have a relationship to the preprint entity.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type identifier of the preprint entity (`preprints`).
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[PreprintsCreateRequestAttributes]` — The properties of the preprint entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">read</a>(...) -> PreprintsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a preprint.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested preprint, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.read(
    preprint_id="preprint_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_id:** `str` — The unique identifier of the preprint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated preprint, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.partial_update(
    preprint_id="preprint_id",
    request={
        "data": {"attributes": {"doi": "{doi}"}, "id": "{preprint_id}", "relationships": {"primary_file": {"data": {"id": "{file_id}", "type": "primary_files"}}}}
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

**preprint_id:** `str` — The unique identifier of the preprint.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">bibliographic_contributors_list</a>(...) -> typing.List[PreprintsBibliographicContributorsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of the Preprint's Bibliographic Contributors, sorted by their index.
Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

Contributors may be filtered by their `bibliographic` and `permission` attributes.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.bibliographic_contributors_list(
    preprint_id="preprint_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_id:** `str` — The unique identifier of the preprint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">citation_list</a>(...) -> PreprintsCitationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The citation details for a preprint, in CSL format.
#### Returns
Returns a JSON object with a `data` key that contains the representation of the details necessary for the preprint citation.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.citation_list(
    preprint_id="preprint_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_id:** `str` — The unique identifier of the preprint whose citation you wish to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">citation_read</a>(...) -> PreprintsCitationReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The citation for a preprint in a specific style.
#### Returns
Returns a JSON object with a `data` key that contains the representation of the preprint citation, in the requested style.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.citation_read(
    preprint_id="preprint_id",
    style_id="style_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_id:** `str` — The unique identifier of the preprint.
    
</dd>
</dl>

<dl>
<dd>

**style_id:** `str` — The unique identifier of the citation style.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">contributors_list</a>(...) -> typing.List[PreprintsContributorsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of the Preprint's Contributors, sorted by their index.

Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

Contributors may be filtered by their `bibliographic` and `permission` attributes.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.contributors_list(
    preprint_id="preprint_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_id:** `str` — The unique identifier of the preprint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">contributors_create</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.

Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
#### Permissions
Only project administrators can add contributors to a Preprint.
#### Required
A relationship object with a `data` key, containing the `users` type and valid user ID is required.

All attributes describing the relationship between the Preprint and the user are optional.
#### Returns
Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.contributors_create(
    preprint_id="preprint_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_id:** `str` — The unique identifier of the Preprint.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[PreprintsContributorsCreateRequestAttributes]` — The properties of the contributor entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preprints.<a href="src/fern/preprints/client.py">contributor_read</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a contributor on this Preprint.
Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.preprints.contributor_read(
    preprint_id="preprint_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**preprint_id:** `str` — The unique identifier of the Preprint.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Registrations
<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">list</a>() -> typing.List[RegistrationsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of registrations on the OSF to which the user has access.

The returned registrations are those which are public or which the user has access to view.

Non-registered nodes cannot be accessed through this endpoint (use the [nodes](#Nodes_nodes_list) endpoints instead).

#### Registrations
A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.

Registrations can be made public immediately or embargoed for up to 4 years.

#### Withdrawals
Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.

Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.list()

```
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

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">read</a>(...) -> RegistrationsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a given registration.
#### Permissions
Only project contributors may retrieve the details of a registration that is embargoed, or has not yet been made public. Attempting to retrieve a private registration for which you are not a contributor will result in a **403 Forbidden** response.

Authentication is not required to view the details of a public registration, as public registrations give read-only access to everyone.
#### Registrations
A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.

Registrations can be made public immediately or embargoed for up to 4 years.

#### Withdrawals
Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.read(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a registration's privacy from **private** to **public**.

Registrations can be updated with either a **PUT** or **PATCH** request. The `public` field is the only field that can be modified on a registration

Registrations can only be turned from private to public, not vice versa.
#### Permissions
Only project administrators may update a registration.
#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated registration, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.partial_update(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">children_list</a>(...) -> typing.List[RegistrationsChildrenListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of children of a registration.

The list consists of the next level child registrations for the given registration. The returned registrations are sorted by their `date_modified`, with the most recently updated child registrations appearing first.

The list will include child registrations that are public, as well as child registrations that are private, if the authenticated user has permission to view them.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 child registrations. If the given registration has zero child registrations, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the child registration.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

#### Filtering
You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/children/?filter[title]=reproducibility.

Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

Most fields are string fields and will be filtered using simple substring matching. Public is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.children_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">citations_list</a>(...) -> typing.List[RegistrationsCitationsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of the registration's alternative citation styles

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 citation styles. Each resource in the array is a separate citation styles object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/citations/?filter[title]=open.

Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.citations_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">citation_read</a>(...) -> RegistrationsCitationReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the citation style details for a registration, in CSL format.
#### Returns
Returns a JSON object with a `data` key that contains the representation of the details necessary for the citation style.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.citation_read(
    registration_id="registration_id",
    citation_id="citation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**citation_id:** `str` — The unique identifier of the citation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">comments_list</a>(...) -> typing.List[RegistrationsCommentsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of the registration's comments.

The returned comments are sorted by their creation date, with the most recent comments appearing first.
#### Permissions
Comments of public registrations are given read-only access to everyone.

If the comment-level is `private`, only registration contributors have permission to comment.

If the comment-level is `public`, any logged-in OSF user can comment.

Comments of private registrations are only visible to contributors and administrators on the registration.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wuerf/comments/?filter[target]=wuerf

Comments may be filtered by their `deleted`, `target`, `date_created`, `date_modified`.

Most fields are string fields and will be filtered using simple substring matching. Deleted is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.comments_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">contributors_list</a>(...) -> typing.List[RegistrationsContributorsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of all contributors on this registration.
The returned contributors are sorted by their index.

Contributors are users who can make changes to the registration or, in the case of private registration, have read access to the registration.

Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed in the contributors list on the OSF, while non-bibliographic contributors are not.

Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 contributors. Each resource in the array contains the full representation of the contributor. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/contributors/?filter[bibliographic]=true.

Contributors may be filtered by their `bibliographic` and `permission` attributes.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.contributors_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">contributors_read</a>(...) -> typing.List[RegistrationsContributorsReadResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a contributor on this registration.

#### Returns
Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.contributors_read(
    registration_id="registration_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">providers_list</a>(...) -> typing.List[RegistrationsProvidersListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of storage providers enabled on the registration

Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.


#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 files. Each resource in the array is a separate file object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.providers_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">files_list</a>(...) -> typing.List[RegistrationsFilesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all the registration's files/folders for a given storage provider.

#### Returns

Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

#### Filtering

You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/files/osfstorage/?filter[kind]=file

Files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.files_list(
    registration_id="registration_id",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the storage provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">files_read</a>(...) -> RegistrationsFilesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a registration file for the given storage provider.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested registration file object, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.files_read(
    registration_id="registration_id",
    provider="provider",
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

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the storage provider.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The unique identifier of the file path.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">forks_list</a>(...) -> typing.List[RegistrationsForksListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of the registration’s forks

The returned forks are sorted by their `forked_date`, with the most recent forks appearing first.

Forking a registration creates a copy of an existing registration and all of its contents.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 forks. If the current registration has no fork, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the registration's fork.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.forks_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">forks_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a fork of the given registration.

Forking a project creates a copy of an existing registration and all of its contents. The fork always points back to the original registration, forming a network of registrations.

You might use a fork to copy another's work to build on and extend. For example, a professor may create an OSF project of materials for individual student use. Each student forks the project to have his or her own copy of the materials to start his/her own work.

When creating a fork, your fork will only contain public components of the current registration and components for which you are a contributor. Private components that you do not have access to will not be forked.
#### Required
There are no required attributes when creating a fork, as all of the forked registration's attributes will be copied from the current registration.

The `title` field is optional, with the default title being "Fork of " prepended to the current registration's title.
#### Returns
Returns a JSON object with a `data` key containing the complete representation of the forked registration, if the request is successful.
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.forks_create(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">identifiers_list</a>(...) -> typing.List[RegistrationsIdentifiersListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of the registration's identifiers.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering

You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/identifiers/?filter[category]=ark

Identifiers may be filtered by their `category` e.g `ark` or `doi`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.identifiers_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">institutions_list</a>(...) -> typing.List[RegistrationsInstitutionsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of institutions affiliated with the registration.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 affiliated institutions. Each resource in the array is a separate institution object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.institutions_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">linked_nodes_list</a>(...) -> typing.List[RegistrationsLinkedNodesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all nodes linked to the registration.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/linked_nodes/?filter[title]=reproducibility/?filter[title]=reproducibility.

Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.linked_nodes_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">logs_list</a>(...) -> typing.List[RegistrationsLogsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of the registration's logs.

The returned logs are sorted by their `date`, with the most recents logs appearing first.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/logs/?filter[action]=made_private.

Logs may be filtered by their `action`, and `date`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.logs_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">view_only_links_list</a>(...) -> typing.List[RegistrationsViewOnlyLinksListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of view only links created for this registration.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

#### Permissions

View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.

#### Filtering

You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/view_only_links/?filter[anonymous]=true.

View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.view_only_links_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">view_only_links_read</a>(...) -> RegistrationsViewOnlyLinksReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a view only link created from this registration.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
#### Permissions

View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.view_only_links_read(
    registration_id="registration_id",
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` — The unique identifier of the view only link.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registrations.<a href="src/fern/registrations/client.py">wikis_list</a>(...) -> typing.List[RegistrationsWikisListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of the registration's wiki pages
#### Returns
A list of all registration's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.

If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
#### Filtering
Wiki pages can be filtered based on their `name` and `date_modified` fields.
+ `filter[name]=<Str>` -- filter wiki pages by name
+ `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.

Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registrations.wikis_list(
    registration_id="registration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_id:** `str` — The unique identifier of the registration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Schema Responses
<details><summary><code>client.schema_responses.<a href="src/fern/schema_responses/client.py">list</a>() -> SchemaResponsesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This retrieves a paginated list of all active Schema Responses that are public.
#### Returns
Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Errors
This request should never return an error.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_responses.list()

```
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

<details><summary><code>client.schema_responses.<a href="src/fern/schema_responses/client.py">schema_response_ppost</a>(...) -> SchemaResponsePpostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint creates a new Schema Response with an `in_progress` state. A new response can only be created if the current schema response is in an `approved` state.
#### Returns
Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.schema_responses import SchemaResponsePpostRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_responses.schema_response_ppost(
    attributes=SchemaResponsePpostRequestAttributes(),
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

**attributes:** `SchemaResponsePpostRequestAttributes` — The properties of the Schema Response.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type identifier of the Schema Response (`schema-response`).
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[SchemaResponsePpostRequestLinks]` — URLs to alternative representations of the Schema Response entity.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[SchemaResponsePpostRequestRelationships]` — Links to other entities or entity collections that have a relationship to the file entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schema_responses.<a href="src/fern/schema_responses/client.py">read</a>(...) -> SchemaResponsesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This retrieves a single Schema response using it's id.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested Schema Response, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_responses.read(
    schema_response_id="schema_response_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_response_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schema_responses.<a href="src/fern/schema_responses/client.py">schema_response_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the `in_progress` state. Once a Schema Response is transitioned to an `approved` it is immutable and another Schema Response must be created to update the Schema Response for that registration.
#### Returns
Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_responses.schema_response_delete(
    schema_response_id="schema_response_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_response_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schema_responses.<a href="src/fern/schema_responses/client.py">schema_response_patch</a>(...) -> SchemaResponsePatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an `in_progress` state.
#### Returns
Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.schema_responses import SchemaResponsePatchRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_responses.schema_response_patch(
    schema_response_id="schema_response_id",
    attributes=SchemaResponsePatchRequestAttributes(),
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

**schema_response_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `SchemaResponsePatchRequestAttributes` — The properties of the Schema Response.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type identifier of the Schema Response (`schema-response`).
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[SchemaResponsePatchRequestLinks]` — URLs to alternative representations of the Schema Response entity.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[SchemaResponsePatchRequestRelationships]` — Links to other entities or entity collections that have a relationship to the file entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Schema Response Actions
<details><summary><code>client.schema_response_actions.<a href="src/fern/schema_response_actions/client.py">schema_response_action_read</a>(...) -> SchemaResponseActionReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This retrieves a paginated list of all Schema Response Actions created for a Schema Response.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_response_actions.schema_response_action_read(
    schema_response_id="schema_response_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_response_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schema_response_actions.<a href="src/fern/schema_response_actions/client.py">create_a_new_schema_response_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This creates a new Schema Response Action in order to trigger a state transition for a Schema Response.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_response_actions.create_a_new_schema_response_action(
    schema_response_id="schema_response_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_response_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schema_response_actions.<a href="src/fern/schema_response_actions/client.py">a_schema_response_action_from_a_schema_response</a>(...) -> GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a Schema Response Action by it's ID.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schema_response_actions.a_schema_response_action_from_a_schema_response(
    schema_response_id="schema_response_id",
    schema_response_action_id="schema_response_action_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_response_id:** `str` — The unique identifier of the Schema Response example `61b9cd62eb66180215222669`.
    
</dd>
</dl>

<dl>
<dd>

**schema_response_action_id:** `str` — The unique identifier of the Schema Response Action example `61b9eae1a7d8ac025c4c46d3`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Registration Schema Blocks
<details><summary><code>client.registration_schema_blocks.<a href="src/fern/registration_schema_blocks/client.py">schema_response_blocks_read</a>(...) -> SchemaResponseBlocksReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This returns a list of all the Registration Schema Blocks are contained in Registration Schema.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registration_schema_blocks.schema_response_blocks_read(
    schema_response_id="schema_response_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_response_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registration_schema_blocks.<a href="src/fern/registration_schema_blocks/client.py">retrieve_a_registration_schema_block</a>(...) -> GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This returns a Registration Schema Block by it's ID.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registration_schema_blocks.retrieve_a_registration_schema_block(
    schema_response_id="schema_response_id",
    schema_response_block_id="schema_response_block_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_response_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**schema_response_block_id:** `str` — The unique identifier of the Schema Response Block example `61b79f9eadbb5701424a2d5e`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Registration Schemas
<details><summary><code>client.registration_schemas.<a href="src/fern/registration_schemas/client.py">list</a>() -> RegistrationSchemasListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users.
#### Returns
Returns a JSON object containing `data` and `links` keys.
The `data` key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object.
The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Errors
This request should never return an error.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registration_schemas.list()

```
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

<details><summary><code>client.registration_schemas.<a href="src/fern/registration_schemas/client.py">registration_schema_read</a>(...) -> RegistrationSchemaReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
#### Errors
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registration_schemas.registration_schema_read(
    registration_schema_id="registration_schema_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_schema_id:** `str` — The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Taxonomies
<details><summary><code>client.taxonomies.<a href="src/fern/taxonomies/client.py">list</a>() -> typing.List[TaxonomiesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of all [bepress disciplines taxonomies](https://www.bepress.com/wp-content/uploads/2016/12/Digital-Commons-Disciplines-taxonomy-2017-01.pdf).
Note: this API endpoint is under active development, and is subject to change in the future.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 taxonomies. Each resource in the array is a separate taxonomy object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include taxonomies that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/taxonomies/?filter['id']='{taxonomy_id}'.

Taxonomies may be filtered by their `id`, `parents`, and `text`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.taxonomies.list()

```
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

<details><summary><code>client.taxonomies.<a href="src/fern/taxonomies/client.py">read</a>(...) -> TaxonomiesReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a taxonomy.
#### Returns

Returns a JSON object with a `data` key containing the representation of the requested taxonomy, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.taxonomies.read(
    taxonomy_id="taxonomy_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**taxonomy_id:** `str` — The unique identifier of the taxonomy.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">list</a>() -> typing.List[UsersListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of all users registered on the OSF. The returned users are sorted by their `date_registered`, with the most recently registered users appearing first.

The subroute `/users/me/` is a special endpoint that always points to the currently logged-in user.
#### Versioning
As of version `2.3`, merged users will not be returned from this endpoint.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 users. Each resource in the array is a separate users object and contains the full representation of the user, meaning additional requests to a user's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

This request should never return an error.
#### Filtering
You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/?filter[family_name]=Nosek.

Users may be filtered by their `id`, `full_name`, `given_name`, `middle_name`, or `family_name`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.list()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">read</a>(...) -> UsersReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a given users.

The returned information includes the user's bibliographic information and the date the user was registered.

Additionally, relationships to the list of institutions with which the user is affiliated, and to the list of nodes which the user contributes to (that the requesting user has permission to see) are returned.

If `me` is given as the `user_id` in the request path, the record of the currently logged-in user will be returned.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested user, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.read(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a user by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

Users can be updated with either a **PUT** or **PATCH** request. The `full_name` field is mandatory in a **PUT** request, and optional in a **PATCH**.

**Note**: if you make a PUT/PATCH request to the `/users/me/` endpoint, you must still provide your full user ID in the ID field of the request. We do not support using the `me` alias in request bodies at this time.
#### Returns
Returns a JSON object with a `data` key containing the new representation of the updated node, if the request is successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
from fern.users import UsersPartialUpdateRequestAttributes

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.users.partial_update(
    user_id="user_id",
    attributes=UsersPartialUpdateRequestAttributes(
        full_name="full_name",
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

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `UsersPartialUpdateRequestAttributes` — The properties of the user entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">addons_list</a>(...) -> typing.List[UsersAddonsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of authorized user addons

#### Permissions

User addons are visible only to the user that authorized the addon.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.addons_list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">addons_read</a>(...) -> UsersAddonsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of an authorized user addon

#### Permissions

User addons are visible only to the user that authorized the addon.

#### Returns
Returns a JSON object with a `data` key containing the representation of the requested user addon, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.addons_read(
    user_id="user_id",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the addon provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">addon_accounts_list</a>(...) -> typing.List[UsersAddonAccountsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


A paginated list of addon accounts authorized by this user.

#### Permissions

Addon accounts are visible only to the user that authorized the account.

#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of at most 10 addon account objects. Each resource in the array is a separate  addon account object and contains the full representation of the addon account.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.addon_accounts_list(
    user_id="user_id",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the addon provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">addon_accounts_read</a>(...) -> UsersAddonAccountsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of an addon account

#### Permissions

Addon accounts are visible only to the user that authorized the account.

#### Returns
Returns a JSON object with a `data` key containing the representation of the requested addon account, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.addon_accounts_read(
    user_id="user_id",
    provider="provider",
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — The unique identifier of the addon provider.
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The unique identifier of the addon account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">institutions_list</a>(...) -> typing.List[UsersInstitutionsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of institutions that the user is affiliated with.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 institutions. Each resource in the array is a complete institution object and contains the full representation of the institution, meaning additional requests to a institution's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.institutions_list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">nodes_list</a>(...) -> typing.List[UsersNodesListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of nodes that the user is a contributor to. The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.

If the user ID in the path is the same as the logged-in user, all nodes will be returned. Otherwise, only the user's public nodes will be returned.

User registrations are not available at this endpoint.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/nodes/?filter[title]=open.

Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.nodes_list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">preprints_list</a>(...) -> typing.List[UsersPreprintsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of preprints that the user contributes to. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 preprints. Each resource in the array is a complete preprint object and contains the full representation of the preprint, meaning additional requests to a preprint's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/preprints/?filter[provider]=psyarxiv.

Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.preprints_list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">registrations_list</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A paginated list of registrations that the user is a contributor to. The returned registrations are sorted by their `date_modified`, with the most recently updated registrations appearing first.

If the user ID in the path is the same as the logged-in user, all registrations will be returned. Otherwise, only the user's public registrations will be returned.

User nodes are not available at this endpoint.
#### Returns
Returns a JSON object containing `data` and `links` keys.

The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
#### Filtering
You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/registrations/?filter[title]=replication.

Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.registrations_list(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ViewOnlyLinks
<details><summary><code>client.view_only_links.<a href="src/fern/view_only_links/client.py">read</a>(...) -> ViewOnlyLinksReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details about a specific view only link.
#### Permissions
Only project administrators may retrieve the details of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.
If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.view_only_links.read(
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` — The unique identifier of the view only link.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.view_only_links.<a href="src/fern/view_only_links/client.py">node_list</a>(...) -> typing.List[ViewOnlyLinksNodeListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


The list of nodes which this view only link gives read-only access to.
#### Permissions
Only project administrators may retrieve the nodes of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response.
#### Returns
Returns a JSON object containing `data` and `links` keys.
The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.view_only_links.node_list(
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` — The unique identifier of the view only link.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Wikis
<details><summary><code>client.wikis.<a href="src/fern/wikis/client.py">wiki_read</a>(...) -> WikiReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details about a specific wiki.
A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node.
#### Returns
Returns a JSON object with a `data` key containing the representation of the requested wiki, if the request was successful.

If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.wikis.wiki_read(
    wiki_id="wiki_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wiki_id:** `str` — The unique identifier of the wiki.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wikis.<a href="src/fern/wikis/client.py">wiki_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the plaintext content of a wiki in markdown format.
#### Returns
Returns `text/markdown` of the wiki content itself.
If the request is unsuccessful, plaintext with the error message will be displayed.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.wikis.wiki_content(
    wiki_id="wiki_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wiki_id:** `str` — The unique identifier of the wiki.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

