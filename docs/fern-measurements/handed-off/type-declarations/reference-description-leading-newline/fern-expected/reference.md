# Reference
<details><summary><code>client.<a href="src/fern/client.py">deposit_packet</a>(...) -> Packet</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.deposit_packet(
    variety="variety",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**variety:** `str` — 
The variety's common name.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 


Key-value labels kept with the packet. Keys are short words.

Values are free text of at most 64 characters.
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[str]` 


        Where the seed was saved.
        (ex. a garden name)
        
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">add_packet_note</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TextNote

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.add_packet_note(
    packet_id="packetId",
    request=TextNote(
        text="text",
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

**packet_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PacketNoteCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

