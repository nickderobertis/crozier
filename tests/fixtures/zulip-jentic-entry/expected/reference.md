# Reference
## Authentication
<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">fetch_api_key</a>(...) -> ApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API endpoint is used by clients such as the Zulip mobile and
terminal apps to implement password-based authentication. Given the
user's Zulip login credentials, it returns a Zulip API key that the client
can use to make requests as the user.

This endpoint is only useful for Zulip servers/organizations with
EmailAuthBackend or LDAPAuthBackend enabled.

The Zulip mobile apps also support SSO/social authentication (GitHub
auth, Google auth, SAML, etc.) that does not use this endpoint. Instead,
the mobile apps reuse the web login flow passing the `mobile_flow_otp` in
a webview, and the credentials are returned to the app (encrypted) via a redirect
to a `zulip://` URL.

!!! warn ""

    **Note:** If you signed up using passwordless authentication and
    never had a password, you can [reset your password](/help/change-your-password).

See the [API keys](/api/api-keys) documentation for more details
on how to download an API key manually.

In a [Zulip development environment](https://zulip.readthedocs.io/en/latest/development/overview.html),
see also [the unauthenticated variant](/api/dev-fetch-api-key).
</dd>
</dl>
</dd>
</dl>

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

client.authentication.fetch_api_key(
    username="iago@zulip.com",
    password="abcd1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

The username to be used for authentication (typically, the email
address, but depending on configuration, it could be an LDAP username).

See the `require_email_format_usernames` parameter documented in
[GET /server_settings](/api/get-server-settings) for details.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — The user's Zulip password (or LDAP password, if LDAP authentication is in use).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">jwt_fetch_api_key</a>(...) -> JwtFetchApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API endpoint is used by clients to implement JSON Web Token
(JWT) authentication. Given a JWT identifying a Zulip user, it
returns a Zulip API key that the client can use to make requests
as the user.

!!! warn ""

    **Note:** This endpoint is only useful for Zulip servers/organizations
    with [JSON web token authentication][prod-jwt-auth] enabled.

See the [API keys](/api/api-keys) documentation for more details
on how to manage API keys manually.

**Changes**: New in Zulip 7.0 (feature level 160).

[prod-jwt-auth]: https://zulip.readthedocs.io/en/latest/production/authentication-methods.html#json-web-tokens-jwt
</dd>
</dl>
</dd>
</dl>

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

client.authentication.jwt_fetch_api_key(
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhhbWxldEB6dWxpcC5jb20ifQ.EsHxSVt54zPR-ywgPH54TB1FYmrGKsfq7hsQEhp_9w0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` 

A JSON Web Token for the target user.

The token payload must contain a custom `email` claim with the target
user's email address, e.g., `{"email": "<target user email>"}`.
    
</dd>
</dl>

<dl>
<dd>

**include_profile:** `typing.Optional[bool]` 

Whether to include a `user` object containing the target
user's profile details in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">dev_fetch_api_key</a>(...) -> ApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For easy testing of mobile apps and other clients and against Zulip
development servers, we support fetching a Zulip API key for any user
on the development server without authentication (so that they can
implement analogues of the one-click login process available for Zulip
development servers on the web).

!!! warn ""

    **Note:** This endpoint is only available on Zulip development
    servers; for obvious security reasons it will always return an error
    in a Zulip production server.
</dd>
</dl>
</dd>
</dl>

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

client.authentication.dev_fetch_api_key(
    username="iago@zulip.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` — The email address for the user that owns the API key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">dev_list_users</a>() -> DevListUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all, non-bot users in a [Zulip development
server](https://zulip.readthedocs.io/en/latest/development/overview.html).
This endpoint is used by mobile developers to fetch users for the
development login flow.

!!! warn ""

    **Note:** This endpoint is only available on Zulip development
    servers; for obvious security reasons it will always return an error
    in a Zulip production server.
</dd>
</dl>
</dd>
</dl>

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

client.authentication.dev_list_users()

```
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

## RealTimeEvents
<details><summary><code>client.real_time_events.<a href="src/fern/real_time_events/client.py">get_events</a>(...) -> GetEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to receive new events from
[a registered event queue](/api/register-queue).

Long-lived clients should use the
`event_queue_longpoll_timeout_seconds` property returned by
`POST /register` as the client-side HTTP request timeout for
calls to this endpoint. It is guaranteed to be higher than
heartbeat frequency and should be respected by clients to
avoid breaking when heartbeat frequency increases.
</dd>
</dl>
</dd>
</dl>

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

client.real_time_events.get_events(
    queue_id="fb67bf8a-c031-47cc-84cf-ed80accacda8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` 

The ID of an event queue that was previously registered via
`POST /api/v1/register` (see [Register a queue](/api/register-queue)).
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[int]` 

The highest event ID in this queue that you've received and
wish to acknowledge. See the [code for
`call_on_each_event`](https://github.com/zulip/python-zulip-api/blob/main/zulip/zulip/__init__.py)
in the [zulip Python
module](https://github.com/zulip/python-zulip-api) for an
example implementation of correctly processing each event
exactly once.
    
</dd>
</dl>

<dl>
<dd>

**dont_block:** `typing.Optional[bool]` 

Set to `true` if the client is requesting a nonblocking reply. If not
specified, the request will block until either a new event is available
or a few minutes have passed, in which case the server will send the
client a heartbeat event.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.real_time_events.<a href="src/fern/real_time_events/client.py">delete_queue</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a previously registered queue.
</dd>
</dl>
</dd>
</dl>

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

client.real_time_events.delete_queue(
    queue_id="fb67bf8a-c031-47cc-84cf-ed80accacda8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` 

The ID of an event queue that was previously registered via
`POST /api/v1/register` (see [Register a queue](/api/register-queue)).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.real_time_events.<a href="src/fern/real_time_events/client.py">register_queue</a>(...) -> RegisterQueueResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This powerful endpoint can be used to register a Zulip "event queue"
(subscribed to certain types of "events", or updates to the messages
and other Zulip data the current user has access to), as well as to
fetch the current state of that data.

(`register` also powers the `call_on_each_event` Python API, and is
intended primarily for complex applications for which the more convenient
`call_on_each_event` API is insufficient).

This endpoint returns a `queue_id` and a `last_event_id`; these can be
used in subsequent calls to the
["events" endpoint](/api/get-events) to request events from
the Zulip server using long-polling.

The server will queue events for up to 10 minutes of inactivity.
After 10 minutes, your event queue will be garbage-collected. The
server will send `heartbeat` events every minute, which makes it easy
to implement a robust client that does not miss events unless the
client loses network connectivity with the Zulip server for 10 minutes
or longer.

Once the server garbage-collects your event queue, the server will
[return an error](/api/get-events#bad_event_queue_id-errors)
with a code of `BAD_EVENT_QUEUE_ID` if you try to fetch events from
the event queue. Your software will need to handle that error
condition by re-initializing itself (e.g. this is what triggers your
browser reloading the Zulip web app when your laptop comes back online
after being offline for more than 10 minutes).

When prototyping with this API, we recommend first calling `register`
with no `event_types` parameter to see all the available data from all
supported event types. Before using your client in production, you
should set appropriate `event_types` and `fetch_event_types` filters
so that your client only requests the data it needs. A few minutes
doing this often saves 90% of the total bandwidth and other resources
consumed by a client using this API.

See the [events system developer documentation][events-system-docs]
if you need deeper details about how the Zulip event queue system
works, avoids clients needing to worry about large classes of
potentially messy races, etc.

**Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
as we now have `web_font_size_px` and `web_line_height_percent`
settings for more control.

Before Zulip 7.0 (feature level 183), the
`realm_community_topic_editing_limit_seconds` property
was returned by the response. It was removed because it
had not been in use since the realm setting
`move_messages_within_stream_limit_seconds` was introduced
in feature level 162.

In Zulip 7.0 (feature level 163), the realm setting
`email_address_visibility` was removed. It was replaced by a [user
setting](/api/update-settings#parameter-email_address_visibility) with
a [realm user default][user-defaults], with the encoding of different
values preserved. Clients can support all versions by supporting the
current API and treating every user as having the realm's
`email_address_visibility` value.

[user-defaults]: /api/update-realm-user-settings-defaults#parameter-email_address_visibility
[events-system-docs]: https://zulip.readthedocs.io/en/latest/subsystems/events-system.html
</dd>
</dl>
</dd>
</dl>

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

client.real_time_events.register_queue()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**apply_markdown:** `typing.Optional[bool]` 

Set to `true` if you would like the content to be rendered in HTML
format (otherwise the API will return the raw text that the user
entered)
    
</dd>
</dl>

<dl>
<dd>

**client_gravatar:** `typing.Optional[bool]` 

Whether the client supports computing gravatars URLs. If
enabled, `avatar_url` will be included in the response only
if there is a Zulip avatar, and will be `null` for users who
are using gravatar as their avatar. This option
significantly reduces the compressed size of user data,
since gravatar URLs are long, random strings and thus do not
compress well. The `client_gravatar` field is set to `true` if
clients can compute their own gravatars.

The default value is `true` for authenticated requests and
`false` for [unauthenticated
requests](/help/public-access-option). Passing `true` in
an unauthenticated request is an error.

**Changes**: Before Zulip 6.0 (feature level 149), this
parameter was silently ignored and processed as though it
were `false` in unauthenticated requests.
    
</dd>
</dl>

<dl>
<dd>

**include_subscribers:** `typing.Optional[RegisterQueueRequestIncludeSubscribers]` 

Whether each returned channel object should include a `subscribers`
field containing a list of the user IDs of its subscribers.

Client apps supporting organizations with many thousands of users
should not pass `true`, because the full subscriber matrix may be
several megabytes of data. The `partial` value, combined with the
`subscriber_count` and fetching subscribers for individual channels as
needed, is recommended to support client app features where channel
subscriber data is useful.

If a client passes `partial` for this parameter, the server may,
for some channels, return a subset of the channel's subscribers
in the `partial_subscribers` field instead of the `subscribers` field,
which always contains the complete set of subscribers.

The server guarantees that it will always return a `subscribers`
field for channels with fewer than 250 total subscribers. When
returning a `partial_subscribers` field, the server guarantees
that all bot users and users active within the last 14 days will
be included. For other cases, the server may use its discretion
to determine which channels and users to include, balancing between
payload size and usefulness of the data provided to the client.

Passing `true` in an [unauthenticated
request](/help/public-access-option) is an error.

**Changes**: The `partial` value is new in Zulip 11.0 (feature level 412).

Before Zulip 6.0 (feature level 149), this parameter was silently
ignored and processed as though it were `false` in unauthenticated
requests.

New in Zulip 2.1.0.
    
</dd>
</dl>

<dl>
<dd>

**slim_presence:** `typing.Optional[bool]` 

If `true`, the `presences` object returned in the response will be keyed
by user ID and the entry for each user's presence data will be in the
modern format.

**Changes**: New in Zulip 3.0 (no feature level; API unstable).
    
</dd>
</dl>

<dl>
<dd>

**presence_history_limit_days:** `typing.Optional[int]` 

Limits how far back in time to fetch user presence data. If not specified,
defaults to 14 days. A value of N means that the oldest presence data
fetched will be from at most N days ago.

**Changes**: New in Zulip 10.0 (feature level 288).
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[EventTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**all_public_streams:** `typing.Optional[AllPublicChannels]` 
    
</dd>
</dl>

<dl>
<dd>

**client_capabilities:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Dictionary containing details on features the client supports that are
relevant to the format of responses sent by the server.

- `notification_settings_null`: Boolean for whether the
  client can handle the current API with `null` values for
  channel-level notification settings (which means the channel
  is not customized and should inherit the user's global
  notification settings for channel messages).
  <br />
  **Changes**: New in Zulip 2.1.0. In earlier Zulip releases,
  channel-level notification settings were simple booleans.

- `bulk_message_deletion`: Boolean for whether the client's
  handler for the `delete_message` event type has been
  updated to process the new bulk format (with a
  `message_ids`, rather than a singleton `message_id`).
  Otherwise, the server will send `delete_message` events
  in a loop.
  <br />
  **Changes**: New in Zulip 3.0 (feature level 13). This
  capability is for backwards-compatibility; it will be
  required in a future server release.

- `user_avatar_url_field_optional`: Boolean for whether the
  client required avatar URLs for all users, or supports
  using `GET /avatar/{user_id}` to access user avatars. If the
  client has this capability, the server may skip sending a
  `avatar_url` field in the `realm_user` at its sole discretion
  to optimize network performance. This is an important optimization
  in organizations with 10,000s of users.
  <br />
  **Changes**: New in Zulip 3.0 (feature level 18).

- `stream_typing_notifications`: Boolean for whether the client
  supports channel typing notifications.
  <br />
  **Changes**: New in Zulip 4.0 (feature level 58). This capability is
  for backwards-compatibility; it will be required in a
  future server release.

- `user_settings_object`: Has no effect with modern servers. Previously,
  this was a boolean for whether the client supported the modern
  [`user_settings` event type](/api/get-events#user_settings-update) and
  the top-level `user_settings` object in this endpoint's response.
  <br />
  **Changes**: Prior to Zulip 12.0 (feature level 439), if false, the
  server would additionally send the legacy `update_global_notifications`
  and `update_display_settings` event types, if requested.
  <br />
  New in Zulip 5.0 (feature level 89). Because the feature level 89 API
  changes were merged together, clients could safely make a request with
  this client capability, and also request all three event types
  (`user_settings`, `update_display_settings`, and
  `update_global_notifications`), and then use the `zulip_feature_level`
  in this endpoint's response or the presence/absence of a `user_settings`
  key to determine where to look for the data.

- `linkifier_url_template`: Boolean for whether the client accepts
  [linkifiers][help-linkifiers] that use [RFC 6570][rfc6570] compliant
  URL templates for linkifying matches. If false or unset, then the
  `realm_linkifiers` array in the `/register` response will be empty
  if present, and no `realm_linkifiers` [events][events-linkifiers]
  will be sent to the client.
  <br />
  **Changes**: New in Zulip 7.0 (feature level 176). This capability
  is for backwards-compatibility.

- `user_list_incomplete`: Boolean for whether the client supports not having an
  incomplete user database. If true, then the `realm_users` array in the `register`
  response will not include data for inaccessible users and clients of guest users will
  not receive `realm_user op:add` events for newly created users that are not accessible
  to the current user.
  <br />
  **Changes**: New in Zulip 8.0 (feature level 232). This
  capability is for backwards-compatibility.

- `include_deactivated_groups`: Boolean for whether the client can handle
  deactivated user groups by themselves. If false, then the `realm_user_groups`
  array in the `/register` response will only include active groups, clients
  will receive a `remove` event instead of `update` event when a group is
  deactivated and no `update` event will be sent to the client if a deactivated
  user group is renamed.
  <br />
  **Changes**: New in Zulip 10.0 (feature level 294). This
  capability is for backwards-compatibility.

- `archived_channels`: Boolean for whether the client supports processing
  [archived channels](/help/archive-a-channel) in the `stream` and
  `subscription` event types. If `false`, the server will not include data
  related to archived channels in the `register` response or in events.
  <br />
  **Changes**: New in Zulip 10.0 (feature level 315). This allows clients to
  access archived channels, without breaking backwards-compatibility for
  existing clients.

- `empty_topic_name`: Boolean for whether the client supports processing
  the empty string as a topic name. Clients not declaring this capability
  will be sent the value of `realm_empty_topic_display_name` found in the
  [POST /register](/api/register-queue) response instead of the empty string
  wherever topic names appear in the register response or events involving
  topic names.
  <br/>
  **Changes**: New in Zulip 10.0 (feature level 334). Previously,
  the empty string was not a valid topic name.

- `simplified_presence_events`: Boolean for whether the client supports
  receiving the [`presence` event type](/api/get-events#presence) with
  user presence data in the modern format. If true, the server will
  send these events with the `presences` field that has the user presence
  data in the modern format. Otherwise, these event will contain fields
  with legacy format user presence data.
  <br />
  **Changes**: New in Zulip 11.0 (feature level 419).

[help-linkifiers]: /help/add-a-custom-linkifier
[rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html
[events-linkifiers]: /api/get-events#realm_linkifiers
    
</dd>
</dl>

<dl>
<dd>

**fetch_event_types:** `typing.Optional[typing.List[str]]` 

Same as the `event_types` parameter except that the values in
`fetch_event_types` are used to fetch initial data. If
`fetch_event_types` is not provided, `event_types` is used and if
`event_types` is not provided, this parameter defaults to `null`.

Event types not supported by the server are ignored, in order to simplify
the implementation of client apps that support multiple server versions.
    
</dd>
</dl>

<dl>
<dd>

**narrow:** `typing.Optional[Narrow]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.real_time_events.<a href="src/fern/real_time_events/client.py">post_real_time</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

(Ignored)
</dd>
</dl>
</dd>
</dl>

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

client.real_time_events.post_real_time()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_types:** `typing.Optional[EventTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**narrow:** `typing.Optional[Narrow]` 
    
</dd>
</dl>

<dl>
<dd>

**all_public_streams:** `typing.Optional[AllPublicChannels]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.real_time_events.<a href="src/fern/real_time_events/client.py">rest_error_handling</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Common error to many endpoints
</dd>
</dl>
</dd>
</dl>

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

client.real_time_events.rest_error_handling()

```
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

## Channels
<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_stream_id</a>(...) -> GetStreamIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the unique ID of a given channel.
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_stream_id(
    stream="Denmark",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream:** `str` — The name of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">add_default_stream</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a channel to the set of [default channels][default-channels]
for new users joining the organization.

[default-channels]: /help/set-default-channels-for-new-users
</dd>
</dl>
</dd>
</dl>

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

client.channels.add_default_stream(
    stream_id=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the target channel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">remove_default_stream</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a channel from the set of [default channels][default-channels]
for new users joining the organization.

[default-channels]: /help/set-default-channels-for-new-users
</dd>
</dl>
</dd>
</dl>

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

client.channels.remove_default_stream(
    stream_id=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the target channel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_stream_topics</a>(...) -> GetStreamTopicsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all topics the user has access to in a specific channel.

Note that for [private channels with
protected history](/help/channel-permissions#private-channels),
the user will only have access to topics of messages sent after they
[subscribed to](/api/subscribe) the channel. Similarly, a user's
[bot](/help/bots-overview#bot-type) will only have access to messages
sent after the bot was subscribed to the channel, instead of when the
user subscribed.

**Changes**: Before Zulip 12.0 (feature level 480), this
endpoint was not supported for archived channels.
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_stream_topics(
    stream_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**allow_empty_topic_name:** `typing.Optional[bool]` 

Whether the client supports processing the empty string as
a topic name in the returned data.

If `false`, the value of `realm_empty_topic_display_name`
found in the [`POST /register`](/api/register-queue) response is
returned replacing the empty string as the topic name.

**Changes**: New in Zulip 10.0 (feature level 334). Previously,
the empty string was not a valid topic.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_subscriptions</a>(...) -> GetSubscriptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all channels that the user is subscribed to.
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_subscribers:** `typing.Optional[GetSubscriptionsRequestIncludeSubscribers]` 

Whether each returned channel object should include a `subscribers`
field containing a list of the user IDs of its subscribers.

Client apps supporting organizations with many thousands of users
should not pass `true`, because the full subscriber matrix may be
several megabytes of data. The `partial` value, combined with the
`subscriber_count` and fetching subscribers for individual channels as
needed, is recommended to support client app features where
channel subscriber data is useful.

If a client passes `partial` for this parameter, the server may,
for some channels, return a subset of the channel's subscribers
in the `partial_subscribers` field instead of the `subscribers` field,
which always contains the complete set of subscribers.

The server guarantees that it will always return a `subscribers`
field for channels with fewer than 250 total subscribers. When
returning a `partial_subscribers` field, the server guarantees
that all bot users and users active within the last 14 days will
be included. For other cases, the server may use its discretion
to determine which channels and users to include, balancing between
payload size and usefulness of the data provided to the client.

**Changes**: The `partial` value is new in Zulip 11.0 (feature level 412).

New in Zulip 2.1.0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">subscribe</a>(...) -> SubscribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribe one or more users to one or more channels.

If any of the specified channels do not exist, they are automatically
created. The initial [channel settings](/api/update-stream) will be determined
by the optional parameters, like `invite_only`, detailed below.

Note that the ability to subscribe oneself and/or other users
to a specified channel depends on the [channel's permissions
settings](/help/channel-permissions).

**Changes**: Before Zulip 10.0 (feature level 362),
subscriptions in archived channels could not be modified.

Before Zulip 10.0 (feature level 357), the
`can_subscribe_group` permission, which allows members of the
group to subscribe themselves to the channel, did not exist.

Before Zulip 10.0 (feature level 349), a user cannot subscribe
other users to a private channel without being subscribed
to that channel themselves. Now, If a user is part of
`can_add_subscribers_group`, they can subscribe themselves or other
users to a private channel without being subscribed to that channel.

Removed `stream_post_policy` and `is_announcement_only`
parameters in Zulip 10.0 (feature level 333), as permission to post
in the channel is now controlled by `can_send_message_group`.

Before Zulip 8.0 (feature level 208), if a user specified by the
[`principals`][principals-param] parameter was a deactivated user,
or did not exist, then an HTTP status code of 403 was returned with
`code: "UNAUTHORIZED_PRINCIPAL"` in the error response. As of this
feature level, an HTTP status code of 400 is returned with
`code: "BAD_REQUEST"` in the error response for these cases.

[principals-param]: /api/subscribe#parameter-principals
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.channels import SubscribeRequestSubscriptionsItem

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.subscribe(
    subscriptions=[
        SubscribeRequestSubscriptionsItem(
            name="Verona",
            description="Italian city",
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

**subscriptions:** `typing.List[SubscribeRequestSubscriptionsItem]` 

A list of dictionaries containing the key `name` and value
specifying the name of the channel to subscribe. If the channel does not
exist a new channel is created. The description of the channel created can
be specified by setting the dictionary key `description` with an
appropriate value.
    
</dd>
</dl>

<dl>
<dd>

**principals:** `typing.Optional[Principals]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization_errors_fatal:** `typing.Optional[bool]` 

A boolean specifying whether authorization errors (such as when the
requesting user is not authorized to access a private channel) should be
considered fatal or not. When `true`, an authorization error is reported
as such. When set to `false`, the response will be a 200 and any channels
where the request encountered an authorization error will be listed
in the `unauthorized` key.
    
</dd>
</dl>

<dl>
<dd>

**announce:** `typing.Optional[bool]` 

If one of the channels specified did not exist previously and is thus created
by this call, this determines whether [notification bot](/help/configure-automated-notices)
will send an announcement about the new channel's creation.
    
</dd>
</dl>

<dl>
<dd>

**invite_only:** `typing.Optional[bool]` 

As described above, this endpoint will create a new channel if passed
a channel name that doesn't already exist. This parameters and the ones
that follow are used to request an initial configuration of a created
channel; they are ignored for channels that already exist.

This parameter determines whether any newly created channels will be
private channels.
    
</dd>
</dl>

<dl>
<dd>

**is_web_public:** `typing.Optional[bool]` 

This parameter determines whether any newly created channels will be
web-public channels.

Note that creating web-public channels requires the
`WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
to be enabled on the Zulip server in question, the organization
to have enabled the `enable_spectator_access` realm setting, and
the current use to have permission under the organization's
`can_create_web_public_channel_group` realm setting.

[server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

**Changes**: New in Zulip 5.0 (feature level 98).
    
</dd>
</dl>

<dl>
<dd>

**is_default_stream:** `typing.Optional[bool]` 

This parameter determines whether any newly created channels will be
added as [default channels][default-channels] for new users joining
the organization.

[default-channels]: /help/set-default-channels-for-new-users

**Changes**: New in Zulip 8.0 (feature level 200). Previously, default channel status
could only be changed using the [dedicated API endpoint](/api/add-default-stream).
    
</dd>
</dl>

<dl>
<dd>

**history_public_to_subscribers:** `typing.Optional[HistoryPublicToSubscribers]` 
    
</dd>
</dl>

<dl>
<dd>

**message_retention_days:** `typing.Optional[MessageRetentionDays]` 
    
</dd>
</dl>

<dl>
<dd>

**topics_policy:** `typing.Optional[TopicsPolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**can_add_subscribers_group:** `typing.Optional[ChannelCanAddSubscribersGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_remove_subscribers_group:** `typing.Optional[CanRemoveSubscribersGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_administer_channel_group:** `typing.Optional[CanAdministerChannelGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_delete_any_message_group:** `typing.Optional[CanDeleteAnyMessageGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_delete_own_message_group:** `typing.Optional[CanDeleteOwnMessageGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_move_messages_out_of_channel_group:** `typing.Optional[CanMoveMessagesOutOfChannelGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_move_messages_within_channel_group:** `typing.Optional[CanMoveMessagesWithinChannelGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_send_message_group:** `typing.Optional[CanSendMessageGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_subscribe_group:** `typing.Optional[CanSubscribeGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_resolve_topics_group:** `typing.Optional[CanResolveTopicsGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_create_topic_group:** `typing.Optional[CanCreateTopicGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` 

This parameter adds the newly created channel to the specified
[channel folder](/help/channel-folders).

**Changes**: New in Zulip 11.0 (feature level 389).
    
</dd>
</dl>

<dl>
<dd>

**send_new_subscription_messages:** `typing.Optional[SendNewSubscriptionMessages]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">unsubscribe</a>(...) -> UnsubscribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unsubscribe yourself or other users from one or more channels.

In addition to managing the current user's subscriptions, this
endpoint can be used to remove other users from channels. This
is possible in 3 situations:

- Organization administrators can remove any user from any
  channel.
- Users can remove a bot that they own from any channel that
  the user [can access](/help/channel-permissions).
- Users can unsubscribe any user from a channel if they [have
  access](/help/channel-permissions) to the channel and are a
  member of the [user group](/api/get-user-groups) specified
  by the [`can_remove_subscribers_group`][can-remove-parameter]
  for the channel.

**Changes**: Before Zulip 10.0 (feature level 362),
subscriptions in archived channels could not be modified.

Before Zulip 8.0 (feature level 208), if a user specified by
the [`principals`][principals-param] parameter was a
deactivated user, or did not exist, then an HTTP status code
of 403 was returned with `code: "UNAUTHORIZED_PRINCIPAL"` in
the error response. As of this feature level, an HTTP status
code of 400 is returned with `code: "BAD_REQUEST"` in the
error response for these cases.

Before Zulip 8.0 (feature level 197),
the `can_remove_subscribers_group` setting
was named `can_remove_subscribers_group_id`.

Before Zulip 7.0 (feature level 161), the
`can_remove_subscribers_group_id` for all channels was always
the system group for organization administrators.

Before Zulip 6.0 (feature level 145), users had no special
privileges for managing bots that they own.

[principals-param]: /api/unsubscribe#parameter-principals
[can-remove-parameter]: /api/subscribe#parameter-can_remove_subscribers_group
</dd>
</dl>
</dd>
</dl>

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

client.channels.unsubscribe(
    subscriptions=[
        "Verona",
        "Denmark"
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

**subscriptions:** `typing.List[str]` 

A list of channel names to unsubscribe from. This parameter is called
`streams` in our Python API.
    
</dd>
</dl>

<dl>
<dd>

**principals:** `typing.Optional[Principals]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">update_subscriptions</a>(...) -> UpdateSubscriptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update which channels you are subscribed to.

**Changes**: Before Zulip 10.0 (feature level 362),
subscriptions in archived channels could not be modified.
</dd>
</dl>
</dd>
</dl>

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

client.channels.update_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**delete:** `typing.Optional[typing.List[str]]` — A list of channel names to unsubscribe from.
    
</dd>
</dl>

<dl>
<dd>

**add:** `typing.Optional[typing.List[UpdateSubscriptionsRequestAddItem]]` 

A list of objects describing which channels to subscribe to, optionally
including per-user subscription parameters (e.g. color) and if the
channel is to be created, its description.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">mute_topic</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Mute or unmute a topic](/help/mute-a-topic) within a channel that
the current user is subscribed to.

**Changes**: Deprecated in Zulip 7.0 (feature level 170). Clients connecting
to newer servers should use the [POST /user_topics](/api/update-user-topic)
endpoint, as this endpoint may be removed in a future release.

Before Zulip 7.0 (feature level 169), this endpoint
returned an error if asked to mute a topic that was already muted
or asked to unmute a topic that had not previously been muted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.channels import MuteTopicRequestOp

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.mute_topic(
    topic="dinner",
    op=MuteTopicRequestOp.ADD,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**topic:** `str` 

The topic to (un)mute. Note that the request will succeed regardless of
whether any messages have been sent to the specified topic.

Clients should use the `max_topic_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum topic length.
    
</dd>
</dl>

<dl>
<dd>

**op:** `MuteTopicRequestOp` — Whether to mute (`add`) or unmute (`remove`) the provided topic.
    
</dd>
</dl>

<dl>
<dd>

**stream_id:** `typing.Optional[int]` 

The ID of the channel to access.

Clients must provide either `stream` or `stream_id` as a parameter
to this endpoint, but not both.

**Changes**: New in Zulip 2.0.0.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[str]` 

The name of the channel to access.

Clients must provide either `stream` or `stream_id` as a parameter
to this endpoint, but not both. Clients should use `stream_id`
instead of the `stream` parameter when possible.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">update_user_topic</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to update the personal preferences for a topic,
such as the topic's visibility policy, which is used to implement
[mute a topic](/help/mute-a-topic) and related features.

This endpoint can be used to update the visibility policy for the single
channel and topic pair indicated by the parameters for a user.

**Changes**: New in Zulip 7.0 (feature level 170). Previously,
toggling whether a topic was muted or unmuted was managed by the
[PATCH /users/me/subscriptions/muted_topics](/api/mute-topic) endpoint.
</dd>
</dl>
</dd>
</dl>

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

client.channels.update_user_topic(
    stream_id=1,
    topic="dinner",
    visibility_policy=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**topic:** `str` 

The topic for which the personal preferences needs to be updated.
Note that the request will succeed regardless of whether
any messages have been sent to the specified topic.

Clients should use the `max_topic_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum topic length.

Note: When the value of `realm_empty_topic_display_name` found in
the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

**Changes**: Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**visibility_policy:** `int` 

Controls which visibility policy to set.

- 0 = None. Removes the visibility policy previously set for the topic.
- 1 = Muted. [Mutes the topic](/help/mute-a-topic) in a channel.
- 2 = Unmuted. [Unmutes the topic](/help/mute-a-topic) in a muted channel.
- 3 = Followed. [Follows the topic](/help/follow-a-topic).

In an unmuted channel, a topic visibility policy of unmuted will have the
same effect as the "None" visibility policy.

**Changes**: In Zulip 7.0 (feature level 219), added followed as
a visibility policy option.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_subscription_status</a>(...) -> GetSubscriptionStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check whether a user is subscribed to a channel.

**Changes**: Prior to Zulip 12.0 (feature level 458), this endpoint
did not support querying subscriptions of bot users.

New in Zulip 3.0 (feature level 12).
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_subscription_status(
    user_id=1,
    stream_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_user_channels</a>(...) -> GetUserChannelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the list of channels that the target user is subscribed to.

The [channel security model](/help/channel-permissions) means only those
subscribed channels to which the acting user has metadata access are
returned.

For organization administrators, this is guaranteed to be all channels
the target user is subscribed to, since organization administrators
implicitly have metadata access to all channels.

**Changes**: Prior to Zulip 12.0 (feature level 458), target users that
were bots resulted in a permissions error.

New in Zulip 12.0 (feature level 440).
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_user_channels(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">update_subscription_settings</a>(...) -> IgnoredParametersSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the current user's personal settings for channels they are
subscribed to. These settings include [color](/help/change-the-color-of-a-channel),
[muting](/help/mute-a-channel), [pinning](/help/pin-a-channel)
and [per-channel notification settings](/help/channel-notifications).

There is a single channel alternative to this bulk endpoint:
[`POST /users/me/subscriptions/{stream_id}`](/api/update-subscription-property).

**Changes**: Prior to Zulip 5.0 (feature level 111), the response object
included the `subscription_data` in the request. The endpoint now returns
the more ergonomic [`ignored_parameters_unsupported`][ignored-parameters]
array instead.

[ignored-parameters]: /api/rest-error-handling#ignored-parameters
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SubscriptionProperty
from fern.environment import FernApiEnvironment
from fern.channels import UpdateSubscriptionSettingsRequestSubscriptionDataItem

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.update_subscription_settings(
    subscription_data=[
        UpdateSubscriptionSettingsRequestSubscriptionDataItem(
            stream_id=1,
            property=SubscriptionProperty.PIN_TO_TOP,
            value=True,
        ),
        UpdateSubscriptionSettingsRequestSubscriptionDataItem(
            stream_id=3,
            property=SubscriptionProperty.COLOR,
            value="#f00f00",
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

**subscription_data:** `typing.List[UpdateSubscriptionSettingsRequestSubscriptionDataItem]` 

A list of objects that describe the changes that should be applied in
each subscription. Each object represents a subscription, and must have
a `stream_id` key that identifies the channel, as well as the `property`
being modified and its new `value`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">update_subscription_property</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the current user's personal settings for a specific channel they
are subscribed to. These settings include [color](/help/change-the-color-of-a-channel),
[muting](/help/mute-a-channel), [pinning](/help/pin-a-channel)
and [per-channel notification settings](/help/channel-notifications).

This is a single channel alternative to the bulk endpoint:
[`POST /users/me/subscriptions/properties`](/api/update-subscription-settings).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SubscriptionProperty
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.channels.update_subscription_property(
    stream_id=1,
    property=SubscriptionProperty.COLOR,
    value=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**property:** `SubscriptionProperty` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `SubscriptionPropertyValue` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_subscribers</a>(...) -> GetSubscribersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all users subscribed to a channel.

**Changes**: Before Zulip 12.0 (feature level 480), this
endpoint was not supported for archived channels.
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_subscribers(
    stream_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_streams</a>(...) -> GetStreamsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all channels that the user [has access to](/help/channel-permissions).
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_streams()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_public:** `typing.Optional[bool]` — Include all public channels.
    
</dd>
</dl>

<dl>
<dd>

**include_web_public:** `typing.Optional[bool]` — Include all web-public channels.
    
</dd>
</dl>

<dl>
<dd>

**include_subscribed:** `typing.Optional[bool]` — Include all channels that the user is subscribed to.
    
</dd>
</dl>

<dl>
<dd>

**exclude_archived:** `typing.Optional[bool]` 

Whether to exclude archived streams from the results.

**Changes**: New in Zulip 10.0 (feature level 315).
    
</dd>
</dl>

<dl>
<dd>

**include_all_active:** `typing.Optional[bool]` 

Deprecated parameter to include all channels. The user must
have administrative privileges to use this parameter.

**Changes**: Deprecated in Zulip 10.0 (feature level
356). Clients interacting with newer servers should use
the equivalent `include_all` parameter, which does not
incorrectly hint that this parameter, and not
`exclude_archived`, controls whether archived channels
appear in the response.
    
</dd>
</dl>

<dl>
<dd>

**include_all:** `typing.Optional[bool]` 

Include all channels that the user has metadata access to.

For organization administrators, this will be all channels
in the organization, since organization administrators
implicitly have metadata access to all channels.

**Changes**: New in Zulip 10.0 (feature level 356). On older
versions, use `include_all_active`, which this replaces.
    
</dd>
</dl>

<dl>
<dd>

**include_default:** `typing.Optional[bool]` — Include all default channels for the user's realm.
    
</dd>
</dl>

<dl>
<dd>

**include_owner_subscribed:** `typing.Optional[bool]` 

If the user is a bot, include all channels that the bot's owner is
subscribed to.
    
</dd>
</dl>

<dl>
<dd>

**include_can_access_content:** `typing.Optional[bool]` 

Include all the channels that the user has content access to.

**Changes**: New in Zulip 10.0 (feature level 356).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_stream_by_id</a>(...) -> GetStreamByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch details for the channel with the ID `stream_id`.

**Changes**: Before Zulip 12.0 (feature level 480), this
endpoint was not supported for archived channels.

New in Zulip 6.0 (feature level 132).
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_stream_by_id(
    stream_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">archive_stream</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Archive the channel](/help/archive-a-channel) with the ID `stream_id`.
</dd>
</dl>
</dd>
</dl>

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

client.channels.archive_stream(
    stream_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">update_stream</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure the channel with the ID `stream_id`. This endpoint supports
an organization administrator editing any property of a channel,
including:

- Channel [name](/help/rename-a-channel) and [description](/help/change-the-channel-description)
- Channel [permissions](/help/channel-permissions), including
  [privacy](/help/change-the-privacy-of-a-channel) and [who can
  send](/help/channel-posting-policy).

Note that an organization administrator's ability to change a
[private channel's permissions](/help/channel-permissions#private-channels)
depends on them being subscribed to the channel.

**Changes**: Before Zulip 10.0 (feature level 362), channel privacy could not be
edited for archived channels.

Removed `stream_post_policy` and `is_announcement_only`
parameters in Zulip 10.0 (feature level 333), as permission to post
in the channel is now controlled by `can_send_message_group`.
</dd>
</dl>
</dd>
</dl>

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

client.channels.update_stream(
    stream_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

The new [description](/help/change-the-channel-description) for
the channel, in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

Clients should use the `max_stream_description_length` returned
by the [`POST /register`](/api/register-queue) endpoint to
determine the maximum channel description length.

**Changes**: Removed unnecessary JSON-encoding of this parameter in
Zulip 4.0 (feature level 64).
    
</dd>
</dl>

<dl>
<dd>

**new_name:** `typing.Optional[str]` 

The new name for the channel.

Clients should use the `max_stream_name_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum channel name length.

**Changes**: Removed unnecessary JSON-encoding of this parameter in
Zulip 4.0 (feature level 64).
    
</dd>
</dl>

<dl>
<dd>

**is_private:** `typing.Optional[bool]` — Change whether the channel is a private channel.
    
</dd>
</dl>

<dl>
<dd>

**is_web_public:** `typing.Optional[bool]` 

Change whether the channel is a web-public channel.

Note that creating web-public channels requires the
`WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
to be enabled on the Zulip server in question, the organization
to have enabled the `enable_spectator_access` realm setting, and
the current use to have permission under the organization's
`can_create_web_public_channel_group` realm setting.

[server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

**Changes**: New in Zulip 5.0 (feature level 98).
    
</dd>
</dl>

<dl>
<dd>

**history_public_to_subscribers:** `typing.Optional[bool]` 

Whether the channel's message history should be available to
newly subscribed members, or users can only access messages
they actually received while subscribed to the channel.

Corresponds to the shared history option for
[private channels](/help/channel-permissions#private-channels).

It's an error for this parameter to be false for a public or
web-public channel and when is_private is false.

This can only be `false` if `can_create_topic_group` for the channel
is the `role:everyone` [system group][system-groups].

**Changes**: Before Zulip 6.0 (feature level 136), `history_public_to_subscribers`
was silently ignored unless the request also contained either `is_private` or
`is_web_public`.

[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**is_default_stream:** `typing.Optional[bool]` 

Add or remove the channel as a [default channel][default-channel]
for new users joining the organization.

[default-channel]: /help/set-default-channels-for-new-users

**Changes**: New in Zulip 8.0 (feature level 200). Previously, default channel status
could only be changed using the [dedicated API endpoint](/api/add-default-stream).
    
</dd>
</dl>

<dl>
<dd>

**message_retention_days:** `typing.Optional[MessageRetentionDays]` 
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` 

A boolean indicating whether the channel is
[archived](/help/archive-a-channel) or
unarchived. Currently only allows unarchiving
previously archived channels.

**Changes**: New in Zulip 11.0 (feature level 388).
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` 

ID of the new [channel folder](/help/channel-folders) to which the
channel should belong.

A `null` value indicates the user wants to remove the channel from its
current channel folder.

**Changes**: New in Zulip 11.0 (feature level 389).
    
</dd>
</dl>

<dl>
<dd>

**topics_policy:** `typing.Optional[TopicsPolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**can_add_subscribers_group:** `typing.Optional[UpdateStreamRequestCanAddSubscribersGroup]` 

The set of users who have permission to add subscribers to this
channel expressed as an [update to a group-setting
value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.

Users in this group need not be subscribed to a private channel to
add subscribers to it.

Note that a user must [have content access](/help/channel-permissions)
to a channel and permission to administer the channel in order to
modify this setting.

**Changes**: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.
    
</dd>
</dl>

<dl>
<dd>

**can_remove_subscribers_group:** `typing.Optional[UpdateStreamRequestCanRemoveSubscribersGroup]` 

The set of users who have permission to unsubscribe others from this
channel expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.

Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.

**Changes**: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part of `can_remove_subscribers_group`. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.

Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.

Before Zulip 8.0 (feature level 197), the `can_remove_subscribers_group`
setting was named `can_remove_subscribers_group_id`.

New in Zulip 7.0 (feature level 161).
    
</dd>
</dl>

<dl>
<dd>

**can_administer_channel_group:** `typing.Optional[UpdateStreamRequestCanAdministerChannelGroup]` 

The set of users who have permission to administer this channel
expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.

Note that a user must [have content access](/help/channel-permissions) to a
channel in order to add other subscribers to the channel.

**Changes**: Prior to Zulip 10.0 (feature level 349) a user needed to
[have content access](/help/channel-permissions) to a channel in order
to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without having
full access to the channel.

New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.
    
</dd>
</dl>

<dl>
<dd>

**can_delete_any_message_group:** `typing.Optional[UpdateStreamRequestCanDeleteAnyMessageGroup]` 

The set of users who have permission to delete any message in the channel
expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Note that a user must [have content access](/help/channel-permissions) to a
channel in order to delete any message in the channel.

Users present in the organization-level `can_delete_any_message_group` setting
can always delete any message in the channel if they
[have content access](/help/channel-permissions) to that channel.

**Changes**: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in `can_delete_any_message_group` were able
delete any message in the organization.
    
</dd>
</dl>

<dl>
<dd>

**can_delete_own_message_group:** `typing.Optional[UpdateStreamRequestCanDeleteOwnMessageGroup]` 

The set of users who have permission to delete the messages that they have
sent in the channel expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Note that a user must [have content access](/help/channel-permissions) to a
channel in order to delete their own message in the channel.

Users with permission to delete any message in the channel
and users present in the organization-level `can_delete_own_message_group` setting
can always delete their own messages in the channel if they
[have content access](/help/channel-permissions) to that channel.

**Changes**: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-level `can_delete_any_message_group`
and `can_delete_own_message_group` settings were able delete their own messages in
the organization.
    
</dd>
</dl>

<dl>
<dd>

**can_move_messages_out_of_channel_group:** `typing.Optional[UpdateStreamRequestCanMoveMessagesOutOfChannelGroup]` 

The set of users who have permission to move messages out of this channel
expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Note that a user must [have content access](/help/channel-permissions) to a
channel in order to move messages out of the channel.

Channel administrators and users present in the organization-level
`can_move_messages_between_channels_group` setting can always move messages
out of the channel if they [have content access](/help/channel-permissions) to
the channel.

**Changes**: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users in `can_move_messages_between_channels_group` were able
move messages between channels.
    
</dd>
</dl>

<dl>
<dd>

**can_move_messages_within_channel_group:** `typing.Optional[UpdateStreamRequestCanMoveMessagesWithinChannelGroup]` 

The set of users who have permission to move messages within this channel
expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Note that a user must [have content access](/help/channel-permissions) to a
channel in order to move messages within the channel.

Channel administrators and users present in the organization-level
`can_move_messages_between_topics_group` setting can always move messages
within the channel if they [have content access](/help/channel-permissions) to
the channel.

**Changes**: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users in `can_move_messages_between_topics_group` were able
move messages between topics of a channel.
    
</dd>
</dl>

<dl>
<dd>

**can_send_message_group:** `typing.Optional[UpdateStreamRequestCanSendMessageGroup]` 

The set of users who have permission to post in this channel
expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.

Note that using this permission to send a message to a new topic requires
also having permission to create new topics in the channel.

**Changes**: New in Zulip 10.0 (feature level 333). Previously
`stream_post_policy` field used to control the permission to
post in the channel.
    
</dd>
</dl>

<dl>
<dd>

**can_subscribe_group:** `typing.Optional[UpdateStreamRequestCanSubscribeGroup]` 

The set of users who have permission to subscribe themselves to this channel
expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.

Users in this group can subscribe to a private channel as well.

Note that a user must [have content access](/help/channel-permissions)
to a channel and permission to administer the channel in order to
modify this setting.

**Changes**: New in Zulip 10.0 (feature level 357).
    
</dd>
</dl>

<dl>
<dd>

**can_resolve_topics_group:** `typing.Optional[UpdateStreamRequestCanResolveTopicsGroup]` 

The set of users who have permission to to resolve topics in this channel
expressed as an [update to a group-setting value][update-group-setting].

[update-group-setting]: /api/group-setting-values#updating-group-setting-values

Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.

**Changes**: New in Zulip 11.0 (feature level 402).
    
</dd>
</dl>

<dl>
<dd>

**can_create_topic_group:** `typing.Optional[UpdateStreamRequestCanCreateTopicGroup]` 

The set of users who have permission to create new topics in this channel
expressed as an [update to a group-setting value][update-group-setting].

Note that using this permission requires also having permission to send
messages in the channel.

For [private channels with protected history](/help/channel-permissions#private-channels),
this setting can only be set to `role:everyone` [system group][system-groups].

**Changes**: New in Zulip 12.0 (feature level 441). Previously, if you
could send messages in a channel, you could create topics in the channel.

[update-group-setting]: /api/group-setting-values#updating-group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_stream_email_address</a>(...) -> GetStreamEmailAddressResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get email address of a channel.

Note that only users with permission to post messages in the channel
can access the channel's email address.

**Changes**: Prior to Zulip 12.0 (feature level 448), users without
permission to post messages in the channel could access the channel's email
if they had metadata access.

New in Zulip 8.0 (feature level 226).
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_stream_email_address(
    stream_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[int]` 

The ID of a user or bot which should appear as the sender when messages
are sent to the channel using the returned channel email address.

`sender_id` can be:

- ID of the current user.
- ID of the Email gateway bot. (Default value)
- ID of a bot owned by the current user.

**Changes**: New in Zulip 10.0 (feature level 335).

Previously, the sender was always Email gateway bot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">delete_topic</a>(...) -> DeleteTopicResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all messages in a topic.

Topics are a field on messages (not an independent data structure), so
deleting all the messages in the topic deletes the topic from Zulip.

Because this endpoint deletes messages in batches, it is possible for
the request to time out after only deleting some messages in the topic.
When this happens, the `complete` boolean field in the success response
will be `false`. Clients should repeat the request when handling such a
response. If all messages in the topic were deleted, then the success
response will return `"complete": true`.

**Changes**: Before Zulip 9.0 (feature level 256), the server never sent
[`stream` op: `update`](/api/get-events#stream-update) events with an
updated `first_message_id` for a channel when the oldest message that
had been sent to it changed.

Before Zulip 8.0 (feature level 211), if the server's
processing was interrupted by a timeout, but some messages in the topic
were deleted, then it would return `"result": "partially_completed"`,
along with a `code` field for an error string, in the success response
to indicate that there was a timeout and that the client should repeat
the request.

As of Zulip 6.0 (feature level 154), instead of returning an error
response when a request times out after successfully deleting some of
the messages in the topic, a success response is returned with
`"result": "partially_completed"` to indicate that some messages were
deleted.

Before Zulip 6.0 (feature level 147), this request did a single atomic
operation, which could time out for very large topics. As of this
feature level, messages are deleted in batches, starting with the newest
messages, so that progress is made even if the request times out and
returns an error.
</dd>
</dl>
</dd>
</dl>

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

client.channels.delete_topic(
    stream_id=1,
    topic_name="new coffee machine",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**topic_name:** `str` 

The name of the topic to delete.

Note: When the value of `realm_empty_topic_display_name` found in
the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

**Changes**: Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">create_channel</a>(...) -> CreateChannelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [channel](/help/create-channels), and optionally subscribe
users to the newly created channel.

The initial [channel settings](/api/update-stream) will be determined
by the optional parameters, like `invite_only`, detailed below.

**Changes**: New in Zulip 11.0 (feature level 417). Previously, this was
only possible via the [`POST /api/subscribe`](/api/subscribe) endpoint,
which handles both channel subscription and creation.
</dd>
</dl>
</dd>
</dl>

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

client.channels.create_channel(
    name="music",
    subscribers=[
        17,
        12
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

**name:** `str` 

The name of the new channel.

Clients should use the `max_stream_name_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum channel name length.
    
</dd>
</dl>

<dl>
<dd>

**subscribers:** `typing.List[int]` — A list of user IDs of the users to be subscribed to the new channel.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

The [description](/help/change-the-channel-description)
to use for the new channel being created, in text/markdown format.

Clients should use the `max_stream_description_length` returned
by the [`POST /register`](/api/register-queue) endpoint to
determine the maximum channel description length.
    
</dd>
</dl>

<dl>
<dd>

**announce:** `typing.Optional[bool]` 

This determines whether [notification bot](/help/configure-automated-notices)
will send an announcement about the new channel's creation.
    
</dd>
</dl>

<dl>
<dd>

**invite_only:** `typing.Optional[bool]` 

This parameter and the ones that follow are used to request an initial
configuration of the new channel.

This parameter determines whether the newly created channel will be
a [private channel](/help/channel-permissions#private-channels).
    
</dd>
</dl>

<dl>
<dd>

**is_web_public:** `typing.Optional[bool]` 

This parameter determines whether the newly created channel will be
a web-public channel.

Note that creating web-public channels requires the
`WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
to be enabled on the Zulip server in question, the organization
to have enabled the `enable_spectator_access` realm setting, and
the current user to have permission under the organization's
`can_create_web_public_channel_group` realm setting.

[server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html
    
</dd>
</dl>

<dl>
<dd>

**is_default_stream:** `typing.Optional[bool]` 

This parameter determines whether the newly created channel will be
added as a [default channel][default-channels] for new users joining
the organization.

[default-channels]: /help/set-default-channels-for-new-users
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` 

This parameter adds the newly created channel to the specified
[channel folder](/help/channel-folders).

**Changes**: New in Zulip 11.0 (feature level 389).
    
</dd>
</dl>

<dl>
<dd>

**topics_policy:** `typing.Optional[TopicsPolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**history_public_to_subscribers:** `typing.Optional[HistoryPublicToSubscribers]` 
    
</dd>
</dl>

<dl>
<dd>

**message_retention_days:** `typing.Optional[MessageRetentionDays]` 
    
</dd>
</dl>

<dl>
<dd>

**can_add_subscribers_group:** `typing.Optional[ChannelCanAddSubscribersGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_create_topic_group:** `typing.Optional[CanCreateTopicGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_delete_any_message_group:** `typing.Optional[CanDeleteAnyMessageGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_delete_own_message_group:** `typing.Optional[CanDeleteOwnMessageGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_remove_subscribers_group:** `typing.Optional[CanRemoveSubscribersGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_administer_channel_group:** `typing.Optional[CanAdministerChannelGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_move_messages_out_of_channel_group:** `typing.Optional[CanMoveMessagesOutOfChannelGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_move_messages_within_channel_group:** `typing.Optional[CanMoveMessagesWithinChannelGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_send_message_group:** `typing.Optional[CanSendMessageGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_subscribe_group:** `typing.Optional[CanSubscribeGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**can_resolve_topics_group:** `typing.Optional[CanResolveTopicsGroup]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">create_channel_folder</a>(...) -> CreateChannelFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [channel folder](/help/channel-folders).

**Changes**: New in Zulip 11.0 (feature level 389).
</dd>
</dl>
</dd>
</dl>

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

client.channels.create_channel_folder(
    name="marketing",
)

```
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

The name of the channel folder.

Clients should use the `max_channel_folder_name_length` returned
by the [`POST /register`](/api/register-queue) endpoint to determine
the maximum channel folder name length.

Value cannot be an empty string.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

The description of the channel folder.

Clients should use the `max_channel_folder_description_length`
returned by the [`POST /register`](/api/register-queue) endpoint
to determine the maximum channel folder description length.

Note that this parameter must be passed as part of the request,
but can be an empty string if no description for the new channel
folder is desired.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">get_channel_folders</a>() -> GetChannelFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches all of the [channel folders](/help/channel-folders) in the
organization, sorted by the `order` field.

**Changes**: Before Zulip 11.0 (feature level 414), the list of channel
folders was sorted by ID as the `order` field didn't exist.

New in Zulip 11.0 (feature level 389).
</dd>
</dl>
</dd>
</dl>

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

client.channels.get_channel_folders()

```
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

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">patch_channel_folders</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reorder the [channel folders](/help/channel-folders) in the user's
organization.

Channel folders are displayed in Zulip UI in order; this endpoint allows
administrative settings UI to change the ordering of channel folders.

This endpoint is used to implement the dragging feature described in the
[manage channel folders documentation](/help/manage-channel-folders).

**Changes**: New in Zulip 11.0 (feature level 414).
</dd>
</dl>
</dd>
</dl>

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

client.channels.patch_channel_folders(
    order=[
        2,
        1
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

**order:** `typing.List[int]` 

A list of channel folder IDs representing the new order.

This list must include the IDs of [all the organization's channel
folders](/api/get-channel-folders), including archived folders.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">update_channel_folder</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name or description of a [channel folder](/help/channel-folders)
with the specified ID.

This endpoint is also used to archive or unarchive the specified channel
folder.

**Changes**: New in Zulip 11.0 (feature level 389).
</dd>
</dl>
</dd>
</dl>

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

client.channels.update_channel_folder(
    channel_folder_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_folder_id:** `int` — The ID of the target channel folder.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

The new name of the channel folder.

Clients should use the `max_channel_folder_name_length` returned
by the [`POST /register`](/api/register-queue) endpoint to determine
the maximum channel folder name length.

Value cannot be an empty string.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

The new description of the channel folder.

Clients should use the `max_channel_folder_description_length`
returned by the [`POST /register`](/api/register-queue) endpoint
to determine the maximum channel folder description length.
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` — Whether to archive or unarchive the channel folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">create_big_blue_button_video_call</a>(...) -> CreateBigBlueButtonVideoCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a video call URL for a BigBlueButton video call.
Requires [BigBlueButton 2.4+](/integrations/big-blue-button)
to be configured on the Zulip server.

The acting user will be given the moderator role on the call.

**Changes**: Prior to Zulip 10.0 (feature level 337), every
user was given the moderator role on BigBlueButton calls, via
encoding a moderator password in the generated URLs.
</dd>
</dl>
</dd>
</dl>

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

client.channels.create_big_blue_button_video_call(
    meeting_name="test_channel meeting",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**meeting_name:** `str` — Meeting name for the BigBlueButton video call.
    
</dd>
</dl>

<dl>
<dd>

**voice_only:** `typing.Optional[bool]` 

Configures whether the call is voice-only; if true,
disables cameras for all users. Only the call
creator/moderator can edit this configuration.

**Changes**: New in Zulip 10.0 (feature level 337).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">create_nextcloud_talk_video_call</a>(...) -> CreateNextcloudTalkVideoCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a video call URL for a Nextcloud Talk video call. Requires
[Nextcloud Talk](/integrations/nextcloud-talk) to be configured on the
Zulip server.

**Changes**: New in Zulip 12.0 (feature level 465).
</dd>
</dl>
</dd>
</dl>

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

client.channels.create_nextcloud_talk_video_call(
    room_name="#Test > team check-in",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**room_name:** `str` — Room name for the Nextcloud Talk conversation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/fern/channels/client.py">create_constructor_groups_video_call</a>() -> CreateConstructorGroupsVideoCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a video call URL for a Constructor Groups video call.
Requires [Constructor Groups](/integrations/constructor-groups)
to be configured on the Zulip server.

**Changes**: New in Zulip 12.0 (feature level 460).
</dd>
</dl>
</dd>
</dl>

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

client.channels.create_constructor_groups_video_call()

```
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

## Messages
<details><summary><code>client.messages.<a href="src/fern/messages/client.py">mark_all_as_read</a>() -> MarkAllAsReadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks all of the current user's unread messages as read.

Because this endpoint marks messages as read in batches, it is possible
for the request to time out after only marking some messages as read.
When this happens, the `complete` boolean field in the success response
will be `false`. Clients should repeat the request when handling such a
response. If all messages were marked as read, then the success response
will return `"complete": true`.

**Changes**: Deprecated; clients should use the [update personal message
flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
as this endpoint will be removed in a future release.

Before Zulip 8.0 (feature level 211), if the server's
processing was interrupted by a timeout, but some messages were marked
as read, then it would return `"result": "partially_completed"`, along
with a `code` field for an error string, in the success response to
indicate that there was a timeout and that the client should repeat the
request.

Before Zulip 6.0 (feature level 153), this request did a single atomic
operation, which could time out with 10,000s of unread messages to mark
as read. As of this feature level, messages are marked as read in
batches, starting with the newest messages, so that progress is made
even if the request times out. And, instead of returning an error when
the request times out and some messages have been marked as read, a
success response with `"result": "partially_completed"` is returned.
</dd>
</dl>
</dd>
</dl>

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

client.messages.mark_all_as_read()

```
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">mark_stream_as_read</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark all the unread messages in a channel as read.

**Changes**: Deprecated; clients should use the [update personal message
flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
as this endpoint will be removed in a future release.
</dd>
</dl>
</dd>
</dl>

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

client.messages.mark_stream_as_read(
    stream_id=43,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">mark_topic_as_read</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark all the unread messages in a topic as read.

**Changes**: Deprecated; clients should use the [update personal message
flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
as this endpoint will be removed in a future release.
</dd>
</dl>
</dd>
</dl>

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

client.messages.mark_topic_as_read(
    stream_id=43,
    topic_name="new coffee machine",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stream_id:** `int` — The ID of the channel to access.
    
</dd>
</dl>

<dl>
<dd>

**topic_name:** `str` 

The name of the topic whose messages should be marked as read.

Note: When the value of `realm_empty_topic_display_name` found in
the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

**Changes**: Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">get_messages</a>(...) -> GetMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is the primary way to fetch a messages. It is used by all official
Zulip clients (e.g. the web, desktop, mobile, and terminal clients) as well as
many bots, API clients, backup scripts, etc.

Most queries will specify a [narrow filter](/api/get-messages#parameter-narrow),
to fetch the messages matching any supported [search
query](/help/search-for-messages). If not specified, it will return messages
corresponding to the user's [combined feed](/help/combined-feed). There are two
ways to specify which messages matching the narrow filter to fetch:

- A range of messages, described by an `anchor` message ID (or a string-format
  specification of how the server should computer an anchor to use) and a maximum
  number of messages in each direction from that anchor.

- A rarely used variant (`message_ids`) where the client specifies the message IDs
  to fetch.

The server returns the matching messages, sorted by message ID, as well as some
metadata that makes it easy for a client to determine whether there are more
messages matching the query that were not returned due to the `num_before` and
`num_after` limits.

Note that a user's message history does not contain messages sent to
channels before they [subscribe](/api/subscribe), and newly created
bot users are not usually subscribed to any channels.

We recommend requesting at most 1000 messages in a batch, to avoid generating very
large HTTP responses. A maximum of 5000 messages can be obtained per request;
attempting to exceed this will result in an error.

**Changes**: The `message_ids` option is new in Zulip 10.0 (feature level 300).
</dd>
</dl>
</dd>
</dl>

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

client.messages.get_messages(
    anchor_date="2005-04-18T12:34:56Z",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**anchor:** `typing.Optional[Anchor]` 

Integer message ID to anchor fetching of new messages. Supports special
string values for when the client wants the server to compute the anchor
to use:

- `newest`: The most recent message.
- `oldest`: The oldest message.
- `first_unread`: The oldest unread message matching the
  query, if any; otherwise, the most recent message.
- `date`: The first message on or after the datetime indicated by the
  [`anchor_date`](#parameter-anchor_date), if any; otherwise, the most
  recent message.

**Changes**: The `date` value is new in Zulip 12.0 (feature level 445).

String values are new in Zulip 3.0 (feature level 1). The
`first_unread` functionality was supported in Zulip 2.1.x
and older by not sending `anchor` and using `use_first_unread_anchor`.

In Zulip 2.1.x and older, `oldest` can be emulated with
`"anchor": 0`, and `newest` with `"anchor": 10000000000000000`
(that specific large value works around a bug in Zulip
2.1.x and older in the `found_newest` return value).
    
</dd>
</dl>

<dl>
<dd>

**include_anchor:** `typing.Optional[bool]` 

Whether a message with the specified ID matching the narrow
should be included.

**Changes**: New in Zulip 6.0 (feature level 155).
    
</dd>
</dl>

<dl>
<dd>

**anchor_date:** `typing.Optional[str]` 

The date or datetime to use for finding the anchor message when `anchor` is
`date`. Accepted formats include ISO 8601 date-only strings
(e.g. `2005-04-18`) as well as full datetime strings
(e.g. `2005-04-18T12:34:56Z`). If only a date is provided, the datetime is set to
midnight (00:00) on that day in UTC. If no timezone is provided, UTC is
assumed.

**Changes**: New in Zulip 12.0 (feature level 445).
    
</dd>
</dl>

<dl>
<dd>

**num_before:** `typing.Optional[int]` 

The number of messages with IDs less than the anchor to retrieve.
Required if `message_ids` is not provided.
    
</dd>
</dl>

<dl>
<dd>

**num_after:** `typing.Optional[int]` 

The number of messages with IDs greater than the anchor to retrieve.
Required if `message_ids` is not provided.
    
</dd>
</dl>

<dl>
<dd>

**narrow:** `typing.Optional[str]` 

The narrow where you want to fetch the messages from. See how to
[construct a narrow](/api/construct-narrow).

Note that many narrows, including all that lack a `channel`, `channels`,
`stream`, or `streams` operator, search the user's personal message
history. See [searching shared
history](/help/search-for-messages#search-shared-history)
for details.

For example, if you would like to fetch messages from all public channels instead
of only the user's message history, then a specific narrow for
messages sent to all public channels can be used:
`{"operator": "channels", "operand": "public"}`.

Newly created bot users are not usually subscribed to any
channels, so bots using this API should either be
subscribed to appropriate channels or use a shared history
search narrow with this endpoint.

**Changes**: See [changes section](/api/construct-narrow#changes)
of search/narrow filter documentation.
    
</dd>
</dl>

<dl>
<dd>

**client_gravatar:** `typing.Optional[bool]` 

Whether the client supports computing gravatars URLs. If
enabled, `avatar_url` will be included in the response only
if there is a Zulip avatar, and will be `null` for users who
are using gravatar as their avatar. This option
significantly reduces the compressed size of user data,
since gravatar URLs are long, random strings and thus do not
compress well. The `client_gravatar` field is set to `true` if
clients can compute their own gravatars.

**Changes**: The default value of this parameter was `false`
prior to Zulip 5.0 (feature level 92).
    
</dd>
</dl>

<dl>
<dd>

**apply_markdown:** `typing.Optional[bool]` 

If `true`, message content is returned in the rendered HTML
format. If `false`, message content is returned in the raw
Markdown-format text that user entered.

See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    
</dd>
</dl>

<dl>
<dd>

**use_first_unread_anchor:** `typing.Optional[bool]` 

Legacy way to specify `"anchor": "first_unread"` in Zulip 2.1.x and older.

Whether to use the (computed by the server) first unread message
matching the narrow as the `anchor`. Mutually exclusive with `anchor`.

**Changes**: Deprecated in Zulip 3.0 (feature level 1) and replaced by
`"anchor": "first_unread"`.
    
</dd>
</dl>

<dl>
<dd>

**message_ids:** `typing.Optional[str]` 

A list of message IDs to fetch. The server will return messages corresponding to the
subset of the requested message IDs that exist and the current user has access to,
potentially filtered by the narrow (if that parameter is provided).

It is an error to pass this parameter as well as any of the parameters involved in
specifying a range of messages: `anchor`, `include_anchor`, `use_first_unread_anchor`,
`num_before`, and `num_after`.

**Changes**: New in Zulip 10.0 (feature level 300). Previously, there was
no way to request a specific set of messages IDs.
    
</dd>
</dl>

<dl>
<dd>

**allow_empty_topic_name:** `typing.Optional[bool]` 

Whether the client supports processing the empty string as a topic in the
topic name fields in the returned data, including in returned edit_history data.

If `false`, the server will use the value of `realm_empty_topic_display_name`
found in the [`POST /register`](/api/register-queue) response instead of empty string
to represent the empty string topic in its response.

**Changes**: New in Zulip 10.0 (feature level 334). Previously, the empty string
was not a valid topic.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">send_message</a>(...) -> SendMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a [channel message](/help/introduction-to-topics) or a
[direct message](/help/direct-messages).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.messages import SendMessageRequestType

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.send_message(
    type=SendMessageRequestType.DIRECT,
    to="to",
    content="Hello",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `SendMessageRequestType` 

The type of message to be sent.

`"direct"` for a direct message and `"stream"` or `"channel"` for a
channel message.

**Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
an additional value for this parameter to request a channel message.

In Zulip 7.0 (feature level 174), `"direct"` was added as
the preferred way to request a direct message, deprecating the original
`"private"`. While `"private"` is still supported for requesting direct
messages, clients are encouraged to use to the modern convention with
servers that support it, because support for `"private"` will eventually
be removed.
    
</dd>
</dl>

<dl>
<dd>

**to:** `SendMessageRequestTo` 

For channel messages, either the name or integer ID of the channel. For
direct messages, either a list containing integer user IDs or a list
containing string Zulip API email addresses.

**Changes**: Support for using user/channel IDs was added in Zulip 2.0.0.
    
</dd>
</dl>

<dl>
<dd>

**content:** `RequiredContent` 
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` 

The topic of the message. Only required for channel messages
(`"type": "stream"` or `"type": "channel"`), ignored otherwise.

Clients should use the `max_topic_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum topic length.

Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
found in the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

When [topics are required](/help/require-topics), this parameter can't
be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

**Changes**: Before Zulip 10.0 (feature level 370), `"(no topic)"`
was not interpreted as an empty string.

Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.

New in Zulip 2.0.0. Previous Zulip releases encoded
this as `subject`, which is currently a deprecated alias.
    
</dd>
</dl>

<dl>
<dd>

**queue_id:** `typing.Optional[str]` 

For clients supporting
[local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo),
the [event queue](/api/register-queue) ID for the client.

If passed, `local_id` is required.

If the message is successfully sent, the server will include
`local_message_id` in the [`message` event](/api/get-events#message) that
the client with this `queue_id` will receive.
    
</dd>
</dl>

<dl>
<dd>

**local_id:** `typing.Optional[str]` 

For clients supporting
[local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo),
a unique string-format identifier chosen freely by the client.

If passed, `queue_id` is required.

If the message is successfully sent, the server will pass it back to
the client without inspecting it as `local_message_id` in the
[`message` event](/api/get-events#message) that the client with the
above `queue_id` will receive.
    
</dd>
</dl>

<dl>
<dd>

**read_by_sender:** `typing.Optional[bool]` 

Whether the message should be initially marked read by its
sender. If unspecified, the server uses a heuristic based
on the client name.

**Changes**: New in Zulip 8.0 (feature level 236).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">get_message_history</a>(...) -> GetMessageHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the message edit history of a previously edited message.

Note that edit history may be disabled in some organizations; see the
[Zulip help center documentation on editing messages][edit-settings].

[edit-settings]: /help/view-a-messages-edit-history
</dd>
</dl>
</dd>
</dl>

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

client.messages.get_message_history(
    message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**allow_empty_topic_name:** `typing.Optional[bool]` 

Whether the topic names i.e. `topic` and `prev_topic` fields in
the `message_history` objects returned can be empty string.

If `false`, the value of `realm_empty_topic_display_name`
found in the [`POST /register`](/api/register-queue) response is
returned replacing the empty string as the topic name.

**Changes**: New in Zulip 10.0 (feature level 334).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">update_message_flags</a>(...) -> UpdateMessageFlagsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or remove personal message flags like `read` and `starred`
on a collection of message IDs.

See also the endpoint for [updating flags on a range of
messages within a narrow](/api/update-message-flags-for-narrow).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.messages import UpdateMessageFlagsRequestOp

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.update_message_flags(
    messages=[
        4,
        8,
        15
    ],
    op=UpdateMessageFlagsRequestOp.ADD,
    flag="read",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**messages:** `typing.List[int]` — An array containing the IDs of the target messages.
    
</dd>
</dl>

<dl>
<dd>

**op:** `UpdateMessageFlagsRequestOp` — Whether to `add` the flag or `remove` it.
    
</dd>
</dl>

<dl>
<dd>

**flag:** `str` — The flag that should be added/removed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">update_message_flags_for_narrow</a>(...) -> UpdateMessageFlagsForNarrowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or remove personal message flags like `read` and `starred`
on a range of messages within a narrow.

See also [the endpoint for updating flags on specific message
IDs](/api/update-message-flags).

**Changes**: New in Zulip 6.0 (feature level 155).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.messages import UpdateMessageFlagsForNarrowRequestNarrowItemNegated, UpdateMessageFlagsForNarrowRequestOp

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.update_message_flags_for_narrow(
    anchor="43",
    num_before=4,
    num_after=8,
    narrow=[
        UpdateMessageFlagsForNarrowRequestNarrowItemNegated(
            operator="channel",
            operand="Denmark",
        )
    ],
    op=UpdateMessageFlagsForNarrowRequestOp.ADD,
    flag="read",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**anchor:** `str` 

Integer message ID to anchor updating of flags. Supports special
string values for when the client wants the server to compute the anchor
to use:

- `newest`: The most recent message.
- `oldest`: The oldest message.
- `first_unread`: The oldest unread message matching the
  query, if any; otherwise, the most recent message.
    
</dd>
</dl>

<dl>
<dd>

**num_before:** `int` 

Limit the number of messages preceding the anchor in the
update range. The server may decrease this to bound
transaction sizes.
    
</dd>
</dl>

<dl>
<dd>

**num_after:** `int` 

Limit the number of messages following the anchor in the
update range. The server may decrease this to bound
transaction sizes.
    
</dd>
</dl>

<dl>
<dd>

**narrow:** `typing.List[UpdateMessageFlagsForNarrowRequestNarrowItem]` 

The narrow you want update flags within. See how to
[construct a narrow](/api/construct-narrow).

Note that, when adding the `read` flag to messages, clients should
consider including a narrow with the `is:unread` filter as an
optimization. Including that filter takes advantage of the fact that
the server has a database index for unread messages.

**Changes**: See [changes section](/api/construct-narrow#changes)
of search/narrow filter documentation.
    
</dd>
</dl>

<dl>
<dd>

**op:** `UpdateMessageFlagsForNarrowRequestOp` — Whether to `add` the flag or `remove` it.
    
</dd>
</dl>

<dl>
<dd>

**flag:** `str` 

The flag that should be added/removed. See [available
flags](/api/update-message-flags#available-flags).
    
</dd>
</dl>

<dl>
<dd>

**include_anchor:** `typing.Optional[bool]` 

Whether a message with the specified ID matching the narrow
should be included in the update range.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">render_message</a>(...) -> RenderMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Render a message to HTML.
</dd>
</dl>
</dd>
</dl>

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

client.messages.render_message(
    content="Hello",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content:** `RequiredContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">add_reaction</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add an [emoji reaction](/help/emoji-reactions) to a message.
</dd>
</dl>
</dd>
</dl>

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

client.messages.add_reaction(
    message_id=1,
    emoji_name="octopus",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**emoji_name:** `str` 

The target emoji's human-readable name.

To find an emoji's name, hover over a message to reveal
three icons on the right, then click the smiley face icon.
Images of available reaction emojis appear. Hover over the
emoji you want, and note that emoji's text name.
    
</dd>
</dl>

<dl>
<dd>

**emoji_code:** `typing.Optional[EmojiCode]` 
    
</dd>
</dl>

<dl>
<dd>

**reaction_type:** `typing.Optional[ReactionType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">remove_reaction</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an [emoji reaction](/help/emoji-reactions) from a message.
</dd>
</dl>
</dd>
</dl>

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

client.messages.remove_reaction(
    message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**emoji_name:** `typing.Optional[str]` 

The target emoji's human-readable name.

To find an emoji's name, hover over a message to reveal
three icons on the right, then click the smiley face icon.
Images of available reaction emojis appear. Hover over the
emoji you want, and note that emoji's text name.
    
</dd>
</dl>

<dl>
<dd>

**emoji_code:** `typing.Optional[EmojiCode]` 
    
</dd>
</dl>

<dl>
<dd>

**reaction_type:** `typing.Optional[ReactionType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">get_read_receipts</a>(...) -> GetReadReceiptsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list containing the IDs for all users who have
marked the message as read (and whose privacy settings allow
sharing that information).

The list of users IDs will include any bots who have marked
the message as read via the API (providing a way for bots to
indicate whether they have processed a message successfully in
a way that can be easily inspected in a Zulip client). Bots
for which this behavior is not desired may disable the
`send_read_receipts` setting via the API.

It will never contain the message's sender.

**Changes**: New in Zulip 6.0 (feature level 137).
</dd>
</dl>
</dd>
</dl>

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

client.messages.get_read_receipts(
    message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">check_messages_match_narrow</a>(...) -> CheckMessagesMatchNarrowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check whether a set of messages match a [narrow](/api/construct-narrow).

For many common narrows (e.g. a topic), clients can write an efficient
client-side check to determine whether a newly arrived message belongs
in the view.

This endpoint is designed to allow clients to handle more complex narrows
for which the client does not (or in the case of full-text search, cannot)
implement this check.

The format of the `match_subject` and `match_content` objects is designed
to match those returned by the [`GET /messages`](/api/get-messages#response)
endpoint, so that a client can splice these fields into a `message` object
received from [`GET /events`](/api/get-events#message) and end up with an
extended message object identical to how a [`GET /messages`](/api/get-messages)
request for the current narrow would have returned the message.
</dd>
</dl>
</dd>
</dl>

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

client.messages.check_messages_match_narrow(
    msg_ids="msg_ids",
    narrow="narrow",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**msg_ids:** `str` — List of IDs for the messages to check.
    
</dd>
</dl>

<dl>
<dd>

**narrow:** `str` 

A structure defining the narrow to check against. See how to
[construct a narrow](/api/construct-narrow).

**Changes**: See [changes section](/api/construct-narrow#changes)
of search/narrow filter documentation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">get_message</a>(...) -> GetMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given a message ID, return the message object.

Additionally, a `raw_content` field is included. This field is
useful for clients that primarily work with HTML-rendered
messages but might need to occasionally fetch the message's
raw [Zulip-flavored Markdown](/help/format-your-message-using-markdown) (e.g. for [view
source](/help/view-the-markdown-source-of-a-message) or
prefilling a message edit textarea).

**Changes**: Before Zulip 5.0 (feature level 120), this
endpoint only returned the `raw_content` field.
</dd>
</dl>
</dd>
</dl>

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

client.messages.get_message(
    message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**apply_markdown:** `typing.Optional[bool]` 

If `true`, message content is returned in the rendered HTML
format. If `false`, message content is returned in the raw
[Zulip-flavored Markdown format](/help/format-your-message-using-markdown) text that user entered.

**Changes**: New in Zulip 5.0 (feature level 120).
    
</dd>
</dl>

<dl>
<dd>

**allow_empty_topic_name:** `typing.Optional[bool]` 

Whether the client supports processing the empty string as a topic in the
topic name fields in the returned data, including in returned edit_history data.

If `false`, the server will use the value of `realm_empty_topic_display_name`
found in the [`POST /register`](/api/register-queue) response instead of empty string
to represent the empty string topic in its response.

**Changes**: New in Zulip 10.0 (feature level 334). Previously, the empty string
was not a valid topic.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">delete_message</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a message.

This API corresponds to the [delete a message completely][delete-completely]
feature documented in the Zulip help center.

A user must be able to access the content of a message in order to delete it.
See [channel permissions](/help/channel-permissions) for more information
about content access for channel messages. For direct messages, the user
must have received or sent the direct message to have content access.

See [restricting message deletion](/help/restrict-message-editing-and-deletion)
for documentation on when users are allowed to delete messages.

The relevant realm settings in the API that are related to the above linked
documentation on when users are allowed to delete messages are:

- `realm_can_delete_any_message_group`
- `realm_can_delete_own_message_group`
- `realm_can_set_delete_message_policy_group`
- `realm_message_content_delete_limit_seconds`

The relevant per-channel permission settings in the API that are related to the
above linked documentation on when users are allowed to delete messages in a
specific channel are:

- `can_delete_any_message_group`
- `can_delete_own_message_group`

More details about these realm and channel settings can be found in the
[`POST /register`](/api/register-queue) response.

**Changes**: Prior to Zulip 10.0 (feature level 281), only organization
administrators had permission to permanently delete a message.

[delete-completely]: /help/delete-a-message#delete-a-message-completely
</dd>
</dl>
</dd>
</dl>

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

client.messages.delete_message(
    message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">update_message</a>(...) -> UpdateMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the content, topic, or channel of the message with the specified
ID.

You can [resolve topics](/help/resolve-a-topic) by editing the topic to
`✔ {original_topic}` with the `propagate_mode` parameter set to
`"change_all"`.

See [configuring message editing][config-message-editing] for detailed
documentation on when users are allowed to edit message content, and
[restricting moving messages][restrict-move-messages] for detailed
documentation on when users are allowed to change a message's topic
and/or channel.

The relevant realm settings in the API that are related to the above
linked documentation on when users are allowed to update messages are:

- `allow_message_editing`
- `can_resolve_topics_group`
- `can_move_messages_between_channels_group`
- `can_move_messages_between_topics_group`
- `message_content_edit_limit_seconds`
- `move_messages_within_stream_limit_seconds`
- `move_messages_between_streams_limit_seconds`

More details about these realm settings can be found in the
[`POST /register`](/api/register-queue) response or in the documentation
of the [`realm op: update_dict`](/api/get-events#realm-update_dict)
event in [`GET /events`](/api/get-events).

**Changes**: Prior to Zulip 10.0 (feature level 367), the permission for
resolving a topic was managed by `can_move_messages_between_topics_group`.
As of this feature level, users belonging to the `can_resolve_topics_group`
will have the permission to [resolve topics](/help/resolve-a-topic) in the organization.

In Zulip 10.0 (feature level 316), `edit_topic_policy`
was removed and replaced by `can_move_messages_between_topics_group`
realm setting.

**Changes**: In Zulip 10.0 (feature level 310), `move_messages_between_streams_policy`
was removed and replaced by `can_move_messages_between_channels_group`
realm setting.

Prior to Zulip 7.0 (feature level 172), anyone could add a
topic to channel messages without a topic, regardless of the organization's
[topic editing permissions](/help/restrict-moving-messages). As of this
feature level, messages without topics have the same restrictions for
topic edits as messages with topics.

Before Zulip 7.0 (feature level 172), by using the `change_all` value for
the `propagate_mode` parameter, users could move messages after the
organization's configured time limits for changing a message's topic or
channel had passed. As of this feature level, the server will [return an
error](/api/update-message#response) with `"code":
"MOVE_MESSAGES_TIME_LIMIT_EXCEEDED"` if users, other than organization
administrators or moderators, try to move messages after these time
limits have passed.

Before Zulip 7.0 (feature level 162), users who were not administrators or
moderators could only edit topics if the target message was sent within the
last 3 days. As of this feature level, that time limit is now controlled by
the realm setting `move_messages_within_stream_limit_seconds`. Also at this
feature level, a similar time limit for moving messages between channels was
added, controlled by the realm setting
`move_messages_between_streams_limit_seconds`. Previously, all users who
had permission to move messages between channels did not have any time limit
restrictions when doing so.

Before Zulip 7.0 (feature level 159), editing channels and topics of messages
was forbidden if the realm setting for `allow_message_editing` was `false`,
regardless of an organization's configuration for the realm settings
`edit_topic_policy` or `move_messages_between_streams_policy`.

Before Zulip 7.0 (feature level 159), message senders were allowed to edit
the topic of their messages indefinitely.

In Zulip 5.0 (feature level 75), the `edit_topic_policy` realm setting
was added, replacing the `allow_community_topic_editing` boolean.

In Zulip 4.0 (feature level 56), the `move_messages_between_streams_policy`
realm setting was added.

[config-message-editing]: /help/restrict-message-editing-and-deletion
[restrict-move-messages]: /help/restrict-moving-messages
</dd>
</dl>
</dd>
</dl>

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

client.messages.update_message(
    message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` 

The topic to move the message(s) to, to request changing the topic.

Clients should use the `max_topic_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum topic length

Should only be sent when changing the topic, and will throw an error
if the target message is not a channel message.

Note: When the value of `realm_empty_topic_display_name` found in
the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

When [topics are required](/help/require-topics), this parameter can't
be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

You can [resolve topics](/help/resolve-a-topic) by editing the topic to
`✔ {original_topic}` with the `propagate_mode` parameter set to
`"change_all"`. The empty string topic cannot be marked as resolved.

**Changes**: Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.

New in Zulip 2.0.0. Previous Zulip releases encoded this as `subject`,
which is currently a deprecated alias.
    
</dd>
</dl>

<dl>
<dd>

**propagate_mode:** `typing.Optional[UpdateMessageRequestPropagateMode]` 

Which message(s) should be edited:

- `"change_later"`: The target message and all following messages.
- `"change_one"`: Only the target message.
- `"change_all"`: All messages in this topic.

Only the default value of `"change_one"` is valid when editing
only the content of a message.

This parameter determines both which messages get moved and also whether
clients that are currently narrowed to the topic containing the message
should navigate or adjust their compose box recipient to point to the
post-edit channel/topic.
    
</dd>
</dl>

<dl>
<dd>

**send_notification_to_old_thread:** `typing.Optional[bool]` 

Whether to send an automated message to the old topic to
notify users where the messages were moved to.

**Changes**: Before Zulip 6.0 (feature level 152), this parameter
had a default of `true` and was ignored unless the channel was changed.

New in Zulip 3.0 (feature level 9).
    
</dd>
</dl>

<dl>
<dd>

**send_notification_to_new_thread:** `typing.Optional[bool]` 

Whether to send an automated message to the new topic to
notify users where the messages came from.

If the move is just [resolving/unresolving a topic](/help/resolve-a-topic),
this parameter will not trigger an additional notification.

**Changes**: Before Zulip 6.0 (feature level 152), this parameter
was ignored unless the channel was changed.

New in Zulip 3.0 (feature level 9).
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[OptionalContent]` 
    
</dd>
</dl>

<dl>
<dd>

**prev_content_sha256:** `typing.Optional[str]` 

An optional SHA-256 hash of the previous raw content of the message
that the client has at the time of the request.

If provided, the server will return an error if it does not match the
SHA-256 hash of the message's content stored in the database.

Clients can use this feature to prevent races where multiple clients
save conflicting edits to a message.

**Changes**: New in Zulip 11.0 (feature level 379).
    
</dd>
</dl>

<dl>
<dd>

**stream_id:** `typing.Optional[int]` 

The channel ID to move the message(s) to, to request moving
messages to another channel.

Should only be sent when changing the channel, and will throw an error
if the target message is not a channel message.

Note that a message's content and channel cannot be changed at the
same time, so sending both `content` and `stream_id` parameters will
throw an error.

**Changes**: New in Zulip 3.0 (feature level 1).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">report_message</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends a notification to the organization's [moderation request
channel](/help/enable-moderation-requests), if it is configured, that
reports the targeted message for [review and moderation](/help/report-a-message).

Clients should check the `moderation_request_channel` realm setting to
decide whether to show the option to report messages in the UI.

If the `report_type` parameter value is `"other"`, the `description`
parameter is required. Clients should also enforce and communicate this
behavior in the UI.

**Changes**: New in Zulip 11.0 (feature level 382). This API builds on
the `moderation_request_channel` realm setting, which was added in
feature level 331.
</dd>
</dl>
</dd>
</dl>

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

client.messages.report_message(
    message_id=1,
    report_type="harassment",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**report_type:** `str` 

The reason that best describes why the current user is reporting the
target message for moderation.

Must be one of the `key` values in the `server_report_message_types`
field in the [`POST /register`](/api/register-queue) response.

**Changes**: Prior to Zulip 12.0 (feature level 435), the allowed
values for this parameter were limited to: `"harassment"`,
`"inappropriate"`, `"norms"`, `"other"`, `"spam"`.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

A short description with additional context about why the current user
is reporting the target message for moderation.

Clients should limit this string to 1000 Unicode code points.

If the `report_type` parameter is `"other"`, this parameter is required,
and its value cannot be an empty string.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">upload_file</a>(...) -> UploadFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Upload](/help/share-and-upload-files) a single file and get the corresponding URL.

Initially, only you will be able to access the link. To share the
uploaded file, you'll need to [send a message][send-message]
containing the resulting link. Users who can already access the link
can reshare it with other users by sending additional Zulip messages
containing the link.

The maximum allowed file size is available in the `max_file_upload_size_mib`
field in the [`POST /register`](/api/register-queue) response. Note that
large files (25MB+) may fail to upload using this API endpoint due to
network-layer timeouts, depending on the quality of your connection to the
Zulip server.

For uploading larger files, `/api/v1/tus` is an endpoint implementing the
[`tus` resumable upload protocol](https://tus.io/protocols/resumable-upload),
which supports uploading arbitrarily large files limited only by the server's
`max_file_upload_size_mib` (Configured via `MAX_FILE_UPLOAD_SIZE` in
`/etc/zulip/settings.py`). Clients which send authenticated credentials
(either via browser-based cookies, or API key via `Authorization` header) may
use this endpoint to upload files.

**Changes**: The `api/v1/tus` endpoint supporting resumable uploads was
introduced in Zulip 10.0 (feature level 296). Previously,
`max_file_upload_size_mib` was typically 25MB.

[uploaded-files]: /help/manage-your-uploaded-files
[send-message]: /api/send-message
</dd>
</dl>
</dd>
</dl>

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

client.messages.upload_file(
    filename="example_filename",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filename:** `typing.Optional[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">check_thumbnail_status</a>(...) -> CheckThumbnailStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check whether a thumbnail exists for a specific file uploaded by a user.
This endpoint is intended to be polled by clients to determine when
thumbnail generation is complete.

**Changes**: New in Zulip 12.0 (feature level 479).
</dd>
</dl>
</dd>
</dl>

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

client.messages.check_thumbnail_status(
    realm_id_str=1,
    filename="4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**realm_id_str:** `int` 

The realm ID component of the file's `path_id`. If the `path_id` is
`1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `realm_id_str` would be `1`.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 

The file path component of the file's `path_id` (everything
after the first `/`). If the `path_id` is
`1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `filename`
would be `4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">get_file_temporary_url</a>(...) -> GetFileTemporaryUrlResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a temporary URL for access to an [uploaded file](/api/upload-file)
that doesn't require authentication.

The `SIGNED_ACCESS_TOKEN_VALIDITY_IN_SECONDS` server setting controls
the valid length of time for temporary access, which generally is set
to a default of 60 seconds. Consumers of this API are expected to
immediately request the URL that it returns, and should not store it
in any way.

**Changes**: New in Zulip 3.0 (feature level 1).
</dd>
</dl>
</dd>
</dl>

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

client.messages.get_file_temporary_url(
    realm_id_str=1,
    filename="4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**realm_id_str:** `int` 

The realm ID component of the file's `path_id`. If the `path_id` is
`1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `realm_id_str` would be `1`.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 

The file path component of the file's `path_id` (everything
after the first `/`). If the `path_id` is
`1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `filename`
would be `4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_attachments</a>() -> GetAttachmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch metadata on files uploaded by the requesting user.
</dd>
</dl>
</dd>
</dl>

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

client.users.get_attachments()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">remove_attachment</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an uploaded file given its attachment ID.

Note that uploaded files that have been referenced in at least
one message are automatically deleted once the last message
containing a link to them is deleted (whether directly or via
a [message retention policy](/help/message-retention-policy)).

Uploaded files that are never used in a message are
automatically deleted a few weeks after being uploaded.

Attachment IDs can be contained from [GET /attachments](/api/get-attachments).
</dd>
</dl>
</dd>
</dl>

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

client.users.remove_attachment(
    attachment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attachment_id:** `int` — The ID of the attachment to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_users</a>(...) -> GetUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details on users in the organization.

By default, returns all accessible users in the organization.
The `user_ids` query parameter can be used to limit the
results to a specific set of user IDs.

Optionally includes values of [custom profile fields](/help/custom-profile-fields).

You can also [fetch details on a single user](/api/get-user).

**Changes**: In Zulip 12.0 (feature level 437), fixed a bug
dating to feature level 232, which caused guest users to
receive fake backwards-compatibility users in the format
intended for clients using `POST /register` without the
`user_list_incomplete` client capability.

This endpoint did not support unauthenticated
access in organizations using the [public access
option](/help/public-access-option) prior to Zulip 11.0
(feature level 387).
</dd>
</dl>
</dd>
</dl>

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

client.users.get_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_gravatar:** `typing.Optional[bool]` 

Whether the client supports computing gravatars URLs. If
enabled, `avatar_url` will be included in the response only
if there is a Zulip avatar, and will be `null` for users who
are using gravatar as their avatar. This option
significantly reduces the compressed size of user data,
since gravatar URLs are long, random strings and thus do not
compress well. The `client_gravatar` field is set to `true` if
clients can compute their own gravatars.

**Changes**: The default value of this parameter was `false`
prior to Zulip 5.0 (feature level 92).
    
</dd>
</dl>

<dl>
<dd>

**include_custom_profile_fields:** `typing.Optional[bool]` 

Whether the client wants [custom profile field](/help/custom-profile-fields)
data to be included in the response.

**Changes**: New in Zulip 2.1.0. Previous versions do not offer these
data via the API.
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[str]` 

Limits the results to the specified user IDs. If not
provided, the server will return all accessible users in
the organization.

**Changes**: New in Zulip 11.0 (feature level 384).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">create_user</a>(...) -> CreateUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user account via the API.

!!! warn ""

    **Note**: On Zulip Cloud, this feature is available only for
    organizations on a [Zulip Cloud Standard](https://zulip.com/plans/)
    or [Zulip Cloud Plus](https://zulip.com/plans/) plan. Administrators
    can request the required `can_create_users` permission for a bot or
    user by contacting [Zulip Cloud support][support] with an
    explanation for why it is needed. Self-hosted installations can
    toggle `can_create_users` on an account using the `manage.py
    change_user_role` [management command][management-commands].

**Changes**: Before Zulip 4.0 (feature level 36), this endpoint was
available to all organization administrators.

[support]: /help/contact-support
[management-commands]: https://zulip.readthedocs.io/en/latest/production/management-commands.html
</dd>
</dl>
</dd>
</dl>

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

client.users.create_user(
    email="username@example.com",
    password="abcd1234",
    full_name="New User",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — The email address of the new user.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — The password of the new user.
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `str` — The full name of the new user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">reactivate_user</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Reactivates a
user](https://zulip.com/help/deactivate-or-reactivate-a-user)
given their user ID.
</dd>
</dl>
</dd>
</dl>

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

client.users.reactivate_user(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_status</a>(...) -> GetUserStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the [status](/help/status-and-availability) currently set by a
user in the organization.

**Changes**: New in Zulip 9.0 (feature level 262). Previously,
user statuses could only be fetched via the [`POST
/register`](/api/register-queue) endpoint.
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user_status(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_status_for_user</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Administrator endpoint for changing the [status](/help/status-and-availability) of
another user.

**Changes**: Prior to Zulip 12.0 (feature level 473), only
bots could not access this API endpoint, regardless of the
role of the bot.

New in Zulip 11.0 (feature level 407).
</dd>
</dl>
</dd>
</dl>

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

client.users.update_status_for_user(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**status_text:** `typing.Optional[str]` 

The text content of the status message. Sending the empty string
will clear the user's status.

**Note**: The limit on the size of the message is 60 Unicode code points.
    
</dd>
</dl>

<dl>
<dd>

**emoji_name:** `typing.Optional[str]` 

The name for the emoji to associate with this status.

**Changes**: New in Zulip 5.0 (feature level 86).
    
</dd>
</dl>

<dl>
<dd>

**emoji_code:** `typing.Optional[str]` 

A unique identifier, defining the specific emoji codepoint requested,
within the namespace of the `reaction_type`.

**Changes**: New in Zulip 5.0 (feature level 86).
    
</dd>
</dl>

<dl>
<dd>

**reaction_type:** `typing.Optional[str]` 

A string indicating the type of emoji. Each emoji `reaction_type`
has an independent namespace for values of `emoji_code`.

Must be one of the following values:

- `unicode_emoji` : In this namespace, `emoji_code` will be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.

- `realm_emoji` : In this namespace, `emoji_code` will be the ID of
  the uploaded [custom emoji](/help/custom-emoji).

- `zulip_extra_emoji` : These are special emoji included with Zulip.
  In this namespace, `emoji_code` will be the name of the emoji (e.g.
  "zulip").

**Changes**: New in Zulip 5.0 (feature level 86).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_presence</a>(...) -> GetUserPresenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the presence status for a specific user.

This endpoint is most useful for embedding data about a user's
presence status in other sites (e.g. an employee directory). Full
Zulip clients like mobile/desktop apps will want to use the [main
presence endpoint](/api/get-presence), which returns data for all
active users in the organization, instead.
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user_presence(
    user_id_or_email="iago@zulip.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id_or_email:** `str` 

The ID or Zulip API email address of the user whose presence you want to fetch.

**Changes**: New in Zulip 4.0 (feature level 43). Previous versions only supported
identifying the user by Zulip API email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_own_user</a>() -> GetOwnUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get basic data about the user/bot that requests this endpoint.

**Changes**: Removed `is_billing_admin` field in Zulip 10.0 (feature level 363), as it was
replaced by the `can_manage_billing_group` realm setting.
</dd>
</dl>
</dd>
</dl>

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

client.users.get_own_user()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">deactivate_own_user</a>() -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivates the current user's account. See also the administrative endpoint for
[deactivating another user](/api/deactivate-user).

This endpoint is primarily useful to Zulip clients providing a user settings UI.
</dd>
</dl>
</dd>
</dl>

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

client.users.deactivate_own_user()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">regenerate_api_key</a>() -> RegenerateApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

!!! warn ""

     **Note**: Users should treat their Zulip API key as
     [carefully as they would their password](/help/protect-your-account).

Generate a new API key for the user making the request.

Changing a user's API key will immediately log them out of Zulip
on devices registered for [mobile push notifications][mobile-push].

[mobile-push]: https://zulip.readthedocs.io/en/latest/production/mobile-push-notifications.html
</dd>
</dl>
</dd>
</dl>

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

client.users.regenerate_api_key()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_alert_words</a>() -> GetAlertWordsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all of the user's configured [alert words][alert-words].

[alert-words]: /help/dm-mention-alert-notifications#alert-words
</dd>
</dl>
</dd>
</dl>

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

client.users.get_alert_words()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">add_alert_words</a>(...) -> AddAlertWordsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add words (or phrases) to the user's set of configured [alert words][alert-words].

[alert-words]: /help/dm-mention-alert-notifications#alert-words
</dd>
</dl>
</dd>
</dl>

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

client.users.add_alert_words(
    alert_words=[
        "foo",
        "bar"
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

**alert_words:** `typing.List[str]` 

An array of strings to be added to the user's set of configured
alert words. Strings already present in the user's set of alert words
already are ignored.

Alert words are case insensitive.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">remove_alert_words</a>(...) -> RemoveAlertWordsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove words (or phrases) from the user's set of configured [alert words][alert-words].

Alert words are case insensitive.

[alert-words]: /help/dm-mention-alert-notifications#alert-words
</dd>
</dl>
</dd>
</dl>

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

client.users.remove_alert_words(
    alert_words=[
        "foo"
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

**alert_words:** `typing.List[str]` 

An array of strings to be removed from the user's set of configured
alert words. Strings that are not in the user's set of alert words
are ignored.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_presence</a>(...) -> UpdatePresenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the current user's [presence][availability] and fetch presence data
of other users in the organization.

This endpoint is meant to be used by clients for both:

- Reporting the current user's presence status (`"active"` or `"idle"`)
  to the server.

- Obtaining the presence data of all other users in the organization via
  regular polling.

Accurate user presence is one of the most expensive parts of any
chat application (in terms of bandwidth and other resources). Therefore,
it is important that clients implementing Zulip's user presence system
use the modern [`last_update_id`](#parameter-last_update_id) protocol to
minimize fetching duplicate user presence data.

Client apps implementing presence are recommended to also consume [`presence`
events](/api/get-events#presence)), in order to learn about newly online users
immediately.

The Zulip server is responsible for implementing [invisible mode][invisible],
which disables sharing a user's presence data. Nonetheless, clients
should check the `presence_enabled` field in user objects in order to
display the current user as online or offline based on whether they are
sharing their presence information.

**Changes**: As of Zulip 8.0 (feature level 228), if the
`CAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCE` server-level setting is
`true`, then user presence data in the response is [limited to users
the current user can see/access][limit-visibility].

[limit-visibility]: /help/guest-users#configure-whether-guests-can-see-all-other-users
[invisible]: /help/status-and-availability#invisible-mode
[availability]: /help/status-and-availability#availability
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.users import UpdatePresenceRequestStatus

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.update_presence(
    status=UpdatePresenceRequestStatus.IDLE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status:** `UpdatePresenceRequestStatus` 

The status of the user on this client.

Clients should report the user as `"active"` on this device if the client
knows that the user is presently using the device (and thus would
potentially see a notification immediately), even if the user
has not directly interacted with the Zulip client.

Otherwise, it should report the user as `"idle"`.

See the related [`new_user_input`](#parameter-new_user_input) parameter
for how a client should report whether the user is actively using the
Zulip client.
    
</dd>
</dl>

<dl>
<dd>

**last_update_id:** `typing.Optional[int]` 

The identifier that specifies what presence data the client already
has received, which allows the server to only return more recent
user presence data.

This should be set to `-1` during initialization of the client in
order to fetch all user presence data, unless the client is obtaining
initial user presence metadata from the
[`POST /register`](/api/register-queue) endpoint.

In subsequent queries to this endpoint, this value should be set to the
most recent value of `presence_last_update_id` returned by the server
in this endpoint's response, which implements incremental fetching
of user presence data.

When this parameter is passed, the user presence data in the response
will always be in the modern format.

**Changes**: New in Zulip 9.0 (feature level 263). Previously, the
server sent user presence data for all users who had been active in the
last two weeks unconditionally.
    
</dd>
</dl>

<dl>
<dd>

**history_limit_days:** `typing.Optional[int]` 

Limits how far back in time to fetch user presence data. If not specified,
defaults to 14 days. A value of N means that the oldest presence data
fetched will be from at most N days ago.

Note that this is only useful during the initial user presence data fetch,
as subsequent fetches should use the `last_update_id` parameter, which
will act as the limit on how much presence data is returned. `history_limit_days`
is ignored if `last_update_id` is passed with a value greater than `0`,
indicating that the client already has some presence data.

**Changes**: New in Zulip 10.0 (feature level 288).
    
</dd>
</dl>

<dl>
<dd>

**new_user_input:** `typing.Optional[bool]` 

Whether the user has interacted with the client (e.g. moved the mouse,
used the keyboard, etc.) since the previous presence request from this
client.

The server uses data from this parameter to implement certain [usage
statistics](/help/analytics).

User interface clients that might run in the background, without the
user ever interacting with them, should be careful to only pass `true`
if the user has actually interacted with the client in order to avoid
corrupting usage statistics graphs.
    
</dd>
</dl>

<dl>
<dd>

**ping_only:** `typing.Optional[bool]` 

Whether the client is sending a ping-only request, meaning it only
wants to update the user's presence `status` on the server.

Otherwise, also requests the server return user presence data for all
users in the organization, which is further specified by the
[`last_update_id`](#parameter-last_update_id) parameter.
    
</dd>
</dl>

<dl>
<dd>

**slim_presence:** `typing.Optional[bool]` 

Legacy parameter for configuring the format (modern or legacy) in
which the server will return user presence data for the organization.

Modern clients should use
[`last_update_id`](#parameter-last_update_id), which guarantees that
user presence data will be returned in the modern format, and
should not pass this parameter as `true` unless interacting with an
older server.

Legacy clients that do not yet support `last_update_id` may use the
value of `true` to request the modern format for user presence data.

**Note**: The legacy format for user presence data will be removed
entirely in a future release.

**Changes**: **Deprecated** in Zulip 9.0 (feature level 263). Using
the modern `last_update_id` parameter is the recommended way to
request the modern format for user presence data.

New in Zulip 3.0 (no feature level as it was an unstable API at that
point).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_status</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change your [status](/help/status-and-availability).

A request to this endpoint will only change the parameters passed.
For example, passing just `status_text` requests a change in the status
text, but will leave the status emoji unchanged.

Clients that wish to set the user's status to a specific value should
pass all supported parameters.

**Changes**: In Zulip 5.0 (feature level 86), added support for
`emoji_name`, `emoji_code`, and `reaction_type` parameters.
</dd>
</dl>
</dd>
</dl>

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

client.users.update_status()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status_text:** `typing.Optional[str]` 

The text content of the status message. Sending the empty string
will clear the user's status.

**Note**: The limit on the size of the message is 60 Unicode code points.
    
</dd>
</dl>

<dl>
<dd>

**away:** `typing.Optional[bool]` 

Whether the user should be marked as "away".

**Changes**: Deprecated in Zulip 6.0 (feature level 148);
starting with that feature level, `away` is a legacy way to
access the user's `presence_enabled` setting, with
`away = !presence_enabled`. To be removed in a future release.
    
</dd>
</dl>

<dl>
<dd>

**emoji_name:** `typing.Optional[str]` 

The name for the emoji to associate with this status.

**Changes**: New in Zulip 5.0 (feature level 86).
    
</dd>
</dl>

<dl>
<dd>

**emoji_code:** `typing.Optional[str]` 

A unique identifier, defining the specific emoji codepoint requested,
within the namespace of the `reaction_type`.

**Changes**: New in Zulip 5.0 (feature level 86).
    
</dd>
</dl>

<dl>
<dd>

**reaction_type:** `typing.Optional[str]` 

A string indicating the type of emoji. Each emoji `reaction_type`
has an independent namespace for values of `emoji_code`.

Must be one of the following values:

- `unicode_emoji` : In this namespace, `emoji_code` will be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.

- `realm_emoji` : In this namespace, `emoji_code` will be the ID of
  the uploaded [custom emoji](/help/custom-emoji).

- `zulip_extra_emoji` : These are special emoji included with Zulip.
  In this namespace, `emoji_code` will be the name of the emoji (e.g.
  "zulip").

**Changes**: New in Zulip 5.0 (feature level 86).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">mute_user</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Mute a user](/help/mute-a-user) from the perspective of the requesting
user. Messages sent by muted users will be automatically marked as read
and hidden for the user who muted them.

Muted users should be implemented by clients as follows:

- The server will immediately mark all messages sent by the muted
  user as read. This will automatically clear any existing mobile
  push notifications related to the muted user.
- The server will mark any new messages sent by the muted user as read
  for the requesting user's account, which prevents all email and mobile
  push notifications.
- Clients should exclude muted users from presence lists or other UI
  for viewing or composing one-on-one direct messages. One-on-one direct
  messages sent by muted users should be hidden everywhere in the Zulip UI.
- Channel messages and group direct messages sent by the muted
  user should avoid displaying the content and name/avatar,
  but should display that N messages by a muted user were
  hidden (so that it is possible to interpret the messages by
  other users who are talking with the muted user).
- Group direct message conversations including the muted user
  should display muted users as "Muted user", rather than
  showing their name, in lists of such conversations, along with using
  a blank grey avatar where avatars are displayed.
- Administrative/settings UI elements for showing "All users that exist
  on this channel or realm", e.g. for organization
  administration or showing channel subscribers, should display
  the user's name as normal.

**Changes**: New in Zulip 4.0 (feature level 48).
</dd>
</dl>
</dd>
</dl>

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

client.users.mute_user(
    muted_user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**muted_user_id:** `int` 

The ID of the user to mute/unmute.

**Changes**: Before Zulip 8.0 (feature level 188), bot users could not
be muted/unmuted, and specifying a bot user's ID returned an error response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">unmute_user</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Unmute a user](/help/mute-a-user#see-your-list-of-muted-users)
from the perspective of the requesting user.

**Changes**: New in Zulip 4.0 (feature level 48).
</dd>
</dl>
</dd>
</dl>

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

client.users.unmute_user(
    muted_user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**muted_user_id:** `int` 

The ID of the user to mute/unmute.

**Changes**: Before Zulip 8.0 (feature level 188), bot users could not
be muted/unmuted, and specifying a bot user's ID returned an error response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">add_apns_token</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint adds an APNs device token to register for iOS push notifications.

**Changes**: Deprecated in Zulip 11.0 (feature level 406). Clients connecting
to newer servers and with E2EE push notifications support should use the
[Register E2EE push device](/api/register-push-device) endpoint, as this
endpoint will be removed in a future release.
</dd>
</dl>
</dd>
</dl>

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

client.users.add_apns_token(
    token="c0ffee",
    appid="org.zulip.Zulip",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — The token provided by the device.
    
</dd>
</dl>

<dl>
<dd>

**appid:** `str` 

The ID of the Zulip app that is making the request.

**Changes**: In Zulip 8.0 (feature level 223), this parameter was made
required. Previously, if it was unspecified, the server would use a default
value (based on the `ZULIP_IOS_APP_ID` server setting, which
defaulted to `"org.zulip.Zulip"`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">remove_apns_token</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint removes an APNs device token for iOS push notifications.

**Changes**: Deprecated in Zulip 11.0 (feature level 406) and will be
removed in a future release. Clients connecting to newer servers and
with E2EE push notifications support should delete the account record
in their local accounts table that corresponds to the `push_account_id`
supplied when registering via the [Register E2EE push device](/api/register-push-device)
endpoint, to stop displaying notifications for that registration.
</dd>
</dl>
</dd>
</dl>

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

client.users.remove_apns_token(
    token="c0ffee",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — The token provided by the device.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">add_fcm_token</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint adds an FCM registration token for push notifications.

**Changes**: Deprecated in Zulip 11.0 (feature level 406). Clients connecting
to newer servers and with E2EE push notifications support should use the
[Register E2EE push device](/api/register-push-device) endpoint, as this
endpoint will be removed in a future release.
</dd>
</dl>
</dd>
</dl>

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

client.users.add_fcm_token(
    token="android-token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — The token provided by the device.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">remove_fcm_token</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint removes an FCM registration token for push notifications.

**Changes**: Deprecated in Zulip 11.0 (feature level 406) and will be
removed in a future release. Clients connecting to newer servers and
with E2EE push notifications support should delete the account record
in their local accounts table that corresponds to the `push_account_id`
supplied when registering via the [Register E2EE push device](/api/register-push-device)
endpoint, to stop displaying notifications for that registration.
</dd>
</dl>
</dd>
</dl>

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

client.users.remove_fcm_token(
    token="android-token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — The token provided by the device.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_by_email</a>(...) -> GetUserByEmailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch details for a single user in the organization given a Zulip
API email address.

You can also fetch details on [all users in the organization](/api/get-users)
or [by user ID](/api/get-user).

Fetching by user ID is generally recommended when possible,
as a user might [change their email address](/help/change-your-email-address)
or change their [email address visibility](/help/configure-email-visibility),
either of which could change the client's ability to look them up by that
email address.

**Changes**: In Zulip 12.0 (feature level 437), fixed a bug
dating to feature level 232, which caused guest users to
receive fake backwards-compatibility users in the format
intended for clients using `POST /register` without the
`user_list_incomplete` client capability.

Starting with Zulip 10.0 (feature level 302), the real email
address can be used in the `email` parameter and will fetch the target user's
data if and only if the target's email visibility setting permits the requester
to see the email address.
The dummy email addresses of the form `user{id}@{realm.host}` still work, and
will now work for **all** users, via identifying them by the embedded user ID.

New in Zulip Server 4.0 (feature level 39).
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user_by_email(
    email="iago@zulip.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 

The email address of the user to fetch. Two forms are supported:

- The real email address of the user (`delivery_email`). The lookup will
  succeed if and only if the user exists and their email address visibility
  setting permits the client to see the email address.

- The dummy Zulip API email address of the form `user{user_id}@{realm_host}`. This
  is identical to simply [getting user by ID](/api/get-user). If the server or
  realm change domains, the dummy email address used has to be adjustment to
  match the new realm domain. This is legacy behavior for
  backwards-compatibility, and will be removed in a future release.

**Changes**: Starting with Zulip 10.0 (feature level 302), lookups by real email
address match the semantics of the target's email visibility setting and dummy
email addresses work for all users, independently of their email visibility
setting.

Previously, lookups were done only using the Zulip API email addresses.
    
</dd>
</dl>

<dl>
<dd>

**client_gravatar:** `typing.Optional[bool]` 

Whether the client supports computing gravatars URLs. If
enabled, `avatar_url` will be included in the response only
if there is a Zulip avatar, and will be `null` for users who
are using gravatar as their avatar. This option
significantly reduces the compressed size of user data,
since gravatar URLs are long, random strings and thus do not
compress well. The `client_gravatar` field is set to `true` if
clients can compute their own gravatars.

**Changes**: The default value of this parameter was `false`
prior to Zulip 5.0 (feature level 92).
    
</dd>
</dl>

<dl>
<dd>

**include_custom_profile_fields:** `typing.Optional[bool]` 

Whether the client wants [custom profile field](/help/custom-profile-fields)
data to be included in the response.

**Changes**: New in Zulip 2.1.0. Previous versions do not offer these
data via the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user_by_email</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Administrative endpoint to update the details of another user in the organization by their email address.
Works the same way as [`PATCH /users/{user_id}`](/api/update-user) but fetching the target user by their
real email address.

The requester needs to have permission to view the target user's real email address, subject to the
user's email address visibility setting. Otherwise, the dummy address of the format
`user{id}@{realm.host}` needs be used. This follows the same rules as `GET /users/{email}`.

**Changes**: New in Zulip 10.0 (feature level 313).
</dd>
</dl>
</dd>
</dl>

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

client.users.update_user_by_email(
    email="hamlet@zulip.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 

The email address of the user, specified following the same rules as
[`GET /users/{email}`](/api/get-user-by-email).
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` 

The user's full name.

**Changes**: Removed unnecessary JSON-encoding of this parameter in
Zulip 5.0 (feature level 106).
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[int]` 

New [role](/api/roles-and-permissions) for the user. Roles are encoded as:

- Organization owner: 100
- Organization administrator: 200
- Organization moderator: 300
- Member: 400
- Guest: 600

Only organization owners can add or remove the owner role.

The owner role cannot be removed from the only organization owner.

**Changes**: New in Zulip 3.0 (feature level 8), replacing the previous
pair of `is_admin` and `is_guest` boolean parameters. Organization moderator
role added in Zulip 4.0 (feature level 60).
    
</dd>
</dl>

<dl>
<dd>

**profile_data:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` — A dictionary containing the updated custom profile field data for the user.
    
</dd>
</dl>

<dl>
<dd>

**new_email:** `typing.Optional[str]` 

New email address for the user. Requires the user making the request
to be an organization owner and additionally have the `.can_change_user_emails`
special permission.

**Changes**: New in Zulip 10.0 (feature level 285).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user</a>(...) -> GetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch details for a single user in the organization.

You can also fetch details on [all users in the organization](/api/get-users)
or [by a user's Zulip API email](/api/get-user-by-email).

**Changes**: In Zulip 12.0 (feature level 437), fixed a bug
dating to feature level 232, which caused guest users to
receive fake backwards-compatibility users in the format
intended for clients using `POST /register` without the
`user_list_incomplete` client capability.

New in Zulip 3.0 (feature level 1).
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**client_gravatar:** `typing.Optional[bool]` 

Whether the client supports computing gravatars URLs. If
enabled, `avatar_url` will be included in the response only
if there is a Zulip avatar, and will be `null` for users who
are using gravatar as their avatar. This option
significantly reduces the compressed size of user data,
since gravatar URLs are long, random strings and thus do not
compress well. The `client_gravatar` field is set to `true` if
clients can compute their own gravatars.

**Changes**: The default value of this parameter was `false`
prior to Zulip 5.0 (feature level 92).
    
</dd>
</dl>

<dl>
<dd>

**include_custom_profile_fields:** `typing.Optional[bool]` 

Whether the client wants [custom profile field](/help/custom-profile-fields)
data to be included in the response.

**Changes**: New in Zulip 2.1.0. Previous versions do not offer these
data via the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">deactivate_user</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Deactivates a
user](https://zulip.com/help/deactivate-or-reactivate-a-user)
given their user ID.

Note that any bots controlled by the user will be deactivated
before the user; clients that don't want this behavior are
expected to prompt the user to adjust the bot's owners before
making this API request.
</dd>
</dl>
</dd>
</dl>

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

client.users.deactivate_user(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[str]` 

Additional actions for the server to perform while deactivating the user.

As with the actual deactivation, actions are first applied
to any bots controlled by the target user, and then to the
target user.

**Changes**: New in Zulip 12.0 (feature level 459).
    
</dd>
</dl>

<dl>
<dd>

**deactivation_notification_comment:** `typing.Optional[str]` 

If not `null`, requests that the deactivated user receive
a notification email about their account deactivation.

If not `""`, encodes custom text written by the administrator
to be included in the notification email.

**Changes**: New in Zulip 5.0 (feature level 135).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Administrative endpoint to update the details of another user in the organization.

Supports everything an administrator can do to edit details of another
user's account, including editing full name,
[role](/help/user-roles), and [custom profile
fields](/help/custom-profile-fields).
</dd>
</dl>
</dd>
</dl>

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

client.users.update_user(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` 

The user's full name.

**Changes**: Removed unnecessary JSON-encoding of this parameter in
Zulip 5.0 (feature level 106).
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[int]` 

New [role](/api/roles-and-permissions) for the user. Roles are encoded as:

- Organization owner: 100
- Organization administrator: 200
- Organization moderator: 300
- Member: 400
- Guest: 600

Only organization owners can add or remove the owner role.

The owner role cannot be removed from the only organization owner.

**Changes**: New in Zulip 3.0 (feature level 8), replacing the previous
pair of `is_admin` and `is_guest` boolean parameters. Organization moderator
role added in Zulip 4.0 (feature level 60).
    
</dd>
</dl>

<dl>
<dd>

**profile_data:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` — A dictionary containing the updated custom profile field data for the user.
    
</dd>
</dl>

<dl>
<dd>

**new_email:** `typing.Optional[str]` 

New email address for the user. Requires the user making the request
to be an organization owner and additionally have the `.can_change_user_emails`
special permission.

**Changes**: New in Zulip 10.0 (feature level 285).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_settings</a>(...) -> IgnoredParametersSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to edit the current user's settings.

When invoked by a realm admin, it supports bulk updates to
settings for specified users or members of user groups using
the `target_users` parameter.

**Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
as we now have `web_font_size_px` and `web_line_height_percent`
settings for more control.

Prior to Zulip 5.0 (feature level 80), this endpoint only
supported the `full_name`, `email`, `old_password`, and
`new_password` parameters. Notification settings were
managed by `PATCH /settings/notifications`, and all other
settings by `PATCH /settings/display`.

The feature level 80 migration to merge these endpoints did not
change how request parameters are encoded. However, it did change
the handling of any invalid parameters present in a request
(see feature level 78 change below).

As of feature level 80, the `PATCH /settings/display` and
`PATCH /settings/notifications` endpoints are deprecated aliases
for this endpoint for backwards-compatibility, and will be removed
once clients have migrated to use this endpoint.

Prior to Zulip 5.0 (feature level 78), this endpoint indicated
which parameters it had processed by including in the response
object `"key": value` entries for values successfully changed by
the request. That was replaced by the more ergonomic
[`ignored_parameters_unsupported`][ignored-parameters] array.

The `PATCH /settings/notifications` and `PATCH /settings/display`
endpoints also had this behavior of indicating processed parameters
before they became aliases of this endpoint in Zulip 5.0 (see
feature level 80 change above).

Before feature level 78, request parameters that were not supported
(or were unchanged) were silently ignored.

[ignored-parameters]: /api/rest-error-handling#ignored-parameters
</dd>
</dl>
</dd>
</dl>

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

client.users.update_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_users:** `typing.Optional[UpdateSettingsRequestTargetUsers]` 

An object specifying the collection of users whose settings should be modified,
for modification of other users' settings by an organization administrator.
When this parameter is absent, this API endpoint always modifies the current
user's own settings.

**Changes**: New in Zulip 12.0 (feature level 444).
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` — A new display name for the user.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 

Asks the server to initiate a confirmation sequence to change the user's email
address to the indicated value. The user will need to demonstrate control of the
new email address by clicking a confirmation link sent to that address.
    
</dd>
</dl>

<dl>
<dd>

**old_password:** `typing.Optional[str]` 

The user's old Zulip password (or LDAP password, if LDAP authentication is in use).

Required only when sending the `new_password` parameter.
    
</dd>
</dl>

<dl>
<dd>

**new_password:** `typing.Optional[str]` 

The user's new Zulip password (or LDAP password, if LDAP authentication is in use).

The `old_password` parameter must be included in the request.
    
</dd>
</dl>

<dl>
<dd>

**twenty_four_hour_time:** `typing.Optional[bool]` 

Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**web_mark_read_on_scroll_policy:** `typing.Optional[int]` 

Whether or not to mark messages as read when the user scrolls through their
feed.

- 1 - Always
- 2 - Only in conversation views
- 3 - Never

**Changes**: New in Zulip 7.0 (feature level 175). Previously, there was no
way for the user to configure this behavior on the web, and the Zulip web and
desktop apps behaved like the "Always" setting when marking messages as read.
    
</dd>
</dl>

<dl>
<dd>

**web_channel_default_view:** `typing.Optional[int]` 

Web/desktop app setting controlling the default navigation
behavior when clicking on a channel link.

- 1 - Top topic in the channel
- 2 - Channel feed
- 3 - List of topics
- 4 - Top unread topic in channel

**Changes**: The "Top unread topic in channel" is new in Zulip 11.0
(feature level 401).

The "List of topics" option is new in Zulip 11.0 (feature level 383).

New in Zulip 9.0 (feature level 269). Previously, this
was not configurable, and every user had the "Channel feed" behavior.
    
</dd>
</dl>

<dl>
<dd>

**starred_message_counts:** `typing.Optional[bool]` 

Whether clients should display the [number of starred
messages](/help/star-a-message#display-the-number-of-starred-messages).

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**receives_typing_notifications:** `typing.Optional[bool]` 

Whether the user is configured to receive typing notifications from other users.
The server will only deliver typing notifications events to users who for whom this
is enabled.

By default, this is set to true, enabling user to receive typing
notifications from other users.

**Changes**: New in Zulip 9.0 (feature level 253). Previously, there were only
options to disable sending typing notifications.
    
</dd>
</dl>

<dl>
<dd>

**web_suggest_update_timezone:** `typing.Optional[bool]` 

Whether the user should be shown an alert, offering to update their
[profile time zone](/help/change-your-timezone), when the time displayed
for the profile time zone differs from the current time displayed by the
time zone configured on their device.

**Changes**: New in Zulip 10.0 (feature level 329).
    
</dd>
</dl>

<dl>
<dd>

**fluid_layout_width:** `typing.Optional[bool]` 

Whether to use the [maximum available screen width](/help/enable-full-width-display)
for the web app's center panel (message feed, recent conversations) on wide screens.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**high_contrast_mode:** `typing.Optional[bool]` 

This setting is reserved for use to control variations in Zulip's design
to help visually impaired users.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**web_font_size_px:** `typing.Optional[int]` 

User-configured primary `font-size` for the web application, in pixels.

**Changes**: New in Zulip 9.0 (feature level 245). Previously, font size was
only adjustable via browser zoom. Note that this setting was not fully
implemented at this feature level.
    
</dd>
</dl>

<dl>
<dd>

**web_line_height_percent:** `typing.Optional[int]` 

User-configured primary `line-height` for the web application, in percent, so a
value of 120 represents a `line-height` of 1.2.

**Changes**: New in Zulip 9.0 (feature level 245). Previously, line height was
not user-configurable. Note that this setting was not fully implemented at this
feature level.
    
</dd>
</dl>

<dl>
<dd>

**color_scheme:** `typing.Optional[int]` 

Controls which [color theme](/help/dark-theme) to use.

- 1 - Automatic
- 2 - Dark theme
- 3 - Light theme

Automatic detection is implementing using the standard `prefers-color-scheme`
media query.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_drafts_synchronization:** `typing.Optional[bool]` 

A boolean parameter to control whether synchronizing drafts is enabled for
the user. When synchronization is disabled, all drafts stored in the server
will be automatically deleted from the server.

This does not do anything (like sending events) to delete local copies of
drafts stored in clients.

**Changes**: New in Zulip 5.0 (feature level 87).
    
</dd>
</dl>

<dl>
<dd>

**translate_emoticons:** `typing.Optional[bool]` 

Whether to [translate emoticons to emoji](/help/configure-emoticon-translations)
in messages the user sends.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**display_emoji_reaction_users:** `typing.Optional[bool]` 

Whether to display the names of reacting users on a message.

When enabled, clients should display the names of reacting users, rather than
a count, for messages with few total reactions. The ideal cutoff may depend on
the space available for displaying reactions; the official web application
displays names when 3 or fewer total reactions are present with this setting
enabled.

**Changes**: New in Zulip 6.0 (feature level 125).
    
</dd>
</dl>

<dl>
<dd>

**default_language:** `typing.Optional[str]` 

What [default language](/help/change-your-language) to use for the account.

This controls both the Zulip UI as well as email notifications sent to the user.

The value needs to be a standard language code that the Zulip server has
translation data for; for example, `"en"` for English or `"de"` for German.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.

Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 63).
    
</dd>
</dl>

<dl>
<dd>

**web_home_view:** `typing.Optional[str]` 

The [home view](/help/configure-home-view) used when opening a new
Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.

- "recent" - Recent conversations view
- "inbox" - Inbox view
- "all_messages" - Combined feed view

**Changes**: Before Zulip 12.0 (feature level 454), the Recent
view had `"recent_topics"` as its string encoding.

New in Zulip 8.0 (feature level 219). Previously, this was called
`default_view`, which was new in Zulip 4.0 (feature level 42).

Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.

Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).
    
</dd>
</dl>

<dl>
<dd>

**web_escape_navigates_to_home_view:** `typing.Optional[bool]` 

Whether the escape key navigates to the
[configured home view](/help/configure-home-view).

**Changes**: New in Zulip 8.0 (feature level 219). Previously, this
was called `escape_navigates_to_default_view`, which was new in Zulip
5.0 (feature level 107).
    
</dd>
</dl>

<dl>
<dd>

**left_side_userlist:** `typing.Optional[bool]` 

Whether the users list on left sidebar in narrow windows.

This feature is not heavily used and is likely to be reworked.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**emojiset:** `typing.Optional[str]` 

The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons),
used to display emoji to the user everywhere they appear in the UI.

- "google" - Google modern
- "twitter" - Twitter
- "text" - Plain text

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.

Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).
    
</dd>
</dl>

<dl>
<dd>

**demote_inactive_streams:** `typing.Optional[int]` 

Whether to [hide inactive channels](/help/manage-inactive-channels) in the left sidebar.

- 1 - Automatic
- 2 - Always
- 3 - Never

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**user_list_style:** `typing.Optional[int]` 

The style selected by the user for the right sidebar user list.

- 1 - Compact
- 2 - With status
- 3 - With avatar and status

**Changes**: New in Zulip 6.0 (feature level 141).
    
</dd>
</dl>

<dl>
<dd>

**web_animate_image_previews:** `typing.Optional[UpdateSettingsRequestWebAnimateImagePreviews]` 

Controls how animated images should be played in the message feed in the web/desktop application.

- "always" - Always play the animated images in the message feed.
- "on_hover" - Play the animated images on hover over them in the message feed.
- "never" - Never play animated images in the message feed.

**Changes**: New in Zulip 9.0 (feature level 275).
    
</dd>
</dl>

<dl>
<dd>

**web_stream_unreads_count_display_policy:** `typing.Optional[int]` 

Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
Channels that do not have an unread count will have a simple dot indicator for whether there are any
unread messages.

- 1 - All channels
- 2 - Unmuted channels and topics
- 3 - No channels

**Changes**: New in Zulip 8.0 (feature level 210).
    
</dd>
</dl>

<dl>
<dd>

**hide_ai_features:** `typing.Optional[bool]` 

Controls whether user wants AI features like topic summarization to
be hidden in all Zulip clients.

**Changes**: New in Zulip 10.0 (feature level 350).
    
</dd>
</dl>

<dl>
<dd>

**web_inbox_show_channel_folders:** `typing.Optional[bool]` 

Determines whether [channel folders](/help/channel-folders)
are used to organize how conversations with unread messages
are displayed in the web/desktop application's Inbox view.

**Changes**: New in Zulip 12.0 (feature level 431).
    
</dd>
</dl>

<dl>
<dd>

**web_left_sidebar_show_channel_folders:** `typing.Optional[bool]` 

Determines whether [channel folders](/help/channel-folders)
are used to organize how channels are displayed in the
web/desktop application's left sidebar.

**Changes**: New in Zulip 11.0 (feature level 411).
    
</dd>
</dl>

<dl>
<dd>

**web_left_sidebar_unreads_count_summary:** `typing.Optional[bool]` 

Determines whether the web/desktop application's left sidebar displays
the unread message count summary.

**Changes**: New in Zulip 11.0 (feature level 398).
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 

The IANA identifier of the user's [profile time zone](/help/change-your-timezone),
which is used primarily to display the user's local time to other users.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/display` endpoint.

Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_desktop_notifications:** `typing.Optional[bool]` 

Enable visual desktop notifications for channel messages.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_email_notifications:** `typing.Optional[bool]` 

Enable email notifications for channel messages.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_push_notifications:** `typing.Optional[bool]` 

Enable mobile notifications for channel messages.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_audible_notifications:** `typing.Optional[bool]` 

Enable audible desktop notifications for channel messages.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**notification_sound:** `typing.Optional[str]` 

Notification sound name.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.

Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 63).
    
</dd>
</dl>

<dl>
<dd>

**enable_desktop_notifications:** `typing.Optional[bool]` 

Enable visual desktop notifications for direct messages and @-mentions.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_sounds:** `typing.Optional[bool]` 

Enable audible desktop notifications for direct messages and
@-mentions.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**email_notifications_batching_period_seconds:** `typing.Optional[int]` 

The duration (in seconds) for which the server should wait to batch
email notifications before sending them.

**Changes**: New in Zulip 5.0 (feature level 82)
    
</dd>
</dl>

<dl>
<dd>

**enable_offline_email_notifications:** `typing.Optional[bool]` 

Enable email notifications for direct messages and @-mentions received
when the user is offline.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_offline_push_notifications:** `typing.Optional[bool]` 

Enable mobile notification for direct messages and @-mentions received
when the user is offline.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_online_push_notifications:** `typing.Optional[bool]` 

Enable mobile notification for direct messages and @-mentions received
when the user is online.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_desktop_notifications:** `typing.Optional[bool]` 

Enable visual desktop notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_email_notifications:** `typing.Optional[bool]` 

Enable email notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_push_notifications:** `typing.Optional[bool]` 

Enable push notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_audible_notifications:** `typing.Optional[bool]` 

Enable audible desktop notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**enable_digest_emails:** `typing.Optional[bool]` 

Enable digest emails when the user is away.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_marketing_emails:** `typing.Optional[bool]` 

Enable marketing emails. Has no function outside Zulip Cloud.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_login_emails:** `typing.Optional[bool]` 

Enable email notifications for new logins to account.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**message_content_in_email_notifications:** `typing.Optional[bool]` 

Include the message's content in email notifications for new messages.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**pm_content_in_desktop_notifications:** `typing.Optional[bool]` 

Include content of direct messages in desktop notifications.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**wildcard_mentions_notify:** `typing.Optional[bool]` 

Whether wildcard mentions (E.g. @**all**) should send notifications
like a personal mention.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_wildcard_mentions_notify:** `typing.Optional[bool]` 

Whether wildcard mentions (e.g., @**all**) in messages sent to followed topics
should send notifications like a personal mention.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**desktop_icon_count_display:** `typing.Optional[int]` 

Unread count badge (appears in desktop sidebar and browser tab)

- 1 - All unread messages
- 2 - DMs, mentions, and followed topics
- 3 - DMs and mentions
- 4 - None

**Changes**: In Zulip 8.0 (feature level 227), added `DMs, mentions, and followed
topics` option, renumbering the options to insert it in order.

Before Zulip 5.0 (feature level 80), this setting was managed by the
`PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**realm_name_in_email_notifications_policy:** `typing.Optional[int]` 

Whether to [include organization name in subject of message notification
emails](/help/email-notifications#include-organization-name-in-subject-line).

- 1 - Automatic
- 2 - Always
- 3 - Never

**Changes**: New in Zulip 7.0 (feature level 168), replacing the
previous `realm_name_in_notifications` boolean;
`true` corresponded to `Always`, and `false` to `Never`.

Before Zulip 5.0 (feature level 80), the previous `realm_name_in_notifications`
setting was managed by the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**automatically_follow_topics_policy:** `typing.Optional[int]` 

Which [topics to follow automatically](/help/mute-a-topic).

- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never

**Changes**: New in Zulip 8.0 (feature level 214).
    
</dd>
</dl>

<dl>
<dd>

**automatically_unmute_topics_in_muted_streams_policy:** `typing.Optional[int]` 

Which [topics to unmute automatically in muted channels](/help/mute-a-topic).

- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never

**Changes**: New in Zulip 8.0 (feature level 214).
    
</dd>
</dl>

<dl>
<dd>

**automatically_follow_topics_where_mentioned:** `typing.Optional[bool]` 

Whether the server will automatically mark the user as following
topics where the user is mentioned.

**Changes**: New in Zulip 8.0 (feature level 235).
    
</dd>
</dl>

<dl>
<dd>

**resolved_topic_notice_auto_read_policy:** `typing.Optional[UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy]` 

Controls whether the resolved-topic notices are marked as read.

- "always" - Always mark resolved-topic notices as read.
- "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
- "never" - Never mark resolved-topic notices as read.

**Changes**: New in Zulip 11.0 (feature level 385).
    
</dd>
</dl>

<dl>
<dd>

**presence_enabled:** `typing.Optional[bool]` 

Display the presence status to other users when online.

**Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
the `PATCH /settings/notifications` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enter_sends:** `typing.Optional[bool]` 

Whether pressing Enter in the compose box sends a message
(or saves a message edit).

**Changes**: Before Zulip 5.0 (feature level 81), this setting was managed by
the `POST /users/me/enter-sends` endpoint, with the same parameter format.
    
</dd>
</dl>

<dl>
<dd>

**send_private_typing_notifications:** `typing.Optional[bool]` 

Whether [typing notifications](/help/typing-notifications) be sent when composing
direct messages.

**Changes**: New in Zulip 5.0 (feature level 105).
    
</dd>
</dl>

<dl>
<dd>

**send_stream_typing_notifications:** `typing.Optional[bool]` 

Whether [typing notifications](/help/typing-notifications) be sent when composing
channel messages.

**Changes**: New in Zulip 5.0 (feature level 105).
    
</dd>
</dl>

<dl>
<dd>

**send_read_receipts:** `typing.Optional[bool]` 

Whether other users are allowed to see whether you've
read messages.

**Changes**: New in Zulip 5.0 (feature level 105).
    
</dd>
</dl>

<dl>
<dd>

**allow_private_data_export:** `typing.Optional[bool]` 

Whether organization administrators are allowed to
export your private data.

**Changes**: New in Zulip 10.0 (feature level 293).
    
</dd>
</dl>

<dl>
<dd>

**email_address_visibility:** `typing.Optional[int]` 

The [policy][permission-level] this user has selected for [which other
users][help-email-visibility] in this organization can see their real
email address.

- 1 = Everyone
- 2 = Members only
- 3 = Administrators only
- 4 = Nobody
- 5 = Moderators only

**Changes**: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.

[permission-level]: /api/roles-and-permissions#permission-levels
[help-email-visibility]: /help/configure-email-visibility
    
</dd>
</dl>

<dl>
<dd>

**web_navigate_to_sent_message:** `typing.Optional[bool]` 

Web/desktop app setting for whether the user's view should
automatically go to the conversation where they sent a message.

**Changes**: New in Zulip 9.0 (feature level 268). Previously,
this behavior was not configurable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">set_typing_status</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Notify other users whether the current user is
[typing a message][help-typing].

Clients implementing Zulip's typing notifications
protocol should work as follows:

- Send a request to this endpoint with `"op": "start"` when a user
  starts composing a message.
- While the user continues to actively type or otherwise interact with
  the compose UI (e.g. interacting with the compose box emoji picker),
  send regular `"op": "start"` requests to this endpoint, using
  `server_typing_started_wait_period_milliseconds` in the
  [`POST /register`][api-register] response as the time interval
  between each request.
- Send a request to this endpoint with `"op": "stop"` when a user
  has stopped using the compose UI for the time period indicated by
  `server_typing_stopped_wait_period_milliseconds` in the
  [`POST /register`][api-register] response or when a user
  cancels the compose action (if it had previously sent a "start"
  notification for that compose action).
- Start displaying a visual typing indicator for a given conversation
  when a [`typing op:start`][start-typing] event is received
  from the server.
- Continue displaying a visual typing indicator for the conversation
  until a [`typing op:stop`][stop-typing] event is received
  from the server or the time period indicated by
  `server_typing_started_expiry_period_milliseconds` in the
  [`POST /register`][api-register] response has passed without
  a new `typing "op": "start"` event for the conversation.

This protocol is designed to allow the server-side typing notifications
implementation to be stateless while being resilient as network failures
will not result in a user being incorrectly displayed as perpetually
typing.

See the subsystems documentation on [typing indicators][typing-protocol-docs]
for additional design details on Zulip's typing notifications protocol.

**Changes**: Clients shouldn't care about the APIs prior to Zulip 8.0 (feature level 215)
for channel typing notifications, as no client actually implemented
the previous API for those.

Support for displaying channel typing notifications was new
in Zulip 4.0 (feature level 58). Clients should indicate they support
processing channel typing notifications via the `stream_typing_notifications`
value in the `client_capabilities` parameter of the
[`POST /register`][client-capabilities] endpoint.

[help-typing]: /help/typing-notifications
[api-register]: /api/register-queue
[start-typing]: /api/get-events#typing-start
[stop-typing]: /api/get-events#typing-stop
[client-capabilities]: /api/register-queue#parameter-client_capabilities
[typing-protocol-docs]: https://zulip.readthedocs.io/en/latest/subsystems/typing-indicators.html
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.users import SetTypingStatusRequestOp

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.set_typing_status(
    op=SetTypingStatusRequestOp.START,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**op:** `SetTypingStatusRequestOp` — Whether the user has started (`"start"`) or stopped (`"stop"`) typing.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[SetTypingStatusRequestType]` 

Type of the message being composed.

**Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
an additional value for this parameter to indicate a channel message is
being composed.

In Zulip 8.0 (feature level 215), stopped supporting
`"private"` as a valid value for this parameter.

In Zulip 7.0 (feature level 174), `"direct"` was added
as the preferred way to indicate a direct message is being composed,
becoming the default value for this parameter and deprecating the
original `"private"`.

New in Zulip 4.0 (feature level 58). Previously, typing notifications
were only for direct messages.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[typing.List[int]]` 

User IDs of the recipients of the message being typed. Required for the
`"direct"` type. Ignored in the case of `"stream"` or `"channel"` type.

Clients should send a JSON-encoded list of user IDs, even if there is only
one recipient.

**Changes**: In Zulip 8.0 (feature level 215), stopped using this parameter
for the `"stream"` type. Previously, in the case of the `"stream"` type, it
accepted a single-element list containing the ID of the channel. A new parameter,
`stream_id`, is now used for this. Note that the `"channel"` type did not
exist at this feature level.

Support for typing notifications for channel' messages
is new in Zulip 4.0 (feature level 58). Previously, typing
notifications were only for direct messages.

Before Zulip 2.0.0, this parameter accepted only a JSON-encoded
list of email addresses. Support for the email address-based format was
removed in Zulip 3.0 (feature level 11).
    
</dd>
</dl>

<dl>
<dd>

**stream_id:** `typing.Optional[int]` 

ID of the channel in which the message is being typed. Required for the `"stream"`
or `"channel"` type. Ignored in the case of `"direct"` type.

**Changes**: New in Zulip 8.0 (feature level 215). Previously, a single-element
list containing the ID of the channel was passed in `to` parameter.
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` 

Topic to which message is being typed. Required for the `"stream"` or `"channel"`
type. Ignored in the case of `"direct"` type.

Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
found in the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

**Changes**: Before Zulip 10.0 (feature level 372),
`"(no topic)"` was not interpreted as an empty string.

Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.

New in Zulip 4.0 (feature level 58). Previously, typing notifications
were only for direct messages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">set_typing_status_for_message_edit</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Notify other users whether the current user is editing a message.

Typing notifications for editing messages follow the same protocol as
[set-typing-status](/api/set-typing-status), see that endpoint for
details.

**Changes**: Before Zulip 10.0 (feature level 361), the endpoint was
named `/message_edit_typing` with `message_id` a required parameter in
the request body. Clients are recommended to start using sending these
typing notifications starting from this feature level.

New in Zulip 10.0 (feature level 351). Previously, typing notifications were
not available when editing messages.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.users import SetTypingStatusForMessageEditRequestOp

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.set_typing_status_for_message_edit(
    message_id=1,
    op=SetTypingStatusForMessageEditRequestOp.START,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `int` — The target message's ID.
    
</dd>
</dl>

<dl>
<dd>

**op:** `SetTypingStatusForMessageEditRequestOp` — Whether the user has started (`"start"`) or stopped (`"stop"`) editing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">create_user_group</a>(...) -> CreateUserGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [user group](/help/user-groups).
</dd>
</dl>
</dd>
</dl>

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

client.users.create_user_group(
    name="marketing",
    description="The marketing team.",
    members=[
        1,
        2,
        3,
        4
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

**name:** `str` — The name of the user group.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of the user group.
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.List[int]` 

An array containing the user IDs of the initial members for the
new user group.
    
</dd>
</dl>

<dl>
<dd>

**subgroups:** `typing.Optional[typing.List[int]]` 

An array containing the IDs of the initial subgroups for the new
user group.

User can add subgroups to the new group irrespective of other
permissions for the new group.

**Changes**: New in Zulip 10.0 (feature level 311).
    
</dd>
</dl>

<dl>
<dd>

**can_add_members_group:** `typing.Optional[CreateUserGroupRequestCanAddMembersGroup]` 

A [group-setting value][setting-values] defining the set of users who
have permission to add members to this user group.

**Changes**: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by the `can_manage_group` setting.

[setting-values]: /api/group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**can_join_group:** `typing.Optional[CreateUserGroupRequestCanJoinGroup]` 

A [group-setting value][setting-values] defining the set of users who
have permission to join this user group.

**Changes**: New in Zulip 10.0 (feature level 301).

[setting-values]: /api/group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**can_leave_group:** `typing.Optional[CreateUserGroupRequestCanLeaveGroup]` 

A [group-setting value][setting-values] defining the set of users who
have permission to leave this user group.

**Changes**: New in Zulip 10.0 (feature level 308).

[setting-values]: /api/group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**can_manage_group:** `typing.Optional[CreateUserGroupRequestCanManageGroup]` 

A [group-setting value][setting-values] defining the set of users who
have permission to [manage this user group][manage-user-groups].

This setting cannot be set to `"role:internet"` and `"role:everyone"`
[system groups][system-groups].

**Changes**: New in Zulip 10.0 (feature level 283).

[setting-values]: /api/group-setting-values
[system-groups]: /api/group-setting-values#system-groups
[manage-user-groups]: /help/manage-user-groups
    
</dd>
</dl>

<dl>
<dd>

**can_mention_group:** `typing.Optional[CreateUserGroupRequestCanMentionGroup]` 

A [group-setting value][setting-values] defining the set of users who
have permission to [mention this user group][mentions].

This setting cannot be set to `"role:internet"` and `"role:owners"`
[system groups][system-groups].

Before Zulip 9.0 (feature level 258), this parameter could only be the
integer form of a [group-setting value][setting-values].

Before Zulip 8.0 (feature level 198), this parameter was named
`can_mention_group_id`.

New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were not [system groups][system-groups].

[setting-values]: /api/group-setting-values
[system-groups]: /api/group-setting-values#system-groups
[mentions]: /help/mention-a-user-or-group
    
</dd>
</dl>

<dl>
<dd>

**can_remove_members_group:** `typing.Optional[CreateUserGroupRequestCanRemoveMembersGroup]` 

A [group-setting value][setting-values] defining the set of users who
have permission to remove members from this user group.

**Changes**: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by the `can_manage_group` setting.

[setting-values]: /api/group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_group_members</a>(...) -> GetUserGroupMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the members of a [user group](/help/user-groups).

**Changes**: New in Zulip 6.0 (feature level 127).
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user_group_members(
    user_group_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_group_id:** `int` — The ID of the target user group.
    
</dd>
</dl>

<dl>
<dd>

**direct_member_only:** `typing.Optional[bool]` 

Whether to consider only the direct members of user group and not members
of its subgroups. Default is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user_group_members</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the members of a [user group](/help/user-groups). The
user IDs must correspond to non-deactivated users.

**Changes**: Prior to Zulip 11.0 (feature level 391), members
could not be added or removed from a deactivated group.

**Changes**: Prior to Zulip 10.0 (feature level 303), group memberships of
deactivated users were visible to the API and could be edited via this endpoint.
</dd>
</dl>
</dd>
</dl>

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

client.users.update_user_group_members(
    user_group_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_group_id:** `int` — The ID of the target user group.
    
</dd>
</dl>

<dl>
<dd>

**delete:** `typing.Optional[typing.List[int]]` — The list of user IDs to be removed from the user group.
    
</dd>
</dl>

<dl>
<dd>

**add:** `typing.Optional[typing.List[int]]` — The list of user IDs to be added to the user group.
    
</dd>
</dl>

<dl>
<dd>

**delete_subgroups:** `typing.Optional[typing.List[int]]` 

The list of user group IDs to be removed from the user group.

**Changes**: New in Zulip 10.0 (feature level 311).
    
</dd>
</dl>

<dl>
<dd>

**add_subgroups:** `typing.Optional[typing.List[int]]` 

The list of user group IDs to be added to the user group.

**Changes**: New in Zulip 10.0 (feature level 311).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user_group</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name, description or any of the permission settings
of a [user group](/help/user-groups).

This endpoint is also used to reactivate a user group.

Note that while permissions settings of deactivated groups can
be edited by this API endpoint, and those permissions settings
do affect the ability to modify the deactivated group and its
membership, the deactivated group itself cannot be mentioned
or used in the value of any permission without first being reactivated.

**Changes**: Starting with Zulip 11.0 (feature level 386), this
endpoint can be used to reactivate a user group.

Prior to Zulip 10.0 (feature level 340), only the name field
of deactivated groups could be modified.
</dd>
</dl>
</dd>
</dl>

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

client.users.update_user_group(
    user_group_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_group_id:** `int` — The ID of the target user group.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

The new name of the group.

**Changes**: Before Zulip 7.0 (feature level 165), this was
a required field.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

The new description of the group.

**Changes**: Before Zulip 7.0 (feature level 165), this was
a required field.
    
</dd>
</dl>

<dl>
<dd>

**can_add_members_group:** `typing.Optional[UpdateUserGroupRequestCanAddMembersGroup]` 

The set of users who have permission to add members to this user group
expressed as an [update to a group-setting value][update-group-setting].

**Changes**: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by the `can_manage_group` setting.

[update-group-setting]: /api/group-setting-values#updating-group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**can_join_group:** `typing.Optional[UpdateUserGroupRequestCanJoinGroup]` 

The set of users who have permission to join this user group
expressed as an [update to a group-setting value][update-group-setting].

**Changes**: New in Zulip 10.0 (feature level 301).

[update-group-setting]: /api/group-setting-values#updating-group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**can_leave_group:** `typing.Optional[UpdateUserGroupRequestCanLeaveGroup]` 

The set of users who have permission to leave this user group
expressed as an [update to a group-setting value][update-group-setting].

**Changes**: New in Zulip 10.0 (feature level 308).

[update-group-setting]: /api/group-setting-values#updating-group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**can_manage_group:** `typing.Optional[UpdateUserGroupRequestCanManageGroup]` 

The set of users who have permission to [manage this user group][manage-user-groups]
expressed as an [update to a group-setting value][update-group-setting].

This setting cannot be set to `"role:internet"` and `"role:everyone"`
[system groups][system-groups].

**Changes**: New in Zulip 10.0 (feature level 283).

[update-group-setting]: /api/group-setting-values#updating-group-setting-values
[system-groups]: /api/group-setting-values#system-groups
[manage-user-groups]: /help/manage-user-groups
    
</dd>
</dl>

<dl>
<dd>

**can_mention_group:** `typing.Optional[UpdateUserGroupRequestCanMentionGroup]` 

The set of users who have permission to [mention this group][mentions],
expressed as an [update to a group-setting value][update-group-setting].

This setting cannot be set to `"role:internet"` and `"role:owners"`
[system groups][system-groups].

**Changes**: In Zulip 9.0 (feature level 260), this parameter was
updated to only accept an object with the `old` and `new` fields
described below. Prior to this feature level, this parameter could be
either of the two forms of a [group-setting value][setting-values].

Before Zulip 9.0 (feature level 258), this parameter could only be the
integer form of a [group-setting value][setting-values].

Before Zulip 8.0 (feature level 198), this parameter was named
`can_mention_group_id`.

New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were not [system groups][system-groups].

[mentions]: /help/mention-a-user-or-group
[update-group-setting]: /api/group-setting-values#updating-group-setting-values
[system-groups]: /api/group-setting-values#system-groups
[setting-values]: /api/group-setting-values
    
</dd>
</dl>

<dl>
<dd>

**can_remove_members_group:** `typing.Optional[UpdateUserGroupRequestCanRemoveMembersGroup]` 

The set of users who have permission to remove members from this user group
expressed as an [update to a group-setting value][update-group-setting].

**Changes**: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by the `can_manage_group` setting.

[update-group-setting]: /api/group-setting-values#updating-group-setting-values
[system-groups]: /api/group-setting-values#system-groups
    
</dd>
</dl>

<dl>
<dd>

**deactivated:** `typing.Optional[bool]` 

A deactivated user group can be reactivated by passing this
parameter as `false`.

Passing `true` does nothing as user group is deactivated
using [`POST /user_groups/{user_group_id}/deactivate`](deactivate-user-group)
endpoint.

**Changes**: New in Zulip 11.0 (feature level 386).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_groups</a>() -> GetUserGroupsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches all of the user groups in the organization.

!!! warn ""

    **Note**: This endpoint is only available to [members and
    administrators](/help/user-roles); bots and guests
    cannot use this endpoint.
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user_groups()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_group_subgroups</a>(...) -> GetUserGroupSubgroupsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the subgroups of a [user group](/help/user-groups).

**Changes**: New in Zulip 6.0 (feature level 127).
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user_group_subgroups(
    user_group_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_group_id:** `int` — The ID of the target user group.
    
</dd>
</dl>

<dl>
<dd>

**direct_subgroup_only:** `typing.Optional[bool]` 

Whether to consider only direct subgroups of the user group
or subgroups of subgroups also.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user_group_subgroups</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the subgroups of a [user group](/help/user-groups).

**Changes**: Prior to Zulip 11.0 (feature level 391), subgroups
could not be added or removed from a deactivated group.

**Changes**: New in Zulip 6.0 (feature level 127).
</dd>
</dl>
</dd>
</dl>

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

client.users.update_user_group_subgroups(
    user_group_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_group_id:** `int` — The ID of the target user group.
    
</dd>
</dl>

<dl>
<dd>

**delete:** `typing.Optional[typing.List[int]]` — The list of user group IDs to be removed from the user group.
    
</dd>
</dl>

<dl>
<dd>

**add:** `typing.Optional[typing.List[int]]` — The list of user group IDs to be added to the user group.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_is_user_group_member</a>(...) -> GetIsUserGroupMemberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check whether a user is member of user group.

**Changes**: Prior to Zulip 12.0 (feature level 458), this endpoint
did not support querying group membership of bot users.

Prior to Zulip 10.0 (feature level 303),
this would return true when passed a deactivated user
who was a member of the user group before being deactivated.

New in Zulip 6.0 (feature level 127).
</dd>
</dl>
</dd>
</dl>

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

client.users.get_is_user_group_member(
    user_group_id=1,
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_group_id:** `int` — The ID of the target user group.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — The target user's ID.
    
</dd>
</dl>

<dl>
<dd>

**direct_member_only:** `typing.Optional[bool]` 

Whether to consider only the direct members of user group and not members
of its subgroups. Default is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">deactivate_user_group</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate a user group. Deactivated user groups cannot be
used for mentions, permissions, or any other purpose, but can
be reactivated or renamed.

Deactivating user groups is preferable to deleting them from
the database, since the deactivation model allows audit logs
of changes to sensitive group-valued permissions to be
maintained.

**Changes**: New in Zulip 10.0 (feature level 290).
</dd>
</dl>
</dd>
</dl>

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

client.users.deactivate_user_group(
    user_group_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_group_id:** `int` — The ID of the target user group.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_bot_api_key</a>(...) -> GetBotApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the API key for a bot user. Only the bot's owner and
organization administrators have access to a bot's API key.

**Changes**: New in Zulip 12.0 (feature level 463).
</dd>
</dl>
</dd>
</dl>

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

client.users.get_bot_api_key(
    bot_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bot_id:** `int` — The user ID of the target bot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">regenerate_bot_api_key</a>(...) -> RegenerateBotApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a new API key for a bot user. Only the bot's owner and
organization administrators have access to a bot's API key.
</dd>
</dl>
</dd>
</dl>

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

client.users.regenerate_bot_api_key(
    bot_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bot_id:** `int` — The user ID of the target bot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Drafts
<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">get_drafts</a>() -> GetDraftsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all drafts for the current user.
</dd>
</dl>
</dd>
</dl>

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

client.drafts.get_drafts()

```
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

<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">create_drafts</a>(...) -> CreateDraftsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one or more drafts on the server. These drafts will be automatically
synchronized to other clients via `drafts` events.
</dd>
</dl>
</dd>
</dl>

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

client.drafts.create_drafts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drafts:** `typing.Optional[typing.List[Draft]]` — A JSON-encoded list of containing new draft objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">delete_draft</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single draft from the server. The deletion will be automatically
synchronized to other clients via a `drafts` event.
</dd>
</dl>
</dd>
</dl>

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

client.drafts.delete_draft(
    draft_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**draft_id:** `int` — The ID of the draft you want to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">edit_draft</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit a draft on the server. The edit will be automatically
synchronized to other clients via `drafts` events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.drafts import EditDraftRequestDraft, EditDraftRequestDraftType

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drafts.edit_draft(
    draft_id=1,
    draft=EditDraftRequestDraft(
        type=EditDraftRequestDraftType.STREAM,
        to=[
            1
        ],
        topic="questions",
        content="how tough is a Lamy Safari?",
        timestamp=1595479019,
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

**draft_id:** `int` — The ID of the draft to be edited.
    
</dd>
</dl>

<dl>
<dd>

**draft:** `EditDraftRequestDraft` — A JSON-encoded object containing a replacement draft object for this ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">get_saved_snippets</a>() -> GetSavedSnippetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all the saved snippets for the current user.

**Changes**: New in Zulip 10.0 (feature level 297).
</dd>
</dl>
</dd>
</dl>

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

client.drafts.get_saved_snippets()

```
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

<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">create_saved_snippet</a>(...) -> CreateSavedSnippetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new saved snippet for the current user.

**Changes**: New in Zulip 10.0 (feature level 297).
</dd>
</dl>
</dd>
</dl>

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

client.drafts.create_saved_snippet(
    title="Example title",
    content="Welcome to the organization.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — The title of the saved snippet.
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` 

The content of the saved snippet in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

Clients should insert this content into a message when using
a saved snippet.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">delete_saved_snippet</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a saved snippet.

**Changes**: New in Zulip 10.0 (feature level 297).
</dd>
</dl>
</dd>
</dl>

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

client.drafts.delete_saved_snippet(
    saved_snippet_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**saved_snippet_id:** `int` — The ID of the saved snippet to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drafts.<a href="src/fern/drafts/client.py">edit_saved_snippet</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit a saved snippet for the current user.

**Changes**: New in Zulip 10.0 (feature level 368).
</dd>
</dl>
</dd>
</dl>

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

client.drafts.edit_saved_snippet(
    saved_snippet_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**saved_snippet_id:** `int` — The ID of the saved snippet to edit.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the saved snippet.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` 

The content of the saved snippet in the original [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

Clients should insert this content into a message when using
a saved snippet.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NavigationViews
<details><summary><code>client.navigation_views.<a href="src/fern/navigation_views/client.py">get_navigation_views</a>() -> GetNavigationViewsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all configured custom navigation views for the current user.

**Changes**: New in Zulip 11.0 (feature level 390).
</dd>
</dl>
</dd>
</dl>

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

client.navigation_views.get_navigation_views()

```
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

<details><summary><code>client.navigation_views.<a href="src/fern/navigation_views/client.py">add_navigation_view</a>(...) -> AddNavigationViewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new custom left sidebar navigation view configuration
for the current user.

This can be used both to configure built-in navigation views,
or to add new navigation views.

**Changes**: New in Zulip 11.0 (feature level 390).
</dd>
</dl>
</dd>
</dl>

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

client.navigation_views.add_navigation_view(
    fragment="narrow/is/alerted",
    is_pinned=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `NavigationView` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.navigation_views.<a href="src/fern/navigation_views/client.py">remove_navigation_view</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a navigation view.

**Changes**: New in Zulip 11.0 (feature level 390).
</dd>
</dl>
</dd>
</dl>

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

client.navigation_views.remove_navigation_view(
    fragment="narrow/is/alerted",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fragment:** `str` 

The unique URL hash of the navigation view to be removed.

This also serves as the identifier for the navigation view.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.navigation_views.<a href="src/fern/navigation_views/client.py">edit_navigation_view</a>(...) -> EditNavigationViewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of an existing configured navigation view,
such as its name or whether it's pinned.

**Changes**: New in Zulip 11.0 (feature level 390).
</dd>
</dl>
</dd>
</dl>

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

client.navigation_views.edit_navigation_view(
    fragment="fragment",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fragment:** `str` 

The unique URL hash of the navigation view to be updated.

This also serves as the identifier for the navigation view.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EditNavigationViewRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reminders
<details><summary><code>client.reminders.<a href="src/fern/reminders/client.py">get_reminders</a>() -> GetRemindersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all [reminders](/help/schedule-a-reminder) for the
current user.

Reminders are messages the user has scheduled to be sent in the
future to themself.

**Changes**: New in Zulip 11.0 (feature level 399).
</dd>
</dl>
</dd>
</dl>

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

client.reminders.get_reminders()

```
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

<details><summary><code>client.reminders.<a href="src/fern/reminders/client.py">create_message_reminder</a>(...) -> CreateMessageReminderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule a reminder to be sent to the current user at the specified time. The reminder will link the relevant message.

**Changes**: New in Zulip 11.0 (feature level 381).
</dd>
</dl>
</dd>
</dl>

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

client.reminders.create_message_reminder()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_id:** `typing.Optional[int]` — The ID of the previously sent message to reference in the reminder message.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_delivery_timestamp:** `typing.Optional[int]` 

The UNIX timestamp for when the reminder will be sent,
in UTC seconds.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 

A note associated with the reminder shown in the Notification Bot message.

**Changes**: New in Zulip 11.0 (feature level 415).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reminders.<a href="src/fern/reminders/client.py">delete_reminder</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete, and therefore cancel sending, a previously [scheduled
reminder](/help/schedule-a-reminder).

**Changes**: New in Zulip 11.0 (feature level 399).
</dd>
</dl>
</dd>
</dl>

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

client.reminders.delete_reminder(
    reminder_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reminder_id:** `int` 

The ID of the reminder to delete.

This is different from the unique ID that the message would have
after being sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ScheduledMessages
<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">get_scheduled_messages</a>() -> GetScheduledMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all [scheduled messages](/help/schedule-a-message) for
the current user.

Scheduled messages are messages the user has scheduled to be
sent in the future via the send later feature.

**Changes**: New in Zulip 7.0 (feature level 173).
</dd>
</dl>
</dd>
</dl>

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

client.scheduled_messages.get_scheduled_messages()

```
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

<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">create_scheduled_message</a>(...) -> CreateScheduledMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [scheduled message](/help/schedule-a-message).

**Changes**: In Zulip 7.0 (feature level 184), moved support for
[editing a scheduled message](/api/update-scheduled-message) to a
separate API endpoint, which removed the `scheduled_message_id`
parameter from this endpoint.

New in Zulip 7.0 (feature level 179).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.scheduled_messages import CreateScheduledMessageRequestType

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.scheduled_messages.create_scheduled_message(
    type=CreateScheduledMessageRequestType.DIRECT,
    to=1,
    content="Hello",
    scheduled_delivery_timestamp=3165826990,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `CreateScheduledMessageRequestType` 

The type of scheduled message to be sent. `"direct"` for a direct
message and `"stream"` or `"channel"` for a channel message.

Note that, while `"private"` is supported for scheduling direct
messages, clients are encouraged to use to the modern convention of
`"direct"` to indicate this message type, because support for
`"private"` may eventually be removed.

**Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
an additional value for this parameter to indicate the type of a channel
message.
    
</dd>
</dl>

<dl>
<dd>

**to:** `CreateScheduledMessageRequestTo` 

The scheduled message's tentative target audience.

For channel messages, the integer ID of the channel.
For direct messages, a list containing integer user IDs.
    
</dd>
</dl>

<dl>
<dd>

**content:** `RequiredContent` 
    
</dd>
</dl>

<dl>
<dd>

**scheduled_delivery_timestamp:** `int` 

The UNIX timestamp for when the message will be sent,
in UTC seconds.
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` 

The topic of the message. Only required for channel messages
(`"type": "stream"` or `"type": "channel"`), ignored otherwise.

Clients should use the `max_topic_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum topic length.

Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
found in the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

When [topics are required](/help/require-topics), this parameter can't
be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

**Changes**: Before Zulip 10.0 (feature level 370), `"(no topic)"`
was not interpreted as an empty string.

Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**read_by_sender:** `typing.Optional[bool]` 

Whether the message should be initially marked read by its
sender. If unspecified, the server uses a heuristic based
on the client name and the recipient.

**Changes**: New in Zulip 8.0 (feature level 236).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">delete_scheduled_message</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete, and therefore cancel sending, a previously [scheduled
message](/help/schedule-a-message).

**Changes**: New in Zulip 7.0 (feature level 173).
</dd>
</dl>
</dd>
</dl>

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

client.scheduled_messages.delete_scheduled_message(
    scheduled_message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scheduled_message_id:** `int` 

The ID of the scheduled message to delete.

This is different from the unique ID that the message would have
after being sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">update_scheduled_message</a>(...) -> UpdateScheduledMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit an existing [scheduled message](/help/schedule-a-message).

**Changes**: New in Zulip 7.0 (feature level 184).
</dd>
</dl>
</dd>
</dl>

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

client.scheduled_messages.update_scheduled_message(
    scheduled_message_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scheduled_message_id:** `int` 

The ID of the scheduled message to update.

This is different from the unique ID that the message would have
after being sent.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateScheduledMessageRequestType]` 

The type of scheduled message to be sent. `"direct"` for a direct
message and `"stream"` or `"channel"` for a channel message.

When updating the type of the scheduled message, the `to` parameter
is required. And, if updating the type of the scheduled message to
`"stream"`/`"channel"`, then the `topic` parameter is also required.

Note that, while `"private"` is supported for scheduling direct
messages, clients are encouraged to use to the modern convention of
`"direct"` to indicate this message type, because support for
`"private"` may eventually be removed.

**Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
an additional value for this parameter to indicate the type of a channel
message.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[UpdateScheduledMessageRequestTo]` 

The scheduled message's tentative target audience.

For channel messages, the integer ID of the channel.
For direct messages, a list containing integer user IDs.

Required when updating the `type` of the scheduled message.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` 

The updated content of the scheduled message.

Clients should use the `max_message_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum message size.
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` 

The updated topic of the scheduled message.

Required when updating the `type` of the scheduled message to
`"stream"` or `"channel"`. Ignored when the existing or updated
`type` of the scheduled message is `"direct"` (or `"private"`).

Clients should use the `max_topic_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum topic length.

Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
found in the [POST /register](/api/register-queue) response is used for this
parameter, it is interpreted as an empty string.

When [topics are required](/help/require-topics), this parameter can't
be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

**Changes**: Before Zulip 10.0 (feature level 370), `"(no topic)"`
was not interpreted as an empty string.

Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_delivery_timestamp:** `typing.Optional[int]` 

The UNIX timestamp for when the message will be sent,
in UTC seconds.

Required when updating a scheduled message that the server
has already tried and failed to send. This state is indicated
with `"failed": true` in `scheduled_messages` objects; see
response description at
[`GET /scheduled_messages`](/api/get-scheduled-messages#response).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mobile
<details><summary><code>client.mobile.<a href="src/fern/mobile/client.py">test_notify</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger sending a test push notification to the user's
selected mobile device or all of their mobile devices.

**Changes**: Deprecated in Zulip 11.0 (feature level 420).
Clients connecting to newer servers and with E2EE push
notifications support should use the
[Send an E2EE test notification to mobile device(s)](/api/e2ee-test-notify)
endpoint, as this endpoint will be removed in a future release.

Starting with Zulip 8.0 (feature level 234), test
notifications sent via this endpoint use `test` rather than
`test-by-device-token` in the `event` field. Also, as of this
feature level, all mobile push notifications now include a
`realm_name` field.

New in Zulip 8.0 (feature level 217).
</dd>
</dl>
</dd>
</dl>

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

client.mobile.test_notify()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `typing.Optional[str]` 

The push token for the device to which to send the test notification.

If this parameter is not submitted, the test notification will be sent
to all of the user's devices registered on the server.

A mobile client should pass this parameter, to avoid triggering a test
notification for other clients.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mobile.<a href="src/fern/mobile/client.py">e2ee_test_notify</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger sending an end-to-end encrypted (E2EE) test push notification
to the user's selected mobile device or all of their mobile devices.

**Changes**: New in Zulip 11.0 (feature level 420).
</dd>
</dl>
</dd>
</dl>

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

client.mobile.e2ee_test_notify()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `typing.Optional[int]` 

The ID for the device to which to send the test notification.

If this parameter is not submitted, the E2EE test notification will
be sent to all of the user's devices registered on the server.

A mobile client should pass this parameter, to avoid triggering a test
notification for other clients.

See [`POST /register_client_device`](/api/register-client-device)
for details on device ID.

**Changes**: New in Zulip 12.0 (feature level 468).

Previously, `push_account_id` was used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mobile.<a href="src/fern/mobile/client.py">register_push_device</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a device to receive end-to-end encrypted mobile push notifications,
or update such a registration.

To perform an initial registration, clients must provide both the
push key fields (`push_key` and `push_key_id`) and the token fields
(`token_kind`, `token_id`, `bouncer_public_key`, and `encrypted_push_registration`).

Once registered, clients should use this endpoint to rotate `push_key` or
FCM/APNs provided token:

- **Rotate push key**: Provide only the push key fields.
- **Rotate token**: Provide only the token fields.

**Changes**: In Zulip 12.0 (feature level 468), the endpoint
was significantly redesigned to support rotation of `push_key` and
token provided by FCM/APNs.

New in Zulip 11.0 (feature level 406).
</dd>
</dl>
</dd>
</dl>

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

client.mobile.register_push_device(
    device_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `int` 

The ID of the device to configure for push notifications.

See [`POST /register_client_device`](/api/register-client-device)
for how to obtain a device ID.
    
</dd>
</dl>

<dl>
<dd>

**push_key_id:** `typing.Optional[int]` 

A random unsigned 32-bit integer generated by the client as an identifier
for `push_key`. It will be included in mobile push notifications
along with encrypted payloads to identify the `push_key` to decrypt.
    
</dd>
</dl>

<dl>
<dd>

**push_key:** `typing.Optional[str]` 

Key that the client would like the server to use to encrypt notifications,
encoded with Base64.

The key is a byte sequence beginning with a single byte that encodes which
cryptosystem to use, followed by the key to use for that cryptosystem.
This byte sequence is encoded using standard Base64 encoding as defined in RFC 4648.

The client should avoid sharing the key anywhere else: in particular it should
generate a fresh key for each server, and to the extent possible keep the key
out of any backups of the client's data.

Supported cryptosystems are:

- `0x31`: LibSodium's [SecretBox][libsodium-secretbox] symmetric key encryption
  system. Keys are 32 bytes, which the server will use with libsodium's
  `crypto_secretbox_easy`. See the [NaCl documentation][nacl-secretbox], which
  details how this system uses `XSalsa20` and `Poly1305` to provide authenticated
  encryption.

[libsodium-secretbox]: https://libsodium.gitbook.io/doc/secret-key_cryptography/secretbox
[nacl-secretbox]: https://nacl.cr.yp.to/secretbox.html

**Changes**: New in Zulip 12.0 (feature level 432). This replaced the
`push_public_key` parameter which had a prototype asymmetric cryptosystem, and
did not have a natural way to support multiple cryptosystems.
    
</dd>
</dl>

<dl>
<dd>

**token_kind:** `typing.Optional[RegisterPushDeviceRequestTokenKind]` — Whether the token was generated by FCM or APNs.
    
</dd>
</dl>

<dl>
<dd>

**token_id:** `typing.Optional[str]` 

Identifier for the FCM/APNs provided token to the device,
produced by taking the first 8 bytes of the SHA-256 hash of
the token, then encoding those bytes using standard Base64 encoding
as defined in RFC 4648.
    
</dd>
</dl>

<dl>
<dd>

**bouncer_public_key:** `typing.Optional[str]` 

Which of the bouncer's public keys the client used to encrypt the
`PushRegistration` dictionary.

When the bouncer rotates the key, a new asymmetric key pair is created,
and the new public key is baked into a new client release. Because
the bouncer routinely rotates key, this field clarifies which
public key the client is using.

The public key is encoded using standard Base64 encoding as defined
in RFC 4648.
    
</dd>
</dl>

<dl>
<dd>

**encrypted_push_registration:** `typing.Optional[str]` 

Ciphertext generated by encrypting a `PushRegistration` dictionary
using the `bouncer_public_key`, encoded using a RFC 4648 standard
base64 encoder.

The `PushRegistration` dictionary contains the fields `token`,
`token_kind`, `timestamp`, and (for iOS devices) `ios_app_id`.
The dictionary is JSON-encoded before encryption.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mobile.<a href="src/fern/mobile/client.py">register_remote_push_device</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a push device to bouncer to receive end-to-end encrypted
mobile push notifications.

Self-hosted servers use this endpoint to asynchronously register
a push device to the bouncer server after receiving a request from
the mobile client to [register E2EE push device](/api/register-push-device).

It is not meant to be used by mobile clients directly.

**Changes**: New in Zulip 11.0 (feature level 406).
</dd>
</dl>
</dd>
</dl>

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

client.mobile.register_remote_push_device(
    realm_uuid="9aa61d0b-8ce5-488d-8e9e-fedc346e6836",
    token_id="+wKIhyAx/Eg=",
    encrypted_push_registration="encrypted-push-registration-data",
    bouncer_public_key="bouncer-public-key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**realm_uuid:** `str` 

The UUID of the realm to which the push device
being registered belongs.
    
</dd>
</dl>

<dl>
<dd>

**token_id:** `str` 

The `token_id` value provided by the mobile client
to [register E2EE push device](/api/register-push-device).

**Changes**: New in Zulip 12.0 (feature level 468),
replacing `push_account_id`.
    
</dd>
</dl>

<dl>
<dd>

**encrypted_push_registration:** `str` 

The `encrypted_push_registration` value provided by the mobile client
to [register E2EE push device](/api/register-push-device).
    
</dd>
</dl>

<dl>
<dd>

**bouncer_public_key:** `str` 

The `bouncer_public_key` value provided by the mobile client
to [register E2EE push device](/api/register-push-device).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mobile.<a href="src/fern/mobile/client.py">register_client_device</a>() -> RegisterClientDeviceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Logged-in mobile devices use this endpoint as an initial step to
register themselves, before registering for E2EE push notifications.

This endpoint is currently not useful for clients other than mobile.

**Changes**: New in Zulip 12.0 (feature level 468).
</dd>
</dl>
</dd>
</dl>

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

client.mobile.register_client_device()

```
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

<details><summary><code>client.mobile.<a href="src/fern/mobile/client.py">remove_client_device</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mobile devices use this endpoint to remove their device record
registered using [`POST /register_client_device`](/api/register-client-device)
when the user logs out.

This endpoint is currently not useful for clients other than mobile.

**Changes**: New in Zulip 12.0 (feature level 470).
</dd>
</dl>
</dd>
</dl>

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

client.mobile.remove_client_device(
    device_id=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `int` — The ID of the device to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ServerAndOrganizations
<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">upload_custom_emoji</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to upload a custom emoji for use in the user's
organization. Access to this endpoint depends on the
[organization's configuration](https://zulip.com/help/custom-emoji#change-who-can-add-custom-emoji).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.upload_custom_emoji(
    emoji_name="smile",
    filename="example_filename",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**emoji_name:** `str` 

The name that should be associated with the uploaded emoji image/gif.
The emoji name can only contain letters, numbers, dashes, and spaces.
Upper and lower case letters are treated the same, and underscores (\_)
are treated the same as spaces (consistent with how the Zulip UI
handles emoji).
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">deactivate_custom_emoji</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Deactivate a custom emoji](/help/custom-emoji#deactivate-custom-emoji) from
the user's organization.

Users can only deactivate custom emoji that they added themselves except for
organization administrators, who can deactivate any custom emoji.

Note that deactivated emoji will still be visible in old messages, reactions,
user statuses and channel descriptions.

**Changes**: Before Zulip 8.0 (feature level 190), this endpoint returned an
HTTP status code of 400 when the emoji did not exist, instead of 404.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.deactivate_custom_emoji(
    emoji_name="green_tick",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**emoji_name:** `str` — The name of the custom emoji to deactivate.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">get_custom_emoji</a>() -> GetCustomEmojiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the custom emoji in the user's organization.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.get_custom_emoji()

```
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

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">get_presence</a>() -> GetPresenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the presence information of all the users in an organization.

If the `CAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCE` server-level
setting is set to `true`, presence information of only accessible
users are returned.

Complete Zulip apps are recommended to fetch presence
information when they post their own state using the [`POST
/presence`](/api/update-presence) API endpoint.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.get_presence()

```
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

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">get_custom_profile_fields</a>() -> GetCustomProfileFieldsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the [custom profile fields](/help/custom-profile-fields)
configured for the user's organization.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.get_custom_profile_fields()

```
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

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">create_custom_profile_field</a>(...) -> CreateCustomProfileFieldResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[Create a custom profile field](/help/custom-profile-fields#add-a-custom-profile-field) in the user's organization.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.create_custom_profile_field(
    field_type=3,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_type:** `int` 

The field type can be any of the supported custom profile field types. See the
[custom profile fields documentation](/help/custom-profile-fields)
for more details on what each type means.

- **1**: Short text
- **2**: Paragraph
- **3**: Dropdown
- **4**: Date picker
- **5**: Link
- **6**: Person picker
- **7**: External account
- **8**: Pronouns

**Changes**: Field type `8` added in Zulip 6.0 (feature level 151).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

The name of the custom profile field, which will appear both in
user-facing settings UI for configuring custom profile fields and
in UI displaying a user's profile.
    
</dd>
</dl>

<dl>
<dd>

**hint:** `typing.Optional[str]` 

The help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.
    
</dd>
</dl>

<dl>
<dd>

**field_data:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Field types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in the `field_data` attribute.

For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.

The interface for field type 7 is not yet stabilized.
    
</dd>
</dl>

<dl>
<dd>

**display_in_profile_summary:** `typing.Optional[bool]` 

Whether clients should display this profile field in a summary section of a
user's profile (or in a more easily accessible "small profile").

At most 2 profile fields may have this property be true in a given
organization.

The "Person picker" profile field is not supported, but that is likely to
be temporary.

[profile-field-types]: /help/custom-profile-fields#profile-field-types

**Changes**: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.

New in Zulip 6.0 (feature level 146).
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[bool]` 

Whether an organization administrator has configured this profile field as
required.

Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.

**Changes**: New in Zulip 9.0 (feature level 244).
    
</dd>
</dl>

<dl>
<dd>

**editable_by_user:** `typing.Optional[bool]` 

Whether regular users can edit this profile field on their own account.

Note that organization administrators can edit custom profile fields for any user
regardless of this setting.

**Changes**: New in Zulip 10.0 (feature level 296).
    
</dd>
</dl>

<dl>
<dd>

**use_for_user_matching:** `typing.Optional[bool]` 

Whether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Account
[profile field types](/help/custom-profile-fields#profile-field-types).

This field is only included when its value is `true`.

**Changes**: New in Zulip 12.0 (feature level 455).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">reorder_custom_profile_fields</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reorder the custom profile fields in the user's organization.

Custom profile fields are displayed in Zulip UI widgets in order; this
endpoint allows administrative settings UI to change the field ordering.

This endpoint is used to implement the dragging feature described in the
[custom profile fields documentation](/help/custom-profile-fields).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.reorder_custom_profile_fields(
    order=[
        11,
        10,
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1
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

**order:** `typing.List[int]` 

A list of the IDs of all the custom profile fields defined in this
organization, in the desired new order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">update_realm_user_settings_defaults</a>(...) -> IgnoredParametersSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the [default values of settings][new-user-defaults] for new users
joining the organization. Essentially all
[personal preference settings](/api/update-settings) are supported.

This feature can be invaluable for customizing Zulip's default
settings for notifications or UI to be appropriate for how the
organization is using Zulip. (Note that this only supports
personal preference settings, like when to send push
notifications or what emoji set to use, not profile or
identity settings that naturally should be different for each user).

Note that this endpoint cannot, at present, be used to modify
settings for existing users in any way.

**Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
as we now have `web_font_size_px` and `web_line_height_percent`
settings for more control.

New in Zulip 5.0 (feature level 96). If any parameters sent in the
request are not supported by this endpoint, an
[`ignored_parameters_unsupported`][ignored-parameters] array will
be returned in the JSON success response.

[new-user-defaults]: /help/configure-default-new-user-settings
[ignored-parameters]: /api/rest-error-handling#ignored-parameters
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.update_realm_user_settings_defaults()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**starred_message_counts:** `typing.Optional[bool]` 

Whether clients should display the [number of starred
messages](/help/star-a-message#display-the-number-of-starred-messages).
    
</dd>
</dl>

<dl>
<dd>

**receives_typing_notifications:** `typing.Optional[bool]` 

Whether the user is configured to receive typing notifications from other users.
The server will only deliver typing notifications events to users who for whom this
is enabled.

**Changes**: New in Zulip 9.0 (feature level 253). Previously, there were
only options to disable sending typing notifications.
    
</dd>
</dl>

<dl>
<dd>

**web_suggest_update_timezone:** `typing.Optional[bool]` 

Whether the user should be shown an alert, offering to update their
[profile time zone](/help/change-your-timezone), when the time displayed
for the profile time zone differs from the current time displayed by the
time zone configured on their device.

**Changes**: New in Zulip 10.0 (feature level 329).
    
</dd>
</dl>

<dl>
<dd>

**fluid_layout_width:** `typing.Optional[bool]` 

Whether to use the [maximum available screen width](/help/enable-full-width-display)
for the web app's center panel (message feed, recent conversations) on wide screens.
    
</dd>
</dl>

<dl>
<dd>

**high_contrast_mode:** `typing.Optional[bool]` 

This setting is reserved for use to control variations in Zulip's design
to help visually impaired users.
    
</dd>
</dl>

<dl>
<dd>

**web_mark_read_on_scroll_policy:** `typing.Optional[int]` 

Whether or not to mark messages as read when the user scrolls through their
feed.

- 1 - Always
- 2 - Only in conversation views
- 3 - Never

**Changes**: New in Zulip 7.0 (feature level 175). Previously, there was no
way for the user to configure this behavior on the web, and the Zulip web and
desktop apps behaved like the "Always" setting when marking messages as read.
    
</dd>
</dl>

<dl>
<dd>

**web_channel_default_view:** `typing.Optional[int]` 

Web/desktop app setting controlling the default navigation
behavior when clicking on a channel link.

- 1 - Top topic in the channel
- 2 - Channel feed
- 3 - List of topics
- 4 - Top unread topic in channel

**Changes**: The "Top unread topic in channel" is new in Zulip 11.0
(feature level 401).

The "List of topics" option is new in Zulip 11.0 (feature level 383).

New in Zulip 9.0 (feature level 269). Previously, this
was not configurable, and every user had the "Channel feed" behavior.
    
</dd>
</dl>

<dl>
<dd>

**web_font_size_px:** `typing.Optional[int]` 

User-configured primary `font-size` for the web application, in pixels.

**Changes**: New in Zulip 9.0 (feature level 245). Previously, font size was
only adjustable via browser zoom. Note that this setting was not fully
implemented at this feature level.
    
</dd>
</dl>

<dl>
<dd>

**web_line_height_percent:** `typing.Optional[int]` 

User-configured primary `line-height` for the web application, in percent, so a
value of 120 represents a `line-height` of 1.2.

**Changes**: New in Zulip 9.0 (feature level 245). Previously, line height was
not user-configurable. Note that this setting was not fully implemented at this
feature level.
    
</dd>
</dl>

<dl>
<dd>

**color_scheme:** `typing.Optional[int]` 

Controls which [color theme](/help/dark-theme) to use.

- 1 - Automatic
- 2 - Dark theme
- 3 - Light theme

Automatic detection is implementing using the standard `prefers-color-scheme`
media query.
    
</dd>
</dl>

<dl>
<dd>

**enable_drafts_synchronization:** `typing.Optional[bool]` 

A boolean parameter to control whether synchronizing drafts is enabled for
the user. When synchronization is disabled, all drafts stored in the server
will be automatically deleted from the server.

This does not do anything (like sending events) to delete local copies of
drafts stored in clients.
    
</dd>
</dl>

<dl>
<dd>

**translate_emoticons:** `typing.Optional[bool]` 

Whether to [translate emoticons to emoji](/help/configure-emoticon-translations)
in messages the user sends.
    
</dd>
</dl>

<dl>
<dd>

**display_emoji_reaction_users:** `typing.Optional[bool]` 

Whether to display the names of reacting users on a message.

When enabled, clients should display the names of reacting users, rather than
a count, for messages with few total reactions. The ideal cutoff may depend on
the space available for displaying reactions; the official web application
displays names when 3 or fewer total reactions are present with this setting
enabled.

**Changes**: New in Zulip 6.0 (feature level 125).
    
</dd>
</dl>

<dl>
<dd>

**web_home_view:** `typing.Optional[str]` 

The [home view](/help/configure-home-view) used when opening a new
Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.

- "recent" - Recent conversations view
- "inbox" - Inbox view
- "all_messages" - Combined feed view

**Changes**: Before Zulip 12.0 (feature level 454), the Recent
view had `"recent_topics"` as its string encoding.

New in Zulip 8.0 (feature level 219). Previously, this was
called `default_view`, which was new in Zulip 4.0 (feature level 42).
    
</dd>
</dl>

<dl>
<dd>

**web_escape_navigates_to_home_view:** `typing.Optional[bool]` 

Whether the escape key navigates to the
[configured home view](/help/configure-home-view).

**Changes**: New in Zulip 8.0 (feature level 219). Previously, this was called
`escape_navigates_to_default_view`, which was new in Zulip 5.0 (feature level 107).
    
</dd>
</dl>

<dl>
<dd>

**left_side_userlist:** `typing.Optional[bool]` 

Whether the users list on left sidebar in narrow windows.

This feature is not heavily used and is likely to be reworked.
    
</dd>
</dl>

<dl>
<dd>

**emojiset:** `typing.Optional[str]` 

The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons),
used to display emoji to the user everywhere they appear in the UI.

- "google" - Google
- "twitter" - Twitter
- "text" - Plain text
    
</dd>
</dl>

<dl>
<dd>

**demote_inactive_streams:** `typing.Optional[int]` 

Whether to [hide inactive channels](/help/manage-inactive-channels) in the left sidebar.

- 1 - Automatic
- 2 - Always
- 3 - Never
    
</dd>
</dl>

<dl>
<dd>

**user_list_style:** `typing.Optional[int]` 

The style selected by the user for the right sidebar user list.

- 1 - Compact
- 2 - With status
- 3 - With avatar and status

**Changes**: New in Zulip 6.0 (feature level 141).
    
</dd>
</dl>

<dl>
<dd>

**web_animate_image_previews:** `typing.Optional[UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews]` 

Controls how animated images should be played in the message feed in the web/desktop application.

- "always" - Always play the animated images in the message feed.
- "on_hover" - Play the animated images on hover over them in the message feed.
- "never" - Never play animated images in the message feed.

**Changes**: New in Zulip 9.0 (feature level 275). Previously, animated images
always used to play in the message feed by default. This setting controls this
behaviour.
    
</dd>
</dl>

<dl>
<dd>

**web_stream_unreads_count_display_policy:** `typing.Optional[int]` 

Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
Channels that do not have an unread count will have a simple dot indicator for whether there are any
unread messages.

- 1 - All channels
- 2 - Unmuted channels and topics
- 3 - No channels

**Changes**: New in Zulip 8.0 (feature level 210).
    
</dd>
</dl>

<dl>
<dd>

**hide_ai_features:** `typing.Optional[bool]` 

Controls whether user wants AI features like topic summarization to
be hidden in all Zulip clients.

**Changes**: New in Zulip 10.0 (feature level 350).
    
</dd>
</dl>

<dl>
<dd>

**web_inbox_show_channel_folders:** `typing.Optional[bool]` 

Determines whether [channel folders](/help/channel-folders)
are used to organize how conversations with unread messages
are displayed in the web/desktop application's Inbox view.

**Changes**: New in Zulip 12.0 (feature level 431).
    
</dd>
</dl>

<dl>
<dd>

**web_left_sidebar_show_channel_folders:** `typing.Optional[bool]` 

Determines whether [channel folders](/help/channel-folders)
are used to organize how channels are displayed in the
web/desktop application's left sidebar.

**Changes**: New in Zulip 11.0 (feature level 411).
    
</dd>
</dl>

<dl>
<dd>

**web_left_sidebar_unreads_count_summary:** `typing.Optional[bool]` 

Determines whether the web/desktop application's left sidebar displays
the unread message count summary.

**Changes**: New in Zulip 11.0 (feature level 398).
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_desktop_notifications:** `typing.Optional[bool]` — Enable visual desktop notifications for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_email_notifications:** `typing.Optional[bool]` — Enable email notifications for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_push_notifications:** `typing.Optional[bool]` — Enable mobile notifications for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**enable_stream_audible_notifications:** `typing.Optional[bool]` — Enable audible desktop notifications for channel messages.
    
</dd>
</dl>

<dl>
<dd>

**notification_sound:** `typing.Optional[str]` — Notification sound name.
    
</dd>
</dl>

<dl>
<dd>

**enable_desktop_notifications:** `typing.Optional[bool]` — Enable visual desktop notifications for direct messages and @-mentions.
    
</dd>
</dl>

<dl>
<dd>

**enable_sounds:** `typing.Optional[bool]` 

Enable audible desktop notifications for direct messages and
@-mentions.
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_desktop_notifications:** `typing.Optional[bool]` 

Enable visual desktop notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_email_notifications:** `typing.Optional[bool]` 

Enable email notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_push_notifications:** `typing.Optional[bool]` 

Enable push notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_audible_notifications:** `typing.Optional[bool]` 

Enable audible desktop notifications for messages sent to followed topics.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**email_notifications_batching_period_seconds:** `typing.Optional[int]` 

The duration (in seconds) for which the server should wait to batch
email notifications before sending them.
    
</dd>
</dl>

<dl>
<dd>

**enable_offline_email_notifications:** `typing.Optional[bool]` 

Enable email notifications for direct messages and @-mentions received
when the user is offline.
    
</dd>
</dl>

<dl>
<dd>

**enable_offline_push_notifications:** `typing.Optional[bool]` 

Enable mobile notification for direct messages and @-mentions received
when the user is offline.
    
</dd>
</dl>

<dl>
<dd>

**enable_online_push_notifications:** `typing.Optional[bool]` 

Enable mobile notification for direct messages and @-mentions received
when the user is online.
    
</dd>
</dl>

<dl>
<dd>

**enable_digest_emails:** `typing.Optional[bool]` — Enable digest emails when the user is away.
    
</dd>
</dl>

<dl>
<dd>

**message_content_in_email_notifications:** `typing.Optional[bool]` — Include the message's content in email notifications for new messages.
    
</dd>
</dl>

<dl>
<dd>

**pm_content_in_desktop_notifications:** `typing.Optional[bool]` — Include content of direct messages in desktop notifications.
    
</dd>
</dl>

<dl>
<dd>

**wildcard_mentions_notify:** `typing.Optional[bool]` 

Whether wildcard mentions (E.g. @**all**) should send notifications
like a personal mention.
    
</dd>
</dl>

<dl>
<dd>

**enable_followed_topic_wildcard_mentions_notify:** `typing.Optional[bool]` 

Whether wildcard mentions (e.g., @**all**) in messages sent to followed topics
should send notifications like a personal mention.

**Changes**: New in Zulip 8.0 (feature level 189).
    
</dd>
</dl>

<dl>
<dd>

**desktop_icon_count_display:** `typing.Optional[int]` 

Unread count badge (appears in desktop sidebar and browser tab)

- 1 - All unread messages
- 2 - DMs, mentions, and followed topics
- 3 - DMs and mentions
- 4 - None

**Changes**: In Zulip 8.0 (feature level 227), added `DMs, mentions, and followed
topics` option, renumbering the options to insert it in order.
    
</dd>
</dl>

<dl>
<dd>

**realm_name_in_email_notifications_policy:** `typing.Optional[int]` 

Whether to [include organization name in subject of message notification
emails](/help/email-notifications#include-organization-name-in-subject-line).

- 1 - Automatic
- 2 - Always
- 3 - Never

**Changes**: New in Zulip 7.0 (feature level 168), replacing the
previous `realm_name_in_notifications` boolean;
`true` corresponded to `Always`, and `false` to `Never`.
    
</dd>
</dl>

<dl>
<dd>

**automatically_follow_topics_policy:** `typing.Optional[int]` 

Which [topics to follow automatically](/help/mute-a-topic).

- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never

**Changes**: New in Zulip 8.0 (feature level 214).
    
</dd>
</dl>

<dl>
<dd>

**automatically_unmute_topics_in_muted_streams_policy:** `typing.Optional[int]` 

Which [topics to unmute automatically in muted channels](/help/mute-a-topic).

- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never

**Changes**: New in Zulip 8.0 (feature level 214).
    
</dd>
</dl>

<dl>
<dd>

**automatically_follow_topics_where_mentioned:** `typing.Optional[bool]` 

Whether the server will automatically mark the user as following
topics where the user is mentioned.

**Changes**: New in Zulip 8.0 (feature level 235).
    
</dd>
</dl>

<dl>
<dd>

**resolved_topic_notice_auto_read_policy:** `typing.Optional[UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy]` 

Controls whether the resolved-topic notices are marked as read.

- "always" - Always mark resolved-topic notices as read.
- "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
- "never" - Never mark resolved-topic notices as read.

**Changes**: New in Zulip 11.0 (feature level 385).
    
</dd>
</dl>

<dl>
<dd>

**presence_enabled:** `typing.Optional[bool]` — Display the presence status to other users when online.
    
</dd>
</dl>

<dl>
<dd>

**enter_sends:** `typing.Optional[bool]` 

Whether pressing Enter in the compose box sends a message
(or saves a message edit).
    
</dd>
</dl>

<dl>
<dd>

**twenty_four_hour_time:** `typing.Optional[bool]` 

Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).

**Changes**: New in Zulip 5.0 (feature level 99).
Previously, this default was edited using the
`default_twenty_four_hour_time` parameter to the `PATCH /realm` endpoint.
    
</dd>
</dl>

<dl>
<dd>

**send_private_typing_notifications:** `typing.Optional[bool]` 

Whether [typing notifications](/help/typing-notifications) be sent when composing
direct messages.

**Changes**: New in Zulip 5.0 (feature level 105).
    
</dd>
</dl>

<dl>
<dd>

**send_stream_typing_notifications:** `typing.Optional[bool]` 

Whether [typing notifications](/help/typing-notifications) be sent when composing
channel messages.

**Changes**: New in Zulip 5.0 (feature level 105).
    
</dd>
</dl>

<dl>
<dd>

**send_read_receipts:** `typing.Optional[bool]` 

Whether other users are allowed to see whether you've
read messages.

**Changes**: New in Zulip 5.0 (feature level 105).
    
</dd>
</dl>

<dl>
<dd>

**email_address_visibility:** `typing.Optional[int]` 

The [policy][permission-level] for [which other users][help-email-visibility]
in this organization can see the user's real email address.

- 1 = Everyone
- 2 = Members only
- 3 = Administrators only
- 4 = Nobody
- 5 = Moderators only

**Changes**: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.

[permission-level]: /api/roles-and-permissions#permission-levels
[help-email-visibility]: /help/configure-email-visibility
    
</dd>
</dl>

<dl>
<dd>

**web_navigate_to_sent_message:** `typing.Optional[bool]` 

Web/desktop app setting for whether the user's view should
automatically go to the conversation where they sent a message.

**Changes**: New in Zulip 9.0 (feature level 268). Previously,
this behavior was not configurable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">get_linkifiers</a>() -> GetLinkifiersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all of an organization's configured
[linkifiers](/help/add-a-custom-linkifier), regular
expression patterns that are automatically linkified when they appear
in messages and topics.

**Changes**: New in Zulip 4.0 (feature level 54). On older versions,
a similar `GET /realm/filters` endpoint was available with each entry in
a `[pattern, url_format, id]` tuple format.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.get_linkifiers()

```
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

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">reorder_linkifiers</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the order that the regular expression patterns in the organization's
[linkifiers](/help/add-a-custom-linkifier) are matched in messages and topics.
Useful when defining linkifiers with overlapping patterns.

**Changes**: New in Zulip 8.0 (feature level 202). Before this feature level,
linkifiers were always processed in order by ID, which meant users would
need to delete and recreate them to reorder the list of linkifiers.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.reorder_linkifiers(
    ordered_linkifier_ids=[
        3,
        2,
        1,
        5
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

**ordered_linkifier_ids:** `typing.List[int]` 

A list of the IDs of all the linkifiers defined in this
organization, in the desired new order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">add_linkifier</a>(...) -> AddLinkifierResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure [linkifiers](/help/add-a-custom-linkifier),
regular expression patterns that are automatically linkified when they
appear in messages and topics.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.add_linkifier(
    pattern="#(?P<id>[0-9]+)",
    url_template="https://github.com/zulip/zulip/issues/{id}",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pattern:** `LinkifierPattern` 
    
</dd>
</dl>

<dl>
<dd>

**url_template:** `LinkifierUrlTemplate` 
    
</dd>
</dl>

<dl>
<dd>

**example_input:** `typing.Optional[str]` 

An example input string that matches the linkifier's pattern.
This is required for reverse linkifiers.

**Changes**: New in Zulip 12.0 (feature level 471).
    
</dd>
</dl>

<dl>
<dd>

**reverse_template:** `typing.Optional[str]` 

A simple template using `{variable}` for variables that can
be used to generate the Markdown linkifier syntax, given a
URL matching the URL template.

`{{ "{{/}}" }}` can be used for literal `{/}` characters.

Server verifies that variables extracted from example_input using
url_pattern when passed to reverse_template returns example_input
back to us.

**Changes**: New in Zulip 12.0 (feature level 471).
    
</dd>
</dl>

<dl>
<dd>

**alternative_url_templates:** `typing.Optional[typing.List[str]]` 

An array of additional [RFC 6570][rfc6570] compliant URL
template strings that are used for reverse linkification
(converting pasted URLs to linkifier pattern text). These
templates have no effect on forward linkification.

[rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html

**Changes**: New in Zulip 12.0 (feature level e2b257).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">remove_linkifier</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove [linkifiers](/help/add-a-custom-linkifier), regular
expression patterns that are automatically linkified when they appear
in messages and topics.
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.remove_linkifier(
    filter_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_id:** `int` — The ID of the linkifier that you want to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">update_linkifier</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a [linkifier](/help/add-a-custom-linkifier), regular
expression patterns that are automatically linkified when they appear
in messages and topics.

**Changes**: New in Zulip 4.0 (feature level 57).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.update_linkifier(
    filter_id=1,
    pattern="#(?P<id>[0-9]+)",
    url_template="https://github.com/zulip/zulip/issues/{id}",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_id:** `int` — The ID of the linkifier that you want to update.
    
</dd>
</dl>

<dl>
<dd>

**pattern:** `LinkifierPattern` 
    
</dd>
</dl>

<dl>
<dd>

**url_template:** `LinkifierUrlTemplate` 
    
</dd>
</dl>

<dl>
<dd>

**example_input:** `typing.Optional[str]` 

An example input string that matches the linkifier's pattern.
This is required for reverse linkifiers. Passing an empty string
will set this field back to null.

**Changes**: New in Zulip 12.0 (feature level 471).
    
</dd>
</dl>

<dl>
<dd>

**reverse_template:** `typing.Optional[str]` 

A simple template using `{variable}` for variables that can
be used to generate the Markdown linkifier syntax, given a
URL matching the URL template. Passing an empty string
will set this field back to null.

Server verifies that variables extracted from example_input using
url_pattern when passed to reverse_template returns example_input
back to us.

`{{ "{{/}}" }}` can be used for literal `{/}` characters.

**Changes**: New in Zulip 12.0 (feature level 471).
    
</dd>
</dl>

<dl>
<dd>

**alternative_url_templates:** `typing.Optional[typing.List[str]]` 

An array of additional [RFC 6570][rfc6570] compliant URL
template strings that are used for reverse linkification
(converting pasted URLs to linkifier pattern text). These
templates have no effect on forward linkification.

[rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html

**Changes**: New in Zulip 12.0 (feature level e2b257).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">add_code_playground</a>(...) -> AddCodePlaygroundResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure [code playgrounds](/help/code-blocks#code-playgrounds) for the organization.

**Changes**: New in Zulip 4.0 (feature level 49). A parameter encoding bug was
fixed in Zulip 4.0 (feature level 57).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.add_code_playground(
    name="Python playground",
    pygments_language="Python",
    url_template="https://python.example.com?code={code}",
)

```
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

The user-visible display name of the playground which can be
used to pick the target playground, especially when multiple
playground options exist for that programming language.
    
</dd>
</dl>

<dl>
<dd>

**pygments_language:** `str` 

The name of the Pygments language lexer for that
programming language.
    
</dd>
</dl>

<dl>
<dd>

**url_template:** `str` 

The [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html)
compliant URL template for the playground. The template should
contain exactly one variable named `code`, which determines how the
extracted code should be substituted in the playground URL.

**Changes**: New in Zulip 8.0 (feature level 196). This replaced the
`url_prefix` parameter, which was used to construct URLs by just
concatenating `url_prefix` and `code`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">remove_code_playground</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a [code playground](/help/code-blocks#code-playgrounds) previously
configured for an organization.

**Changes**: New in Zulip 4.0 (feature level 49).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.remove_code_playground(
    playground_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**playground_id:** `int` — The ID of the playground that you want to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">get_realm_exports</a>() -> GetRealmExportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all the public and standard [data exports][export-data]
of the organization.

**Changes**: Prior to Zulip 10.0 (feature level 304), only
public data exports could be fetched using this endpoint.

New in Zulip 2.1.

[export-data]: /help/export-your-organization#export-data-in-an-importable-format
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.get_realm_exports()

```
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

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">export_realm</a>(...) -> ExportRealmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a public or a standard [data export][export-data] of the organization.

!!! warn ""

    **Note**: If you're the administrator of a self-hosted installation,
    you may be looking for the documentation on [server data export and
    import][data-export] or [server backups][backups].

**Changes**: Prior to Zulip 10.0 (feature level 304), only
public data exports could be created using this endpoint.

New in Zulip 2.1.

[export-data]: /help/export-your-organization#export-data-in-an-importable-format
[data-export]: https://zulip.readthedocs.io/en/stable/production/export-and-import.html#data-export
[backups]: https://zulip.readthedocs.io/en/stable/production/export-and-import.html#backups
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.export_realm()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**export_type:** `typing.Optional[ExportRealmRequestExportType]` 

Whether the data export should be public, full with consent,
or full without consent.

- `public` = Public data only export.
- `full_with_consent` = Public and private data export (with consent), which includes
  private data for users who have granted consent.
- `full_without_consent` = All public and private data export, which includes private data for
  all users. This option requires the organization to have
  the `owner_full_content_access` feature enabled.

If not specified, defaults to `public`.

**Changes**: Zulip 12.0 (feature level 449) changed the type of
this field from int to string with `1` being replaced by `public` and
`2` being replaced by `full_with_consent`. The option `full_without_consent`
was added for full exports without member consent.

**Changes**: New in Zulip 10.0 (feature level 304). Previously,
all export requests were public data exports.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">get_realm_export_consents</a>() -> GetRealmExportConsentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches which users have [consented](/help/export-your-organization#configure-whether-administrators-can-export-your-private-data)
for their private data to be exported by organization administrators.

**Changes**: Changes in Zulip 12.0 (feature level 430). Added an
integer field `email_address_visibility` to the objects in the
`export_consents` array.

New in Zulip 10.0 (feature level 295).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.get_realm_export_consents()

```
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

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">test_welcome_bot_custom_message</a>(...) -> TestWelcomeBotCustomMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends a test Welcome Bot custom message to the acting administrator.
This allows administrators to preview how the custom welcome message will
appear when received by new users upon joining the organization.

**Changes**: New in Zulip 11.0 (feature level 416).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.test_welcome_bot_custom_message(
    welcome_message_custom_text="Welcome to Zulip! We\'re excited to have you on board.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**welcome_message_custom_text:** `str` 

Custom message text, in Zulip Markdown format, to be used for
this test message.

Maximum length is 8000 Unicode code points.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server_and_organizations.<a href="src/fern/server_and_organizations/client.py">get_server_settings</a>() -> GetServerSettingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch global settings for a Zulip server.

**Note:** this endpoint does not require any authentication at all, and you can use it to check:

- If this is a Zulip server, and if so, what version of Zulip it's running.
- What a Zulip client (e.g. a mobile app or
  [zulip-terminal](https://github.com/zulip/zulip-terminal/)) needs to
  know in order to display a login prompt for the server (e.g. what
  authentication methods are available).
</dd>
</dl>
</dd>
</dl>

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

client.server_and_organizations.get_server_settings()

```
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

## Invites
<details><summary><code>client.invites.<a href="src/fern/invites/client.py">get_invites</a>() -> GetInvitesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all unexpired [invitations](/help/invite-new-users) (i.e. email
invitations and reusable invitation links) that can be managed by the user.

Note that administrators can manage invitations that were created by other users.

**Changes**: Prior to Zulip 8.0 (feature level 209), non-admin users could
only create email invitations, and therefore the response would never include
reusable invitation links for these users.
</dd>
</dl>
</dd>
</dl>

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

client.invites.get_invites()

```
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

<details><summary><code>client.invites.<a href="src/fern/invites/client.py">send_invites</a>(...) -> SendInvitesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send [invitations](/help/invite-new-users) to specified email addresses.

**Changes**: In Zulip 6.0 (feature level 126), the `invite_expires_in_days`
parameter was removed and replaced by `invite_expires_in_minutes`.

In Zulip 5.0 (feature level 117), added support for passing `null` as
the `invite_expires_in_days` parameter to request an invitation that never
expires.

In Zulip 5.0 (feature level 96), the `invite_expires_in_days` parameter was
added which specified the number of days before the invitation would expire.
</dd>
</dl>
</dd>
</dl>

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

client.invites.send_invites(
    invitee_emails="example@zulip.com, logan@zulip.com",
    stream_ids=[
        1,
        10
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

**invitee_emails:** `str` 

The string containing the email addresses, separated by commas or
newlines, that will be sent an invitation.
    
</dd>
</dl>

<dl>
<dd>

**stream_ids:** `typing.List[int]` 

A list containing the [IDs of the channels](/api/get-stream-id) that the
newly created user will be automatically subscribed to if the invitation
is accepted, in addition to any default channels that the new user may
be subscribed to based on the `include_realm_default_subscriptions`
parameter.

Requested channels must either be default channels for the
organization, or ones the acting user has permission to add
subscribers to.

This list must be empty if the current user has the unlikely
configuration of being able to send invitations while lacking
permission to [subscribe other users to channels][can-subscribe-others].

**Changes**: Prior to Zulip 10.0 (feature level 342), default channels
that the acting user did not directly have permission to add
subscribers to would be rejected.

Before Zulip 7.0 (feature level 180), specifying `stream_ids` as an
empty list resulted in an error.

[can-subscribe-others]: /help/configure-who-can-invite-to-channels
    
</dd>
</dl>

<dl>
<dd>

**invite_expires_in_minutes:** `typing.Optional[InviteExpirationParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**invite_as:** `typing.Optional[InviteRoleParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**group_ids:** `typing.Optional[typing.List[int]]` 

A list containing the [IDs of the user groups](/api/get-user-groups) that
the newly created user will be automatically added to if the invitation
is accepted. If the list is empty, then the new user will not be
added to any user groups. The acting user must have permission to add users
to the groups listed in this request.

**Changes**: New in Zulip 10.0 (feature level 322).
    
</dd>
</dl>

<dl>
<dd>

**include_realm_default_subscriptions:** `typing.Optional[bool]` 

Boolean indicating whether the newly created user should be subscribed
to the [default channels][default-channels] for the organization.

Note that this parameter can be `true` even if the user creating the
invitation does not generally have permission to [subscribe other
users to channels][can-subscribe-others].

**Changes**: New in Zulip 9.0 (feature level 261). Previous versions
of Zulip behaved as though this parameter was always `false`; clients
needed to include the organization's default channels in the
`stream_ids` parameter for a newly created user to be automatically
subscribed to them.

[default-channels]: /help/set-default-channels-for-new-users
[can-subscribe-others]: /help/configure-who-can-invite-to-channels
    
</dd>
</dl>

<dl>
<dd>

**notify_referrer_on_join:** `typing.Optional[bool]` 

A boolean indicating whether the referrer would like to receive a
direct message from [notification
bot](/help/configure-automated-notices) when a user account is created
using this invitation.

**Changes**: New in Zulip 9.0 (feature level 267). Previously,
referrers always received such direct messages.
    
</dd>
</dl>

<dl>
<dd>

**welcome_message_custom_text:** `typing.Optional[str]` 

Custom message text, in Zulip Markdown format, to be sent by the
Welcome Bot to new users that join the organization via this
invitation.

Maximum length is 8000 Unicode code points.

Only organization administrators can use this feature; for other
users, the value is always `null`.

- `null`: the organization's default `welcome_message_custom_text` is used.
- Empty string: no Welcome Bot custom message is sent.
- Otherwise, the provided string is the custom message.

**Changes**: New in Zulip 11.0 (feature level 416).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invites.<a href="src/fern/invites/client.py">create_invite_link</a>(...) -> CreateInviteLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a [reusable invitation link](/help/invite-new-users#create-a-reusable-invitation-link)
which can be used to invite new users to the organization.

**Changes**: In Zulip 8.0 (feature level 209), added support for non-admin
users [with permission](/help/restrict-account-creation#change-who-can-send-invitations)
to use this endpoint. Previously, it was restricted to administrators only.

In Zulip 6.0 (feature level 126), the `invite_expires_in_days`
parameter was removed and replaced by `invite_expires_in_minutes`.

In Zulip 5.0 (feature level 117), added support for passing `null` as
the `invite_expires_in_days` parameter to request an invitation that never
expires.

In Zulip 5.0 (feature level 96), the `invite_expires_in_days` parameter was
added which specified the number of days before the invitation would expire.
</dd>
</dl>
</dd>
</dl>

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

client.invites.create_invite_link()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invite_expires_in_minutes:** `typing.Optional[InviteExpirationParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**invite_as:** `typing.Optional[InviteRoleParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**stream_ids:** `typing.Optional[typing.List[int]]` 

A list containing the [IDs of the channels](/api/get-stream-id) that the
newly created user will be automatically subscribed to if the invitation
is accepted, in addition to any default channels that the new user may
be subscribed to based on the `include_realm_default_subscriptions`
parameter.

Requested channels must either be default channels for the
organization, or ones the acting user has permission to add
subscribers to.

This list must be empty if the current user has the unlikely
configuration of being able to create reusable invitation links while
lacking permission to [subscribe other users to
channels][can-subscribe-others].

**Changes**: Prior to Zulip 10.0 (feature level 342), default channels
that the acting user did not directly have permission to add
subscribers to would be rejected.

[can-subscribe-others]: /help/configure-who-can-invite-to-channels
    
</dd>
</dl>

<dl>
<dd>

**group_ids:** `typing.Optional[typing.List[int]]` 

A list containing the [IDs of the user groups](/api/get-user-groups) that
the newly created user will be automatically added to if the invitation
is accepted. If the list is empty, then the new user will not be
added to any user groups. The acting user must have permission to add users
to the groups listed in this request.

**Changes**: New in Zulip 10.0 (feature level 322).
    
</dd>
</dl>

<dl>
<dd>

**include_realm_default_subscriptions:** `typing.Optional[bool]` 

Boolean indicating whether the newly created user should be subscribed
to the [default channels][default-channels] for the organization.

Note that this parameter can be `true` even if the current user does
not generally have permission to [subscribe other users to
channels][can-subscribe-others].

**Changes**: New in Zulip 9.0 (feature level 261). Previous versions
of Zulip behaved as though this parameter was always `false`; clients
needed to include the organization's default channels in the
`stream_ids` parameter for a newly created user to be automatically
subscribed to them.

[default-channels]: /help/set-default-channels-for-new-users
[can-subscribe-others]: /help/configure-who-can-invite-to-channels
    
</dd>
</dl>

<dl>
<dd>

**welcome_message_custom_text:** `typing.Optional[str]` 

Custom message text, in Zulip Markdown format, to be sent by the
Welcome Bot to new users that join the organization via this
invitation.

Maximum length is 8000 Unicode code points.

Only organization administrators can use this feature; for other
users, the value is always `null`.

- `null`: the organization's default `welcome_message_custom_text` is used.
- Empty string: no Welcome Bot custom message is sent.
- Otherwise, the provided string is the custom message.

**Changes**: New in Zulip 11.0 (feature level 416).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invites.<a href="src/fern/invites/client.py">revoke_email_invite</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an [email invitation](/help/invite-new-users#send-email-invitations).

A user can only revoke [invitations that they can
manage](/help/invite-new-users#manage-pending-invitations).
</dd>
</dl>
</dd>
</dl>

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

client.invites.revoke_email_invite(
    invite_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invite_id:** `int` — The ID of the email invitation to be revoked.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invites.<a href="src/fern/invites/client.py">revoke_invite_link</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a [reusable invitation link](/help/invite-new-users#create-a-reusable-invitation-link).

A user can only revoke [invitations that they can
manage](/help/invite-new-users#manage-pending-invitations).

**Changes**: Prior to Zulip 8.0 (feature level 209), only organization
administrators were able to create and revoke reusable invitation links.
</dd>
</dl>
</dd>
</dl>

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

client.invites.revoke_invite_link(
    invite_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invite_id:** `int` — The ID of the reusable invitation link to be revoked.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invites.<a href="src/fern/invites/client.py">resend_email_invite</a>(...) -> JsonSuccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resend an [email invitation](/help/invite-new-users#send-email-invitations).

A user can only resend [invitations that they can
manage](/help/invite-new-users#manage-pending-invitations).
</dd>
</dl>
</dd>
</dl>

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

client.invites.resend_email_invite(
    invite_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invite_id:** `int` — The ID of the email invitation to be resent.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">zulip_outgoing_webhooks</a>() -> ZulipOutgoingWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Outgoing webhooks allow you to build or set up Zulip integrations which are
notified when certain types of messages are sent in Zulip.
</dd>
</dl>
</dd>
</dl>

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

client.webhooks.zulip_outgoing_webhooks()

```
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

