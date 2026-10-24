# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_all_messages_of_all_circuits</a>(...) -> Data</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_all_messages_of_all_circuits(
    since=1493483370,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `typing.Optional[Seconds]` — limit to messages that have changed since the specified UTC seconds.
    
</dd>
</dl>

<dl>
<dd>

**poll:** `typing.Optional[int]` — set the poll priority of matching message(s) to prio.
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — include comments and field units.
    
</dd>
</dl>

<dl>
<dd>

**indexed:** `typing.Optional[bool]` — always return field indexes instead of names.
    
</dd>
</dl>

<dl>
<dd>

**numeric:** `typing.Optional[bool]` — return numeric values of value list entries.
    
</dd>
</dl>

<dl>
<dd>

**valuename:** `typing.Optional[bool]` — include value and name for named values.
    
</dd>
</dl>

<dl>
<dd>

**full:** `typing.Optional[bool]` — include all available attributes.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[bool]` — retrieve the data from the bus if not yet cached.
    
</dd>
</dl>

<dl>
<dd>

**write:** `typing.Optional[bool]` — retrieve write messages in addition to read/poll messages.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — include raw master/slave data.
    
</dd>
</dl>

<dl>
<dd>

**def:** `typing.Optional[bool]` — include message and field definition.
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — authenticate with user name.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — authenticate with user secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_all_messages_of_a_particular_circuit</a>(...) -> Data</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_all_messages_of_a_particular_circuit(
    circuit="circuit",
    since=1493483370,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**circuit:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[Seconds]` — limit to messages that have changed since the specified UTC seconds.
    
</dd>
</dl>

<dl>
<dd>

**poll:** `typing.Optional[int]` — set the poll priority of matching message(s) to prio.
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[bool]` — exact search for circuit/message name.
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — include comments and field units.
    
</dd>
</dl>

<dl>
<dd>

**indexed:** `typing.Optional[bool]` — always return field indexes instead of names.
    
</dd>
</dl>

<dl>
<dd>

**numeric:** `typing.Optional[bool]` — return numeric values of value list entries.
    
</dd>
</dl>

<dl>
<dd>

**valuename:** `typing.Optional[bool]` — include value and name for named values.
    
</dd>
</dl>

<dl>
<dd>

**full:** `typing.Optional[bool]` — include all available attributes.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[bool]` — retrieve the data from the bus if not yet cached.
    
</dd>
</dl>

<dl>
<dd>

**write:** `typing.Optional[bool]` — retrieve write messages in addition to read/poll messages.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — include raw master/slave data.
    
</dd>
</dl>

<dl>
<dd>

**def:** `typing.Optional[bool]` — include message and field definition.
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — authenticate with user name.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — authenticate with user secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_a_particular_message_of_a_particular_circuit</a>(...) -> Data</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_a_particular_message_of_a_particular_circuit(
    circuit="circuit",
    message="message",
    since=1493483370,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**circuit:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[Seconds]` — limit to messages that have changed since the specified UTC seconds.
    
</dd>
</dl>

<dl>
<dd>

**poll:** `typing.Optional[int]` — set the poll priority of matching message(s) to prio.
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[bool]` — exact search for circuit/message name.
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — include comments and field units.
    
</dd>
</dl>

<dl>
<dd>

**indexed:** `typing.Optional[bool]` — always return field indexes instead of names.
    
</dd>
</dl>

<dl>
<dd>

**numeric:** `typing.Optional[bool]` — return numeric values of value list entries.
    
</dd>
</dl>

<dl>
<dd>

**valuename:** `typing.Optional[bool]` — include value and name for named values.
    
</dd>
</dl>

<dl>
<dd>

**full:** `typing.Optional[bool]` — include all available attributes.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[bool]` — retrieve the data from the bus if not yet cached.
    
</dd>
</dl>

<dl>
<dd>

**write:** `typing.Optional[bool]` — retrieve write messages in addition to read/poll messages.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — include raw master/slave data.
    
</dd>
</dl>

<dl>
<dd>

**def:** `typing.Optional[bool]` — include message and field definition.
    
</dd>
</dl>

<dl>
<dd>

**define:** `typing.Optional[str]` — update/replace a message definition.
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — authenticate with user name.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — authenticate with user secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_all_known_field_data_types</a>() -> DataTypes</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_all_known_field_data_types()

```
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

<details><summary><code>client.<a href="src/fern/client.py">get_all_known_field_templates_for_the_root</a>() -> Templates</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_all_known_field_templates_for_the_root()

```
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

<details><summary><code>client.<a href="src/fern/client.py">get_all_known_field_templates_for_the_path</a>(...) -> Templates</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_all_known_field_templates_for_the_path(
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">retrieve_raw_data_from_grabbed_and_or_decoded_messages</a>(...) -> RawMessages</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.retrieve_raw_data_from_grabbed_and_or_decoded_messages(
    since=1493483370,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `typing.Optional[Seconds]` — limit to messages that have changed since the specified UTC seconds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">decode_raw_data_with_the_specified_field_defintion</a>(...) -> typing.Optional[FieldValue]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.decode_raw_data_with_the_specified_field_defintion(
    def_="def",
    raw="raw",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**def:** `str` — the field definition (starting with type).
    
</dd>
</dl>

<dl>
<dd>

**raw:** `str` — the raw symbols to decode as hex sequence.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">retrieve_a_particular_file</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.retrieve_a_particular_file(
    file="file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `str` — the file to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

