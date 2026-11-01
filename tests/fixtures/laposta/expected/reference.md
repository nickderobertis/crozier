# Reference
## Lists
<details><summary><code>client.lists.<a href="src/fern/lists/client.py">alle_lijsten_opvragen</a>() -> ListList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All lists in an array of list objects. The list objects have been ordered in an array with the name 'data'. No parameters need to be provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lists.alle_lijsten_opvragen()

```
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

<details><summary><code>client.lists.<a href="src/fern/lists/client.py">lijst_toevoegen</a>(...) -> ListEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If there is something wrong with the parameters provided, a code is displayed with an error message. You may use these in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lists.lijst_toevoegen(
    name="Nieuwsbrief",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name given to the list in question
    
</dd>
</dl>

<dl>
<dd>

**locked:** `typing.Optional[bool]` — If a list is locked, it cannot be changed by a user of the application. (true or false)
    
</dd>
</dl>

<dl>
<dd>

**remarks:** `typing.Optional[str]` — Potential remarks
    
</dd>
</dl>

<dl>
<dd>

**subscribe_notification_email:** `typing.Optional[str]` — Email address to which a notification will be sent upon a subscription
    
</dd>
</dl>

<dl>
<dd>

**unsubscribe_notification_email:** `typing.Optional[str]` — Email address to which a notification will be sent upon the cancelling of a subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/fern/lists/client.py">lijst_opvragen</a>(...) -> ListEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All information about a list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lists.lijst_opvragen(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/fern/lists/client.py">lijst_wijzigen</a>(...) -> ListEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You will only have to include the fields that need to be modified in the application. Fields that are not mentioned will keep their current value. As soon as a field is mentioned, it is checked and may therefore cause an error message. A code is displayed with this error message. You may use this code in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lists.lijst_wijzigen(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — A name for the list in question
    
</dd>
</dl>

<dl>
<dd>

**locked:** `typing.Optional[bool]` — If a list is locked, it cannot be changed by a user of the application. (true or false)
    
</dd>
</dl>

<dl>
<dd>

**remarks:** `typing.Optional[str]` — Potential remarks
    
</dd>
</dl>

<dl>
<dd>

**subscribe_notification_email:** `typing.Optional[str]` — Email address to which a notification will be sent upon a subscription
    
</dd>
</dl>

<dl>
<dd>

**unsubscribe_notification_email:** `typing.Optional[str]` — Email address to which a notification will be sent upon the cancelling of a subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/fern/lists/client.py">lijst_verwijderen</a>(...) -> ListEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This permanently deletes a list. If the list does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lists.lijst_verwijderen(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/fern/lists/client.py">lijst_synchroniseren_bulk</a>(...) -> SyncResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds, updates or unsubscribes multiple subscribers in one request. This endpoint is off by default: an account without access gets a 401 with the message "Not permitted to issue bulk requests (1)". Contact Laposta to have it enabled for your account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lists.lijst_synchroniseren_bulk(
    list_id="BaImMu3JZA",
    actions="string",
    members={
        "key": "value"
    },
    member_id="ZKfjhLJHfl",
    email="relatie@example.net",
    custom_fields={
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

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `str` — An array with at least one of the following options: add, update, or unsubscribe_excluded. These determine whether members may be added, updated and/or unsubscribed (read details below).
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.Dict[str, typing.Any]` — An array with member objects. A minimum of 1, maximum of 500,000.
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — The id of the subscriber, or simply their email address. Both work.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email address of the relation to be changed or added. If the member_id is also specified, then a new email address can be specified here for the existing relation.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Dict[str, typing.Any]` — A JSON object where the key is the name of the extra field and the value is the value of the extra field.
    
</dd>
</dl>

<dl>
<dd>

**mode_verouderd:** `typing.Optional[str]` — For backwards compatibility you can still pass edit, add or add_and_edit, but this parameter is being phased out. Do not send mode together with actions.
    
</dd>
</dl>

<dl>
<dd>

**source_url:** `typing.Optional[str]` — The URL from which the relation was registered.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/fern/lists/client.py">lijst_leegmaken</a>(...) -> ListEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This permanently purges all active subscribers from a list, but doesn't delete the list itself. If the list does not exist, an error message is displayed. In response, you are shown another list object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lists.lijst_leegmaken(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Fields
<details><summary><code>client.fields.<a href="src/fern/fields/client.py">alle_velden_opvragen</a>(...) -> FieldList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All fields of a list in an array of field objects. The field objects are formatted in an array named 'data'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fields.alle_velden_opvragen(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fields.<a href="src/fern/fields/client.py">veld_toevoegen</a>(...) -> FieldEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.fields import VeldToevoegenRequestDatatype

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fields.veld_toevoegen(
    list_id="BaImMu3JZA",
    name="Nieuwsbrief",
    datatype=VeldToevoegenRequestDatatype.TEXT,
    required=True,
    in_form=True,
    in_list=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — A name for this field
    
</dd>
</dl>

<dl>
<dd>

**datatype:** `VeldToevoegenRequestDatatype` — The data type: text, numeric, date, select_single or select_multiple
    
</dd>
</dl>

<dl>
<dd>

**required:** `bool` — Is this a mandatory field?
    
</dd>
</dl>

<dl>
<dd>

**in_form:** `bool` — Does this field occur in the subscription form? (boolean)
    
</dd>
</dl>

<dl>
<dd>

**in_list:** `bool` — Is this field visible in Laposta's overview? (boolean)
    
</dd>
</dl>

<dl>
<dd>

**defaultvalue:** `typing.Optional[str]` — A potential default value
    
</dd>
</dl>

<dl>
<dd>

**datatype_display:** `typing.Optional[VeldToevoegenRequestDatatypeDisplay]` — Only applicable for select_single: the desired display (select, radio)
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.List[typing.Any]]` — What selection options are available? (mandatory for the data types select_single of select_multiple). The options can be given as an array. In the answer the options are repeated, but there is also an extra field options_full. Also listed are the option IDs, which may eventually be used to change the options later.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fields.<a href="src/fern/fields/client.py">veld_opvragen</a>(...) -> FieldEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All information about a field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fields.veld_opvragen(
    field_id="Z87ysHha9A",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_id:** `str` — The id of the field. You find it in the response of [Get all fields](/velden/alle-velden-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fields.<a href="src/fern/fields/client.py">veld_wijzigen</a>(...) -> FieldEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You will only have to include the parts that need to be modified. Parts that are not mentioned will keep their current values. As soon as a part is mentioned it does get checked, and thus can cause an error message. This error message contains a code with a message. See above under 'Error messages' what these codes stand for. Pass options_full as a complete replacement for the option list. The key of each entry determines the operation: You may also pass options_full as an array of {"id", "value"} objects — the same shape as the response. The API will handle both formats.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fields.veld_wijzigen(
    field_id="field_id",
    list_id="BaImMu3JZA",
    required=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**required:** `bool` — Is this a mandatory field?
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — A name for this field
    
</dd>
</dl>

<dl>
<dd>

**datatype:** `typing.Optional[VeldWijzigenRequestDatatype]` — The data type of this field (text, numeric, date, select_single, select_multiple)
    
</dd>
</dl>

<dl>
<dd>

**datatype_display:** `typing.Optional[VeldWijzigenRequestDatatypeDisplay]` — Only applicable for select_single: the desired display (select, radio)
    
</dd>
</dl>

<dl>
<dd>

**options_full:** `typing.Optional[typing.List[typing.Any]]` — The full set of options for a select_single or select_multiple field, as a key/value map of id → label. The key controls what happens to each option: Existing numeric ID (e.g. "2") — keeps or modifies the option. Changing the label updates it in-place; the ID stays the same, so existing member data is preserved. Non-numeric key (e.g. "new-0") — adds a new option; a fresh ID is assigned automatically. Omitting an existing ID — deletes that option. Always include every option you want to keep. Must be sent as JSON. Alternative format: instead of a key/value map you may also pass an array of objects in the same shape as the response: [{"id": "1", "value": "Red"}, {"id": "new-0", "value": "Orange"}]. The API will normalise this automatically.
    
</dd>
</dl>

<dl>
<dd>

**defaultvalue:** `typing.Optional[str]` — The default value (will be used in the absence of this field)
    
</dd>
</dl>

<dl>
<dd>

**in_form:** `typing.Optional[bool]` — Does this field occur in the subscription form? (boolean)
    
</dd>
</dl>

<dl>
<dd>

**in_list:** `typing.Optional[bool]` — Is this field visible in Laposta's overview? (boolean)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fields.<a href="src/fern/fields/client.py">veld_verwijderen</a>(...) -> FieldEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This permanently deletes a field. If the field does not exist, an error message is displayed. In response you are shown another field object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fields.veld_verwijderen(
    field_id="Z87ysHha9A",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_id:** `str` — The id of the field. You find it in the response of [Get all fields](/velden/alle-velden-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Segments
<details><summary><code>client.segments.<a href="src/fern/segments/client.py">alle_segmenten_opvragen</a>(...) -> SegmentList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All segments of a list in an array of segment objects. The segment objects are included in an array named 'data'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.segments.alle_segmenten_opvragen(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.segments.<a href="src/fern/segments/client.py">segment_toevoegen</a>(...) -> SegmentEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If there is something wrong with the provided parameters, an error code and message will be displayed. See above under Error Messages for what the codes mean.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.segments.segment_toevoegen(
    list_id="BaImMu3JZA",
    name="Nieuwsbrief",
    definition="{\"blocks\":[{\"rules\":[{\"input\":{\"subject\":\"woonplaats\",\"comparator\":\"equal\",\"multi\":\"\",\"text\":\"Utrecht\"},\"type\":\"members\"}]}]}",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the segment
    
</dd>
</dl>

<dl>
<dd>

**definition:** `str` — The segment definition as JSON text. Note that a field name that does not exist is accepted and produces a segment that matches nobody.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.segments.<a href="src/fern/segments/client.py">segment_opvragen</a>(...) -> SegmentEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All information about a segment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.segments.segment_opvragen(
    segment_id="pDrp5KOD0z",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**segment_id:** `str` — The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.segments.<a href="src/fern/segments/client.py">segment_wijzigen</a>(...) -> SegmentEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You only need to include the fields that need to be changed in the request. Fields that are not mentioned retain their current value. Once a field is mentioned, it is checked and can therefore cause an error message. This error message will include a code and a message. See above under Error Messages for what the codes mean.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.segments.segment_wijzigen(
    segment_id="pDrp5KOD0z",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**segment_id:** `str` — The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the segment
    
</dd>
</dl>

<dl>
<dd>

**definition:** `typing.Optional[str]` — The definition of the segment (string in JSON format)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.segments.<a href="src/fern/segments/client.py">segment_verwijderen</a>(...) -> SegmentEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This permanently deletes a segment. After this, the segment cannot be retrieved again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.segments.segment_verwijderen(
    segment_id="pDrp5KOD0z",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**segment_id:** `str` — The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscribers
<details><summary><code>client.subscribers.<a href="src/fern/subscribers/client.py">alle_relaties_opvragen</a>(...) -> MemberList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All fields of a list in an array of member objects. The member objects are formatted in an array named 'data'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscribers.alle_relaties_opvragen(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[AlleRelatiesOpvragenRequestState]` — The status of the requested subscribers: active, unsubscribed or cleaned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscribers.<a href="src/fern/subscribers/client.py">relatie_toevoegen</a>(...) -> MemberEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If there is something wrong with the parameters provided, a code is displayed with an error message. You can use this in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscribers.relatie_toevoegen(
    list_id="BaImMu3JZA",
    ip="198.51.100.10",
    email="relatie@example.net",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` — The IP address the sign-up came from. For a form on your site that is the visitor address, not your server address.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email address of the subscriber to be added
    
</dd>
</dl>

<dl>
<dd>

**source_url:** `typing.Optional[str]` — The URL from which the subscriber is registered
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Dict[str, typing.Any]]` — The values of the extra fields. The name (key) of the field is the 'custom_name' (part of the Field object). This is the same as the 'Variable' in the application. You pass labels as an array, with square brackets: custom_fields[labels][]=Klant. Without those brackets the call still succeeds but nothing changes, and a label that the list does not have returns error code 203.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.List[typing.Any]]` — Additional instructions, with possibilities being: upsert: true to overwrite fields if the email address is already linked to an active contact in this list. Normally, you would receive an error if the email address is already linked to an active contact. Note: If a subscriber is unsubscribed and you perform an upsert with that email address, it will be set to active again. If you want to prevent an unsubscribed subscriber from being reactivated, you can use the suppress_reactivation option. suppress_reactivation: true to prevent an unsubscribed subscriber from being reactivated during an upsert suppress_email_notification: true to prevent a notification email from being sent every time someone logs in via an API ignore_doubleoptin: true to instantly activate subscribers on a double-optin list and ensure that no confirmation email is sent when signing up through the API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscribers.<a href="src/fern/subscribers/client.py">relatie_opvragen</a>(...) -> MemberEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All information about a subscriber in a member object
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscribers.relatie_opvragen(
    member_id="ZKfjhLJHfl",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `str` — The id of the subscriber, or simply their email address. Both work.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscribers.<a href="src/fern/subscribers/client.py">relatie_wijzigen</a>(...) -> MemberEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You only have to include the fields that need to be modified in the request. Fields that are not named will keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscribers.relatie_wijzigen(
    member_id="member_id",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email address of the subscriber that must be modified
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[RelatieWijzigenRequestState]` — The new status of the subscriber: active or unsubscribed
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Dict[str, typing.Any]]` — The values of the extra created fields. You pass labels as an array, with square brackets: custom_fields[labels][]=Klant. Only labels the list already has are accepted; you create new labels in the application or during an import.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscribers.<a href="src/fern/subscribers/client.py">relatie_verwijderen</a>(...) -> MemberEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This permanently deletes a subscriber. If the subscriber does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the subscriber.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscribers.relatie_verwijderen(
    member_id="ZKfjhLJHfl",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `str` — The id of the subscriber, or simply their email address. Both work.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscribers.<a href="src/fern/subscribers/client.py">relatiegeschiedenis_opvragen</a>(...) -> History</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The full event history of a subscriber, similar to the details shown in the application.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subscribers.relatiegeschiedenis_opvragen(
    member_id="ZKfjhLJHfl",
    list_id="BaImMu3JZA",
    campaign_id="njhgaf61ye",
    event_date_from="2026-04-01 00:00:00",
    event_date_to="2026-05-01 00:00:00",
    cursor="opaque_cursor_value",
    order_by="event_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `str` — The id of the subscriber, or simply their email address. Both work.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**event_date_from:** `typing.Optional[str]` — Only return events from this date and time, inclusive. Use the regular format or ISO format described above.
    
</dd>
</dl>

<dl>
<dd>

**event_date_to:** `typing.Optional[str]` — Only return events before this date and time, exclusive. Use the regular format or ISO format described above.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of history items to return. Default is 100, maximum is 1000
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor from pagination.next_cursor to request the next page. Do not interpret this value yourself; send it back unchanged.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order by. Currently only event_date is supported
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[RelatiegeschiedenisOpvragenRequestOrder]` — Sort direction: desc or asc. Default is desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">alle_webhooks_opvragen</a>(...) -> WebhookList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All webhooks of a list in an array of member objects. The webhook objects are formatted in an array named 'data'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.alle_webhooks_opvragen(
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">webhook_toevoegen</a>(...) -> WebhookEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.webhooks import WebhookToevoegenRequestEvent

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.webhook_toevoegen(
    list_id="BaImMu3JZA",
    event=WebhookToevoegenRequestEvent.SUBSCRIBED,
    url="https://example.net/laposta-webhook",
    blocked=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**event:** `WebhookToevoegenRequestEvent` — When will the webhook be requested? (subscribed, modified of deactivated)
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL to be accessed
    
</dd>
</dl>

<dl>
<dd>

**blocked:** `bool` — Is the accessing of the webhook (temporarily) blocked? (true or false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">webhook_opvragen</a>(...) -> WebhookEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All information about a webhook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.webhook_opvragen(
    webhook_id="k5RaJhbnLa",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">webhook_wijzigen</a>(...) -> WebhookEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If there is something wrong with the parameters provided, a code is displayed with an error message. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.webhook_wijzigen(
    webhook_id="k5RaJhbnLa",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[WebhookWijzigenRequestEvent]` — When will the webhook be requested? (subscribed, modified or deactivated)
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL to be accessed
    
</dd>
</dl>

<dl>
<dd>

**blocked:** `typing.Optional[bool]` — Is the accessing of the webhook (temporarily) blocked? (true or false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">webhook_verwijderen</a>(...) -> WebhookEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This permanently deletes a webhook. Potentially outstanding requests from the webhook will still be completed. If the field does not exist, an error message is displayed. In response you are shown another webhook object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the webhook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.webhook_verwijderen(
    webhook_id="k5RaJhbnLa",
    list_id="BaImMu3JZA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Campaigns
<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">alle_campagnes_opvragen</a>() -> CampaignList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All campaigns in an array of campaign objects. The campaign objects have been ordered in an array with the name 'data'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.alle_campagnes_opvragen()

```
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

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_aanmaken</a>(...) -> CampaignEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a campaign. A campaign you create through the API can be filled with `/content` afterwards; campaigns built in the drag-and-drop editor cannot.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_aanmaken(
    type="regular",
    name="Nieuwsbrief",
    subject="De nieuwsbrief van maart",
    from_name="Voorbeeld BV",
    from_email="nieuwsbrief@example.net",
    list_ids={
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

**type:** `str` — Type of campaign (must be set to: regular)
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — A name for this campaign for internal use
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject line
    
</dd>
</dl>

<dl>
<dd>

**from_name:** `str` — The name of the sender
    
</dd>
</dl>

<dl>
<dd>

**from_email:** `str` — The email address of the sender (must be a sender address approved within the program)
    
</dd>
</dl>

<dl>
<dd>

**list_ids:** `typing.Dict[str, typing.Any]` — Recipients, array of list_ids and segment_ids if needed
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Email address for receiving replies
    
</dd>
</dl>

<dl>
<dd>

**stats_ga:** `typing.Optional[str]` — Link Google Analytics (true or false)
    
</dd>
</dl>

<dl>
<dd>

**stats_mtrack:** `typing.Optional[str]` — Link Mtrack (true or false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_opvragen</a>(...) -> CampaignEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All information about a campaign
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_opvragen(
    campaign_id="njhgaf61ye",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_wijzigen</a>(...) -> CampaignEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You only have to submit the fields that require to be modified in the application. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_wijzigen(
    campaign_id="njhgaf61ye",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — A name for this campaign for internal use
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject line
    
</dd>
</dl>

<dl>
<dd>

**from_name:** `typing.Optional[str]` — The name of the sender
    
</dd>
</dl>

<dl>
<dd>

**from_email:** `typing.Optional[str]` — The email address of the sender (must be a sender address approved within the program)
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Email address for receiving replies
    
</dd>
</dl>

<dl>
<dd>

**list_ids:** `typing.Optional[typing.Dict[str, typing.Any]]` — Recipients, array of list_ids and segment_ids if needed
    
</dd>
</dl>

<dl>
<dd>

**stats_ga:** `typing.Optional[str]` — Link Google Analytics (true or false)
    
</dd>
</dl>

<dl>
<dd>

**stats_mtrack:** `typing.Optional[str]` — Link Mtrack (true or false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_verwijderen</a>(...) -> CampaignEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This deletes a campaign. Unsent campaigns will be permanently deleted. Campaigns that have been sent are permanently deleted only after 180 days. In the meantime, they can be restored in the overview of campaigns in our program. In response you are shown another campaign object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_verwijderen(
    campaign_id="njhgaf61ye",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_content_opvragen</a>(...) -> CampaignContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requesting the content of a campaign. Please note that this is only possible if it involves a campaign that has been exported, and not for a campaign created within the application using the drag & drop editor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_content_opvragen(
    campaign_id="njhgaf61ye",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_content_vullen</a>(...) -> CampaignContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filling in the content of a campaign The campaign can either be filled directly with html, or through a URL, in which case Laposta imports the html found at the specified URL. One of the two must be chosen. If both parameters are given the html is taken. If the import fails, a 400 error message from the API will occur. If it does succeed in importing the html, but problems were found during the import, they are shown in the variable report in the response. These may include: Solving these problems is not necessary in order to properly send the newsletter, but it is highly recommended. In the case of a free account, our advertising is added to the bottom of the newsletter. If the offered html does not contain an unsubscribe link, it will simply be added by our program.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_content_vullen(
    campaign_id="njhgaf61ye",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**html:** `typing.Optional[str]` — The html for the campaign
    
</dd>
</dl>

<dl>
<dd>

**import_url:** `typing.Optional[str]` — The URL from which the html must be imported
    
</dd>
</dl>

<dl>
<dd>

**inline_css:** `typing.Optional[bool]` — Potential inlining of css (true or false)
    
</dd>
</dl>

<dl>
<dd>

**javascript:** `typing.Optional[str]` — JavaScript was encountered
    
</dd>
</dl>

<dl>
<dd>

**flash:** `typing.Optional[str]` — Flash was encountered
    
</dd>
</dl>

<dl>
<dd>

**no_unsubscribe:** `typing.Optional[str]` — No unsubscribe could be located
    
</dd>
</dl>

<dl>
<dd>

**empty_unsubscribe:** `typing.Optional[str]` — Empty unsubscribe encountered
    
</dd>
</dl>

<dl>
<dd>

**css:** `typing.Optional[str]` — Missing external css files (listed)
    
</dd>
</dl>

<dl>
<dd>

**images:** `typing.Optional[str]` — Missing external images (listed)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_testen</a>(...) -> CampaignEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sending a test mail Note: only in the case of a campaign for which there already is content, but which has not yet been sent, is it possible for a test email to be sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_testen(
    campaign_id="njhgaf61ye",
    email="relatie@example.net",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email address to which the test should be sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_inplannen</a>(...) -> CampaignEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedules the campaign for a moment in the future. You cancel a scheduled campaign by deleting it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_inplannen(
    campaign_id="njhgaf61ye",
    delivery_requested="2026-05-18 14:30:00",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**delivery_requested:** `str` — The time and date of sending. Use the regular format or ISO format described above.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagne_verzenden</a>(...) -> CampaignEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends the campaign to all connected lists and segments right away. This call cannot be undone, and it is not blocked when the campaign was already sent: a second call starts delivery again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagne_verzenden(
    campaign_id="njhgaf61ye",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/fern/campaigns/client.py">campagnegeschiedenis_opvragen</a>(...) -> History</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The full event history of a campaign. A campaign can contain many events; use pagination to retrieve additional pages.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.campaigns.campagnegeschiedenis_opvragen(
    campaign_id="njhgaf61ye",
    event_date_from="2026-04-01 00:00:00",
    event_date_to="2026-05-01 00:00:00",
    cursor="opaque_cursor_value",
    order_by="event_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**event_date_from:** `typing.Optional[str]` — Only return events from this date and time, inclusive. Use the regular format or ISO format described above.
    
</dd>
</dl>

<dl>
<dd>

**event_date_to:** `typing.Optional[str]` — Only return events before this date and time, exclusive. Use the regular format or ISO format described above.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of history items to return. Default is 100, maximum is 1000
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor from pagination.next_cursor to request the next page. Do not interpret this value yourself; send it back unchanged.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order by. Currently only event_date is supported
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[CampagnegeschiedenisOpvragenRequestOrder]` — Sort direction: desc or asc. Default is desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Results
<details><summary><code>client.results.<a href="src/fern/results/client.py">campagneresultaten_opvragen</a>(...) -> ReportEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The results of a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.results.campagneresultaten_opvragen(
    campaign_id="njhgaf61ye",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.results.<a href="src/fern/results/client.py">alle_resultaten_opvragen</a>() -> ReportList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The results of all campaigns in an array of list objects. The report objects have been ordered in an array with the name 'data'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<username>",
    leave_empty="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.results.alle_resultaten_opvragen()

```
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

