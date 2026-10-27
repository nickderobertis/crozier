# Reference
## Chats
<details><summary><code>client.chats.<a href="src/fern/chats/client.py">list_chats</a>(...) -> ListChatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of chats that the user is part of
</dd>
</dl>
</dd>
</dl>

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

client.chats.list_chats(
    orderby="lastMessagePreview/createdDateTime desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return (default is 10, max is 50)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — OData filter query
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `typing.Optional[str]` — OData orderby query
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ListChatsRequestExpand]` — OData expand query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/fern/chats/client.py">create_chat</a>(...) -> Chat</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new one-on-one or group chat
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ConversationMemberInput
from fern.environment import FernApiEnvironment
from fern.chats import CreateChatRequestChatType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chats.create_chat(
    chat_type=CreateChatRequestChatType.ONE_ON_ONE,
    members=[
        ConversationMemberInput(
            odata_type="#microsoft.graph.aadUserConversationMember",
            user_odata_bind="https://graph.microsoft.com/v1.0/users(\'userId\')",
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

**chat_type:** `CreateChatRequestChatType` 
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.List[ConversationMemberInput]` 
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` — Subject or topic for the chat (only for group chats)
    
</dd>
</dl>

<dl>
<dd>

**installed_apps:** `typing.Optional[typing.List[CreateChatRequestInstalledAppsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/fern/chats/client.py">get_chat</a>(...) -> Chat</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the properties and relationships of a chat
</dd>
</dl>
</dd>
</dl>

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

client.chats.get_chat(
    chat_id="chat-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[GetChatRequestExpand]` — OData expand query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/fern/chats/client.py">delete_chat</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a chat
</dd>
</dl>
</dd>
</dl>

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

client.chats.delete_chat(
    chat_id="chat-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/fern/chats/client.py">update_chat</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the properties of a chat
</dd>
</dl>
</dd>
</dl>

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

client.chats.update_chat(
    chat_id="chat-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` — Subject or topic for the chat
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Chat Members
<details><summary><code>client.chat_members.<a href="src/fern/chat_members/client.py">list_chat_members</a>(...) -> ListChatMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of members in a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_members.list_chat_members(
    chat_id="chat-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_members.<a href="src/fern/chat_members/client.py">add_chat_member</a>(...) -> ConversationMember</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a member to a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_members.add_chat_member(
    chat_id="chat-id",
    odata_type="#microsoft.graph.aadUserConversationMember",
    user_odata_bind="https://graph.microsoft.com/v1.0/users(\'userId\')",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**request:** `ConversationMemberInput` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_members.<a href="src/fern/chat_members/client.py">add_multiple_chat_members</a>(...) -> typing.List[AddMultipleChatMembersResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add multiple members to a chat in a single request
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ConversationMemberInput
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chat_members.add_multiple_chat_members(
    chat_id="chat-id",
    values=[
        ConversationMemberInput(
            odata_type="#microsoft.graph.aadUserConversationMember",
            user_odata_bind="https://graph.microsoft.com/v1.0/users(\'userId\')",
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

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.List[ConversationMemberInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_members.<a href="src/fern/chat_members/client.py">get_chat_member</a>(...) -> ConversationMember</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific member of a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_members.get_chat_member(
    chat_id="chat-id",
    conversation_member_id="conversationMember-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**conversation_member_id:** `str` — The unique identifier of the conversation member
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_members.<a href="src/fern/chat_members/client.py">remove_chat_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a member from a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_members.remove_chat_member(
    chat_id="chat-id",
    conversation_member_id="conversationMember-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**conversation_member_id:** `str` — The unique identifier of the conversation member
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_members.<a href="src/fern/chat_members/client.py">update_chat_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a member's role in a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_members.update_chat_member(
    chat_id="chat-id",
    conversation_member_id="conversationMember-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**conversation_member_id:** `str` — The unique identifier of the conversation member
    
</dd>
</dl>

<dl>
<dd>

**odata_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[UpdateChatMemberRequestRolesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Chat Messages
<details><summary><code>client.chat_messages.<a href="src/fern/chat_messages/client.py">list_chat_messages</a>(...) -> ListChatMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of messages in a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_messages.list_chat_messages(
    chat_id="chat-id",
    orderby="createdDateTime desc",
    filter="lastModifiedDateTime gt 2022-09-22T00:00:00.000Z",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `typing.Optional[str]` — OData orderby query
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — OData filter query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_messages.<a href="src/fern/chat_messages/client.py">send_chat_message</a>(...) -> ChatMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a new message in a chat
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.chat_messages import SendChatMessageRequestBody

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chat_messages.send_chat_message(
    chat_id="chat-id",
    body=SendChatMessageRequestBody(
        content="content",
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

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**body:** `SendChatMessageRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**importance:** `typing.Optional[SendChatMessageRequestImportance]` 
    
</dd>
</dl>

<dl>
<dd>

**mentions:** `typing.Optional[typing.List[SendChatMessageRequestMentionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.List[ChatMessageAttachment]]` 
    
</dd>
</dl>

<dl>
<dd>

**hosted_contents:** `typing.Optional[typing.List[SendChatMessageRequestHostedContentsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_messages.<a href="src/fern/chat_messages/client.py">get_chat_message</a>(...) -> ChatMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific message in a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_messages.get_chat_message(
    chat_id="chat-id",
    chat_message_id="chatMessage-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**chat_message_id:** `str` — The unique identifier of the chat message
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[GetChatMessageRequestExpand]` — OData expand query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_messages.<a href="src/fern/chat_messages/client.py">delete_chat_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft delete a message in a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_messages.delete_chat_message(
    chat_id="chat-id",
    chat_message_id="chatMessage-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**chat_message_id:** `str` — The unique identifier of the chat message
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_messages.<a href="src/fern/chat_messages/client.py">update_chat_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a message in a chat
</dd>
</dl>
</dd>
</dl>

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

client.chat_messages.update_chat_message(
    chat_id="chat-id",
    chat_message_id="chatMessage-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The unique identifier of the chat
    
</dd>
</dl>

<dl>
<dd>

**chat_message_id:** `str` — The unique identifier of the chat message
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[UpdateChatMessageRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chat_messages.<a href="src/fern/chat_messages/client.py">get_all_messages_for_user</a>(...) -> GetAllMessagesForUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all messages from all chats that a user is a participant in
</dd>
</dl>
</dd>
</dl>

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

client.chat_messages.get_all_messages_for_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `typing.Optional[GetAllMessagesForUserRequestModel]` — Payment model for metered API
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Teams
<details><summary><code>client.teams.<a href="src/fern/teams/client.py">list_joined_teams</a>() -> ListJoinedTeamsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the teams in Microsoft Teams that the user is a direct member of
</dd>
</dl>
</dd>
</dl>

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

client.teams.list_joined_teams()

```
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

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">list_all_teams</a>(...) -> ListAllTeamsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all teams in an organization (requires admin permissions)
</dd>
</dl>
</dd>
</dl>

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

client.teams.list_all_teams()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[str]` — OData filter query
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">create_team</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new team
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.teams import CreateTeamRequestChannels

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.teams.create_team(
    request=CreateTeamRequestChannels(
        template_odata_bind="https://graph.microsoft.com/v1.0/teamsTemplates(\'standard\')",
        display_name="displayName",
        description="description",
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

**request:** `CreateTeamRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">get_team</a>(...) -> Team</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the properties and relationships of the specified team
</dd>
</dl>
</dd>
</dl>

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

client.teams.get_team(
    team_id="team-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**select:** `typing.Optional[str]` — OData select query
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[GetTeamRequestExpand]` — OData expand query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">delete_team</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a team
</dd>
</dl>
</dd>
</dl>

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

client.teams.delete_team(
    team_id="team-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">update_team</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the properties of a team
</dd>
</dl>
</dd>
</dl>

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

client.teams.update_team(
    team_id="team-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[UpdateTeamRequestVisibility]` 
    
</dd>
</dl>

<dl>
<dd>

**member_settings:** `typing.Optional[TeamMemberSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**guest_settings:** `typing.Optional[TeamGuestSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**messaging_settings:** `typing.Optional[TeamMessagingSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**fun_settings:** `typing.Optional[TeamFunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**discovery_settings:** `typing.Optional[TeamDiscoverySettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">archive_team</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive the specified team
</dd>
</dl>
</dd>
</dl>

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

client.teams.archive_team(
    team_id="team-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**should_set_spo_site_read_only_for_members:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">unarchive_team</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore an archived team
</dd>
</dl>
</dd>
</dl>

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

client.teams.unarchive_team(
    team_id="team-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Team Members
<details><summary><code>client.team_members.<a href="src/fern/team_members/client.py">list_team_members</a>(...) -> ListTeamMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the members of a team
</dd>
</dl>
</dd>
</dl>

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

client.team_members.list_team_members(
    team_id="team-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — OData filter query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.<a href="src/fern/team_members/client.py">add_team_member</a>(...) -> ConversationMember</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new member to a team
</dd>
</dl>
</dd>
</dl>

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

client.team_members.add_team_member(
    team_id="team-id",
    odata_type="#microsoft.graph.aadUserConversationMember",
    user_odata_bind="https://graph.microsoft.com/v1.0/users(\'userId\')",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**request:** `ConversationMemberInput` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.<a href="src/fern/team_members/client.py">add_multiple_team_members</a>(...) -> typing.List[AddMultipleTeamMembersResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add multiple members to a team in a single request
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ConversationMemberInput
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.team_members.add_multiple_team_members(
    team_id="team-id",
    values=[
        ConversationMemberInput(
            odata_type="#microsoft.graph.aadUserConversationMember",
            user_odata_bind="https://graph.microsoft.com/v1.0/users(\'userId\')",
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

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.List[ConversationMemberInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channels
<details><summary><code>client.channels.<a href="src/fern/channels/client.py">list_all_channels</a>(...) -> ListAllChannelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all channels across a team, including shared channels
</dd>
</dl>
</dd>
</dl>

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

client.channels.list_all_channels(
    team_id="team-id",
    filter="membershipType eq \'shared\'",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — OData filter query
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">list_channels</a>(...) -> ListChannelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of channels in a team
</dd>
</dl>
</dd>
</dl>

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

client.channels.list_channels(
    team_id="team-id",
    filter="membershipType eq \'private\'",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — OData filter query
    
</dd>
</dl>

<dl>
<dd>

**select:** `typing.Optional[str]` — OData select query
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">create_channel</a>(...) -> Channel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new channel in a team
</dd>
</dl>
</dd>
</dl>

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

client.channels.create_channel(
    team_id="team-id",
    display_name="displayName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**odata_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**membership_type:** `typing.Optional[CreateChannelRequestMembershipType]` 
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.Optional[typing.List[ConversationMemberInput]]` — Required when creating a private channel
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_channel</a>(...) -> Channel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the properties and relationships of a channel
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_channel(
    team_id="team-id",
    channel_id="channel-id",
    select="summary",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**select:** `typing.Optional[str]` — OData select query
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[GetChannelRequestExpand]` — OData expand query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">delete_channel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a channel
</dd>
</dl>
</dd>
</dl>

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

client.channels.delete_channel(
    team_id="team-id",
    channel_id="channel-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">update_channel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the properties of a channel
</dd>
</dl>
</dd>
</dl>

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

client.channels.update_channel(
    team_id="team-id",
    channel_id="channel-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_channel_from_all_channels</a>(...) -> Channel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a channel from the list of all channels
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_channel_from_all_channels(
    team_id="team-id",
    channel_id="channel-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channel Members
<details><summary><code>client.channel_members.<a href="src/fern/channel_members/client.py">list_channel_members</a>(...) -> ListChannelMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of members in a channel
</dd>
</dl>
</dd>
</dl>

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

client.channel_members.list_channel_members(
    team_id="team-id",
    channel_id="channel-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — OData filter query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channel_members.<a href="src/fern/channel_members/client.py">add_channel_member</a>(...) -> ConversationMember</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a member to a private channel
</dd>
</dl>
</dd>
</dl>

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

client.channel_members.add_channel_member(
    team_id="team-id",
    channel_id="channel-id",
    odata_type="#microsoft.graph.aadUserConversationMember",
    user_odata_bind="https://graph.microsoft.com/v1.0/users(\'userId\')",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**request:** `ConversationMemberInput` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channel Messages
<details><summary><code>client.channel_messages.<a href="src/fern/channel_messages/client.py">list_channel_messages</a>(...) -> ListChannelMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of messages in a channel
</dd>
</dl>
</dd>
</dl>

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

client.channel_messages.list_channel_messages(
    team_id="team-id",
    channel_id="channel-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[int]` — Number of items to return
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of items to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ListChannelMessagesRequestExpand]` — OData expand query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channel_messages.<a href="src/fern/channel_messages/client.py">send_channel_message</a>(...) -> ChatMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a new message in a channel
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.channel_messages import SendChannelMessageRequestBody

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channel_messages.send_channel_message(
    team_id="team-id",
    channel_id="channel-id",
    body=SendChannelMessageRequestBody(
        content="content",
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

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**body:** `SendChannelMessageRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**importance:** `typing.Optional[SendChannelMessageRequestImportance]` 
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — The subject of the channel message
    
</dd>
</dl>

<dl>
<dd>

**mentions:** `typing.Optional[typing.List[SendChannelMessageRequestMentionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.List[ChatMessageAttachment]]` 
    
</dd>
</dl>

<dl>
<dd>

**hosted_contents:** `typing.Optional[typing.List[SendChannelMessageRequestHostedContentsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channel_messages.<a href="src/fern/channel_messages/client.py">get_channel_message</a>(...) -> ChatMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific message in a channel
</dd>
</dl>
</dd>
</dl>

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

client.channel_messages.get_channel_message(
    team_id="team-id",
    channel_id="channel-id",
    chat_message_id="chatMessage-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**chat_message_id:** `str` — The unique identifier of the chat message
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[GetChannelMessageRequestExpand]` — OData expand query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channel_messages.<a href="src/fern/channel_messages/client.py">delete_channel_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft delete a message in a channel
</dd>
</dl>
</dd>
</dl>

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

client.channel_messages.delete_channel_message(
    team_id="team-id",
    channel_id="channel-id",
    chat_message_id="chatMessage-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**chat_message_id:** `str` — The unique identifier of the chat message
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channel_messages.<a href="src/fern/channel_messages/client.py">update_channel_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a message in a channel
</dd>
</dl>
</dd>
</dl>

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

client.channel_messages.update_channel_message(
    team_id="team-id",
    channel_id="channel-id",
    chat_message_id="chatMessage-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of the team
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `str` — The unique identifier of the channel
    
</dd>
</dl>

<dl>
<dd>

**chat_message_id:** `str` — The unique identifier of the chat message
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[UpdateChannelMessageRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

