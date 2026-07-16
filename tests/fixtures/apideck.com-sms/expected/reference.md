# Reference
## Messages
<details><summary><code>client.messages.<a href="src/fern/messages/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Messages
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.messages.all_(
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.messages.add(
    body="Hi! How are you doing?",
    from_="+15017122661",
    to="+15017122662",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**body:** `str` — The message text.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `str` — The phone number that initiated the message.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — The phone number that received the message.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the object was created.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The user who created the object.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[MessageDirection]` — The direction of the message.
    
</dd>
</dl>

<dl>
<dd>

**error:** `typing.Optional[MessageError]` — The error returned if your message status is failed or undelivered.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for an object.
    
</dd>
</dl>

<dl>
<dd>

**messaging_service_id:** `typing.Optional[str]` — The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID.
    
</dd>
</dl>

<dl>
<dd>

**number_of_media_files:** `typing.Optional[int]` — The number of media files associated with the message.
    
</dd>
</dl>

<dl>
<dd>

**number_of_units:** `typing.Optional[int]` — The number of units that make up the complete message. Messages can be split up due to the constraints of the message size.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[MessagePrice]` — Price of the message.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — A client reference.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[dt.datetime]` — The scheduled date and time of the message.
    
</dd>
</dl>

<dl>
<dd>

**sent_at:** `typing.Optional[dt.datetime]` — The date and time that the message was sent
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[MessageStatus]` — Status of the delivery of the message.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[MessageType]` — Set to sms for SMS messages and mms for MMS messages.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the object was last updated.
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` — The user who last updated the object.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Define a webhook to receive delivery notifications.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.messages.one(
    id="id",
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.messages.delete(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.messages.update(
    id_="id",
    body="Hi! How are you doing?",
    from_="+15017122661",
    to="+15017122662",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` — The message text.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `str` — The phone number that initiated the message.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — The phone number that received the message.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the object was created.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The user who created the object.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[MessageDirection]` — The direction of the message.
    
</dd>
</dl>

<dl>
<dd>

**error:** `typing.Optional[MessageError]` — The error returned if your message status is failed or undelivered.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for an object.
    
</dd>
</dl>

<dl>
<dd>

**messaging_service_id:** `typing.Optional[str]` — The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID.
    
</dd>
</dl>

<dl>
<dd>

**number_of_media_files:** `typing.Optional[int]` — The number of media files associated with the message.
    
</dd>
</dl>

<dl>
<dd>

**number_of_units:** `typing.Optional[int]` — The number of units that make up the complete message. Messages can be split up due to the constraints of the message size.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[MessagePrice]` — Price of the message.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — A client reference.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[dt.datetime]` — The scheduled date and time of the message.
    
</dd>
</dl>

<dl>
<dd>

**sent_at:** `typing.Optional[dt.datetime]` — The date and time that the message was sent
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[MessageStatus]` — Status of the delivery of the message.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[MessageType]` — Set to sms for SMS messages and mms for MMS messages.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the object was last updated.
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` — The user who last updated the object.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Define a webhook to receive delivery notifications.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

