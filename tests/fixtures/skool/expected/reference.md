# Reference
## Sessions
<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">create_session</a>(...) -> Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an authenticated session for API access. Sessions are required for all other endpoints.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.sessions.create_session(
    email="email",
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

**email:** `str` — Skool account email
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Skool account password
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">list_groups</a>(...) -> typing.List[Group]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of Skool groups/communities the authenticated user has access to.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.list_groups(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific Skool group/community.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.get_group(
    group_slug="group_slug",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Members
<details><summary><code>client.members.<a href="src/fern/members/client.py">list_members</a>(...) -> typing.List[Member]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of members in a Skool group.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.members.list_members(
    group_slug="group_slug",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
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

<details><summary><code>client.members.<a href="src/fern/members/client.py">get_member</a>(...) -> Member</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific member in a group.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.members.get_member(
    group_slug="group_slug",
    member_id="member_id",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Posts
<details><summary><code>client.posts.<a href="src/fern/posts/client.py">list_posts</a>(...) -> typing.List[Post]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve posts from a Skool group community feed.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.posts.list_posts(
    group_slug="group_slug",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">create_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new post in a Skool group community.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.posts.create_post(
    group_slug="group_slug",
    session_id="session_id",
    title="title",
    content="content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">get_post</a>(...) -> Post</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific post with its content and comments.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.posts.get_post(
    group_slug="group_slug",
    post_id="post_id",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**post_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">list_comments</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve comments on a specific post.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.posts.list_comments(
    group_slug="group_slug",
    post_id="post_id",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**post_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">create_comment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a comment to a post.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.posts.create_comment(
    group_slug="group_slug",
    post_id="post_id",
    session_id="session_id",
    content="content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**post_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Chat
<details><summary><code>client.chat.<a href="src/fern/chat/client.py">list_chat_messages</a>(...) -> typing.List[ChatMessage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve chat messages from a Skool group's chat.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.chat.list_chat_messages(
    group_slug="group_slug",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` 
    
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

<details><summary><code>client.chat.<a href="src/fern/chat/client.py">send_chat_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message to a group chat channel.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.chat.send_chat_message(
    group_slug="group_slug",
    session_id="session_id",
    content="content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Analytics
<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">get_group_analytics</a>(...) -> GetGroupAnalyticsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve analytics data for a Skool group.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.analytics.get_group_analytics(
    group_slug="group_slug",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">list_webhooks</a>(...) -> typing.List[Webhook]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all configured webhooks.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.list_webhooks(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">create_webhook</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook to receive real-time notifications for events in your Skool communities.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.webhooks import CreateWebhookRequestEventsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.create_webhook(
    session_id="session_id",
    url="url",
    group="group",
    events=[
        CreateWebhookRequestEventsItem.POST
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

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL to receive webhook notifications
    
</dd>
</dl>

<dl>
<dd>

**group:** `str` — The group slug to monitor
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[CreateWebhookRequestEventsItem]` — Events to subscribe to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">delete_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a configured webhook.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.delete_webhook(
    webhook_id="webhook_id",
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

