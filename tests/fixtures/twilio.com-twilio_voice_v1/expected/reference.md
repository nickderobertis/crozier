# Reference
<details><summary><code>client.<a href="src/fern/client.py">delete_archived_call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from fern import FernApi

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.delete_archived_call(
    date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
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

**date:** `dt.date` — The date of the Call in UTC.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The Twilio-provided Call SID that uniquely identifies the Call resource to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_byoc_trunk</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.list_byoc_trunk()

```
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

<details><summary><code>client.<a href="src/fern/client.py">create_byoc_trunk</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.create_byoc_trunk()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cnam_lookup_enabled:** `typing.Optional[bool]` — Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    
</dd>
</dl>

<dl>
<dd>

**connection_policy_sid:** `typing.Optional[str]` — The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**from_domain_sid:** `typing.Optional[str]` — The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com".
    
</dd>
</dl>

<dl>
<dd>

**status_callback_method:** `typing.Optional[CreateByocTrunkRequestStatusCallbackMethod]` — The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
    
</dd>
</dl>

<dl>
<dd>

**status_callback_url:** `typing.Optional[str]` — The URL that we should call to pass status parameters (such as call ended) to your application.
    
</dd>
</dl>

<dl>
<dd>

**voice_fallback_method:** `typing.Optional[CreateByocTrunkRequestVoiceFallbackMethod]` — The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    
</dd>
</dl>

<dl>
<dd>

**voice_fallback_url:** `typing.Optional[str]` — The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.
    
</dd>
</dl>

<dl>
<dd>

**voice_method:** `typing.Optional[CreateByocTrunkRequestVoiceMethod]` — The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
    
</dd>
</dl>

<dl>
<dd>

**voice_url:** `typing.Optional[str]` — The URL we should call when the BYOC Trunk receives a call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_byoc_trunk</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.fetch_byoc_trunk(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_byoc_trunk</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.update_byoc_trunk(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.
    
</dd>
</dl>

<dl>
<dd>

**cnam_lookup_enabled:** `typing.Optional[bool]` — Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    
</dd>
</dl>

<dl>
<dd>

**connection_policy_sid:** `typing.Optional[str]` — The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**from_domain_sid:** `typing.Optional[str]` — The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com".
    
</dd>
</dl>

<dl>
<dd>

**status_callback_method:** `typing.Optional[UpdateByocTrunkRequestStatusCallbackMethod]` — The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
    
</dd>
</dl>

<dl>
<dd>

**status_callback_url:** `typing.Optional[str]` — The URL that we should call to pass status parameters (such as call ended) to your application.
    
</dd>
</dl>

<dl>
<dd>

**voice_fallback_method:** `typing.Optional[UpdateByocTrunkRequestVoiceFallbackMethod]` — The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    
</dd>
</dl>

<dl>
<dd>

**voice_fallback_url:** `typing.Optional[str]` — The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
    
</dd>
</dl>

<dl>
<dd>

**voice_method:** `typing.Optional[UpdateByocTrunkRequestVoiceMethod]` — The HTTP method we should use to call `voice_url`
    
</dd>
</dl>

<dl>
<dd>

**voice_url:** `typing.Optional[str]` — The URL we should call when the BYOC Trunk receives a call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_byoc_trunk</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.delete_byoc_trunk(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_connection_policy</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.list_connection_policy()

```
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

<details><summary><code>client.<a href="src/fern/client.py">create_connection_policy</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.create_connection_policy()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_connection_policy_target</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.list_connection_policy_target(
    connection_policy_sid="ConnectionPolicySid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_policy_sid:** `str` — The SID of the Connection Policy from which to read the Targets.
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_connection_policy_target</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.create_connection_policy_target(
    connection_policy_sid="ConnectionPolicySid",
    target="Target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_policy_sid:** `str` — The SID of the Connection Policy that owns the Target.
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` — The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the Target is enabled. The default is `true`.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` — The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
    
</dd>
</dl>

<dl>
<dd>

**weight:** `typing.Optional[int]` — The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_connection_policy_target</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.fetch_connection_policy_target(
    connection_policy_sid="ConnectionPolicySid",
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

**connection_policy_sid:** `str` — The SID of the Connection Policy that owns the Target.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The unique string that we created to identify the Target resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_connection_policy_target</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.update_connection_policy_target(
    connection_policy_sid="ConnectionPolicySid",
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

**connection_policy_sid:** `str` — The SID of the Connection Policy that owns the Target.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The unique string that we created to identify the Target resource to update.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the Target is enabled.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` — The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[str]` — The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
    
</dd>
</dl>

<dl>
<dd>

**weight:** `typing.Optional[int]` — The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_connection_policy_target</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.delete_connection_policy_target(
    connection_policy_sid="ConnectionPolicySid",
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

**connection_policy_sid:** `str` — The SID of the Connection Policy that owns the Target.
    
</dd>
</dl>

<dl>
<dd>

**sid:** `str` — The unique string that we created to identify the Target resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_connection_policy</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.fetch_connection_policy(
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

**sid:** `str` — The unique string that we created to identify the Connection Policy resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_connection_policy</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.update_connection_policy(
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

**sid:** `str` — The unique string that we created to identify the Connection Policy resource to update.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_connection_policy</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.delete_connection_policy(
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

**sid:** `str` — The unique string that we created to identify the Connection Policy resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_dialing_permissions_country_bulk_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.create_dialing_permissions_country_bulk_update(
    update_request="UpdateRequest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**update_request:** `str` — URL encoded JSON array of update objects. example : `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_dialing_permissions_country</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all voice dialing country permissions for this account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.list_dialing_permissions_country()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**iso_code:** `typing.Optional[str]` — Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
    
</dd>
</dl>

<dl>
<dd>

**continent:** `typing.Optional[str]` — Filter to retrieve the country permissions by specifying the continent
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` — Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
    
</dd>
</dl>

<dl>
<dd>

**low_risk_numbers_enabled:** `typing.Optional[bool]` — Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.
    
</dd>
</dl>

<dl>
<dd>

**high_risk_special_numbers_enabled:** `typing.Optional[bool]` — Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`
    
</dd>
</dl>

<dl>
<dd>

**high_risk_tollfraud_numbers_enabled:** `typing.Optional[bool]` — Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers enabled. Can be: `true` or `false`.
    
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

<details><summary><code>client.<a href="src/fern/client.py">fetch_dialing_permissions_country</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve voice dialing country permissions identified by the given ISO country code
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.fetch_dialing_permissions_country(
    iso_code="IsoCode",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**iso_code:** `str` — The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_dialing_permissions_hrs_prefixes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the high-risk special services prefixes from the country resource corresponding to the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.list_dialing_permissions_hrs_prefixes(
    iso_code="IsoCode",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**iso_code:** `str` — The [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to identify the country permissions from which high-risk special service number prefixes are fetched
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_ip_record</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.list_ip_record()

```
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

<details><summary><code>client.<a href="src/fern/client.py">create_ip_record</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.create_ip_record(
    ip_address="IpAddress",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ip_address:** `str` — An IP address in dotted decimal notation, IPv4 only.
    
</dd>
</dl>

<dl>
<dd>

**cidr_prefix_length:** `typing.Optional[int]` — An integer representing the length of the [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address. By default the entire IP address is used, which for IPv4 is value 32.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_ip_record</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.fetch_ip_record(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the IP Record resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_ip_record</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.update_ip_record(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the IP Record resource to update.
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_ip_record</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.delete_ip_record(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the IP Record resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_dialing_permissions_settings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve voice dialing permissions inheritance for the sub-account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.fetch_dialing_permissions_settings()

```
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

<details><summary><code>client.<a href="src/fern/client.py">update_dialing_permissions_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update voice dialing permissions inheritance for the sub-account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.update_dialing_permissions_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dialing_permissions_inheritance:** `typing.Optional[bool]` — `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_source_ip_mapping</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.list_source_ip_mapping()

```
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

<details><summary><code>client.<a href="src/fern/client.py">create_source_ip_mapping</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.create_source_ip_mapping(
    ip_record_sid="IpRecordSid",
    sip_domain_sid="SipDomainSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ip_record_sid:** `str` — The Twilio-provided string that uniquely identifies the IP Record resource to map from.
    
</dd>
</dl>

<dl>
<dd>

**sip_domain_sid:** `str` — The SID of the SIP Domain that the IP Record should be mapped to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_source_ip_mapping</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.fetch_source_ip_mapping(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the IP Record resource to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_source_ip_mapping</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.update_source_ip_mapping(
    sid="Sid",
    sip_domain_sid="SipDomainSid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sid:** `str` — The Twilio-provided string that uniquely identifies the IP Record resource to update.
    
</dd>
</dl>

<dl>
<dd>

**sip_domain_sid:** `str` — The SID of the SIP Domain that the IP Record should be mapped to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_source_ip_mapping</a>(...)</code></summary>
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

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.delete_source_ip_mapping(
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

**sid:** `str` — The Twilio-provided string that uniquely identifies the IP Record resource to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

