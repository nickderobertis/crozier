# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">delete_account</a>(...) -> DeleteAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint used to delete an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.accounts import DeleteAccountRequestIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounts.delete_account(
    identification=DeleteAccountRequestIdentification(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identification:** `DeleteAccountRequestIdentification` — Account identification requires an accountId, domain or both
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">upsert_account</a>(...) -> UpsertAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint used to create or update an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.accounts import UpsertAccountRequestIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounts.upsert_account(
    identification=UpsertAccountRequestIdentification(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identification:** `UpsertAccountRequestIdentification` — Account identification requires an accountId, domain or both
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]]` — The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">add_user_to_account</a>(...) -> AddUserToAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add up to 100 users to an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.accounts import AddUserToAccountRequestAccount, AddUserToAccountRequestUsersItem, AddUserToAccountRequestUsersItemIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounts.add_user_to_account(
    account=AddUserToAccountRequestAccount(),
    users=[
        AddUserToAccountRequestUsersItem(
            identification=AddUserToAccountRequestUsersItemIdentification(),
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

**account:** `AddUserToAccountRequestAccount` — Account identification requires an accountId, domain or both
    
</dd>
</dl>

<dl>
<dd>

**users:** `typing.List[AddUserToAccountRequestUsersItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">remove_user_from_account</a>(...) -> RemoveUserFromAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove up to 100 users from an account.

When removing a user, the user will still be stored in journy.io, but marked as "removed".
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.accounts import RemoveUserFromAccountRequestAccount, RemoveUserFromAccountRequestUsersItem, RemoveUserFromAccountRequestUsersItemIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounts.remove_user_from_account(
    account=RemoveUserFromAccountRequestAccount(),
    users=[
        RemoveUserFromAccountRequestUsersItem(
            identification=RemoveUserFromAccountRequestUsersItemIdentification(),
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

**account:** `RemoveUserFromAccountRequestAccount` — Account identification requires an accountId, domain or both
    
</dd>
</dl>

<dl>
<dd>

**users:** `typing.List[RemoveUserFromAccountRequestUsersItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/fern/events/client.py">get_events</a>() -> GetEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to list events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.events.get_events()

```
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

<details><summary><code>client.events.<a href="src/fern/events/client.py">track_journey_event</a>(...) -> TrackJourneyEventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint used to track an event for a user or an account.

This endpoint is moved to [Track](#operation/trackEvent).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.events import TrackJourneyEventRequestIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.events.track_journey_event(
    identification=TrackJourneyEventRequestIdentification(),
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

**identification:** `TrackJourneyEventRequestIdentification` — Event identification requires a user, account or both
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, TrackJourneyEventRequestMetadataValue]]` — Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**triggered_at:** `typing.Optional[str]` — If left blank this defaults to the current datetime
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">link</a>(...) -> LinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

💡 You don't need to use this endpoint if you use our JavaScript snippet in your application.

This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.

When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named "__journey" will be set.

This will only work if your website and application are under the same top level domain.

Website, blog or landing pages
* www.my-domain.tld
* blog.my-domain.tld
* landing-page.my-domain.tld

Application
* app.my-domain.tld

The cookie on my-domain.tld will also be send to your app domain.

You should call this endpoint after the user succesfully logged in (so that you know the user's ID). Use the value of the cookie as device ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.users import LinkRequestIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.users.link(
    device_id="deviceId",
    identification=LinkRequestIdentification(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identification:** `LinkRequestIdentification` — User identification requires a userId, email or both
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete_user</a>(...) -> DeleteUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to delete a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.users import DeleteUserRequestIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.users.delete_user(
    identification=DeleteUserRequestIdentification(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identification:** `DeleteUserRequestIdentification` — User identification requires a userId, email or both
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">upsert_user</a>(...) -> UpsertUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to create or update a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.users import UpsertUserRequestIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.users.upsert_user(
    identification=UpsertUserRequestIdentification(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identification:** `UpsertUserRequestIdentification` — User identification requires a userId, email or both
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]]` — The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Properties
<details><summary><code>client.properties.<a href="src/fern/properties/client.py">get_account_properties</a>() -> GetAccountPropertiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to list account properties.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.properties.get_account_properties()

```
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

<details><summary><code>client.properties.<a href="src/fern/properties/client.py">get_user_properties</a>() -> GetUserPropertiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to list user properties.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.properties.get_user_properties()

```
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

## Segments
<details><summary><code>client.segments.<a href="src/fern/segments/client.py">get_account_segments</a>() -> GetAccountSegmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to list account segments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.segments.get_account_segments()

```
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

<details><summary><code>client.segments.<a href="src/fern/segments/client.py">get_user_segments</a>() -> GetUserSegmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to list user segments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.segments.get_user_segments()

```
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

## Track
<details><summary><code>client.track.<a href="src/fern/track/client.py">event</a>(...) -> TrackEventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint used to track an event for a user or an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.track import TrackEventRequestIdentification

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.track.event(
    identification=TrackEventRequestIdentification(),
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

**identification:** `TrackEventRequestIdentification` — Event identification requires a user, account or both
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, TrackEventRequestMetadataValue]]` — Event metadata, possible values are strings, booleans, numbers and datetimes (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**triggered_at:** `typing.Optional[str]` — If left blank this defaults to the current datetime
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Websites
<details><summary><code>client.websites.<a href="src/fern/websites/client.py">get_tracking_snippet</a>(...) -> GetTrackingSnippetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint used to get a snippet for a website.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.websites.get_tracking_snippet(
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — The domain you want to receive a snippet for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Validation
<details><summary><code>client.validation.<a href="src/fern/validation/client.py">get_validity</a>() -> GetValidityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint used to test the validity and some basic information about a specific API Key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.validation.get_validity()

```
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

