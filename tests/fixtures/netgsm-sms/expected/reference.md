# Reference
## BulkSms
<details><summary><code>client.bulk_sms.<a href="src/fern/bulk_sms/client.py">send_rest_sms</a>(...) -> RestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send SMS via REST protocol
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.bulk_sms import RestSendRequestMessagesItem

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bulk_sms.send_rest_sms(
    msgheader="msgheader",
    messages=[
        RestSendRequestMessagesItem()
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

**msgheader:** `str` — Message header/sender ID
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[RestSendRequestMessagesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**appname:** `typing.Optional[str]` — Application name
    
</dd>
</dl>

<dl>
<dd>

**encoding:** `typing.Optional[str]` — Message encoding
    
</dd>
</dl>

<dl>
<dd>

**iysfilter:** `typing.Optional[str]` — IYS filter
    
</dd>
</dl>

<dl>
<dd>

**partnercode:** `typing.Optional[str]` — Partner code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sms.<a href="src/fern/bulk_sms/client.py">cancel_sms</a>(...) -> CancelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a scheduled SMS
</dd>
</dl>
</dd>
</dl>

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

client.bulk_sms.cancel_sms(
    jobid="jobid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**jobid:** `str` — Job ID of the SMS to cancel
    
</dd>
</dl>

<dl>
<dd>

**appname:** `typing.Optional[str]` — Application name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Queries
<details><summary><code>client.queries.<a href="src/fern/queries/client.py">get_sms_headers</a>(...) -> MsgHeaderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get user's SMS headers
</dd>
</dl>
</dd>
</dl>

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

client.queries.get_sms_headers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**appname:** `typing.Optional[str]` — Application name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queries.<a href="src/fern/queries/client.py">get_inbox_messages</a>(...) -> SmsInboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List SMS messages received by your subscriber number
</dd>
</dl>
</dd>
</dl>

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

client.queries.get_inbox_messages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**appname:** `typing.Optional[str]` — Application name
    
</dd>
</dl>

<dl>
<dd>

**startdate:** `typing.Optional[str]` — Start date (e.g., ddMMyyyyHHmmss)
    
</dd>
</dl>

<dl>
<dd>

**stopdate:** `typing.Optional[str]` — End date (e.g., ddMMyyyyHHmmss)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queries.<a href="src/fern/queries/client.py">get_sms_report</a>(...) -> ReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get delivery status report for sent SMS messages
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.queries.get_sms_report(
    startdate=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    stopdate=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**startdate:** `datetime.datetime` — Start date
    
</dd>
</dl>

<dl>
<dd>

**stopdate:** `datetime.datetime` — End date
    
</dd>
</dl>

<dl>
<dd>

**appname:** `typing.Optional[str]` — Application name
    
</dd>
</dl>

<dl>
<dd>

**jobids:** `typing.Optional[typing.List[str]]` — Message IDs to query
    
</dd>
</dl>

<dl>
<dd>

**pagenumber:** `typing.Optional[int]` — Page number (starts from 0)
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Records per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

