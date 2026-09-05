# Reference
## Events
<details><summary><code>client.events.<a href="src/fern/events/client.py">get_events_v3events_get_page</a>(...) -> CollectionResponseExternalUnifiedEvent</code></summary>
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
    token="<token>",
    private_app_legacy="<private-app-legacy>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.get_events_v3events_get_page()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**occurred_after:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**occurred_before:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**index_table_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**index_specific_metadata:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to display per page.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**object_property_propname:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**property_propname:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

