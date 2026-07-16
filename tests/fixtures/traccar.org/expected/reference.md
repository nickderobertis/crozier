# Reference
## Attributes
<details><summary><code>client.attributes.<a href="src/fern/attributes/client.py">fetch_a_list_of_attributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without params, it returns a list of Attributes the user has access to
</dd>
</dl>
</dd>
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
client.attributes.fetch_a_list_of_attributes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Standard users can use this only with _deviceId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Standard users can use this only with _groupId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/fern/attributes/client.py">create_an_attribute</a>(...)</code></summary>
<dl>
<dd>

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
client.attributes.create_an_attribute()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expression:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — String|Number|Boolean
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/fern/attributes/client.py">update_an_attribute</a>(...)</code></summary>
<dl>
<dd>

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
client.attributes.update_an_attribute(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attribute:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expression:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — String|Number|Boolean
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/fern/attributes/client.py">delete_an_attribute</a>(...)</code></summary>
<dl>
<dd>

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
client.attributes.delete_an_attribute(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Calendars
<details><summary><code>client.calendars.<a href="src/fern/calendars/client.py">fetch_a_list_of_calendars</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without params, it returns a list of Calendars the user has access to
</dd>
</dl>
</dd>
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
client.calendars.fetch_a_list_of_calendars()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calendars.<a href="src/fern/calendars/client.py">create_a_calendar</a>(...)</code></summary>
<dl>
<dd>

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
client.calendars.create_a_calendar()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[CalendarAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[str]` — base64 encoded in iCalendar format
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calendars.<a href="src/fern/calendars/client.py">update_a_calendar</a>(...)</code></summary>
<dl>
<dd>

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
client.calendars.update_a_calendar(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[CalendarAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[str]` — base64 encoded in iCalendar format
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calendars.<a href="src/fern/calendars/client.py">delete_a_calendar</a>(...)</code></summary>
<dl>
<dd>

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
client.calendars.delete_a_calendar(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Commands
<details><summary><code>client.commands.<a href="src/fern/commands/client.py">fetch_a_list_of_saved_commands</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without params, it returns a list of Saved Commands the user has access to
</dd>
</dl>
</dd>
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
client.commands.fetch_a_list_of_saved_commands()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Standard users can use this only with _deviceId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Standard users can use this only with _groupId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commands.<a href="src/fern/commands/client.py">create_a_saved_command</a>(...)</code></summary>
<dl>
<dd>

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
client.commands.create_a_saved_command()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[CommandAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commands.<a href="src/fern/commands/client.py">fetch_a_list_of_saved_commands_supported_by_device_at_the_moment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support
</dd>
</dl>
</dd>
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
client.commands.fetch_a_list_of_saved_commands_supported_by_device_at_the_moment()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Standard users can use this only with _deviceId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commands.<a href="src/fern/commands/client.py">dispatch_commands_to_device</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Dispatch a new command or Saved Command if _body.id_ set
</dd>
</dl>
</dd>
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
client.commands.dispatch_commands_to_device()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[CommandAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commands.<a href="src/fern/commands/client.py">fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited</a>(...)</code></summary>
<dl>
<dd>

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
client.commands.fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Internal device identifier. Only works if device has already reported some locations
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `typing.Optional[str]` — Protocol name. Can be used instead of device id
    
</dd>
</dl>

<dl>
<dd>

**text_channel:** `typing.Optional[bool]` — When `true` return SMS commands. If not specified or `false` return data commands
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commands.<a href="src/fern/commands/client.py">update_a_saved_command</a>(...)</code></summary>
<dl>
<dd>

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
client.commands.update_a_saved_command(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[CommandAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commands.<a href="src/fern/commands/client.py">delete_a_saved_command</a>(...)</code></summary>
<dl>
<dd>

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
client.commands.delete_a_saved_command(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Devices
<details><summary><code>client.devices.<a href="src/fern/devices/client.py">fetch_a_list_of_devices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without any params, returns a list of the user's devices
</dd>
</dl>
</dd>
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
client.devices.fetch_a_list_of_devices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — To fetch one or more devices. Multiple params can be passed like `id=31&id=42`
    
</dd>
</dl>

<dl>
<dd>

**unique_id:** `typing.Optional[str]` — To fetch one or more devices. Multiple params can be passed like `uniqueId=333331&uniqieId=44442`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.<a href="src/fern/devices/client.py">create_a_device</a>(...)</code></summary>
<dl>
<dd>

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
client.devices.create_a_device()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[DeviceAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**geofence_ids:** `typing.Optional[typing.Sequence[int]]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**last_update:** `typing.Optional[dt.datetime]` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**position_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unique_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.<a href="src/fern/devices/client.py">update_a_device</a>(...)</code></summary>
<dl>
<dd>

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
client.devices.update_a_device(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[DeviceAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**geofence_ids:** `typing.Optional[typing.Sequence[int]]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**last_update:** `typing.Optional[dt.datetime]` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**position_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unique_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.<a href="src/fern/devices/client.py">delete_a_device</a>(...)</code></summary>
<dl>
<dd>

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
client.devices.delete_a_device(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.<a href="src/fern/devices/client.py">update_total_distance_and_hours_of_the_device</a>(...)</code></summary>
<dl>
<dd>

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
client.devices.update_total_distance_and_hours_of_the_device(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**hours:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**total_distance:** `typing.Optional[float]` — in meters
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Drivers
<details><summary><code>client.drivers.<a href="src/fern/drivers/client.py">fetch_a_list_of_drivers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without params, it returns a list of Drivers the user has access to
</dd>
</dl>
</dd>
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
client.drivers.fetch_a_list_of_drivers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Standard users can use this only with _deviceId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Standard users can use this only with _groupId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drivers.<a href="src/fern/drivers/client.py">create_a_driver</a>(...)</code></summary>
<dl>
<dd>

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
client.drivers.create_a_driver()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[DriverAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unique_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drivers.<a href="src/fern/drivers/client.py">update_a_driver</a>(...)</code></summary>
<dl>
<dd>

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
client.drivers.update_a_driver(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[DriverAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unique_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drivers.<a href="src/fern/drivers/client.py">delete_a_driver</a>(...)</code></summary>
<dl>
<dd>

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
client.drivers.delete_a_driver(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.events.<a href="src/fern/events/client.py">get_events_id</a>(...)</code></summary>
<dl>
<dd>

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
client.events.get_events_id(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Geofences
<details><summary><code>client.geofences.<a href="src/fern/geofences/client.py">fetch_a_list_of_geofences</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without params, it returns a list of Geofences the user has access to
</dd>
</dl>
</dd>
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
client.geofences.fetch_a_list_of_geofences()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Standard users can use this only with _deviceId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Standard users can use this only with _groupId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.geofences.<a href="src/fern/geofences/client.py">create_a_geofence</a>(...)</code></summary>
<dl>
<dd>

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
client.geofences.create_a_geofence()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**area:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[GeofenceAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**calendar_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.geofences.<a href="src/fern/geofences/client.py">update_a_geofence</a>(...)</code></summary>
<dl>
<dd>

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
client.geofences.update_a_geofence(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**area:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[GeofenceAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**calendar_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.geofences.<a href="src/fern/geofences/client.py">delete_a_geofence</a>(...)</code></summary>
<dl>
<dd>

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
client.geofences.delete_a_geofence(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Groups
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">fetch_a_list_of_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without any params, returns a list of the Groups the user belongs to
</dd>
</dl>
</dd>
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
client.groups.fetch_a_list_of_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">create_a_group</a>(...)</code></summary>
<dl>
<dd>

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
client.groups.create_a_group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[GroupAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">update_a_group</a>(...)</code></summary>
<dl>
<dd>

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
client.groups.update_a_group(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[GroupAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_a_group</a>(...)</code></summary>
<dl>
<dd>

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
client.groups.delete_a_group(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Maintenance
<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">fetch_a_list_of_maintenance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without params, it returns a list of Maintenance the user has access to
</dd>
</dl>
</dd>
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
client.maintenance.fetch_a_list_of_maintenance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Standard users can use this only with _deviceId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Standard users can use this only with _groupId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">create_a_maintenance</a>(...)</code></summary>
<dl>
<dd>

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
client.maintenance.create_a_maintenance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[MaintenanceAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">update_a_maintenance</a>(...)</code></summary>
<dl>
<dd>

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
client.maintenance.update_a_maintenance(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[MaintenanceAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">delete_a_maintenance</a>(...)</code></summary>
<dl>
<dd>

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
client.maintenance.delete_a_maintenance(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">fetch_a_list_of_notifications</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Without params, it returns a list of Notifications the user has access to
</dd>
</dl>
</dd>
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
client.notifications.fetch_a_list_of_notifications()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Can only be used by admins or managers to fetch all entities
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Standard users can use this only with their own _userId_
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Standard users can use this only with _deviceId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Standard users can use this only with _groupId_s, they have access to
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">create_a_notification</a>(...)</code></summary>
<dl>
<dd>

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
client.notifications.create_a_notification()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**always:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[NotificationAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**calendar_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mail:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sms:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**web:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">send_test_notification_to_current_user_via_email_and_sms</a>()</code></summary>
<dl>
<dd>

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
client.notifications.send_test_notification_to_current_user_via_email_and_sms()

```
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

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">fetch_a_list_of_available_notification_types</a>()</code></summary>
<dl>
<dd>

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
client.notifications.fetch_a_list_of_available_notification_types()

```
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

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">update_a_notification</a>(...)</code></summary>
<dl>
<dd>

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
client.notifications.update_a_notification(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**always:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[NotificationAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**calendar_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mail:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sms:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**web:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">delete_a_notification</a>(...)</code></summary>
<dl>
<dd>

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
client.notifications.delete_a_notification(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permissions
<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">link_an_object_to_another_object</a>(...)</code></summary>
<dl>
<dd>

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
client.permissions.link_an_object_to_another_object()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_id:** `typing.Optional[int]` — Computed Attribute Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**calendar_id:** `typing.Optional[int]` — Calendar Id, can be second parameter only and only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Device Id, can be first parameter or second only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `typing.Optional[int]` — Driver Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**geofence_id:** `typing.Optional[int]` — Geofence Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Group Id, can be first parameter or second only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**managed_user_id:** `typing.Optional[int]` — User Id, can be second parameter only and only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**notification_id:** `typing.Optional[int]` — Notification Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — User Id, can be only first parameter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">unlink_an_object_from_another_object</a>(...)</code></summary>
<dl>
<dd>

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
client.permissions.unlink_an_object_from_another_object()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_id:** `typing.Optional[int]` — Computed Attribute Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**calendar_id:** `typing.Optional[int]` — Calendar Id, can be second parameter only and only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — Device Id, can be first parameter or second only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `typing.Optional[int]` — Driver Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**geofence_id:** `typing.Optional[int]` — Geofence Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Group Id, can be first parameter or second only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**managed_user_id:** `typing.Optional[int]` — User Id, can be second parameter only and only in combination with userId
    
</dd>
</dl>

<dl>
<dd>

**notification_id:** `typing.Optional[int]` — Notification Id, can be second parameter only
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — User Id, can be only first parameter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Positions
<details><summary><code>client.positions.<a href="src/fern/positions/client.py">fetches_a_list_of_positions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user's Devices. _from_ and _to_ fields are not required with _id_.
</dd>
</dl>
</dd>
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
client.positions.fetches_a_list_of_positions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `typing.Optional[int]` — _deviceId_ is optional, but requires the _from_ and _to_ parameters when used
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[dt.datetime]` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[dt.datetime]` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — To fetch one or more positions. Multiple params can be passed like `id=31&id=42`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reports
<details><summary><code>client.reports.<a href="src/fern/reports/client.py">fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

At least one _deviceId_ or one _groupId_ must be passed
</dd>
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
client.reports.fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
    from_=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**from_:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**to:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — % can be used to return events of all types
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

At least one _deviceId_ or one _groupId_ must be passed
</dd>
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
client.reports.fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
    from_=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**from_:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**to:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

At least one _deviceId_ or one _groupId_ must be passed
</dd>
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
client.reports.fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
    from_=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**from_:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**to:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

At least one _deviceId_ or one _groupId_ must be passed
</dd>
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
client.reports.fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
    from_=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**from_:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**to:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

At least one _deviceId_ or one _groupId_ must be passed
</dd>
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
client.reports.fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
    from_=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**from_:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**to:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Server
<details><summary><code>client.server.<a href="src/fern/server/client.py">fetch_server_information</a>()</code></summary>
<dl>
<dd>

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
client.server.fetch_server_information()

```
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

<details><summary><code>client.server.<a href="src/fern/server/client.py">update_server_information</a>(...)</code></summary>
<dl>
<dd>

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
client.server.update_server_information()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attributes:** `typing.Optional[ServerAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**bing_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinate_format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_readonly:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**force_settings:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**limit_commands:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**map_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**map_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**poi_layer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**readonly:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**registration:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**twelve_hour_format:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**zoom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Session
<details><summary><code>client.session.<a href="src/fern/session/client.py">fetch_session_information</a>(...)</code></summary>
<dl>
<dd>

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
client.session.fetch_session_information()

```
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
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.session.<a href="src/fern/session/client.py">create_a_new_session</a>(...)</code></summary>
<dl>
<dd>

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
client.session.create_a_new_session(
    email="email",
    password="password",
)

```
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
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.session.<a href="src/fern/session/client.py">close_the_session</a>()</code></summary>
<dl>
<dd>

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
client.session.close_the_session()

```
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

## Statistics
<details><summary><code>client.statistics.<a href="src/fern/statistics/client.py">fetch_server_statistics</a>(...)</code></summary>
<dl>
<dd>

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
client.statistics.fetch_server_statistics(
    from_=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**from_:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**to:** `dt.datetime` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">fetch_a_list_of_users</a>(...)</code></summary>
<dl>
<dd>

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
client.users.fetch_a_list_of_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Can only be used by admin or manager users
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">create_a_user</a>(...)</code></summary>
<dl>
<dd>

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
client.users.create_a_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**administrator:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[UserAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinate_format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**device_readonly:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expiration_time:** `typing.Optional[dt.datetime]` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**limit_commands:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**map_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**poi_layer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**readonly:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**twelve_hour_format:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**user_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**zoom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_a_user</a>(...)</code></summary>
<dl>
<dd>

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
client.users.update_a_user(
    id_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**administrator:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[UserAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**coordinate_format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**device_readonly:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expiration_time:** `typing.Optional[dt.datetime]` — in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**limit_commands:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**map_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**poi_layer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**readonly:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**twelve_hour_format:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**user_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**zoom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete_a_user</a>(...)</code></summary>
<dl>
<dd>

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
client.users.delete_a_user(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

