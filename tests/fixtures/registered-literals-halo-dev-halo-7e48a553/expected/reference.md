# Reference
## AttachmentV1Alpha1Console
<details><summary><code>client.attachment_v1alpha1console.<a href="src/fern/attachment_v1alpha1console/client.py">search_attachments</a>(...) -> AttachmentList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search attachments with pagination, sorting, keyword, grouping, and media type filters.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1console.search_attachments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**ungrouped:** `typing.Optional[bool]` — Filter attachments without group. This parameter will ignore group parameter.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword for searching.
    
</dd>
</dl>

<dl>
<dd>

**accepts:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Acceptable media types.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attachment_v1alpha1console.<a href="src/fern/attachment_v1alpha1console/client.py">external_transfer_attachment</a>(...) -> Attachment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an attachment by transferring a remote file from the provided URL to the specified storage policy.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1console.external_transfer_attachment(
    policy_name="policyName",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_name:** `str` — storage policy <code>metadata.name</code>
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — remote file URL to transfer into storage
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — custom file name
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — attachment group <code>metadata.name</code>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attachment_v1alpha1console.<a href="src/fern/attachment_v1alpha1console/client.py">upload_attachment</a>(...) -> Attachment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload an attachment from a multipart file with the specified storage policy and optional group.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1console.upload_attachment(
    file="example_file",
    policy_name="policyName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` — Attachment file.
    
</dd>
</dl>

<dl>
<dd>

**policy_name:** `str` — Storage policy <code>metadata.name</code>.
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — Attachment group <code>metadata.name</code>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attachment_v1alpha1console.<a href="src/fern/attachment_v1alpha1console/client.py">match_attachment_permalinks_for_console</a>(...) -> AttachmentPermalinkMatchList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Match URL strings against Attachment permalinks for console.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1console.match_attachment_permalinks_for_console(
    urls=[
        "urls"
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

**urls:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attachment_v1alpha1console.<a href="src/fern/attachment_v1alpha1console/client.py">upload_attachment_for_console</a>(...) -> Attachment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload attachment endpoint for console.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1console.upload_attachment_for_console(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The file to upload. If not provided, the url will be used.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — The filename to use when uploading from url. If not provided, the filename will be extracted from the url.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The url to upload from. If not provided, the file will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AuthProviderV1Alpha1Console
<details><summary><code>client.auth_provider_v1alpha1console.<a href="src/fern/auth_provider_v1alpha1console/client.py">list_auth_providers</a>() -> typing.List[ListedAuthProvider]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all auth providers
</dd>
</dl>
</dd>
</dl>

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

client.auth_provider_v1alpha1console.list_auth_providers()

```
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

<details><summary><code>client.auth_provider_v1alpha1console.<a href="src/fern/auth_provider_v1alpha1console/client.py">disable_auth_provider</a>(...) -> AuthProvider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables an auth provider
</dd>
</dl>
</dd>
</dl>

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

client.auth_provider_v1alpha1console.disable_auth_provider(
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

**name:** `str` — metadata.name of the auth provider to disable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth_provider_v1alpha1console.<a href="src/fern/auth_provider_v1alpha1console/client.py">enable_auth_provider</a>(...) -> AuthProvider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables an auth provider
</dd>
</dl>
</dd>
</dl>

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

client.auth_provider_v1alpha1console.enable_auth_provider(
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

**name:** `str` — metadata.name of the auth provider to enable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CategoryV1Alpha1Console
<details><summary><code>client.category_v1alpha1console.<a href="src/fern/category_v1alpha1console/client.py">list_category_tree</a>() -> typing.List[CategoryTreeNode]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Categories as a canonical tree for console category management.
</dd>
</dl>
</dd>
</dl>

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

client.category_v1alpha1console.list_category_tree()

```
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

<details><summary><code>client.category_v1alpha1console.<a href="src/fern/category_v1alpha1console/client.py">update_category_position</a>(...) -> typing.List[CategoryTreeNode]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move a Category within the Console category tree.
</dd>
</dl>
</dd>
</dl>

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

client.category_v1alpha1console.update_category_position(
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

**name:** `str` — Category metadata.name
    
</dd>
</dl>

<dl>
<dd>

**before_name:** `typing.Optional[str]` — target next sibling Category metadata.name, or null to append
    
</dd>
</dl>

<dl>
<dd>

**parent_name:** `typing.Optional[str]` — target parent Category metadata.name, or null for root
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CommentV1Alpha1Console
<details><summary><code>client.comment_v1alpha1console.<a href="src/fern/comment_v1alpha1console/client.py">list_comments</a>(...) -> ListedCommentList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List comments with pagination, sorting, keyword, and commenter filters.
</dd>
</dl>
</dd>
</dl>

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

client.comment_v1alpha1console.list_comments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword used to match the raw comment text.
    
</dd>
</dl>

<dl>
<dd>

**approved:** `typing.Optional[str]` — Approval state filter. When false, comments with pending replies are also included.
    
</dd>
</dl>

<dl>
<dd>

**owner_kind:** `typing.Optional[str]` — Kind of the commenter identity. Defaults to User when ownerName is provided.
    
</dd>
</dl>

<dl>
<dd>

**owner_name:** `typing.Optional[str]` — Name of the commenter identity to filter by.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comment_v1alpha1console.<a href="src/fern/comment_v1alpha1console/client.py">create_comment</a>(...) -> Comment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a comment for a subject. Console-created comments are created through the comment service with request IP and user agent captured.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Ref
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.comment_v1alpha1console.create_comment(
    content="content",
    raw="raw",
    subject_ref=Ref(
        group="group",
        kind="kind",
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

**content:** `str` — Rendered HTML content for the comment. Unsafe HTML is rejected.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `str` — Original comment text submitted by the editor.
    
</dd>
</dl>

<dl>
<dd>

**subject_ref:** `Ref` 
    
</dd>
</dl>

<dl>
<dd>

**allow_notification:** `typing.Optional[bool]` — Whether to notify the owner of future replies. Only an explicit false disables notifications.
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — Whether the comment should be hidden from normal display.
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[CommentEmailOwner]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comment_v1alpha1console.<a href="src/fern/comment_v1alpha1console/client.py">update_comment_content</a>(...) -> Comment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update only the body of an existing comment. Requires its current version.
</dd>
</dl>
</dd>
</dl>

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

client.comment_v1alpha1console.update_comment_content(
    name="name",
    content="content",
    raw="raw",
    version=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CommentContentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comment_v1alpha1console.<a href="src/fern/comment_v1alpha1console/client.py">create_reply</a>(...) -> Reply</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an approved reply under an existing comment.
</dd>
</dl>
</dd>
</dl>

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

client.comment_v1alpha1console.create_reply(
    name="name",
    content="content",
    raw="raw",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the comment to reply to.
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — Rendered HTML content for the reply. Unsafe HTML is rejected.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `str` — Original reply text submitted by the editor.
    
</dd>
</dl>

<dl>
<dd>

**allow_notification:** `typing.Optional[bool]` — Whether to notify the owner of future replies. Only an explicit false disables notifications.
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — Whether the reply should be hidden from normal display.
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[CommentEmailOwner]` 
    
</dd>
</dl>

<dl>
<dd>

**quote_reply:** `typing.Optional[str]` — Metadata name of the reply being quoted, if this reply quotes another reply.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IndicesV1Alpha1Console
<details><summary><code>client.indices_v1alpha1console.<a href="src/fern/indices_v1alpha1console/client.py">rebuild_all_indices</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a request to rebuild all search indices.
</dd>
</dl>
</dd>
</dl>

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

client.indices_v1alpha1console.rebuild_all_indices()

```
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

## MenuItemV1Alpha1Console
<details><summary><code>client.menu_item_v1alpha1console.<a href="src/fern/menu_item_v1alpha1console/client.py">list_menu_item_tree</a>(...) -> typing.List[MenuItemTreeNode]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List MenuItems as a canonical tree for console menu management.
</dd>
</dl>
</dd>
</dl>

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

client.menu_item_v1alpha1console.list_menu_item_tree(
    menu_name="menuName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**menu_name:** `str` — Menu metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.menu_item_v1alpha1console.<a href="src/fern/menu_item_v1alpha1console/client.py">update_menu_item_position</a>(...) -> typing.List[MenuItemTreeNode]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move a MenuItem within its owning Menu.
</dd>
</dl>
</dd>
</dl>

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

client.menu_item_v1alpha1console.update_menu_item_position(
    name="name",
    menu_name="menuName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — MenuItem metadata.name
    
</dd>
</dl>

<dl>
<dd>

**menu_name:** `str` — selected Menu metadata.name
    
</dd>
</dl>

<dl>
<dd>

**before_name:** `typing.Optional[str]` — target next sibling MenuItem metadata.name, or null to append
    
</dd>
</dl>

<dl>
<dd>

**parent_name:** `typing.Optional[str]` — target parent MenuItem metadata.name, or null for root
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MenuV1Alpha1Console
<details><summary><code>client.menu_v1alpha1console.<a href="src/fern/menu_v1alpha1console/client.py">delete_menu</a>(...) -> Menu</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Menu and MenuItems owned by the Menu.
</dd>
</dl>
</dd>
</dl>

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

client.menu_v1alpha1console.delete_menu(
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

**name:** `str` — Menu metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NotifierV1Alpha1Console
<details><summary><code>client.notifier_v1alpha1console.<a href="src/fern/notifier_v1alpha1console/client.py">fetch_sender_config</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch sender config of notifier
</dd>
</dl>
</dd>
</dl>

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

client.notifier_v1alpha1console.fetch_sender_config(
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

**name:** `str` — Notifier metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifier_v1alpha1console.<a href="src/fern/notifier_v1alpha1console/client.py">save_sender_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save sender config of notifier
</dd>
</dl>
</dd>
</dl>

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

client.notifier_v1alpha1console.save_sender_config(
    name="name",
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

**name:** `str` — Notifier metadata.name
    
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

<details><summary><code>client.notifier_v1alpha1console.<a href="src/fern/notifier_v1alpha1console/client.py">verify_email_sender_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify email sender config.
</dd>
</dl>
</dd>
</dl>

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

client.notifier_v1alpha1console.verify_email_sender_config()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Gets email display name.
    
</dd>
</dl>

<dl>
<dd>

**enable:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**encryption:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**host:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**port:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — Gets email sender address.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PluginV1Alpha1Console
<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">list_plugins</a>(...) -> PluginList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List plugins using query criteria and sort params
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.list_plugins()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword of plugin display name or description
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the plugin is enabled
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">fetch_css_bundle</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compatibility alias for the UI plugin CSS bundle.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.fetch_css_bundle()

```
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

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">fetch_js_bundle</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compatibility alias for the UI plugin JS bundle.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.fetch_js_bundle()

```
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

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">install_plugin_from_uri</a>(...) -> Plugin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Install a plugin from uri.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.install_plugin_from_uri(
    uri="uri",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InstallFromUriRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">install_plugin</a>(...) -> Plugin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Install a plugin by uploading a Jar file.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.install_plugin(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Plugin JAR file.
    
</dd>
</dl>

<dl>
<dd>

**preset_name:** `typing.Optional[str]` — Plugin preset name. Halo finds the plugin from plugin presets.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[InstallPluginRequestSource]` — Install source. Defaults to file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">fetch_plugin_json_config</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch converted json config of plugin by configured configMapName.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.fetch_plugin_json_config(
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

**name:** `str` — metadata.name of the plugin whose JSON config will be fetched.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">update_plugin_json_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the config of plugin setting.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.update_plugin_json_config(
    name="name",
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

**name:** `str` — metadata.name of the plugin whose JSON config will be updated.
    
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

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">change_plugin_running_state</a>(...) -> Plugin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the running state of a plugin by metadata.name.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.change_plugin_running_state(
    name="name",
    enable=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the plugin whose running state will be changed.
    
</dd>
</dl>

<dl>
<dd>

**enable:** `bool` — Whether the plugin should be enabled.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — Whether to change the state asynchronously.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">reload_plugin</a>(...) -> Plugin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reload a plugin by metadata.name.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.reload_plugin(
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

**name:** `str` — metadata.name of the plugin to reload.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">reset_plugin_config</a>(...) -> ConfigMap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset the configMap of plugin setting.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.reset_plugin_config(
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

**name:** `str` — metadata.name of the plugin whose setting config will be reset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">fetch_plugin_setting</a>(...) -> Setting</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch setting of plugin.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.fetch_plugin_setting(
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

**name:** `str` — metadata.name of the plugin whose setting will be fetched.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">upgrade_plugin</a>(...) -> Plugin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upgrade a plugin by uploading a Jar file
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.upgrade_plugin(
    name="name",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the plugin to upgrade.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Plugin JAR file.
    
</dd>
</dl>

<dl>
<dd>

**preset_name:** `typing.Optional[str]` — Plugin preset name. Halo finds the plugin from plugin presets.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[UpgradePluginRequestSource]` — Install source. Defaults to file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plugin_v1alpha1console.<a href="src/fern/plugin_v1alpha1console/client.py">upgrade_plugin_from_uri</a>(...) -> Plugin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upgrade a plugin from uri.
</dd>
</dl>
</dd>
</dl>

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

client.plugin_v1alpha1console.upgrade_plugin_from_uri(
    name="name",
    uri="uri",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the plugin to upgrade.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpgradeFromUriRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PostV1Alpha1Console
<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">list_posts</a>(...) -> ListedPostList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List posts with pagination, sorting, keyword, publish phase, and category filters.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.list_posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**publish_phase:** `typing.Optional[ListPostsRequestPublishPhase]` — Filter posts by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword used to match post title, slug, or excerpt.
    
</dd>
</dl>

<dl>
<dd>

**category_with_children:** `typing.Optional[str]` — Category metadata name used to include posts in that category and its child categories.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">draft_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a draft post together with its initial content.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ContentUpdateParam, Post, Metadata, PostSpec, Excerpt, PostSpecVisible
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_v1alpha1console.draft_post(
    content=ContentUpdateParam(
        content="content",
        raw="raw",
        raw_type="rawType",
    ),
    post=Post(
        api_version="apiVersion",
        kind="kind",
        metadata=Metadata(
            name="name",
        ),
        spec=PostSpec(
            allow_comment=True,
            deleted=True,
            excerpt=Excerpt(
                auto_generate=True,
            ),
            pinned=True,
            priority=1,
            publish=True,
            slug="slug",
            title="title",
            visible=PostSpecVisible.PUBLIC,
        ),
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

**request:** `PostRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">update_draft_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update post metadata, spec, and content in one request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ContentUpdateParam, Post, Metadata, PostSpec, Excerpt, PostSpecVisible
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_v1alpha1console.update_draft_post(
    name="name",
    content=ContentUpdateParam(
        content="content",
        raw="raw",
        raw_type="rawType",
    ),
    post=Post(
        api_version="apiVersion",
        kind="kind",
        metadata=Metadata(
            name="name",
        ),
        spec=PostSpec(
            allow_comment=True,
            deleted=True,
            excerpt=Excerpt(
                auto_generate=True,
            ),
            pinned=True,
            priority=1,
            publish=True,
            slug="slug",
            title="title",
            visible=PostSpecVisible.PUBLIC,
        ),
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

**name:** `str` — metadata.name of the post to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">fetch_post_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a post content snapshot reconstructed from its base snapshot.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.fetch_post_content(
    name="name",
    snapshot_name="snapshotName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the post.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `str` — Content snapshot metadata.name to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">update_post_content</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update only the content of an existing post.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.update_post_content(
    name="name",
    content="content",
    raw="raw",
    raw_type="rawType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the post whose content will be updated.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Content` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">delete_post_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a content snapshot from a post and return the deleted content.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.delete_post_content(
    name="name",
    snapshot_name="snapshotName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the post.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `str` — Content snapshot metadata.name to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">fetch_post_head_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the editable head content of a post.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.fetch_post_head_content(
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

**name:** `str` — metadata.name of the post.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">publish_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a post. By default, the request waits until the release snapshot is available.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.publish_post(
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

**name:** `str` — metadata.name of the post to publish.
    
</dd>
</dl>

<dl>
<dd>

**head_snapshot:** `typing.Optional[str]` — Snapshot metadata.name to publish. Defaults to the current base snapshot when no head snapshot exists.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — Whether to return immediately after marking the post for publishing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">recycle_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move a post to the recycle bin by marking it as deleted.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.recycle_post(
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

**name:** `str` — metadata.name of the post to recycle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">fetch_post_release_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the released content currently served for a published post.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.fetch_post_release_content(
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

**name:** `str` — metadata.name of the post.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">revert_to_specified_snapshot_for_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore the post content from a specified snapshot.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.revert_to_specified_snapshot_for_post(
    name="name",
    snapshot_name="snapshotName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the post whose content will be restored.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `str` — snapshot <code>metadata.name</code> to restore as the post's head content
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">list_post_snapshots</a>(...) -> typing.List[ListedSnapshotDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List content snapshots for a post.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.list_post_snapshots(
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

**name:** `str` — metadata.name of the post.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1console.<a href="src/fern/post_v1alpha1console/client.py">unpublish_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpublish a post so it is no longer served as published content.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1console.unpublish_post(
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

**name:** `str` — metadata.name of the post to unpublish.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ReplyV1Alpha1Console
<details><summary><code>client.reply_v1alpha1console.<a href="src/fern/reply_v1alpha1console/client.py">list_replies</a>(...) -> ListedReplyList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List replies for a comment with pagination, sorting, labels, and field selectors.
</dd>
</dl>
</dd>
</dl>

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

client.reply_v1alpha1console.list_replies(
    comment_name="commentName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment_name:** `str` — Metadata name of the comment whose replies should be listed.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reply_v1alpha1console.<a href="src/fern/reply_v1alpha1console/client.py">update_reply_content</a>(...) -> Reply</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update only the body of an existing reply. Requires its current version.
</dd>
</dl>
</dd>
</dl>

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

client.reply_v1alpha1console.update_reply_content(
    name="name",
    content="content",
    raw="raw",
    version=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CommentContentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SinglePageV1Alpha1Console
<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">list_single_pages</a>(...) -> ListedSinglePageList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List single pages with pagination, sorting, keyword, publish phase, visibility, and contributor filters.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.list_single_pages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**contributor:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Contributor user names used to filter single pages. A page matches when any listed contributor appears in status.contributors.
    
</dd>
</dl>

<dl>
<dd>

**publish_phase:** `typing.Optional[ListSinglePagesRequestPublishPhase]` — Filter single pages by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.
    
</dd>
</dl>

<dl>
<dd>

**visible:** `typing.Optional[ListSinglePagesRequestVisible]` — Filter single pages by visibility, such as PUBLIC, INTERNAL, or PRIVATE.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword used to match single page title, slug, or excerpt.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">draft_single_page</a>(...) -> SinglePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a draft single page together with its initial content.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ContentUpdateParam, SinglePage, Metadata, SinglePageSpec, Excerpt, SinglePageSpecVisible
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.single_page_v1alpha1console.draft_single_page(
    content=ContentUpdateParam(
        content="content",
        raw="raw",
        raw_type="rawType",
    ),
    page=SinglePage(
        api_version="apiVersion",
        kind="kind",
        metadata=Metadata(
            name="name",
        ),
        spec=SinglePageSpec(
            allow_comment=True,
            deleted=True,
            excerpt=Excerpt(
                auto_generate=True,
            ),
            pinned=True,
            priority=1,
            publish=True,
            slug="slug",
            title="title",
            visible=SinglePageSpecVisible.PUBLIC,
        ),
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

**request:** `SinglePageRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">update_draft_single_page</a>(...) -> SinglePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update single page metadata, spec, and content in one request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ContentUpdateParam, SinglePage, Metadata, SinglePageSpec, Excerpt, SinglePageSpecVisible
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.single_page_v1alpha1console.update_draft_single_page(
    name="name",
    content=ContentUpdateParam(
        content="content",
        raw="raw",
        raw_type="rawType",
    ),
    page=SinglePage(
        api_version="apiVersion",
        kind="kind",
        metadata=Metadata(
            name="name",
        ),
        spec=SinglePageSpec(
            allow_comment=True,
            deleted=True,
            excerpt=Excerpt(
                auto_generate=True,
            ),
            pinned=True,
            priority=1,
            publish=True,
            slug="slug",
            title="title",
            visible=SinglePageSpecVisible.PUBLIC,
        ),
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

**name:** `str` — metadata.name of the single page to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SinglePageRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">fetch_single_page_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a single page content snapshot reconstructed from its base snapshot.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.fetch_single_page_content(
    name="name",
    snapshot_name="snapshotName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the single page.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `str` — Content snapshot metadata.name to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">update_single_page_content</a>(...) -> SinglePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update only the content of an existing single page.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.update_single_page_content(
    name="name",
    content="content",
    raw="raw",
    raw_type="rawType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the single page whose content will be updated.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Content` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">delete_single_page_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a content snapshot from a single page and return the deleted content.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.delete_single_page_content(
    name="name",
    snapshot_name="snapshotName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the single page.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `str` — Content snapshot metadata.name to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">fetch_single_page_head_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the editable head content of a single page.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.fetch_single_page_head_content(
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

**name:** `str` — metadata.name of the single page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">publish_single_page</a>(...) -> SinglePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a single page. By default, the request waits until the release snapshot is available.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.publish_single_page(
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

**name:** `str` — metadata.name of the single page to publish.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — Whether to return immediately after marking the single page for publishing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">fetch_single_page_release_content</a>(...) -> ContentWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the released content currently served for a published single page.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.fetch_single_page_release_content(
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

**name:** `str` — metadata.name of the single page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">revert_to_specified_snapshot_for_single_page</a>(...) -> SinglePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore the single page content from a specified snapshot.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.revert_to_specified_snapshot_for_single_page(
    name="name",
    snapshot_name="snapshotName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the single page whose content will be restored.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `str` — snapshot <code>metadata.name</code> to restore as the single page's head content
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_page_v1alpha1console.<a href="src/fern/single_page_v1alpha1console/client.py">list_single_page_snapshots</a>(...) -> typing.List[ListedSnapshotDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List content snapshots for a single page.
</dd>
</dl>
</dd>
</dl>

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

client.single_page_v1alpha1console.list_single_page_snapshots(
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

**name:** `str` — metadata.name of the single page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SystemV1Alpha1Console
<details><summary><code>client.system_v1alpha1console.<a href="src/fern/system_v1alpha1console/client.py">get_stats</a>() -> DashboardStats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get stats.
</dd>
</dl>
</dd>
</dl>

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

client.system_v1alpha1console.get_stats()

```
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

## TagV1Alpha1Console
<details><summary><code>client.tag_v1alpha1console.<a href="src/fern/tag_v1alpha1console/client.py">list_post_tags</a>(...) -> TagList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List post tags with pagination, sorting, and keyword filtering.
</dd>
</dl>
</dd>
</dl>

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

client.tag_v1alpha1console.list_post_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword used to match the tag display name or slug.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ThemeV1Alpha1Console
<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">list_themes</a>(...) -> ThemeList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List themes.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.list_themes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**uninstalled:** `typing.Optional[bool]` — Whether to list uninstalled themes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">fetch_activated_theme</a>() -> Theme</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the activated theme.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.fetch_activated_theme()

```
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

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">install_theme_from_uri</a>(...) -> Theme</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Install a theme from uri.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.install_theme_from_uri(
    uri="uri",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InstallFromUriRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">install_theme</a>() -> Theme</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Install a theme by uploading a zip file.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.install_theme()

```
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

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">activate_theme</a>(...) -> Theme</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activate a theme by metadata.name.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.activate_theme(
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

**name:** `str` — metadata.name of the theme to activate.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">invalidate_cache</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate theme template cache.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.invalidate_cache(
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

**name:** `str` — metadata.name of the theme whose template cache will be invalidated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">fetch_theme_json_config</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch converted json config of theme by configured configMapName.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.fetch_theme_json_config(
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

**name:** `str` — metadata.name of the theme whose JSON config will be fetched.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">update_theme_json_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the configMap of theme setting.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.update_theme_json_config(
    name="name",
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

**name:** `str` — metadata.name of the theme whose JSON config will be updated.
    
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

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">reload</a>(...) -> Theme</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reload theme setting.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.reload(
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

**name:** `str` — metadata.name of the theme to reload.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">reset_theme_config</a>(...) -> ConfigMap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset the configMap of theme setting.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.reset_theme_config(
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

**name:** `str` — metadata.name of the theme whose setting config will be reset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">fetch_theme_setting</a>(...) -> Setting</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch setting of theme.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.fetch_theme_setting(
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

**name:** `str` — metadata.name of the theme whose setting will be fetched.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">upgrade_theme</a>(...) -> Theme</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upgrade theme
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.upgrade_theme(
    name="name",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the theme to upgrade.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — Theme zip file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.theme_v1alpha1console.<a href="src/fern/theme_v1alpha1console/client.py">upgrade_theme_from_uri</a>(...) -> Theme</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upgrade a theme from uri.
</dd>
</dl>
</dd>
</dl>

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

client.theme_v1alpha1console.upgrade_theme_from_uri(
    name="name",
    uri="uri",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the theme to upgrade.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpgradeFromUriRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UiPluginV1Alpha1Console
<details><summary><code>client.ui_plugin_v1alpha1console.<a href="src/fern/ui_plugin_v1alpha1console/client.py">fetch_ui_plugin_css_bundle</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merge CSS bundles of enabled plugins and the activated theme into one.
</dd>
</dl>
</dd>
</dl>

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

client.ui_plugin_v1alpha1console.fetch_ui_plugin_css_bundle()

```
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

<details><summary><code>client.ui_plugin_v1alpha1console.<a href="src/fern/ui_plugin_v1alpha1console/client.py">fetch_ui_plugin_js_bundle</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merge JS bundles of enabled plugins and the activated theme into one.
</dd>
</dl>
</dd>
</dl>

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

client.ui_plugin_v1alpha1console.fetch_ui_plugin_js_bundle()

```
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

<details><summary><code>client.ui_plugin_v1alpha1console.<a href="src/fern/ui_plugin_v1alpha1console/client.py">fetch_ui_plugin_providers</a>() -> UiPluginProviderDescriptor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the currently enabled UI provider descriptor.
</dd>
</dl>
</dd>
</dl>

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

client.ui_plugin_v1alpha1console.fetch_ui_plugin_providers()

```
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

## UserV1Alpha1Console
<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">list_users</a>(...) -> UserEndpointListedUserList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List users
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.list_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size number. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**label_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Label selector. e.g.: hidden!=true
    
</dd>
</dl>

<dl>
<dd>

**field_selector:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Field selector. e.g.: metadata.name==halo
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword to search
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Role metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">create_user</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new user.
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.create_user(
    email="email",
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

**email:** `str` — email address of the user
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — user <code>metadata.name</code>, which also serves as the login name
    
</dd>
</dl>

<dl>
<dd>

**annotations:** `typing.Optional[typing.Dict[str, str]]` — metadata annotations to set on the user
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[str]` — avatar URL of the user
    
</dd>
</dl>

<dl>
<dd>

**bio:** `typing.Optional[str]` — biography or profile text of the user
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — display name shown in the console and theme
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — raw password to set for the user
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — phone number of the user
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` — role <code>metadata.name</code> values to grant to the user after creation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">get_current_user_detail</a>() -> DetailedUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current user detail
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.get_current_user_detail()

```
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

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">update_current_user</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update current user profile, but password.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Metadata, UserSpec
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_v1alpha1console.update_current_user(
    api_version="apiVersion",
    kind="kind",
    metadata=Metadata(
        name="name",
    ),
    spec=UserSpec(
        display_name="displayName",
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

**request:** `User` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">change_own_password</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change own password of user.
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.change_own_password(
    old_password="oldPassword",
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

**old_password:** `str` — old password
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — new password
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">send_email_verification_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send email verification code for user
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.send_email_verification_code(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — email address to verify
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">verify_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify email for user by code.
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.verify_email(
    code="code",
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

**code:** `str` — email verification code
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — current password of the authenticated user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">get_user_detail</a>(...) -> DetailedUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get user detail by metadata.name
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.get_user_detail(
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

**name:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">upload_user_avatar</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

upload user avatar
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.upload_user_avatar(
    name="name",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — Avatar file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">delete_user_avatar</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

delete user avatar
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.delete_user_avatar(
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

**name:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">change_anyone_password</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change anyone password of user for admin.
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.change_anyone_password(
    name="name",
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

**name:** `str` — User metadata.name. If the name is equal to '-', it will change the password of current user.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — new password
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">get_permissions</a>(...) -> UserPermission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get permissions of user
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.get_permissions(
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

**name:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">grant_permission</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Grant permissions to user
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.grant_permission(
    name="name",
    roles=[
        "roles"
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

**name:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` — role <code>metadata.name</code> values to grant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">disable_user</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable user by metadata.name
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.disable_user(
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

**username:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_v1alpha1console.<a href="src/fern/user_v1alpha1console/client.py">enable_user</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable user by metadata.name
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1console.enable_user(
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

**username:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SystemConfigV1Alpha1Console
<details><summary><code>client.system_config_v1alpha1console.<a href="src/fern/system_config_v1alpha1console/client.py">get_system_config_by_group</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get system config by group
</dd>
</dl>
</dd>
</dl>

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

client.system_config_v1alpha1console.get_system_config_by_group(
    group="group",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group:** `str` — Group of the system config
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system_config_v1alpha1console.<a href="src/fern/system_config_v1alpha1console/client.py">update_system_config_by_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update system config by group
</dd>
</dl>
</dd>
</dl>

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

client.system_config_v1alpha1console.update_system_config_by_group(
    group="group",
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

**group:** `str` — Group of the system config
    
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

## MigrationV1Alpha1Console
<details><summary><code>client.migration_v1alpha1console.<a href="src/fern/migration_v1alpha1console/client.py">get_backup_files</a>() -> typing.List[BackupFile]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get backup files from backup root.
</dd>
</dl>
</dd>
</dl>

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

client.migration_v1alpha1console.get_backup_files()

```
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

<details><summary><code>client.migration_v1alpha1console.<a href="src/fern/migration_v1alpha1console/client.py">download_backups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a file from the specified backup as an octet-stream attachment.
</dd>
</dl>
</dd>
</dl>

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

client.migration_v1alpha1console.download_backups(
    name="name",
    filename="filename",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Backup metadata.name.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` — Backup filename.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.migration_v1alpha1console.<a href="src/fern/migration_v1alpha1console/client.py">restore_backup</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore backup by uploading file or providing download link or backup name.
</dd>
</dl>
</dd>
</dl>

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

client.migration_v1alpha1console.restore_backup(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**backup_name:** `typing.Optional[str]` — Backup <code>metadata.name</code>.
    
</dd>
</dl>

<dl>
<dd>

**download_url:** `typing.Optional[str]` — Remote backup HTTP URL.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — Backup file.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Filename of backup file in backups root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PolicyAlpha1Console
<details><summary><code>client.policy_alpha1console.<a href="src/fern/policy_alpha1console/client.py">get_policy_config_by_group</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get policy config by group
</dd>
</dl>
</dd>
</dl>

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

client.policy_alpha1console.get_policy_config_by_group(
    name="name",
    group="group",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the policy
    
</dd>
</dl>

<dl>
<dd>

**group:** `str` — Config group name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.policy_alpha1console.<a href="src/fern/policy_alpha1console/client.py">update_policy_config_by_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update policy config by group
</dd>
</dl>
</dd>
</dl>

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

client.policy_alpha1console.update_policy_config_by_group(
    name="name",
    group="group",
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

**name:** `str` — metadata.name of the policy
    
</dd>
</dl>

<dl>
<dd>

**group:** `str` — Config group name
    
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

