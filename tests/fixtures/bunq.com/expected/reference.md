# Reference
## attachment-public
<details><summary><code>client.attachment_public.<a href="src/fern/attachment_public/client.py">create_attachment_public</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new public attachment. Create a POST request with a payload that contains a binary representation of the file, without any JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg, or image/png) in the Content-Type header. You are required to provide a description of the attachment using the X-Bunq-Attachment-Description header.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.attachment_public.create_attachment_public(
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

**request:** `AttachmentPublic` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attachment_public.<a href="src/fern/attachment_public/client.py">read_attachment_public</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific attachment's metadata through its UUID. The Content-Type header of the response will describe the MIME type of the attachment file.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.attachment_public.read_attachment_public(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## content
<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_attachment_public</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the raw content of a specific attachment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_attachment_public(
    attachment_public_uuid="attachment-publicUUID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attachment_public_uuid:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_place_lookup_photo</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View endpoint for place opening periods.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_place_lookup_photo(
    place_lookup_id=1,
    photo_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**place_lookup_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**photo_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_attachment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the raw content of a specific attachment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_attachment(
    user_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_card_export_statement_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the raw content of a card statement export. The returned file format could be CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_card_export_statement_card(
    user_id=1,
    card_id=1,
    export_statement_card_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**export_statement_card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_chat_conversation_attachment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the raw content of a specific attachment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_chat_conversation_attachment(
    user_id=1,
    chat_conversation_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**chat_conversation_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_export_annual_overview</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to retrieve the raw content of an annual overview.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_export_annual_overview(
    user_id=1,
    export_annual_overview_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**export_annual_overview_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_attachment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the raw content of a specific attachment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_monetary_account_attachment(
    user_id=1,
    monetary_account_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_customer_statement</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the raw content of a statement export. The returned file format could be MT940, CSV or PDF depending on the statement format specified during the statement creation. The doc won't display the response of a request to get the content of a statement export.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_monetary_account_customer_statement(
    user_id=1,
    monetary_account_id=1,
    customer_statement_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**customer_statement_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_event_statement</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the raw content of a payment statement export.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_monetary_account_event_statement(
    user_id=1,
    monetary_account_id=1,
    event_id=1,
    statement_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**statement_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_export_rib</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to retrieve the raw content of an RIB.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.content.list_all_content_for_user_monetary_account_export_rib(
    user_id=1,
    monetary_account_id=1,
    export_rib_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**export_rib_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## avatar
<details><summary><code>client.avatar.<a href="src/fern/avatar/client.py">create_avatar</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.avatar.create_avatar()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**anchor_uuid:** `typing.Optional[str]` — The public UUID of object this avatar is anchored to.
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[typing.Sequence[Image]]` — The actual image information of this avatar.
    
</dd>
</dl>

<dl>
<dd>

**style:** `typing.Optional[str]` — The style (if applicable) for this Avatar.
    
</dd>
</dl>

<dl>
<dd>

**uuid_:** `typing.Optional[str]` — The public UUID of the avatar.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatar.<a href="src/fern/avatar/client.py">read_avatar</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.avatar.read_avatar(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## device
<details><summary><code>client.device.<a href="src/fern/device/client.py">list_all_device</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collection of Devices. A Device is either a DevicePhone or a DeviceServer.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.device.list_all_device()

```
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

<details><summary><code>client.device.<a href="src/fern/device/client.py">read_device</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single Device. A Device is either a DevicePhone or a DeviceServer.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.device.read_device(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## device-server
<details><summary><code>client.device_server.<a href="src/fern/device_server/client.py">list_all_device_server</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collection of all the DeviceServers you have created.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.device_server.list_all_device_server()

```
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

<details><summary><code>client.device_server.<a href="src/fern/device_server/client.py">create_device_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new DeviceServer providing the installation token in the header and signing the request with the private part of the key you used to create the installation. The API Key that you are using will be bound to the IP address of the DeviceServer which you have created.<br/><br/>Using a Wildcard API Key gives you the freedom to make API calls even if the IP address has changed after the POST device-server.<br/><br/>Find out more at this link <a href="https:/bunq.com/en/apikey-dynamic-ip" target="_blank">https:/bunq.com/en/apikey-dynamic-ip</a>.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.device_server.create_device_server(
    description="description",
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

**description:** `str` — The description of the DeviceServer. This is only for your own reference when reading the DeviceServer again.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` — The API key. You can request an API key in the bunq app.
    
</dd>
</dl>

<dl>
<dd>

**permitted_ips:** `typing.Optional[typing.Sequence[str]]` — An array of IPs (v4 or v6) this DeviceServer will be able to do calls from. These will be linked to the API key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_server.<a href="src/fern/device_server/client.py">read_device_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one of your DeviceServers.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.device_server.read_device_server(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## installation
<details><summary><code>client.installation.<a href="src/fern/installation/client.py">list_all_installation</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You must have an active session to make this call. This call returns the Id of the the Installation you are using in your session.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.installation.list_all_installation()

```
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

<details><summary><code>client.installation.<a href="src/fern/installation/client.py">create_installation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is the only API call that does not require you to use the "X-Bunq-Client-Authentication" and "X-Bunq-Client-Signature" headers.
 You provide the server with the public part of the key pair that you are going to use to create the value of the signature header for all future API calls. The server creates an installation for you. Store the Installation Token and ServerPublicKey from the response. This token is used in the "X-Bunq-Client-Authentication" header for the creation of a DeviceServer and SessionServer.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.installation.create_installation(
    client_public_key="client_public_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_public_key:** `str` — Your public key. This is the public part of the key pair that you are going to use to create value of the "X-Bunq-Client-Signature" header for all future API calls.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.installation.<a href="src/fern/installation/client.py">read_installation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You must have an active session to make this call. This call is used to check whether the Id you provide is the Id of your current installation or not.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.installation.read_installation(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## server-public-key
<details><summary><code>client.server_public_key.<a href="src/fern/server_public_key/client.py">list_all_server_public_key_for_installation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Show the ServerPublicKey for this Installation.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.server_public_key.list_all_server_public_key_for_installation(
    installation_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**installation_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## payment-service-provider-credential
<details><summary><code>client.payment_service_provider_credential.<a href="src/fern/payment_service_provider_credential/client.py">create_payment_service_provider_credential</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a Payment Service Provider and provide credentials
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_service_provider_credential.create_payment_service_provider_credential(
    client_payment_service_provider_certificate="client_payment_service_provider_certificate",
    client_payment_service_provider_certificate_chain="client_payment_service_provider_certificate_chain",
    client_public_key_signature="client_public_key_signature",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_payment_service_provider_certificate:** `str` — Payment Services Directive 2 compatible QSEAL certificate
    
</dd>
</dl>

<dl>
<dd>

**client_payment_service_provider_certificate_chain:** `str` — Intermediate and root certificate belonging to the provided certificate.
    
</dd>
</dl>

<dl>
<dd>

**client_public_key_signature:** `str` — The Base64 encoded signature of the public key provided during installation and with the installation token appended as a nonce. Signed with the private key belonging to the QSEAL certificate.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_service_provider_credential.<a href="src/fern/payment_service_provider_credential/client.py">read_payment_service_provider_credential</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a Payment Service Provider and provide credentials
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_service_provider_credential.read_payment_service_provider_credential(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sandbox-user-company
<details><summary><code>client.sandbox_user_company.<a href="src/fern/sandbox_user_company/client.py">create_sandbox_user_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create a sandbox userCompany.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.sandbox_user_company.create_sandbox_user_company(
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

**request:** `SandboxUserCompany` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sandbox-user-person
<details><summary><code>client.sandbox_user_person.<a href="src/fern/sandbox_user_person/client.py">create_sandbox_user_person</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create a sandbox userPerson.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.sandbox_user_person.create_sandbox_user_person(
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

**request:** `SandboxUserPerson` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## server-error
<details><summary><code>client.server_error.<a href="src/fern/server_error/client.py">create_server_error</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint that will always throw an error.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.server_error.create_server_error(
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

**request:** `ServerError` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## session-server
<details><summary><code>client.session_server.<a href="src/fern/session_server/client.py">create_session_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new session for a DeviceServer. Provide the Installation token in the "X-Bunq-Client-Authentication" header. And don't forget to create the "X-Bunq-Client-Signature" header. The response contains a Session token that should be used for as the "X-Bunq-Client-Authentication" header for all future API calls. The ip address making this call needs to match the ip address bound to your API key.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.session_server.create_session_server(
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

**secret:** `str` — The API key of the user you want to login. If your API key has not been used before, it will be bound to the ip address of this DeviceServer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## session
<details><summary><code>client.session.<a href="src/fern/session/client.py">delete_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the current session.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.session.delete_session(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.user.<a href="src/fern/user/client.py">list_all_user</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collection of all available users.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.user.list_all_user()

```
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">read_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.user.read_user(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## user-company
<details><summary><code>client.user_company.<a href="src/fern/user_company/client.py">read_user_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific company.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.user_company.read_user_company(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_company.<a href="src/fern/user_company/client.py">update_user_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify a specific company's data.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.user_company.update_user_company(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**address_main:** `typing.Optional[Address]` — The company's main address.
    
</dd>
</dl>

<dl>
<dd>

**address_postal:** `typing.Optional[Address]` — The company's postal address.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[typing.Sequence[Pointer]]` — The aliases of the account.
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[Avatar]` — The company's avatar.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The public UUID of the company's avatar.
    
</dd>
</dl>

<dl>
<dd>

**billing_contract:** `typing.Optional[typing.Sequence[BillingContractSubscription]]` — The subscription of the company.
    
</dd>
</dl>

<dl>
<dd>

**chamber_of_commerce_number:** `typing.Optional[str]` — The company's chamber of commerce number.
    
</dd>
</dl>

<dl>
<dd>

**counter_bank_iban:** `typing.Optional[str]` — The company's other bank account IBAN, through which we verify it.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — The country as an ISO 3166-1 alpha-2 country code.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp of the company object's creation.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[Customer]` — The customer profile of the company.
    
</dd>
</dl>

<dl>
<dd>

**customer_limit:** `typing.Optional[CustomerLimit]` — The customer limits of the company.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit_without_confirmation_login:** `typing.Optional[Amount]` — The amount the company can pay in the session without asking for credentials.
    
</dd>
</dl>

<dl>
<dd>

**deny_reason:** `typing.Optional[str]` — The user deny reason.
    
</dd>
</dl>

<dl>
<dd>

**directors:** `typing.Optional[typing.Sequence[LabelUser]]` — The existing bunq aliases for the company's directors.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The company's display name.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the modified company.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    
</dd>
</dl>

<dl>
<dd>

**legal_form:** `typing.Optional[str]` — The company's legal form.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The company name.
    
</dd>
</dl>

<dl>
<dd>

**notification_filters:** `typing.Optional[typing.Sequence[NotificationFilter]]` — The types of notifications that will result in a push notification or URL callback for this UserCompany.
    
</dd>
</dl>

<dl>
<dd>

**public_nick_name:** `typing.Optional[str]` — The company's public nick name.
    
</dd>
</dl>

<dl>
<dd>

**public_uuid:** `typing.Optional[str]` — The company's public UUID.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    
</dd>
</dl>

<dl>
<dd>

**relations:** `typing.Optional[typing.Sequence[RelationUser]]` — The relations for this user.
    
</dd>
</dl>

<dl>
<dd>

**sector_of_industry:** `typing.Optional[str]` — The sector of industry.
    
</dd>
</dl>

<dl>
<dd>

**session_timeout:** `typing.Optional[int]` — The setting for the session timeout of the company in seconds.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The user status. Can be: ACTIVE, SIGNUP, RECOVERY.
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.
    
</dd>
</dl>

<dl>
<dd>

**tax_resident:** `typing.Optional[typing.Sequence[TaxResident]]` — The user's tax residence numbers for different countries.
    
</dd>
</dl>

<dl>
<dd>

**type_of_business_entity:** `typing.Optional[str]` — The type of business entity.
    
</dd>
</dl>

<dl>
<dd>

**ubo:** `typing.Optional[typing.Sequence[Ubo]]` — The names of the company's ultimate beneficiary owners. Minimum zero, maximum four.
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp of the company object's last update.
    
</dd>
</dl>

<dl>
<dd>

**version_terms_of_service:** `typing.Optional[str]` — The version of the terms of service accepted by the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## name
<details><summary><code>client.name.<a href="src/fern/name/client.py">list_all_name_for_user_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all the known (trade) names for a specific user company.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.name.list_all_name_for_user_company(
    user_company_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_company_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## user-payment-service-provider
<details><summary><code>client.user_payment_service_provider.<a href="src/fern/user_payment_service_provider/client.py">read_user_payment_service_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view UserPaymentServiceProvider for session creation.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.user_payment_service_provider.read_user_payment_service_provider(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## user-person
<details><summary><code>client.user_person.<a href="src/fern/user_person/client.py">read_user_person</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific person.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.user_person.read_user_person(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_person.<a href="src/fern/user_person/client.py">update_user_person</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify a specific person object's data.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.user_person.update_user_person(
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**address_main:** `typing.Optional[Address]` — The person's main address.
    
</dd>
</dl>

<dl>
<dd>

**address_postal:** `typing.Optional[Address]` — The person's postal address.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[typing.Sequence[Pointer]]` — The aliases of the user.
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[Avatar]` — The user's avatar.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The public UUID of the user's avatar.
    
</dd>
</dl>

<dl>
<dd>

**country_of_birth:** `typing.Optional[str]` — The person's country of birth. Formatted as a SO 3166-1 alpha-2 country code.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp of the person object's creation.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit_without_confirmation_login:** `typing.Optional[Amount]` — The amount the user can pay in the session without asking for credentials.
    
</dd>
</dl>

<dl>
<dd>

**date_of_birth:** `typing.Optional[str]` — The person's date of birth. Accepts ISO8601 date formats.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The display name for the person.
    
</dd>
</dl>

<dl>
<dd>

**document_back_attachment_id:** `typing.Optional[int]` — The reference to the uploaded picture/scan of the back side of the identification document.
    
</dd>
</dl>

<dl>
<dd>

**document_country_of_issuance:** `typing.Optional[str]` — The country which issued the identification document the person registered with.
    
</dd>
</dl>

<dl>
<dd>

**document_front_attachment_id:** `typing.Optional[int]` — The reference to the uploaded picture/scan of the front side of the identification document.
    
</dd>
</dl>

<dl>
<dd>

**document_number:** `typing.Optional[str]` — The identification document number the person registered with.
    
</dd>
</dl>

<dl>
<dd>

**document_type:** `typing.Optional[str]` — The type of identification document the person registered with.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The person's first name.
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[str]` — The person's gender. Can be MALE, FEMALE or UNKNOWN.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the modified person object.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The person's last name.
    
</dd>
</dl>

<dl>
<dd>

**legal_guardian_alias:** `typing.Optional[Pointer]` — The legal guardian of the user. Required for minors.
    
</dd>
</dl>

<dl>
<dd>

**legal_name:** `typing.Optional[str]` — The person's legal name.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The person's middle name.
    
</dd>
</dl>

<dl>
<dd>

**nationality:** `typing.Optional[str]` — The person's nationality. Formatted as a SO 3166-1 alpha-2 country code.
    
</dd>
</dl>

<dl>
<dd>

**notification_filters:** `typing.Optional[typing.Sequence[NotificationFilter]]` — The types of notifications that will result in a push notification or URL callback for this UserPerson.
    
</dd>
</dl>

<dl>
<dd>

**place_of_birth:** `typing.Optional[str]` — The person's place of birth.
    
</dd>
</dl>

<dl>
<dd>

**public_nick_name:** `typing.Optional[str]` — The public nick name for the person.
    
</dd>
</dl>

<dl>
<dd>

**public_uuid:** `typing.Optional[str]` — The person's public UUID.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    
</dd>
</dl>

<dl>
<dd>

**relations:** `typing.Optional[typing.Sequence[RelationUser]]` — The relations for this user.
    
</dd>
</dl>

<dl>
<dd>

**session_timeout:** `typing.Optional[int]` — The setting for the session timeout of the user in seconds.
    
</dd>
</dl>

<dl>
<dd>

**signup_track_type:** `typing.Optional[str]` — The type of signup track the user is following.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The user status. The user status. Can be: ACTIVE, BLOCKED, SIGNUP, RECOVERY, DENIED or ABORTED.
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.
    
</dd>
</dl>

<dl>
<dd>

**subscription_type:** `typing.Optional[str]` — The subscription type the user should start on.
    
</dd>
</dl>

<dl>
<dd>

**tax_resident:** `typing.Optional[typing.Sequence[TaxResident]]` — The user's tax residence numbers for different countries.
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp of the person object's last update.
    
</dd>
</dl>

<dl>
<dd>

**version_terms_of_service:** `typing.Optional[str]` — The version of the terms of service accepted by the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## attachment
<details><summary><code>client.attachment.<a href="src/fern/attachment/client.py">read_attachment_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific attachment. The header of the response contains the content-type of the attachment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.attachment.read_attachment_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attachment.<a href="src/fern/attachment/client.py">create_attachment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new monetary account attachment. Create a POST request with a payload that contains the binary representation of the file, without any JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg) in the Content-Type header. You are required to provide a description of the attachment using the X-Bunq-Attachment-Description header.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.attachment.create_attachment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AttachmentMonetaryAccount` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## billing-contract-subscription
<details><summary><code>client.billing_contract_subscription.<a href="src/fern/billing_contract_subscription/client.py">list_all_billing_contract_subscription_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all subscription billing contract for the authenticated user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.billing_contract_subscription.list_all_billing_contract_subscription_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## bunqme-fundraiser-profile
<details><summary><code>client.bunqme_fundraiser_profile.<a href="src/fern/bunqme_fundraiser_profile/client.py">list_all_bunqme_fundraiser_profile_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

bunq.me public profile of the user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_fundraiser_profile.list_all_bunqme_fundraiser_profile_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bunqme_fundraiser_profile.<a href="src/fern/bunqme_fundraiser_profile/client.py">read_bunqme_fundraiser_profile_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

bunq.me public profile of the user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_fundraiser_profile.read_bunqme_fundraiser_profile_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## card
<details><summary><code>client.card.<a href="src/fern/card/client.py">list_all_card_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all the cards available to the user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card.list_all_card_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.card.<a href="src/fern/card/client.py">read_card_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the details of a specific card.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card.read_card_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.card.<a href="src/fern/card/client.py">update_card_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the card details. Allow to change pin code, status, limits, country permissions and the monetary account connected to the card. When the card has been received, it can be also activated through this endpoint.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card.update_card_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**activation_code:** `typing.Optional[str]` — DEPRECATED: Activate a card by setting status to ACTIVE when the order_status is ACCEPTED_FOR_PRODUCTION.
    
</dd>
</dl>

<dl>
<dd>

**card_limit:** `typing.Optional[Amount]` — The spending limit for the card.
    
</dd>
</dl>

<dl>
<dd>

**card_limit_atm:** `typing.Optional[Amount]` — The ATM spending limit for the card.
    
</dd>
</dl>

<dl>
<dd>

**country_permission:** `typing.Optional[typing.Sequence[CardCountryPermission]]` — The countries for which to grant (temporary) permissions to use the card.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_fallback:** `typing.Optional[int]` — ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.
    
</dd>
</dl>

<dl>
<dd>

**order_status:** `typing.Optional[str]` — The order status to set for the card. Set to CARD_REQUEST_PENDING to get a virtual card produced.
    
</dd>
</dl>

<dl>
<dd>

**pin_code:** `typing.Optional[str]` — The plaintext pin code. Requests require encryption to be enabled.
    
</dd>
</dl>

<dl>
<dd>

**pin_code_assignment:** `typing.Optional[typing.Sequence[CardPinAssignment]]` — Array of Types, PINs, account IDs assigned to the card.
    
</dd>
</dl>

<dl>
<dd>

**primary_account_numbers:** `typing.Optional[typing.Sequence[CardPrimaryAccountNumber]]` — Array of PANs and their attributes.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status to set for the card. Can be ACTIVE, DEACTIVATED, LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when order status is ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Can only be set to DEACTIVATED after initial activation, i.e. order_status is DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are permanent and cannot be changed after.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## card-batch
<details><summary><code>client.card_batch.<a href="src/fern/card_batch/client.py">create_card_batch_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to update multiple cards in a batch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import CardBatchEntry, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card_batch.create_card_batch_for_user(
    user_id=1,
    cards=[
        CardBatchEntry(
            id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**cards:** `typing.Sequence[CardBatchEntry]` — The cards that need to be updated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## card-batch-replace
<details><summary><code>client.card_batch_replace.<a href="src/fern/card_batch_replace/client.py">create_card_batch_replace_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to replace multiple cards in a batch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import CardBatchReplaceEntry, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card_batch_replace.create_card_batch_replace_for_user(
    user_id=1,
    cards=[
        CardBatchReplaceEntry(
            id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**cards:** `typing.Sequence[CardBatchReplaceEntry]` — The cards that need to be replaced.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## card-credit
<details><summary><code>client.card_credit.<a href="src/fern/card_credit/client.py">create_card_credit_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new credit card request.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card_credit.create_card_credit_for_user(
    user_id=1,
    name_on_card="name_on_card",
    product_type="product_type",
    second_line="second_line",
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**name_on_card:** `str` — The user's name as it will be on the card. Check 'card-name' for the available card names for a user.
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `str` — The product type of the card to order.
    
</dd>
</dl>

<dl>
<dd>

**second_line:** `str` — The second line of text on the card, used as name/description for it. It can contain at most 17 characters and it can be empty.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of card to order. Can be MASTERCARD.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[Pointer]` — The pointer to the monetary account that will be connected at first with the card. Its IBAN code is also the one that will be printed on the card itself. The pointer must be of type IBAN.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_fallback:** `typing.Optional[int]` — ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.
    
</dd>
</dl>

<dl>
<dd>

**order_status:** `typing.Optional[str]` — The order status of this card. Can be CARD_REQUEST_PENDING or VIRTUAL_DELIVERY.
    
</dd>
</dl>

<dl>
<dd>

**pin_code_assignment:** `typing.Optional[typing.Sequence[CardPinAssignment]]` — Array of Types, PINs, account IDs assigned to the card.
    
</dd>
</dl>

<dl>
<dd>

**preferred_name_on_card:** `typing.Optional[str]` — The user's preferred name that can be put on the card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## card-debit
<details><summary><code>client.card_debit.<a href="src/fern/card_debit/client.py">create_card_debit_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new debit card request.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card_debit.create_card_debit_for_user(
    user_id=1,
    name_on_card="name_on_card",
    product_type="product_type",
    second_line="second_line",
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**name_on_card:** `str` — The user's name as it will be on the card. Check 'card-name' for the available card names for a user.
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `str` — The product type of the card to order.
    
</dd>
</dl>

<dl>
<dd>

**second_line:** `str` — The second line of text on the card, used as name/description for it. It can contain at most 17 characters and it can be empty.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of card to order. Can be MAESTRO or MASTERCARD.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[Pointer]` — The pointer to the monetary account that will be connected at first with the card. Its IBAN code is also the one that will be printed on the card itself. The pointer must be of type IBAN.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_fallback:** `typing.Optional[int]` — ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.
    
</dd>
</dl>

<dl>
<dd>

**order_status:** `typing.Optional[str]` — The order status of this card. Can be CARD_REQUEST_PENDING or VIRTUAL_DELIVERY.
    
</dd>
</dl>

<dl>
<dd>

**pin_code_assignment:** `typing.Optional[typing.Sequence[CardPinAssignment]]` — Array of Types, PINs, account IDs assigned to the card.
    
</dd>
</dl>

<dl>
<dd>

**preferred_name_on_card:** `typing.Optional[str]` — The user's preferred name that can be put on the card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## card-name
<details><summary><code>client.card_name.<a href="src/fern/card_name/client.py">list_all_card_name_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all the accepted card names for a specific user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.card_name.list_all_card_name_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## export-statement-card
<details><summary><code>client.export_statement_card.<a href="src/fern/export_statement_card/client.py">list_all_export_statement_card_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card.list_all_export_statement_card_for_user_card(
    user_id=1,
    card_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_statement_card.<a href="src/fern/export_statement_card/client.py">read_export_statement_card_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing card statement exports. Statement exports can be created in either CSV or PDF file format.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card.read_export_statement_card_for_user_card(
    user_id=1,
    card_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## export-statement-card-csv
<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">list_all_export_statement_card_csv_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardCsv
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_csv.list_all_export_statement_card_csv_for_user_card(
    user_id=1,
    card_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">create_export_statement_card_csv_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardCsv
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_csv.create_export_statement_card_csv_for_user_card(
    user_id=1,
    card_id=1,
    date_end="date_end",
    date_start="date_start",
    regional_format="regional_format",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**date_end:** `str` — The end date for making statements.
    
</dd>
</dl>

<dl>
<dd>

**date_start:** `str` — The start date for making statements.
    
</dd>
</dl>

<dl>
<dd>

**regional_format:** `str` — Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">read_export_statement_card_csv_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardCsv
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_csv.read_export_statement_card_csv_for_user_card(
    user_id=1,
    card_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">delete_export_statement_card_csv_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardCsv
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_csv.delete_export_statement_card_csv_for_user_card(
    user_id=1,
    card_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## export-statement-card-pdf
<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">list_all_export_statement_card_pdf_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardPdf
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_pdf.list_all_export_statement_card_pdf_for_user_card(
    user_id=1,
    card_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">create_export_statement_card_pdf_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardPdf
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_pdf.create_export_statement_card_pdf_for_user_card(
    user_id=1,
    card_id=1,
    date_end="date_end",
    date_start="date_start",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**date_end:** `str` — The end date for making statements.
    
</dd>
</dl>

<dl>
<dd>

**date_start:** `str` — The start date for making statements.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">read_export_statement_card_pdf_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardPdf
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_pdf.read_export_statement_card_pdf_for_user_card(
    user_id=1,
    card_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">delete_export_statement_card_pdf_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to serialize ExportStatementCardPdf
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_statement_card_pdf.delete_export_statement_card_pdf_for_user_card(
    user_id=1,
    card_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## generated-cvc2
<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">list_all_generated_cvc2for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all generated CVC2 codes for a card.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.generated_cvc2.list_all_generated_cvc2for_user_card(
    user_id=1,
    card_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">create_generated_cvc2for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a new CVC2 code for a card.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.generated_cvc2.create_generated_cvc2for_user_card(
    user_id=1,
    card_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of generated cvc2. Can be STATIC or GENERATED.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">read_generated_cvc2for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details for a specific generated CVC2 code.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.generated_cvc2.read_generated_cvc2for_user_card(
    user_id=1,
    card_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">update_generated_cvc2for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for generating and retrieving a new CVC2 code.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.generated_cvc2.update_generated_cvc2for_user_card(
    user_id=1,
    card_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of generated cvc2. Can be STATIC or GENERATED.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## replace
<details><summary><code>client.replace.<a href="src/fern/replace/client.py">create_replace_for_user_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request a card replacement.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.replace.create_replace_for_user_card(
    user_id=1,
    card_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**name_on_card:** `typing.Optional[str]` — The user's name as it will be on the card. Check 'card-name' for the available card names for a user.
    
</dd>
</dl>

<dl>
<dd>

**pin_code_assignment:** `typing.Optional[typing.Sequence[CardPinAssignment]]` — Array of Types, PINs, account IDs assigned to the card.
    
</dd>
</dl>

<dl>
<dd>

**preferred_name_on_card:** `typing.Optional[str]` — The user's preferred name that can be put on the card.
    
</dd>
</dl>

<dl>
<dd>

**second_line:** `typing.Optional[str]` — The second line on the card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## certificate-pinned
<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">list_all_certificate_pinned_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all the pinned certificate chain for the given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.certificate_pinned.list_all_certificate_pinned_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">create_certificate_pinned_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pin the certificate chain.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Certificate, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.certificate_pinned.create_certificate_pinned_for_user(
    user_id=1,
    certificate_chain=[Certificate()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**certificate_chain:** `typing.Sequence[Certificate]` — The certificate chain in .PEM format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">read_certificate_pinned_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the pinned certificate chain with the specified ID.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.certificate_pinned.read_certificate_pinned_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">delete_certificate_pinned_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the pinned certificate chain with the specific ID.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.certificate_pinned.delete_certificate_pinned_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## challenge-request
<details><summary><code>client.challenge_request.<a href="src/fern/challenge_request/client.py">read_challenge_request_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for apps to fetch a challenge request.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.challenge_request.read_challenge_request_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.challenge_request.<a href="src/fern/challenge_request/client.py">update_challenge_request_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for apps to fetch a challenge request.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.challenge_request.update_challenge_request_for_user(
    user_id=1,
    item_id=1,
    status="status",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**status:** `str` — The status of the identity check. Can be ACCEPTED_PENDING_RESPONSE or REJECTED_PENDING_RESPONSE.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## company
<details><summary><code>client.company.<a href="src/fern/company/client.py">list_all_company_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and manage companies.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.company.list_all_company_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.company.<a href="src/fern/company/client.py">create_company_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and manage companies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Address, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.company.create_company_for_user(
    user_id=1,
    address_main=Address(),
    address_postal=Address(),
    country="country",
    legal_form="legal_form",
    name="name",
    subscription_type="subscription_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**address_main:** `Address` — The company's main address.
    
</dd>
</dl>

<dl>
<dd>

**address_postal:** `Address` — The company's postal address.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — The country where the company is registered.
    
</dd>
</dl>

<dl>
<dd>

**legal_form:** `str` — The company's legal form.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The company name.
    
</dd>
</dl>

<dl>
<dd>

**subscription_type:** `str` — The subscription type for the company.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The public UUID of the company's avatar.
    
</dd>
</dl>

<dl>
<dd>

**chamber_of_commerce_number:** `typing.Optional[str]` — The company's chamber of commerce number.
    
</dd>
</dl>

<dl>
<dd>

**signup_track_type:** `typing.Optional[str]` — The type of signup track the user is following.
    
</dd>
</dl>

<dl>
<dd>

**ubo:** `typing.Optional[typing.Sequence[Ubo]]` — The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.
    
</dd>
</dl>

<dl>
<dd>

**vat_number:** `typing.Optional[CompanyVatNumber]` — All the vat numbers of the company
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.company.<a href="src/fern/company/client.py">read_company_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and manage companies.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.company.read_company_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.company.<a href="src/fern/company/client.py">update_company_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and manage companies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Address, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.company.update_company_for_user(
    user_id=1,
    item_id=1,
    address_main=Address(),
    address_postal=Address(),
    country="country",
    legal_form="legal_form",
    name="name",
    subscription_type="subscription_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**address_main:** `Address` — The company's main address.
    
</dd>
</dl>

<dl>
<dd>

**address_postal:** `Address` — The company's postal address.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — The country where the company is registered.
    
</dd>
</dl>

<dl>
<dd>

**legal_form:** `str` — The company's legal form.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The company name.
    
</dd>
</dl>

<dl>
<dd>

**subscription_type:** `str` — The subscription type for the company.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The public UUID of the company's avatar.
    
</dd>
</dl>

<dl>
<dd>

**chamber_of_commerce_number:** `typing.Optional[str]` — The company's chamber of commerce number.
    
</dd>
</dl>

<dl>
<dd>

**signup_track_type:** `typing.Optional[str]` — The type of signup track the user is following.
    
</dd>
</dl>

<dl>
<dd>

**ubo:** `typing.Optional[typing.Sequence[Ubo]]` — The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.
    
</dd>
</dl>

<dl>
<dd>

**vat_number:** `typing.Optional[CompanyVatNumber]` — All the vat numbers of the company
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## confirmation-of-funds
<details><summary><code>client.confirmation_of_funds.<a href="src/fern/confirmation_of_funds/client.py">create_confirmation_of_funds_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to confirm availability of funds on an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Amount, FernApi, Pointer

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.confirmation_of_funds.create_confirmation_of_funds_for_user(
    user_id=1,
    amount=Amount(),
    pointer_iban=Pointer(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` — The amount we want to check for.
    
</dd>
</dl>

<dl>
<dd>

**pointer_iban:** `Pointer` — The pointer (IBAN) of the account we're querying.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## credential-password-ip
<details><summary><code>client.credential_password_ip.<a href="src/fern/credential_password_ip/client.py">list_all_credential_password_ip_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a credential of a user for server authentication, or delete the credential of a user for server authentication.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.credential_password_ip.list_all_credential_password_ip_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credential_password_ip.<a href="src/fern/credential_password_ip/client.py">read_credential_password_ip_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a credential of a user for server authentication, or delete the credential of a user for server authentication.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.credential_password_ip.read_credential_password_ip_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ip
<details><summary><code>client.ip.<a href="src/fern/ip/client.py">list_all_ip_for_user_credential_password_ip</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the IPs which may be used for a credential of a user for server authentication.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.ip.list_all_ip_for_user_credential_password_ip(
    user_id=1,
    credential_password_ip_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**credential_password_ip_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip.<a href="src/fern/ip/client.py">create_ip_for_user_credential_password_ip</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the IPs which may be used for a credential of a user for server authentication.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.ip.create_ip_for_user_credential_password_ip(
    user_id=1,
    credential_password_ip_id=1,
    ip="ip",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**credential_password_ip_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` — The IP address.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip.<a href="src/fern/ip/client.py">read_ip_for_user_credential_password_ip</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the IPs which may be used for a credential of a user for server authentication.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.ip.read_ip_for_user_credential_password_ip(
    user_id=1,
    credential_password_ip_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**credential_password_ip_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip.<a href="src/fern/ip/client.py">update_ip_for_user_credential_password_ip</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the IPs which may be used for a credential of a user for server authentication.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.ip.update_ip_for_user_credential_password_ip(
    user_id=1,
    credential_password_ip_id=1,
    item_id=1,
    ip="ip",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**credential_password_ip_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` — The IP address.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## currency-cloud-beneficiary
<details><summary><code>client.currency_cloud_beneficiary.<a href="src/fern/currency_cloud_beneficiary/client.py">list_all_currency_cloud_beneficiary_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to manage CurrencyCloud beneficiaries.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_cloud_beneficiary.list_all_currency_cloud_beneficiary_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.currency_cloud_beneficiary.<a href="src/fern/currency_cloud_beneficiary/client.py">create_currency_cloud_beneficiary_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to manage CurrencyCloud beneficiaries.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_cloud_beneficiary.create_currency_cloud_beneficiary_for_user(
    user_id=1,
    all_field=["all_field"],
    country="country",
    currency="currency",
    legal_entity_type="legal_entity_type",
    name="name",
    payment_type="payment_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**all_field:** `typing.Sequence[str]` — All fields that were required by CurrencyCloud. Obtained through the CurrencyCloudBeneficiaryRequirement listing.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — The country of the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — The currency of the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**legal_entity_type:** `str` — The legal entity type of the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `str` — The payment type this requirement is for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.currency_cloud_beneficiary.<a href="src/fern/currency_cloud_beneficiary/client.py">read_currency_cloud_beneficiary_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to manage CurrencyCloud beneficiaries.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_cloud_beneficiary.read_currency_cloud_beneficiary_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## currency-cloud-beneficiary-requirement
<details><summary><code>client.currency_cloud_beneficiary_requirement.<a href="src/fern/currency_cloud_beneficiary_requirement/client.py">list_all_currency_cloud_beneficiary_requirement_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to list requirements for CurrencyCloud beneficiaries.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_cloud_beneficiary_requirement.list_all_currency_cloud_beneficiary_requirement_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.event.<a href="src/fern/event/client.py">list_all_event_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collection of events for a given user. You can add query the parameters monetary_account_id, status and/or display_user_event to filter the response. When monetary_account_id={id,id} is provided only events that relate to these monetary account ids are returned. When status={AWAITING_REPLY/FINALIZED} is provided the response only contains events with the status AWAITING_REPLY or FINALIZED. When display_user_event={true/false} is set to false user events are excluded from the response, when not provided user events are displayed. User events are events that are not related to a monetary account (for example: connect invites).
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.event.list_all_event_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event.<a href="src/fern/event/client.py">read_event_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific event for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.event.read_event_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## export-annual-overview
<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">list_all_export_annual_overview_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all the annual overviews for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_annual_overview.list_all_export_annual_overview_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">create_export_annual_overview_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new annual overview for a specific year. An overview can be generated only for a past year.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_annual_overview.create_export_annual_overview_for_user(
    user_id=1,
    year=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**year:** `int` — The year for which the overview is.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">read_export_annual_overview_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an annual overview for a user by its id.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_annual_overview.read_export_annual_overview_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">delete_export_annual_overview_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing annual overviews of all the user's monetary accounts. Once created, annual overviews can be downloaded in PDF format via the 'export-annual-overview/{id}/content' endpoint.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_annual_overview.delete_export_annual_overview_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## feature-announcement
<details><summary><code>client.feature_announcement.<a href="src/fern/feature_announcement/client.py">read_feature_announcement_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

view for updating the feature display.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.feature_announcement.read_feature_announcement_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## insight-preference-date
<details><summary><code>client.insight_preference_date.<a href="src/fern/insight_preference_date/client.py">list_all_insight_preference_date_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to allow users to set insight/budget preferences.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.insight_preference_date.list_all_insight_preference_date_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## insights
<details><summary><code>client.insights.<a href="src/fern/insights/client.py">list_all_insights_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get insights about transactions between given time range.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.insights.list_all_insights_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## insights-search
<details><summary><code>client.insights_search.<a href="src/fern/insights_search/client.py">list_all_insights_search_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get events based on time and insight category.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.insights_search.list_all_insights_search_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## invoice
<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">list_all_invoice_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to list bunq invoices by user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.invoice.list_all_invoice_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">read_invoice_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to list bunq invoices by user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.invoice.read_invoice_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">list_all_invoice_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view a bunq invoice.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.invoice.list_all_invoice_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">read_invoice_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view a bunq invoice.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.invoice.read_invoice_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## pdf-content
<details><summary><code>client.pdf_content.<a href="src/fern/pdf_content/client.py">list_all_pdf_content_for_user_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a PDF export of an invoice.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.pdf_content.list_all_pdf_content_for_user_invoice(
    user_id=1,
    invoice_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## legal-name
<details><summary><code>client.legal_name.<a href="src/fern/legal_name/client.py">list_all_legal_name_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for getting available legal names that can be used by the user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.legal_name.list_all_legal_name_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## limit
<details><summary><code>client.limit.<a href="src/fern/limit/client.py">list_all_limit_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all limits for the authenticated user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.limit.list_all_limit_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## monetary-account
<details><summary><code>client.monetary_account.<a href="src/fern/monetary_account/client.py">list_all_monetary_account_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collection of all your MonetaryAccounts.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account.list_all_monetary_account_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account.<a href="src/fern/monetary_account/client.py">read_monetary_account_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific MonetaryAccount.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account.read_monetary_account_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## monetary-account-bank
<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">list_all_monetary_account_bank_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a listing of all MonetaryAccountBanks of a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_bank.list_all_monetary_account_bank_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">create_monetary_account_bank_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new MonetaryAccountBank.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_bank.create_monetary_account_bank_for_user(
    user_id=1,
    currency="currency",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The UUID of the Avatar of the MonetaryAccountBank.
    
</dd>
</dl>

<dl>
<dd>

**country_iban:** `typing.Optional[str]` — The country of the monetary account IBAN.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit:** `typing.Optional[Amount]` — The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the MonetaryAccountBank. Defaults to 'bunq account'.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The legal name of the user / company using this monetary account.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `typing.Optional[str]` — The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**setting:** `typing.Optional[MonetaryAccountSetting]` — The settings of the MonetaryAccountBank.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">read_monetary_account_bank_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific MonetaryAccountBank.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_bank.read_monetary_account_bank_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">update_monetary_account_bank_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific existing MonetaryAccountBank.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_bank.update_monetary_account_bank_for_user(
    user_id=1,
    item_id=1,
    currency="currency",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The UUID of the Avatar of the MonetaryAccountBank.
    
</dd>
</dl>

<dl>
<dd>

**country_iban:** `typing.Optional[str]` — The country of the monetary account IBAN.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit:** `typing.Optional[Amount]` — The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the MonetaryAccountBank. Defaults to 'bunq account'.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The legal name of the user / company using this monetary account.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `typing.Optional[str]` — The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**setting:** `typing.Optional[MonetaryAccountSetting]` — The settings of the MonetaryAccountBank.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## monetary-account-external
<details><summary><code>client.monetary_account_external.<a href="src/fern/monetary_account_external/client.py">list_all_monetary_account_external_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for managing monetary accounts which are connected to external services.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_external.list_all_monetary_account_external_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_external.<a href="src/fern/monetary_account_external/client.py">read_monetary_account_external_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for managing monetary accounts which are connected to external services.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_external.read_monetary_account_external_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## monetary-account-joint
<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">list_all_monetary_account_joint_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The endpoint for joint monetary accounts.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_joint.list_all_monetary_account_joint_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">create_monetary_account_joint_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The endpoint for joint monetary accounts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import CoOwner, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_joint.create_monetary_account_joint_for_user(
    user_id=1,
    all_co_owner=[CoOwner()],
    currency="currency",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**all_co_owner:** `typing.Sequence[CoOwner]` — The users the account will be joint with.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[typing.Sequence[Pointer]]` — The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The UUID of the Avatar of the MonetaryAccountJoint.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit:** `typing.Optional[Amount]` — The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the MonetaryAccountJoint. Defaults to 'bunq account'.
    
</dd>
</dl>

<dl>
<dd>

**overdraft_limit:** `typing.Optional[Amount]` — The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `typing.Optional[str]` — The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**setting:** `typing.Optional[MonetaryAccountSetting]` — The settings of the MonetaryAccountJoint.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">read_monetary_account_joint_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The endpoint for joint monetary accounts.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_joint.read_monetary_account_joint_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">update_monetary_account_joint_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The endpoint for joint monetary accounts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import CoOwner, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_joint.update_monetary_account_joint_for_user(
    user_id=1,
    item_id=1,
    all_co_owner=[CoOwner()],
    currency="currency",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**all_co_owner:** `typing.Sequence[CoOwner]` — The users the account will be joint with.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[typing.Sequence[Pointer]]` — The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The UUID of the Avatar of the MonetaryAccountJoint.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit:** `typing.Optional[Amount]` — The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the MonetaryAccountJoint. Defaults to 'bunq account'.
    
</dd>
</dl>

<dl>
<dd>

**overdraft_limit:** `typing.Optional[Amount]` — The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `typing.Optional[str]` — The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**setting:** `typing.Optional[MonetaryAccountSetting]` — The settings of the MonetaryAccountJoint.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## monetary-account-savings
<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">list_all_monetary_account_savings_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a listing of all MonetaryAccountSavingss of a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_savings.list_all_monetary_account_savings_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">create_monetary_account_savings_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new MonetaryAccountSavings.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_savings.create_monetary_account_savings_for_user(
    user_id=1,
    currency="currency",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.
    
</dd>
</dl>

<dl>
<dd>

**all_co_owner:** `typing.Optional[typing.Sequence[CoOwner]]` — The users the account will be joint with.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The UUID of the Avatar of the MonetaryAccountSavings.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit:** `typing.Optional[Amount]` — The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the MonetaryAccountSavings. Defaults to 'bunq account'.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `typing.Optional[str]` — The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**savings_goal:** `typing.Optional[Amount]` — The Savings Goal set for this MonetaryAccountSavings.
    
</dd>
</dl>

<dl>
<dd>

**setting:** `typing.Optional[MonetaryAccountSetting]` — The settings of the MonetaryAccountSavings.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">read_monetary_account_savings_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific MonetaryAccountSavings.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_savings.read_monetary_account_savings_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">update_monetary_account_savings_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific existing MonetaryAccountSavings.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.monetary_account_savings.update_monetary_account_savings_for_user(
    user_id=1,
    item_id=1,
    currency="currency",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.
    
</dd>
</dl>

<dl>
<dd>

**all_co_owner:** `typing.Optional[typing.Sequence[CoOwner]]` — The users the account will be joint with.
    
</dd>
</dl>

<dl>
<dd>

**avatar_uuid:** `typing.Optional[str]` — The UUID of the Avatar of the MonetaryAccountSavings.
    
</dd>
</dl>

<dl>
<dd>

**daily_limit:** `typing.Optional[Amount]` — The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the MonetaryAccountSavings. Defaults to 'bunq account'.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `typing.Optional[str]` — The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**savings_goal:** `typing.Optional[Amount]` — The Savings Goal set for this MonetaryAccountSavings.
    
</dd>
</dl>

<dl>
<dd>

**setting:** `typing.Optional[MonetaryAccountSetting]` — The settings of the MonetaryAccountSavings.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## note-attachment
<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.create_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.read_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.update_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `int` — The reference to the uploaded file to attach to this note.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the attachment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage attachment notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_attachment.delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## note-text
<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_bunqme_fundraiser_result(
    user_id=1,
    monetary_account_id=1,
    bunqme_fundraiser_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_fundraiser_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_draft_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_draft_payment(
    user_id=1,
    monetary_account_id=1,
    draft_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**draft_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_ideal_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    ideal_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**ideal_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_payment_batch(
    user_id=1,
    monetary_account_id=1,
    payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_payment(
    user_id=1,
    monetary_account_id=1,
    payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_request_inquiry_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_request_inquiry_batch(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_request_inquiry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_request_inquiry(
    user_id=1,
    monetary_account_id=1,
    request_inquiry_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_inquiry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_request_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_request_response(
    user_id=1,
    monetary_account_id=1,
    request_response_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_response_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_schedule_payment_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_schedule_payment_batch(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_batch_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_batch_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_schedule_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_schedule_payment(
    user_id=1,
    monetary_account_id=1,
    schedule_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_schedule_schedule_instance(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    schedule_instance_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_instance_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_sofort_merchant_transaction(
    user_id=1,
    monetary_account_id=1,
    sofort_merchant_transaction_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**sofort_merchant_transaction_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_switch_service_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_switch_service_payment(
    user_id=1,
    monetary_account_id=1,
    switch_service_payment_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**switch_service_payment_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the notes for a given user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.create_note_text_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.read_note_text_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.update_note_text_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content of the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage text notes.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.note_text.delete_note_text_for_user_monetary_account_whitelist_whitelist_result(
    user_id=1,
    monetary_account_id=1,
    whitelist_id=1,
    whitelist_result_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**whitelist_result_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## bunqme-fundraiser-result
<details><summary><code>client.bunqme_fundraiser_result.<a href="src/fern/bunqme_fundraiser_result/client.py">read_bunqme_fundraiser_result_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

bunq.me fundraiser result containing all payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_fundraiser_result.read_bunqme_fundraiser_result_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## bunqme-tab
<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">list_all_bunqme_tab_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_tab.list_all_bunqme_tab_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">create_bunqme_tab_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import BunqMeTabEntry, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_tab.create_bunqme_tab_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    bunqme_tab_entry=BunqMeTabEntry(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_tab_entry:** `BunqMeTabEntry` — The bunq.me entry containing the payment information.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the bunq.me. Ignored in POST requests but can be used for cancelling the bunq.me by setting status as CANCELLED with a PUT request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">read_bunqme_tab_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_tab.read_bunqme_tab_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">update_bunqme_tab_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import BunqMeTabEntry, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_tab.update_bunqme_tab_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
    bunqme_tab_entry=BunqMeTabEntry(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**bunqme_tab_entry:** `BunqMeTabEntry` — The bunq.me entry containing the payment information.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the bunq.me. Ignored in POST requests but can be used for cancelling the bunq.me by setting status as CANCELLED with a PUT request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## bunqme-tab-result-response
<details><summary><code>client.bunqme_tab_result_response.<a href="src/fern/bunqme_tab_result_response/client.py">read_bunqme_tab_result_response_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view bunq.me TabResultResponse objects belonging to a tab. A TabResultResponse is an object that holds details on a tab which has been paid from the provided monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.bunqme_tab_result_response.read_bunqme_tab_result_response_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## currency-cloud-payment-quote
<details><summary><code>client.currency_cloud_payment_quote.<a href="src/fern/currency_cloud_payment_quote/client.py">create_currency_cloud_payment_quote_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for managing currency conversions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Pointer

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_cloud_payment_quote.create_currency_cloud_payment_quote_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    pointers=[Pointer()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**pointers:** `typing.Sequence[Pointer]` — The points we want to know the fees for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## currency-conversion
<details><summary><code>client.currency_conversion.<a href="src/fern/currency_conversion/client.py">list_all_currency_conversion_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for managing currency conversions.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_conversion.list_all_currency_conversion_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.currency_conversion.<a href="src/fern/currency_conversion/client.py">read_currency_conversion_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for managing currency conversions.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_conversion.read_currency_conversion_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## currency-conversion-quote
<details><summary><code>client.currency_conversion_quote.<a href="src/fern/currency_conversion_quote/client.py">create_currency_conversion_quote_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to create a quote for currency conversions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Amount, FernApi, Pointer

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_conversion_quote.create_currency_conversion_quote_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    amount=Amount(),
    counterparty_alias=Pointer(),
    currency_source="currency_source",
    currency_target="currency_target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` — The amount to convert.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `Pointer` — The Alias of the party we are transferring the money to.
    
</dd>
</dl>

<dl>
<dd>

**currency_source:** `str` — The currency we are converting.
    
</dd>
</dl>

<dl>
<dd>

**currency_target:** `str` — The currency we are converting towards.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the quote.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.currency_conversion_quote.<a href="src/fern/currency_conversion_quote/client.py">read_currency_conversion_quote_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to create a quote for currency conversions.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_conversion_quote.read_currency_conversion_quote_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.currency_conversion_quote.<a href="src/fern/currency_conversion_quote/client.py">update_currency_conversion_quote_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to create a quote for currency conversions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Amount, FernApi, Pointer

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.currency_conversion_quote.update_currency_conversion_quote_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
    amount=Amount(),
    counterparty_alias=Pointer(),
    currency_source="currency_source",
    currency_target="currency_target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` — The amount to convert.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `Pointer` — The Alias of the party we are transferring the money to.
    
</dd>
</dl>

<dl>
<dd>

**currency_source:** `str` — The currency we are converting.
    
</dd>
</dl>

<dl>
<dd>

**currency_target:** `str` — The currency we are converting towards.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the quote.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## customer-statement
<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">list_all_customer_statement_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.customer_statement.list_all_customer_statement_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">create_customer_statement_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.customer_statement.create_customer_statement_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    date_end="date_end",
    date_start="date_start",
    statement_format="statement_format",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**date_end:** `str` — The end date for making statements.
    
</dd>
</dl>

<dl>
<dd>

**date_start:** `str` — The start date for making statements.
    
</dd>
</dl>

<dl>
<dd>

**statement_format:** `str` — The format type of statement. Allowed values: MT940, CSV, PDF.
    
</dd>
</dl>

<dl>
<dd>

**include_attachment:** `typing.Optional[bool]` — Only for PDF exports. Includes attachments to mutations in the export, such as scanned receipts.
    
</dd>
</dl>

<dl>
<dd>

**regional_format:** `typing.Optional[str]` — Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">read_customer_statement_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.customer_statement.read_customer_statement_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">delete_customer_statement_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.customer_statement.delete_customer_statement_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## draft-payment
<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">list_all_draft_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a listing of all DraftPayments from a given MonetaryAccount.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.draft_payment.list_all_draft_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">create_draft_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new DraftPayment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import DraftPaymentEntry, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.draft_payment.create_draft_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    entries=[DraftPaymentEntry()],
    number_of_required_accepts=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.Sequence[DraftPaymentEntry]` — The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.
    
</dd>
</dl>

<dl>
<dd>

**number_of_required_accepts:** `int` — The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.
    
</dd>
</dl>

<dl>
<dd>

**previous_updated_timestamp:** `typing.Optional[str]` — The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[Schedule]` — The schedule details when creating or updating a scheduled payment.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the DraftPayment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">read_draft_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific DraftPayment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.draft_payment.read_draft_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">update_draft_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a DraftPayment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import DraftPaymentEntry, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.draft_payment.update_draft_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
    entries=[DraftPaymentEntry()],
    number_of_required_accepts=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.Sequence[DraftPaymentEntry]` — The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.
    
</dd>
</dl>

<dl>
<dd>

**number_of_required_accepts:** `int` — The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.
    
</dd>
</dl>

<dl>
<dd>

**previous_updated_timestamp:** `typing.Optional[str]` — The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[Schedule]` — The schedule details when creating or updating a scheduled payment.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the DraftPayment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## statement
<details><summary><code>client.statement.<a href="src/fern/statement/client.py">create_statement_for_user_monetary_account_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create a statement export of a single payment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.statement.create_statement_for_user_monetary_account_event(
    user_id=1,
    monetary_account_id=1,
    event_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExportStatementPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.statement.<a href="src/fern/statement/client.py">read_statement_for_user_monetary_account_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create a statement export of a single payment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.statement.read_statement_for_user_monetary_account_event(
    user_id=1,
    monetary_account_id=1,
    event_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## export-rib
<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">list_all_export_rib_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all the RIBs for a monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_rib.list_all_export_rib_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">create_export_rib_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new RIB.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_rib.create_export_rib_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExportRib` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">read_export_rib_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a RIB for a monetary account by its id.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_rib.read_export_rib_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">delete_export_rib_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create new and read existing RIBs of a monetary account
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.export_rib.delete_export_rib_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ideal-merchant-transaction
<details><summary><code>client.ideal_merchant_transaction.<a href="src/fern/ideal_merchant_transaction/client.py">list_all_ideal_merchant_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View for requesting iDEAL transactions and polling their status.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.ideal_merchant_transaction.list_all_ideal_merchant_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ideal_merchant_transaction.<a href="src/fern/ideal_merchant_transaction/client.py">create_ideal_merchant_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View for requesting iDEAL transactions and polling their status.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.ideal_merchant_transaction.create_ideal_merchant_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[LabelMonetaryAccount]` — The alias of the monetary account to add money to.
    
</dd>
</dl>

<dl>
<dd>

**amount_guaranteed:** `typing.Optional[Amount]` — In case of a successful transaction, the amount of money that will be transferred.
    
</dd>
</dl>

<dl>
<dd>

**amount_requested:** `typing.Optional[Amount]` — The requested amount of money to add.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `typing.Optional[LabelMonetaryAccount]` — The alias of the monetary account the money comes from.
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[str]` — When the transaction will expire.
    
</dd>
</dl>

<dl>
<dd>

**issuer:** `typing.Optional[str]` — The BIC of the issuer.
    
</dd>
</dl>

<dl>
<dd>

**issuer_authentication_url:** `typing.Optional[str]` — The URL to visit to 
    
</dd>
</dl>

<dl>
<dd>

**issuer_name:** `typing.Optional[str]` — The Name of the issuer.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the monetary account this ideal merchant transaction links to.
    
</dd>
</dl>

<dl>
<dd>

**purchase_identifier:** `typing.Optional[str]` — The 'purchase ID' of the iDEAL transaction.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the transaction.
    
</dd>
</dl>

<dl>
<dd>

**status_timestamp:** `typing.Optional[str]` — When the status was last updated.
    
</dd>
</dl>

<dl>
<dd>

**transaction_identifier:** `typing.Optional[str]` — The 'transaction ID' of the iDEAL transaction.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ideal_merchant_transaction.<a href="src/fern/ideal_merchant_transaction/client.py">read_ideal_merchant_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View for requesting iDEAL transactions and polling their status.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.ideal_merchant_transaction.read_ideal_merchant_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## mastercard-action
<details><summary><code>client.mastercard_action.<a href="src/fern/mastercard_action/client.py">list_all_mastercard_action_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

MasterCard transaction view.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.mastercard_action.list_all_mastercard_action_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mastercard_action.<a href="src/fern/mastercard_action/client.py">read_mastercard_action_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

MasterCard transaction view.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.mastercard_action.read_mastercard_action_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## payment
<details><summary><code>client.payment.<a href="src/fern/payment/client.py">list_all_payment_for_user_monetary_account_mastercard_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

MasterCard transaction view.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment.list_all_payment_for_user_monetary_account_mastercard_action(
    user_id=1,
    monetary_account_id=1,
    mastercard_action_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**mastercard_action_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment.<a href="src/fern/payment/client.py">list_all_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a listing of all Payments performed on a given MonetaryAccount (incoming and outgoing).
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment.list_all_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment.<a href="src/fern/payment/client.py">create_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Payment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment.create_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**address_billing:** `typing.Optional[Address]` — A billing Address provided with the Payment, currently unused.
    
</dd>
</dl>

<dl>
<dd>

**address_shipping:** `typing.Optional[Address]` — A shipping Address provided with the Payment, currently unused.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.
    
</dd>
</dl>

<dl>
<dd>

**allow_bunqto:** `typing.Optional[bool]` — Whether or not sending a bunq.to payment is allowed.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[Amount]` — The Amount transferred by the Payment. Will be negative for outgoing Payments and positive for incoming Payments (relative to the MonetaryAccount indicated by monetary_account_id).
    
</dd>
</dl>

<dl>
<dd>

**attachment:** `typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]]` — The Attachments attached to the Payment.
    
</dd>
</dl>

<dl>
<dd>

**balance_after_mutation:** `typing.Optional[Amount]` — The new balance of the monetary account after the mutation.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[int]` — The id of the PaymentBatch if this Payment was part of one.
    
</dd>
</dl>

<dl>
<dd>

**bunqto_expiry:** `typing.Optional[str]` — When bunq.to payment is about to expire.
    
</dd>
</dl>

<dl>
<dd>

**bunqto_share_url:** `typing.Optional[str]` — The status of the bunq.to payment.
    
</dd>
</dl>

<dl>
<dd>

**bunqto_status:** `typing.Optional[str]` — The status of the bunq.to payment.
    
</dd>
</dl>

<dl>
<dd>

**bunqto_sub_status:** `typing.Optional[str]` — The sub status of the bunq.to payment.
    
</dd>
</dl>

<dl>
<dd>

**bunqto_time_responded:** `typing.Optional[str]` — The timestamp of when the bunq.to payment was responded to.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp when the Payment was done.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description for the Payment. Maximum 140 characters for Payments to external IBANs, 9000 characters for Payments to only other bunq MonetaryAccounts.
    
</dd>
</dl>

<dl>
<dd>

**geolocation:** `typing.Optional[Geolocation]` — The Geolocation where the Payment was done from.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the created Payment.
    
</dd>
</dl>

<dl>
<dd>

**merchant_reference:** `typing.Optional[str]` — Optional data included with the Payment specific to the merchant.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the MonetaryAccount the Payment was made to or from (depending on whether this is an incoming or outgoing Payment).
    
</dd>
</dl>

<dl>
<dd>

**payment_auto_allocate_instance:** `typing.Optional[PaymentAutoAllocateInstance]` — A reference to the PaymentAutoAllocateInstance if it exists.
    
</dd>
</dl>

<dl>
<dd>

**request_reference_split_the_bill:** `typing.Optional[typing.Sequence[RequestInquiryReference]]` — The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    
</dd>
</dl>

<dl>
<dd>

**scheduled_id:** `typing.Optional[int]` — The id of the JobScheduled if the Payment was scheduled.
    
</dd>
</dl>

<dl>
<dd>

**sub_type:** `typing.Optional[str]` — The sub-type of the Payment, can be PAYMENT, WITHDRAWAL, REVERSAL, REQUEST, BILLING, SCT, SDD or NLO.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of Payment, can be BUNQ, EBA_SCT, EBA_SDD, IDEAL, SWIFT or FIS (card).
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp when the Payment was last updated (will be updated when chat messages are received).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment.<a href="src/fern/payment/client.py">read_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific previous Payment.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment.read_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## notification-filter-url
<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">list_all_notification_filter_url_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the url notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_url.list_all_notification_filter_url_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">create_notification_filter_url_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the url notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_url.create_notification_filter_url_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**notification_filters:** `typing.Optional[typing.Sequence[NotificationFilterUrl]]` — The types of notifications that will result in a url notification for this monetary account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">list_all_notification_filter_url_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the url notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_url.list_all_notification_filter_url_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">create_notification_filter_url_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the url notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_url.create_notification_filter_url_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**notification_filters:** `typing.Optional[typing.Sequence[NotificationFilterUrl]]` — The types of notifications that will result in a url notification for this user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## payment-auto-allocate
<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">list_all_payment_auto_allocate_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage a users automatic payment auto allocated settings.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_auto_allocate.list_all_payment_auto_allocate_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">create_payment_auto_allocate_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage a users automatic payment auto allocated settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PaymentAutoAllocateDefinition

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_auto_allocate.create_payment_auto_allocate_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    definition=[
        PaymentAutoAllocateDefinition(
            type="type",
        )
    ],
    payment_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**definition:** `typing.Sequence[PaymentAutoAllocateDefinition]` — The definition of how the money should be allocated.
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — The payment that should be used to define the triggers for the payment auto allocate.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — Whether a payment should be sorted ONCE or RECURRING.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">read_payment_auto_allocate_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage a users automatic payment auto allocated settings.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_auto_allocate.read_payment_auto_allocate_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">update_payment_auto_allocate_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage a users automatic payment auto allocated settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PaymentAutoAllocateDefinition

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_auto_allocate.update_payment_auto_allocate_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
    definition=[
        PaymentAutoAllocateDefinition(
            type="type",
        )
    ],
    payment_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**definition:** `typing.Sequence[PaymentAutoAllocateDefinition]` — The definition of how the money should be allocated.
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `int` — The payment that should be used to define the triggers for the payment auto allocate.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — Whether a payment should be sorted ONCE or RECURRING.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">delete_payment_auto_allocate_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage a users automatic payment auto allocated settings.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_auto_allocate.delete_payment_auto_allocate_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">list_all_payment_auto_allocate_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a users automatic payment auto allocated settings.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_auto_allocate.list_all_payment_auto_allocate_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## definition
<details><summary><code>client.definition.<a href="src/fern/definition/client.py">list_all_definition_for_user_monetary_account_payment_auto_allocate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all the definitions in a payment auto allocate.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.definition.list_all_definition_for_user_monetary_account_payment_auto_allocate(
    user_id=1,
    monetary_account_id=1,
    payment_auto_allocate_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_auto_allocate_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## instance
<details><summary><code>client.instance.<a href="src/fern/instance/client.py">list_all_instance_for_user_monetary_account_payment_auto_allocate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all the times a users payment was automatically allocated.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.instance.list_all_instance_for_user_monetary_account_payment_auto_allocate(
    user_id=1,
    monetary_account_id=1,
    payment_auto_allocate_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_auto_allocate_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instance.<a href="src/fern/instance/client.py">read_instance_for_user_monetary_account_payment_auto_allocate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all the times a users payment was automatically allocated.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.instance.read_instance_for_user_monetary_account_payment_auto_allocate(
    user_id=1,
    monetary_account_id=1,
    payment_auto_allocate_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment_auto_allocate_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## payment-batch
<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">list_all_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all the payment batches for a monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_batch.list_all_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">create_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a payment batch by sending an array of single payment objects, that will become part of the batch.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_batch.create_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payments:** `typing.Optional[PaymentBatchAnchoredPayment]` — The list of mutations that were made.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">read_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the details of a specific payment batch.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_batch.read_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">update_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a bunq.to payment batch. The status of all the payments will be set to REVOKED.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_batch.update_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payments:** `typing.Optional[PaymentBatchAnchoredPayment]` — The list of mutations that were made.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## request-inquiry
<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">list_all_request_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all payment requests for a user's monetary account. bunqme_share_url is always null if the counterparty is a bunq user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry.list_all_request_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">create_request_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new payment request.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry.create_request_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id_=1,
    allow_bunqme=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**allow_bunqme:** `bool` — Whether or not sending a bunq.me request is allowed.
    
</dd>
</dl>

<dl>
<dd>

**address_billing:** `typing.Optional[Address]` — The billing address provided by the accepting user if an address was requested.
    
</dd>
</dl>

<dl>
<dd>

**address_shipping:** `typing.Optional[Address]` — The shipping address provided by the accepting user if an address was requested.
    
</dd>
</dl>

<dl>
<dd>

**allow_amount_higher:** `typing.Optional[bool]` — [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**allow_amount_lower:** `typing.Optional[bool]` — [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**amount_inquired:** `typing.Optional[Amount]` — The requested amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_responded:** `typing.Optional[Amount]` — The responded amount.
    
</dd>
</dl>

<dl>
<dd>

**attachment:** `typing.Optional[typing.Sequence[BunqId]]` — The attachments attached to the payment.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[int]` — The id of the batch if the request was part of a batch.
    
</dd>
</dl>

<dl>
<dd>

**bunqme_share_url:** `typing.Optional[str]` — The url that points to the bunq.me request.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp of the payment request's creation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the inquiry.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[int]` — The ID of the associated event if the request was made using 'split the bill'.
    
</dd>
</dl>

<dl>
<dd>

**geolocation:** `typing.Optional[Geolocation]` — The geolocation where the payment was done.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the created RequestInquiry.
    
</dd>
</dl>

<dl>
<dd>

**merchant_reference:** `typing.Optional[str]` — The client's custom reference that was attached to the request and the mutation.
    
</dd>
</dl>

<dl>
<dd>

**minimum_age:** `typing.Optional[int]` — The minimum age the user accepting the RequestInquiry must have.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the monetary account the request response applies to.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — The URL which the user is sent to after accepting or rejecting the Request.
    
</dd>
</dl>

<dl>
<dd>

**reference_split_the_bill:** `typing.Optional[RequestReferenceSplitTheBillAnchorObject]` — The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction
    
</dd>
</dl>

<dl>
<dd>

**require_address:** `typing.Optional[str]` — Whether or not an address must be provided on accept.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_id:** `typing.Optional[int]` — The id of the scheduled job if the request was scheduled.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the request.
    
</dd>
</dl>

<dl>
<dd>

**time_expiry:** `typing.Optional[str]` — The timestamp of when the payment request expired.
    
</dd>
</dl>

<dl>
<dd>

**time_responded:** `typing.Optional[str]` — The timestamp of when the payment request was responded to.
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp of the payment request's last update.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_created:** `typing.Optional[LabelUser]` — The label that's displayed to the counterparty with the mutation. Includes user.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_revoked:** `typing.Optional[LabelUser]` — The label that's displayed to the counterparty with the mutation. Includes user.
    
</dd>
</dl>

<dl>
<dd>

**want_tip:** `typing.Optional[bool]` — [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">read_request_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details of a specific payment request, including its status. bunqme_share_url is always null if the counterparty is a bunq user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry.read_request_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">update_request_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a request for payment, by updating the status to REVOKED.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry.update_request_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id_=1,
    item_id=1,
    allow_bunqme=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**allow_bunqme:** `bool` — Whether or not sending a bunq.me request is allowed.
    
</dd>
</dl>

<dl>
<dd>

**address_billing:** `typing.Optional[Address]` — The billing address provided by the accepting user if an address was requested.
    
</dd>
</dl>

<dl>
<dd>

**address_shipping:** `typing.Optional[Address]` — The shipping address provided by the accepting user if an address was requested.
    
</dd>
</dl>

<dl>
<dd>

**allow_amount_higher:** `typing.Optional[bool]` — [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**allow_amount_lower:** `typing.Optional[bool]` — [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**amount_inquired:** `typing.Optional[Amount]` — The requested amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_responded:** `typing.Optional[Amount]` — The responded amount.
    
</dd>
</dl>

<dl>
<dd>

**attachment:** `typing.Optional[typing.Sequence[BunqId]]` — The attachments attached to the payment.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[int]` — The id of the batch if the request was part of a batch.
    
</dd>
</dl>

<dl>
<dd>

**bunqme_share_url:** `typing.Optional[str]` — The url that points to the bunq.me request.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp of the payment request's creation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the inquiry.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[int]` — The ID of the associated event if the request was made using 'split the bill'.
    
</dd>
</dl>

<dl>
<dd>

**geolocation:** `typing.Optional[Geolocation]` — The geolocation where the payment was done.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the created RequestInquiry.
    
</dd>
</dl>

<dl>
<dd>

**merchant_reference:** `typing.Optional[str]` — The client's custom reference that was attached to the request and the mutation.
    
</dd>
</dl>

<dl>
<dd>

**minimum_age:** `typing.Optional[int]` — The minimum age the user accepting the RequestInquiry must have.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the monetary account the request response applies to.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — The URL which the user is sent to after accepting or rejecting the Request.
    
</dd>
</dl>

<dl>
<dd>

**reference_split_the_bill:** `typing.Optional[RequestReferenceSplitTheBillAnchorObject]` — The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction
    
</dd>
</dl>

<dl>
<dd>

**require_address:** `typing.Optional[str]` — Whether or not an address must be provided on accept.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_id:** `typing.Optional[int]` — The id of the scheduled job if the request was scheduled.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the request.
    
</dd>
</dl>

<dl>
<dd>

**time_expiry:** `typing.Optional[str]` — The timestamp of when the payment request expired.
    
</dd>
</dl>

<dl>
<dd>

**time_responded:** `typing.Optional[str]` — The timestamp of when the payment request was responded to.
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp of the payment request's last update.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_created:** `typing.Optional[LabelUser]` — The label that's displayed to the counterparty with the mutation. Includes user.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_revoked:** `typing.Optional[LabelUser]` — The label that's displayed to the counterparty with the mutation. Includes user.
    
</dd>
</dl>

<dl>
<dd>

**want_tip:** `typing.Optional[bool]` — [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## request-inquiry-batch
<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">list_all_request_inquiry_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all the request batches for a monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry_batch.list_all_request_inquiry_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">create_request_inquiry_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request batch by sending an array of single request objects, that will become part of the batch.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry_batch.create_request_inquiry_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[int]` — The ID of the associated event if the request batch was made using 'split the bill'.
    
</dd>
</dl>

<dl>
<dd>

**reference_split_the_bill:** `typing.Optional[RequestReferenceSplitTheBillAnchorObject]` — The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction
    
</dd>
</dl>

<dl>
<dd>

**request_inquiries:** `typing.Optional[typing.Sequence[RequestInquiry]]` — The list of requests that were made.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the request.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_inquired:** `typing.Optional[Amount]` — The total amount originally inquired for this batch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">read_request_inquiry_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the details of a specific request batch.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry_batch.read_request_inquiry_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">update_request_inquiry_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a request batch. The status of all the requests will be set to REVOKED.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_inquiry_batch.update_request_inquiry_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[int]` — The ID of the associated event if the request batch was made using 'split the bill'.
    
</dd>
</dl>

<dl>
<dd>

**reference_split_the_bill:** `typing.Optional[RequestReferenceSplitTheBillAnchorObject]` — The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction
    
</dd>
</dl>

<dl>
<dd>

**request_inquiries:** `typing.Optional[typing.Sequence[RequestInquiry]]` — The list of requests that were made.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the request.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_inquired:** `typing.Optional[Amount]` — The total amount originally inquired for this batch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## request-response
<details><summary><code>client.request_response.<a href="src/fern/request_response/client.py">list_all_request_response_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all RequestResponses for a MonetaryAccount.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_response.list_all_request_response_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_response.<a href="src/fern/request_response/client.py">read_request_response_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details for a specific existing RequestResponse.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_response.read_request_response_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_response.<a href="src/fern/request_response/client.py">update_request_response_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status to accept or reject the RequestResponse.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.request_response.update_request_response_for_user_monetary_account(
    user_id=1,
    monetary_account_id_=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**address_billing:** `typing.Optional[Address]` — The billing address provided by the accepting user if an address was requested.
    
</dd>
</dl>

<dl>
<dd>

**address_shipping:** `typing.Optional[Address]` — The shipping address provided by the accepting user if an address was requested.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount with the public information of the MonetaryAccount this RequestResponse was received on.
    
</dd>
</dl>

<dl>
<dd>

**amount_inquired:** `typing.Optional[Amount]` — The requested Amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_responded:** `typing.Optional[Amount]` — The Amount the RequestResponse was accepted with.
    
</dd>
</dl>

<dl>
<dd>

**attachment:** `typing.Optional[typing.Sequence[Attachment]]` — The Attachments attached to the RequestResponse.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount with the public information of the MonetaryAccount that is requesting money with this RequestResponse.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp when the Request Response was created.
    
</dd>
</dl>

<dl>
<dd>

**credit_scheme_identifier:** `typing.Optional[str]` — The credit scheme id provided by the counterparty for DIRECT_DEBIT inquiries.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description for the RequestResponse provided by the requesting party. Maximum 9000 characters.
    
</dd>
</dl>

<dl>
<dd>

**eligible_whitelist_id:** `typing.Optional[int]` — The whitelist id for this action or null.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[int]` — The ID of the latest event for the request.
    
</dd>
</dl>

<dl>
<dd>

**geolocation:** `typing.Optional[Geolocation]` — The Geolocation where the RequestResponse was created.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the Request Response.
    
</dd>
</dl>

<dl>
<dd>

**mandate_identifier:** `typing.Optional[str]` — The mandate id provided by the counterparty for DIRECT_DEBIT inquiries.
    
</dd>
</dl>

<dl>
<dd>

**minimum_age:** `typing.Optional[int]` — The minimum age the user accepting the RequestResponse must have.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the MonetaryAccount the RequestResponse was received on.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — The URL which the user is sent to after accepting or rejecting the Request.
    
</dd>
</dl>

<dl>
<dd>

**request_reference_split_the_bill:** `typing.Optional[typing.Sequence[RequestInquiryReference]]` — The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    
</dd>
</dl>

<dl>
<dd>

**require_address:** `typing.Optional[str]` — Whether or not an address must be provided on accept.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the RequestResponse. Can be ACCEPTED, PENDING, REJECTED, REFUND_REQUESTED, REFUNDED or REVOKED.
    
</dd>
</dl>

<dl>
<dd>

**sub_type:** `typing.Optional[str]` — The subtype of the RequestInquiry. Can be ONCE or RECURRING for DIRECT_DEBIT RequestInquiries and NONE for all other.
    
</dd>
</dl>

<dl>
<dd>

**time_expiry:** `typing.Optional[str]` — The timestamp of when the RequestResponse expired or will expire.
    
</dd>
</dl>

<dl>
<dd>

**time_refund_requested:** `typing.Optional[str]` — The timestamp of when a refund request for the RequestResponse was claimed.
    
</dd>
</dl>

<dl>
<dd>

**time_refunded:** `typing.Optional[str]` — The timestamp of when the RequestResponse was refunded.
    
</dd>
</dl>

<dl>
<dd>

**time_responded:** `typing.Optional[str]` — The timestamp of when the RequestResponse was responded to.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of the RequestInquiry. Can be DIRECT_DEBIT, DIRECT_DEBIT_B2B, IDEAL, SOFORT or INTERNAL.
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp when the Request Response was last updated (will be updated when chat messages are received).
    
</dd>
</dl>

<dl>
<dd>

**user_refund_requested:** `typing.Optional[LabelUser]` — The label of the user that requested the refund.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## schedule
<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">list_all_schedule_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collection of scheduled definition for a given monetary account. You can add the parameter type to filter the response. When type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is provided only schedule definition object that relate to these definitions are returned.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule.list_all_schedule_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">read_schedule_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific schedule definition for a given monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule.read_schedule_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">list_all_schedule_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collection of scheduled definition for all accessible monetary accounts of the user. You can add the parameter type to filter the response. When type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is provided only schedule definition object that relate to these definitions are returned.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule.list_all_schedule_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## schedule-payment
<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">list_all_schedule_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment.list_all_schedule_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">create_schedule_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment.create_schedule_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment:** `typing.Optional[SchedulePaymentEntry]` — The payment details.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[Schedule]` — The schedule details.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The schedule status, options: ACTIVE, FINISHED, CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">read_schedule_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment.read_schedule_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">update_schedule_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment.update_schedule_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payment:** `typing.Optional[SchedulePaymentEntry]` — The payment details.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[Schedule]` — The schedule details.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The schedule status, options: ACTIVE, FINISHED, CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">delete_schedule_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment.delete_schedule_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## schedule-payment-batch
<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">create_schedule_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payment batches.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment_batch.create_schedule_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payments:** `typing.Optional[typing.Sequence[SchedulePaymentEntry]]` — The payment details.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[Schedule]` — The schedule details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">read_schedule_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payment batches.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment_batch.read_schedule_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">update_schedule_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payment batches.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment_batch.update_schedule_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**payments:** `typing.Optional[typing.Sequence[SchedulePaymentEntry]]` — The payment details.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[Schedule]` — The schedule details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">delete_schedule_payment_batch_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint for schedule payment batches.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_payment_batch.delete_schedule_payment_batch_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## schedule-instance
<details><summary><code>client.schedule_instance.<a href="src/fern/schedule_instance/client.py">list_all_schedule_instance_for_user_monetary_account_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

view for reading, updating and listing the scheduled instance.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_instance.list_all_schedule_instance_for_user_monetary_account_schedule(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_instance.<a href="src/fern/schedule_instance/client.py">read_schedule_instance_for_user_monetary_account_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

view for reading, updating and listing the scheduled instance.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_instance.read_schedule_instance_for_user_monetary_account_schedule(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_instance.<a href="src/fern/schedule_instance/client.py">update_schedule_instance_for_user_monetary_account_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

view for reading, updating and listing the scheduled instance.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.schedule_instance.update_schedule_instance_for_user_monetary_account_schedule(
    user_id=1,
    monetary_account_id=1,
    schedule_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**error_message:** `typing.Optional[typing.Sequence[Error]]` — The message when the scheduled instance has run and failed due to user error.
    
</dd>
</dl>

<dl>
<dd>

**request_reference_split_the_bill:** `typing.Optional[typing.Sequence[RequestInquiryReference]]` — The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    
</dd>
</dl>

<dl>
<dd>

**result_object:** `typing.Optional[ScheduleInstanceAnchorObject]` — The result object of this schedule instance. (Payment, PaymentBatch)
    
</dd>
</dl>

<dl>
<dd>

**scheduled_object:** `typing.Optional[ScheduleAnchorObject]` — The scheduled object. (Payment, PaymentBatch)
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — The state of the scheduleInstance. (FINISHED_SUCCESSFULLY, RETRY, FAILED_USER_ERROR)
    
</dd>
</dl>

<dl>
<dd>

**time_end:** `typing.Optional[str]` — The schedule end time (UTC).
    
</dd>
</dl>

<dl>
<dd>

**time_start:** `typing.Optional[str]` — The schedule start time (UTC).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## share-invite-monetary-account-inquiry
<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">list_all_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[DEPRECATED - use /share-invite-monetary-account-response] Get a list with all the share inquiries for a monetary account, only if the requesting user has permission to change the details of the various ones.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.share_invite_monetary_account_inquiry.list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">create_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[DEPRECATED - use /share-invite-monetary-account-response] Create a new share inquiry for a monetary account, specifying the permission the other bunq user will have on it.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.share_invite_monetary_account_inquiry.create_share_invite_monetary_account_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**access_type:** `typing.Optional[str]` — Type of access that is in place.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[LabelMonetaryAccount]` — The label of the monetary account that's being shared.
    
</dd>
</dl>

<dl>
<dd>

**counter_user_alias:** `typing.Optional[LabelUser]` — The label of the user to share with.
    
</dd>
</dl>

<dl>
<dd>

**draft_share_invite_bank_id:** `typing.Optional[int]` — DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the newly created share invite.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the monetary account the share applies to.
    
</dd>
</dl>

<dl>
<dd>

**relationship:** `typing.Optional[str]` — The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc
    
</dd>
</dl>

<dl>
<dd>

**share_detail:** `typing.Optional[ShareDetail]` — DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.
    
</dd>
</dl>

<dl>
<dd>

**share_type:** `typing.Optional[str]` — DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — DEPRECATED: USE `access_type` INSTEAD | The start date of this share.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the share. Can be ACTIVE, REVOKED, REJECTED.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_created:** `typing.Optional[LabelUser]` — The user who created the share.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_revoked:** `typing.Optional[LabelUser]` — The user who revoked the share.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">read_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[DEPRECATED - use /share-invite-monetary-account-response] Get the details of a specific share inquiry.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.share_invite_monetary_account_inquiry.read_share_invite_monetary_account_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">update_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[DEPRECATED - use /share-invite-monetary-account-response] Update the details of a share. This includes updating status (revoking or cancelling it), granted permission and validity period of this share.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.share_invite_monetary_account_inquiry.update_share_invite_monetary_account_inquiry_for_user_monetary_account(
    user_id=1,
    monetary_account_id_=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id_:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**access_type:** `typing.Optional[str]` — Type of access that is in place.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[LabelMonetaryAccount]` — The label of the monetary account that's being shared.
    
</dd>
</dl>

<dl>
<dd>

**counter_user_alias:** `typing.Optional[LabelUser]` — The label of the user to share with.
    
</dd>
</dl>

<dl>
<dd>

**draft_share_invite_bank_id:** `typing.Optional[int]` — DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the newly created share invite.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the monetary account the share applies to.
    
</dd>
</dl>

<dl>
<dd>

**relationship:** `typing.Optional[str]` — The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc
    
</dd>
</dl>

<dl>
<dd>

**share_detail:** `typing.Optional[ShareDetail]` — DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.
    
</dd>
</dl>

<dl>
<dd>

**share_type:** `typing.Optional[str]` — DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — DEPRECATED: USE `access_type` INSTEAD | The start date of this share.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the share. Can be ACTIVE, REVOKED, REJECTED.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_created:** `typing.Optional[LabelUser]` — The user who created the share.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_revoked:** `typing.Optional[LabelUser]` — The user who revoked the share.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sofort-merchant-transaction
<details><summary><code>client.sofort_merchant_transaction.<a href="src/fern/sofort_merchant_transaction/client.py">list_all_sofort_merchant_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View for requesting Sofort transactions and polling their status.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.sofort_merchant_transaction.list_all_sofort_merchant_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sofort_merchant_transaction.<a href="src/fern/sofort_merchant_transaction/client.py">read_sofort_merchant_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View for requesting Sofort transactions and polling their status.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.sofort_merchant_transaction.read_sofort_merchant_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## switch-service-payment
<details><summary><code>client.switch_service_payment.<a href="src/fern/switch_service_payment/client.py">read_switch_service_payment_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An incoming payment made towards an account of an external bank and redirected to a bunq account via switch service.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.switch_service_payment.read_switch_service_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## translink-transaction
<details><summary><code>client.translink_transaction.<a href="src/fern/translink_transaction/client.py">list_all_translink_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create translink transactions.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.translink_transaction.list_all_translink_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.translink_transaction.<a href="src/fern/translink_transaction/client.py">create_translink_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create translink transactions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Payment

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.translink_transaction.create_translink_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    description="description",
    payments=[Payment()],
    reference="reference",
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the payment request.
    
</dd>
</dl>

<dl>
<dd>

**payments:** `typing.Sequence[Payment]` — The list of payments we want to send in a single transaction.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `str` — The request reference.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — Type of transaction, can be TRIP, REFUND, WITHDRAWAL or TOP_UP.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.translink_transaction.<a href="src/fern/translink_transaction/client.py">read_translink_transaction_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create translink transactions.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.translink_transaction.read_translink_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## whitelist-sdd
<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">list_all_whitelist_sdd_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a listing of all SDD whitelist entries for a target monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd.list_all_whitelist_sdd_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">read_whitelist_sdd_for_user_monetary_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific SDD whitelist entry.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd.read_whitelist_sdd_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">list_all_whitelist_sdd_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a listing of all recurring SDD whitelist entries for a target monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd.list_all_whitelist_sdd_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">read_whitelist_sdd_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific recurring SDD whitelist entry.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd.read_whitelist_sdd_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## notification-filter-email
<details><summary><code>client.notification_filter_email.<a href="src/fern/notification_filter_email/client.py">list_all_notification_filter_email_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the email notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_email.list_all_notification_filter_email_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_filter_email.<a href="src/fern/notification_filter_email/client.py">create_notification_filter_email_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the email notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_email.create_notification_filter_email_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**notification_filters:** `typing.Optional[typing.Sequence[NotificationFilterEmail]]` — The types of notifications that will result in a email notification for this user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## notification-filter-push
<details><summary><code>client.notification_filter_push.<a href="src/fern/notification_filter_push/client.py">list_all_notification_filter_push_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the push notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_push.list_all_notification_filter_push_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_filter_push.<a href="src/fern/notification_filter_push/client.py">create_notification_filter_push_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the push notification filters for a user.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.notification_filter_push.create_notification_filter_push_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**notification_filters:** `typing.Optional[typing.Sequence[NotificationFilterPush]]` — The types of notifications that will result in a push notification for this user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## oauth-client
<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">list_all_oauth_client_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Clients.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.oauth_client.list_all_oauth_client_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">create_oauth_client_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Clients.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.oauth_client.create_oauth_client_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the Oauth Client, can be ACTIVE or CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">read_oauth_client_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Clients.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.oauth_client.read_oauth_client_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">update_oauth_client_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Clients.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.oauth_client.update_oauth_client_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the Oauth Client, can be ACTIVE or CANCELLED.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## callback-url
<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">list_all_callback_url_for_user_oauth_client</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Client Callback URLs.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.callback_url.list_all_callback_url_for_user_oauth_client(
    user_id=1,
    oauth_client_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**oauth_client_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">create_callback_url_for_user_oauth_client</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Client Callback URLs.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.callback_url.create_callback_url_for_user_oauth_client(
    user_id=1,
    oauth_client_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**oauth_client_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL for this callback.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">read_callback_url_for_user_oauth_client</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Client Callback URLs.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.callback_url.read_callback_url_for_user_oauth_client(
    user_id=1,
    oauth_client_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**oauth_client_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">update_callback_url_for_user_oauth_client</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Client Callback URLs.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.callback_url.update_callback_url_for_user_oauth_client(
    user_id=1,
    oauth_client_id=1,
    item_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**oauth_client_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL for this callback.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">delete_callback_url_for_user_oauth_client</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used for managing OAuth Client Callback URLs.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.callback_url.delete_callback_url_for_user_oauth_client(
    user_id=1,
    oauth_client_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**oauth_client_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## payment-service-provider-draft-payment
<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">list_all_payment_service_provider_draft_payment_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the PaymentServiceProviderDraftPayment's for a PISP.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_service_provider_draft_payment.list_all_payment_service_provider_draft_payment_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">create_payment_service_provider_draft_payment_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the PaymentServiceProviderDraftPayment's for a PISP.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Amount, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_service_provider_draft_payment.create_payment_service_provider_draft_payment_for_user(
    user_id=1,
    amount=Amount(),
    counterparty_iban="counterparty_iban",
    counterparty_name="counterparty_name",
    description="description",
    sender_iban="sender_iban",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` — The Amount to transfer with the Payment. Must be bigger than 0.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_iban:** `str` — The IBAN of the counterparty.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_name:** `str` — The name of the counterparty.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the payment.
    
</dd>
</dl>

<dl>
<dd>

**sender_iban:** `str` — The IBAN of the sender.
    
</dd>
</dl>

<dl>
<dd>

**sender_name:** `typing.Optional[str]` — The name of the sender.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">read_payment_service_provider_draft_payment_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the PaymentServiceProviderDraftPayment's for a PISP.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_service_provider_draft_payment.read_payment_service_provider_draft_payment_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">update_payment_service_provider_draft_payment_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage the PaymentServiceProviderDraftPayment's for a PISP.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import Amount, FernApi

client = FernApi(
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.payment_service_provider_draft_payment.update_payment_service_provider_draft_payment_for_user(
    user_id=1,
    item_id=1,
    amount=Amount(),
    counterparty_iban="counterparty_iban",
    counterparty_name="counterparty_name",
    description="description",
    sender_iban="sender_iban",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `Amount` — The Amount to transfer with the Payment. Must be bigger than 0.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_iban:** `str` — The IBAN of the counterparty.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_name:** `str` — The name of the counterparty.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the payment.
    
</dd>
</dl>

<dl>
<dd>

**sender_iban:** `str` — The IBAN of the sender.
    
</dd>
</dl>

<dl>
<dd>

**sender_name:** `typing.Optional[str]` — The name of the sender.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## registry-settlement
<details><summary><code>client.registry_settlement.<a href="src/fern/registry_settlement/client.py">list_all_registry_settlement_for_user_registry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a listing of all Slice group settlements.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.registry_settlement.list_all_registry_settlement_for_user_registry(
    user_id=1,
    registry_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**registry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry_settlement.<a href="src/fern/registry_settlement/client.py">create_registry_settlement_for_user_registry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Slice group settlement.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.registry_settlement.create_registry_settlement_for_user_registry(
    user_id=1,
    registry_id=1,
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**registry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RegistrySettlement` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry_settlement.<a href="src/fern/registry_settlement/client.py">read_registry_settlement_for_user_registry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific Slice group settlement.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.registry_settlement.read_registry_settlement_for_user_registry(
    user_id=1,
    registry_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**registry_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## reward
<details><summary><code>client.reward.<a href="src/fern/reward/client.py">list_all_reward_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view Rewards.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.reward.list_all_reward_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward.<a href="src/fern/reward/client.py">read_reward_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view Rewards.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.reward.read_reward_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## reward-recipient
<details><summary><code>client.reward_recipient.<a href="src/fern/reward_recipient/client.py">list_all_reward_recipient_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view Rewards.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.reward_recipient.list_all_reward_recipient_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward_recipient.<a href="src/fern/reward_recipient/client.py">read_reward_recipient_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view Rewards.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.reward_recipient.read_reward_recipient_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## reward-sender
<details><summary><code>client.reward_sender.<a href="src/fern/reward_sender/client.py">list_all_reward_sender_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view Rewards.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.reward_sender.list_all_reward_sender_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reward_sender.<a href="src/fern/reward_sender/client.py">read_reward_sender_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to view Rewards.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.reward_sender.read_reward_sender_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## share-invite-monetary-account-response
<details><summary><code>client.share_invite_monetary_account_response.<a href="src/fern/share_invite_monetary_account_response/client.py">list_all_share_invite_monetary_account_response_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all the shares a user was invited to.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.share_invite_monetary_account_response.list_all_share_invite_monetary_account_response_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.share_invite_monetary_account_response.<a href="src/fern/share_invite_monetary_account_response/client.py">read_share_invite_monetary_account_response_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the details of a specific share a user was invited to.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.share_invite_monetary_account_response.read_share_invite_monetary_account_response_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.share_invite_monetary_account_response.<a href="src/fern/share_invite_monetary_account_response/client.py">update_share_invite_monetary_account_response_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accept or reject a share a user was invited to.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.share_invite_monetary_account_response.update_share_invite_monetary_account_response_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**access_type:** `typing.Optional[str]` — Type of access that is wanted, one of VIEW_BALANCE, VIEW_TRANSACTION, DRAFT_PAYMENT or FULL_TRANSIENT
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `typing.Optional[int]` — The card to link to the shared monetary account. Used only if share_detail is ShareDetailCardPayment.
    
</dd>
</dl>

<dl>
<dd>

**counter_alias:** `typing.Optional[LabelMonetaryAccount]` — The monetary account and user who created the share.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp of the ShareInviteBankResponse creation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of this share. It is basically the monetary account description.
    
</dd>
</dl>

<dl>
<dd>

**draft_share_invite_bank_id:** `typing.Optional[int]` — The id of the draft share invite bank.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — The expiration date of this share.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the ShareInviteBankResponse.
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `typing.Optional[int]` — The id of the monetary account the ACCEPTED share applies to. null otherwise.
    
</dd>
</dl>

<dl>
<dd>

**relation_user:** `typing.Optional[RelationUser]` — All of the relation users towards this MA.
    
</dd>
</dl>

<dl>
<dd>

**share_detail:** `typing.Optional[ShareDetail]` — The share details.
    
</dd>
</dl>

<dl>
<dd>

**share_type:** `typing.Optional[str]` — The share type, either STANDARD or MUTUAL.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — The start date of this share.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of the share. Can be ACTIVE, REVOKED, REJECTED.
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp of the ShareInviteBankResponse last update.
    
</dd>
</dl>

<dl>
<dd>

**user_alias_cancelled:** `typing.Optional[LabelUser]` — The user who cancelled the share if it has been revoked or rejected.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## token-qr-request-ideal
<details><summary><code>client.token_qr_request_ideal.<a href="src/fern/token_qr_request_ideal/client.py">create_token_qr_request_ideal_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request from an ideal transaction.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.token_qr_request_ideal.create_token_qr_request_ideal_for_user(
    user_id=1,
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The token passed from a site or read from a QR code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## token-qr-request-sofort
<details><summary><code>client.token_qr_request_sofort.<a href="src/fern/token_qr_request_sofort/client.py">create_token_qr_request_sofort_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request from an SOFORT transaction.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.token_qr_request_sofort.create_token_qr_request_sofort_for_user(
    user_id=1,
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The token passed from a site or read from a QR code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-currency
<details><summary><code>client.transferwise_currency.<a href="src/fern/transferwise_currency/client.py">list_all_transferwise_currency_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get a list of supported currencies for Transferwise.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_currency.list_all_transferwise_currency_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-quote
<details><summary><code>client.transferwise_quote.<a href="src/fern/transferwise_quote/client.py">create_transferwise_quote_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get quotes from Transferwise. These can be used to initiate payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_quote.create_transferwise_quote_for_user(
    user_id=1,
    currency_source="currency_source",
    currency_target="currency_target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**currency_source:** `str` — The source currency.
    
</dd>
</dl>

<dl>
<dd>

**currency_target:** `str` — The target currency.
    
</dd>
</dl>

<dl>
<dd>

**amount_fee:** `typing.Optional[Amount]` — The fee amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_source:** `typing.Optional[Amount]` — The source amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_target:** `typing.Optional[Amount]` — The target amount.
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` — The timestamp of the quote's creation.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — The id of the quote.
    
</dd>
</dl>

<dl>
<dd>

**quote_id:** `typing.Optional[str]` — The quote id Transferwise needs.
    
</dd>
</dl>

<dl>
<dd>

**rate:** `typing.Optional[str]` — The rate.
    
</dd>
</dl>

<dl>
<dd>

**time_delivery_estimate:** `typing.Optional[str]` — The estimated delivery time.
    
</dd>
</dl>

<dl>
<dd>

**time_expiry:** `typing.Optional[str]` — The expiration timestamp of the quote.
    
</dd>
</dl>

<dl>
<dd>

**updated:** `typing.Optional[str]` — The timestamp of the quote's last update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_quote.<a href="src/fern/transferwise_quote/client.py">read_transferwise_quote_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get quotes from Transferwise. These can be used to initiate payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_quote.read_transferwise_quote_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-quote-temporary
<details><summary><code>client.transferwise_quote_temporary.<a href="src/fern/transferwise_quote_temporary/client.py">create_transferwise_quote_temporary_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get temporary quotes from Transferwise. These cannot be used to initiate payments
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_quote_temporary.create_transferwise_quote_temporary_for_user(
    user_id=1,
    currency_source="currency_source",
    currency_target="currency_target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**currency_source:** `str` — The source currency.
    
</dd>
</dl>

<dl>
<dd>

**currency_target:** `str` — The target currency.
    
</dd>
</dl>

<dl>
<dd>

**amount_source:** `typing.Optional[Amount]` — The source amount. Required if target amount is left empty.
    
</dd>
</dl>

<dl>
<dd>

**amount_target:** `typing.Optional[Amount]` — The target amount. Required if source amount is left empty.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_quote_temporary.<a href="src/fern/transferwise_quote_temporary/client.py">read_transferwise_quote_temporary_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get temporary quotes from Transferwise. These cannot be used to initiate payments
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_quote_temporary.read_transferwise_quote_temporary_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-recipient
<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">list_all_transferwise_recipient_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage recipient accounts with Transferwise.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_recipient.list_all_transferwise_recipient_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">create_transferwise_recipient_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage recipient accounts with Transferwise.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_recipient.create_transferwise_recipient_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
    name_account_holder="name_account_holder",
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**name_account_holder:** `str` — The name of the account holder.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The chosen recipient account type. The possible options are provided dynamically in the response endpoint.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — The country of the receiving account.
    
</dd>
</dl>

<dl>
<dd>

**detail:** `typing.Optional[typing.Sequence[TransferwiseRequirementField]]` — The fields which were specified as "required" and have since been filled by the user. Always provide the full list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">read_transferwise_recipient_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage recipient accounts with Transferwise.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_recipient.read_transferwise_recipient_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">delete_transferwise_recipient_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage recipient accounts with Transferwise.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_recipient.delete_transferwise_recipient_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-recipient-requirement
<details><summary><code>client.transferwise_recipient_requirement.<a href="src/fern/transferwise_recipient_requirement/client.py">list_all_transferwise_recipient_requirement_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to determine the recipient account requirements for Transferwise transfers.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_recipient_requirement.list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_recipient_requirement.<a href="src/fern/transferwise_recipient_requirement/client.py">create_transferwise_recipient_requirement_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to determine the recipient account requirements for Transferwise transfers.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_recipient_requirement.create_transferwise_recipient_requirement_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
    name_account_holder="name_account_holder",
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**name_account_holder:** `str` — The name of the account holder.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The chosen recipient account type. The possible options are provided dynamically in the response endpoint.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — The country of the receiving account.
    
</dd>
</dl>

<dl>
<dd>

**detail:** `typing.Optional[typing.Sequence[TransferwiseRequirementField]]` — The fields which were specified as "required" and have since been filled by the user. Always provide the full list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-transfer
<details><summary><code>client.transferwise_transfer.<a href="src/fern/transferwise_transfer/client.py">list_all_transferwise_transfer_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create Transferwise payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_transfer.list_all_transferwise_transfer_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_transfer.<a href="src/fern/transferwise_transfer/client.py">create_transferwise_transfer_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create Transferwise payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_transfer.create_transferwise_transfer_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
    monetary_account_id="monetary_account_id",
    recipient_id="recipient_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_id:** `str` — The id of the monetary account the payment should be made from.
    
</dd>
</dl>

<dl>
<dd>

**recipient_id:** `str` — The id of the target account.
    
</dd>
</dl>

<dl>
<dd>

**alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.
    
</dd>
</dl>

<dl>
<dd>

**amount_source:** `typing.Optional[Amount]` — The source amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_target:** `typing.Optional[Amount]` — The target amount.
    
</dd>
</dl>

<dl>
<dd>

**counterparty_alias:** `typing.Optional[LabelMonetaryAccount]` — The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.
    
</dd>
</dl>

<dl>
<dd>

**pay_in_reference:** `typing.Optional[str]` — The Pay-In reference of the payment.
    
</dd>
</dl>

<dl>
<dd>

**quote:** `typing.Optional[TransferwiseQuote]` — The quote details used to created the payment.
    
</dd>
</dl>

<dl>
<dd>

**rate:** `typing.Optional[str]` — The rate of the payment.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — The reference of the payment.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status.
    
</dd>
</dl>

<dl>
<dd>

**status_transferwise:** `typing.Optional[str]` — The status as Transferwise reports it.
    
</dd>
</dl>

<dl>
<dd>

**status_transferwise_issue:** `typing.Optional[str]` — A status to indicatie if Transferwise has an issue with this payment and requires more information.
    
</dd>
</dl>

<dl>
<dd>

**sub_status:** `typing.Optional[str]` — The subStatus.
    
</dd>
</dl>

<dl>
<dd>

**time_delivery_estimate:** `typing.Optional[str]` — The estimated delivery time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_transfer.<a href="src/fern/transferwise_transfer/client.py">read_transferwise_transfer_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to create Transferwise payments.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_transfer.read_transferwise_transfer_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-transfer-requirement
<details><summary><code>client.transferwise_transfer_requirement.<a href="src/fern/transferwise_transfer_requirement/client.py">create_transferwise_transfer_requirement_for_user_transferwise_quote</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to determine the account requirements for Transferwise transfers.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_transfer_requirement.create_transferwise_transfer_requirement_for_user_transferwise_quote(
    user_id=1,
    transferwise_quote_id=1,
    recipient_id="recipient_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**transferwise_quote_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**recipient_id:** `str` — The id of the target account.
    
</dd>
</dl>

<dl>
<dd>

**detail:** `typing.Optional[typing.Sequence[TransferwiseRequirementField]]` — The fields which were specified as "required" and have since been filled by the user. Always provide the full list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transferwise-user
<details><summary><code>client.transferwise_user.<a href="src/fern/transferwise_user/client.py">list_all_transferwise_user_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage Transferwise users.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_user.list_all_transferwise_user_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_user.<a href="src/fern/transferwise_user/client.py">create_transferwise_user_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to manage Transferwise users.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.transferwise_user.create_transferwise_user_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**oauth_code:** `typing.Optional[str]` — The OAuth code returned by Transferwise we should be using to gain access to the user's Transferwise account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## tree-progress
<details><summary><code>client.tree_progress.<a href="src/fern/tree_progress/client.py">list_all_tree_progress_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

See how many trees this user has planted.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.tree_progress.list_all_tree_progress_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## whitelist-sdd-one-off
<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">list_all_whitelist_sdd_one_off_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a listing of all one off SDD whitelist entries for a target monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_one_off.list_all_whitelist_sdd_one_off_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">create_whitelist_sdd_one_off_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new one off SDD whitelist entry.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_one_off.create_whitelist_sdd_one_off_for_user(
    user_id=1,
    monetary_account_paying_id=1,
    request_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_paying_id:** `int` — ID of the monetary account of which you want to pay from.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `int` — ID of the request for which you want to whitelist the originating SDD.
    
</dd>
</dl>

<dl>
<dd>

**maximum_amount_per_month:** `typing.Optional[Amount]` — The maximum amount of money that is allowed to be deducted based on the whitelist.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">read_whitelist_sdd_one_off_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific one off SDD whitelist entry.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_one_off.read_whitelist_sdd_one_off_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">update_whitelist_sdd_one_off_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_one_off.update_whitelist_sdd_one_off_for_user(
    user_id=1,
    item_id=1,
    monetary_account_paying_id=1,
    request_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_paying_id:** `int` — ID of the monetary account of which you want to pay from.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `int` — ID of the request for which you want to whitelist the originating SDD.
    
</dd>
</dl>

<dl>
<dd>

**maximum_amount_per_month:** `typing.Optional[Amount]` — The maximum amount of money that is allowed to be deducted based on the whitelist.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">delete_whitelist_sdd_one_off_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_one_off.delete_whitelist_sdd_one_off_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## whitelist-sdd-recurring
<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">list_all_whitelist_sdd_recurring_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a listing of all recurring SDD whitelist entries for a target monetary account.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_recurring.list_all_whitelist_sdd_recurring_for_user(
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

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">create_whitelist_sdd_recurring_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new recurring SDD whitelist entry.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_recurring.create_whitelist_sdd_recurring_for_user(
    user_id=1,
    monetary_account_paying_id=1,
    request_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_paying_id:** `int` — ID of the monetary account of which you want to pay from.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `int` — ID of the request for which you want to whitelist the originating SDD.
    
</dd>
</dl>

<dl>
<dd>

**maximum_amount_per_month:** `typing.Optional[Amount]` — The maximum amount of money that is allowed to be deducted based on the whitelist.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">read_whitelist_sdd_recurring_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific recurring SDD whitelist entry.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_recurring.read_whitelist_sdd_recurring_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">update_whitelist_sdd_recurring_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_recurring.update_whitelist_sdd_recurring_for_user(
    user_id=1,
    item_id=1,
    monetary_account_paying_id=1,
    request_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**monetary_account_paying_id:** `int` — ID of the monetary account of which you want to pay from.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `int` — ID of the request for which you want to whitelist the originating SDD.
    
</dd>
</dl>

<dl>
<dd>

**maximum_amount_per_month:** `typing.Optional[Amount]` — The maximum amount of money that is allowed to be deducted based on the whitelist.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">delete_whitelist_sdd_recurring_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
</dd>
</dl>
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
    cache_control="YOUR_CACHE_CONTROL",
    bunq_language="YOUR_BUNQ_LANGUAGE",
    bunq_region="YOUR_BUNQ_REGION",
    bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
    bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
    bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
)
client.whitelist_sdd_recurring.delete_whitelist_sdd_recurring_for_user(
    user_id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

