# Reference
## conversation
<details><summary><code>client.conversation.<a href="src/fern/conversation/client.py">list_conversations</a>(...) -> ListConversationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is **DEPRECATED**. Please use [/v0.2/conversations](/api/conversation.v2#get-conversations).

List all conversations associated with your application. This endpoint required an admin JWT. To find all conversations for the currently logged in user, see [GET /users/:id/conversations](#getuserConversations)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.conversation.list_conversations(
    page_size=50,
    record_index=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_start:** `typing.Optional[str]` — Return the records that occurred after this point in time.
    
</dd>
</dl>

<dl>
<dd>

**date_end:** `typing.Optional[str]` — Return the records that occurred before this point in time.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` — Return this amount of records in the response
    
</dd>
</dl>

<dl>
<dd>

**record_index:** `typing.Optional[RecordIndex]` — Return calls from this index in the response
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListConversationsRequestOrder]` — Return the records in ascending or descending order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/fern/conversation/client.py">create_conversation</a>(...) -> CreateConversationResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.conversation.create_conversation()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**display_name:** `typing.Optional[DisplayName]` 
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[ImageUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[NameConversation]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[CreateConversationRequestProperties]` — Conversation properties
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/fern/conversation/client.py">retrieve_conversation</a>(...) -> RetrieveConversationResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.conversation.retrieve_conversation(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/fern/conversation/client.py">replace_conversation</a>(...) -> ReplaceConversationResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.conversation.replace_conversation(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[DisplayName]` 
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[ImageUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[NameConversation]` 
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[ReplaceConversationRequestProperties]` — Conversation properties
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/fern/conversation/client.py">delete_conversation</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.conversation.delete_conversation(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/fern/conversation/client.py">record_conversation</a>(...)</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.conversation.record_conversation(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    action="start",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**action:** `Action` 
    
</dd>
</dl>

<dl>
<dd>

**event_method:** `typing.Optional[EventMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**event_url:** `typing.Optional[EventUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[Format]` 
    
</dd>
</dl>

<dl>
<dd>

**split:** `typing.Optional[Split]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## event
<details><summary><code>client.event.<a href="src/fern/event/client.py">get_events</a>(...) -> typing.List[EventRetrieved]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is **DEPRECATED**. Please use [/v0.2/events](/api/conversation.v2#get-events).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event.get_events(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event.<a href="src/fern/event/client.py">create_event</a>(...) -> CreateEventResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event.create_event(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    from_="MEM-63f61863-4a51-4f6b-86e1-46edebio0391",
    type="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**from:** `MemberId` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `EventType` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[EventBody]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[MemberId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event.<a href="src/fern/event/client.py">get_event</a>(...) -> EventRetrieved</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event.get_event(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    event_id="event_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Event ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event.<a href="src/fern/event/client.py">delete_event</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event.delete_event(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    event_id="event_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Event ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## member
<details><summary><code>client.member.<a href="src/fern/member/client.py">get_members</a>(...) -> typing.List[GetMembersResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is **DEPRECATED**. Please use [/v0.2/members](/api/conversation.v2#get-members).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.member.get_members(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.member.<a href="src/fern/member/client.py">create_member</a>(...) -> CreateMemberResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Channel
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.member.create_member(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    channel=Channel(),
    user_id="USR-63f61863-4a51-4f6b-86e1-46edebio0391",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**channel:** `Channel` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[MemberAction]` 
    
</dd>
</dl>

<dl>
<dd>

**knocking_id:** `typing.Optional[KnockerId]` 
    
</dd>
</dl>

<dl>
<dd>

**media:** `typing.Optional[Media]` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `typing.Optional[MemberId]` 
    
</dd>
</dl>

<dl>
<dd>

**member_id_inviting:** `typing.Optional[MemberIdInviting]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.member.<a href="src/fern/member/client.py">get_member</a>(...) -> GetMemberResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.member.get_member(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — Member ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.member.<a href="src/fern/member/client.py">update_member</a>(...) -> UpdateMemberResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.member.update_member(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — Member ID
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[MemberAction]` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[Channel]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.member.<a href="src/fern/member/client.py">delete_member</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.member.delete_member(
    conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — Conversation ID
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — Member ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## leg
<details><summary><code>client.leg.<a href="src/fern/leg/client.py">list_legs</a>() -> ListLegsResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.leg.list_legs()

```
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

<details><summary><code>client.leg.<a href="src/fern/leg/client.py">delete_leg</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.leg.delete_leg(
    leg_id="leg_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**leg_id:** `str` — Leg ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## user
<details><summary><code>client.user.<a href="src/fern/user/client.py">get_users</a>() -> typing.List[GetUsersResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is **DEPRECATED**. Please use [/v0.2/users](/api/conversation.v2#get-users).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_users()

```
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">create_user</a>(...) -> CreateUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Note: Users must be created with an admin JWT.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.create_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**display_name:** `typing.Optional[DisplayNameUser]` 
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[ImageUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[NameUser]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_user</a>(...) -> GetUserResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_user(
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

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">update_user</a>(...) -> UpdateUserResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.update_user(
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

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[Channel]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[DisplayNameUser]` 
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[ImageUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[NameUser]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">delete_user</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.delete_user(
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

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">getuser_conversations</a>(...) -> typing.List[GetuserConversationsResponseItem]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.getuser_conversations(
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

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

