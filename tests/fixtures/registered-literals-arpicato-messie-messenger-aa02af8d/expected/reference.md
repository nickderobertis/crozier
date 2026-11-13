# Reference
## auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L34-L60">whoami</a>() -> Whoami</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all info that is useful for presenting this bridge in a manager interface.
* Server details: remote network details, available login flows, homeserver name, bridge bot user ID, command prefix
* User details: management room ID, list of logins with current state and info
</dd>
</dl>
</dd>
</dl>

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

client.auth.whoami()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L62-L84">get_login_flows</a>() -> GetLoginFlowsResponse</code></summary>
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

client.auth.get_login_flows()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L86-L108">get_login_i_ds</a>() -> GetLoginIDsResponse</code></summary>
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

client.auth.get_login_i_ds()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L110-L165">start_login</a>(...) -> LoginStep</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint starts a new login process, which is used to log into the bridge.

The basic flow of the entire login, including calling this endpoint, is:
1. Call `GET /v3/login/flows` to get the list of available flows.
   If there's more than one flow, ask the user to pick which one they want to use.
2. Call this endpoint with the chosen flow ID to start the login.
   The first login step will be returned.
3. Render the information provided in the step.
4. Call the `/login/step/...` endpoint corresponding to the step type:
   * For `user_input` and `cookies`, acquire the requested fields before calling the endpoint.
   * For `display_and_wait`, call the endpoint immediately
     (as there's nothing to acquire on the client side).
5. Handle the data returned by the login step endpoint:
   * If an error is returned, the login has failed and must be restarted
     (from either step 1 or step 2) if the user wants to try again.
   * If step type `complete` is returned, the login finished successfully.
   * Otherwise, go to step 3 with the new data.
</dd>
</dl>
</dd>
</dl>

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

client.auth.start_login(
    flow_id="qr",
    login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**flow_id:** `str` — The login flow ID to use.
    
</dd>
</dl>

<dl>
<dd>

**login_id:** `typing.Optional[UserLoginId]` — An existing login ID to re-login as. If this is specified and the user logs into a different account, the provided ID will be logged out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L167-L210">submit_login_step_user_input</a>(...) -> LoginStep</code></summary>
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

client.auth.submit_login_step_user_input(
    login_process_id="loginProcessID",
    step_id="stepID",
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

**login_process_id:** `str` — The ID of the login process, as returned in the `login_id` field of the start call.
    
</dd>
</dl>

<dl>
<dd>

**step_id:** `str` — The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L212-L255">submit_login_step_cookies</a>(...) -> LoginStep</code></summary>
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

client.auth.submit_login_step_cookies(
    login_process_id="loginProcessID",
    step_id="stepID",
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

**login_process_id:** `str` — The ID of the login process, as returned in the `login_id` field of the start call.
    
</dd>
</dl>

<dl>
<dd>

**step_id:** `str` — The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L257-L292">submit_login_step_display_and_wait</a>(...) -> LoginStep</code></summary>
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

client.auth.submit_login_step_display_and_wait(
    login_process_id="loginProcessID",
    step_id="stepID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**login_process_id:** `str` — The ID of the login process, as returned in the `login_id` field of the start call.
    
</dd>
</dl>

<dl>
<dd>

**step_id:** `str` — The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L294-L323">logout</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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

client.auth.logout(
    login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**login_id:** `LogoutRequestLoginId` — The ID of the login to log out. Use `all` to log out of all logins.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## snc
<details><summary><code>client.snc.<a href="src/fern/snc/client.py#L38-L67">get_contacts</a>(...) -> GetContactsResponse</code></summary>
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

client.snc.get_contacts(
    login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**login_id:** `typing.Optional[UserLoginId]` — An optional explicit login ID to do the action through.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snc.<a href="src/fern/snc/client.py#L69-L105">search_users</a>(...) -> SearchUsersResponse</code></summary>
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

client.snc.search_users(
    login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**login_id:** `typing.Optional[UserLoginId]` — An optional explicit login ID to do the action through.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — The search query to send to the remote network
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snc.<a href="src/fern/snc/client.py#L107-L144">resolve_identifier</a>(...) -> ResolvedIdentifier</code></summary>
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

client.snc.resolve_identifier(
    identifier="username",
    login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — The identifier to resolve or start a chat with.
    
</dd>
</dl>

<dl>
<dd>

**login_id:** `typing.Optional[UserLoginId]` — An optional explicit login ID to do the action through.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snc.<a href="src/fern/snc/client.py#L146-L183">create_dm</a>(...) -> CreateDmResponse</code></summary>
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

client.snc.create_dm(
    identifier="username",
    login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — The identifier to resolve or start a chat with.
    
</dd>
</dl>

<dl>
<dd>

**login_id:** `typing.Optional[UserLoginId]` — An optional explicit login ID to do the action through.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snc.<a href="src/fern/snc/client.py#L185-L270">create_group</a>(...) -> CreatedGroup</code></summary>
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

client.snc.create_group(
    type_path_param="type",
    login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type_path_param:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**login_id:** `typing.Optional[UserLoginId]` — An optional explicit login ID to do the action through.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of group to create.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — The public username for the created group.
    
</dd>
</dl>

<dl>
<dd>

**participants:** `typing.Optional[typing.List[str]]` — The users to add to the group initially.
    
</dd>
</dl>

<dl>
<dd>

**parent:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[GroupCreateParamsName]` — The `m.room.name` event content for the room.
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[GroupCreateParamsAvatar]` — The `m.room.avatar` event content for the room.
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[GroupCreateParamsTopic]` — The `m.room.topic` event content for the room.
    
</dd>
</dl>

<dl>
<dd>

**disappear:** `typing.Optional[GroupCreateParamsDisappear]` — The `com.beeper.disappearing_timer` event content for the room.
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[str]` 

An existing Matrix room ID to bridge to.
The other parameters must be already in sync with the room state when using this parameter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

