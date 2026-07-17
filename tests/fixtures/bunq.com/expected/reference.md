# Reference
## attachment-public
<details><summary><code>client.attachment_public.<a href="src/fern/attachment_public/client.py">create_attachment_public</a>(...) -> AttachmentPublicCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.attachment_public.create_attachment_public(
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

<details><summary><code>client.attachment_public.<a href="src/fern/attachment_public/client.py">read_attachment_public</a>(...) -> AttachmentPublicRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_attachment_public</a>(...) -> typing.List[AttachmentPublicContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_place_lookup_photo</a>(...) -> typing.List[PlacePhotoLookupContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_attachment</a>(...) -> typing.List[AttachmentUserContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_card_export_statement_card</a>(...) -> typing.List[ExportStatementCardContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_chat_conversation_attachment</a>(...) -> typing.List[AttachmentConversationContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_export_annual_overview</a>(...) -> typing.List[ExportAnnualOverviewContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_attachment</a>(...) -> typing.List[AttachmentMonetaryAccountContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_customer_statement</a>(...) -> typing.List[ExportStatementContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_event_statement</a>(...) -> typing.List[ExportStatementPaymentContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.content.<a href="src/fern/content/client.py">list_all_content_for_user_monetary_account_export_rib</a>(...) -> typing.List[ExportRibContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.avatar.<a href="src/fern/avatar/client.py">create_avatar</a>(...) -> AvatarCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `Avatar` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatar.<a href="src/fern/avatar/client.py">read_avatar</a>(...) -> AvatarRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.device.<a href="src/fern/device/client.py">list_all_device</a>() -> typing.List[DeviceListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.device.<a href="src/fern/device/client.py">read_device</a>(...) -> DeviceRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.device_server.<a href="src/fern/device_server/client.py">list_all_device_server</a>() -> typing.List[DeviceServerListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.device_server.<a href="src/fern/device_server/client.py">create_device_server</a>(...) -> DeviceServerCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `DeviceServer` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_server.<a href="src/fern/device_server/client.py">read_device_server</a>(...) -> DeviceServerRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.installation.<a href="src/fern/installation/client.py">list_all_installation</a>() -> typing.List[InstallationListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.installation.<a href="src/fern/installation/client.py">create_installation</a>(...) -> InstallationCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.installation.<a href="src/fern/installation/client.py">read_installation</a>(...) -> InstallationRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.server_public_key.<a href="src/fern/server_public_key/client.py">list_all_server_public_key_for_installation</a>(...) -> typing.List[InstallationServerPublicKeyListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.payment_service_provider_credential.<a href="src/fern/payment_service_provider_credential/client.py">create_payment_service_provider_credential</a>(...) -> PaymentServiceProviderCredentialCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_service_provider_credential.<a href="src/fern/payment_service_provider_credential/client.py">read_payment_service_provider_credential</a>(...) -> PaymentServiceProviderCredentialRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.sandbox_user_company.<a href="src/fern/sandbox_user_company/client.py">create_sandbox_user_company</a>(...) -> SandboxUserCompanyCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sandbox_user_company.create_sandbox_user_company(
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
<details><summary><code>client.sandbox_user_person.<a href="src/fern/sandbox_user_person/client.py">create_sandbox_user_person</a>(...) -> SandboxUserPersonCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sandbox_user_person.create_sandbox_user_person(
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
<details><summary><code>client.server_error.<a href="src/fern/server_error/client.py">create_server_error</a>(...) -> ServerErrorCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.server_error.create_server_error(
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
<details><summary><code>client.session_server.<a href="src/fern/session_server/client.py">create_session_server</a>(...) -> SessionServerCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.session.<a href="src/fern/session/client.py">delete_session</a>(...) -> SessionDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.user.<a href="src/fern/user/client.py">list_all_user</a>() -> typing.List[UserListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">read_user</a>(...) -> UserRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.user_company.<a href="src/fern/user_company/client.py">read_user_company</a>(...) -> UserCompanyRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.user_company.<a href="src/fern/user_company/client.py">update_user_company</a>(...) -> UserCompanyUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `UserCompany` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.name.<a href="src/fern/name/client.py">list_all_name_for_user_company</a>(...) -> typing.List[UserCompanyNameListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.user_payment_service_provider.<a href="src/fern/user_payment_service_provider/client.py">read_user_payment_service_provider</a>(...) -> UserPaymentServiceProviderRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.user_person.<a href="src/fern/user_person/client.py">read_user_person</a>(...) -> UserPersonRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.user_person.<a href="src/fern/user_person/client.py">update_user_person</a>(...) -> UserPersonUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `UserPerson` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.attachment.<a href="src/fern/attachment/client.py">read_attachment_for_user</a>(...) -> AttachmentUserRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.attachment.<a href="src/fern/attachment/client.py">create_attachment_for_user_monetary_account</a>(...) -> AttachmentMonetaryAccountCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.attachment.create_attachment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
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
<details><summary><code>client.billing_contract_subscription.<a href="src/fern/billing_contract_subscription/client.py">list_all_billing_contract_subscription_for_user</a>(...) -> typing.List[BillingContractSubscriptionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.bunqme_fundraiser_profile.<a href="src/fern/bunqme_fundraiser_profile/client.py">list_all_bunqme_fundraiser_profile_for_user</a>(...) -> typing.List[BunqMeFundraiserProfileUserListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.bunqme_fundraiser_profile.<a href="src/fern/bunqme_fundraiser_profile/client.py">read_bunqme_fundraiser_profile_for_user</a>(...) -> BunqMeFundraiserProfileUserRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.card.<a href="src/fern/card/client.py">list_all_card_for_user</a>(...) -> typing.List[CardListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.card.<a href="src/fern/card/client.py">read_card_for_user</a>(...) -> CardRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.card.<a href="src/fern/card/client.py">update_card_for_user</a>(...) -> CardUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `Card` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.card_batch.<a href="src/fern/card_batch/client.py">create_card_batch_for_user</a>(...) -> CardBatchCreate</code></summary>
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
from fern import FernApi, CardBatchEntry
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**cards:** `typing.List[CardBatchEntry]` — The cards that need to be updated.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.card_batch_replace.<a href="src/fern/card_batch_replace/client.py">create_card_batch_replace_for_user</a>(...) -> CardBatchReplaceCreate</code></summary>
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
from fern import FernApi, CardBatchReplaceEntry
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**cards:** `typing.List[CardBatchReplaceEntry]` — The cards that need to be replaced.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.card_credit.<a href="src/fern/card_credit/client.py">create_card_credit_for_user</a>(...) -> CardCreditCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**pin_code_assignment:** `typing.Optional[typing.List[CardPinAssignment]]` — Array of Types, PINs, account IDs assigned to the card.
    
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
<details><summary><code>client.card_debit.<a href="src/fern/card_debit/client.py">create_card_debit_for_user</a>(...) -> CardDebitCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `CardDebit` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.card_name.<a href="src/fern/card_name/client.py">list_all_card_name_for_user</a>(...) -> typing.List[CardNameListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.export_statement_card.<a href="src/fern/export_statement_card/client.py">list_all_export_statement_card_for_user_card</a>(...) -> typing.List[ExportStatementCardListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_statement_card.<a href="src/fern/export_statement_card/client.py">read_export_statement_card_for_user_card</a>(...) -> ExportStatementCardRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">list_all_export_statement_card_csv_for_user_card</a>(...) -> typing.List[ExportStatementCardCsvListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">create_export_statement_card_csv_for_user_card</a>(...) -> ExportStatementCardCsvCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">read_export_statement_card_csv_for_user_card</a>(...) -> ExportStatementCardCsvRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_statement_card_csv.<a href="src/fern/export_statement_card_csv/client.py">delete_export_statement_card_csv_for_user_card</a>(...) -> ExportStatementCardCsvDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">list_all_export_statement_card_pdf_for_user_card</a>(...) -> typing.List[ExportStatementCardPdfListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">create_export_statement_card_pdf_for_user_card</a>(...) -> ExportStatementCardPdfCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">read_export_statement_card_pdf_for_user_card</a>(...) -> ExportStatementCardPdfRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_statement_card_pdf.<a href="src/fern/export_statement_card_pdf/client.py">delete_export_statement_card_pdf_for_user_card</a>(...) -> ExportStatementCardPdfDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">list_all_generated_cvc2for_user_card</a>(...) -> typing.List[CardGeneratedCvc2Listing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">create_generated_cvc2for_user_card</a>(...) -> CardGeneratedCvc2Create</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `CardGeneratedCvc2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">read_generated_cvc2for_user_card</a>(...) -> CardGeneratedCvc2Read</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.generated_cvc2.<a href="src/fern/generated_cvc2/client.py">update_generated_cvc2for_user_card</a>(...) -> CardGeneratedCvc2Update</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `CardGeneratedCvc2` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.replace.<a href="src/fern/replace/client.py">create_replace_for_user_card</a>(...) -> CardReplaceCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**pin_code_assignment:** `typing.Optional[typing.List[CardPinAssignment]]` — Array of Types, PINs, account IDs assigned to the card.
    
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
<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">list_all_certificate_pinned_for_user</a>(...) -> typing.List[CertificatePinnedListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">create_certificate_pinned_for_user</a>(...) -> CertificatePinnedCreate</code></summary>
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
from fern import FernApi, Certificate
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.certificate_pinned.create_certificate_pinned_for_user(
    user_id=1,
    certificate_chain=[
        Certificate()
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

**certificate_chain:** `typing.List[Certificate]` — The certificate chain in .PEM format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">read_certificate_pinned_for_user</a>(...) -> CertificatePinnedRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.certificate_pinned.<a href="src/fern/certificate_pinned/client.py">delete_certificate_pinned_for_user</a>(...) -> CertificatePinnedDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.challenge_request.<a href="src/fern/challenge_request/client.py">read_challenge_request_for_user</a>(...) -> MasterCardIdentityCheckChallengeRequestUserRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.challenge_request.<a href="src/fern/challenge_request/client.py">update_challenge_request_for_user</a>(...) -> MasterCardIdentityCheckChallengeRequestUserUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.company.<a href="src/fern/company/client.py">list_all_company_for_user</a>(...) -> typing.List[CompanyListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.company.<a href="src/fern/company/client.py">create_company_for_user</a>(...) -> CompanyCreate</code></summary>
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
from fern import FernApi, Address
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `Company` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.company.<a href="src/fern/company/client.py">read_company_for_user</a>(...) -> CompanyRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.company.<a href="src/fern/company/client.py">update_company_for_user</a>(...) -> CompanyUpdate</code></summary>
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
from fern import FernApi, Address
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `Company` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.confirmation_of_funds.<a href="src/fern/confirmation_of_funds/client.py">create_confirmation_of_funds_for_user</a>(...) -> ConfirmationOfFundsCreate</code></summary>
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
from fern import FernApi, Amount, Pointer
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.credential_password_ip.<a href="src/fern/credential_password_ip/client.py">list_all_credential_password_ip_for_user</a>(...) -> typing.List[UserCredentialPasswordIpListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.credential_password_ip.<a href="src/fern/credential_password_ip/client.py">read_credential_password_ip_for_user</a>(...) -> UserCredentialPasswordIpRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.ip.<a href="src/fern/ip/client.py">list_all_ip_for_user_credential_password_ip</a>(...) -> typing.List[PermittedIpListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.ip.<a href="src/fern/ip/client.py">create_ip_for_user_credential_password_ip</a>(...) -> PermittedIpCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PermittedIp` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip.<a href="src/fern/ip/client.py">read_ip_for_user_credential_password_ip</a>(...) -> PermittedIpRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.ip.<a href="src/fern/ip/client.py">update_ip_for_user_credential_password_ip</a>(...) -> PermittedIpUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PermittedIp` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.currency_cloud_beneficiary.<a href="src/fern/currency_cloud_beneficiary/client.py">list_all_currency_cloud_beneficiary_for_user</a>(...) -> typing.List[CurrencyCloudBeneficiaryListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.currency_cloud_beneficiary.<a href="src/fern/currency_cloud_beneficiary/client.py">create_currency_cloud_beneficiary_for_user</a>(...) -> CurrencyCloudBeneficiaryCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.currency_cloud_beneficiary.create_currency_cloud_beneficiary_for_user(
    user_id=1,
    all_field=[
        "all_field"
    ],
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

**all_field:** `typing.List[str]` — All fields that were required by CurrencyCloud. Obtained through the CurrencyCloudBeneficiaryRequirement listing.
    
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

<details><summary><code>client.currency_cloud_beneficiary.<a href="src/fern/currency_cloud_beneficiary/client.py">read_currency_cloud_beneficiary_for_user</a>(...) -> CurrencyCloudBeneficiaryRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.currency_cloud_beneficiary_requirement.<a href="src/fern/currency_cloud_beneficiary_requirement/client.py">list_all_currency_cloud_beneficiary_requirement_for_user</a>(...) -> typing.List[CurrencyCloudBeneficiaryRequirementListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.event.<a href="src/fern/event/client.py">list_all_event_for_user</a>(...) -> typing.List[EventListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.event.<a href="src/fern/event/client.py">read_event_for_user</a>(...) -> EventRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">list_all_export_annual_overview_for_user</a>(...) -> typing.List[ExportAnnualOverviewListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">create_export_annual_overview_for_user</a>(...) -> ExportAnnualOverviewCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">read_export_annual_overview_for_user</a>(...) -> ExportAnnualOverviewRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_annual_overview.<a href="src/fern/export_annual_overview/client.py">delete_export_annual_overview_for_user</a>(...) -> ExportAnnualOverviewDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.feature_announcement.<a href="src/fern/feature_announcement/client.py">read_feature_announcement_for_user</a>(...) -> FeatureAnnouncementRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.insight_preference_date.<a href="src/fern/insight_preference_date/client.py">list_all_insight_preference_date_for_user</a>(...) -> typing.List[InsightPreferenceDateListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.insights.<a href="src/fern/insights/client.py">list_all_insights_for_user</a>(...) -> typing.List[InsightListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.insights_search.<a href="src/fern/insights_search/client.py">list_all_insights_search_for_user</a>(...) -> typing.List[InsightEventListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">list_all_invoice_for_user</a>(...) -> typing.List[InvoiceByUserListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">read_invoice_for_user</a>(...) -> InvoiceByUserRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">list_all_invoice_for_user_monetary_account</a>(...) -> typing.List[InvoiceListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.invoice.<a href="src/fern/invoice/client.py">read_invoice_for_user_monetary_account</a>(...) -> InvoiceRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.pdf_content.<a href="src/fern/pdf_content/client.py">list_all_pdf_content_for_user_invoice</a>(...) -> typing.List[InvoiceExportPdfContentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.legal_name.<a href="src/fern/legal_name/client.py">list_all_legal_name_for_user</a>(...) -> typing.List[UserLegalNameListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.limit.<a href="src/fern/limit/client.py">list_all_limit_for_user</a>(...) -> typing.List[CustomerLimitListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.monetary_account.<a href="src/fern/monetary_account/client.py">list_all_monetary_account_for_user</a>(...) -> typing.List[MonetaryAccountListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account.<a href="src/fern/monetary_account/client.py">read_monetary_account_for_user</a>(...) -> MonetaryAccountRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">list_all_monetary_account_bank_for_user</a>(...) -> typing.List[MonetaryAccountBankListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">create_monetary_account_bank_for_user</a>(...) -> MonetaryAccountBankCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `MonetaryAccountBank` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">read_monetary_account_bank_for_user</a>(...) -> MonetaryAccountBankRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account_bank.<a href="src/fern/monetary_account_bank/client.py">update_monetary_account_bank_for_user</a>(...) -> MonetaryAccountBankUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `MonetaryAccountBank` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.monetary_account_external.<a href="src/fern/monetary_account_external/client.py">list_all_monetary_account_external_for_user</a>(...) -> typing.List[MonetaryAccountExternalListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account_external.<a href="src/fern/monetary_account_external/client.py">read_monetary_account_external_for_user</a>(...) -> MonetaryAccountExternalRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">list_all_monetary_account_joint_for_user</a>(...) -> typing.List[MonetaryAccountJointListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">create_monetary_account_joint_for_user</a>(...) -> MonetaryAccountJointCreate</code></summary>
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
from fern import FernApi, CoOwner
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monetary_account_joint.create_monetary_account_joint_for_user(
    user_id=1,
    all_co_owner=[
        CoOwner()
    ],
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

**request:** `MonetaryAccountJoint` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">read_monetary_account_joint_for_user</a>(...) -> MonetaryAccountJointRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account_joint.<a href="src/fern/monetary_account_joint/client.py">update_monetary_account_joint_for_user</a>(...) -> MonetaryAccountJointUpdate</code></summary>
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
from fern import FernApi, CoOwner
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monetary_account_joint.update_monetary_account_joint_for_user(
    user_id=1,
    item_id=1,
    all_co_owner=[
        CoOwner()
    ],
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

**request:** `MonetaryAccountJoint` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">list_all_monetary_account_savings_for_user</a>(...) -> typing.List[MonetaryAccountSavingsListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">create_monetary_account_savings_for_user</a>(...) -> MonetaryAccountSavingsCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `MonetaryAccountSavings` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">read_monetary_account_savings_for_user</a>(...) -> MonetaryAccountSavingsRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.monetary_account_savings.<a href="src/fern/monetary_account_savings/client.py">update_monetary_account_savings_for_user</a>(...) -> MonetaryAccountSavingsUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `MonetaryAccountSavings` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> typing.List[NoteAttachmentBunqMeFundraiserResultListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteAttachmentBunqMeFundraiserResultCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentBunqMeFundraiserResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteAttachmentBunqMeFundraiserResultRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteAttachmentBunqMeFundraiserResultUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentBunqMeFundraiserResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteAttachmentBunqMeFundraiserResultDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_draft_payment</a>(...) -> typing.List[NoteAttachmentDraftPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_draft_payment</a>(...) -> NoteAttachmentDraftPaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentDraftPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_draft_payment</a>(...) -> NoteAttachmentDraftPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_draft_payment</a>(...) -> NoteAttachmentDraftPaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentDraftPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_draft_payment</a>(...) -> NoteAttachmentDraftPaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> typing.List[NoteAttachmentIdealMerchantTransactionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteAttachmentIdealMerchantTransactionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentIdealMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteAttachmentIdealMerchantTransactionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteAttachmentIdealMerchantTransactionUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentIdealMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteAttachmentIdealMerchantTransactionDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_mastercard_action</a>(...) -> typing.List[NoteAttachmentMasterCardActionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_mastercard_action</a>(...) -> NoteAttachmentMasterCardActionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentMasterCardAction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_mastercard_action</a>(...) -> NoteAttachmentMasterCardActionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_mastercard_action</a>(...) -> NoteAttachmentMasterCardActionUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentMasterCardAction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_mastercard_action</a>(...) -> NoteAttachmentMasterCardActionDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_payment_batch</a>(...) -> typing.List[NoteAttachmentPaymentBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_payment_batch</a>(...) -> NoteAttachmentPaymentBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentPaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_payment_batch</a>(...) -> NoteAttachmentPaymentBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_payment_batch</a>(...) -> NoteAttachmentPaymentBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentPaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_payment_batch</a>(...) -> NoteAttachmentPaymentBatchDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_payment</a>(...) -> typing.List[NoteAttachmentPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_payment</a>(...) -> NoteAttachmentPaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_payment</a>(...) -> NoteAttachmentPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_payment</a>(...) -> NoteAttachmentPaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_payment</a>(...) -> NoteAttachmentPaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...) -> typing.List[NoteAttachmentRequestInquiryBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteAttachmentRequestInquiryBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentRequestInquiryBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteAttachmentRequestInquiryBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteAttachmentRequestInquiryBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentRequestInquiryBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteAttachmentRequestInquiryBatchDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_request_inquiry</a>(...) -> typing.List[NoteAttachmentRequestInquiryListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_request_inquiry</a>(...) -> NoteAttachmentRequestInquiryCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentRequestInquiry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_request_inquiry</a>(...) -> NoteAttachmentRequestInquiryRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_request_inquiry</a>(...) -> NoteAttachmentRequestInquiryUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentRequestInquiry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_request_inquiry</a>(...) -> NoteAttachmentRequestInquiryDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_request_response</a>(...) -> typing.List[NoteAttachmentRequestResponseListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_request_response</a>(...) -> NoteAttachmentRequestResponseCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentRequestResponse` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_request_response</a>(...) -> NoteAttachmentRequestResponseRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_request_response</a>(...) -> NoteAttachmentRequestResponseUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentRequestResponse` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_request_response</a>(...) -> NoteAttachmentRequestResponseDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...) -> typing.List[NoteAttachmentSchedulePaymentBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteAttachmentSchedulePaymentBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentSchedulePaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteAttachmentSchedulePaymentBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteAttachmentSchedulePaymentBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentSchedulePaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteAttachmentSchedulePaymentBatchDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_schedule_payment</a>(...) -> typing.List[NoteAttachmentSchedulePaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_schedule_payment</a>(...) -> NoteAttachmentSchedulePaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentSchedulePayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_schedule_payment</a>(...) -> NoteAttachmentSchedulePaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_schedule_payment</a>(...) -> NoteAttachmentSchedulePaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentSchedulePayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_schedule_payment</a>(...) -> NoteAttachmentSchedulePaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...) -> typing.List[NoteAttachmentScheduleInstanceListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteAttachmentScheduleInstanceCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentScheduleInstance` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteAttachmentScheduleInstanceRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteAttachmentScheduleInstanceUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentScheduleInstance` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteAttachmentScheduleInstanceDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> typing.List[NoteAttachmentSofortMerchantTransactionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteAttachmentSofortMerchantTransactionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentSofortMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteAttachmentSofortMerchantTransactionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteAttachmentSofortMerchantTransactionUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentSofortMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteAttachmentSofortMerchantTransactionDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_switch_service_payment</a>(...) -> typing.List[NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_switch_service_payment</a>(...) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentBankSwitchServiceNetherlandsIncomingPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_switch_service_payment</a>(...) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_switch_service_payment</a>(...) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentBankSwitchServiceNetherlandsIncomingPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_switch_service_payment</a>(...) -> NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> typing.List[NoteAttachmentWhitelistResultListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">create_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteAttachmentWhitelistResultCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentWhitelistResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">read_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteAttachmentWhitelistResultRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">update_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteAttachmentWhitelistResultUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteAttachmentWhitelistResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_attachment.<a href="src/fern/note_attachment/client.py">delete_note_attachment_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteAttachmentWhitelistResultDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> typing.List[NoteTextBunqMeFundraiserResultListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteTextBunqMeFundraiserResultCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextBunqMeFundraiserResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteTextBunqMeFundraiserResultRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteTextBunqMeFundraiserResultUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextBunqMeFundraiserResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_bunqme_fundraiser_result</a>(...) -> NoteTextBunqMeFundraiserResultDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_draft_payment</a>(...) -> typing.List[NoteTextDraftPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_draft_payment</a>(...) -> NoteTextDraftPaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextDraftPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_draft_payment</a>(...) -> NoteTextDraftPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_draft_payment</a>(...) -> NoteTextDraftPaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextDraftPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_draft_payment</a>(...) -> NoteTextDraftPaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> typing.List[NoteTextIdealMerchantTransactionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteTextIdealMerchantTransactionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextIdealMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteTextIdealMerchantTransactionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteTextIdealMerchantTransactionUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextIdealMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_ideal_merchant_transaction</a>(...) -> NoteTextIdealMerchantTransactionDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_mastercard_action</a>(...) -> typing.List[NoteTextMasterCardActionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_mastercard_action</a>(...) -> NoteTextMasterCardActionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextMasterCardAction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_mastercard_action</a>(...) -> NoteTextMasterCardActionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_mastercard_action</a>(...) -> NoteTextMasterCardActionUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextMasterCardAction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_mastercard_action</a>(...) -> NoteTextMasterCardActionDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_payment_batch</a>(...) -> typing.List[NoteTextPaymentBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_payment_batch</a>(...) -> NoteTextPaymentBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextPaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_payment_batch</a>(...) -> NoteTextPaymentBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_payment_batch</a>(...) -> NoteTextPaymentBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextPaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_payment_batch</a>(...) -> NoteTextPaymentBatchDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_payment</a>(...) -> typing.List[NoteTextPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_payment</a>(...) -> NoteTextPaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_payment</a>(...) -> NoteTextPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_payment</a>(...) -> NoteTextPaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_payment</a>(...) -> NoteTextPaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_request_inquiry_batch</a>(...) -> typing.List[NoteTextRequestInquiryBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteTextRequestInquiryBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextRequestInquiryBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteTextRequestInquiryBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteTextRequestInquiryBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextRequestInquiryBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_request_inquiry_batch</a>(...) -> NoteTextRequestInquiryBatchDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_request_inquiry</a>(...) -> typing.List[NoteTextRequestInquiryListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_request_inquiry</a>(...) -> NoteTextRequestInquiryCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextRequestInquiry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_request_inquiry</a>(...) -> NoteTextRequestInquiryRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_request_inquiry</a>(...) -> NoteTextRequestInquiryUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextRequestInquiry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_request_inquiry</a>(...) -> NoteTextRequestInquiryDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_request_response</a>(...) -> typing.List[NoteTextRequestResponseListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_request_response</a>(...) -> NoteTextRequestResponseCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextRequestResponse` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_request_response</a>(...) -> NoteTextRequestResponseRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_request_response</a>(...) -> NoteTextRequestResponseUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextRequestResponse` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_request_response</a>(...) -> NoteTextRequestResponseDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_schedule_payment_batch</a>(...) -> typing.List[NoteTextSchedulePaymentBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteTextSchedulePaymentBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextSchedulePaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteTextSchedulePaymentBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteTextSchedulePaymentBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextSchedulePaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_schedule_payment_batch</a>(...) -> NoteTextSchedulePaymentBatchDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_schedule_payment</a>(...) -> typing.List[NoteTextSchedulePaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_schedule_payment</a>(...) -> NoteTextSchedulePaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextSchedulePayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_schedule_payment</a>(...) -> NoteTextSchedulePaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_schedule_payment</a>(...) -> NoteTextSchedulePaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextSchedulePayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_schedule_payment</a>(...) -> NoteTextSchedulePaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...) -> typing.List[NoteTextScheduleInstanceListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteTextScheduleInstanceCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextScheduleInstance` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteTextScheduleInstanceRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteTextScheduleInstanceUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextScheduleInstance` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_schedule_schedule_instance</a>(...) -> NoteTextScheduleInstanceDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> typing.List[NoteTextSofortMerchantTransactionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteTextSofortMerchantTransactionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextSofortMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteTextSofortMerchantTransactionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteTextSofortMerchantTransactionUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextSofortMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_sofort_merchant_transaction</a>(...) -> NoteTextSofortMerchantTransactionDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_switch_service_payment</a>(...) -> typing.List[NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_switch_service_payment</a>(...) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextBankSwitchServiceNetherlandsIncomingPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_switch_service_payment</a>(...) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_switch_service_payment</a>(...) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextBankSwitchServiceNetherlandsIncomingPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_switch_service_payment</a>(...) -> NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">list_all_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> typing.List[NoteTextWhitelistResultListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">create_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteTextWhitelistResultCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextWhitelistResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">read_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteTextWhitelistResultRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">update_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteTextWhitelistResultUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NoteTextWhitelistResult` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.note_text.<a href="src/fern/note_text/client.py">delete_note_text_for_user_monetary_account_whitelist_whitelist_result</a>(...) -> NoteTextWhitelistResultDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.bunqme_fundraiser_result.<a href="src/fern/bunqme_fundraiser_result/client.py">read_bunqme_fundraiser_result_for_user_monetary_account</a>(...) -> BunqMeFundraiserResultRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">list_all_bunqme_tab_for_user_monetary_account</a>(...) -> typing.List[BunqMeTabListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">create_bunqme_tab_for_user_monetary_account</a>(...) -> BunqMeTabCreate</code></summary>
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
from fern import FernApi, BunqMeTabEntry
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `BunqMeTab` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">read_bunqme_tab_for_user_monetary_account</a>(...) -> BunqMeTabRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.bunqme_tab.<a href="src/fern/bunqme_tab/client.py">update_bunqme_tab_for_user_monetary_account</a>(...) -> BunqMeTabUpdate</code></summary>
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
from fern import FernApi, BunqMeTabEntry
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `BunqMeTab` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.bunqme_tab_result_response.<a href="src/fern/bunqme_tab_result_response/client.py">read_bunqme_tab_result_response_for_user_monetary_account</a>(...) -> BunqMeTabResultResponseRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.currency_cloud_payment_quote.<a href="src/fern/currency_cloud_payment_quote/client.py">create_currency_cloud_payment_quote_for_user_monetary_account</a>(...) -> CurrencyCloudPaymentQuoteCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.currency_cloud_payment_quote.create_currency_cloud_payment_quote_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    pointers=[
        Pointer()
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

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**pointers:** `typing.List[Pointer]` — The points we want to know the fees for.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.currency_conversion.<a href="src/fern/currency_conversion/client.py">list_all_currency_conversion_for_user_monetary_account</a>(...) -> typing.List[CurrencyConversionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.currency_conversion.<a href="src/fern/currency_conversion/client.py">read_currency_conversion_for_user_monetary_account</a>(...) -> CurrencyConversionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.currency_conversion_quote.<a href="src/fern/currency_conversion_quote/client.py">create_currency_conversion_quote_for_user_monetary_account</a>(...) -> CurrencyConversionQuoteCreate</code></summary>
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
from fern import FernApi, Amount, Pointer
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `CurrencyConversionQuote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.currency_conversion_quote.<a href="src/fern/currency_conversion_quote/client.py">read_currency_conversion_quote_for_user_monetary_account</a>(...) -> CurrencyConversionQuoteRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.currency_conversion_quote.<a href="src/fern/currency_conversion_quote/client.py">update_currency_conversion_quote_for_user_monetary_account</a>(...) -> CurrencyConversionQuoteUpdate</code></summary>
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
from fern import FernApi, Amount, Pointer
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `CurrencyConversionQuote` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">list_all_customer_statement_for_user_monetary_account</a>(...) -> typing.List[ExportStatementListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">create_customer_statement_for_user_monetary_account</a>(...) -> ExportStatementCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">read_customer_statement_for_user_monetary_account</a>(...) -> ExportStatementRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.customer_statement.<a href="src/fern/customer_statement/client.py">delete_customer_statement_for_user_monetary_account</a>(...) -> ExportStatementDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">list_all_draft_payment_for_user_monetary_account</a>(...) -> typing.List[DraftPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">create_draft_payment_for_user_monetary_account</a>(...) -> DraftPaymentCreate</code></summary>
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
from fern import FernApi, DraftPaymentEntry
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_payment.create_draft_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    entries=[
        DraftPaymentEntry()
    ],
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

**request:** `DraftPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">read_draft_payment_for_user_monetary_account</a>(...) -> DraftPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.draft_payment.<a href="src/fern/draft_payment/client.py">update_draft_payment_for_user_monetary_account</a>(...) -> DraftPaymentUpdate</code></summary>
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
from fern import FernApi, DraftPaymentEntry
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.draft_payment.update_draft_payment_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    item_id=1,
    entries=[
        DraftPaymentEntry()
    ],
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

**request:** `DraftPayment` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.statement.<a href="src/fern/statement/client.py">create_statement_for_user_monetary_account_event</a>(...) -> ExportStatementPaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.statement.create_statement_for_user_monetary_account_event(
    user_id=1,
    monetary_account_id=1,
    event_id=1,
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

<details><summary><code>client.statement.<a href="src/fern/statement/client.py">read_statement_for_user_monetary_account_event</a>(...) -> ExportStatementPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">list_all_export_rib_for_user_monetary_account</a>(...) -> typing.List[ExportRibListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">create_export_rib_for_user_monetary_account</a>(...) -> ExportRibCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.export_rib.create_export_rib_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
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

<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">read_export_rib_for_user_monetary_account</a>(...) -> ExportRibRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.export_rib.<a href="src/fern/export_rib/client.py">delete_export_rib_for_user_monetary_account</a>(...) -> ExportRibDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.ideal_merchant_transaction.<a href="src/fern/ideal_merchant_transaction/client.py">list_all_ideal_merchant_transaction_for_user_monetary_account</a>(...) -> typing.List[IdealMerchantTransactionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.ideal_merchant_transaction.<a href="src/fern/ideal_merchant_transaction/client.py">create_ideal_merchant_transaction_for_user_monetary_account</a>(...) -> IdealMerchantTransactionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IdealMerchantTransaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ideal_merchant_transaction.<a href="src/fern/ideal_merchant_transaction/client.py">read_ideal_merchant_transaction_for_user_monetary_account</a>(...) -> IdealMerchantTransactionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.mastercard_action.<a href="src/fern/mastercard_action/client.py">list_all_mastercard_action_for_user_monetary_account</a>(...) -> typing.List[MasterCardActionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.mastercard_action.<a href="src/fern/mastercard_action/client.py">read_mastercard_action_for_user_monetary_account</a>(...) -> MasterCardActionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.payment.<a href="src/fern/payment/client.py">list_all_payment_for_user_monetary_account_mastercard_action</a>(...) -> typing.List[MasterCardPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment.<a href="src/fern/payment/client.py">list_all_payment_for_user_monetary_account</a>(...) -> typing.List[PaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment.<a href="src/fern/payment/client.py">create_payment_for_user_monetary_account</a>(...) -> PaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Payment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment.<a href="src/fern/payment/client.py">read_payment_for_user_monetary_account</a>(...) -> PaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">list_all_notification_filter_url_for_user_monetary_account</a>(...) -> typing.List[NotificationFilterUrlMonetaryAccountListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">create_notification_filter_url_for_user_monetary_account</a>(...) -> NotificationFilterUrlMonetaryAccountCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**notification_filters:** `typing.Optional[typing.List[NotificationFilterUrl]]` — The types of notifications that will result in a url notification for this monetary account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">list_all_notification_filter_url_for_user</a>(...) -> typing.List[NotificationFilterUrlListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.notification_filter_url.<a href="src/fern/notification_filter_url/client.py">create_notification_filter_url_for_user</a>(...) -> NotificationFilterUrlCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NotificationFilterUrl` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">list_all_payment_auto_allocate_for_user_monetary_account</a>(...) -> typing.List[PaymentAutoAllocateListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">create_payment_auto_allocate_for_user_monetary_account</a>(...) -> PaymentAutoAllocateCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PaymentAutoAllocate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">read_payment_auto_allocate_for_user_monetary_account</a>(...) -> PaymentAutoAllocateRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">update_payment_auto_allocate_for_user_monetary_account</a>(...) -> PaymentAutoAllocateUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PaymentAutoAllocate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">delete_payment_auto_allocate_for_user_monetary_account</a>(...) -> PaymentAutoAllocateDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_auto_allocate.<a href="src/fern/payment_auto_allocate/client.py">list_all_payment_auto_allocate_for_user</a>(...) -> typing.List[PaymentAutoAllocateUserListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.definition.<a href="src/fern/definition/client.py">list_all_definition_for_user_monetary_account_payment_auto_allocate</a>(...) -> typing.List[PaymentAutoAllocateDefinitionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.instance.<a href="src/fern/instance/client.py">list_all_instance_for_user_monetary_account_payment_auto_allocate</a>(...) -> typing.List[PaymentAutoAllocateInstanceListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.instance.<a href="src/fern/instance/client.py">read_instance_for_user_monetary_account_payment_auto_allocate</a>(...) -> PaymentAutoAllocateInstanceRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">list_all_payment_batch_for_user_monetary_account</a>(...) -> typing.List[PaymentBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">create_payment_batch_for_user_monetary_account</a>(...) -> PaymentBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">read_payment_batch_for_user_monetary_account</a>(...) -> PaymentBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_batch.<a href="src/fern/payment_batch/client.py">update_payment_batch_for_user_monetary_account</a>(...) -> PaymentBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PaymentBatch` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">list_all_request_inquiry_for_user_monetary_account</a>(...) -> typing.List[RequestInquiryListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">create_request_inquiry_for_user_monetary_account</a>(...) -> RequestInquiryCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RequestInquiry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">read_request_inquiry_for_user_monetary_account</a>(...) -> RequestInquiryRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.request_inquiry.<a href="src/fern/request_inquiry/client.py">update_request_inquiry_for_user_monetary_account</a>(...) -> RequestInquiryUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `RequestInquiry` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">list_all_request_inquiry_batch_for_user_monetary_account</a>(...) -> typing.List[RequestInquiryBatchListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">create_request_inquiry_batch_for_user_monetary_account</a>(...) -> RequestInquiryBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `RequestInquiryBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">read_request_inquiry_batch_for_user_monetary_account</a>(...) -> RequestInquiryBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.request_inquiry_batch.<a href="src/fern/request_inquiry_batch/client.py">update_request_inquiry_batch_for_user_monetary_account</a>(...) -> RequestInquiryBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `RequestInquiryBatch` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.request_response.<a href="src/fern/request_response/client.py">list_all_request_response_for_user_monetary_account</a>(...) -> typing.List[RequestResponseListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.request_response.<a href="src/fern/request_response/client.py">read_request_response_for_user_monetary_account</a>(...) -> RequestResponseRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.request_response.<a href="src/fern/request_response/client.py">update_request_response_for_user_monetary_account</a>(...) -> RequestResponseUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `RequestResponse` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">list_all_schedule_for_user_monetary_account</a>(...) -> typing.List[ScheduleListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">read_schedule_for_user_monetary_account</a>(...) -> ScheduleRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">list_all_schedule_for_user</a>(...) -> typing.List[ScheduleUserListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">list_all_schedule_payment_for_user_monetary_account</a>(...) -> typing.List[SchedulePaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">create_schedule_payment_for_user_monetary_account</a>(...) -> SchedulePaymentCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `SchedulePayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">read_schedule_payment_for_user_monetary_account</a>(...) -> SchedulePaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">update_schedule_payment_for_user_monetary_account</a>(...) -> SchedulePaymentUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `SchedulePayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment.<a href="src/fern/schedule_payment/client.py">delete_schedule_payment_for_user_monetary_account</a>(...) -> SchedulePaymentDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">create_schedule_payment_batch_for_user_monetary_account</a>(...) -> SchedulePaymentBatchCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `SchedulePaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">read_schedule_payment_batch_for_user_monetary_account</a>(...) -> SchedulePaymentBatchRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">update_schedule_payment_batch_for_user_monetary_account</a>(...) -> SchedulePaymentBatchUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `SchedulePaymentBatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schedule_payment_batch.<a href="src/fern/schedule_payment_batch/client.py">delete_schedule_payment_batch_for_user_monetary_account</a>(...) -> SchedulePaymentBatchDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.schedule_instance.<a href="src/fern/schedule_instance/client.py">list_all_schedule_instance_for_user_monetary_account_schedule</a>(...) -> typing.List[ScheduleInstanceListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.schedule_instance.<a href="src/fern/schedule_instance/client.py">read_schedule_instance_for_user_monetary_account_schedule</a>(...) -> ScheduleInstanceRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.schedule_instance.<a href="src/fern/schedule_instance/client.py">update_schedule_instance_for_user_monetary_account_schedule</a>(...) -> ScheduleInstanceUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `ScheduleInstance` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">list_all_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...) -> typing.List[ShareInviteMonetaryAccountInquiryListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">create_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...) -> ShareInviteMonetaryAccountInquiryCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**monetary_account_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ShareInviteMonetaryAccountInquiry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">read_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...) -> ShareInviteMonetaryAccountInquiryRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.share_invite_monetary_account_inquiry.<a href="src/fern/share_invite_monetary_account_inquiry/client.py">update_share_invite_monetary_account_inquiry_for_user_monetary_account</a>(...) -> ShareInviteMonetaryAccountInquiryUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `ShareInviteMonetaryAccountInquiry` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.sofort_merchant_transaction.<a href="src/fern/sofort_merchant_transaction/client.py">list_all_sofort_merchant_transaction_for_user_monetary_account</a>(...) -> typing.List[SofortMerchantTransactionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.sofort_merchant_transaction.<a href="src/fern/sofort_merchant_transaction/client.py">read_sofort_merchant_transaction_for_user_monetary_account</a>(...) -> SofortMerchantTransactionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.switch_service_payment.<a href="src/fern/switch_service_payment/client.py">read_switch_service_payment_for_user_monetary_account</a>(...) -> BankSwitchServiceNetherlandsIncomingPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.translink_transaction.<a href="src/fern/translink_transaction/client.py">list_all_translink_transaction_for_user_monetary_account</a>(...) -> typing.List[TranslinkTransactionListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.translink_transaction.<a href="src/fern/translink_transaction/client.py">create_translink_transaction_for_user_monetary_account</a>(...) -> TranslinkTransactionCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.translink_transaction.create_translink_transaction_for_user_monetary_account(
    user_id=1,
    monetary_account_id=1,
    description="description",
    payments=[
        Payment()
    ],
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

**payments:** `typing.List[Payment]` — The list of payments we want to send in a single transaction.
    
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

<details><summary><code>client.translink_transaction.<a href="src/fern/translink_transaction/client.py">read_translink_transaction_for_user_monetary_account</a>(...) -> TranslinkTransactionRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">list_all_whitelist_sdd_for_user_monetary_account</a>(...) -> typing.List[WhitelistSddMonetaryAccountPayingListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">read_whitelist_sdd_for_user_monetary_account</a>(...) -> WhitelistSddMonetaryAccountPayingRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">list_all_whitelist_sdd_for_user</a>(...) -> typing.List[WhitelistSddListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.whitelist_sdd.<a href="src/fern/whitelist_sdd/client.py">read_whitelist_sdd_for_user</a>(...) -> WhitelistSddRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.notification_filter_email.<a href="src/fern/notification_filter_email/client.py">list_all_notification_filter_email_for_user</a>(...) -> typing.List[NotificationFilterEmailListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.notification_filter_email.<a href="src/fern/notification_filter_email/client.py">create_notification_filter_email_for_user</a>(...) -> NotificationFilterEmailCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NotificationFilterEmail` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.notification_filter_push.<a href="src/fern/notification_filter_push/client.py">list_all_notification_filter_push_for_user</a>(...) -> typing.List[NotificationFilterPushListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.notification_filter_push.<a href="src/fern/notification_filter_push/client.py">create_notification_filter_push_for_user</a>(...) -> NotificationFilterPushCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `NotificationFilterPush` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">list_all_oauth_client_for_user</a>(...) -> typing.List[OauthClientListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">create_oauth_client_for_user</a>(...) -> OauthClientCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `OauthClient` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">read_oauth_client_for_user</a>(...) -> OauthClientRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.oauth_client.<a href="src/fern/oauth_client/client.py">update_oauth_client_for_user</a>(...) -> OauthClientUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `OauthClient` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">list_all_callback_url_for_user_oauth_client</a>(...) -> typing.List[OauthCallbackUrlListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">create_callback_url_for_user_oauth_client</a>(...) -> OauthCallbackUrlCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `OauthCallbackUrl` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">read_callback_url_for_user_oauth_client</a>(...) -> OauthCallbackUrlRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">update_callback_url_for_user_oauth_client</a>(...) -> OauthCallbackUrlUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `OauthCallbackUrl` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.callback_url.<a href="src/fern/callback_url/client.py">delete_callback_url_for_user_oauth_client</a>(...) -> OauthCallbackUrlDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">list_all_payment_service_provider_draft_payment_for_user</a>(...) -> typing.List[PaymentServiceProviderDraftPaymentListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">create_payment_service_provider_draft_payment_for_user</a>(...) -> PaymentServiceProviderDraftPaymentCreate</code></summary>
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
from fern import FernApi, Amount
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PaymentServiceProviderDraftPayment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">read_payment_service_provider_draft_payment_for_user</a>(...) -> PaymentServiceProviderDraftPaymentRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.payment_service_provider_draft_payment.<a href="src/fern/payment_service_provider_draft_payment/client.py">update_payment_service_provider_draft_payment_for_user</a>(...) -> PaymentServiceProviderDraftPaymentUpdate</code></summary>
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
from fern import FernApi, Amount
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `PaymentServiceProviderDraftPayment` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.registry_settlement.<a href="src/fern/registry_settlement/client.py">list_all_registry_settlement_for_user_registry</a>(...) -> typing.List[RegistrySettlementListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.registry_settlement.<a href="src/fern/registry_settlement/client.py">create_registry_settlement_for_user_registry</a>(...) -> RegistrySettlementCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry_settlement.create_registry_settlement_for_user_registry(
    user_id=1,
    registry_id=1,
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

<details><summary><code>client.registry_settlement.<a href="src/fern/registry_settlement/client.py">read_registry_settlement_for_user_registry</a>(...) -> RegistrySettlementRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.reward.<a href="src/fern/reward/client.py">list_all_reward_for_user</a>(...) -> typing.List[RewardListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.reward.<a href="src/fern/reward/client.py">read_reward_for_user</a>(...) -> RewardRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.reward_recipient.<a href="src/fern/reward_recipient/client.py">list_all_reward_recipient_for_user</a>(...) -> typing.List[RewardRecipientListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.reward_recipient.<a href="src/fern/reward_recipient/client.py">read_reward_recipient_for_user</a>(...) -> RewardRecipientRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.reward_sender.<a href="src/fern/reward_sender/client.py">list_all_reward_sender_for_user</a>(...) -> typing.List[RewardSenderListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.reward_sender.<a href="src/fern/reward_sender/client.py">read_reward_sender_for_user</a>(...) -> RewardSenderRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.share_invite_monetary_account_response.<a href="src/fern/share_invite_monetary_account_response/client.py">list_all_share_invite_monetary_account_response_for_user</a>(...) -> typing.List[ShareInviteMonetaryAccountResponseListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.share_invite_monetary_account_response.<a href="src/fern/share_invite_monetary_account_response/client.py">read_share_invite_monetary_account_response_for_user</a>(...) -> ShareInviteMonetaryAccountResponseRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.share_invite_monetary_account_response.<a href="src/fern/share_invite_monetary_account_response/client.py">update_share_invite_monetary_account_response_for_user</a>(...) -> ShareInviteMonetaryAccountResponseUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `ShareInviteMonetaryAccountResponse` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.token_qr_request_ideal.<a href="src/fern/token_qr_request_ideal/client.py">create_token_qr_request_ideal_for_user</a>(...) -> TokenQrRequestIdealCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.token_qr_request_sofort.<a href="src/fern/token_qr_request_sofort/client.py">create_token_qr_request_sofort_for_user</a>(...) -> TokenQrRequestSofortCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.transferwise_currency.<a href="src/fern/transferwise_currency/client.py">list_all_transferwise_currency_for_user</a>(...) -> typing.List[TransferwiseCurrencyListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.transferwise_quote.<a href="src/fern/transferwise_quote/client.py">create_transferwise_quote_for_user</a>(...) -> TransferwiseQuoteCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `TransferwiseQuote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_quote.<a href="src/fern/transferwise_quote/client.py">read_transferwise_quote_for_user</a>(...) -> TransferwiseQuoteRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.transferwise_quote_temporary.<a href="src/fern/transferwise_quote_temporary/client.py">create_transferwise_quote_temporary_for_user</a>(...) -> TransferwiseQuoteTemporaryCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.transferwise_quote_temporary.<a href="src/fern/transferwise_quote_temporary/client.py">read_transferwise_quote_temporary_for_user</a>(...) -> TransferwiseQuoteTemporaryRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">list_all_transferwise_recipient_for_user_transferwise_quote</a>(...) -> typing.List[TransferwiseAccountQuoteListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">create_transferwise_recipient_for_user_transferwise_quote</a>(...) -> TransferwiseAccountQuoteCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**detail:** `typing.Optional[typing.List[TransferwiseRequirementField]]` — The fields which were specified as "required" and have since been filled by the user. Always provide the full list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">read_transferwise_recipient_for_user_transferwise_quote</a>(...) -> TransferwiseAccountQuoteRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.transferwise_recipient.<a href="src/fern/transferwise_recipient/client.py">delete_transferwise_recipient_for_user_transferwise_quote</a>(...) -> TransferwiseAccountQuoteDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.transferwise_recipient_requirement.<a href="src/fern/transferwise_recipient_requirement/client.py">list_all_transferwise_recipient_requirement_for_user_transferwise_quote</a>(...) -> typing.List[TransferwiseAccountRequirementListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.transferwise_recipient_requirement.<a href="src/fern/transferwise_recipient_requirement/client.py">create_transferwise_recipient_requirement_for_user_transferwise_quote</a>(...) -> TransferwiseAccountRequirementCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**detail:** `typing.Optional[typing.List[TransferwiseRequirementField]]` — The fields which were specified as "required" and have since been filled by the user. Always provide the full list.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.transferwise_transfer.<a href="src/fern/transferwise_transfer/client.py">list_all_transferwise_transfer_for_user_transferwise_quote</a>(...) -> typing.List[TransferwiseTransferListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.transferwise_transfer.<a href="src/fern/transferwise_transfer/client.py">create_transferwise_transfer_for_user_transferwise_quote</a>(...) -> TransferwiseTransferCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `TransferwiseTransfer` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transferwise_transfer.<a href="src/fern/transferwise_transfer/client.py">read_transferwise_transfer_for_user_transferwise_quote</a>(...) -> TransferwiseTransferRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.transferwise_transfer_requirement.<a href="src/fern/transferwise_transfer_requirement/client.py">create_transferwise_transfer_requirement_for_user_transferwise_quote</a>(...) -> TransferwiseTransferRequirementCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**detail:** `typing.Optional[typing.List[TransferwiseRequirementField]]` — The fields which were specified as "required" and have since been filled by the user. Always provide the full list.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.transferwise_user.<a href="src/fern/transferwise_user/client.py">list_all_transferwise_user_for_user</a>(...) -> typing.List[TransferwiseUserListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.transferwise_user.<a href="src/fern/transferwise_user/client.py">create_transferwise_user_for_user</a>(...) -> TransferwiseUserCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.tree_progress.<a href="src/fern/tree_progress/client.py">list_all_tree_progress_for_user</a>(...) -> typing.List[TreeProgressListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">list_all_whitelist_sdd_one_off_for_user</a>(...) -> typing.List[WhitelistSddOneOffListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">create_whitelist_sdd_one_off_for_user</a>(...) -> WhitelistSddOneOffCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `WhitelistSddOneOff` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">read_whitelist_sdd_one_off_for_user</a>(...) -> WhitelistSddOneOffRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">update_whitelist_sdd_one_off_for_user</a>(...) -> WhitelistSddOneOffUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `WhitelistSddOneOff` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_one_off.<a href="src/fern/whitelist_sdd_one_off/client.py">delete_whitelist_sdd_one_off_for_user</a>(...) -> WhitelistSddOneOffDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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
<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">list_all_whitelist_sdd_recurring_for_user</a>(...) -> typing.List[WhitelistSddRecurringListing]</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">create_whitelist_sdd_recurring_for_user</a>(...) -> WhitelistSddRecurringCreate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `WhitelistSddRecurring` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">read_whitelist_sdd_recurring_for_user</a>(...) -> WhitelistSddRecurringRead</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">update_whitelist_sdd_recurring_for_user</a>(...) -> WhitelistSddRecurringUpdate</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `WhitelistSddRecurring` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whitelist_sdd_recurring.<a href="src/fern/whitelist_sdd_recurring/client.py">delete_whitelist_sdd_recurring_for_user</a>(...) -> WhitelistSddRecurringDelete</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    bunq_client_authentication="<X-Bunq-Client-Authentication>",
    environment=FernApiEnvironment.DEFAULT,
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

