# Reference
<details><summary><code>client.<a href="src/fern/client.py">fetch_deactivation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a list of all United States numbers that have been deactivated on a specific date.
</dd>
</dl>
</dd>
</dl>

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

client.fetch_deactivation()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date:** `typing.Optional[datetime.date]` — The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_domain_cert_v4</a>(...) -> MessagingV1DomainCertV4</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_domain_cert_v4(
    domain_sid="DomainSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_sid:** `str` — Unique string used to identify the domain that this certificate should be associated with.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_domain_cert_v4</a>(...) -> MessagingV1DomainCertV4</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.update_domain_cert_v4(
    domain_sid="DomainSid",
    tls_cert="TlsCert",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_sid:** `str` — Unique string used to identify the domain that this certificate should be associated with.
    
</dd>
</dl>

<dl>
<dd>

**tls_cert:** `str` — Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_domain_cert_v4</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.delete_domain_cert_v4(
    domain_sid="DomainSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_sid:** `str` — Unique string used to identify the domain that this certificate should be associated with.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_domain_config</a>(...) -> MessagingV1DomainConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_domain_config(
    domain_sid="DomainSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_sid:** `str` — Unique string used to identify the domain that this config should be associated with.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_domain_config</a>(...) -> MessagingV1DomainConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.update_domain_config(
    domain_sid="DomainSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_sid:** `str` — Unique string used to identify the domain that this config should be associated with.
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — URL to receive click events to your webhook whenever the recipients click on the shortened links
    
</dd>
</dl>

<dl>
<dd>

**fallback_url:** `typing.Optional[str]` — Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_linkshortening_messaging_service</a>(...) -> MessagingV1LinkshorteningMessagingService</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_linkshortening_messaging_service(
    domain_sid="DomainSid",
    messaging_service_sid="MessagingServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_sid:** `str` — The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
    
</dd>
</dl>

<dl>
<dd>

**messaging_service_sid:** `str` — A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_linkshortening_messaging_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.delete_linkshortening_messaging_service(
    domain_sid="DomainSid",
    messaging_service_sid="MessagingServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_sid:** `str` — The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
    
</dd>
</dl>

<dl>
<dd>

**messaging_service_sid:** `str` — A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_domain_config_messaging_service</a>(...) -> MessagingV1DomainConfigMessagingService</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_domain_config_messaging_service(
    messaging_service_sid="MessagingServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**messaging_service_sid:** `str` — Unique string used to identify the Messaging service that this domain should be associated with.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_service</a>(...) -> ListServiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_service()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_service</a>(...) -> MessagingV1Service</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_service(
    friendly_name="FriendlyName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**friendly_name:** `str` — A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    
</dd>
</dl>

<dl>
<dd>

**area_code_geomatch:** `typing.Optional[bool]` — Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.
    
</dd>
</dl>

<dl>
<dd>

**fallback_method:** `typing.Optional[CreateServiceRequestFallbackMethod]` — The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
    
</dd>
</dl>

<dl>
<dd>

**fallback_to_long_code:** `typing.Optional[bool]` — Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**fallback_url:** `typing.Optional[str]` — The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
    
</dd>
</dl>

<dl>
<dd>

**inbound_method:** `typing.Optional[CreateServiceRequestInboundMethod]` — The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
    
</dd>
</dl>

<dl>
<dd>

**inbound_request_url:** `typing.Optional[str]` — The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
    
</dd>
</dl>

<dl>
<dd>

**mms_converter:** `typing.Optional[bool]` — Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**scan_message_content:** `typing.Optional[ServiceEnumScanMessageContent]` — Reserved.
    
</dd>
</dl>

<dl>
<dd>

**smart_encoding:** `typing.Optional[bool]` — Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**status_callback:** `typing.Optional[str]` — The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
    
</dd>
</dl>

<dl>
<dd>

**sticky_sender:** `typing.Optional[bool]` — Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**synchronous_validation:** `typing.Optional[bool]` — Reserved.
    
</dd>
</dl>

<dl>
<dd>

**use_inbound_webhook_on_number:** `typing.Optional[bool]` — A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.
    
</dd>
</dl>

<dl>
<dd>

**usecase:** `typing.Optional[str]` — A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..].
    
</dd>
</dl>

<dl>
<dd>

**validity_period:** `typing.Optional[int]` — How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_external_campaign</a>(...) -> MessagingV1ExternalCampaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_external_campaign(
    campaign_id="CampaignId",
    messaging_service_sid="MessagingServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — ID of the preregistered campaign.
    
</dd>
</dl>

<dl>
<dd>

**messaging_service_sid:** `str` — The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_usecase</a>() -> MessagingV1Usecase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_usecase()

```
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

<details><summary><code>client.<a href="src/fern/client.py">list_us_app_to_person</a>(...) -> ListUsAppToPersonResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_us_app_to_person(
    messaging_service_sid="MessagingServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**messaging_service_sid:** `str` — The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_us_app_to_person</a>(...) -> MessagingV1ServiceUsAppToPerson</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_us_app_to_person(
    messaging_service_sid="MessagingServiceSid",
    brand_registration_sid="BrandRegistrationSid",
    description="Description",
    has_embedded_links=True,
    has_embedded_phone=True,
    message_flow="MessageFlow",
    message_samples=[
        "MessageSamples"
    ],
    us_app_to_person_usecase="UsAppToPersonUsecase",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**messaging_service_sid:** `str` — The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to create the resources from.
    
</dd>
</dl>

<dl>
<dd>

**brand_registration_sid:** `str` — A2P Brand Registration SID
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
    
</dd>
</dl>

<dl>
<dd>

**has_embedded_links:** `bool` — Indicates that this SMS campaign will send messages that contain links.
    
</dd>
</dl>

<dl>
<dd>

**has_embedded_phone:** `bool` — Indicates that this SMS campaign will send messages that contain phone numbers.
    
</dd>
</dl>

<dl>
<dd>

**message_flow:** `str` — Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
    
</dd>
</dl>

<dl>
<dd>

**message_samples:** `typing.List[str]` — Message samples, at least 1 and up to 5 sample messages (at least 2 for sole proprietor), >=20 chars, <=1024 chars each.
    
</dd>
</dl>

<dl>
<dd>

**us_app_to_person_usecase:** `str` — A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
    
</dd>
</dl>

<dl>
<dd>

**help_keywords:** `typing.Optional[typing.List[str]]` — End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    
</dd>
</dl>

<dl>
<dd>

**help_message:** `typing.Optional[str]` — When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_keywords:** `typing.Optional[typing.List[str]]` — If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_message:** `typing.Optional[str]` — If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
    
</dd>
</dl>

<dl>
<dd>

**opt_out_keywords:** `typing.Optional[typing.List[str]]` — End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    
</dd>
</dl>

<dl>
<dd>

**opt_out_message:** `typing.Optional[str]` — Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_us_app_to_person_usecase</a>(...) -> MessagingV1ServiceUsAppToPersonUsecase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_us_app_to_person_usecase(
    messaging_service_sid="MessagingServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**messaging_service_sid:** `str` — The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.
    
</dd>
</dl>

<dl>
<dd>

**brand_registration_sid:** `typing.Optional[str]` — The unique string to identify the A2P brand.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_us_app_to_person</a>(...) -> MessagingV1ServiceUsAppToPerson</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_us_app_to_person(
    messaging_service_sid="MessagingServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**messaging_service_sid:** `str` — The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_us_app_to_person</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.delete_us_app_to_person(
    messaging_service_sid="MessagingServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**messaging_service_sid:** `str` — The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to delete the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the US A2P Compliance resource to delete `QE2c6890da8086d771620e9b13fadeba0b`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_alpha_sender</a>(...) -> ListAlphaSenderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_alpha_sender(
    service_sid="ServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_alpha_sender</a>(...) -> MessagingV1ServiceAlphaSender</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_alpha_sender(
    service_sid="ServiceSid",
    alpha_sender="AlphaSender",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.
    
</dd>
</dl>

<dl>
<dd>

**alpha_sender:** `str` — The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z, a-z, 0-9, space, hyphen `-`, plus `+`, underscore `_` and ampersand `&`. This value cannot contain only numbers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_alpha_sender</a>(...) -> MessagingV1ServiceAlphaSender</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_alpha_sender(
    service_sid="ServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the AlphaSender resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_alpha_sender</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.delete_alpha_sender(
    service_sid="ServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the AlphaSender resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_phone_number</a>(...) -> ListPhoneNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_phone_number(
    service_sid="ServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_phone_number</a>(...) -> MessagingV1ServicePhoneNumber</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_phone_number(
    service_sid="ServiceSid",
    phone_number_sid="PhoneNumberSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_sid:** `str` — The SID of the Phone Number being added to the Service.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_phone_number</a>(...) -> MessagingV1ServicePhoneNumber</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_phone_number(
    service_sid="ServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the PhoneNumber resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_phone_number</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.delete_phone_number(
    service_sid="ServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the PhoneNumber resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_short_code</a>(...) -> ListShortCodeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_short_code(
    service_sid="ServiceSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_short_code</a>(...) -> MessagingV1ServiceShortCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_short_code(
    service_sid="ServiceSid",
    short_code_sid="ShortCodeSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.
    
</dd>
</dl>

<dl>
<dd>

**short_code_sid:** `str` — The SID of the ShortCode resource being added to the Service.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_short_code</a>(...) -> MessagingV1ServiceShortCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_short_code(
    service_sid="ServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the ShortCode resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_short_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.delete_short_code(
    service_sid="ServiceSid",
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_sid:** `str` — The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The SID of the ShortCode resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_service</a>(...) -> MessagingV1Service</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_service(
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The SID of the Service resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_service</a>(...) -> MessagingV1Service</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.update_service(
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The SID of the Service resource to update.
    
</dd>
</dl>

<dl>
<dd>

**area_code_geomatch:** `typing.Optional[bool]` — Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.
    
</dd>
</dl>

<dl>
<dd>

**fallback_method:** `typing.Optional[UpdateServiceRequestFallbackMethod]` — The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
    
</dd>
</dl>

<dl>
<dd>

**fallback_to_long_code:** `typing.Optional[bool]` — Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**fallback_url:** `typing.Optional[str]` — The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    
</dd>
</dl>

<dl>
<dd>

**inbound_method:** `typing.Optional[UpdateServiceRequestInboundMethod]` — The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
    
</dd>
</dl>

<dl>
<dd>

**inbound_request_url:** `typing.Optional[str]` — The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
    
</dd>
</dl>

<dl>
<dd>

**mms_converter:** `typing.Optional[bool]` — Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**scan_message_content:** `typing.Optional[ServiceEnumScanMessageContent]` — Reserved.
    
</dd>
</dl>

<dl>
<dd>

**smart_encoding:** `typing.Optional[bool]` — Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**status_callback:** `typing.Optional[str]` — The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
    
</dd>
</dl>

<dl>
<dd>

**sticky_sender:** `typing.Optional[bool]` — Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.
    
</dd>
</dl>

<dl>
<dd>

**synchronous_validation:** `typing.Optional[bool]` — Reserved.
    
</dd>
</dl>

<dl>
<dd>

**use_inbound_webhook_on_number:** `typing.Optional[bool]` — A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.
    
</dd>
</dl>

<dl>
<dd>

**usecase:** `typing.Optional[str]` — A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..]
    
</dd>
</dl>

<dl>
<dd>

**validity_period:** `typing.Optional[int]` — How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.delete_service(
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The SID of the Service resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_tollfree_verification</a>(...) -> ListTollfreeVerificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_tollfree_verification()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tollfree_phone_number_sid:** `typing.Optional[str]` — The SID of the Phone Number associated with the Tollfree Verification.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TollfreeVerificationEnumStatus]` — The compliance status of the Tollfree Verification record.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_tollfree_verification</a>(...) -> MessagingV1TollfreeVerification</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TollfreeVerificationEnumOptInType
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.create_tollfree_verification(
    business_name="BusinessName",
    business_website="BusinessWebsite",
    message_volume="MessageVolume",
    notification_email="NotificationEmail",
    opt_in_image_urls=[
        "OptInImageUrls"
    ],
    opt_in_type=TollfreeVerificationEnumOptInType.VERBAL,
    production_message_sample="ProductionMessageSample",
    tollfree_phone_number_sid="TollfreePhoneNumberSid",
    use_case_categories=[
        "UseCaseCategories"
    ],
    use_case_summary="UseCaseSummary",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**business_name:** `str` — The name of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_website:** `str` — The website of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**message_volume:** `str` — Estimate monthly volume of messages from the Tollfree Number.
    
</dd>
</dl>

<dl>
<dd>

**notification_email:** `str` — The email address to receive the notification about the verification result. .
    
</dd>
</dl>

<dl>
<dd>

**opt_in_image_urls:** `typing.List[str]` — Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_type:** `TollfreeVerificationEnumOptInType` — Describe how a user opts-in to text messages.
    
</dd>
</dl>

<dl>
<dd>

**production_message_sample:** `str` — An example of message content, i.e. a sample message.
    
</dd>
</dl>

<dl>
<dd>

**tollfree_phone_number_sid:** `str` — The SID of the Phone Number associated with the Tollfree Verification.
    
</dd>
</dl>

<dl>
<dd>

**use_case_categories:** `typing.List[str]` — The category of the use case for the Tollfree Number. List as many are applicable..
    
</dd>
</dl>

<dl>
<dd>

**use_case_summary:** `str` — Use this to further explain how messaging is used by the business or organization.
    
</dd>
</dl>

<dl>
<dd>

**additional_information:** `typing.Optional[str]` — Additional information to be provided for verification.
    
</dd>
</dl>

<dl>
<dd>

**business_city:** `typing.Optional[str]` — The city of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_email:** `typing.Optional[str]` — The email address of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_first_name:** `typing.Optional[str]` — The first name of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_last_name:** `typing.Optional[str]` — The last name of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_phone:** `typing.Optional[str]` — The phone number of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_country:** `typing.Optional[str]` — The country of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_postal_code:** `typing.Optional[str]` — The postal code of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_state_province_region:** `typing.Optional[str]` — The state/province/region of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_street_address:** `typing.Optional[str]` — The address of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_street_address2:** `typing.Optional[str]` — The address of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**customer_profile_sid:** `typing.Optional[str]` — Customer's Profile Bundle BundleSid.
    
</dd>
</dl>

<dl>
<dd>

**external_reference_id:** `typing.Optional[str]` — An optional external reference ID supplied by customer and echoed back on status retrieval.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_tollfree_verification</a>(...) -> MessagingV1TollfreeVerification</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_tollfree_verification(
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The unique string to identify Tollfree Verification.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_tollfree_verification</a>(...) -> MessagingV1TollfreeVerification</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.update_tollfree_verification(
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The unique string to identify Tollfree Verification.
    
</dd>
</dl>

<dl>
<dd>

**additional_information:** `typing.Optional[str]` — Additional information to be provided for verification.
    
</dd>
</dl>

<dl>
<dd>

**business_city:** `typing.Optional[str]` — The city of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_email:** `typing.Optional[str]` — The email address of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_first_name:** `typing.Optional[str]` — The first name of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_last_name:** `typing.Optional[str]` — The last name of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_phone:** `typing.Optional[str]` — The phone number of the contact for the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_country:** `typing.Optional[str]` — The country of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_name:** `typing.Optional[str]` — The name of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_postal_code:** `typing.Optional[str]` — The postal code of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_state_province_region:** `typing.Optional[str]` — The state/province/region of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_street_address:** `typing.Optional[str]` — The address of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_street_address2:** `typing.Optional[str]` — The address of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**business_website:** `typing.Optional[str]` — The website of the business or organization using the Tollfree number.
    
</dd>
</dl>

<dl>
<dd>

**message_volume:** `typing.Optional[str]` — Estimate monthly volume of messages from the Tollfree Number.
    
</dd>
</dl>

<dl>
<dd>

**notification_email:** `typing.Optional[str]` — The email address to receive the notification about the verification result. .
    
</dd>
</dl>

<dl>
<dd>

**opt_in_image_urls:** `typing.Optional[typing.List[str]]` — Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_type:** `typing.Optional[TollfreeVerificationEnumOptInType]` — Describe how a user opts-in to text messages.
    
</dd>
</dl>

<dl>
<dd>

**production_message_sample:** `typing.Optional[str]` — An example of message content, i.e. a sample message.
    
</dd>
</dl>

<dl>
<dd>

**use_case_categories:** `typing.Optional[typing.List[str]]` — The category of the use case for the Tollfree Number. List as many are applicable..
    
</dd>
</dl>

<dl>
<dd>

**use_case_summary:** `typing.Optional[str]` — Use this to further explain how messaging is used by the business or organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_brand_registrations</a>(...) -> ListBrandRegistrationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_brand_registrations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_brand_registrations</a>(...) -> MessagingV1BrandRegistrations</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_brand_registrations(
    a2p_profile_bundle_sid="A2PProfileBundleSid",
    customer_profile_bundle_sid="CustomerProfileBundleSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**a2p_profile_bundle_sid:** `str` — A2P Messaging Profile Bundle Sid.
    
</dd>
</dl>

<dl>
<dd>

**customer_profile_bundle_sid:** `str` — Customer Profile Bundle Sid.
    
</dd>
</dl>

<dl>
<dd>

**brand_type:** `typing.Optional[str]` — Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
    
</dd>
</dl>

<dl>
<dd>

**mock:** `typing.Optional[bool]` — A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
    
</dd>
</dl>

<dl>
<dd>

**skip_automatic_sec_vet:** `typing.Optional[bool]` — A flag to disable automatic secondary vetting for brands which it would otherwise be done.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_brand_registration_otp</a>(...) -> MessagingV1BrandRegistrationsBrandRegistrationOtp</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.create_brand_registration_otp(
    brand_registration_sid="BrandRegistrationSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand_registration_sid:** `str` — Brand Registration Sid of Sole Proprietor Brand.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_brand_vetting</a>(...) -> ListBrandVettingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.list_brand_vetting(
    brand_sid="BrandSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand_sid:** `str` — The SID of the Brand Registration resource of the vettings to read .
    
</dd>
</dl>

<dl>
<dd>

**vetting_provider:** `typing.Optional[BrandVettingEnumVettingProvider]` — The third-party provider of the vettings to read
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many resources to return in each list page. The default is 50, and the maximum is 1000.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page index. This value is simply for client state.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The page token. This is provided by the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_brand_vetting</a>(...) -> MessagingV1BrandRegistrationsBrandVetting</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, BrandVettingEnumVettingProvider
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.create_brand_vetting(
    brand_sid="BrandSid",
    vetting_provider=BrandVettingEnumVettingProvider.CAMPAIGN_VERIFY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand_sid:** `str` — The SID of the Brand Registration resource of the vettings to create .
    
</dd>
</dl>

<dl>
<dd>

**vetting_provider:** `BrandVettingEnumVettingProvider` — The third-party provider of the vettings to create .
    
</dd>
</dl>

<dl>
<dd>

**vetting_id:** `typing.Optional[str]` — The unique ID of the vetting
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_brand_vetting</a>(...) -> MessagingV1BrandRegistrationsBrandVetting</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_brand_vetting(
    brand_sid="BrandSid",
    brand_vetting_sid="BrandVettingSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand_sid:** `str` — The SID of the Brand Registration resource of the vettings to read .
    
</dd>
</dl>

<dl>
<dd>

**brand_vetting_sid:** `str` — The Twilio SID of the third-party vetting record.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_brand_registrations</a>(...) -> MessagingV1BrandRegistrations</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.fetch_brand_registrations(
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The SID of the Brand Registration resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_brand_registrations</a>(...) -> MessagingV1BrandRegistrations</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

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

client.update_brand_registrations(
    sid="Sid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The SID of the Brand Registration resource to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

