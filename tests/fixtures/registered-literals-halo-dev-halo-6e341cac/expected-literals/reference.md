# Reference
## NotifierV1Alpha1Uc
<details><summary><code>client.notifier_v1alpha1uc.<a href="src/fern/notifier_v1alpha1uc/client.py">fetch_receiver_config</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch receiver config of notifier
</dd>
</dl>
</dd>
</dl>

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

client.notifier_v1alpha1uc.fetch_receiver_config(
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

<details><summary><code>client.notifier_v1alpha1uc.<a href="src/fern/notifier_v1alpha1uc/client.py">save_receiver_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save receiver config of notifier
</dd>
</dl>
</dd>
</dl>

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

client.notifier_v1alpha1uc.save_receiver_config(
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

## NotificationV1Alpha1Uc
<details><summary><code>client.notification_v1alpha1uc.<a href="src/fern/notification_v1alpha1uc/client.py">list_user_notification_preferences</a>(...) -> ReasonTypeNotifierMatrix</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List notification preferences for the authenticated user.
</dd>
</dl>
</dd>
</dl>

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

client.notification_v1alpha1uc.list_user_notification_preferences(
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

<details><summary><code>client.notification_v1alpha1uc.<a href="src/fern/notification_v1alpha1uc/client.py">save_user_notification_preferences</a>(...) -> ReasonTypeNotifierMatrix</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save notification preferences for the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ReasonTypeNotifierRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification_v1alpha1uc.save_user_notification_preferences(
    username="username",
    reason_type_notifiers=[
        ReasonTypeNotifierRequest(
            notifiers=[
                "notifiers"
            ],
            reason_type="reasonType",
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

**username:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**reason_type_notifiers:** `typing.List[ReasonTypeNotifierRequest]` — notifier selections grouped by reason type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_v1alpha1uc.<a href="src/fern/notification_v1alpha1uc/client.py">list_user_notifications</a>(...) -> NotificationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List notifications for the authenticated user.
</dd>
</dl>
</dd>
</dl>

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

client.notification_v1alpha1uc.list_user_notifications(
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

<details><summary><code>client.notification_v1alpha1uc.<a href="src/fern/notification_v1alpha1uc/client.py">mark_notifications_as_read</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark the specified notifications as read.
</dd>
</dl>
</dd>
</dl>

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

client.notification_v1alpha1uc.mark_notifications_as_read(
    username="username",
    names=[
        "names"
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

**username:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**names:** `typing.List[str]` — notification <code>metadata.name</code> values to mark as read
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_v1alpha1uc.<a href="src/fern/notification_v1alpha1uc/client.py">delete_specified_notification</a>(...) -> Notification</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified notification.
</dd>
</dl>
</dd>
</dl>

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

client.notification_v1alpha1uc.delete_specified_notification(
    username="username",
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

**username:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Notification metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_v1alpha1uc.<a href="src/fern/notification_v1alpha1uc/client.py">mark_notification_as_read</a>(...) -> Notification</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark the specified notification as read.
</dd>
</dl>
</dd>
</dl>

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

client.notification_v1alpha1uc.mark_notification_as_read(
    username="username",
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

**username:** `str` — User metadata.name
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Notification metadata.name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserConnectionV1Alpha1Uc
<details><summary><code>client.user_connection_v1alpha1uc.<a href="src/fern/user_connection_v1alpha1uc/client.py">disconnect_my_connection</a>(...) -> typing.List[UserConnection]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect my connection from a third-party platform.
</dd>
</dl>
</dd>
</dl>

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

client.user_connection_v1alpha1uc.disconnect_my_connection(
    register_id="registerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**register_id:** `str` — The registration ID of the third-party platform.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PostV1Alpha1Uc
<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">list_my_posts</a>(...) -> ListedPostList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List posts owned by the current user with pagination, sorting, keyword, publish phase, and category filters.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1uc.list_my_posts()

```
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

**publish_phase:** `typing.Optional[ListMyPostsRequestPublishPhase]` — Filter posts by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.
    
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

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">create_my_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a draft post for the current user. To create it with initial content, put JSON-serialized Content into metadata.annotations['content.halo.run/content-json'].
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Metadata, PostSpec, Excerpt
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_v1alpha1uc.create_my_post(
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
        visible="PUBLIC",
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

**request:** `Post` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">get_my_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a post owned by the current user by metadata.name.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1uc.get_my_post(
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

**name:** `str` — metadata.name of a post owned by the current user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">update_my_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update post metadata and editable spec fields for the current user. Content is not updated by this operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Metadata, PostSpec, Excerpt
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_v1alpha1uc.update_my_post(
    name="name",
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
        visible="PUBLIC",
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

**name:** `str` — metadata.name of a post owned by the current user.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Post` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">get_my_post_draft</a>(...) -> Snapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the editable draft snapshot of a post owned by the current user.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1uc.get_my_post_draft(
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

**name:** `str` — metadata.name of a post owned by the current user.
    
</dd>
</dl>

<dl>
<dd>

**patched:** `typing.Optional[bool]` — Whether to return the head snapshot patched against the base snapshot. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">update_my_post_draft</a>(...) -> Snapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the editable draft snapshot of a post owned by the current user. The snapshot must belong to the post and must be the current head snapshot.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Metadata, SnapShotSpec, Ref
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_v1alpha1uc.update_my_post_draft(
    name="name",
    api_version="apiVersion",
    kind="kind",
    metadata=Metadata(
        name="name",
    ),
    spec=SnapShotSpec(
        owner="owner",
        raw_type="rawType",
        subject_ref=Ref(
            group="group",
            kind="kind",
            name="name",
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

**name:** `str` — metadata.name of a post owned by the current user.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Snapshot` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">publish_my_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a post owned by the current user from its current head snapshot.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1uc.publish_my_post(
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

**name:** `str` — metadata.name of a post owned by the current user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">recycle_my_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move a post owned by the current user to the recycle bin.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1uc.recycle_my_post(
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

**name:** `str` — metadata.name of a post owned by the current user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.post_v1alpha1uc.<a href="src/fern/post_v1alpha1uc/client.py">unpublish_my_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpublish a post owned by the current user so it is no longer served as published content.
</dd>
</dl>
</dd>
</dl>

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

client.post_v1alpha1uc.unpublish_my_post(
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

**name:** `str` — metadata.name of a post owned by the current user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SnapshotV1Alpha1Uc
<details><summary><code>client.snapshot_v1alpha1uc.<a href="src/fern/snapshot_v1alpha1uc/client.py">get_snapshot_for_post</a>(...) -> Snapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a content snapshot for a post owned by the current user. The snapshot must belong to the post specified by postName.
</dd>
</dl>
</dd>
</dl>

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

client.snapshot_v1alpha1uc.get_snapshot_for_post(
    name="name",
    post_name="postName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — metadata.name of the snapshot to fetch.
    
</dd>
</dl>

<dl>
<dd>

**post_name:** `str` — metadata.name of the post that owns the snapshot. The post must belong to the current user.
    
</dd>
</dl>

<dl>
<dd>

**patched:** `typing.Optional[bool]` — Whether to return the snapshot patched against the post base snapshot. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AnnotationSettingV1AlphaUc
<details><summary><code>client.annotation_setting_v1alpha_uc.<a href="src/fern/annotation_setting_v1alpha_uc/client.py">list_available_annotation_settings</a>(...) -> typing.List[AnnotationSetting]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available AnnotationSettings for the given targetRef. The available AnnotationSettings are determined by the currently activated theme and started plugins.
</dd>
</dl>
</dd>
</dl>

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

client.annotation_setting_v1alpha_uc.list_available_annotation_settings(
    target_ref="targetRef",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_ref:** `str` — The targetRef of the AnnotationSetting. e.g.: 'content.halo.run/Post
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserPreferenceV1Alpha1Uc
<details><summary><code>client.user_preference_v1alpha1uc.<a href="src/fern/user_preference_v1alpha1uc/client.py">get_my_preference</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get my preference by group.
</dd>
</dl>
</dd>
</dl>

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

client.user_preference_v1alpha1uc.get_my_preference(
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

**group:** `str` — Group of user preference, e.g. `notification`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_preference_v1alpha1uc.<a href="src/fern/user_preference_v1alpha1uc/client.py">update_my_preference</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update my preference by group.
</dd>
</dl>
</dd>
</dl>

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

client.user_preference_v1alpha1uc.update_my_preference(
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

**group:** `str` — Group of user preference, e.g. `notification`.
    
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

## UserV1Alpha1Uc
<details><summary><code>client.user_v1alpha1uc.<a href="src/fern/user_v1alpha1uc/client.py">get_my_user</a>() -> UcUserVo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current user profile without password hash.
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1uc.get_my_user()

```
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

<details><summary><code>client.user_v1alpha1uc.<a href="src/fern/user_v1alpha1uc/client.py">change_my_password</a>(...) -> UcUserVo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set or change the password of the current user.
</dd>
</dl>
</dd>
</dl>

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

client.user_v1alpha1uc.change_my_password(
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

**password:** `str` — new password of the current user
    
</dd>
</dl>

<dl>
<dd>

**old_password:** `typing.Optional[str]` — Old password. Required and verified only when the current user has a password; ignored otherwise.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TwoFactorAuthV1Alpha1Uc
<details><summary><code>client.two_factor_auth_v1alpha1uc.<a href="src/fern/two_factor_auth_v1alpha1uc/client.py">get_two_factor_authentication_settings</a>() -> TwoFactorAuthSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Two-factor authentication settings.
</dd>
</dl>
</dd>
</dl>

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

client.two_factor_auth_v1alpha1uc.get_two_factor_authentication_settings()

```
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

<details><summary><code>client.two_factor_auth_v1alpha1uc.<a href="src/fern/two_factor_auth_v1alpha1uc/client.py">disable_two_factor</a>(...) -> TwoFactorAuthSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable Two-factor authentication
</dd>
</dl>
</dd>
</dl>

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

client.two_factor_auth_v1alpha1uc.disable_two_factor(
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

**request:** `PasswordRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.two_factor_auth_v1alpha1uc.<a href="src/fern/two_factor_auth_v1alpha1uc/client.py">enable_two_factor</a>(...) -> TwoFactorAuthSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable Two-factor authentication
</dd>
</dl>
</dd>
</dl>

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

client.two_factor_auth_v1alpha1uc.enable_two_factor(
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

**request:** `PasswordRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.two_factor_auth_v1alpha1uc.<a href="src/fern/two_factor_auth_v1alpha1uc/client.py">configurer_totp</a>(...) -> TwoFactorAuthSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure a TOTP
</dd>
</dl>
</dd>
</dl>

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

client.two_factor_auth_v1alpha1uc.configurer_totp(
    code="code",
    password="password",
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` — TOTP code generated from the new secret.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Current password of the authenticated user.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` — Raw TOTP secret returned by the auth-link endpoint.
    
</dd>
</dl>

<dl>
<dd>

**current_totp_code:** `typing.Optional[str]` — Current TOTP code, required when replacing an existing TOTP authenticator.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.two_factor_auth_v1alpha1uc.<a href="src/fern/two_factor_auth_v1alpha1uc/client.py">delete_totp</a>(...) -> TwoFactorAuthSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the current user's configured TOTP authenticator after password verification.
</dd>
</dl>
</dd>
</dl>

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

client.two_factor_auth_v1alpha1uc.delete_totp(
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

**request:** `PasswordRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.two_factor_auth_v1alpha1uc.<a href="src/fern/two_factor_auth_v1alpha1uc/client.py">get_totp_auth_link</a>() -> TotpAuthLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get TOTP auth link, including secret
</dd>
</dl>
</dd>
</dl>

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

client.two_factor_auth_v1alpha1uc.get_totp_auth_link()

```
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

## DeviceV1Alpha1Uc
<details><summary><code>client.device_v1alpha1uc.<a href="src/fern/device_v1alpha1uc/client.py">list_devices</a>() -> typing.List[UserDevice]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all user devices
</dd>
</dl>
</dd>
</dl>

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

client.device_v1alpha1uc.list_devices()

```
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

<details><summary><code>client.device_v1alpha1uc.<a href="src/fern/device_v1alpha1uc/client.py">revoke_device</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a own device
</dd>
</dl>
</dd>
</dl>

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

client.device_v1alpha1uc.revoke_device(
    device_id="deviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `str` — Device ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PersonalAccessTokenV1Alpha1Uc
<details><summary><code>client.personal_access_token_v1alpha1uc.<a href="src/fern/personal_access_token_v1alpha1uc/client.py">obtain_pats</a>() -> typing.List[PersonalAccessToken]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Obtain PAT list.
</dd>
</dl>
</dd>
</dl>

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

client.personal_access_token_v1alpha1uc.obtain_pats()

```
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

<details><summary><code>client.personal_access_token_v1alpha1uc.<a href="src/fern/personal_access_token_v1alpha1uc/client.py">generate_pat</a>(...) -> PersonalAccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a PAT.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Metadata
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.personal_access_token_v1alpha1uc.generate_pat(
    api_version="apiVersion",
    kind="kind",
    metadata=Metadata(
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

**request:** `PersonalAccessToken` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_token_v1alpha1uc.<a href="src/fern/personal_access_token_v1alpha1uc/client.py">obtain_pat</a>(...) -> PersonalAccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Obtain a PAT.
</dd>
</dl>
</dd>
</dl>

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

client.personal_access_token_v1alpha1uc.obtain_pat(
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

**name:** `str` — metadata.name of the PAT to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_token_v1alpha1uc.<a href="src/fern/personal_access_token_v1alpha1uc/client.py">delete_pat</a>(...) -> PersonalAccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a PAT
</dd>
</dl>
</dd>
</dl>

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

client.personal_access_token_v1alpha1uc.delete_pat(
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

**name:** `str` — metadata.name of the PAT to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_token_v1alpha1uc.<a href="src/fern/personal_access_token_v1alpha1uc/client.py">restore_pat</a>(...) -> PersonalAccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore a PAT.
</dd>
</dl>
</dd>
</dl>

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

client.personal_access_token_v1alpha1uc.restore_pat(
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

**name:** `str` — metadata.name of the PAT to restore.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_token_v1alpha1uc.<a href="src/fern/personal_access_token_v1alpha1uc/client.py">revoke_pat</a>(...) -> PersonalAccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a PAT
</dd>
</dl>
</dd>
</dl>

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

client.personal_access_token_v1alpha1uc.revoke_pat(
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

**name:** `str` — metadata.name of the PAT to revoke.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AttachmentV1Alpha1Uc
<details><summary><code>client.attachment_v1alpha1uc.<a href="src/fern/attachment_v1alpha1uc/client.py">list_my_attachments</a>(...) -> AttachmentList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List attachments of the current user uploaded.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1uc.list_my_attachments()

```
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

<details><summary><code>client.attachment_v1alpha1uc.<a href="src/fern/attachment_v1alpha1uc/client.py">create_attachment_for_post</a>(...) -> Attachment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create attachment for the given post. Deprecated in favor of /attachments/-/upload.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1uc.create_attachment_for_post(
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

**file:** `core.File` — attachment data
    
</dd>
</dl>

<dl>
<dd>

**wait_for_permalink:** `typing.Optional[bool]` — Wait for permalink.
    
</dd>
</dl>

<dl>
<dd>

**post_name:** `typing.Optional[str]` — post <code>metadata.name</code>
    
</dd>
</dl>

<dl>
<dd>

**single_page_name:** `typing.Optional[str]` — single page <code>metadata.name</code>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attachment_v1alpha1uc.<a href="src/fern/attachment_v1alpha1uc/client.py">match_attachment_permalinks_for_uc</a>(...) -> AttachmentPermalinkMatchList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Match URL strings against Attachment permalinks for user center.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1uc.match_attachment_permalinks_for_uc(
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

<details><summary><code>client.attachment_v1alpha1uc.<a href="src/fern/attachment_v1alpha1uc/client.py">upload_attachment_for_uc</a>(...) -> Attachment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload attachment to user center storage.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1uc.upload_attachment_for_uc(
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

<details><summary><code>client.attachment_v1alpha1uc.<a href="src/fern/attachment_v1alpha1uc/client.py">external_transfer_attachment1</a>(...) -> Attachment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload attachment from the given URL.
Deprecated in favor of /attachments/-/upload.
</dd>
</dl>
</dd>
</dl>

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

client.attachment_v1alpha1uc.external_transfer_attachment1(
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

**url:** `str` — remote file URL to transfer into user-center storage
    
</dd>
</dl>

<dl>
<dd>

**wait_for_permalink:** `typing.Optional[bool]` — Wait for permalink.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — custom file name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

